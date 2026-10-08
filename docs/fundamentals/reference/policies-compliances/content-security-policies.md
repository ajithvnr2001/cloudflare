---
url: https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/
title: Content Security Policies (CSPs) and Cloudflare \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:26.331326+00:00
---

# Content Security Policies (CSPs) and Cloudflare · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Reference

  4. /Policies
  5. /Content Security Policies (CSPs)



# Content Security Policies (CSPs)

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUsing a CSP with Cloudflare Product requirements

A **Content Security Policy (CSP)** is an added layer of security that helps detect and mitigate certain types of attacks, including:

  * Content/code injection
  * Cross-site scripting (XSS)
  * Embedding malicious resources
  * Malicious iframes (clickjacking)



To learn more about configuring a CSP in general, refer to the [Mozilla documentation ↗︎](https://developer.mozilla.org/docs/web/http/csp).

## Using a CSP with Cloudflare

Cloudflare's [CDN](https://developers.cloudflare.com/cache/) is compatible with CSP.

Cloudflare does not:

  * Modify CSP headers from the origin web server (except when using Zaraz, to ensure the [Zaraz script is always running ↗︎](https://blog.cloudflare.com/cloudflare-zaraz-supports-csp/)).
  * Require changes to acceptable sources for first or third-party content.
  * Modify URLs (besides adding the [`/cdn-cgi/` endpoint](https://developers.cloudflare.com/fundamentals/reference/cdn-cgi-endpoint/) and [Cloudflare Fonts](https://developers.cloudflare.com/speed/optimization/content/fonts/) that rewrites Google Fonts urls).
  * Interfere with locations specified in your CSP.



If you require the CSP headers to be changed or added, you can change them using some Cloudflare products:

  * If your website is [proxied](https://developers.cloudflare.com/dns/proxy-status/) through Cloudflare, you can use a [response header transform rule](https://developers.cloudflare.com/rules/transform/response-header-modification/) to replace or add CSP headers.
  * If your website is hosted using [Cloudflare Pages](https://developers.cloudflare.com/pages/), you can set a [`_headers file`](https://developers.cloudflare.com/pages/configuration/headers/) to modify or add CSP headers.



### Product requirements

To use certain Cloudflare features, however, you may need to update the headers in your CSP:

Feature(s) | Updated headers  
---|---  
[Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/) | `script-src 'self' ajax.cloudflare.com;`  
[Scrape Shield](https://developers.cloudflare.com/waf/tools/scrape-shield/) | `script-src 'self' 'unsafe-inline'`  
[Web Analytics](https://developers.cloudflare.com/web-analytics/) | `script-src static.cloudflareinsights.com; connect-src cloudflareinsights.com`  
[Bot products](https://developers.cloudflare.com/bots/) | Refer to [JavaScript detections and CSPs](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/#if-you-have-a-content-security-policy-csp).  
[Client-side security](https://developers.cloudflare.com/client-side-security/) (formerly Page Shield) | Refer to [CSP header format](https://developers.cloudflare.com/client-side-security/reference/csp-header/).  
[Zaraz](https://developers.cloudflare.com/zaraz/) | No updates required ([details ↗︎](https://blog.cloudflare.com/cloudflare-zaraz-supports-csp/)).  
[Turnstile](https://developers.cloudflare.com/turnstile/) | Refer to [Turnstile CSP](https://developers.cloudflare.com/turnstile/reference/content-security-policy/).  
  
[PreviousCompliance documentation](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/compliance-docs/)[NextDelivering Videos with Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/reference/policies-compliances/content-security-policies.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
