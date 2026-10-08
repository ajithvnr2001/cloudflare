---
url: https://developers.cloudflare.com/logs/faq/common-calculations/
title: Common calculations FAQ \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:09.179509+00:00
---

# Common calculations FAQ · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/faq/common-calculations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Faq](https://developers.cloudflare.com/logs/faq/)
  4. /Common Calculations



# Common calculations FAQ

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/faq/common-calculations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview How can I calculate bytes served by the origin from Cloudflare Logs? How do I calculate bandwidth usage for my zone?

[❮ Back to FAQ](https://developers.cloudflare.com/logs/faq/)

### How can I calculate bytes served by the origin from Cloudflare Logs?

The best way to calculate bytes served by the origin is to use the `CacheResponseBytes` field in Cloudflare Logs, and to filter only requests that come from the origin. Make sure to filter out `OriginResponseStatus` values `0` and `304`, which indicate a revalidated response.

### How do I calculate bandwidth usage for my zone?

Bandwidth (or data transfer) can be calculated by adding the `EdgeResponseBytes` field in HTTP request logs. There are some types of requests that are not factored into bandwidth calculations. In order to only include relevant requests in calculations, add the filter `ClientRequestSource = 'eyeball'`.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/faq/common-calculations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
