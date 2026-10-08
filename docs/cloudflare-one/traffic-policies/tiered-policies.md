---
url: https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/
title: Tiered policies \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:15.968748+00:00
---

# Tiered policies · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Traffic policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)
  4. /Tiered policies



# Tiered policies

Last updated Oct 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOrganizations vs. Tenant API

Note

Only available on Enterprise plans.

Gateway tiered policies allow you to share and enforce Gateway policies across multiple Zero Trust accounts. This enables centralized policy management for organizations that manage multiple accounts.

There are two approaches for setting up tiered policies, depending on your deployment model and policy requirements:

  * **[Cloudflare Organizations](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/)** — Share DNS, network, HTTP, and resolver policies across accounts in a Cloudflare Organization using the dashboard.
  * **[Tenant API](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/tenant-api/)** — Manage DNS policies across parent and child accounts for Managed Service Provider (MSP) deployments.



## Organizations vs. Tenant API

Feature | [Cloudflare Organizations](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/) | [Tenant API](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/tenant-api/)  
---|---|---  
**Supported policy types** | DNS, Network, HTTP, Resolver | DNS only  
**Account model** | Source / Recipient accounts | Parent / Child accounts  
**Shareable settings** | Block pages, extended email matching | Block pages  
**Setup** | Dashboard (self-serve) | API-only  
**Availability** | Enterprise | Enterprise (GA)  
  
[PreviousGranular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/)[NextCloudflare Organizations](https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/organizations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-policies/tiered-policies/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
