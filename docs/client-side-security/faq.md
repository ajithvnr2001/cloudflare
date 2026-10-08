---
url: https://developers.cloudflare.com/client-side-security/faq/
title: Client-side security FAQ \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.309897+00:00
---

# Client-side security FAQ · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /FAQ



# Client-side security FAQ

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/faq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat happens to CSP HTTP headers set by the origin server when I create a content security rule?Can I add a nonce CSP directive to a content security rule?

## What happens to CSP HTTP headers set by the origin server when I create a content security rule?

When you create content security rules, Cloudflare will generate content security policy (CSP) directives from those rules based on their configuration:

  * Log rules will create CSP directives for the `Content-Security-Policy-Report-Only` HTTP header.
  * Allow rules will create CSP directives for the `Content-Security-Policy` HTTP header.



Client-side security only adds new CSP HTTP headers to the response. This means that Cloudflare will keep any `Content-Security-Policy-Report-Only` and `Content-Security-Policy` HTTP headers in the response set by the origin server and it will add separate HTTP headers for the content security rules configured on your Cloudflare zone.

It is recommended that you only have one rule in [allow mode](https://developers.cloudflare.com/client-side-security/rules/#rule-actions) (that is, a content security rule being enforced). If there is more than one `Content-Security-Policy` HTTP header in the response, the most restrictive policy wins. For more information, refer to the [MDN documentation ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy#multiple_content_security_policies).

## Can I add a `nonce` CSP directive to a content security rule?

Client-side security currently does not support [`nonce` ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP#nonces) directives in content security rules. Instead, you can use a [`hash` ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP#hashes) CSP directive. For details on the supported directives and values, refer to [Supported CSP directives](https://developers.cloudflare.com/client-side-security/rules/csp-directives/).

[PreviousClient-side security API](https://developers.cloudflare.com/client-side-security/reference/api/)[NextTroubleshooting](https://developers.cloudflare.com/client-side-security/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
