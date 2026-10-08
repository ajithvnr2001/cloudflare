---
url: https://developers.cloudflare.com/durable-objects/api/stub/
title: Durable Object Stub \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:06.390785+00:00
---

# Durable Object Stub · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/api/stub/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Workers Binding API
  4. /Durable Object Stub



# Durable Object Stub

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/api/stub/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDescriptionProperties id nameRelated resources

## Description

The `DurableObjectStub` interface is a client used to invoke methods on a remote Durable Object. The type of `DurableObjectStub` is generic to allow for RPC methods to be invoked on the stub.

Durable Objects implement E-order semantics, a concept deriving from the [E distributed programming language ↗︎](https://en.wikipedia.org/wiki/E_\(programming_language\)). When you make multiple calls to the same Durable Object, it is guaranteed that the calls will be delivered to the remote Durable Object in the order in which you made them. E-order semantics makes many distributed programming problems easier. E-order is implemented by the [Cap'n Proto ↗︎](https://capnproto.org) distributed object-capability RPC protocol, which Cloudflare Workers uses for internal communications.

If an exception is thrown by a Durable Object stub all in-flight calls and future calls will fail with [exceptions](https://developers.cloudflare.com/durable-objects/observability/troubleshooting/). To continue invoking methods on a remote Durable Object a Worker must recreate the stub. There are no ordering guarantees between different stubs.
    
    
    import { DurableObject } from "cloudflare:workers";
    
    // Durable Object
    export class MyDurableObject extends DurableObject {
    	constructor(ctx, env) {
    		super(ctx, env);
    	}
    
    	async sayHello() {
    		return "Hello, World!";
    	}
    }
    
    // Worker
    export default {
    	async fetch(request, env) {
    		// A stub is a client used to invoke methods on the Durable Object
    		const stub = env.MY_DURABLE_OBJECT.getByName("foo");
    
    		// Methods on the Durable Object are invoked via the stub
    		const rpcResponse = await stub.sayHello();
    
    		return new Response(rpcResponse);
    	},
    };
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export interface Env {
    	MY_DURABLE_OBJECT: DurableObjectNamespace<MyDurableObject>;
    }
    
    // Durable Object
    export class MyDurableObject extends DurableObject {
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    	}
    
    	async sayHello(): Promise<string> {
    		return "Hello, World!";
    	}
    }
    
    // Worker
    export default {
    	async fetch(request, env) {
    		// A stub is a client used to invoke methods on the Durable Object
    		const stub = env.MY_DURABLE_OBJECT.getByName("foo");
    
    		// Methods on the Durable Object are invoked via the stub
    		const rpcResponse = await stub.sayHello();
    
    		return new Response(rpcResponse);
    	},
    } satisfies ExportedHandler<Env>;

## Properties

### `id`

`id` is a property of the `DurableObjectStub` corresponding to the [`DurableObjectId`](https://developers.cloudflare.com/durable-objects/api/id) used to create the stub.
    
    
    const id = env.MY_DURABLE_OBJECT.newUniqueId();
    const stub = env.MY_DURABLE_OBJECT.get(id);
    console.assert(id.equals(stub.id), "This should always be true");
    
    
    id = env.MY_DURABLE_OBJECT.newUniqueId()
    stub = env.MY_DURABLE_OBJECT.get(id)
    assert id.equals(stub.id), "This should always be true"

### `name`

`name` is an optional property of a `DurableObjectStub`, which returns a name if it was provided upon stub creation either directly via [`DurableObjectNamespace::getByName`](https://developers.cloudflare.com/durable-objects/api/namespace/#getbyname) or indirectly via a [`DurableObjectId`](https://developers.cloudflare.com/durable-objects/api/id) created by [`DurableObjectNamespace::idFromName`](https://developers.cloudflare.com/durable-objects/api/namespace/#idfromname). This value is undefined if the [`DurableObjectId`](https://developers.cloudflare.com/durable-objects/api/id) used to create the `DurableObjectStub` was constructed using [`DurableObjectNamespace::newUniqueId`](https://developers.cloudflare.com/durable-objects/api/namespace/#newuniqueid).
    
    
    const stub = env.MY_DURABLE_OBJECT.getByName("foo");
    console.assert(stub.name === "foo", "This should always be true");
    
    
    stub = env.MY_DURABLE_OBJECT.getByName("foo")
    assert stub.name == "foo", "This should always be true"

## Related resources

  * [Durable Objects: Easy, Fast, Correct – Choose Three ↗︎](https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/).



[PreviousDurable Object ID](https://developers.cloudflare.com/durable-objects/api/id/)[NextDurable Object State](https://developers.cloudflare.com/durable-objects/api/state/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/api/stub.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
