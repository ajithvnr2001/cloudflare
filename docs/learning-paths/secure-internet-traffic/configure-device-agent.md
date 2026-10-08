---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/
title: Configure the device agent \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:56.939161+00:00
---

# Configure the device agent · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /Secure Internet Traffic
  4. /Configure the device agent



# Configure the device agent

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewObjectives

The Cloudflare One Client (known as the Cloudflare One Agent in mobile app stores) encrypts designated traffic from a user's device to Cloudflare's global network. In this learning path, we will first define all of your parameters and deployment rules, and then we will install and connect the client. If you prefer to start the client download now, refer to [Download the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

Note

The following steps are identical to [Configure the device agent](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/) in the Replace your VPN implementation guide. If you have already completed Replace your VPN, you can skip ahead to [Determine when to use PAC files](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/pac-files/).

## Objectives

By the end of this module, you will be able to:

  * Define which users can connect devices to your Zero Trust instance.
  * Configure global and device-specific settings for the Cloudflare One Client.
  * Route user traffic through Cloudflare Gateway.
  * Route domains to a private DNS server, if required.



Troubleshoot the Cloudflare One Client

For step-by-step guidance on diagnosing and resolving Cloudflare One Client issues, refer to the [Cloudflare One Client troubleshooting guide](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/). The guide covers:

  * How to collect diagnostic logs via the Cloudflare dashboard or CLI
  * How to review key configuration files
  * Common misconfigurations and their fixes
  * Best practices for filing support tickets



[PreviousVerify device connectivity](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/validate-traffic-in-gateway/)[NextDefine device enrollment permissions](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/configure-device-agent/device-enrollment-permissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/configure-device-agent/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
