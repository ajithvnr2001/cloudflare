---
url: https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/
title: CASB introduces new granular roles \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:27.352148+00:00
---

# CASB introduces new granular roles · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2025

## CASB introduces new granular roles

[CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-28-casb-roles/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:

  * **Cloudflare CASB Read:** Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.
  * **Cloudflare CASB:** Provides full administrative access to configure and manage all aspects of the CASB product.



These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the **Super Administrator** or **Administrator** roles.

To enable [Data Loss Prevention (DLP)](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/), scans in CASB, account members will need the **Cloudflare Zero Trust** role.

You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under **Manage Account** > **Members**.

To learn more about managing roles and permissions, refer to the [Manage account members and roles documentation](https://developers.cloudflare.com/fundamentals/manage-members/roles/).
