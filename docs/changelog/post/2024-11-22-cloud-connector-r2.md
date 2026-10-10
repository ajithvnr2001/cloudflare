---
url: https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/
title: Cloud Connector Now Supports R2 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.785206+00:00
---

# Cloud Connector Now Supports R2 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-11-22-cloud-connector-r2/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 22, 2024

## Cloud Connector Now Supports R2

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, you can use [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) to route traffic to your [R2 buckets](https://developers.cloudflare.com/r2/) based on URLs, headers, geolocation, and more.

Example setup:
    
    
    curl --request PUT \
    "https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '[
      {
        "expression": "http.request.uri.path wildcard \"/images/*\"",
        "provider": "cloudflare_r2",
        "description": "Connect to R2 bucket containing images",
        "parameters": {
          "host": "mybucketcustomdomain.example.com"
        }
      }
    ]'

Get started using [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/) documentation.
