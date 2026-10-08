---
url: https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/
title: Recovering from a hacked site \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:27.750928+00:00
---

# Recovering from a hacked site · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /Security
  4. /Recovering from a hacked site



# Recovering from a hacked site

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRecovering from an attackPreventing and mitigating the risks of a future hack

If your website has been hacked recently, review the recommended steps below to recover a hacked website and prevent future hacks.

## Recovering from an attack

To recover from an attack, reach out to your hosting provider to request:

  * Details about the hack, including how they believe the site was hacked.
  * That your hosting provider remove any malicious content placed on your website.



Once the hack has been resolved, you should resolve site warnings in [Google Webmaster Tools ↗︎](https://www.google.com/webmasters/tools) and resubmit your site for Google's review.

* * *

## Preventing and mitigating the risks of a future hack

To prevent the risk of a hacked site:

  * Activate Cloudflare's [WAF managed rules](https://developers.cloudflare.com/waf/managed-rules/) so they can challenge or block known malicious behavior.
  * If you use a Content Management System (CMS), make sure you have the most recent version installed (CMS platforms push out updates to address known vulnerabilities).
  * If you use plugins, make sure they are updated.
  * If you have an admin login page, protect it with Cloudflare's [Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) or a [Cloudflare Access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).
  * Use a backup service so you can avoid losing valid content.



[PreviousProtect your origin server](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/)[NextScan for PCI compliance](https://developers.cloudflare.com/fundamentals/security/pci-scans/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/security/recovering-from-hacked-site.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
