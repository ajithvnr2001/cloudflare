---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/
title: Product compatibility \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:02.098280+00:00
---

# Product compatibility · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /[SaaS customers](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/)
  5. /Product compatibility



# Product compatibility

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

As a general rule, settings on the customer zone will override settings on the SaaS zone. In addition, [O2O](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/) does not permit traffic directed to a custom hostname zone into another custom hostname zone.

The following table provides a list of compatibility guidelines for various Cloudflare products and features.

Note

This is not an exhaustive list of Cloudflare products and features.

Product | Customer zone | SaaS provider zone | Notes  
---|---|---|---  
[Access](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/) | Yes | Yes |   
[Always Online](https://developers.cloudflare.com/cache/how-to/always-online/) | No | No | In an O2O setup, Always Online does not trigger on the eyeball zone because the upstream SaaS provider zone is still reachable. Enabling it on the SaaS provider zone is not recommended because the eyeball zone may cache Internet Archive responses.  
[API Shield](https://developers.cloudflare.com/api-shield/) | Yes | No |   
[Argo Smart Routing](https://developers.cloudflare.com/argo-smart-routing/) | No | Yes | Customer zones can still use Smart Routing for non-O2O traffic.  
[Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) | Yes | Yes |   
[Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/) | Yes | Yes |   
[Cache](https://developers.cloudflare.com/cache/) | Yes* | Yes | Though caching is possible on a customer zone, it is generally discouraged (especially for HTML).  
  
Your SaaS provider likely performs its own caching outside of Cloudflare and caching on your zone might lead to out-of-sync or stale cache states.  
  
Customer zones can still cache content that are not routed through a SaaS provider's zone.  
[China Network](https://developers.cloudflare.com/china-network/) | No | No |   
[DNS](https://developers.cloudflare.com/dns/) | Yes* | Yes | As a SaaS customer, do not remove the records related to your Cloudflare for SaaS setup.  
  
Otherwise, your traffic will begin routing away from your SaaS provider.  
[HTTP/2 prioritization ↗︎](https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/) | Yes | Yes* | This feature must be enabled on the customer zone to function.  
[Image resizing](https://developers.cloudflare.com/images/optimization/transformations/overview/) | Yes | Yes |   
IPv6 | Yes | Yes |   
[IPv6 Compatibility](https://developers.cloudflare.com/network/ipv6-compatibility/) | Yes | Yes* | If the customer zone has **IPv6 Compatibility** enabled, generally the SaaS zone should as well.  
  
If not, make sure the SaaS zone enables [Pseudo IPv4](https://developers.cloudflare.com/network/pseudo-ipv4/).  
[Load Balancing](https://developers.cloudflare.com/load-balancing/) | No | Yes | Customer zones can still use Load Balancing for non-O2O traffic.  
[Page Rules](https://developers.cloudflare.com/rules/page-rules/) | Yes* | Yes | Page Rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.  
[Origin Rules](https://developers.cloudflare.com/rules/origin-rules/) | No | Yes |   
[Client-side security](https://developers.cloudflare.com/client-side-security/) (formerly Page Shield) | Yes | Yes |   
[Polish](https://developers.cloudflare.com/images/polish/) | Yes* | Yes | Polish only runs on cached assets. If the customer zone is bypassing cache for SaaS zone destined traffic, then images optimized by Polish will not be loaded from origin.  
[Rate Limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) | Yes* | Yes | Rate Limiting rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.  
[Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/) | No | No |   
[Security Level](https://developers.cloudflare.com/waf/tools/security-level/) | Yes | Yes |   
[Spectrum](https://developers.cloudflare.com/spectrum/) | No | No |   
[Transform Rules](https://developers.cloudflare.com/rules/transform/) | Yes* | Yes | Transform Rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.  
[WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/) | Yes | Yes | WAF custom rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.  
[WAF managed rules](https://developers.cloudflare.com/waf/managed-rules/) | Yes | Yes |   
[Waiting Room](https://developers.cloudflare.com/waiting-room/) | Yes | Yes |   
[WebSockets](https://developers.cloudflare.com/network/websockets/) | No | No |   
[Workers](https://developers.cloudflare.com/workers/) | Yes* | Yes | Similar to Page Rules, Workers that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.  
[Zaraz](https://developers.cloudflare.com/zaraz/) | Yes | No |   
  
[PreviousWP Engine](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/wpengine/)[NextRemove domain](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
