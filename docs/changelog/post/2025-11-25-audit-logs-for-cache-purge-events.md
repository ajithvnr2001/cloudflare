---
url: https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/
title: Audit Logs for Cache Purge Events \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.271458+00:00
---

# Audit Logs for Cache Purge Events · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2025

## Audit Logs for Cache Purge Events

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now review detailed audit logs for cache purge events, giving you visibility into what purge requests were sent, what they contained, and by whom. Audit your purge requests via the Dashboard or API for all purge methods:

  * Purge everything
  * List of prefixes
  * List of tags
  * List of hosts
  * List of files



#### Example

The detailed audit payload is visible within the Cloudflare Dashboard (under **Manage Account** > **Audit Logs**) and via the API. Below is an example of the Audit Logs v2 payload structure:
    
    
    {
      "action": {
        "result": "success",
        "type": "create"
      },
      "actor": {
        "id": "1234567890abcdef",
        "email": "user@example.com",
        "type": "user"
      },
      "resource": {
        "product": "purge_cache",
        "request": {
          "files": [
            "https://example.com/images/logo.png",
            "https://example.com/css/styles.css"
          ]
        }
      },
      "zone": {
        "id": "023e105f4ecef8ad9ca31a8372d0c353",
        "name": "example.com"
      }
    }

#### Get started

To get started, refer to the [Audit Logs documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).
