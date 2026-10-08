---
url: https://developers.cloudflare.com/ddos-protection/change-log/
title: Changelog for global changes to DDoS protection \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:46.743826+00:00
---

# Changelog for global changes to DDoS protection · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/change-log/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /Changelog



# Changelog

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRSS feeds

Cloudflare has a regular cadence of releasing updates and new rules to the DDoS managed rulesets. The updates either improve a rule's accuracy, lower false positives rates, or increase the protection due to a change in the threat landscape.

The release cycle for a new rule within the regular cadence follows this process:

  * Cloudflare adds a new rule configured with the _Log_ action, and announces the rule in the "Scheduled changes" section of each managed ruleset.
  * From that point on, if this rule matches any traffic, the matched traffic will be visible in one of the [analytics dashboards](https://developers.cloudflare.com/ddos-protection/reference/analytics/). If you suspect this might be a false positive, you can lower the sensitivity for that rule. Refer to [override examples](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/http-overrides/override-examples/#legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive) for details.
  * Cloudflare updates the rule action to mitigate traffic (for example, using the _Block_ action) after a period of at least seven days, usually on a Monday. The exact date is shown in the scheduled changes list.



Changes to existing rules follow the same process, except that Cloudflare will create a temporary updated rule (denoted as `BETA` in rule description) before updating the original rule on the next release cycle.

Cloudflare is very proactive in responding to new attack vectors, which may need to be released outside of the 7-day cycle, defined as an Emergency Release. This emergency release is only used to respond to new high priority threats with a low false positive probability.

## RSS feeds

  * [General updates](https://developers.cloudflare.com/ddos-protection/change-log/general-updates/) \- [Subscribe to RSS](https://developers.cloudflare.com/ddos-protection/change-log/general-updates/index.xml)
  * [Network-layer DDoS managed ruleset](https://developers.cloudflare.com/ddos-protection/change-log/network/) \- [Subscribe to RSS](https://developers.cloudflare.com/ddos-protection/change-log/network/index.xml)
  * [HTTP DDoS managed ruleset](https://developers.cloudflare.com/ddos-protection/change-log/http/) \- [Subscribe to RSS](https://developers.cloudflare.com/ddos-protection/change-log/http/index.xml)



[PreviousFAQ](https://developers.cloudflare.com/ddos-protection/frequently-asked-questions/)[NextOverview](https://developers.cloudflare.com/ddos-protection/change-log/network/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/change-log/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
