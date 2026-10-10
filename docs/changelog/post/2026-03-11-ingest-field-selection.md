---
url: https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/
title: Ingest field selection for Log Explorer \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.544777+00:00
---

# Ingest field selection for Log Explorer · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-11-ingest-field-selection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 11, 2026

## Ingest field selection for Log Explorer

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.

Previously, ingesting logs often meant taking an "all or nothing" approach to data fields. With **Ingest Field Selection** , you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.

#### Key capabilities

  * **Granular control:** Select only the specific fields you need when enabling a new dataset.
  * **Dynamic updates:** Update fields for existing, already enabled logstreams at any time.
  * **Historical consistency:** Even if you disable a field later, you can still query and receive results for that field for the period it was captured.
  * **Data integrity:** Core fields, such as `Timestamp`, are automatically retained to ensure your logs remain searchable and chronologically accurate.



#### Example configuration

When configuring a dataset via the dashboard or API, you can define a specific set of fields. The `Timestamp` field remains mandatory to ensure data indexability.
    
    
    {
      "dataset": "firewall_events",
      "enabled": true,
      "fields": [
        "Timestamp",
        "ClientRequestHost",
        "ClientIP",
        "Action",
        "EdgeResponseStatus",
        "OriginResponseStatus"
      ]
    }

For more information, refer to the [Log Explorer documentation](https://developers.cloudflare.com/log-explorer/).
