---
url: https://developers.cloudflare.com/tenant/how-to/get-account-details/
title: Get account details \u00b7 Cloudflare Tenant docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:59.587285+00:00
---

# Get account details · Cloudflare Tenant docs

> Source: https://developers.cloudflare.com/tenant/how-to/get-account-details/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Tenant](https://developers.cloudflare.com/tenant/)
  3. /[How to](https://developers.cloudflare.com/tenant/how-to/)
  4. /Get account details



# Get account details

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tenant/how-to/get-account-details/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

An [**Account**](https://developers.cloudflare.com/tenant/glossary/#account) will contain various settings, resources, and subscriptions to products for users. Each Tenant can have multiple associated accounts.

To retrieve a list of accounts associated with a Tenant details, send a `GET` request to the `/tenants/{tenant_id}/accounts` endpoint. You can find the Tenant tag and all Tenants associated with the user with the [**Tenant Details**](https://developers.cloudflare.com/tenant/how-to/get-tenant-details/) API. The Tenant Accounts API also requires pagination passed as query parameters:

  * `page` number

    * Page number of accounts list response, indexed from 1
  * `per_page` number

    * Number of accounts to display per page
  * `order` string

    * (optional) Order by a specific column, has to be a valid top-level key from the response

    * `direction` number

      * (optional) 0 for ascending or 1 for descending, is 0 by default

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/tenants/{tenant_id}/accounts?page=1&per_page=10" \
    --header "X-Auth-Email: <EMAIL>" \
    --header "X-Auth-Key: <API_KEY>"

A successful request will return an HTTP status of `200` and a response body containing account information and feature flags for all accounts managed by the Tenant.

[PreviousManage subscriptions](https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/)[NextGet tenant details](https://developers.cloudflare.com/tenant/how-to/get-tenant-details/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tenant/how-to/get-account-details.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
