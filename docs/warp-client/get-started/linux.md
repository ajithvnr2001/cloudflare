---
url: https://developers.cloudflare.com/warp-client/get-started/linux/
title: Linux desktop client \u00b7 Cloudflare WARP client docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:51.720916+00:00
---

# Linux desktop client · Cloudflare WARP client docs

> Source: https://developers.cloudflare.com/warp-client/get-started/linux/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WARP Client](https://developers.cloudflare.com/warp-client/)
  3. /[Get started](https://developers.cloudflare.com/warp-client/get-started/)
  4. /Linux



# Linux

Last updated May 7, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/warp-client/get-started/linux/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUsing WARP Initial connection Switch modes Switch tunnel protocol Using 1.1.1.1 for Families Enable WARP+ Unlimited Additional commandsFeedback

Looking for Zero Trust?

This documentation is for the consumer version of WARP (1.1.1.1 with WARP). If you are using WARP for Zero Trust security, refer to the [Cloudflare One Client documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/).

You have two ways of installing WARP on Linux, depending on the distro you are using:

  * Find the latest WARP client in the [package repository ↗︎](https://pkg.cloudflareclient.com/).
  * Install the `cloudflare-warp` package that suits your distro: 
    * **apt-based OS** (like Ubuntu): `sudo apt install cloudflare-warp`.
    * **yum-based OS** (like CentOS or RHEL): `sudo yum install cloudflare-warp`.



Note

If you get an error message when trying to install via the terminal, download the package that suits your distro from the [package repository ↗︎](https://pkg.cloudflareclient.com/).

## Using WARP

The command line interface is the primary way to use WARP.

### Initial connection

To connect for the very first time:

  1. Register the client `warp-cli registration new`.
  2. Connect `warp-cli connect`.
  3. Run `curl https://www.cloudflare.com/cdn-cgi/trace` and verify that `warp=on`.



### Switch modes

You can use `warp-cli mode --help` to get a list of modes to switch between. For example:

  * **DNS only mode via DoH:** `warp-cli mode doh`
  * **WARP with DoH:** `warp-cli mode warp+doh`



### Switch tunnel protocol

You can switch the protocol that WARP uses to route traffic from the device to Cloudflare.

  * **WireGuard:** `warp-cli tunnel protocol set WireGuard`
  * **MASQUE:** (default) `warp-cli tunnel protocol set MASQUE`



Note

The protocol values are case-sensitive.

For information on WireGuard versus MASQUE, refer to our [blog post ↗︎](https://blog.cloudflare.com/zero-trust-warp-with-a-masque).

### Using 1.1.1.1 for Families

The Linux client supports all 1.1.1.1 for Families modes, in either WARP on DNS-only mode:

  * **Families mode off:** `warp-cli dns families off`
  * **Malware protection:** `warp-cli dns families malware`
  * **Malware and adult content:** `warp-cli dns families full`



### Enable WARP+ Unlimited

To enable [WARP+ Unlimited](https://developers.cloudflare.com/warp-client/warp-modes/#warp-unlimited) on Linux, you will need an iOS or Android device that has an existing WARP+ Unlimited subscription.

  1. On your iOS or Android device, launch the **1.1.1.1 Faster Internet** app.

  2. Go to **Settings** > **Account** and copy the **Key** value.

  3. On your Linux device, run the following command:
         
         warp-cli registration license <KEY>

  4. Verify the new registration:
         
         warp-cli registration show
         
         Account type: Unlimited
         ...




Your WARP+ Unlimited subscription is now active on this device.

### Additional commands

A complete list of all supported commands can be found by running:
    
    
    warp-cli --help

## Feedback

You can find logs required to debug WARP issues by running `sudo warp-diag`. This will place a `warp-debugging-info.zip` file in the path from which you ran the command.

To report bugs or provide feedback to the team use the command `sudo warp-diag feedback`. This will submit a support ticket.

[PreviousiOS](https://developers.cloudflare.com/warp-client/get-started/ios/)[NextmacOS](https://developers.cloudflare.com/warp-client/get-started/macos/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/warp-client/get-started/linux.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
