---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/
title: Firewall \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:49.921241+00:00
---

# Firewall · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Reusable components[Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/)

  4. /[Cloudflare One Client checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)
  5. /Firewall



# Firewall

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/firewall/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesEnable the firewall checkValidate firewall status On macOS On Windows

The Firewall device posture attribute ensures that a firewall is running on a device.

## Prerequisites

  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Cloudflare One Client Checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/).




## Enable the firewall check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks**.

  2. Go to **Cloudflare One Client checks** and select **Add a check**.

  3. Select **Firewall**.

  4. Enter a descriptive name for the check.

  5. Select your operating system.

  6. Configure **Enable firewall check** based on your desired security policy:

     * **Enabled** : (Recommended) The posture check passes only if the firewall is running.
     * **Disabled** : The posture check passes only if the firewall is turned off.

Note

The **Enable firewall check** toggle does not turn the posture check on or off; rather, the toggle determines whether the Cloudflare One Client looks for an active or inactive firewall.

  7. Select **Save**.




Next, go to **Insights** > **Logs** > **Posture logs** and verify that the firewall check is returning the expected results.

## Validate firewall status

Operating systems determine firewall configuration in various ways. Follow the steps below to understand how the Cloudflare One Client determines if the firewall is enabled.

### On macOS

macOS has two firewalls: an application-based firewall and a port-based firewall. The Cloudflare One Client will report a firewall is enabled if either firewall is running.

#### Application-based firewall

  1. Open **System Settings** and go to **Network**.
  2. Verify that **Firewall** is `Active`.



#### Port-based firewall

  1. Open Terminal and run:
         
         sudo /sbin/pfctl -s info

  2. Verify that **Status** is `Enabled`.




### On Windows

  1. Open PowerShell and run:
         
         Get-NetFirewallProfile -PolicyStore ActiveStore -Name Public

  2. Verify that **Enabled** is `True`.




[PreviousFile check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/)[NextOS version](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/posture-checks/client-checks/firewall.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
