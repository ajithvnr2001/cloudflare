---
url: https://developers.cloudflare.com/email-service/concepts/deliverability/
title: Email deliverability \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:12.539056+00:00
---

# Email deliverability · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/concepts/deliverability/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Concepts
  4. /Email deliverability



# Email deliverability

Understand bounce handling and reputation management for optimal email delivery.

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/concepts/deliverability/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBounces Hard bounces Soft bouncesReputation management Best practices

When you send an email, there is no guarantee it reaches the recipient's inbox. Inbox providers like Gmail, Yahoo, Outlook, and iCloud invest heavily in filtering out unwanted email. If you send poorly targeted emails, have high bounce rates, or trigger spam complaints, these providers may flag your domain as untrustworthy. Once that happens, even your legitimate emails can end up in spam or be blocked outright.

This concept is referred to as email deliverability: maintaining a healthy sending reputation so that inbox providers trust your emails. Cloudflare Email Service helps with this by automatically handling bounces, managing suppression lists, and authenticating your emails through SPF, DKIM, and DMARC.

## Bounces

Bounces occur when emails cannot be delivered to recipients. There are two types of bounces: **hard bounces** and **soft bounces**.

### Hard bounces

Hard bounces are permanent delivery failures that occur when:

  * The recipient address does not exist.
  * The recipient domain does not exist.
  * The receiving server permanently rejects the recipient.



**Hard bounces are never retried** because the failure is permanent. Emails that hard bounce will generate a bounce notification to the sender address and can be monitored through [analytics](https://developers.cloudflare.com/email-service/observability/metrics-analytics/).

Email Service adds eligible recipient-side hard bounces to your [suppression list](https://developers.cloudflare.com/email-service/concepts/suppressions/). Suppressions have no expiration when the mailbox or domain does not exist.

They also have no expiration when the recipient remains unavailable across repeated delivery attempts. Other eligible hard-bounce suppressions last seven days.

### Soft bounces

Soft bounces are temporary failures that may succeed if retried:

  * Recipient mailbox is full
  * Email server temporarily down
  * Rate limiting or greylisting



Cloudflare automatically retries soft bounces with exponential backoff. Eligible recipient-side failures create a 24-hour suppression.

## Reputation management

Cloudflare automatically manages:

  * **IP reputation** : Managed sending infrastructure optimized for deliverability
  * **Domain authentication** : DKIM signing, SPF alignment, DMARC compliance
  * **Feedback processing** : ISP complaint handling and suppression list management



### Best practices

#### Content and list hygiene

Avoid content that can trigger spam-detection or can be perceived as unwanted content:

  * Avoid spam trigger words (FREE, URGENT, GUARANTEED)
  * Include both HTML and plain text versions
  * Use legitimate URLs and clear sender identification



Ensure that your email lists are clean and contain intended recipients:

  * Validate emails before sending
  * Implement double opt-in for subscriptions
  * Remove hard bounced addresses immediately



Ensure that your deliverability stays above key metrics to avoid affecting your email sending reputation:

  * Delivery rate >95%
  * Hard bounce rate < 2%
  * Complaint rate < 0.1%



#### Use separate domains for separate purposes

Each domain builds its own deliverability reputation with inbox providers. Use separate domains or subdomains for different types of email so that one category does not affect the reputation of another. For example:

  * `notifications.yourdomain.com` for transactional emails (order confirmations, password resets)
  * `marketing.yourdomain.com` for marketing and promotional emails
  * `yourdomain.com` for important account-related communications



This way, if marketing emails generate higher complaint rates, your transactional email deliverability is not impacted. Each domain can be onboarded separately through [domain configuration](https://developers.cloudflare.com/email-service/configuration/domains/).

[PreviousEmail lifecycle](https://developers.cloudflare.com/email-service/concepts/email-lifecycle/)[NextEmail authentication](https://developers.cloudflare.com/email-service/concepts/email-authentication/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/concepts/deliverability.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
