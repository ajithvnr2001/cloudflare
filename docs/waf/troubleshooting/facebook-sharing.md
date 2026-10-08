---
url: https://developers.cloudflare.com/waf/troubleshooting/facebook-sharing/
title: Issues sharing to Facebook \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:49.303492+00:00
---

# Issues sharing to Facebook · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/troubleshooting/facebook-sharing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Troubleshooting
  4. /Issues sharing to Facebook



# Issues sharing to Facebook

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/troubleshooting/facebook-sharing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewResolution

Cloudflare does not block or challenge requests from Facebook by default. However, a post of a website to Facebook returns an _Attention Required_ error in the following situations:

  * You have globally [enabled Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/).
  * There is a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/) or [page rule](https://developers.cloudflare.com/rules/page-rules/) setting turning on Under Attack mode.
  * There is a [custom rule](https://developers.cloudflare.com/waf/custom-rules/) with a challenge or block action that includes a Facebook IP address.



A country challenge can block a Facebook IP address. Facebook is known to crawl from both the US and Ireland.

## Resolution

To resolve issues sharing to Facebook, do one of the following:

  * Remove the corresponding IP, ASN, or country custom rule that challenges or blocks Facebook IPs.
  * Create a [skip rule](https://developers.cloudflare.com/waf/custom-rules/skip/) for ASNs`AS32934` and `AS63293` (use the _Skip_ action and configure the rule to skip **Security Level**).
  * Review existing configuration rules and Page Rules and make sure they are not affecting requests from Facebook IPs.



If you experience issues with Facebook sharing, you can re-scrape pages via the **Fetch New Scrape Information** option on Facebook's Object Debugger. Facebook [provides an API ↗︎](https://developers.facebook.com/docs/sharing/opengraph/using-objects) to help update a large number of resources.

If you continue to have issues, you can [contact Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) with the URLs of your website that cannot share to Facebook, and confirming that you have re-scraped the URLs.

[PreviousFake bot detection blocking legitimate requests](https://developers.cloudflare.com/waf/troubleshooting/fake-bot-managed-rules/)[NextSameSite cookie interaction with Cloudflare](https://developers.cloudflare.com/waf/troubleshooting/samesite-cookie-interaction/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/troubleshooting/facebook-sharing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
