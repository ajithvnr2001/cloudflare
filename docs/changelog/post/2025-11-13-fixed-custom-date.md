---
url: https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/
title: Fixed custom SQL date picker inconsistencies \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:29.263447+00:00
---

# Fixed custom SQL date picker inconsistencies · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 13, 2025

## Fixed custom SQL date picker inconsistencies

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-13-fixed-custom-date/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We've resolved a bug in Log Explorer that caused inconsistencies between the custom SQL date field filters and the date picker dropdown. Previously, users attempting to filter logs based on a custom date field via a SQL query sometimes encountered unexpected results or mismatching dates when using the interactive date picker.

This fix ensures that the custom SQL date field filters now align correctly with the selection made in the date picker dropdown, providing a reliable and predictable filtering experience for your log data. This is particularly important for users creating custom log views based on time-sensitive fields.
