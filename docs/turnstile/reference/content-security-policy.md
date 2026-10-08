---
url: https://developers.cloudflare.com/turnstile/reference/content-security-policy/
title: Content Security Policy \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:08.009305+00:00
---

# Content Security Policy · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/reference/content-security-policy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /Reference
  4. /Content Security Policy



# Content Security Policy

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/reference/content-security-policy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPre-clearance support

If your website uses a [Content Security Policy (CSP) ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) header, you must configure it to allow Turnstile's scripts and iframes. Without the correct CSP directives, Turnstile may fail to load.

Cloudflare recommends using the nonce-based approach documented with [CSP3 ↗︎](https://w3c.github.io/webappsec-csp/#framework-directive-source-list). Include your nonce in the `api.js` script tag and Turnstile will propagate it to dynamically loaded resources. Turnstile works with [`strict-dynamic` ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy#strict-dynamic).

Alternatively, add the following values to your CSP header:

  * **script-src** : `https://challenges.cloudflare.com`
  * **frame-src** : `https://challenges.cloudflare.com`



We recommend validating your CSP with [Google's CSP Evaluator ↗︎](https://csp-evaluator.withgoogle.com/).

Note

You cannot set your own CSP and/or Referer-Policy via meta tags or [Transform rules](https://developers.cloudflare.com/rules/transform/) in challenge pages.

## Pre-clearance support

If you are using [Turnstile in pre-clearance mode](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile), Turnstile sets the `cf_clearance` cookie by doing a fetch request to a special endpoint in [`/cdn-cgi/`](https://developers.cloudflare.com/fundamentals/reference/cdn-cgi-endpoint/) of your domain.

For this request to succeed, your `connect-src` directive must include `'self'`.

[PreviousWaiting Room Analytics ↗︎](https://developers.cloudflare.com/waiting-room/waiting-room-analytics/#turnstile-widget-traffic)[NextSupported languages](https://developers.cloudflare.com/turnstile/reference/supported-languages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/reference/content-security-policy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
