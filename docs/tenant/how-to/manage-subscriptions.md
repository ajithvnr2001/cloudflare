---
url: https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/
title: Manage subscriptions \u00b7 Cloudflare Tenant docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:59.892522+00:00
---

# Manage subscriptions · Cloudflare Tenant docs

> Source: https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Tenant](https://developers.cloudflare.com/tenant/)
  3. /[How to](https://developers.cloudflare.com/tenant/how-to/)
  4. /Manage subscriptions



# Manage subscriptions

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tenant/how-to/manage-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewZone subscriptions Create zone subscription Get zone subscription details Update zone subscriptionAccount subscriptions Create account subscription Get account subscription details Update account subscription Delete account subscription

Once your customer has a zone provisioned, you can add zone and account-level subscriptions.

## Zone subscriptions

### Create zone subscription

To create a zone subscription, typically used to upgrade a zone's plan from `PARTNERS_FREE` to a paid [Zone plan](https://developers.cloudflare.com/tenant/reference/subscriptions/#zone-plans), send a [POST](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/create/) request to the `/zones/{zone_id}/subscription` endpoint and include the following values:

  * `rate_plan` object

    * Contains the zone plan corresponding to what customers would order in the dashboard. For a list of available values, refer to [Zone subscriptions](https://developers.cloudflare.com/tenant/reference/subscriptions/#zone-plans).
  * `component_values` array

    * Additional services depending on your reseller agreement, such as additional `page_rules`.
  * `frequency` string

    * How often the subscription is renewed automatically (defaults to `"monthly"`).

Request (without `component_values`)bash
    
    
    curl 'https://api.cloudflare.com/client/v4/zones/{zone_id}/subscription' \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "rate_plan": {
        "id": "<RATE_PLAN>"
      },
      "frequency": "annual"
    }'

Request (with `component_values`)bash
    
    
    curl 'https://api.cloudflare.com/client/v4/zones/{zone_id}/subscription' \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "rate_plan": {
        "id": "PARTNERS_BIZ"
      },
      "component_values": [
        {
          "name": "page_rules",
          "value": 50
        }
      ]
    }

### Get zone subscription details

To get the details of a zone subscription, send a [`GET`](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/get/) request to the `/zones/<ZONE_ID>/subscription` endpoint.

### Update zone subscription

To update a subscription on a zone, typically used to update an existing subscription's 'component_values' or to downgrade a zone's subscription, send a [`PUT`](https://developers.cloudflare.com/api/resources/zones/subresources/subscriptions/methods/update/) request to the `/zones/<ZONE_ID>/subscription` endpoint.

* * *

## Account subscriptions

Depending on your agreement, you may be allowed to resell other add-on services. These are provisioned as account-level subscriptions.

### Create account subscription

To create an account subscription, send a [POST](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/create/) request to the `/accounts/{account_id}/subscriptions` endpoint and include the following values:

  * `rate_plan` object

    * Contains the account subscription corresponding to a specific add-on service. For a list of available values, refer to [Available subscriptions](https://developers.cloudflare.com/tenant/reference/subscriptions/).
  * `component_values` array

    * Additional services depending on your reseller agreement, such as additional endpoints for load balancing or additional seats for Cloudflare Zero Trust. If not included, the subscription includes the default values associated with each purchase.
  * `frequency` string

    * How often the subscription is renewed automatically (defaults to `"monthly"`).

Requestbash
    
    
    curl 'https://api.cloudflare.com/client/v4/accounts/{account_id}/subscriptions' \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "rate_plan": {
        "id": "<RATE_PLAN_NAME>"
      }
    }'

### Get account subscription details

To get all subscriptions for an account, send a [`GET`](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/get/) request to the `/accounts/<ACCOUNT_ID>/subscriptions` endpoint.

### Update account subscription

To update a subscription on an account, send a [`PUT`](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/update/) request to the `/accounts/<ACCOUNT_ID>/subscriptions/<SUBSCRIPTION_ID>` endpoint.

### Delete account subscription

To delete a subscription on an account, send a [`DELETE`](https://developers.cloudflare.com/api/resources/accounts/subresources/subscriptions/methods/delete/) request to the `/accounts/<ACCOUNT_ID>/subscriptions/<SUBSCRIPTION_ID>` endpoint.

[PreviousManage accounts](https://developers.cloudflare.com/tenant/how-to/manage-accounts/)[NextGet account details](https://developers.cloudflare.com/tenant/how-to/get-account-details/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tenant/how-to/manage-subscriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
