---
url: https://developers.cloudflare.com/email-service/platform/limits/
title: Limits \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:15.221798+00:00
---

# Limits · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Platform
  4. /Limits



# Limits

Email sending quotas, rate limits, and how to request higher limits for production use

Last updated Sep 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/platform/limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDaily sending limitsVerified destination addressesEmail content limitsSuppression list limitsZone limitsEmail Routing limits Routing to Workers on the Workers Free plan Emails sent from WorkersCompliance

Cloudflare Email Service has the following limits to ensure optimal performance and prevent abuse. These limits apply to emails sent via the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/), the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/), and [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) unless noted otherwise.

## Daily sending limits

New accounts start with a conservative daily quota and scale up over time based on your sending behavior, deliverability rates, and account standing. Limits are applied per account and may be adjusted automatically as your reputation improves.

If you need higher sending limits sooner than automatic adjustment provides, refer to "Need a higher limit?" at the bottom of this page to request an increase.

## Verified destination addresses

Before you onboard a sending domain, you can send emails only to [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#destination-addresses) in your account. After you onboard a sending domain, you can send to any recipient immediately.

Sends to verified destination addresses are always free: they do not count toward your monthly [quota](https://developers.cloudflare.com/email-service/platform/pricing/) or your daily sending limits, on any plan, including when only Email Routing is configured. You can only send from your routing domains.

## Email content limits

Component | Limit | Notes  
---|---|---  
**Recipients (to, cc, bcc)** | 50 per email | Combined across all recipient fields  
**Subject line** | 998 characters | RFC 5322 compliant  
**Total message size** | 5 MiB | Including attachments  
**Total message size** | 25 MiB | For [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#destination-addresses) only  
**Header size** | 16 KB | All custom headers combined  
  
## Suppression list limits

The following limits apply to the Email Sending [suppression list](https://developers.cloudflare.com/email-service/concepts/suppressions/) API:

Limit | Value | Notes  
---|---|---  
**Active entries** | 1 per address and scope | One `account` suppression and one per sending domain  
**Results per page** | 1,000 | Maximum `per_page` value with a default of 100  
**Items per bulk import** | 1,000 | Split larger imports across several requests  
**Bulk import requests** | 10 per minute | Applies per account and returns `429` when exceeded  
**Note length** | 1,000 characters | The optional `note` field on an entry  
  
The suppression list has no total-count field. Refer to the [list suppressions API reference](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/methods/list/) for pagination details.

## Zone limits

Limit | Value | Notes  
---|---|---  
**Domains per zone** | 30 | Combined total of domains configured for Email Routing or Email Sending in a zone, including the apex domain  
  
## Email Routing limits

The following limits apply to inbound email handled by Email Routing.

Limit | Value | Notes  
---|---|---  
**Routing rules per domain** | 200 | Each rule maps an email pattern to a destination  
**Destination addresses per account** | 200 | Verified destination addresses are shared across all domains in the account  
**Inbound message size** | 25 MiB | Messages larger than this are rejected  
**Reply`References` entries** | 100 | If the incoming email has more than 100 `References` entries, `message.reply()` throws. Reduces reply loops.  
  
Each routing rule maps one email pattern to one destination address or one Worker. To forward a single email pattern to multiple destinations, use a Worker that calls `forward()` once per destination. All destinations must be verified beforehand.

### Routing to Workers on the Workers Free plan

Workers that handle incoming emails count toward the standard Workers CPU and memory limits. On the Workers Free plan, complex handlers may exceed these limits and fail to process a message. Failed invocations appear in [Workers logs](https://developers.cloudflare.com/workers/observability/logs/) with the `EXCEEDED_CPU` error. Upgrade to the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) for higher CPU and memory limits.

### Emails sent from Workers

Emails sent from a Worker using the `send_email` binding appear in the Email Routing summary as **dropped** , even when they were delivered successfully. To track outbound send success, use [Email sending metrics and logs](https://developers.cloudflare.com/email-service/observability/) instead.

## Compliance

All email sending must follow applicable anti-spam laws and regulations to maintain good standing and deliverability.

  * **CAN-SPAM Act** (United States)
  * **GDPR** (European Union)
  * **CASL** (Canada)
  * Include proper unsubscribe mechanisms
  * Honor opt-out requests promptly



Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form ↗︎](https://forms.gle/eX6pXvit1wBv77Yw5). If the limit can be increased, Cloudflare will contact you with next steps.

[PreviousFAQ](https://developers.cloudflare.com/email-service/reference/faq/)[NextPricing](https://developers.cloudflare.com/email-service/platform/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
