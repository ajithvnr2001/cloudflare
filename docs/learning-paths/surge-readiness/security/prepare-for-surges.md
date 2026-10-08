---
url: https://developers.cloudflare.com/learning-paths/surge-readiness/security/prepare-for-surges/
title: Prepare for surges and mitigate DDoS attacks \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:01.458476+00:00
---

# Prepare for surges and mitigate DDoS attacks · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/surge-readiness/security/prepare-for-surges/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Surge Readiness

  4. /Security
  5. /Prepare for surges and attacks



# Prepare for surges and mitigate DDoS attacks

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/surge-readiness/security/prepare-for-surges/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReduce server strainUnlimited DDoS ProtectionBrowser Integrity Check

## Reduce server strain

Utilize Cloudflare's [caching](https://developers.cloudflare.com/cache/) to enhance load times and reduce server strain. Also, features like the [Waiting Room](https://developers.cloudflare.com/waiting-room) and [Rate Limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) can be used to effectively manage excess demand and ensure a stable user experience.

## Unlimited DDoS Protection

Cloudflare's Advanced [DDoS protection](https://developers.cloudflare.com/ddos-protection/) is always on for Enterprise customers and is used to mitigate DDoS attacks of all forms and sizes including those that target UDP and ICMP protocols, as well as SYN/ACK, DNS amplification, SMURF, and Layer 7 attacks.

## Browser Integrity Check

[Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/) looks for requests with HTTP headers commonly used by spammers, bots, and crawlers such as requests with a missing or non-standard user agent. If a threat is found, Cloudflare will present a challenge page before allowing access. This may affect your API and can be selectively disabled using [Page Rules](https://developers.cloudflare.com/rules/page-rules/).

[PreviousControl incoming requests](https://developers.cloudflare.com/learning-paths/surge-readiness/security/control-incoming-requests/)[NextSecure against attacks](https://developers.cloudflare.com/learning-paths/surge-readiness/security/secure-against-attacks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/surge-readiness/security/prepare-for-surges.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
