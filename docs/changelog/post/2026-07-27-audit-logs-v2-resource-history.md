---
url: https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/
title: Audit Logs v2 \u2014 Resource History \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:04.832203+00:00
---

# Audit Logs v2 — Resource History · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 27, 2026

## Audit Logs v2 — Resource History

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Audit Logs v2 now includes **Resource History**. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.

Resource History uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.

![Resource History in Audit Logs v2](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1578,height=840,format=webp/_astro/Audit_logs_v2_resource_history.tpxHc9ML.png)

**Dashboard:**

  1. Go to **Manage Account** > **Audit Logs**.
  2. Open any audit log entry.
  3. Select the **History** tab to see the full history for that resource.
  4. Select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.



**API:**

Use the History endpoint to retrieve the change history for any audit log entry:
    
    
    GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history

The endpoint is also available for organization-scoped audit logs at `/organizations/{organization_id}/logs/audit/{id}/history`.

For more information, refer to the [Resource History documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/#resource-history).
