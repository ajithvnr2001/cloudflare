---
url: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/
title: Create CIPA policy \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:46.470429+00:00
---

# Create CIPA policy · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Cybersafe

  4. /[Onboarding Cloudflare Gateway](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/)
  5. /Create CIPA policy



# Create CIPA policy

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate CIPA policy

## Create CIPA policy

  1. Go to **Traffic policies** > **Firewall policies**.

  2. Create a policy to block using the CIPA filter:

Selector | Operator | Value | Action  
---|---|---|---  
Content Categories | in | _CIPA Filter_ | Block  
  
  3. In **Logs** > **Gateway** > **DNS** , verify that you see the blocked domain.




Your environment is now protected against all of the subcategories listed in [Configuration](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/#configuration).

[PreviousCreate a test policy](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-test-policy/)[NextBlock pages](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-block-pages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
