---
url: https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/
title: Flagship API reference now available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:57.413151+00:00
---

# Flagship API reference now available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 10, 2026

## Flagship API reference now available

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-10-api-reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The **[Flagship API reference](https://developers.cloudflare.com/api/resources/flagship/)** is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.

For example, create a new boolean flag with the API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      -d '{
        "key": "new-checkout",
        "enabled": true,
        "default_variation": "off",
        "variations": {
          "off": false,
          "on": true
        },
        "rules": []
      }'

To create an API token, go to [Account API Tokens ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens) in the Cloudflare dashboard and search for Flagship.

The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the [Flagship reference in the Cloudflare skill ↗︎](https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship) to create and manage Flagship resources.

Refer to the [Flagship documentation](https://developers.cloudflare.com/flagship/) to learn more about evaluating feature flags from your applications.
