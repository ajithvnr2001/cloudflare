---
url: https://developers.cloudflare.com/api-shield/plans/
title: Plans \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:18.016091+00:00
---

# Plans · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/plans/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /Plans



# Plans

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/plans/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed beta access does not imply future plan availability or pricing.

To subscribe to API Shield, upgrade to an Enterprise plan and contact your account team.

Existing operation and uploaded schema limits remain based on your zone plan. These limits do not determine Application Profiles availability.

The uploaded schema allowance counts schemas enabled for validation. Cloudflare calculates schema size after processing an upload, so it may differ from the original file size.

Plan type | Saved endpoints | Enabled uploaded schemas | Combined size of enabled schemas | Rule action  
---|---|---|---|---  
**Free** | 100 | 5 | 200 KiB | `Block` only  
**Pro** | 250 | 5 | 500 KiB | `Block` only  
**Business** | 500 | 10 | 2 MiB | `Block` only  
**Enterprise without API Shield** | 3000 | 10 | 5 MiB | `Log` or `Block`  
**Enterprise with API Shield** | 10,000 | 10 | 10+ MiB | `Log` or `Block`  
  
[PreviousGet started](https://developers.cloudflare.com/api-shield/get-started/)[NextOverview](https://developers.cloudflare.com/api-shield/security/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/plans.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
