---
url: https://developers.cloudflare.com/client-side-security/reference/csp-header/
title: CSP HTTP header format \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.456671+00:00
---

# CSP HTTP header format · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/reference/csp-header/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /Reference
  4. /CSP HTTP header format



# CSP HTTP header format

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/reference/csp-header/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRelated resources

The format of the Content Security Policy (CSP) report-only HTTP header added by Cloudflare is the following:
    
    
    content-security-policy-report-only: script-src 'unsafe-inline' 'unsafe-eval'; connect-src 'none'; report-uri https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report?<QUERY_STRING>

If you [configured the reporting endpoint](https://developers.cloudflare.com/client-side-security/reference/settings/#reporting-endpoint) to use the same hostname, the HTTP header will have the following format:
    
    
    content-security-policy-report-only: script-src 'unsafe-inline' 'unsafe-eval'; connect-src 'none'; report-uri <YOUR_HOSTNAME>/cdn-cgi/script_monitor/report?<QUERY_STRING>

Notes

Cloudflare adds the CSP report-only HTTP header used to monitor webpage resources to a sample of sent responses.

Configuring [log rules](https://developers.cloudflare.com/client-side-security/rules/) will add other CSP report-only headers to responses. Cloudflare does not perform any sampling for these report-only headers related to customer-defined content security rules.

## Related resources

  * [Mozilla Developer Network's (MDN) documentation on Content-Security-Policy-Report-Only ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy-Report-Only)



[PreviousPCI DSS compliance](https://developers.cloudflare.com/client-side-security/reference/pci-dss/)[NextRoles and permissions](https://developers.cloudflare.com/client-side-security/reference/roles-and-permissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/reference/csp-header.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
