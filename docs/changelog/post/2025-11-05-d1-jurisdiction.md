---
url: https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/
title: D1 can restrict data localization with jurisdictions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.162970+00:00
---

# D1 can restrict data localization with jurisdictions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-05-d1-jurisdiction/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 5, 2025

## D1 can restrict data localization with jurisdictions

[D1](https://developers.cloudflare.com/d1/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set a [jurisdiction](https://developers.cloudflare.com/d1/configuration/data-location/) when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include `eu` and `fedramp`.

A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.
    
    
    npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<account_id>/d1/database" \
         -H "Authorization: Bearer $TOKEN" \
         -H "Content-Type: application/json" \
         --data '{"name": "db-with-jurisdiction", "jurisdiction": "eu" }'

To learn more, visit D1's data location [documentation](https://developers.cloudflare.com/d1/configuration/data-location/).
