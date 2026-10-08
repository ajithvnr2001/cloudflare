---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/
title: Error 1019 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.424497+00:00
---

# Error 1019 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1019



# Error 1019

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1019: Compute server error Common cause Resolution

## Error 1019: Compute server error

This error indicates a compute server error related to a Cloudflare Worker.

### Common cause

A Cloudflare Worker script recursively references itself.

### Resolution

Ensure your Cloudflare Worker does not access a URL that calls the same Workers script.

[PreviousError 1018](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/)[NextError 1020](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/)

Was this helpful?

YesNo
