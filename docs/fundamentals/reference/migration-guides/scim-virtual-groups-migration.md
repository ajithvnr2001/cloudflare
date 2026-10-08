---
url: https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/
title: SCIM v1 to v2 Migration \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:25.966082+00:00
---

# SCIM v1 to v2 Migration · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Reference

  4. /Migration guides
  5. /SCIM migration



# SCIM v1 to v2 Migration

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMigration stepsMore resources

Cloudflare's first iteration of SCIM integration introduced a concept called _Virtual Groups_ , typically identified by the pattern `CF-<accountID>-<Role Name>` in your IdP. Virtual Groups were an early implementation of group-based access control: they acted as placeholders created automatically by SCIM to map IdP groups to account memberships.

While customers could add or remove members from these groups within their IdP, Virtual Groups had important limitations:

  * They could not be renamed or deleted in the IdP.
  * They could not be managed within Cloudflare.
  * Functionally, managing a Virtual Group was equivalent to syncing users and editing each member’s policies individually.



With the GA of [User Groups](https://developers.cloudflare.com/changelog/2025-06-23-user-groups-ga/), Virtual Groups are now deprecated. Customers should migrate to [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/), which provide a more flexible and scalable way to assign and manage policies. To maintain SCIM synchronization with the Cloudflare Dashboard, we strongly recommend migrating to **SCIM User Groups**.

If you have never synced a group linked to a `CF-<accountID>-<Role Name>` Virtual Group from your IdP to Cloudflare, no action is needed.

## Migration steps

  1. **Create a new SCIM integration** in your IdP using an [Account Owned Token](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/) provisioned in Cloudflare.
  2. **Assign users & groups to your new Application** in your IdP, following a naming convention that aligns with your internal processes.
  3. **Sync groups to Cloudflare** and verify they appear in the **User Groups** pane of the Cloudflare Dashboard.
  4. **Attach permission policies** to the new User Groups so members inherit the correct access upon assignment to the group.
  5. **Migrate users** into the new groups incrementally, testing synchronization of users & groups into the Cloudflare Dashboard.
  6. **Clean up legacy resources** by removing SCIM v1 Virtual Groups and IdP mappings that follow the `CF-<accountID>-<Role Name>` pattern.



## More resources

  * [User Groups changelog](https://developers.cloudflare.com/changelog/2025-06-02-user-groups-beta/)
  * [User Groups documentation](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/)
  * [Create an Account Owned Token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/#create-an-account-owned-token)
  * [SCIM provisioning setup guide](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)



[PreviousAuthorizing an application](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/)[NextCloudflare Cookies](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/reference/migration-guides/scim-virtual-groups-migration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
