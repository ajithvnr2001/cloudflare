---
url: https://developers.cloudflare.com/sandbox/sdk/guides/deploy/
title: Deploy a Sandbox application (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:24.487540+00:00
---

# Deploy a Sandbox application (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/deploy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /Deploy a Sandbox application



# Deploy a Sandbox application

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/deploy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewKeep the package and image alignedDeploy from your machineWorkers BuildsRelated

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Sandbox runs on [Containers](https://developers.cloudflare.com/containers/). For deploy commands, Workers Builds, and rollout flags, refer to [Deploy Containers](https://developers.cloudflare.com/containers/guides/deploy/) and [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/).

To put `exposePort()` on a custom domain, refer to [Configure preview URLs on a custom domain](https://developers.cloudflare.com/sandbox/sdk/guides/preview-urls-custom-domain/).

## Keep the package and image aligned

The Worker depends on `@cloudflare/sandbox`. The container image must come from the same release line (Dockerfile and base image tags from the template or docs for that version).

When you bump the npm package:

  1. Update the Dockerfile or image reference for the same line.

  2. Run `wrangler deploy` so the new image is published.

  3. If the Worker and image must cut over together, deploy with an immediate rollout:

npmyarnpnpm
         
         npx wrangler deploy --containers-rollout=immediate
         
         yarn wrangler deploy --containers-rollout=immediate
         
         pnpm wrangler deploy --containers-rollout=immediate

Use this for breaking package and image pairs. Refer to [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/).




## Deploy from your machine

  1. Start Docker if `image` is a Dockerfile path. Registry image references do not need Docker at deploy time.

  2. From the project root:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  3. Confirm the Worker URL responds, then exercise a sandbox route.




The first deploy can take several minutes while the image provisions.

## Workers Builds

For production, use `wrangler deploy` so the package and image can update together.

Non-production Workers Builds defaults to `wrangler versions upload`, which does not publish a new image. [Version URLs](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/) are not generated for these Workers (they implement Durable Objects). Test with `wrangler dev`, or with a staging Worker or [environment](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#wrangler-environments) that runs `wrangler deploy`.

More detail: [Before production](https://developers.cloudflare.com/containers/guides/deploy/#before-production).

## Related

  * [Deploy Containers](https://developers.cloudflare.com/containers/guides/deploy/)
  * [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/)
  * [Configure preview URLs on a custom domain](https://developers.cloudflare.com/sandbox/sdk/guides/preview-urls-custom-domain/)



[PreviousBrowser terminals](https://developers.cloudflare.com/sandbox/sdk/guides/browser-terminals/)[NextConfigure preview URLs on a custom domain](https://developers.cloudflare.com/sandbox/sdk/guides/preview-urls-custom-domain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/deploy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
