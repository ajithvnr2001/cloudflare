---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/
title: JumpCloud \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:00.001786+00:00
---

# JumpCloud · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)[Deploy](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/)[Managed deployment](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/)

  4. /[Partners](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/)
  5. /JumpCloud



# JumpCloud

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWindowsmacOS

## Windows

  1. Log in to the [JumpCloud Admin Portal ↗︎](https://console.jumpcloud.com).

  2. Go to **Device Management** > **Software Management**.

  3. Select the **Windows** tab, then select **(+)**.

![Configuring the Cloudflare One Client in the JumpCloud Windows tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2154,height=1562,format=webp/_astro/jumpcloud.COKUk56X.png)

_Note: Labels in this image may reflect a previous product name._

  4. In the **Software Name** field, enter a unique display name.

  5. In the **Package ID** field, enter `warp`.

  6. Select **Install this software**.

  7. (Optional) Select **Keep software package up to date** to automatically update this app as updates become available.

  8. (Optional) Select **Allow end users to delay updates for up to one week** to avoid updates during a busy time.

  9. Select **save**.

  10. Select the device(s) you want to deploy the app to:

     * **Single device** : Go to the **Devices** tab and select the target device.
     * **Device group** : Go to the **Device Groups** tab and select the target device group.
  11. Select **save**.

  12. Select **save** again.




Verify that the Cloudflare One Client was installed by selecting the app and viewing the **Status** tab.

After deploying the Cloudflare One Client, you can check its connection progress using the [Connectivity status](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/) messages displayed in the Cloudflare One Client GUI.

## macOS

  1. Log in to the [JumpCloud Admin Portal ↗︎](https://console.jumpcloud.com).

  2. Go to **Device Management** > **Software Management**.

  3. Select the **Apple** tab, then select **(+)**.

![Configuring the Cloudflare One Client in the JumpCloud Apple tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1780,height=1286,format=webp/_astro/jumpcloud-mac.B_6biy3e.png)

_Note: Labels in this image may reflect a previous product name._

  4. In the **Software Description** field, enter a unique display name.

  5. In the **Software Package URL** , enter the URL location of the `Cloudflare_WARP_<VERSION>.pkg` file. If you do not already have the installer package, [download it here](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#macos).

  6. Select the device(s) you want to deploy the app to:

     * **Single device** : Go to the **Devices** tab and select the target device. To select all devices, select the checkbox next to **Type**.
     * **Device group** : Go to the **Device Groups** tab and select the target device group. To select all device groups, select the checkbox next to **Type**.
  7. Select **save** to install the client.




Verify that the Cloudflare One Client was installed by selecting the app and viewing the **Status** tab.

After deploying the Cloudflare One Client, you can check its connection progress using the [Connectivity status](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/) messages displayed in the Cloudflare One Client GUI.

[PreviousJamf](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jamf/)[NextKandji](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/kandji/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/jumpcloud.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
