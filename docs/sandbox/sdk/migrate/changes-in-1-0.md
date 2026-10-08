---
url: https://developers.cloudflare.com/sandbox/sdk/migrate/changes-in-1-0/
title: Changes in Sandbox SDK 1.0 \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:26.626357+00:00
---

# Changes in Sandbox SDK 1.0 · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/migrate/changes-in-1-0/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[Migrate to 1.0](https://developers.cloudflare.com/sandbox/sdk/migrate/)
  5. /Changes in 1.0



# Changes in Sandbox SDK 1.0

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/migrate/changes-in-1-0/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhere each 0.x feature goesDecisions your code makesRelated resources

In Sandbox SDK 0.x, the `Sandbox` class from the package is your Durable Object. It starts the container, keeps it running, and sends each call to a server inside the container. In 1.0, you write the Durable Object class, and it calls the container directly through `this.ctx.container`.

In 0.x, the `Sandbox` class from the package starts the container, keeps it running, and manages previews and backups. The container runs the SDK server and bash sessions from the `cloudflare/sandbox` image. In 1.0, your own Durable Object does the same jobs. The container runs your image and your commands, plus the `sandbox-shim` helper when you use `Files`.

`this.ctx.container` does what the 0.x SDK server did. It runs commands, connects to ports, intercepts outbound requests, and saves snapshots. The package keeps only small helpers, such as the `Files` class.

Decisions that depend on your application stay in your code: how long a sandbox runs, what it can reach, and what happens when a call fails. For example, a cancelled command may already have changed files, and only your application knows whether running it again is safe.

## Where each 0.x feature goes

Each 0.x feature moves to one of three places, depending on which part of 0.x did its work:

  * The `Sandbox` class handles lifetime, preview URLs, tunnels, backups, and process tracking. In 1.0, these become code in your Durable Object class, which keeps any records it needs in its own storage.
  * The SDK server runs commands, sessions, and file calls. In 1.0, these become `exec()` calls, or calls to the `Files` class, which runs the `sandbox-shim` helper through `exec()`.
  * Wrangler configuration and class properties set the image, Internet access, and outbound rules. In 1.0, these become options to `start()` and outbound handlers that your class registers.



Some 0.x features have no equivalent. For each 0.x API and its replacement, refer to the [API map](https://developers.cloudflare.com/sandbox/sdk/migrate/api-map/).

## Decisions your code makes

A container has no Internet access unless `start()` passes `enableInternet: true`. To allow one destination, your class registers an outbound handler for its hostname. The handler can add a credential that the container never sees. For more information, refer to [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/).

`exec()` takes an array of arguments and starts that process without a shell. Text passed as an argument cannot start a second command. A shell runs only when you start one, such as `["sh", "-c", "npm ci && npm test"]`. Each call also sets its own `cwd` and `env`. No session carries them from one call to the next.

Your class decides how long a sandbox runs by setting the inactivity timeout after `start()`, and again in the constructor when a restarted Durable Object finds the container running. A deploy does not replace running containers. A new image applies only to containers that start after the deploy. The same holds for code that your class runs when it starts a container, such as the outbound handlers it registers. For more information, refer to [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/).

Your image provides every tool that your commands use. The 0.x image includes Python, Git, `curl`, `wget`, `jq`, `unzip`, and `ps`. `cloudflare/debian-trixie` and `node:24-trixie-slim`, which these pages use, include none of them. `Files` and `S3Mount` also need the `sandbox-shim` helper in the image. For the `COPY` line, refer to [`@cloudflare/sandbox` requirements](https://developers.cloudflare.com/sandbox/reference/#requirements).

The package writes nothing to Durable Object storage. A preview token, a process record, or a snapshot ID exists only if your class stores it. The keys that 0.x wrote stay in storage, and 1.0 code ignores them.

The package also retries nothing and sets no time limits. To stop a command that runs too long, run it under GNU coreutils `timeout`, as [Replace timeouts](https://developers.cloudflare.com/sandbox/sdk/migrate/commands/#replace-timeouts) describes.

## Related resources

  * [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/)
  * [API map](https://developers.cloudflare.com/sandbox/sdk/migrate/api-map/)
  * [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/)
  * [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/)



[PreviousOverview](https://developers.cloudflare.com/sandbox/sdk/migrate/)[NextPlan the move](https://developers.cloudflare.com/sandbox/sdk/migrate/plan-the-move/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/migrate/changes-in-1-0.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
