---
url: https://developers.cloudflare.com/tenant/structure/
title: Tenant structure \u00b7 Cloudflare Tenant docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:00.051047+00:00
---

# Tenant structure · Cloudflare Tenant docs

> Source: https://developers.cloudflare.com/tenant/structure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Tenant](https://developers.cloudflare.com/tenant/)
  3. /Tenant structure



# Tenant structure

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tenant/structure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTenants and Tenant adminsAccounts, users, and resources

Cloudflare helps Channel and Alliance partners manage their and their customers' accounts through a Tenant structure.

![Partner accounts contain a tenant, which is a container for customer accounts and zones. For more details, keep reading.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=5582,height=3855,format=webp/_astro/tenant-diagram.D0Hfc9bM.png)

## Tenants and Tenant admins

A **Tenant** is a special type of Cloudflare account that contains other accounts and resources.

Once you sign a partner agreement with Cloudflare, we create a special Tenant account and then add your user to that account as a **Tenant admin**. Cloudflare can add multiple users as Tenant admins upon request.

Tenant admins then become the default [**Super administrator(s)**](https://developers.cloudflare.com/fundamentals/manage-members/roles/) for all accounts and zones contained within the Tenant.

This means that each Tenant admin's user API key can be used to provision accounts based on the catalog specified in your partner agreement.

If needed, you can also [create additional **Super administrators**](https://developers.cloudflare.com/fundamentals/manage-members/manage/).

## Accounts, users, and resources

This Tenant structure gives your account streamlined administrative access to customer:

  * Accounts1
  * Users2
  * Resources3



At the same time, this structure keeps your customers' data and settings separate from each other.

## Footnotes

  1. An entity that contains various settings, users, and resources (zones, Zero Trust applications, Workers).

↩
  2. A member of a Cloudflare account with their own user profile and [an associated role](https://developers.cloudflare.com/fundamentals/manage-members/roles/) that specifies their privileges within that account.

↩
  3. A resource is an entity owned by an account, which could be a zone/domain, a Workers instance, or a Zero Trust application.

↩



[PreviousOverview](https://developers.cloudflare.com/tenant/)[NextGet started](https://developers.cloudflare.com/tenant/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tenant/structure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
