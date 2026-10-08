---
url: https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/
title: Archive and audit security action items \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:49.034082+00:00
---

# Archive and audit security action items · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 20, 2026

## Archive and audit security action items

[Security Overview](https://developers.cloudflare.com/security/overview/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-27-archive-and-audit-security-action-items/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Archive and audit security action items

Introducing enhanced archiving capabilities for security action items within the Security Overview dashboard. This update allows security teams to maintain a cleaner workspace by removing resolved, accepted, or irrelevant items from their active list while maintaining a clear paper trail for compliance.

* * *

#### Why this matters

Managing a high volume of security insights can be overwhelming. Previously, users lacked a structured way to dismiss items without losing the context of why they were ignored.

With these new archiving options—**False Positive** , **Accept Risk** , and **Other** —you can now suppress items indefinitely with required rationale text for risk-based decisions. This ensures that your team remains focused on critical, actionable vulnerabilities while preserving institutional knowledge for audits.

#### Key features

  * **Structured Archiving:** Choose from specific categories to define why an action item is being moved.
  * **Required Rationale:** For "Accept Risk" and "Other" categories, users must provide documentation, ensuring accountability for security decisions.
  * **Audit Log Transparency:** New API endpoints allow you to programmatically retrieve the history of status changes and rationale for any insight at the account or zone level.
  * **Reversible Actions:** Any archived item can be moved back to the active list at any time if the security context changes.



:::note Archiving a suspicious activity item will remove it from the Security Overview page, but the activity will remain visible in your Security Analytics dashboard for deeper forensic analysis. :::

* * *

#### Example: Retrieve audit logs via API

To review the history and rationale of a specific archived issue at the account level, you can use the following API command:
    
    
    curl "[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){account_id}/insights/{insight_id}/audit-log" \
         -H "Authorization: Bearer <API_TOKEN>" \
         -H "Content-Type: application/json"
