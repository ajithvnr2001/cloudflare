---
url: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-test-policy/
title: Create a test policy \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:46.580559+00:00
---

# Create a test policy · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-test-policy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Cybersafe

  4. /[Onboarding Cloudflare Gateway](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/)
  5. /Create a test policy



# Create a test policy

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-test-policy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTest a policy in the browser

To ensure a smooth deployment, we recommend testing a simple policy before deploying DNS filtering to your organization.

## Test a policy in the browser

  1. Go to **Traffic policies** > **Firewall policies**.
  2. Create a policy to block all security categories: 

Selector | Operator | Value | Action  
---|---|---|---  
Security Categories | in | _All security risks_ | Block  
  
  3. In the browser, go to `malware.testcategory.com`. You should see a generic Gateway block page.
  4. In **Logs** > **Gateway** > **DNS** , verify that you see the blocked domain.



Note

When testing against frequently-visited sites, you may need to [clear the DNS cache](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/#clear-dns-cache) in your browser or OS. Otherwise, the DNS lookup will return the locally-cached IP address and bypass your DNS policies.

You have now validated DNS filtering!

[PreviousVerify local connectivity](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-verify-local-connectivity/)[NextCreate CIPA policy](https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/cybersafe/gateway-onboarding/gateway-create-test-policy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
