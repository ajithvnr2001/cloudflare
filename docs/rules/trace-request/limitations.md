---
url: https://developers.cloudflare.com/rules/trace-request/limitations/
title: Cloudflare Trace limitations \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:55.431156+00:00
---

# Cloudflare Trace limitations · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/trace-request/limitations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Trace a request](https://developers.cloudflare.com/rules/trace-request/)
  4. /Limitations



# Cloudflare Trace limitations

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/trace-request/limitations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAutomatic rule bypassesUnsupported features

## Automatic rule bypasses

Trace does not display rules that are automatically bypassed for operational reasons.

For example, when SSL/TLS certificates are in `pending_validation` status, security rules are automatically disabled for domain control validation (DCV) paths like `/.well-known/pki-validation/` and `/.well-known/acme-challenge/`. These bypasses will not appear in trace results.

For more information, refer to [Why are some rules bypassed?](https://developers.cloudflare.com/waf/troubleshooting/faq/#why-are-some-rules-bypassed-when-i-did-not-create-an-exception) in the WAF documentation.

* * *

## Unsupported features

Trace currently does not support:

  * Hostnames using [Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  * [Spectrum](https://developers.cloudflare.com/spectrum/) applications



Additionally, the following products will not appear in trace results:

  * [Firewall rules (deprecated)](https://developers.cloudflare.com/firewall/)
  * [Load Balancing](https://developers.cloudflare.com/load-balancing/) and [Load Balancer Custom Rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/)
  * [IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)
  * [Rate limiting rules (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/)
  * [WAF managed rules (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/)
  * [Content security rules](https://developers.cloudflare.com/client-side-security/rules/)



[PreviousUse Cloudflare Trace](https://developers.cloudflare.com/rules/trace-request/how-to/)[NextChangelog](https://developers.cloudflare.com/rules/trace-request/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/trace-request/limitations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
