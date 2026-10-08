---
url: https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/
title: SCIM audit logging Support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:41.308956+00:00
---

# SCIM audit logging Support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 18, 2026

## SCIM audit logging Support

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare dashboard SCIM provisioning operations are now captured in [Audit Logs v2](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/), giving you visibility into user and group changes made by your identity provider.

![SCIM audit logging](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2556,height=1332,format=webp/_astro/2026-03-18-scim-audit-logging.DPKMiE8X.png)

**Logged actions:**

Action Type | Description  
---|---  
Create SCIM User | User provisioned from IdP  
Replace SCIM User | User fully replaced (PUT)  
Update SCIM User | User attributes modified (PATCH)  
Delete SCIM User | Member deprovisioned  
Create SCIM Group | Group provisioned from IdP  
Update SCIM Group | Group membership or attributes modified  
Delete SCIM Group | Group deprovisioned  
  
For more details, refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).
