---
url: https://developers.cloudflare.com/email-service/configuration/subdomains/
title: Subdomains \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:12.829622+00:00
---

# Subdomains · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/configuration/subdomains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Configuration
  4. /Subdomains



# Subdomains

Last updated Sep 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/configuration/subdomains/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd a subdomain to Email RoutingAdd a subdomain to Email SendingNext steps

Email Routing is a zone-level feature that applies to the apex domain (for example, `example.com`) by default. Email Sending treats each domain separately and is onboarded per domain. You can extend either service to subdomains of the same zone, such as `mail.example.com` or `corp.example.com`, but the onboarding flow differs between the two.

A zone can have up to 30 domains configured for Email Routing or Email Sending combined, including the apex domain. Refer to [Limits](https://developers.cloudflare.com/email-service/platform/limits/) for the full list of platform limits.

## Add a subdomain to Email Routing

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account and domain.

  2. Go to **Compute** > **Email Service** > **Email Routing**.

[ Go to **Email Routing** ↗ ](https://dash.cloudflare.com/?to=/:account/email-service/routing)
  3. Select the apex domain, then open **Settings**.

  4. Under **Subdomains** , enter the subdomain you want to enable in the inline form and submit it.




Cloudflare adds the required DNS records to the subdomain. Once the records propagate, you can create [literal routing rules](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/) for addresses on the subdomain. Catch-all rules are only available for the apex domain.

## Add a subdomain to Email Sending

Email Sending treats a subdomain as a separate sending domain. Onboard the subdomain through the standard onboarding flow:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account.

  2. Go to **Compute** > **Email Service** > **Email Sending**.

[ Go to **Email Sending** ↗ ](https://dash.cloudflare.com/?to=/:account/email-service/sending)
  3. Select **Onboard Domain** and choose the subdomain you want to send from. The onboarding flow adds the `cf-bounce` MX, SPF, DKIM, and DMARC records to the subdomain.

  4. Select **Done**.




Once verified, you can send emails from addresses on the subdomain (for example, `notifications@mail.example.com`) using either the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) or the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/).

## Next steps

  * [Domain configuration](https://developers.cloudflare.com/email-service/configuration/domains/) — manage DNS records for sending and routing.
  * [Routing rules and addresses](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/) — create routing rules on subdomains.
  * [Deliverability](https://developers.cloudflare.com/email-service/concepts/deliverability/) — separate subdomains for different email types.



[PreviousEmail routing rules and addresses](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/)[NextConfigure MTA-STS](https://developers.cloudflare.com/email-service/configuration/mta-sts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/configuration/subdomains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
