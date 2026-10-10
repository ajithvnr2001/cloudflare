---
url: https://developers.cloudflare.com/changelog/post/2025-07-29-audit-logs-v2-ui-beta/
title: Audit logs (version 2) - UI Beta Release \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.558181+00:00
---

# Audit logs (version 2) - UI Beta Release · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-29-audit-logs-v2-ui-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 29, 2025

## Audit logs (version 2) - UI Beta Release

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Audit Logs v2 UI is now available to all Cloudflare customers in Beta. This release builds on the public [Beta of the Audit Logs v2 API](https://developers.cloudflare.com/changelog/product/audit-logs/) and introduces a redesigned user interface with powerful new capabilities to make it easier to investigate account activity.

**Enabling the new UI**

To try the new user interface, go to **Manage Account > Audit Logs**. The previous version of Audit Logs remains available and can be re-enabled at any time using the **Switch back to old Audit Logs** link in the banner at the top of the page.

**New Features:**

  * **Advanced Filtering** : Filter logs by actor, resource, method, and more for faster insights.
  * **On-hover filter controls** : Easily include or exclude values in queries by hovering over fields within a log entry.
  * **Detailed Log Sidebar** : View rich context for each log entry without leaving the main view.
  * **JSON Log View** : Inspect the raw log data in a structured JSON format.
  * **Custom Time Ranges** : Define your own time windows to view historical activity.
  * **Infinite Scroll** : Seamlessly browse logs without clicking through pages.

![Audit Logs v2 new UI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1300,height=686,format=webp/_astro/Audit_logs_v2_filters.Bacd1IHg.png)

For more details on Audit Logs v2, see the [Audit Logs documentation ↗︎](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

**Known issues**

  * A small number of audit logs may currently be unavailable in Audit Logs v2. In some cases, certain fields such as actor information may be missing in certain audit logs. We are actively working to improve coverage and completeness for General Availability.
  * Export to CSV is not supported in the new UI.



We are actively refining the Audit Logs v2 experience and welcome your feedback. You can share overall feedback by clicking the thumbs up or thumbs down icons at the top of the page, or provide feedback on specific audit log entries using the thumbs icons next to each audit log line or by filling out our [feedback form ↗︎](https://docs.google.com/forms/d/e/1FAIpQLSfXGkJpOG1jUPEh-flJy9B13icmcdBhveFwe-X0EzQjJQnQfQ/viewform?usp=sharing).
