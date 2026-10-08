---
url: https://developers.cloudflare.com/sandbox/sdk/concepts/security/
title: Security model (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:23.072034+00:00
---

# Security model (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/concepts/security/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Concepts](https://developers.cloudflare.com/sandbox/sdk/concepts/)
  5. /Security model



# Security model

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/concepts/security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewContainer isolationWithin a sandboxInput validation Command injectionAuthentication Sandbox access Preview URLs Quick tunnel URLsSecrets managementHandle outbound trafficWhat the SDK protects againstWhat you must implementBest practicesRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

The Sandbox SDK is built on [Containers](https://developers.cloudflare.com/containers/), which run each sandbox in its own VM for strong isolation.

## Container isolation

Each sandbox runs in a separate VM, providing complete isolation:

  * **Filesystem isolation** \- Sandboxes cannot access other sandboxes' files
  * **Process isolation** \- Processes in one sandbox cannot see or affect others
  * **Network isolation** \- Sandboxes have separate network stacks
  * **Resource limits** \- CPU, memory, and disk quotas are enforced per sandbox



For complete security details about the underlying container platform, see [Containers architecture](https://developers.cloudflare.com/containers/concepts/architecture/).

## Within a sandbox

All code within a single sandbox shares resources:

  * **Filesystem** \- All processes see the same files
  * **Processes** \- All sessions can see all processes
  * **Network** \- Processes can communicate via localhost



For complete isolation, use separate sandboxes per user:
    
    
    // Good - Each user in separate sandbox
    const userSandbox = getSandbox(env.Sandbox, `user-${userId}`);
    
    // Bad - Users sharing one sandbox
    const shared = getSandbox(env.Sandbox, 'shared');
    // Users can read each other's files!

## Input validation

### Command injection

Always validate user input before using it in commands:
    
    
    // Dangerous - user input directly in command
    const filename = userInput;
    await sandbox.exec(`cat ${filename}`);
    // User could input: "file.txt; rm -rf /"
    
    // Safe - validate input
    const filename = userInput.replace(/[^a-zA-Z0-9._-]/g, '');
    await sandbox.exec(`cat ${filename}`);
    
    // Better - use file API
    await sandbox.writeFile('/tmp/input', userInput);
    await sandbox.exec('cat /tmp/input');

## Authentication

### Sandbox access

Sandbox IDs provide basic access control but aren't cryptographically secure. Add application-level authentication:
    
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        const userId = await authenticate(request);
        if (!userId) {
          return new Response('Unauthorized', { status: 401 });
        }
    
        // User can only access their sandbox
        const sandbox = getSandbox(env.Sandbox, userId);
        return Response.json({ authorized: true });
      }
    };

### Preview URLs

Preview URLs include randomly generated tokens. Anyone with the URL can access the service.

To revoke access, unexpose the port:
    
    
    await sandbox.unexposePort(8080);

### Quick tunnel URLs

Quick tunnels (`sandbox.tunnels.get(port)`) return a `*.trycloudflare.com` URL with a random hostname assigned by Cloudflare — there is no separate access token. The hostname itself is the access control: anyone who knows the URL can reach the service. To revoke access, destroy the tunnel:
    
    
    await sandbox.tunnels.destroy(8080);

URLs do not survive a container restart, so a restart effectively rotates the hostname. As with preview URLs, add application-level authentication for any sensitive service. See the [Tunnels API](https://developers.cloudflare.com/sandbox/sdk/api/tunnels/) for details.
    
    
    from flask import Flask, request, abort
    import os
    
    app = Flask(__name__)
    
    def check_auth():
        token = request.headers.get('Authorization')
        if token != f"Bearer {os.environ['AUTH_TOKEN']}":
            abort(401)
    
    @app.route('/api/data')
    def get_data():
        check_auth()
        return {'data': 'protected'}

## Secrets management

Use environment variables, not hardcoded secrets, for values the sandbox process must consume directly:
    
    
    // Bad - hardcoded in file
    await sandbox.writeFile('/workspace/config.js', `
      const API_KEY = 'sk_live_abc123';
    `);
    
    // Good - use environment variables for values the sandbox process needs
    await sandbox.startProcess('node app.js', {
      env: {
        API_KEY: env.API_KEY,  // From Worker environment binding
      }
    });

For external API credentials that the sandbox does not need to read directly, keep the credential in the Worker and inject it with an outbound handler.

Clean up temporary sensitive data:
    
    
    try {
      await sandbox.writeFile('/tmp/sensitive.txt', secretData);
      await sandbox.exec('python process.py /tmp/sensitive.txt');
    } finally {
      await sandbox.deleteFile('/tmp/sensitive.txt');
    }

## Handle outbound traffic

Passing external API credentials directly to a sandbox — via environment variables or files — means the sandbox process holds a live credential that any code running inside it can read. Outbound handlers remove that exposure by keeping credentials in the Worker and injecting them into outbound requests.

The flow works as follows:
    
    
    Sandbox request → Outbound handler (injects real credentials) → External API

The sandbox never sees the real credential. Rotate the secret in your Worker's environment and every request uses the updated value.

This pattern is useful when accessing GitHub for private repository operations, AI services, or object storage where you want to keep credentials out of the container entirely. For implementation details, refer to [Handle outbound traffic](https://developers.cloudflare.com/sandbox/sdk/guides/outbound-traffic/).

## What the SDK protects against

  * Sandbox-to-sandbox access (VM isolation)
  * Resource exhaustion (enforced quotas)
  * Container escapes (VM-based isolation)



## What you must implement

  * Authentication and authorization
  * Input validation and sanitization
  * Rate limiting
  * Application-level security (SQL injection, XSS, etc.)



## Best practices

**Use separate sandboxes for isolation** :
    
    
    const sandbox = getSandbox(env.Sandbox, `user-${userId}`);

**Validate all inputs** :
    
    
    const safe = input.replace(/[^a-zA-Z0-9._-]/g, '');
    await sandbox.exec(`command ${safe}`);

**Use environment variables for secrets** :
    
    
    await sandbox.startProcess('node app.js', {
      env: { API_KEY: env.API_KEY }
    });

**Clean up temporary resources** :
    
    
    try {
      const sandbox = getSandbox(env.Sandbox, sessionId);
      await sandbox.exec('npm test');
    } finally {
      await sandbox.destroy();
    }

## Related resources

  * [Containers architecture](https://developers.cloudflare.com/containers/concepts/architecture/) \- Underlying platform security
  * [Sandbox lifecycle](https://developers.cloudflare.com/sandbox/sdk/concepts/sandboxes/) \- Resource management



[PreviousTerminal connections](https://developers.cloudflare.com/sandbox/sdk/concepts/terminal/)[NextDirectory backups](https://developers.cloudflare.com/sandbox/sdk/concepts/backup-restore/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/concepts/security.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
