---
url: https://developers.cloudflare.com/changelog/post/2025-06-23-user-groups-ga/
title: Cloudflare User Groups & SCIM User Groups are now in GA \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:14.951784+00:00
---

# Cloudflare User Groups & SCIM User Groups are now in GA · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-23-user-groups-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 23, 2025

## Cloudflare User Groups & SCIM User Groups are now in GA

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-23-user-groups-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're announcing the GA of **User Groups for Cloudflare Dashboard** and **System for Cross Domain Identity Management (SCIM) User Groups** , strengthening our RBAC capabilities with stable, production-ready primitives for managing access at scale.

**What's New**

**User Groups [GA]** : [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.

**SCIM User Groups [GA]** : Centralize & simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.

**Stability & Scale**: These features have undergone extensive testing during the Public Beta period and are now ready for production use across enterprises of all sizes.

Note

SCIM Virtual Groups (identified by the pattern `CF-<accountID>-<Role Name>` in your IdP) are now officially deprecated as of June 2, 2025. SCIM Virtual Groups end-of-life will take effect on December 2, 2025. We strongly recommend migrating to SCIM User Groups to ensure continued support for SCIM synchronization to the Cloudflare Dashboard. If you haven’t used Virtual Groups, no action is required.

For more info:

  * [Get started with User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/)
  * [Explore our SCIM integration guide](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)


