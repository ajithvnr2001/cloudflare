---
url: https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/
title: Email dispositions \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:59.373924+00:00
---

# Email dispositions · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Your Email

  4. /[Enable auto-moves](https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/)
  5. /Email dispositions



# Email dispositions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/email-dispositions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Email security returns five potential verdicts for every email it scans. Review the detections and consider how you would treat them once an auto-move is enabled. Below is an overview of the disposition and recommendation actions by Cloudflare:

Disposition | Description | Recommendation |   
---|---|---|---  
MALICIOUS | Traffic invoked multiple phishing verdict triggers, met thresholds for bad behavior, and is associated with active campaigns. | Block |   
SUSPICIOUS | Traffic associated with phishing campaigns (and is under further analysis by our automated systems). | Research these messages internally to evaluate legitimacy. |   
SPOOF | Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies ([SPF ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/), [DKIM ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/), [DMARC ↗︎](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/)), or have mismatching Envelope From and Header From values. | Block after investigating (can be triggered by third-party mail services). |   
SPAM | Traffic associated with non-malicious, commercial campaigns. | Route to existing Spam quarantine folder. |   
BULK | Traffic associated with [Graymail ↗︎](https://en.wikipedia.org/wiki/Graymail), that falls in between the definitions of SPAM and SUSPICIOUS. For example, a marketing email that intentionally obscures its unsubscribe link. | Monitor or tag |   
  
[PreviousOverview](https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/)[NextConfigure auto-moves](https://developers.cloudflare.com/learning-paths/secure-your-email/enable-auto-moves/configure-auto-moves/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-your-email/enable-auto-moves/email-dispositions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
