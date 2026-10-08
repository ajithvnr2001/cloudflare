---
url: https://developers.cloudflare.com/learning-paths/secure-your-email/get-started/deployment-models/
title: Deployment models \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:59.568452+00:00
---

# Deployment models · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-your-email/get-started/deployment-models/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Your Email

  4. /[Get started with Email security](https://developers.cloudflare.com/learning-paths/secure-your-email/get-started/)
  5. /Deployment models



# Deployment models

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-your-email/get-started/deployment-models/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Email security offers multiple deployment models:

  * API for Microsoft 365 users.
  * BCC for Google Workspace users.
  * MX/Inline for all email providers.



When you choose the [API deployment](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/), Email security can both scan and take actions on emails after they have reached a user's inbox.

If you are a Google Workspace user, you can enable Email security via [BCC setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/bcc-journaling/bcc-setup/gmail-bcc-setup/gmail-bcc-setup/). Email security scans a copy of your email after it lands in your inbox.

![Google Workspace BCC deployment diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=606,height=466,format=webp/_astro/Gmail_Deployment_BCC.YSoTUoiz.png)

With MX/Inline, Email security scans your email before they land in your inbox, giving you the highest level of protection.

![Microsoft 365 and Google Workspace MX/Inline](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=591,height=252,format=webp/_astro/Email_security_Deployment_Inline.Dsh4g8YD.png)

Refer to [Before you begin](https://developers.cloudflare.com/cloudflare-one/email-security/setup/) for a comprehensive comparison of each deployment method, and [Understanding Email Security Deployments](https://developers.cloudflare.com/reference-architecture/architectures/email-security-deployments/) to learn about each deployment method.

[PreviousCreate an Email security account](https://developers.cloudflare.com/learning-paths/secure-your-email/get-started/create-email-security-account/)[NextRecommended deployment model](https://developers.cloudflare.com/learning-paths/secure-your-email/get-started/recommended-deployment-model/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-your-email/get-started/deployment-models.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
