---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/
title: Error 1015 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.268099+00:00
---

# Error 1015 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1015



# Error 1015

Last updated May 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1015: You are being rate limited Common cause Resolution

## Error 1015: You are being rate limited

The website you are trying to visit has received too many requests and has temporarily blocked you from accessing it.

### Common cause

The website owner has configured rate limiting rules that restrict how many requests a visitor can make to their site in a given time period. When you exceed this limit, Cloudflare returns a `1015` error.

### Resolution

**If you are a site visitor:**

  * Wait for a period of time, then try accessing the website again later. Do not repeatedly try to access the website within a short period of time, as this may extend the block.
  * If you are still blocked or need help, contact the website owner or the website's support team directly for help. Cloudflare does not control which visitors are rate limited, the website owner sets these rules.



**If you are the site owner:**

  * Review your current [rate limiting thresholds](https://developers.cloudflare.com/waf/rate-limiting-rules/) and adjust your configuration.
  * If a rate limiting rule is blocking requests in a short time period (for example, one second), try increasing the time period to 10 seconds.



Note

 _Unable to purge_ is another `1015` error code relating to [Cloudflare cache purge](https://developers.cloudflare.com/cache/how-to/purge-cache). Retry the cache purge and contact [Cloudflare support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) if errors persist.

[PreviousError 1014](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/)[NextError 1016](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1016/)

Was this helpful?

YesNo
