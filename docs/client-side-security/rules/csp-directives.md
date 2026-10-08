---
url: https://developers.cloudflare.com/client-side-security/rules/csp-directives/
title: Supported CSP directives \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:58.231345+00:00
---

# Supported CSP directives · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/rules/csp-directives/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /[Rules](https://developers.cloudflare.com/client-side-security/rules/)
  4. /Supported CSP directives



# Supported CSP directives

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/rules/csp-directives/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMore resources

[Content security rules](https://developers.cloudflare.com/client-side-security/rules/) support most Content Security Policy (CSP) directives, covering both monitored and unmonitored resources. You can use a content security rule to control other types of resources besides scripts and their connections, even though Cloudflare is not monitoring these resources.

Each CSP directive can contain multiple values, including:

  * Schemes
  * Hostnames
  * URIs
  * Special keywords between single quotes (for example, `'none'`)
  * Hashes between single quotes (for example, `'sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC'`)



Hostname and URI values support a `*` wildcard for the leftmost subdomain.

The following table lists the supported CSP directives and special values you can use in content security rules:

Directive | Name in the dashboard | Supported special values | Monitored  
---|---|---|---  
`script-src` | Scripts | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | [Yes](https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/)  
`connect-src` | Connections | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | [Yes](https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/)  
`default-src` | Default | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`img-src` | Images | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`style-src` | Styles | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`font-src` | Fonts | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`object-src` | Objects | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`media-src` | Media | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`child-src` | Child | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`form-action` | Form actions | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`worker-src` | Workers | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`base-uri` | Base URI | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`manifest-src` | Manifests | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`frame-src` | Frames | `'none'`  
`'self'`  
`'unsafe-inline'`  
`'unsafe-eval'`  
`'<HASH>'` | No  
`frame-ancestors` | Frame ancestors | `'none'`  
`'self'` | No  
`upgrade-insecure-requests` | Upgrade insecure requests | N/A | No  
  
## More resources

For more information on CSP directives and their values, refer to the following resources in the MDN documentation:

  * [Content-Security-Policy response header ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
  * [CSP guide ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)



[PreviousRule violations](https://developers.cloudflare.com/client-side-security/rules/violations/)[NextHandle an alert](https://developers.cloudflare.com/client-side-security/best-practices/handle-an-alert/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/rules/csp-directives.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
