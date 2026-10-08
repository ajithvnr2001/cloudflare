---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/
title: Set up the Cloudflare One Client for your organization \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:02.558138+00:00
---

# Set up the Cloudflare One Client for your organization · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)

  4. /[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)
  5. /First-time setup



# First-time setup

Last updated Jun 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTraffic and DNS mode (default) 1\. Create a Cloudflare Zero Trust account. 2\. Set up a login method. 3\. Define device enrollment permissions. 4\. Install the Cloudflare root certificate on your devices. 5\. Download and deploy the Cloudflare One Client to your devices. 6\. Log in to your organization's Cloudflare Zero Trust instance from your devices.DNS only mode 1\. Create a Cloudflare Zero Trust account. 2\. Set up a login method. 3\. Define device enrollment permissions. 4\. (Optional) Add a DNS location to Gateway. 5\. Download and deploy the Cloudflare One Client to your devices.

This guide walks you through setting up the Cloudflare One Client (formerly WARP) for your organization for the first time. After completing these steps, your devices will route traffic through Cloudflare's network, where you can apply security policies.

Choose a setup mode based on your needs:

  * **Traffic and DNS mode** (default) — Enables the full suite of security features, including HTTP inspection, identity-based policies, and device posture checks.
  * **DNS-only mode** — Filters only DNS queries. Does not inspect HTTP traffic or enforce device posture checks.



## Traffic and DNS mode (default)

This mode enables the complete suite of [device security features](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/).

### 1\. Create a Cloudflare Zero Trust account.

The [Cloudflare One dashboard ↗︎](https://dash.cloudflare.com/one/) will be your go-to place to check device connectivity data, as well as create Secure Web Gateway and Zero Trust policies for your organization.

As you complete the [Cloudflare Zero Trust onboarding](https://developers.cloudflare.com/cloudflare-one/setup/), you will be asked to create a team name for your organization. You will need the team name when you deploy the Cloudflare One Client on your devices; it will allow your users to connect to your organization's Cloudflare Zero Trust instance.

### 2\. Set up a login method.

Configure [One-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/) or connect a [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) in Zero Trust. This is the login method your users will utilize when authenticating to add a new device to your Cloudflare Zero Trust setup.

### 3\. Define device enrollment permissions.

Create [device enrollment rules](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/) to define which users in your organization should be able to connect devices to your organization's Cloudflare Zero Trust setup. As you create your rule, you will be asked to select which login method you would like users to authenticate with.

### 4\. Install the Cloudflare root certificate on your devices.

Advanced security features including HTTP traffic inspection require users to install and trust the [Cloudflare root certificate](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/) on their machine or device. If you are installing certificates manually on all your devices, these steps will need to be performed on each new device that is to be subject to HTTP filtering.

### 5\. Download and deploy the Cloudflare One Client to your devices.

Choose one of the [different ways](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) to deploy the Cloudflare One Client, depending on what works best for your organization.

### 6\. Log in to your organization's Cloudflare Zero Trust instance from your devices.

Once the Cloudflare One Client is installed on the device, [log in to your Zero Trust organization](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/). The user is prompted to authenticate with one of your configured login methods. New organizations include the [Cloudflare identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) as the default, so users can sign in with their Cloudflare account credentials. You can also connect a [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) or enable a [one-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/).

Next, build [Secure Web Gateway policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) to filter DNS, HTTP, and Network traffic on your devices.

## DNS only mode

This mode is best suited for organizations that only want to apply DNS filtering to outbound traffic from their company devices. It does not enable advanced HTTP filtering features such as HTTP policies, identity-based policies, device posture checks, or Browser Isolation.

### 1\. Create a Cloudflare Zero Trust account.

Zero Trust will be your go-to place to check device connectivity data, as well as create Secure Web Gateway and Zero Trust policies for your organization.

As you complete the [Cloudflare Zero Trust onboarding](https://developers.cloudflare.com/cloudflare-one/setup/), you will be asked to create a team name for your organization. You will need the team name when you deploy the Cloudflare One Client on your devices; it will allow your users to connect to your organization's Cloudflare Zero Trust instance.

### 2\. Set up a login method.

Configure [One-time PIN](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/) or connect a [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) in Zero Trust. This is the login method your users will utilize when authenticating to add a new device to your Cloudflare Zero Trust setup.

### 3\. Define device enrollment permissions.

Create [device enrollment rules](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/) to define which users in your organization should be able to connect devices to your organization's Cloudflare Zero Trust setup. As you create your rule, you will be asked to select which login method you would like users to authenticate with.

### 4\. (Optional) Add a DNS location to Gateway.

By default, the Cloudflare One Client sends DNS queries to Cloudflare using an encrypted protocol called DNS-over-HTTPS (DoH). If you need to apply different DNS policies to different offices or network locations, [add a DNS location](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/) to Gateway. Gateway will assign a unique DoH subdomain to each location, which you provide as a parameter when deploying the Cloudflare One Client to your devices.

### 5\. Download and deploy the Cloudflare One Client to your devices.

Choose one of the [different ways](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) to deploy the Cloudflare One Client, depending on what works best for your organization.

Next, create [DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/) to control how DNS queries from your devices get resolved.

[PreviousMigrate 1.1.1.1 app](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/cloudflare-one-agent-migration/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
