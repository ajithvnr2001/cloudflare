---
url: https://developers.cloudflare.com/ddos-protection/reference/simulate-ddos-attack/
title: Simulating test DDoS attacks \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:54.970035+00:00
---

# Simulating test DDoS attacks · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/reference/simulate-ddos-attack/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /Reference
  4. /Simulating test DDoS attacks



# Simulating test DDoS attacks

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/reference/simulate-ddos-attack/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you start

After onboarding to Cloudflare, you may want to simulate DDoS attacks against your Internet properties to test the protection, [reporting](https://developers.cloudflare.com/ddos-protection/reference/reports/), and [alerting](https://developers.cloudflare.com/ddos-protection/reference/alerts/) mechanisms. Follow the guidelines in this section to simulate a DDoS attack.

You can only launch DDoS attacks against your own Internet properties — your zone, Spectrum application, or IP range (depending on your Cloudflare services) — and provided that:

  * The Internet properties are not shared with other organizations or individuals.
  * The Internet properties have been onboarded to Cloudflare in an account under your name or ownership.



## Before you start

You do not have to obtain permission from Cloudflare to launch a DDoS attack simulation against your own Internet properties.

It is recommended that you choose the right service and enable the correct features to test against the corresponding DDoS attacks. For example, if you want to test Cloudflare against an HTTP DDoS attack and you are only using Magic Transit, the test is going to fail because you need to onboard your HTTP application to Cloudflare's reverse proxy service to test our HTTP DDoS Protection.

[PreviousLogs](https://developers.cloudflare.com/ddos-protection/reference/logs/)[NextFAQ](https://developers.cloudflare.com/ddos-protection/frequently-asked-questions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/reference/simulate-ddos-attack.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
