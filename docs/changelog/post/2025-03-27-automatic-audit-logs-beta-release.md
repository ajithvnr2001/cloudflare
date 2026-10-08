---
url: https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/
title: Audit logs (version 2) - Beta Release \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:07.691673+00:00
---

# Audit logs (version 2) - Beta Release · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 27, 2025

## Audit logs (version 2) - Beta Release

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.

Availability: Audit logs (version 2) is now in Beta, with support limited to **API access**.

Use the following API endpoint to retrieve audit logs:
    
    
    GET https://api.cloudflare.com/client/v4/accounts/<account_id>/logs/audit?since=<date>&before=<date>

You can access detailed documentation for audit logs (version 2) Beta API release [here ↗︎](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/).

**Key Improvements in the Beta Release:**

  * **Automated & standardized logging**: Logs are now generated automatically using a standardized system, replacing manual, team-dependent logging. This ensures consistency across all Cloudflare services.

  * **Expanded product coverage** : Increased audit log coverage from 75% to 95%. Key API endpoints such as `/accounts`, `/zones`, and `/organizations` are now included.

  * **Granular filtering** : Logs now follow a uniform format, enabling precise filtering by actions, users, methods, and resources—allowing for faster and more efficient investigations.

  * **Enhanced context and traceability** : Each log entry now includes detailed context, such as the authentication method used, the interface (API or Dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for better traceability.

  * **Comprehensive activity capture** : Expanded logging to include GET requests and failed attempts, ensuring that all critical activities are recorded.




**Known Limitations in Beta**

  * Error handling for the API is not implemented.
  * There may be gaps or missing entries in the available audit logs.
  * UI is unavailable in this Beta release.
  * System-level logs and User-Activity logs are not included.



Support for these features is coming as part of the GA release later this year. For more details, including a sample audit log, check out our blog post: [Introducing Automatic Audit Logs ↗︎](https://blog.cloudflare.com/introducing-automatic-audit-logs/)
