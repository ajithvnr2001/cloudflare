---
url: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/
title: Report phish \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:59.123496+00:00
---

# Report phish · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Your Email

  4. /[Configure Email security](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/)
  5. /Report phish



# Report phish

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview PhishNet for Microsoft 365 PhishNet for Google Workspace

Before deploying Email security to production, you will have to consider reporting any phishing attacks, evaluating which disposition to assign a specific message, and using different screen criteria to search through your inbox.

PhishNet is an add-in button that helps users to submit phish samples missed by Email security detection.

### PhishNet for Microsoft 365

To set up PhishNet Microsoft 365:

  1. Log in to the Microsoft admin panel. Go to **Microsoft 365 admin center** > **Settings** > **Integrated Apps**.
  2. Select **Upload custom apps**.
  3. Choose **Provide link to manifest file** and paste the following URL:


    
    
    https://phishnet-o365.area1cloudflare-webapps.workers.dev?clientId=ODcxNDA0MjMyNDM3NTA4NjQwNDk1Mzc3MDIxNzE0OTcxNTg0Njk5NDEyOTE2NDU5ODQyNjU5NzYzNjYyNDQ3NjEwMzIxODEyMDk1NQ

  4. Verify and complete the wizard.



### PhishNet for Google Workspace

To set up PhishNet for Google Workspace:

  1. Log in to the Google Workspace Marketplace using an administrator account.
  2. Select **Admin install** to install Cloudflare PhishNet.



Refer to [Set up PhishNet for Google Workspace](https://developers.cloudflare.com/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/#set-up-phishnet-for-google-workspace) for more information.

[PreviousSet additional detections](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/set-additional-detections/)[NextEnable audit logs](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/audit-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-your-email/configure-email-security/report-phish.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
