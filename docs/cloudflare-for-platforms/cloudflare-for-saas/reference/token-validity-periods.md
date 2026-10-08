---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods/
title: Token validity periods \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:01.005040+00:00
---

# Token validity periods · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /Reference
  5. /Token validity periods



# Token validity periods

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you perform [TXT](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/) domain control validation, you will need to share these tokens with your customers.

However, these tokens expire after a certain amount of time, depending on your chosen certificate authority.

Certificate authority | Token validity  
---|---  
Let's Encrypt | 7 days  
Google Trust Services | 14 days  
SSL.com | 14 days  
  
Caution

Tokens may also become invalid upon validation failure. For more details, refer to [Domain control validation flow](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/#dcv-tokens).

[PreviousCustom CSRs](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-csrs/)[NextDeprecation - Version 1](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
