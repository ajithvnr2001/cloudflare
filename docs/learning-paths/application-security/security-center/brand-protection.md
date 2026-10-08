---
url: https://developers.cloudflare.com/learning-paths/application-security/security-center/brand-protection/
title: Brand Protection \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:43.640464+00:00
---

# Brand Protection · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/security-center/brand-protection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Security Center](https://developers.cloudflare.com/learning-paths/application-security/security-center/)
  5. /Brand Protection



# Brand Protection

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/security-center/brand-protection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTypes of queriesAlerts

Brand Protection allows you to proactively identify and mitigate domain impersonation and phishing attacks. By monitoring newly registered domains and visual assets across the Internet, Cloudflare helps protect your brand's reputation and prevents your customers or employees from submitting sensitive information to fraudulent sites.

Common threats include:

  * [Typosquatting ↗︎](https://en.wikipedia.org/wiki/Typosquatting): For example, typing `cloudfalre.com` instead of `cloudflare.com`.
  * Concatenation of services (`cloudflare-service.com`) often registered by attackers to trick unsuspecting victims into submitting private information such as passwords.
  * [Homoglyph attacks ↗︎](https://en.wikipedia.org/wiki/IDN_homograph_attack) that use lookalike characters to trick unsuspecting victims.



## Types of queries

  1. [Domain search](https://developers.cloudflare.com/security-center/brand-protection/#domain-search): allows you to search for domains that might be trying to impersonate your brand.

  2. [Logo search](https://developers.cloudflare.com/security-center/brand-protection/#logo-queries): allows you to search for logos that might look and feel like your brand's logo.




## Alerts

Brand Protection integrates with Cloudflare's ANS (Alerts Notification Service) to provide configurable alerts when new domains are detected.

Any matches that are found during the new domain search are then inserted into an internal alerts table which triggers an alert for the user. This allows you to receive real-time notifications and take immediate action to investigate and potentially block any suspicious domains that may be attempting to impersonate your brand.

[PreviousSecurity Insights](https://developers.cloudflare.com/learning-paths/application-security/security-center/insights/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/security-center/brand-protection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
