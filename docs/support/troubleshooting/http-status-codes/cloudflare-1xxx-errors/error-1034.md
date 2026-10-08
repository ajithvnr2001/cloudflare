---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1034/
title: Error 1034 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:57.977076+00:00
---

# Error 1034 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1034/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1034



# Error 1034

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1034/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1034: Edge IP Restricted Common causes

## Error 1034: Edge IP Restricted

This error indicates that the IP address used for the domain is restricted by Cloudflare's edge validation.

Edge IP Validation (EIV) is a safeguard for restricted IP space that is meant to be used by specific Cloudflare accounts, such as [BYOIP](https://developers.cloudflare.com/byoip/) prefixes, dedicated/[static](https://developers.cloudflare.com/byoip/concepts/static-ips/) IP allocations, or other customer-associated IP ranges. When EIV is enabled, Cloudflare checks whether incoming traffic to those IPs is associated with an authorized account before allowing the request to proceed. This helps prevent accidental misrouting or unauthorized use of dedicated IP space while keeping properly configured traffic flowing normally.

### Common causes

#### Pointing to reserved IP addresses

Customers who previously pointed their domains to `1.1.1.1` will now encounter a `1034` error. This is due to edge validation checks in Cloudflare's systems to prevent misconfiguration and potential abuse.

**Resolution** : Ensure DNS records are pointed to IP addresses you control. If a placeholder IP address is needed for "originless" setups, use the IPv6 reserved address `100::` or the IPv4 reserved address `192.0.2.0`.

#### SaaS provider IP restrictions

If you are using a SaaS provider that uses [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/), the provider may restrict access to their infrastructure to validated IP addresses only. In this case, requests to their IP addresses from domains that are not properly configured with the provider will be blocked with a `1034` error.

**Resolution** : Verify that your domain is correctly configured with your SaaS provider. This typically involves:

  1. Ensuring your DNS records point to the correct IP addresses or hostnames provided by your SaaS provider.
  2. Confirming that your domain has been properly registered and validated with the SaaS provider's platform.
  3. Contacting your SaaS provider's support team if you continue to experience this error after verifying your configuration.



#### Zone routing through a BYOIP address map from a different account

If your zone is a member of a Cloudflare [Address Map](https://developers.cloudflare.com/byoip/how-to/address-maps/) that contains IP addresses from a BYOIP prefix, and your Cloudflare account does not have access to that prefix, EIV will block all traffic to the zone with a `1034` error.

This typically happens when:

  * Your zone was previously onboarded to a third-party CDN or SaaS service that uses Cloudflare's infrastructure with their own BYOIP prefix, and the zone membership was not cleaned up when you stopped using the service.
  * Your zone was moved between Cloudflare accounts after being enrolled in a BYOIP address map.



**Resolution** :

  1. Go to **Cloudflare Dashboard** > **Account Home** > **Network** > **Address Maps** and look for any address map that lists your affected zone as a member. If the IP addresses in that map match what your zone currently resolves to, and those IPs are not in [Cloudflare's published IP ranges ↗︎](https://www.cloudflare.com/ips/), this cause applies.
  2. Select the address map that contains your zone.
  3. In the **Memberships** tab, find your zone and select **Remove**.
  4. Wait 1–2 minutes for the change to propagate, then test your domain.



If you cannot remove the zone yourself (for example, if the address map is owned by a third-party service that previously used your domain), contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) with the address map ID so we can investigate and assist.

[PreviousError 1033](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/)[NextError 1035](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1035/)

Was this helpful?

YesNo
