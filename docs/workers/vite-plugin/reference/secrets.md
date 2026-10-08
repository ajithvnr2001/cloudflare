---
url: https://developers.cloudflare.com/workers/vite-plugin/reference/secrets/
title: Secrets \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:05.299568+00:00
---

# Secrets · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/vite-plugin/reference/secrets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/)

  4. /Reference
  5. /Secrets



# Secrets

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/vite-plugin/reference/secrets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Secrets](https://developers.cloudflare.com/workers/configuration/secrets/) are typically used for storing sensitive information such as API keys and auth tokens. For deployed Workers, they are set via the dashboard or Wrangler CLI.

In local development, secrets can be provided to your Worker by using a [`.dev.vars`](https://developers.cloudflare.com/workers/configuration/secrets/#local-development-with-secrets) file. If you are using [Cloudflare Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/cloudflare-environments/) then the relevant `.dev.vars` file will be selected. For example, `CLOUDFLARE_ENV=staging vite dev` will load `.dev.vars.staging` if it exists and fall back to `.dev.vars`.

Note

The `vite build` command copies the relevant `.dev.vars` file to the output directory. This is only used when running `vite preview` and is not deployed with your Worker.

[PreviousMigrating from wrangler dev](https://developers.cloudflare.com/workers/vite-plugin/reference/migrating-from-wrangler-dev/)[NextVite Environments](https://developers.cloudflare.com/workers/vite-plugin/reference/vite-environments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/vite-plugin/reference/secrets.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
