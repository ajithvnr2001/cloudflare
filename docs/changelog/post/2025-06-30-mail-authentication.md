---
url: https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/
title: Mail authentication requirements for Email Routing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.320979+00:00
---

# Mail authentication requirements for Email Routing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 30, 2025

## Mail authentication requirements for Email Routing

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Email Routing platform supports [SPF ↗︎](https://datatracker.ietf.org/doc/html/rfc7208) records and [DKIM (DomainKeys Identified Mail) ↗︎](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) signatures and honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them, we still forward the emails to upstream mailbox providers.

Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to forward them. We also strongly recommend that all senders implement the DMARC protocol.

If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where the forward action may fail due to missing authentication on the incoming email.

SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking bad emails. If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure you have them properly configured.
