---
url: https://developers.cloudflare.com/sandbox/sdk/api/
title: API reference (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:21.028182+00:00
---

# API reference (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)
  4. /API reference



# API reference

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

The Sandbox SDK provides a comprehensive API for executing code, managing files, running processes, and exposing services in isolated sandboxes.

### [Lifecycle](https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/)

Create and manage sandbox containers. Get sandbox instances, configure options, and clean up resources.

### [Commands](https://developers.cloudflare.com/sandbox/sdk/api/commands/)

Execute commands and stream output. Run scripts, manage background processes, and capture execution results.

### [Files](https://developers.cloudflare.com/sandbox/sdk/api/files/)

Read, write, and manage files in the sandbox filesystem. Includes directory operations and file metadata.

### [File watching](https://developers.cloudflare.com/sandbox/sdk/api/file-watching/)

Monitor real-time filesystem changes using native inotify. Build development tools, hot-reload systems, and responsive file processing.

### [Code interpreter](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/)

Execute Python and JavaScript code with rich outputs including charts, tables, and formatted data.

### [Ports](https://developers.cloudflare.com/sandbox/sdk/api/ports/)

Expose services running in the sandbox via preview URLs. Access web servers and APIs from the internet.

### [Tunnels](https://developers.cloudflare.com/sandbox/sdk/api/tunnels/)

Expose services on zero-config `*.trycloudflare.com` URLs via `sandbox.tunnels.get(port)`. Best for quick development and `.workers.dev` deployments.

### [Storage](https://developers.cloudflare.com/sandbox/sdk/api/storage/)

Mount S3-compatible buckets (R2, S3, GCS) as local filesystems for persistent data storage across sandbox lifecycles.

### [Backups](https://developers.cloudflare.com/sandbox/sdk/api/backups/)

Create point-in-time snapshots of directories and restore them from R2.

### [Sessions](https://developers.cloudflare.com/sandbox/sdk/api/sessions/)

Create isolated execution contexts within a sandbox. Each session maintains its own shell state, environment variables, and working directory.

### [Terminal](https://developers.cloudflare.com/sandbox/sdk/api/terminal/)

Connect browser-based terminal UIs to sandbox shells via WebSocket, with the xterm.js SandboxAddon for automatic reconnection and resize handling.

[PreviousConnect to Workers bindings](https://developers.cloudflare.com/sandbox/sdk/guides/workers-connections/)[NextLifecycle](https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
