---
url: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/five-junk-admin-quarantine/
title: Deliver emails to the junk email folder - Microsoft 365 \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:43.054081+00:00
---

# Deliver emails to the junk email folder - Microsoft 365 · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/five-junk-admin-quarantine/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)Pre-delivery deploymentPrerequisites[Microsoft 365 as MX Record](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/)

  4. /Use cases
  5. /5 - Junk email folder and administrative quarantine



# 5 - Junk email folder and administrative quarantine

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/five-junk-admin-quarantine/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure anti-spam policiesCreate transport rules

In this tutorial, you will learn to deliver `BULK` messages to the user's junk email folder, and `MALICIOUS`, `SPAM`, and `SPOOF` messages to the Administrative Quarantine (this requires an administrator to release the emails).

## Configure anti-spam policies

To configure anti-spam policies:

  1. Open the [Microsoft 365 Defender console ↗︎](https://security.microsoft.com/).

  2. Go to **Email & collaboration** > **Policies & rules**.

  3. Select **Threat policies**.

  4. Under **Policies** , select **Anti-spam**.

  5. Select the **Anti-spam inbound policy (Default)** text (not the checkbox).

  6. In **Actions** , scroll down and select **Edit actions**.

  7. Set the following conditions and actions (you might need to scroll up or down to find them):



  * **Spam** : _Move messages to Junk Email folder_.
  * **High confidence spam** : _Quarantine message_. 
    * **Select quarantine policy** : _AdminOnlyAccessPolicy_.
  * **Phishing** : _Quarantine message_. 
    * **Select quarantine policy** : _AdminOnlyAccessPolicy_.
  * **High confidence phishing** : _Quarantine message_. 
    * **Select quarantine policy** : _AdminOnlyAccessPolicy_.
  * **Retain spam in quarantine for this many days** : Default is 15 days. Email security recommends 15-30 days. 
    * Select the spam actions in the above step.


  8. Select **Save**.



## Create transport rules

To create the transport rules that will send emails with certain [disposition](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions) to Email security:

  1. Open the new [Exchange admin center ↗︎](https://admin.exchange.microsoft.com/#/homepage).

  2. Go to **Mail flow** > **Rules**.

  3. Select **Add a Rule** > **Create a new rule**.

  4. Set the following rule conditions:

     * **Name** : _Email security Deliver to Junk Email folder`_.
     * **Apply this rule if** : _The message headers_ > _includes any of these words_. 
       * **Enter text** : `X-CFEmailSecurity-Disposition` > **Save**.
       * **Enter words** : `BULK` > **Add** > **Save**.
     * **Apply this rule if** : Select **+** to add a second condition.
     * **And** : _The sender_ > _IP address is in any of these ranges or exactly matches_ > enter the egress IPs in the [Egress IPs](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/) page.
     * **Do the following** \- __Modify the message properties_ > _Set the Spam Confidence Level (SCL)_ > _5__.
  5. Select **Next**.

  6. You can use the default values on this screen. Select **Next**.

  7. Review your settings and select **Finish** > **Done**.

  8. Select the rule Email security Deliver to Junk Email folder` you have just created, and **Enable**.

  9. Select **Add a Rule** > **Create a new rule**.

  10. Set the following rule conditions:

     * **Name** : _`Email security Admin Managed Host Quarantine`_.
     * **Apply this rule if** : _The message headers_ > _includes any of these words_. 
       * **Enter text** : `X-CFEmailSecurity-Disposition` > **Save**.
       * **Enter words** : _`MALICIOUS`, `UCE`, `SPOOF`_ > **Add** > **Save**.
     * **Apply this rule if** : Select **+** to add a second condition.
     * **And** : _The sender_ > _IP address is in any of these ranges or exactly matches_ > enter the egress IPs in the [Egress IPs](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/) page.
     * **Do the following** : __Redirect the message to_ > _hosted quarantine__.
  11. Select **Next**.

  12. You can use the default values on this screen. Select **Next**.

  13. Review your settings and select **Finish** > **Done**.

  14. Select the rule _`Email security Admin Managed Host Quarantine`_ you have just created, and select **Enable**.




[Previous4 - User managed quarantine and administrative quarantine](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/four-user-quarantine-admin-quarantine/)[NextGoogle Workspace as MX Record](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/five-junk-admin-quarantine.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
