---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/validate-traffic-in-gateway/
title: Verify device connectivity \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:57.406963+00:00
---

# Verify device connectivity · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/validate-traffic-in-gateway/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Connect devices and networks to Cloudflare](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/)
  5. /Verify device connectivity



# Verify device connectivity

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/validate-traffic-in-gateway/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBest practices

To validate that Cloudflare is receiving traffic from a user device:

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Traffic policies** > **Traffic settings**.
  2. Under **Log traffic activity** , enable activity logging for all DNS logs.
  3. On your device, open a browser and go to any website.
  4. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Insights** > **Logs** > **DNS**.
  5. Make sure DNS queries from your device appear.



## Best practices

Securing your organization with Zero Trust usually happens in two phases: the first phase is establishing connectivity, and the second phase is building policies for distinct applications. We recommend verifying that all connectivity is working as expected before moving on to build complex security policies. This will reduce the amount of troubleshooting and challenges that arise from managing complex systems.

Troubleshoot the Cloudflare One Client

For step-by-step guidance on diagnosing and resolving Cloudflare One Client issues, refer to the [Cloudflare One Client troubleshooting guide](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/). The guide covers:

  * How to collect diagnostic logs via the Cloudflare dashboard or CLI
  * How to review key configuration files
  * Common misconfigurations and their fixes
  * Best practices for filing support tickets



[PreviousMDM deployment](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/mdm/)[NextOverview](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/connect-devices-networks/validate-traffic-in-gateway.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
