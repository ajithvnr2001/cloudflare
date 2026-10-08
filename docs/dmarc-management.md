---
url: https://developers.cloudflare.com/dmarc-management/
title: Overview \u00b7 Cloudflare DMARC Management docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:55.278663+00:00
---

# Overview · Cloudflare DMARC Management docs

> Source: https://developers.cloudflare.com/dmarc-management/

  1. [Home](https://developers.cloudflare.com/)
  2. /DMARC Management



# Cloudflare DMARC Management

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/dmarc-management/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRelated products

Stop brand impersonation.

Available on all plans

When someone receives an email that claims to be from your domain, email servers check whether that message is authentic. Three DNS-based mechanisms handle this verification:

  * **[SPF (Sender Policy Framework) ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)** confirms the email was sent from an IP address or domain your domain authorizes.
  * **[DKIM (DomainKeys Identified Mail) ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)** authenticates the sender's domain and verifies the email content was not altered in transit, using a cryptographic signature.
  * **[DMARC (Domain-based Message Authentication Reporting and Conformance) ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)** ties SPF and DKIM together and tells receiving servers what to do when a check fails (for example, reject the email, quarantine it, or take no action).



Cloudflare DMARC Management helps you track every source that is sending emails from your domain and review DMARC reports for each source. These reports show whether messages sent from your domain are passing SPF, DKIM, and DMARC checks — so you can identify unauthorized senders and protect your domain from being used in phishing or spoofing attacks.

Note

DMARC Management is available to all Cloudflare customers with [Cloudflare DNS](https://developers.cloudflare.com/dns/).

* * *

## Related products

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Protect your email inbox with Email security.

[Cloudflare DNS](https://developers.cloudflare.com/dns/)

Fast, resilient and easy-to-manage DNS service.

[NextEnable DMARC Management](https://developers.cloudflare.com/dmarc-management/enable/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dmarc-management/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
