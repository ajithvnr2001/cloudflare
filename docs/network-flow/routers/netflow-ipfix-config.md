---
url: https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/
title: Netflow/IPFIX configuration \u00b7 Cloudflare Network Flow docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:23.428661+00:00
---

# Netflow/IPFIX configuration · Cloudflare Network Flow docs

> Source: https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network Flow](https://developers.cloudflare.com/network-flow/)
  3. /Routers
  4. /Netflow/IPFIX configuration



# Netflow/IPFIX configuration

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin1\. Access your router configuration2\. Configure Flow Exporter3\. Configure Flow Record4\. Save and apply configuration5\. Verify your configuration

Configure your router to export flow data to Cloudflare's network for analysis in Network Flow (formerly Magic Network Monitoring). Network Flow supports the NetFlow v5, NetFlow v9, and IPFIX formats.

## Before you begin

Before configuring NetFlow or IPFIX, verify the following:

  * Your router supports NetFlow or IPFIX export capabilities. Refer to [Supported routers](https://developers.cloudflare.com/network-flow/routers/supported-routers/) for a list of compatible routers.
  * You have administrative access to your router's configuration interface.
  * You have [registered your router with Cloudflare](https://developers.cloudflare.com/network-flow/get-started/#2-register-your-router-with-cloudflare).



## 1\. Access your router configuration

Log in to your router's configuration application or command-line interface. The exact method varies by router vendor and model.

## 2\. Configure Flow Exporter

Open your router's NetFlow configuration menu and set up the **Flow Exporter** with the following values:

  * **Destination IP address** : `162.159.65.1`
  * **Destination Port** : `2055`
  * **Transport Protocol** : `UDP`



These settings direct your router to send flow data to Cloudflare's network for analysis.

## 3\. Configure Flow Record

Set up your router's **Flow Record** configuration with the following fields. These fields define what traffic metadata your router collects and exports.

Match fields identify the traffic:

  * `match ipv4 protocol`
  * `match ipv4 source address`
  * `match ipv4 destination address`
  * `match transport source-port`
  * `match transport destination-port`
  * `match interface input`



Collect fields capture statistics about the traffic:

  * `collect transport tcp flag`
  * `collect counter packets long`
  * `collect counter bytes long`
  * `collect flow sampler`
  * `collect timestamp sys-uptime first`
  * `collect timestamp sys-uptime last`



## 4\. Save and apply configuration

Save your NetFlow or IPFIX configuration changes and apply them to your router. Verify that your router's NetFlow template does not contain duplicated fields, as duplicates can cause export errors.

## 5\. Verify your configuration

After configuring NetFlow or IPFIX, verify that data is being sent to Cloudflare:

  1. Wait five to ten minutes for flow data to be transmitted and processed.
  2. Check your router status in the Cloudflare dashboard under **Network flow** > **Configure Network flow** > **Check routers** (visible during onboarding) or view analytics in the **Network flow** page.
  3. If data is not appearing, verify your Flow Exporter settings and confirm your router's public IP address matches the IP registered with Cloudflare.



[PreviousRecommended sampling rate](https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/)[NextsFlow configuration](https://developers.cloudflare.com/network-flow/routers/sflow-config/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network-flow/routers/netflow-ipfix-config.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
