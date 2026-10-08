---
url: https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/
title: Manage domains \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:38.929002+00:00
---

# Manage domains · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

  4. /[Setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)
  5. /Manage domains



# Manage domains

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd domainsFilter domainsEdit domainsPrevent Cloudflare from scanning a domain

Once you have deployed your domain, Email security allows you to add, filter and edit domains. You can also choose to stop a domain from being scanned.

## Add domains

To protect a new domain:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com) > Email security.
  2. Select **Settings** , go to **Domains** and select **View**.
  3. Select **Add a domain**.



## Filter domains

To filter your domains:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) > **Email security**.
  2. Go to **Settings** > **Domain management** > **Domains** , then select **View**.
  3. Select **Show filters** > **Configured method**. Choose among the following filters: - **MS Graph API** : To view domains connected via MS Graph API. - **BCC/Journaling** : To view domains connected via BCC/Journaling. - **MX/Inline** : To view domains connected via MX/Inline. - **Retro Scan** : To view domains scanned by Retro Scan.
  4. Select **Apply filters**.



## Edit domains

To edit your domains:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) > **Email security**.
  2. Go to **Settings** > **Domain management** > **Domains** , then select **View**.
  3. On the **Domains** page, locate your domain, select the three dots > **Edit**.
  4. If you did not manually add your domain, you will only be able to edit **Hops**. If you manually added your domain, you will be able to edit **Domain name** and **Hops**.
  5. Select **Save**.



## Prevent Cloudflare from scanning a domain

To stop scanning domains:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) > **Email security**.
  2. Go to **Settings** > **Domain management** > **Domains** , then select **View**.
  3. On the **Domains** page, locate your domain, select the three dots > **Stop scanning**.
  4. Select **Stop scanning** again to stop Cloudflare from scanning your domain.



[PreviousPartner domain TLS](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/email-security/monitoring/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/setup/manage-domains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
