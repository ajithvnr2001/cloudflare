---
url: https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/
title: Lifecycle of a Durable Object \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:07.627499+00:00
---

# Lifecycle of a Durable Object · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Concepts
  4. /Lifecycle of a Durable Object



# Lifecycle of a Durable Object

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDurable Object Lifecycle state transitionsShutdown behavior Code updates Working without shutdown hooks

This section describes the lifecycle of a [Durable Object](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/).

To use a Durable Object you need to create a [Durable Object Stub](https://developers.cloudflare.com/durable-objects/api/stub/). Simply creating the Durable Object Stub does not send a request to the Durable Object, and therefore the Durable Object is not yet instantiated. A request is sent to the Durable Object and its lifecycle begins only once a method is invoked on the Durable Object Stub.
    
    
    const stub = env.MY_DURABLE_OBJECT.getByName("foo");
    // Now the request is sent to the remote Durable Object.
    const rpcResponse = await stub.sayHello();

## Durable Object Lifecycle state transitions

A Durable Object can be in one of the following states at any moment:

State | Description  
---|---  
**Active, in-memory** | The Durable Object runs, in memory, and handles incoming requests.  
**Idle, in-memory non-hibernateable** | The Durable Object waits for the next incoming request/event, but does not satisfy the criteria for hibernation.  
**Idle, in-memory hibernateable** | The Durable Object waits for the next incoming request/event and satisfies the criteria for hibernation. It is up to the runtime to decide when to hibernate the Durable Object. Currently, it is after 10 seconds of inactivity while in this state.  
**Hibernated** | The Durable Object is removed from memory. Hibernated WebSocket connections stay connected.  
**Inactive** | The Durable Object is completely removed from the host process and might need to cold start. This is the initial state of all Durable Objects.  
  
This is how a Durable Object transitions among these states (each state is in a rounded rectangle).

![Lifecycle of a Durable Object](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2866,height=2276,format=webp/_astro/durable-object-lifecycle.DdQka9ef.png)

Assuming a Durable Object does not run, the first incoming request or event (like an alarm) will execute the `constructor()` of the Durable Object class, then run the corresponding function invoked.

At this point the Durable Object is in the **active in-memory state**.

Once all incoming requests or events have been processed, the Durable Object remains idle in-memory for a few seconds either in a hibernateable state or in a non-hibernateable state.

Hibernation can only occur if **all** of the conditions below are true:

  * No `setTimeout`/`setInterval` scheduled callbacks are set, since there would be no way to recreate the callback after hibernating.
  * No I/O operation or promise passed to `this.ctx.waitUntil()` remains unfinished, and no outbound connection remains open.
  * No WebSocket standard API is used.
  * No request/event is still being processed, because hibernating would mean losing track of the async function which is eventually supposed to return a response to that request.



After 10 seconds of no incoming request or event, and all the above conditions satisfied, the Durable Object will transition into the **hibernated** state.

Caution

When hibernated, the in-memory state is discarded, so ensure you persist all important information in the Durable Object's storage.

If any of the above conditions is false, the Durable Object remains in-memory, in the **idle, in-memory, non-hibernateable** state.

In case of an incoming request or event while in the **hibernated** state, the `constructor()` will run again, and the Durable Object will transition to the **active, in-memory** state and execute the invoked function.

While in the **idle, in-memory, non-hibernateable** state, after 70-140 seconds of inactivity (no incoming requests or events), the Durable Object will be evicted entirely from memory and potentially from the Cloudflare host and transition to the **inactive** state.

Pending operations prevent eviction

Pending I/O and open outbound connections prevent a Durable Object from being evicted. Examples include service binding requests, Durable Object remote procedure call (RPC) calls, outbound `fetch()` requests, [`this.ctx.container.monitor()`](https://developers.cloudflare.com/containers/api/durable-object-container/#monitor), promises passed to `this.ctx.waitUntil()`, and pending `setTimeout()` and `setInterval()` timers. TCP sockets and outbound WebSockets also prevent eviction.

Each operation prevents eviction until it completes or for up to 15 minutes from when it starts, whichever comes first. Operations started together do not combine their windows. Starting another operation later can extend the Durable Object's time in memory. The limit applies to each operation, not to the total time in memory.

While an operation prevents eviction, the Durable Object continues to [incur duration charges](https://developers.cloudflare.com/durable-objects/platform/pricing/#when-does-a-durable-object-incur-duration-charges). When no operation prevents eviction, the standard eviction rules resume.

Objects in the **hibernated** state keep their Websocket clients connected, and the runtime decides if and when to transition the object to the **inactive** state (for example deciding to move the object to a different host) thus restarting the lifecycle.

The next incoming request or event starts the cycle again.

Lifecycle states incurring duration charges

A Durable Object incurs charges only when it is **actively running in-memory** , or when it is **idle in-memory and non-hibernateable** (indicated as green rectangles in the diagram).

## Shutdown behavior

Durable Objects will occasionally shut down and objects are restarted, which will run your Durable Object class constructor. This can happen for various reasons, including:

  * New Worker [deployments](https://developers.cloudflare.com/workers/versions-and-deployments/) with code updates
  * Lack of requests to an object following the state transitions documented above
  * Cloudflare updates to the Workers runtime system
  * Workers runtime decisions on where to host objects



When a Durable Object is shut down, the object instance is automatically restarted and new requests are routed to the new instance. In-flight requests are handled as follows:

  * **HTTP & RPC requests**: In-flight requests are allowed to finish if they do not access a Durable Object's storage. If a request attempts to access a Durable Object's storage, it will be stopped immediately and return an error to maintain Durable Objects global uniqueness property. When the Worker runtime system is being updated, in-flight requests have up to 30 seconds to complete.
  * **WebSocket connections** : WebSocket requests are terminated automatically during shutdown. This is so that the new instance can take over the connection as soon as possible.
  * **Other invocations (email, cron)** : Other invocations are treated similarly to HTTP requests.



It is important to ensure that any services using Durable Objects are designed to handle the possibility of a Durable Object being shut down.

### Code updates

When your Durable Object code is updated, your Worker and Durable Objects are released globally in an eventually consistent manner. This will cause a Durable Object to shut down, with the behavior described above. Updates can also create a situation where a request reaches a new version of your Worker in one location, and calls to a Durable Object still running a previous version elsewhere. Refer to [Code updates](https://developers.cloudflare.com/durable-objects/platform/known-issues/#code-updates) for more information about handling this scenario.

### Working without shutdown hooks

Durable Objects may shut down at any time due to deployments, inactivity, or runtime decisions. Rather than relying on shutdown hooks (which are not provided), design your application to write state incrementally.

Shutdown hooks or lifecycle callbacks that run before shutdown are not provided because Cloudflare cannot guarantee these hooks would execute in all cases, and external software may rely too heavily on these (unreliable) hooks.

Instead of relying on shutdown hooks, you can regularly write to storage to recover gracefully from shutdowns.

For example, if you are processing a stream of data and need to save your progress, write your position to storage as you go rather than waiting to persist it at the end:
    
    
    // Good: Write progress as you go
    async processData(data) {
      data.forEach(async (item, index) => {
        await this.processItem(item);
        // Save progress frequently
        await this.ctx.storage.put("lastProcessedIndex", index);
      });
    }

While this may feel unintuitive, Durable Object storage writes are fast and synchronous, so you can persist state with minimal performance concerns.

This approach ensures your Durable Object can safely resume from any point, even if it shuts down unexpectedly.

[PreviousWhat are Durable Objects?](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/)[NextRules of Durable Objects](https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/concepts/durable-object-lifecycle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
