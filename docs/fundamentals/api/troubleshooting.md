---
url: https://developers.cloudflare.com/fundamentals/api/troubleshooting/
title: Troubleshooting \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:21.851124+00:00
---

# Troubleshooting · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /Cloudflare's API
  4. /Troubleshooting



# Troubleshooting

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/api/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewThe token is not verifiedThe token has incorrect permissionsThe incorrect syntax is usedYou have the incorrect user permissions

## The token is not verified

Ensure the token has been verified by running the following `curl` command and confirming that the response returns `"status": "active"`.
    
    
    curl "https://api.cloudflare.com/client/v4/user/tokens/verify" \
    --header "Authorization: Bearer <API_TOKEN>"
    
    
    {
      "success": true,
      "errors": [],
      "messages": [],
      "result": {
        "id": "f267e341f3dd4697bd3b9f71dd96247f",
        "status": "active",
        "not_before": "2018-07-01T05:20:00Z",
        "expires_on": "2020-01-01T00:00:00Z"
      }
    }

## The token has incorrect permissions

Review the permissions groups for your token in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/profile/api-tokens). Refer to [API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) for more information.

## The incorrect syntax is used

Occasionally customers will attempt to use an API token with an API key syntax. Ensure you are using the Bearer option rather than the email and API key pair.

## You have the incorrect user permissions

You cannot create a token that exceeds the permission granted to you on your account. For example, if you have been granted an **Admin (Read only)** role, you would need your Super Administrator to update your role so that you could create a token for yourself.

[PreviousSDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)[NextOverview](https://developers.cloudflare.com/fundamentals/oauth/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
