---
url: https://developers.cloudflare.com/tenant/how-to/get-tenant-details/
title: Get tenant details \u00b7 Cloudflare Tenant docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:59.604358+00:00
---

# Get tenant details · Cloudflare Tenant docs

> Source: https://developers.cloudflare.com/tenant/how-to/get-tenant-details/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Tenant](https://developers.cloudflare.com/tenant/)
  3. /[How to](https://developers.cloudflare.com/tenant/how-to/)
  4. /Get tenant details



# Get tenant details

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tenant/how-to/get-tenant-details/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A [**Tenant Admin**](https://developers.cloudflare.com/tenant/glossary/#tenant-admin)'s unit and membership details will be used for access of resources and all Tenant operations on the API. The unit ID (`unit_tag`), for example, can be used to create an account on a specific unit.

This is especially useful when a Tenant Admin has multiple units and wants to create an account on a specific unit. All accounts created are associated with the units, each of which can have one or more memberships.

To retrieve tenant details, send a `GET` request to the `/user/tenants` endpoint:

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/user/tenants" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

A successful request will return an HTTP status of `200` and a response body containing tenant information, unit information, memberships, and tenant entitlements for all tenants administered by the user.

[PreviousGet account details](https://developers.cloudflare.com/tenant/how-to/get-account-details/)[NextOverview](https://developers.cloudflare.com/tenant/reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tenant/how-to/get-tenant-details.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
