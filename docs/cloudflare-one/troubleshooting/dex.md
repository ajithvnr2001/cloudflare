---
url: https://developers.cloudflare.com/cloudflare-one/troubleshooting/dex/
title: DEX \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:18.429912+00:00
---

# DEX · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/troubleshooting/dex/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Troubleshooting](https://developers.cloudflare.com/cloudflare-one/troubleshooting/)
  4. /DEX



# DEX

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/troubleshooting/dex/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewData visibility No data displayed for certain users Fleet status not updatingRemote captures Remote capture fails to startMore DEX resources

Review common troubleshooting scenarios for Digital Experience Monitoring (DEX).

## Data visibility

### No data displayed for certain users

If you do not see DEX data for specific users in your organization, verify the following:

  * **Client version** : Ensure the users are running a version of the Cloudflare One Client that supports DEX.
  * **DEX enabled** : Confirm that DEX is enabled for the [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) assigned to those users.
  * **Traffic routing** : DEX requires that traffic to Cloudflare's orchestration API is not blocked by local firewalls or SSL-inspecting proxies.



### Fleet status not updating

The Fleet status dashboard can take several minutes to reflect changes in device connectivity. If a device remains in an incorrect state, try disconnecting and reconnecting the Cloudflare One Client to force a status update.

## Remote captures

### Remote capture fails to start

Remote captures require the Cloudflare One Client to be connected and able to communicate with the Cloudflare control plane. If a capture fails to start:

  * Verify the device status in the Zero Trust dashboard.
  * Ensure the device has sufficient disk space to store the capture files before upload.
  * Check for any local firewall rules that might be blocking the capture command.



* * *

## More DEX resources

For more information, refer to the full DEX documentation.

[DEX troubleshooting ❯](https://developers.cloudflare.com/cloudflare-one/insights/dex/troubleshooting/)

[PreviousBrowser Isolation](https://developers.cloudflare.com/cloudflare-one/troubleshooting/browser-isolation/)[NextEmail Security](https://developers.cloudflare.com/cloudflare-one/troubleshooting/email-security/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/troubleshooting/dex.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
