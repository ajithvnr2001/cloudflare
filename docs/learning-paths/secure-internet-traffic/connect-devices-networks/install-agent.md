---
url: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/
title: Download and install the Cloudflare One Client \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:57.340090+00:00
---

# Download and install the Cloudflare One Client · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Secure Internet Traffic

  4. /[Connect devices and networks to Cloudflare](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/)
  5. /Download and install the Cloudflare One Client



# Download and install the Cloudflare One Client

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstall the Cloudflare One Client

Most admins test by manually downloading the Cloudflare One Client and enrolling in your organization's Cloudflare Zero Trust instance.

## Install the Cloudflare One Client

  1. First, uninstall any existing third-party VPN software if possible. Sometimes products placed in a disconnected or disabled state will still interfere with the Cloudflare One Client.

  2. If you are running third-party firewall or TLS decryption software, verify that it does not inspect or block traffic to the following destinations:

     * IPv4 API endpoints: `162.159.137.105` and `162.159.138.105`
     * IPv6 API endpoints: `2606:4700:7::a29f:8969` and `2606:4700:7::a29f:8a69`
     * SNIs for Cloudflare One Client version 2026.6.0 and later: `api.devices.cloudflare.com`
     * SNIs for versions earlier than 2026.6.0: `zero-trust-client.cloudflareclient.com` and `notifications.cloudflareclient.com`

For more information, refer to [WARP with firewall](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/).

  3. Manually install the Cloudflare One Client on the device.

Window, macOS, and Linux

To enroll your device using the client GUI:

     1. [Download](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/) and install the Cloudflare One Client.

     2. Launch the Cloudflare One Client.

     3. On the **What would you like to use the Cloudflare One Client for?** screen, select **Zero Trust security**.

     4. Enter your team name.

     5. Complete the authentication steps required by your organization.

Once authenticated, you will see a Success page and a dialog prompting you to open the Cloudflare One Client.

     6. Select **Open the Cloudflare One Client** to complete the registration.

     7. [Download](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/) and install the Cloudflare One Client.

     8. Launch the Cloudflare One Client.

     9. Select the Cloudflare logo in the menu bar.

     10. Select the gear icon.

     11. Go to **Preferences** > **Account**.

     12. Select **Login with Cloudflare Zero Trust**.

     13. Enter your team name.

     14. Complete the authentication steps required by your organization.

Once authenticated, you will see a Success page and a dialog prompting you to open the Cloudflare One Client.

     15. Select **Open Cloudflare WARP.app** to complete the registration.

iOS, Android, and ChromeOS

     1. [Download](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/) and install the Cloudflare One Agent app.
     2. Launch the Cloudflare One Agent app.
     3. Select **Next**.
     4. Review the privacy policy and select **Accept**.
     5. Enter your team name.
     6. Complete the authentication steps required by your organization.
     7. After authenticating, select **Install VPN Profile**.
     8. In the **Connection request** popup window, select **OK**.
     9. If you did not enable [auto-connect ↗︎](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect), manually turn on the switch to **Connected**.



The Cloudflare One Client should show as **Connected**. The device is now connected to your organization and secured with Cloudflare Zero Trust.

[PreviousChoose an on-ramp](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/choose-on-ramp/)[NextMDM deployment](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/connect-devices-networks/mdm/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/secure-internet-traffic/connect-devices-networks/install-agent.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
