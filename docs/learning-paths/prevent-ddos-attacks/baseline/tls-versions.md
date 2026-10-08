---
url: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/tls-versions/
title: Update TLS versions \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:51.845344+00:00
---

# Update TLS versions · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/tls-versions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Prevent Ddos Attacks

  4. /[Baseline DDoS protection](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/)
  5. /Update TLS versions



# Update TLS versions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/tls-versions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdditional resources

In some circumstances - specifically when an application allows client-initiated SSL/TLS renegotiation - previous versions of SSL/TLS can be more vulnerable to DDoS attacks.

When you use an SSL/TLS certificate issued by Cloudflare1, you can reduce the impact of this vulnerability by:

  * Updating the [Minimum TLS Version](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/) accepted by your application.
  * Allowing [TLS 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/).



## Additional resources

For more details on this vulnerability, refer to [Secure Server- and Client-Initiated SSL Renegotiation ↗︎](https://crashtest-security.com/secure-client-initiated-ssl-renegotiation/).

## Footnotes

  1. Meaning either [Universal](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) or [Advanced](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) certificates. ↩




[PreviousEnable WAF](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/enable-waf/)[NextSet up alerts](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/set-up-alerts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/prevent-ddos-attacks/baseline/tls-versions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
