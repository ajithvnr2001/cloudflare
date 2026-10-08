---
url: https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/
title: Lifecycle (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:21.896793+00:00
---

# Lifecycle (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[API reference](https://developers.cloudflare.com/sandbox/sdk/api/)
  5. /Lifecycle



# Lifecycle

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethods getSandbox()

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Create and manage sandbox containers. Get sandbox instances, configure options, and clean up resources.

## Methods

### `getSandbox()`

Get or create a sandbox instance by ID.
    
    
    const sandbox = getSandbox(
      binding: DurableObjectNamespace<Sandbox>,
      sandboxId: string,
      options?: SandboxOptions
    ): Sandbox

**Parameters** :

  * `binding` \- The Durable Object namespace binding from your Worker environment
  * `sandboxId` \- Unique identifier for this sandbox. The same ID always returns the same sandbox instance. In user-facing apps, scope IDs to a single user.
  * `options` (optional) - See [SandboxOptions](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/) for all available options: 
    * `enableDefaultSession` \- Use the default session for operations without an explicit `sessionId`. Set to `false` to evaluate each call in isolation (default: `true`)
    * `sleepAfter` \- Duration of inactivity before automatic sleep (default: `"10m"`)
    * `keepAlive` \- Prevent automatic sleep entirely. Persists across hibernation (default: `false`)
    * `containerTimeouts` \- Configure container startup timeouts
    * `normalizeId` \- Lowercase sandbox IDs for preview URL compatibility (default: `false`)



**Returns** : `Sandbox` instance

Note

The container starts lazily on first operation. Calling `getSandbox()` returns immediately—the container only spins up when you execute a command, write a file, or perform other operations. See [Sandbox lifecycle](https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/) for details.

Implicit execution mode

By default, sandbox methods that do not specify a `sessionId` run in the sandbox's default session and preserve shell state between calls. It is recommended to set `enableDefaultSession` to `false` to ensure operations run in isolation. The `createSession()` API exists when sessions are required. Default sessions will be removed in a future version of the Sandbox SDK.
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request, env) {
    		const sandbox = getSandbox(env.Sandbox, "user-123");
    		const result = await sandbox.exec("python script.py");
    		return Response.json(result);
    	},
    };
    
    
    import { getSandbox } from '@cloudflare/sandbox';
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        const sandbox = getSandbox(env.Sandbox, 'user-123');
        const result = await sandbox.exec('python script.py');
        return Response.json(result);
      }
    };

Caution

When using `keepAlive: true`, you **must** call `destroy()` when finished to prevent containers running indefinitely.

* * *

### `setKeepAlive()`

Enable or disable keepAlive mode dynamically after sandbox creation.
    
    
    await sandbox.setKeepAlive(keepAlive: boolean): Promise<void>

**Parameters** :

  * `keepAlive` \- `true` to prevent automatic sleep, `false` to allow normal sleep behavior



When enabled, the sandbox automatically sends heartbeat pings every 30 seconds to prevent container eviction. When disabled, the sandbox returns to normal sleep behavior based on the `sleepAfter` configuration.
    
    
    const sandbox = getSandbox(env.Sandbox, "user-123");
    
    // Enable keepAlive for a long-running process
    await sandbox.setKeepAlive(true);
    await sandbox.startProcess("python long_running_analysis.py");
    
    // Later, disable keepAlive when done
    await sandbox.setKeepAlive(false);
    
    
    const sandbox = getSandbox(env.Sandbox, 'user-123');
    
    // Enable keepAlive for a long-running process
    await sandbox.setKeepAlive(true);
    await sandbox.startProcess('python long_running_analysis.py');
    
    // Later, disable keepAlive when done
    await sandbox.setKeepAlive(false);

Heartbeat mechanism

When keepAlive is enabled, the sandbox automatically sends lightweight ping requests to the container every 30 seconds to prevent eviction. This happens transparently without affecting your application code.

Resource management

Containers with `keepAlive: true` will not automatically timeout. Always disable keepAlive or call `destroy()` when done to prevent containers running indefinitely.

* * *

### `destroy()`

Destroy the sandbox container and free up resources.
    
    
    await sandbox.destroy(): Promise<void>

Immediately terminates the container and permanently deletes all state:

  * All files in `/workspace`, `/tmp`, and `/home`
  * All running processes
  * All sessions (including the default session)
  * Network connections and exposed ports


    
    
    async function executeCode(code) {
    	const sandbox = getSandbox(env.Sandbox, `temp-${Date.now()}`);
    
    	try {
    		await sandbox.writeFile("/tmp/code.py", code);
    		const result = await sandbox.exec("python /tmp/code.py");
    		return result.stdout;
    	} finally {
    		await sandbox.destroy();
    	}
    }
    
    
    async function executeCode(code: string): Promise<string> {
      const sandbox = getSandbox(env.Sandbox, `temp-${Date.now()}`);
    
      try {
        await sandbox.writeFile('/tmp/code.py', code);
        const result = await sandbox.exec('python /tmp/code.py');
        return result.stdout;
      } finally {
        await sandbox.destroy();
      }
    }

Note

Containers automatically sleep after 10 minutes of inactivity but still count toward account limits. Use `destroy()` to immediately free up resources.

* * *

## Related resources

  * [Sandbox lifecycle concept](https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/) \- Understanding container lifecycle and state
  * [Sandbox options configuration](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/) \- Configure `keepAlive` and other options
  * [Sessions API](https://developers.cloudflare.com/sandbox/sdk/api/sessions/) \- Create execution contexts within a sandbox



[PreviousOverview](https://developers.cloudflare.com/sandbox/sdk/api/)[NextCommands](https://developers.cloudflare.com/sandbox/sdk/api/commands/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/api/lifecycle.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
