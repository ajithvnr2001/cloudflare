---
url: https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/
title: Connect your domains \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:40.429993+00:00
---

# Connect your domains · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)Post-delivery deployment[BCC/Journaling](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/)BCC setup

  4. /Gmail BCC setup
  5. /Connect your domains



# Connect your domains

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd additional domainsVerify successful deployment

To connect your domains, you will need to [enable your Gmail BCC integration](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/#enable-gmail-bcc-integration). Once you have enabled your Gmail BCC integration, the Cloudflare dashboard will redirect you to the **Set up Email security** page.

On the **Set up Email security** page:

  1. **Connect domains** : Select at least one domain. Then, select **Continue**.
  2. (**Optional**) **Add manual domains** : Select **Add domain name** to manually enter additional domains. Then, select **Continue**.
  3. (**Optional**) **Adjust hop count** : Enter the number of hops. Then, select **Continue**. Configuring the hop count will determine where you want Cloudflare to sit in the email processing chain.
  4. (**Optional** , select **Skip for now** to skip this step) **Move messages** : Refer to [Auto-moves](https://developers.cloudflare.com/cloudflare-one/email-security/settings/auto-moves/) to configure auto-moves. Then, select **Continue**.
  5. **Select your processing location** : Configure where you want Cloudflare to process your email. **Global** will be the default option. If you choose **Global** , `<account tag>@CF-emailsecurity.com` will be your regional service address. Once you have chosen your processing location, select **Continue**. Refer to [Regional processing](https://developers.cloudflare.com/cloudflare-one/email-security/reference/regional-processing/) to learn more.
  6. **Review details** : Review your connected domains and service addresses. Then, select **Go to domains.**



Your domains are now added successfully.

On the **Domains** page, select the three dots > **View integration**. The dashboard will display your [domain information](https://developers.cloudflare.com/cloudflare-one/email-security/settings/domain-management/domain/).

Under **Source** , the dashboard will display **Google integration** , along with the **Integration name**.

## Add additional domains

To add additional domains:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Email security** > **Settings**.
  2. Select **Connect an integration** > **BCC/Journaling** > **Integrate with Google** > **Authorize**.
  3. **Connect domains** : Select the domains you want to add, then select **Next**.
  4. (Optional) Select **Add manual domains** : Enter additional domains manually, then select **Next**.
  5. (Optional) Select **Adjust hop count** : Enter the number of hops.
  6. **Review details** : Review your selected domains, then use the following email to configure the service address with your third-party email provider: 
         
         <account tag>@CF-emailsecurity.com

  7. Select **Save**.



## Verify successful deployment

To verify that the deployment has been successful and that your emails are being scanned:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), select **Email security**.
  2. Go to **Settings** > **Domain management** > **Domains** , then select **View**.
  3. Under **Your domains** , locate your domain, and verify that **Status** (which describes the state of the configuration) displays **Active**.



[PreviousEnable Gmail BCC integration](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/enable-gmail-integration/)[NextAdd BCC rules](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/add-bcc-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/connect-domains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
