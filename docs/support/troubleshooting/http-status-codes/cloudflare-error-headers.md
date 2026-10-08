---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/
title: Cloudflare error diagnostic headers \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:59.263219+00:00
---

# Cloudflare error diagnostic headers · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)

  4. /[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)
  5. /Cloudflare error diagnostic headers



# Cloudflare error diagnostic headers

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow to capture these headersUsing cf-error-type for diagnosis

When Cloudflare generates an error page (as opposed to forwarding an error from your origin server), the response includes two diagnostic headers:

  * **`cf-error-type`** : Identifies the error category. Common values: 
    * `1000` — DNS resolution failure (A record points to a Cloudflare IP)
    * `1016` — Origin DNS error (CNAME target does not resolve)
    * `1101` — Worker threw an unhandled exception
    * `1102` — Worker exceeded resource limits (CPU or memory)
    * `52x` — Origin connectivity error (521, 522, 523, 524, 525, 526)
  * **`cf-error-origin`** : Identifies which Cloudflare system generated the error.



These headers are present **only on Cloudflare-generated error pages** , not on errors forwarded from your origin server.

## How to capture these headers

Reproduce the error and inspect response headers using one of:

  * `curl -v https://example.com` — look for `cf-error-type` in the response headers
  * Browser DevTools: select **Network** > select the failing request > **Headers**
  * Export a HAR file and inspect the response headers



## Using cf-error-type for diagnosis

`cf-error-type` prefix | Origin | Next step  
---|---|---  
`1xxx` | DNS / routing layer | Check DNS records; verify no Cloudflare IP in A record  
`1101` / `1102` | Workers runtime | Check `wrangler tail` for the exception  
`52x` | Origin connectivity | Check origin server is up and reachable  
  
[PreviousError 530](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-530/)[NextOverview](https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/)

Was this helpful?

YesNo
