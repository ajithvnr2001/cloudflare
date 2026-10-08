---
url: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/
title: Set additional detections \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:01.077212+00:00
---

# Set additional detections · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Your Email

  4. /[Configure Email security](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/)
  5. /Set additional detections



# Set additional detections

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure domain ageConfigure blank email detectionConfigure ACH change from free email detectionConfigure HTML Attachment Email Detection

Email security allows you to configure the following additional detections:

  * [Domain age](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-domain-age)
  * [Blank email detection](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-blank-email-detection)
  * [Automated Clearing House (ACH)](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-ach-change-from-free-email-detection) change from free email detection.
  * [HTML attachment email detection](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/#configure-html-attachment-email-detection)



To configure additional detections:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
  2. Select **Email security**.
  3. Select **Settings**.
  4. On the Settings page, go to **Detection settings** > **Additional detections** , and select **Edit**.



## Configure domain age

The domain age is the time since the domain has been registered.

To configure a domain age:

  1. On the **Edit additional detections** page: 
     * Select **Malicious domain age** : Controls the threshold for a malicious disposition. Maximum of 100 days.
     * Select **Suspicious domain age** : Controls the threshold for a suspicious disposition. Maximum of 100 days.
  2. Select **Save**.



## Configure blank email detection

Blank email detection detects emails with blank bodies and assigns a default disposition. You can choose between **Malicious** and **Suspicious** as dispositions.

To enable blank email detection:

  1. On the **Edit additional detections** page, enable **Blank email detection**.
  2. Choose between **Malicious** and **Suspicious**.
  3. Select **Save**.



## Configure ACH change from free email detection

[Automated Clearing House (ACH) ↗︎](https://en.wikipedia.org/wiki/Automated_clearing_house) is a banking term related to direct deposits. ACH change from free email detection detects payroll inquiries or change requests from free email domains and assigns a default disposition. You can choose between **Malicious** and **Suspicious** as dispositions.

To enable ACH change from free email detection:

  1. On the **Edit additional detections** page, enable **ACH change from free email detection**.
  2. Choose between **Malicious** and **Suspicious**.
  3. Select **Save**.



## Configure HTML Attachment Email Detection

HTML attachment email detection detects HTM and HTML attachments in emails and assigns a default disposition.

To enable HTML attachment email detection:

  1. On the **Edit additional detections** page, enable **HTML attachment email detection**.
  2. Choose between **Malicious** and **Suspicious**.
  3. Select **Save**.



[PreviousCreate allow policies](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/create-allow-policies/)[NextReport phish](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-your-email/configure-email-security/set-additional-detections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
