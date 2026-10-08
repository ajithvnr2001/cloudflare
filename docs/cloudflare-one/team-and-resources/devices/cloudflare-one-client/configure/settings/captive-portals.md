---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/captive-portals/
title: Captive portal detection \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:56.928903+00:00
---

# Captive portal detection · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/captive-portals/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)[Configure](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/)

  4. /[Client settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/)
  5. /Captive portal detection



# Captive portal detection

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/captive-portals/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAllow users to connect to captive portals No user interaction required User interaction requiredHow captive portal detection worksLimitationsGet captive portal logs Related resources

Captive portals are used by public Wi-Fi networks (such as airports, coffee shops, and hotels) to make a user agree to their Terms of Service or provide payment before allowing access to the Internet. When a user connects to the Wi-Fi, the captive portal blocks all HTTPS traffic until the user completes a captive portal login flow in their browser. This prevents the Cloudflare One Client (formerly WARP) from connecting to Cloudflare. At the same time, the Cloudflare One Client creates [firewall rules](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic) on the device to send all traffic to Cloudflare. The user is therefore unable to access the captive portal login screen unless they temporarily disconnect the Cloudflare One Client.

## Allow users to connect to captive portals

To allow users to connect through a captive portal, administrators can configure the following device client settings:

### No user interaction required

  * Enable [Captive portal detection](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#captive-portal-detection). This allows the Cloudflare One Client to temporarily disconnect when it detects a captive portal on the network. For more details, refer to how captive portal detection works and its limitations.
  * Set [Device tunnel protocol](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol) to **MASQUE**. When using MASQUE, client traffic will look like standard HTTPS traffic and is therefore less likely to be blocked by captive portals.



### User interaction required

  * Enable [Lock device client switch](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch) and enable [Allow admin override codes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes). Users can contact the IT administrator for a one-time code that allows them to manually disconnect the Cloudflare One Client and connect to a portal.
  * For employees who travel, disable [Lock device client switch](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch) and set an [Auto connect](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect) duration. This allows the user to manually disconnect the Cloudflare One Client without contacting IT.



## How captive portal detection works

If the Cloudflare One Client cannot establish a connection to Cloudflare, it will:

  1. Start the captive portal timer.

  2. Send a series of requests to the [Cloudflare captive portal URLs](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#captive-portal) and other OS and browser-specific captive portal URLs. These requests are sent outside of the WARP tunnel.

  3. If a request is intercepted, the Cloudflare One Client assumes the network is behind a captive portal and fully opens the [system firewall](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic). While the firewall is open, all device traffic will bypass the Cloudflare One Client.

  4. Re-enable the firewall after the user successfully connects to the portal or after the timeout period expires.




## Limitations

  * Due to how captive portal detection works, it may be possible for an employee to spoof a captive portal in order to disconnect the Cloudflare One Client.
  * Some captive portals, particularly those on airlines, may be slow to respond and exceed the captive portal detection timeout. Users will likely see a [CF_CAPTIVE_PORTAL_TIMED_OUT](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#cf_captive_portal_timed_out) error when they try to connect. For context on the steps leading up to these errors, refer to [Connectivity status](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/).
  * The Cloudflare One Client may not be able to detect multi-stage captive portals, which redirect the user to different networks during the login process. Users will need to manually disconnect the Cloudflare One Client to get through the captive portal.
  * Some public Wi-Fi networks are incompatible with running the Cloudflare One Client: 
    * Captive portals that intercept all DNS traffic will block the Cloudflare One Client's [DoH connection](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#overview). Users will likely see a [CF_NO_NETWORK](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#cf_no_network) error after they login to the captive portal.
    * Captive portals that only allow HTTPS traffic will block the Cloudflare One Client's [Wireguard UDP connection](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#overview). Users will likely see a [CF_HAPPY_EYEBALLS_MITM_FAILURE](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/#cf_happy_eyeballs_mitm_failure) error after they login to the captive portal.



Check system notifications

Captive portal detection relies on system notifications to prompt the user. The login screen may not appear if a notification is dismissed or if the device is in Do Not Disturb mode, is screen recording, or if notifications for the Cloudflare One Client app are disabled in system settings.

## Get captive portal logs Beta

Feature availability

[Client modes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/) | [Zero Trust plans ↗︎](https://www.cloudflare.com/teams-pricing/)  
---|---  
All modes | All plans  
  
System | Availability | Minimum client version  
---|---|---  
Windows | ✅ | 2025.4.589.1  
macOS | ✅ | 2025.4.589.1  
Linux | ❌ |   
iOS | ❌ |   
Android | ❌ |   
ChromeOS | ❌ |   
  
Captive portal logs are used by Cloudflare Support to troubleshoot Cloudflare One Client captive portal issues. When an end user reports an issue with a captive portal, the IT administrator can ask the user to collect captive portal logs on their device. The administrator can then attach the logs to a Cloudflare Support ticket.

To get captive portal logs:

  1. Open a terminal window.

  2. Run the following command:
         
         warp-diag captive-portal

  3. When prompted with `You're currently connected via interface '<INTERFACE>' (<SSID>). Is this interface connected to the network causing issues?`, select **Yes** to confirm.




  1. Open the Cloudflare One Client.
  2. Go to **Settings** (gear icon) > **Preferences** > **Advanced**.
  3. Select **Collect Captive Portal Diag**.
  4. The Cloudflare One Client will ask if the device is connected (or attempting to connect) to the Wi-Fi network that is causing issues. Select **Yes** to confirm.



macOS limitation

On macOS, [**Automatically join this network** ↗︎](https://support.apple.com/guide/mac-help/wi-fi-settings-on-mac-mh11935/mac) should be enabled on the Wi-Fi network that is causing issues. This setting is enabled by default. If manually disabled, the captive portal diagnostic will fail to capture meaningful data and the device will not automatically reconnect to this network.

Once the diagnostic finishes running, the Cloudflare One Client will place a `warp-captive-portal-diag-<date>-<time>.zip` file on the user's desktop. The end user can now share this file with their IT administrator.

## Related resources

  * [Connectivity status](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/) \- Learn about the status messages displayed by the Cloudflare One Client during its connection process, and understand each stage as the client establishes a secure tunnel to Cloudflare.



[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/)[NextEmergency Disconnect](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/captive-portals.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
