---
url: https://developers.cloudflare.com/r2/api/
title: API \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:42.237153+00:00
---

# API · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /API



# API

Last updated Jun 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 provides three API surfaces for interacting with your data:

  * **[Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/):** An in-Worker API accessed by binding an R2 bucket to a [Worker](https://developers.cloudflare.com/workers/). Use the Workers API to read, write, and list objects from within a Worker.
  * **[S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/):** An S3-compatible HTTP API available at `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`. Use existing S3 SDKs and tools to interact with R2.
  * **[Cloudflare REST API](https://developers.cloudflare.com/api/resources/r2/):** The `api.cloudflare.com` REST API used by the Cloudflare Dashboard and Wrangler CLI. Supports bucket management and object operations. [Rate limits apply](https://developers.cloudflare.com/r2/platform/limits/#cloudflare-rest-api). Use the S3-compatible API or Workers API for high-throughput workloads.



[PreviousDelete objects](https://developers.cloudflare.com/r2/objects/delete-objects/)[NextAuthentication](https://developers.cloudflare.com/r2/api/tokens/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
