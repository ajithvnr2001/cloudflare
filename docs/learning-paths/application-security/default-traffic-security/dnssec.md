---
url: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/dnssec/
title: DNSSEC \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:42.761318+00:00
---

# DNSSEC · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/dnssec/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Default traffic security](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/)
  5. /DNSSEC



# DNSSEC

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/dnssec/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

DNS Security Extensions (DNSSEC) adds an extra layer of authentication to DNS, ensuring requests are not routed to a spoofed domain.

For additional background on DNSSEC, visit the [Cloudflare Learning Center ↗︎](https://www.cloudflare.com/learning/dns/dns-security/).

When you [enable DNSSEC](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/), Cloudflare signs your zone, publishes your public signing keys, and generates your **DS** record.

Note:

Cloudflare automatically adds **DS** records for domains using Cloudflare Registrar or those using `.ch` and `.cz` top-level domains.

[PreviousBrowser Integrity](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/browser-integrity/)[NextSSL / TLS](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/default-traffic-security/dnssec.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
