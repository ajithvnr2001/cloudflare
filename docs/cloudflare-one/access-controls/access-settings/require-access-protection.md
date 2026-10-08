---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/
title: Require Access protection \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:09.867959+00:00
---

# Require Access protection · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)

  4. /Access settings
  5. /Require Access protection



# Require Access protection

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTurn on Access protectionAllow traffic to a hostnameBlocked request behavior

Cloudflare Access allows you to require Access protection for all hostnames in your account. When this setting is turned on, traffic to any hostname without a matching [Access application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/) is automatically blocked.

This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. Without this setting, a developer could deploy a new application or create a DNS record and inadvertently expose the resource before configuring an Access application.

## Turn on Access protection

Caution

Turning on Access protection blocks traffic to any hostname that does not have an Access application. Before turning on this setting, verify that all publicly accessible hostnames have an Access application with an Allow or Bypass policy.

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and go to **Zero Trust** > **Access controls** > **Access settings**.

  2. Turn on **Block traffic to all domains in this account**. You will see a dialog confirming you understand the scope of this change. Select **Confirm**.

Traffic to all hostnames in the account is now blocked unless an Access application exists for the hostname.

  3. (Optional) Under **Hostnames to Exempt** , select specific domains to exempt from the **Block traffic to all domains in this account** setting. Traffic to exempted hostnames is allowed even if no Access application exists.

Note

Cloudflare recommends limiting exemptions to hostnames that host only public-facing content. Internal applications should have an Access application configured.




## Allow traffic to a hostname

To allow traffic to a hostname when **Block traffic to all domains in this account** is turned on:

  1. [Create an Access application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) for the hostname.
  2. Add an [Allow policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#allow) to grant access to authorized users.
  3. (Optional) Add a [Bypass policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#bypass) if the hostname should be publicly accessible without authentication.



## Blocked request behavior

When a user attempts to access a hostname without an Access application, Cloudflare displays a block page with `Error 1050: This resource is blocked by this account's Default-Deny policy.` The user cannot proceed until an administrator creates an Access application for that hostname.

[PreviousSession management](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/)[NextIndependent MFA](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/access-settings/require-access-protection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
