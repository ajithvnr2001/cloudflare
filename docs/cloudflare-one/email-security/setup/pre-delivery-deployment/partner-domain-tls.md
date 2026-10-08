---
url: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/
title: Partner domain TLS \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:42.176960+00:00
---

# Partner domain TLS · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)

  4. /Pre-delivery deployment
  5. /Partner domain TLS



# Partner domain TLS

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To add additional TLS (Transport Layer Security) requirements for emails coming from certain domains, you can enforce higher levels of SSL/TLS inspection. If TLS is required, mail without TLS from the specified domain will be dropped.

Note

To enforce TLS across all emails, you will need to enforce TLS requirements when you are onboarding your domain. To only enforce TLS for specific emails, you can do so by going to **Settings** > **Partner domain TLS** > **Add a domain**.

To set up a partner domain:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and select **Email security**.
  2. Select **Settings** > **Partner domain TLS** > **View**.
  3. Select **Add a domain**.
  4. Enter a valid domain name. You can also exclude subdomains by selecting **Add exclude**.
  5. (Optional) Add an optional note to describe your rule(s).
  6. Select **Save**.



To edit a partner domain, select the three dots > **Edit**.

To delete a partner domain, select the three dots > **Delete**.

[PreviousEgress IPs](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/)[NextManage domains](https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
