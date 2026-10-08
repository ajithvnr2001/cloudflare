---
url: https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/
title: Deprecating Sandbox SDK features \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.121065+00:00
---

# Deprecating Sandbox SDK features · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 9, 2026

## Deprecating Sandbox SDK features

[Sandboxes](https://developers.cloudflare.com/sandbox/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Sandbox SDK 1.0 preview

A preview of **Sandbox SDK 1.0** is available on `@cloudflare/sandbox@next`. For new projects, or to move past these deprecations in one migration, refer to the [Sandbox SDK 1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) and [Migrate](https://developers.cloudflare.com/sandbox/1-0-preview/migrate/).

Today we are announcing the deprecation of several features from the Sandbox SDK. The SDK has grown and matured substantially since it first launched. As agent workflows have developed, we have shipped many new features and experiments so developers can easily integrate secure, isolated code execution into their workflows.

We want the SDK to continue providing a stable foundation for agentic workflows while we iterate quickly on the codebase. These deprecated features have either been superseded by newer capabilities or seen low adoption. Do not build new work on them. Migrate using the [2026 deprecation migration guide](https://developers.cloudflare.com/sandbox/guides/2026-deprecation/), or move to the [Sandbox SDK 1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) when you can.

#### HTTP and WebSocket transports

In April 2026, we released the new RPC transport and deprecated the WebSocket transport. This setting governs how the sandbox container talks to the Workers ecosystem. The RPC transport removes the limitations of both the HTTP and WebSocket transports. As of this announcement, RPC is the recommended default. HTTP and WebSocket transports are deprecated and will not ship in future Sandbox SDK majors.

To migrate, update the `SANDBOX_TRANSPORT` variable to `rpc` or set the `transport` option when calling `getSandbox()`. For more information, refer to the [transport configuration documentation](https://developers.cloudflare.com/sandbox/configuration/transport/).

#### Desktop

The desktop feature ran a full Linux desktop inside the sandbox (display server, desktop environment, and VNC/noVNC) so agents and apps could drive a GUI with screenshots, mouse, and keyboard — the same _computer-use_ shape other sandbox products expose for UI automation. Adoption stayed low, and we removed it in `0.10.2`. If you need that capability again, you can build it on top of the sandbox with [extensions](https://developers.cloudflare.com/sandbox/1-0-preview/extensions/) rather than a built-in `sandbox.desktop` API.

#### Expose ports

We recently released support for Cloudflare Tunnel in the Sandbox SDK. This provides a robust API for exposing services running in your sandbox to the public internet. It fixes issues many were facing with local development and deployment to `workers.dev` domains. To migrate from `exposePort()` to tunnels, refer to the [tunnels API documentation](https://developers.cloudflare.com/sandbox/api/tunnels/) and the [expose services guide](https://developers.cloudflare.com/sandbox/guides/expose-services/).

#### Default sessions

By default, the `exec()` method in the Sandbox SDK maintains a default session across all calls, so a `cd` in one call is honored in the next. This convenience helped developers writing `exec` statements by hand, but confused agents and caused hard-to-trace bugs. As of `0.10.3`, we have introduced the [`enableDefaultSession`](https://developers.cloudflare.com/sandbox/configuration/sandbox-options/) flag on the `getSandbox()` interface to turn this off. Default sessions as a concept — and the flag — will be removed in an upcoming release.

We recommend setting `enableDefaultSession: false` today and using the [`sandbox.createSession()` API](https://developers.cloudflare.com/sandbox/api/sessions/) when you need the previous behavior.

#### Other changes

We are also consolidating all APIs that buffer data to support streaming by default. This includes [`readFile`, `writeFile`](https://developers.cloudflare.com/sandbox/api/files/), and [`exec`](https://developers.cloudflare.com/sandbox/api/commands/). The stream equivalents will be removed.

We are exploring moving non-core features like the [code interpreter](https://developers.cloudflare.com/sandbox/guides/code-execution/), [terminal](https://developers.cloudflare.com/sandbox/api/terminal/), and [git APIs](https://developers.cloudflare.com/sandbox/guides/git-workflows/) into helpers. These features will retain their existing APIs, so migration should be simple.

#### Next steps

If you use any of these features on the **current stable** package, refer to the [2026 deprecation migration guide](https://developers.cloudflare.com/sandbox/guides/2026-deprecation/). Coding agents can use the **`sandbox-stable`** skill for stable-package work and that guide for cleanup ([Agent setup](https://developers.cloudflare.com/agent-setup/) · [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills)).

If you are moving to **Sandbox SDK 1.0** (`@next`), use the [1.0 preview](https://developers.cloudflare.com/sandbox/1-0-preview/) and [Migrate](https://developers.cloudflare.com/sandbox/1-0-preview/migrate/) guides instead — or the **`sandbox-migrate-to-next`** skill after installing Cloudflare Skills. New projects should prefer **`sandbox-next`** on `@next`.

For any questions, ask in the [Cloudflare Developers Discord ↗︎](https://discord.gg/cloudflaredev).
