---
url: https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/
title: Sandbox lifecycle (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:22.849205+00:00
---

# Sandbox lifecycle (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Concepts](https://developers.cloudflare.com/sandbox/sdk/concepts/)
  5. /Sandbox lifecycle



# Sandbox lifecycle

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLifecycle states Creation Active Idle DestructionContainer lifetime and stateNaming strategies Per-user sandboxes Per-session sandboxes Per-task sandboxesRequest routingLifecycle management When to destroy Managing keepAlive containers Handling container restartsVersion compatibilityBest practicesRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

A sandbox is an isolated execution environment where your code runs. Each sandbox:

  * Has a unique identifier (sandbox ID)
  * Contains an isolated filesystem
  * Runs in a dedicated Linux container
  * Maintains state while the container is active
  * Exists as a Cloudflare Durable Object



## Lifecycle states

### Creation

A sandbox is created the first time you reference its ID:
    
    
    const sandbox = getSandbox(env.Sandbox, "user-123");
    await sandbox.exec('echo "Hello"'); // First request creates sandbox

### Active

The sandbox container is running and processing requests. All state remains available: files, running processes, shell sessions, and environment variables.

### Idle

After a period of inactivity (10 minutes by default, configurable via [`sleepAfter`](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/)), the container stops to free resources. When the next request arrives, a fresh container starts. All previous state is lost and the environment resets to its initial state.

**Note** : Containers with [`keepAlive: true`](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/#keepalive) never enter the idle state. They automatically send heartbeat pings every 30 seconds to prevent eviction.

### Destruction

Sandboxes are explicitly destroyed or automatically cleaned up:
    
    
    await sandbox.destroy();
    // All files, processes, and state deleted permanently

## Container lifetime and state

Sandbox state exists only while the container is active. Understanding this is critical for building reliable applications.

**While the container is active** (typically minutes to hours of activity):

  * Files written to `/workspace`, `/tmp`, `/home` remain available
  * Background processes continue running
  * Shell sessions maintain their working directory and environment
  * Code interpreter contexts retain variables and imports



**When the container stops** (due to inactivity or explicit destruction):

  * All files are deleted
  * All processes terminate
  * All shell state resets
  * All code interpreter contexts are cleared



The next request creates a fresh container with a clean environment.

## Naming strategies

### Per-user sandboxes
    
    
    const sandbox = getSandbox(env.Sandbox, `user-${userId}`);

Use this pattern for interactive environments, playgrounds, and notebooks where each user returns to their own active workspace.

### Per-session sandboxes
    
    
    const sessionId = `session-${Date.now()}-${Math.random()}`;
    const sandbox = getSandbox(env.Sandbox, sessionId);
    // Later:
    await sandbox.destroy();

Use this pattern for one-time execution, CI/CD, and tests that need a clean environment.

### Per-task sandboxes
    
    
    const sandbox = getSandbox(env.Sandbox, `build-${repoName}-${commit}`);

Idempotent operations with clear task-to-sandbox mapping. Good for builds, pipelines, and background jobs.

## Request routing

The first request to a sandbox determines its geographic location. Subsequent requests route to the same location.

**For global apps** :

  * Option 1: Multiple sandboxes per user with region suffix (`user-123-us`, `user-123-eu`)
  * Option 2: Single sandbox per user (simpler, but some users see higher latency)



## Lifecycle management

### When to destroy
    
    
    try {
    	const sandbox = getSandbox(env.Sandbox, sessionId);
    	await sandbox.exec("npm run build");
    } finally {
    	await sandbox.destroy(); // Clean up temporary sandboxes
    }

**Destroy when** : Session ends, task completes, resources no longer needed

**Do not destroy** : Personal environments, long-running services

### Managing keepAlive containers

Containers with [`keepAlive: true`](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/#keepalive) require explicit management since they do not timeout automatically:
    
    
    const sandbox = getSandbox(env.Sandbox, 'persistent-task', {
      keepAlive: true
    });
    
    // Later, when done with long-running work
    await sandbox.setKeepAlive(false); // Allow normal timeout behavior
    // Or explicitly destroy:
    await sandbox.destroy();

### Handling container restarts

Containers restart after inactivity or failures. Design your application to handle state loss:
    
    
    // Check if required files exist before using them
    const files = await sandbox.listFiles("/workspace");
    if (!files.includes("data.json")) {
    	// Reinitialize: container restarted and lost previous state
    	await sandbox.writeFile("/workspace/data.json", initialData);
    }
    
    await sandbox.exec("python process.py");

## Version compatibility

The SDK automatically checks that your npm package version matches the Docker container image version. **Version mismatches can cause features to break or behave unexpectedly.**

**What happens** :

  * On sandbox startup, the SDK queries the container's version
  * If versions do not match, a warning is logged
  * Some features may not work correctly if versions are incompatible



**When you might see warnings** :

  * You updated the npm package (`npm install @cloudflare/sandbox@0`) but forgot to update the `FROM` line in your Dockerfile



**How to fix** : Update your Dockerfile to match your npm package version. For example, if using `@cloudflare/sandbox@0.7.0`:
    
    
    # Default image (JavaScript/TypeScript)
    FROM docker.io/cloudflare/sandbox:0.7.0
    
    # Or Python image if you need Python support
    FROM docker.io/cloudflare/sandbox:0.7.0-python

See [Dockerfile reference](https://developers.cloudflare.com/sandbox/sdk/configuration/dockerfile/) for details on image variants and extending the base image.

## Best practices

  * **Name consistently** \- Use clear, predictable naming schemes
  * **Clean up temporary sandboxes** \- Always destroy when done
  * **Reuse user workspaces** \- One long-lived sandbox per user is often sufficient
  * **Batch operations** \- Combine commands: `npm install && npm test && npm build`
  * **Design for ephemeral state** \- Containers restart after inactivity, losing all state



## Related resources

  * [Architecture](https://developers.cloudflare.com/sandbox/sdk/concepts/architecture/) \- How sandboxes fit in the system
  * [Container runtime](https://developers.cloudflare.com/sandbox/sdk/concepts/containers/) \- What runs inside sandboxes
  * [Session management](https://developers.cloudflare.com/sandbox/sdk/concepts/sessions/) \- Advanced state isolation
  * [Directory backups](https://developers.cloudflare.com/sandbox/sdk/concepts/backup-restore/) \- Why restored files do not survive sleep unless you restore again
  * [Lifecycle API](https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/) \- Create and manage sandboxes
  * [Sessions API](https://developers.cloudflare.com/sandbox/sdk/api/sessions/) \- Create and manage execution sessions



[PreviousArchitecture](https://developers.cloudflare.com/sandbox/sdk/concepts/architecture/)[NextContainer runtime](https://developers.cloudflare.com/sandbox/sdk/concepts/containers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/concepts/sandboxes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
