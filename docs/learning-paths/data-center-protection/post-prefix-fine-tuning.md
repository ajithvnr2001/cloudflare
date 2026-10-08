---
url: https://developers.cloudflare.com/learning-paths/data-center-protection/post-prefix-fine-tuning/
title: Post prefix advertisement monitoring and fine tuning \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:47.962807+00:00
---

# Post prefix advertisement monitoring and fine tuning · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/data-center-protection/post-prefix-fine-tuning/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Data Center Protection
  4. /Post prefix advertisement monitoring and fine tuning



# Post prefix advertisement monitoring and fine tuning

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/data-center-protection/post-prefix-fine-tuning/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDDOS Managed Rules Adaptive DDOS rules Advanced TCP Protection and Advanced DNS ProtectionCloudflare Network Firewall rulesAlerts for Magic Tunnel health checks and DDoSOptional

On this page, you can find suggestions to monitor your prefix advertisements and fine-tune them.

## DDOS Managed Rules

### Adaptive DDOS rules

[These rules](https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/) are based on a seven-day rolling window. We recommend reviewing the logs from these adaptive rules in Network Analytics seven days after your last prefix advertisement.

If you see matches for legitimate traffic, consider lowering the sensitivity of the rule and then review the logs again. Once you are satisfied that legitimate traffic is not being flagged, [create a DDoS override](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/#create-a-ddos-override) for this rule with action as `DDOS Dynamic` or `Block`.

### Advanced TCP Protection and Advanced DNS Protection

For both [Advanced TCP Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/) and [Advanced DNS Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/), your Cloudflare account team will need to configure manual thresholds for your account, based on your ingress traffic.

Once all your prefixes are advertised and/or once all your expected traffic is cut over to the Magic Transit prefixes, reach out to your Cloudflare account team to have the thresholds configured.

You can then change the mode on your Advanced TCP and DNS protections from `monitoring` to `mitigation`. You can also create a filter for `monitoring` mode for any traffic flows for which you see false positives. Try to keep this specific so that the protection is enabled for other inbound traffic flows.

## Cloudflare Network Firewall rules

We strongly encourage you to ensure you have a Cloudflare Network Firewall ruleset configured and customized to your environment to help stop unwanted and attack traffic.

You can configure Cloudflare Network Firewall rules and keep them in `disabled` mode to review the traffic that would have matched, using `verdict = drop` and the rule ID within Network Analytics. Once you are satisfied that the rule is blocking/permitting the intended traffic, you can change the mode to `enabled`.

Refer to Cloudflare Network Firewall's [best practices](https://developers.cloudflare.com/cloudflare-network-firewall/best-practices/) for configuration guidance and suggestions.

## Alerts for Magic Tunnel health checks and DDoS

  * Ensure all teams/members needing to receive these are getting the alerts.
  * Check the Tunnel Health Check Alert configuration for Sensitivity and Alert interval and tunnels in-scope.
  * Refer to [Set up tunnel health alerts](https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/#set-up-tunnel-health-alerts) and [DDoS alerts](https://developers.cloudflare.com/ddos-protection/reference/alerts/) for more details.



## Optional

  * Enable [Logpush](https://developers.cloudflare.com/logs/logpush/) to your Security Information and Event Management (SIEM).
  * Enable Cloudflare Network Firewall's [Intrusion Detection System (IDS)](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/). Requires Logpush and is only available for accounts with [Cloudflare Advanced Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/plans/#advanced-features).
  * Use [Network Flow](https://developers.cloudflare.com/network-flow/) (formerly Magic Network Monitoring) for visibility into traffic on your non-Magic Transit prefixes, using NetFlow or sFlow from your CPEs.



[PreviousTroubleshooting connectivity issues after prefix advertisement](https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/data-center-protection/post-prefix-fine-tuning.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
