---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/
title: Connection request details \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:00.939986+00:00
---

# Connection request details · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /Reference
  5. /Connection request details



# Connection request details

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHost headerSNI

When forwarding connections to your origin server, Cloudflare will set request parameters according to the following:

## Host header

Cloudflare will not alter the Host header by default, and will forward exactly as sent by the client. If you wish to change the value of the Host header you can utilise [Page-Rules](https://developers.cloudflare.com/workers/configuration/workers-with-page-rules/) or [Workers](https://developers.cloudflare.com/workers/) using the steps outlined in [certificate management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/).

## SNI

When establishing a TLS connection to your origin server, if the request is being sent to your configured Fallback Host then the value of the SNI sent by Cloudflare will match the value of the Host header sent by the client (i.e. the custom hostname).

If however the request is being forwarded to a Custom Origin, then the value of the SNI will be that of the Custom Origin.

[PreviousRemove domain](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain/)[NextTroubleshooting](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
