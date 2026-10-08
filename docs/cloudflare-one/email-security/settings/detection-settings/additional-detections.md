---
url: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/
title: Additional detections \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:36.194485+00:00
---

# Additional detections · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)Settings

  4. /Detection settings
  5. /Additional detections



# Additional detections

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/additional-detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure domain ageConfigure blank email detectionConfigure ACH change from free email detectionConfigure HTML attachment email detection

Email security allows you to configure the following additional detections:

  * Domain age
  * Blank email detection
  * [Automated Clearing House (ACH) ↗︎](https://en.wikipedia.org/wiki/Automated_clearing_house) change from free email detection
  * HTML attachment email detection



To configure additional detections:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
  2. Select **Email security**.
  3. Select **Settings** > **Additional detections** > **View**.
  4. On the **Detection settings** page, select **Edit**.



## Configure domain age

The domain age is the time since the domain has been registered.

Because of the domain age detection, [trusted domains](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/trusted-domains/) can be used to create an exception to the age detection.

To configure a domain age:

  1. On the **Edit additional detections** page: 
     * Select **Malicious domain age** : Controls the threshold for a malicious disposition. Maximum of 100 days. It is recommended to set the **Malicious domain age** to 7 days.
     * Select **Suspicious domain age** : Controls the threshold for a suspicious disposition. Maximum of 100 days. It is recommended to set the **Suspicious domain age** between 30 and 45 days.
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



## Configure HTML attachment email detection

HTML attachment email detection detects HTM and HTML attachments in emails and assigns a default disposition.

To enable HTML attachment email detection:

  1. On the **Edit additional detections** page, enable **HTML attachment email detection**.
  2. Choose between **Malicious** and **Suspicious**.
  3. Select **Save**.



[PreviousConfigure text add-ons](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/)[NextDetection settings best practices](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/best-practices/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/settings/detection-settings/additional-detections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
