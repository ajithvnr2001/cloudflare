---
url: https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/
title: Validate Rulesets changes before deployment \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:14.858976+00:00
---

# Validate Rulesets changes before deployment · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 17, 2026

## Validate Rulesets changes before deployment

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-17-rulesets-dry-run-validation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Rules now validates ruleset changes before deployment, helping you catch invalid expressions, action parameters, permission issues, unavailable features, and quota limits without publishing the configuration.

The Cloudflare dashboard performs this validation automatically when you create or update rules from **Security** > **Security rules** or **Rules** > **Overview**.

Supported Rulesets API mutation endpoints now also accept the `dry_run=true` query parameter. A dry run performs the same authorization and server-side validation checks as the requested change, but does not persist or publish it. Successful operations that normally return a `200` response return `result: null`. Operations that normally return `204` continue to do so.

#### API example

Add `dry_run=true` to a Rulesets API request to validate it without creating the ruleset:
    
    
    curl --request POST \
      "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets?dry_run=true" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Custom firewall rules",
        "kind": "zone",
        "phase": "http_request_firewall_custom",
        "rules": [
          {
            "action": "block",
            "expression": "ip.src.country eq \"GB\"",
            "description": "Block requests from the United Kingdom",
            "enabled": true
          }
        ]
      }'

For more information, refer to [Validate rule changes before deployment](https://developers.cloudflare.com/ruleset-engine/rulesets-api/dry-run/).
