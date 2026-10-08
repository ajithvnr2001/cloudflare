---
url: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/
title: Supported URL components in Bulk Redirects \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:59.520706+00:00
---

# Supported URL components in Bulk Redirects · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)[Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)

  4. /Reference
  5. /Supported URL components



# Supported URL components in Bulk Redirects

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/url-components/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The source and target URLs of a URL redirect support different URL components.

The provided URL component examples in the reference table are based on the following URL:
    
    
    https://user:password@www.example.com:443/search?q=term#results

URL component | Supported in source URL 1 | Supported in target URL  
---|---|---  
**Scheme**  
For example:  
`https` | Yes, `http` or `https` only  
(optional) | Yes  
**User information**  
For example:  
`user:password` | No | Yes (optional)  
**Host**  
For example:  
`www.example.com` | Yes | Yes (optional)  
**Port**  
For example:  
`443` | No | Yes (optional)  
**Path**  
For example:  
`/search` | Yes | Yes  
**Query string**  
For example:  
`q=term` | No | Yes, if [**Preserve query string**](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/#preserve-query-string) is `false` (optional)  
  
You can only add a query string to the target URL if you do not keep the original query string (that is, if **Preserve query string** is `false`). If you set **Preserve query string** to `true`, the query string of the request will be passed along [when there is a match for the source URL](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/#matching-the-source-url-of-redirects).  
**Fragment**  
For example:  
`results` | No | Yes (optional)  
  
Bulk Redirects also support target URLs without an authority component 2, like the following URL:
    
    
    magnet:?xt=urn:btih:2bd9d334e8d1e5bd7768755173222db5c6dea13b&dn=archlinux-2021.07.01-x86_64.iso

## Footnotes

  1. **Supported in source URL** = **No** means that you cannot include the component in the source URL to match against the URL of incoming requests. ↩

  2. The URL authority is the combination of user information, host, and port components. ↩




[PreviousURL redirect parameters](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/)[NextAvailable fields and functions](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/fields-functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/bulk-redirects/reference/url-components.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
