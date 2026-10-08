---
url: https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-container-api/
title: Migrate from the Container class to the Durable Object Container API \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:36.161145+00:00
---

# Migrate from the Container class to the Durable Object Container API · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-container-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Guides
  4. /Migrate from the Container class to the Durable Object Container API



# Migrate from the Container class to the Durable Object Container API

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-container-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReplace Container class helpers

The Durable Object Container API lets your Durable Object coordinate container compute with persistent storage, alarms, and request handling. Access it as `this.ctx.container` inside a Durable Object with a container binding. When migrating from the `Container` class, replace its helpers with application code where needed.

Before changing code, identify which helpers your application uses. Some helpers require application code to preserve their existing behavior. For an API comparison, refer to [Choose an API](https://developers.cloudflare.com/containers/api/#choose-an-api).

You can migrate the implementation without replacing the Durable Object. Keep the Worker name, exported class name, binding, container image, and existing migration tags unchanged. Changing the TypeScript base class does not require a new Durable Object migration.

## Replace Container class helpers

The `Container` class extends `DurableObject`. Replace its inherited lifecycle and routing helpers with application code that uses `ctx.container`.

  1. In your Worker, change the class to extend `DurableObject` from `cloudflare:workers`. Keep the exported class name to retain its existing container definition and Durable Object binding. Do not add a new Durable Object migration solely because you changed the base class. Refer to [Wrangler configuration](https://developers.cloudflare.com/containers/configuration/wrangler/).
  2. Replace `start()` calls with [`ctx.container.start()`](https://developers.cloudflare.com/containers/api/durable-object-container/#start). Replace `stop()` calls with [`signal()`](https://developers.cloudflare.com/containers/api/durable-object-container/#signal) or [`destroy()`](https://developers.cloudflare.com/containers/api/durable-object-container/#destroy), as appropriate. Do not assume `start()` waits for a port to become ready.
  3. Replace `defaultPort`, `containerFetch()`, and automatic `fetch()` routing with [`getTcpPort(port).fetch()`](https://developers.cloudflare.com/containers/api/durable-object-container/#gettcpport) and your own request routing. Check port readiness before forwarding requests.
  4. Replace `sleepAfter` with [`setInactivityTimeout()`](https://developers.cloudflare.com/containers/api/durable-object-container/#setinactivitytimeout). Replace lifecycle hooks and `schedule()` with application code, [`monitor()`](https://developers.cloudflare.com/containers/api/durable-object-container/#monitor), and [Durable Object alarms](https://developers.cloudflare.com/durable-objects/api/alarms/) where appropriate.
  5. Test startup, concurrent requests, readiness, idle shutdown, alarm delivery, storage continuity, and recovery after a container restart. A container can be temporarily unavailable after `stop()` or `destroy()`. Retry allocation before checking port readiness. Then remove `@cloudflare/containers` only if no other code imports it.



Keep the same image in the `containers` section of your Wrangler configuration unless you intend to change the container application itself. The direct API still runs the image associated with its Durable Object class.

For process handling and output, refer to [Execute commands](https://developers.cloudflare.com/containers/guides/execute-commands/) and the [`exec()` reference](https://developers.cloudflare.com/containers/api/durable-object-container/#exec).

[PreviousUse snapshots](https://developers.cloudflare.com/containers/guides/snapshots/)[NextMigrate to the Durable Object scheduling policy](https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-scheduling-policy/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/guides/migrate-to-durable-object-container-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
