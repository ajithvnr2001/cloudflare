---
url: https://developers.cloudflare.com/rules/transform/request-header-modification/reference/header-format/
title: Format of HTTP request header names and values \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:57.540906+00:00
---

# Format of HTTP request header names and values · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/request-header-modification/reference/header-format/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)[Modify request headers](https://developers.cloudflare.com/rules/transform/request-header-modification/)

  4. /Reference
  5. /Format of header names and values



# Format of HTTP request header names and values

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/header-format/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The **name** of the HTTP request header you want to set or remove can only contain:

  * Alphanumeric characters: `a`-`z`, `A`-`Z`, and `0`-`9`
  * The following special characters: `-` and `_`



The **value** of the HTTP request header you want to set can only contain:

  * Alphanumeric characters: `a`-`z`, `A`-`Z`, and `0`-`9`
  * The following special characters: `_ :;.,\/"'?!(){}[]@<>=-+*#$&`|~^%`



The maximum length of the HTTP request header value is 4 KB (~4,096 characters).

[PreviousCreate a rule using Terraform ↗︎](https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/#create-a-request-header-transform-rule)[NextAvailable fields and functions](https://developers.cloudflare.com/rules/transform/request-header-modification/reference/fields-functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/request-header-modification/reference/header-format.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
