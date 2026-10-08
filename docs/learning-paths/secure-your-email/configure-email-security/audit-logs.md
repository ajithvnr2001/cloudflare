---
url: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/audit-logs/
title: Enable audit logs \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:58.810046+00:00
---

# Enable audit logs · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/audit-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Your Email

  4. /[Configure Email security](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/)
  5. /Enable audit logs



# Enable audit logs

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/audit-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

With Email security, you can enable logs to review actions performed on your account.

To enable audit logs:

  1. In the Cloudflare dashboard, go to the **Logpush** page.

[ Go to **Logpush** ↗ ](https://dash.cloudflare.com/?to=/:account/logs)
  2. Select your storage destination.

  3. Select the three dots > **Edit**.

  4. Under **Configure logpush job** :

     * **Job name** : Enter the job name, if it is not already prepopulated.
     * **If logs match** > Select **Filtered logs** : 
       * **Field** : Choose `ResourceType`.
       * **Operator** : Choose `starts with`.
       * **Value** : Enter `email_security`.
  5. Select **Submit**.




You can now view logs via the Cloudflare dashboard.

[PreviousReport phish](https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/report-phish/)[NextOverview](https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-your-email/configure-email-security/audit-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
