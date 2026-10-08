---
url: https://developers.cloudflare.com/changelog/post/2026-06-29-warp-linux-ga/
title: Cloudflare One Client for Linux (version 2026.6.822.0) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:59.894532+00:00
---

# Cloudflare One Client for Linux (version 2026.6.822.0) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-29-warp-linux-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 29, 2026

## Cloudflare One Client for Linux (version 2026.6.822.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-29-warp-linux-ga/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

  * The client now applies DNS search suffixes configured in your [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles) / [network policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies). Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See [DNS search suffixes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) for details.
  * Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See [Hardware-backed registration](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/) for details.
  * Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.
  * Added new warp-cli debug commands for interactive connection diagnosis. See [Extra debug logging](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging) for details.
  * The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.
  * Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated [Cloudflare One MDM documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs) for details.



**Additional changes and improvements**

  * Starting with 2026.6.822.0, the client unifies all API requests under the `api.devices.cloudflare.com` SNI, where previously both `zero-trust-client.cloudflareclient.com` and `notifications.cloudflareclient.com` were used. Review [Cloudflare One Client with firewall](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/) to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.
  * [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) functionality using the Cloudflare One Client is now supported on RHEL 9 and 10.
  * Cloudflare Mesh now supports [hostname-based routing](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes).
  * Client Certificate device-posture checks now support template variables (e.g. `${serial_number}`, `${device_uuid}`) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.
  * Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the system display settings.
  * Path MTU Discovery (PMTUD) is now enabled by default.
  * Fixed the in-client captive-portal browser rendering a blank "Success" page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.
  * Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.
  * Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.
  * Fixed an issue where some Debian releases experienced inaccurate version reporting for posture checks.
  * Users can now register with team names in any case format without errors.
  * New UI fixes 
    * Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.
    * Added a re-auth button and banner to the home screen so users don't miss it when their session expires.
    * Added clear error messaging when the Cloudflare certificate needs to be installed.
    * Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.
    * New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.
    * Added ability to configure proxy mode for consumer users.
    * Added back the option to quit for consumer users.



For RHEL deployments, this release introduces a dependency on the [Extra Packages for Enterprise Linux](https://docs.fedoraproject.org/en-US/epel/) repository (EPEL). The EPEL repository provides packages that support the captive portal detection’s in-app browser authentication and system tray icon. See [Getting started with EPEL](https://docs.fedoraproject.org/en-US/epel/getting-started/) for instructions on enabling EPEL.

**Known issues**

  * Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.


