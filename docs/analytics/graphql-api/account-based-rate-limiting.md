---
url: https://developers.cloudflare.com/analytics/graphql-api/account-based-rate-limiting/
title: GraphQL API - Account-based rate limiting \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:12.164337+00:00
---

# GraphQL API - Account-based rate limiting · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/account-based-rate-limiting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)
  4. /Account-based rate limiting



# Account-based rate limiting

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/account-based-rate-limiting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBenefitsEnable account-based rate limitingLimitsQuery requirementsRequest higher limitsRate limit errors

By default, the GraphQL Analytics API applies rate limits per user or per API token. As you grow — adding more zones and accounts — all of your analytics traffic competes for that single per-credential quota.

**Account-based rate limiting** applies limits per account and per zone instead. Each account and zone gets its own independent budget, so a single user or token can query many resources at once without exhausting one shared quota. This is the recommended model if you query analytics across multiple zones or accounts.

## Benefits

  * **Scales with your footprint.** Throughput grows with the number of accounts and zones you query, instead of being capped by a single per-credential limit.
  * **Higher quotas for Enterprise.** Enterprise customers receive higher default per-account (15 rps) and per-zone (10 rps) quotas.
  * **Easy limit increases.** Need more headroom? Get in touch, we can accommodate needed increases to your limits.



## Enable account-based rate limiting

Send the following HTTP header with your requests to the existing GraphQL API endpoint (`https://api.cloudflare.com/client/v4/graphql`):
    
    
    X-Rate-Limit-Type: account-based

Your endpoint URL and credentials stay the same. Requests without this header continue to use the default per-user / per-token limits, so you can adopt this gradually.

## Limits

Scope | Default limit  
---|---  
Each account | 1 request per second (300 requests per 5-minute window)  
Each zone | 1 request per second (300 requests per 5-minute window)  
  
A single `accounts` block counts one request against the referenced account. A single `zones` block counts one request against the referenced zone; if the `zones` block is nested inside an `accounts` block, it counts against that account instead.

Because limits apply per resource, the total throughput available to one user or token scales with the number of distinct accounts and zones you query.

Note

If you send more than one request per second sustained to a **single** account or zone, request a higher limit for that resource (refer to Request higher limits).

## Query requirements

Most queries work unchanged. Only queries that select a **list** or **range** of zones at the top (`viewer`) level need adjusting: nest those zones inside a single `accounts` block. The adjusted queries are valid under **both** rate limiting models.

Querying a single zone — no change:
    
    
    {
      viewer {
        zones(filter: { zoneTag: "<ZONE_TAG>" }) {
          # ...
        }
      }
    }

Querying a single account — no change:
    
    
    {
      viewer {
        accounts(filter: { accountTag: "<ACCOUNT_TAG>" }) {
          # ...
        }
      }
    }

Querying a list or range of zones — nest inside the owning account:
    
    
    # Not supported: a list of zones at the viewer level
    {
      viewer {
        zones(filter: { zoneTag_in: ["<ZONE_A>", "<ZONE_B>"] }) {
          # ...
        }
      }
    }
    
    # Supported: the same zones nested inside their account
    {
      viewer {
        accounts(filter: { accountTag: "<ACCOUNT_TAG>" }) {
          zones(filter: { zoneTag_in: ["<ZONE_A>", "<ZONE_B>"] }) {
            # ...
          }
        }
      }
    }

The same applies to range filters such as `zoneTag_gt`. The query semantics are identical — you only need the account tag that owns the zones, which you already have.

## Request higher limits

If you need more than the default per-account or per-zone throughput, contact your Cloudflare account team to request an increase for the specific accounts and zones you query. Increases under this model are applied per resource and take effect quickly, without an engineering release.

## Rate limit errors

When a limit is exceeded, the API returns an error with `extensions.code` set to `budget`, naming the account or zone that was throttled:
    
    
    {
      "data": null,
      "errors": [
        {
          "extensions": { "code": "budget", "timestamp": "2026-01-01T01:01:01Z" },
          "message": "Account <ACCOUNT_TAG> has exceeded its rate limit. Please try again after 5 minutes. Refer to this page for more details about rate limits: https://developers.cloudflare.com/analytics/graphql-api/limits/",
          "path": null
        }
      ]
    }

The equivalent zone error reports `Zone <ZONE_TAG> has exceeded its rate limit`. Retry after the 5-minute window, spread traffic across resources, or request a higher limit.

[PreviousLimits](https://developers.cloudflare.com/analytics/graphql-api/limits/)[NextSampling](https://developers.cloudflare.com/analytics/graphql-api/sampling/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/account-based-rate-limiting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
