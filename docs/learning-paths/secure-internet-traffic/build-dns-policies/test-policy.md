---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/
title: Test a policy \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:55.969849+00:00
---

# Test a policy · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Build DNS security policies](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/)
  5. /Test a policy



# Test a policy

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTest a policy in the browser

It is common for a misconfigured Gateway policy to accidentally block traffic to benign sites. To ensure a smooth deployment, we recommend testing a simple policy before deploying DNS filtering to your organization.

## Test a policy in the browser

  1. Go to **Traffic policies** > **Firewall policies**.
  2. Turn off all existing DNS policies.
  3. Turn on any existing security policies or create a policy to block all security categories: 

Selector | Operator | Value | Action  
---|---|---|---  
Security Categories | in | _All security risks_ | Block  
  
  4. Ensure that your browser is not configured to use an alternate DNS resolver. For example, Chrome has a **Use secure DNS** setting that will cause the browser to send requests to 1.1.1.1 and bypass your DNS policies.
  5. In the browser, go to `malware.testcategory.com`. Your browser will display: 
     * The Gateway block page, if your device is connected through the Cloudflare One Client in Traffic and DNS mode.
     * A generic error page, if your device is connected through another method, such as DNS only mode.



Note

[Custom block pages](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/gateway-block-page/) require you to install a root certificate on the device.

  6. In **Logs** > **Gateway** > **DNS** , verify that you see the blocked domain.
  7. Slowly turn on or add other policies to your configuration.
  8. When testing against frequently-visited sites, you may need to [clear the DNS cache](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/#clear-dns-cache) in your browser or OS. Otherwise, the DNS lookup will return the locally-cached IP address and bypass your DNS policies.



You have now validated DNS filtering on a test device.

[PreviousOnboard DNS for a network](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/onboard-dns/)[NextOverview](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-network-policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/build-dns-policies/test-policy.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
