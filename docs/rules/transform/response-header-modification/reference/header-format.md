---
url: https://developers.cloudflare.com/rules/transform/response-header-modification/reference/header-format/
title: Format of HTTP response header names and values \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:57.952452+00:00
---

# Format of HTTP response header names and values · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/transform/response-header-modification/reference/header-format/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Transform Rules](https://developers.cloudflare.com/rules/transform/)[Modify response headers](https://developers.cloudflare.com/rules/transform/response-header-modification/)

  4. /Reference
  5. /Format of header names and values



# Format of HTTP response header names and values

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/transform/response-header-modification/reference/header-format/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The **name** of the HTTP response header you want to set or remove can only contain:

  * Alphanumeric characters: `a`-`z`, `A`-`Z`, and `0`-`9`
  * The following special characters: `-` and `_`



The **value** of the HTTP response header you want to set can only contain:

  * Alphanumeric characters: `a`-`z`, `A`-`Z`, and `0`-`9`
  * The following special characters: `_ :;.,\/"'?!(){}[]@<>=-+*#$&`|~^%`



The **length** of the HTTP response header can be a maximum of 4 KB (~4,096 characters).

[PreviousCreate a rule using Terraform ↗︎](https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/#create-a-response-header-transform-rule)[NextAvailable fields and functions](https://developers.cloudflare.com/rules/transform/response-header-modification/reference/fields-functions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/transform/response-header-modification/reference/header-format.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
