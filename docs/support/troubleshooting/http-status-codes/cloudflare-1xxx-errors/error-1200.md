---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1200/
title: Error 1200 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:58.275202+00:00
---

# Error 1200 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1200/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1200



# Error 1200

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1200/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1200: Cache connection limit Common cause Resolution

## Error 1200: Cache connection limit

This error indicates that the number of requests queued on Cloudflare's edge exceeds the limit.

### Common cause

There are too many requests queued on Cloudflare's edge that are awaiting process by your origin web server. This limit protects Cloudflare's systems.

### Resolution

Tune your origin webserver to accept incoming connections faster. Adjust your caching settings to improve cache-hit rates so that fewer requests reach your origin web server. Reach out to your hosting provider or web administrator for assistance.

[PreviousError 1104](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1104/)[NextOverview](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)

Was this helpful?

YesNo
