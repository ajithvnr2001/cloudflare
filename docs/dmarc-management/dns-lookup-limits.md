---
url: https://developers.cloudflare.com/dmarc-management/dns-lookup-limits/
title: DNS lookup limit \u00b7 Cloudflare DMARC Management docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:55.086006+00:00
---

# DNS lookup limit · Cloudflare DMARC Management docs

> Source: https://developers.cloudflare.com/dmarc-management/dns-lookup-limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DMARC Management](https://developers.cloudflare.com/dmarc-management/)
  3. /DNS lookup limit



# DNS lookup limit

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dmarc-management/dns-lookup-limits/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

An [SPF record ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) lists which servers are authorized to send email for your domain. SPF records can reference other domains and services (for example, using `include:` or `mx` mechanisms), and each such reference requires a separate DNS lookup to verify. The [SPF specification (RFC 7208) ↗︎](https://www.rfc-editor.org/rfc/rfc7208.html) limits the total number of these lookups to 10 per SPF check. If your SPF record exceeds this limit, receiving mail servers may treat the SPF check as a permanent error and reject or flag your emails.

To check if your SPF records are compliant with the SPF specification:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), and select your account and domain.
  2. Go to **Email** > **DMARC Management**.
  3. In **Email record overview** , select **View records**.
  4. Find your SPF record, and select the three dots next to it > **Edit**.
  5. DMARC Management will inspect your records and check for the total number of DNS lookups. If the record exceeds the limit, DMARC Management will display a warning. To fix this, remove unnecessary entries in your SPF record. Refer to [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records) for more information.



[PreviousSecurity records](https://developers.cloudflare.com/dmarc-management/security-records/)[NextStatistics and details](https://developers.cloudflare.com/dmarc-management/statistics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dmarc-management/dns-lookup-limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
