---
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain/
title: Remove domain from SaaS provider \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:02.467861+00:00
---

# Remove domain from SaaS provider · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/)

  4. /[SaaS customers](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/)
  5. /Remove domain



# Remove domain

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If your SaaS domain is also a [domain using Cloudflare](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/), you can use your Cloudflare DNS to remove your domain from your SaaS provider.

This means that - if you [remove the DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records) pointing to your SaaS provider - Cloudflare will stop routing domain traffic through your SaaS provider and the associated custom hostname will enter a **Moved** state.

This also means that you need to keep DNS records pointing to your SaaS provider for as long as you are a customer. Otherwise, you could accidentally remove your domain from their services.

[PreviousProduct compatibility](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/)[NextConnection request details](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
