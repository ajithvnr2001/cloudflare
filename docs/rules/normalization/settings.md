---
url: https://developers.cloudflare.com/rules/normalization/settings/
title: URL normalization settings \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:49.361499+00:00
---

# URL normalization settings · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/normalization/settings/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[URL normalization](https://developers.cloudflare.com/rules/normalization/)
  4. /Settings



# URL normalization settings

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/normalization/settings/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNormalization typeNormalize incoming URLsNormalize URLs to origin

The Cloudflare dashboard provides the following settings to manage URL normalization:

## Normalization type

Default value: _RFC-3986_

Selects the type of normalization to perform:

  * _RFC-3986_ – Applies URL normalization strictly according to [RFC 3986 ↗︎](https://datatracker.ietf.org/doc/html/rfc3986).
  * _Cloudflare_ – In addition to what is defined in RFC 3986, applies [extra URL normalization techniques](https://developers.cloudflare.com/rules/normalization/how-it-works/#cloudflare-normalization).



## Normalize incoming URLs

Default value: _On_

Configures the URLs of all incoming traffic to Cloudflare:

  * When enabled, all incoming URLs are normalized before they pass to subsequent Cloudflare features that can receive a URL as input, such as Page Rules, WAF custom rules, Workers, and Access.
  * When disabled, incoming URLs are not normalized before passing to subsequent Cloudflare features.



## Normalize URLs to origin

Default value: _Off_

Configures URLs sent to the origin:

  * When enabled, requests sent to the origin are normalized.
  * When disabled, requests sent to the origin are not modified.



You can only view and enable this option when **Normalize incoming URLs** is enabled.

For examples of how these settings affect URL normalization, refer to the [URL normalization examples](https://developers.cloudflare.com/rules/normalization/examples/).

[PreviousConfigure in the dashboard](https://developers.cloudflare.com/rules/normalization/manage/)[NextExamples](https://developers.cloudflare.com/rules/normalization/examples/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/normalization/settings.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
