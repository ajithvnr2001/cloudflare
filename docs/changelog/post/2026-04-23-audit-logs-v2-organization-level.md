---
url: https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/
title: Audit Logs v2 \u2014 Organization-level support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:48.707972+00:00
---

# Audit Logs v2 — Organization-level support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 23, 2026

## Audit Logs v2 — Organization-level support

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Audit Logs v2 now supports organization-level audit logs. Org Admins can retrieve audit events for actions performed at the organization level via the Audit Logs v2 API.

To retrieve organization-level audit logs, use the following endpoint:
    
    
    GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit

This release covers user-initiated actions performed through organization-level APIs. Audit logs for system-initiated actions, a dashboard UI, and Logpush support for organizations will be added in future releases.

Note

Organization-level audit logs are separate from account-level audit logs. Actions performed within a specific account continue to be available via the account-level Audit Logs UI, Audit Logs v2 API, and Logpush.

For more information, refer to the [Audit Logs documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).
