---
url: https://developers.cloudflare.com/ohttp-relay/reference/product-compatibility/
title: Product compatibility \u00b7 Cloudflare OHTTP Relay docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:27.908877+00:00
---

# Product compatibility · Cloudflare OHTTP Relay docs

> Source: https://developers.cloudflare.com/ohttp-relay/reference/product-compatibility/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare OHTTP Relay](https://developers.cloudflare.com/ohttp-relay/)
  3. /[Reference](https://developers.cloudflare.com/ohttp-relay/reference/)
  4. /Product compatibility



# Product compatibility

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ohttp-relay/reference/product-compatibility/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When [using Cloudflare OHTTP Relay (formerly Privacy Gateway)](https://developers.cloudflare.com/ohttp-relay/get-started/), the majority of Cloudflare products will be compatible with your application.

However, the following products are not compatible:

  * [API Shield](https://developers.cloudflare.com/api-shield/): [Schema Validation](https://developers.cloudflare.com/api-shield/security/schema-validation/) and [API discovery](https://developers.cloudflare.com/api-shield/security/api-discovery/) are not possible since Cloudflare cannot see the request URLs.
  * [Cache](https://developers.cloudflare.com/cache/): Caching of application content is no longer possible since each between client and gateway is end-to-end encrypted.
  * [WAF](https://developers.cloudflare.com/waf/): Rules implemented based on request content are not supported since Cloudflare cannot see the request or response content.



[PreviousCloudflare OHTTP Relay metrics](https://developers.cloudflare.com/ohttp-relay/reference/metrics/)[NextLegal](https://developers.cloudflare.com/ohttp-relay/reference/legal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ohttp-relay/reference/product-compatibility.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
