---
url: https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/
title: Control API Access \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:21.141766+00:00
---

# Control API Access · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /How to
  5. /Control API Access



# Control API Access

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccount-level access controlMember-level access control

Super administrators of an Enterprise account are capable of selectively scoping the API access. API access can be restricted for the entire account or only for specified account members.

Note that the feature does not disable API calls not related to the Enterprise account.

## Account-level access control

To restrict the API access for the entire account:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. Locate the **Enable API Access** section and then update the setting.




## Member-level access control

Note

Member-level settings will override the account-level setting. If a specific member has API access enabled whereas the account has the access disabled, that member can still call APIs related to the Enterprise account.

To restrict the API access for a specific member:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. Click on the member to expand and choose the intended **API Access**. If `Account Default`, then it follows the account level setting.




[PreviousCreate tokens via API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/)[NextRestrict tokens](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/how-to/control-api-access.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
