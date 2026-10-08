---
url: https://developers.cloudflare.com/tenant/reference/subscriptions/
title: Available subscriptions \u00b7 Cloudflare Tenant docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:59.955787+00:00
---

# Available subscriptions · Cloudflare Tenant docs

> Source: https://developers.cloudflare.com/tenant/reference/subscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Tenant](https://developers.cloudflare.com/tenant/)
  3. /[Reference](https://developers.cloudflare.com/tenant/reference/)
  4. /Available subscriptions



# Available subscriptions

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tenant/reference/subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewZone plansOther subscriptions Zero Trust subscriptions Developer subscriptions Application performance and security Network servicesGetting new subscriptions

When [provisioning services for an account](https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/), you need to include certain values with each API call to specify a particular service.

The subscriptions available to you will vary depending on your current partner program ([Agency Partner Program ↗︎](https://www.cloudflare.com/cloudflare-partners-self-serve-program-closed-beta/) or [Enterprise Resellers and MSP Program ↗︎](https://portal.cloudflarepartners.com)).

The following values are samples and not exhaustive. For the complete list of subscription values available to you, make an API call to the [zone subscriptions](https://developers.cloudflare.com/api/resources/zones/subresources/rate_plans/methods/get/) or [account subscriptions](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/get/) endpoints.

## Zone plans

When creating or updating a [zone plan](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/get/), Partners can use one of the following values for the `id` of the `rate_plan` field (which controls the zone-level plan subscription).

Partner program | Available subscriptions  
---|---  
Enterprise and self-serve resellers | `PARTNERS_FREE`, `PARTNERS_PRO`, `PARTNERS_BIZ`, `PARTNERS_ENT`  
Agency partners | `CF_FREE`, `CF_PRO_20_20`, `CF_BIZ`  
MSP partners | `msp_biz`  
  
## Other subscriptions

When you [create an account subscription](https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/#account-subscriptions), it provisions an add-on service for that account.

### Zero Trust subscriptions

The following table lists sample values for various Zero Trust subscriptions.

Feature | Subscription IDs  
---|---  
[Access](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) | `PARTNERS_ACCESS_BASIC`, `PARTNERS_ACCESS_ENT`, `PARTNERS_ACCESS_PREMIUM`, `TEAMS_ACCESS_ENT`, `TEAMS_ACCESS`  
[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) | `TEAMS_GATEWAY_ENT`, `TEAMS_GATEWAY`  
[Cloudflare Zero Trust](https://developers.cloudflare.com/cloudflare-one/) | `TEAMS_ENT`, `TEAMS_FREE`, `TEAMS_STANDARD`  
  
### Developer subscriptions

The following table lists sample values for various Developer platform subscriptions.

Feature | Subscription IDs  
---|---  
[Images](https://developers.cloudflare.com/images/) | `IMAGES_ENT`,`IMAGES_BASIC`  
[Image transformations](https://developers.cloudflare.com/images/optimization/transformations/overview/) | `IMAGE_RESIZING_ENT`, `IMAGE_RESIZING_BASIC`  
[Stream](https://developers.cloudflare.com/stream/) | `PARTNERS_STREAM_ENT`, `PARTNERS_STREAM_BASIC`, `STREAM_BASIC`  
[Workers](https://developers.cloudflare.com/workers) | `PARTNERS_WORKERS_ENT`, `WORKERS_PAID`, `PARTNERS_WORKERS_SS`, `PARTNERS_WORKERS_BASIC`  
  
### Application performance and security

The following table lists sample values for various application performance and security subscriptions.

Feature | Subscription IDs  
---|---  
[API Shield](https://developers.cloudflare.com/api-shield/) | `API_SHIELD_ZONE`  
[Advanced certificate manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) | `ADVANCED_CERT_MANAGER_FREE`, `ADVANCED_CERT_MANAGER`  
[Argo smart routing](https://developers.cloudflare.com/argo-smart-routing/) | `PARTNERS_ZONE_ARGO`, `ARGO_ZONE_BASIC`  
[Ethereum gateway](https://developers.cloudflare.com/web3/ethereum-gateway/) | `WEB3_ETHEREUM_ENT`, `WEB3_ETHEREUM_ENT_CONTRACT`, `WEB3_ETHEREUM_ENT_PAYGO`  
[IPFS gateway](https://developers.cloudflare.com/web3/ipfs-gateway/) | `WEB3_IPFS_ENT`, `WEB3_IPFS_ENT_CONTRACT`, `WEB3_IPFS_ENT_PAYGO`  
[Load balancing](https://developers.cloudflare.com/load-balancing/) | `PARTNERS_LOAD_BALANCING`, `PARTNERS_LOAD_BALANCING_ENT`, `LOAD_BALANCING_BASIC_PLUS`  
[Rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) | `PARTNERS_RATE_LIMITING`  
[Spectrum](https://developers.cloudflare.com/spectrum/) | `PARTNERS_SPECTRUM`  
[Waiting Room](https://developers.cloudflare.com/waiting-room/) | `WAITING_ROOMS_BASIC`, `WAITING_ROOMS_ADV`  
  
### Network services

The following table lists sample values for various network services subscriptions.

Feature | Subscription IDs  
---|---  
[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) | `MAGIC_FIREWALL_BASIC`, `MAGIC_FIREWALL_ADVANCED`  
[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) | `MAGIC_WAN`  
  
## Getting new subscriptions

If your reseller plan does not have access to a specific subscription, you will receive the following error when making an API call:
    
    
    "errors": [
            {
                "code": 1225,
                "message": "Your account does not have access to this product. Contact billing@cloudflare.com for assistance."
            }
    ]

To change your program or - in some cases - get a specific subscription added to your reseller plan, contact `partners@cloudflare.com`. Agency Partners should contact [agency@cloudflare.com](mailto:agency@cloudflare.com)

[PreviousOverview](https://developers.cloudflare.com/tenant/reference/)[NextGlossary](https://developers.cloudflare.com/tenant/glossary/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tenant/reference/subscriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
