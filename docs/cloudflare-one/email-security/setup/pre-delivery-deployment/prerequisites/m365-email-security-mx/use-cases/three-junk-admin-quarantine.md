---
url: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/
title: Junk email and administrative quarantine - Microsoft 365 \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:43.854935+00:00
---

# Junk email and administrative quarantine - Microsoft 365 · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)Pre-delivery deploymentPrerequisites[Microsoft 365 as MX Record](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/)

  4. /Use cases
  5. /3 - Junk email and administrative quarantine



# 3 - Junk email and administrative quarantine

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate quarantine policiesConfigure quarantine notificationsConfigure anti-spam policiesCreate transport rules

In this tutorial, you will learn how to deliver `BULK` messages to the users's junk email folder, and `MALICIOUS`, `SPAM`, and `SPOOF` messages to the administrative quarantine (this requires an administrator to release the emails).

## Create quarantine policies

To create quarantine policies:

  1. Open the [Microsoft 365 Defender console ↗︎](https://security.microsoft.com/)

  2. Go to **Email & collaboration** > **Policies & rules**.

  3. Select **Threat policies**.

  4. Under **Rules** , select **Quarantine policies**.

  5. Select **Add custom policy**.

  6. Set the **Policy name** to `UserNotifyAdminRelease`.

  7. Select **Next**.

  8. In **Recipient message access** , select **Set specific access (Advanced)** , and then:

     * In **Select release action preference** , choose _Allow recipients to request a message to be released from quarantine_.
     * In **Select additional actions recipients can take on quarantined messages** , select the **Delete** and **Preview** checkboxes.
  9. Select **Next**.

  10. In **Quarantine notification** , select **Enable**.

  11. Select **Next**.

  12. Review your settings and select **Submit**.

  13. Select **Done**.




## Configure quarantine notifications

To configure quarantine notifications:

  1. Open the [Microsoft 365 Defender console ↗︎](https://security.microsoft.com/).

  2. Go to **Email & collaboration** > **Policies & rules**.

  3. Select **Threat policies**.

  4. Under **Rules** , select **Quarantine policies**.

  5. Select **Global settings**.

  6. Scroll to the bottom and set the desired frequency in **Send end-user spam notifications every (days)**. This value can only be incremented in days.

  7. Select **Save**.




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
    * **Select quarantine policy** : _UserNotifyAdminRelease_.
  * **Phishing** : _Quarantine message_. 
    * **Select quarantine policy** : _UserNotifyAdminRelease_.
  * **High confidence phishing** : _Quarantine message_. 
    * **Select quarantine policy** : _UserNotifyAdminRelease_.
  * **Retain spam in quarantine for this many days** : Default is 15 days. Email security recommends 15-30 days. 
    * Select the spam actions in the above step.


  8. Select **Save**.



## Create transport rules

To create the transport rules that will send emails with certain [disposition](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions) to Email security:

  1. Open the new [Exchange admin center ↗︎](https://admin.exchange.microsoft.com/#/homepage).

  2. Go to **Mail flow** > **Rules**.

  3. Select **Add a Rule** > **Create a new rule**.

  4. Set the following rule conditions:

     * **Name** : _`Email security Deliver to Junk Email folder`_.
     * **Apply this rule if** : _The message headers_ > _includes any of these words_. 
       * **Enter text** : `X-CFEmailSecurity-Disposition` > **Save**.
       * **Enter words** : `BULK` > **Add** > **Save**.
     * **Apply this rule if** : Select **+** to add a second condition.
     * **And** : _The sender_ > _IP address is in any of these ranges or exactly matches_ > enter the egress IPs in the [Egress IPs](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/) page.
     * **Do the following** \- __Modify the message properties_ > _Set the Spam Confidence Level (SCL)_ > _5__.
  5. Select **Next**.

  6. You can use the default values on this screen. Select **Next**.

  7. Review your settings and select **Finish** > **Done**.

  8. Select the rule `Email security Deliver to Junk Email folder` you have just created, and **Enable**.

  9. Select **Add a Rule** > **Create a new rule**.

  10. Set the following rule conditions:

     * **Name** : _`Email security User Quarantine Message`_.
     * **Apply this rule if** : _The message headers_ > _includes any of these words_. 
       * **Enter text** : `X-CFEmailSecurity-Disposition` > **Save**.
       * **Enter words** : _`MALICIOUS`, `UCE`, `SPOOF`_ > **Add** > **Save**.
     * **Apply this rule if** : Select **+** to add a second condition.
     * **And** : _The sender_ > _IP address is in any of these ranges or exactly matches_ > enter the egress IPs in the [Egress IPs](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/) page.
     * **Do the following** : __Modify the message properties_ > _Set the Spam Confidence Level (SCL)_ > _9__.
  11. Select **Next**.

  12. You can use the default values on this screen. Select **Next**.

  13. Review your settings and select **Finish** > **Done**.

  14. Select the rule _`Email security User Quarantine Message`_ you have just created, and select **Enable**.




[Previous2 - Junk email and user managed quarantine](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/two-junk-user-quarantine/)[Next4 - User managed quarantine and administrative quarantine](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/four-user-quarantine-admin-quarantine/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/m365-email-security-mx/use-cases/three-junk-admin-quarantine.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
