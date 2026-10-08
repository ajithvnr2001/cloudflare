---
url: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/
title: MX/Inline deployment \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:42.050662+00:00
---

# MX/Inline deployment · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)

  4. /Pre-delivery deployment
  5. /MX/Inline deployment



# MX/Inline deployment

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

With pre-delivery deployment, also known as Inline deployment, Email security evaluates email messages before they reach a user's inbox.

![Inline deployment diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=591,height=252,format=webp/_astro/Email_security_Deployment_Inline.Dsh4g8YD.png)

Before you change your MX records, you will have to set up the [Time to Live (TTL)](https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/) on your DNS records. If you do not set up the TTL, the DNS propagation will take longer to happen.

Cloudflare recommends to decrease the TTL to five minutes (also known as [Auto](https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/#proxied-records)) 3 to 5 days prior to the planned MX record change. Reducing the TTL allows the DNS record to propagate ahead of time, so changes take effect rapidly. Once you have completed your onboarding process, you can choose to increase the TTL.

When you have configured your TTL, you can deploy Email security via MX/Inline. An MX record is a [DNS record](https://developers.cloudflare.com/dns/manage-dns-records/).

If your DNS records are hosted by Cloudflare (or any other provider, except for Google), you can [edit your DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records) via the dashboard or the API to point your MX records to Cloudflare.

By changing your MX records, Email security will be positioned between your incoming emails and Microsoft 0365 or Gmail.

Email security becomes a hop in the [SMTP ↗︎](https://www.cloudflare.com/en-gb/learning/email-security/what-is-smtp/) processing chain and physically interacts with incoming email messages. Based on your policies, various messages are blocked before reaching the inbox.

When you choose an inline deployment, you get the following benefits:

  * Messages are processed and physically blocked before arriving in a user's mailbox.
  * Your deployment is simpler, because any complex processing can happen downstream and without modification.
  * Email security can modify delivered messages, adding subject or body mark-ups.
  * Email security can offer high availability and adaptive message pooling.
  * You can set up advanced handling downstream for non-quarantined messages with added X-headers.



[PreviousCisco - Cisco as MX Record](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-mx/)[NextSet up MX/Inline deployment](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
