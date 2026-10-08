---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/
title: Device serial numbers \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:48.855724+00:00
---

# Device serial numbers · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Reusable components[Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/)

  4. /[Cloudflare One Client checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)
  5. /Device serial numbers



# Device serial numbers

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCreate a list of serial numbersValidate the serial number macOS Windows Linux iOS, Android and ChromeOS

Cloudflare One allows you to build Zero Trust rules based on device serial numbers. You can create these rules so that access to applications is granted only to users connecting from company devices.

## Prerequisites

  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Cloudflare One Client Checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/).




## Create a list of serial numbers

To create rules based on device serial numbers, you first need to create a [Gateway List](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) of numbers.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Lists**.

  2. Select **Create manual list** or **Upload CSV**. For larger teams, we recommend uploading a CSV or using Cloudflare's [API endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/list/).

  3. Give your list a descriptive name, as this name will appear when configuring your policies.

  4. Set **List Type** to _Serial numbers_.

  5. Enter the serial numbers of the devices your team manages, or upload your CSV file.

  6. Select **Save**.




You can now create an [Access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) or a Gateway [network policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/common-policies/#enforce-device-posture) that checks if the device presents a serial number on your list. In Access, the serial number check will appear as a _Device Posture - Serial Number List_ selector. In Gateway, your serial number list will appear in the **Value** dropdown when you choose the [Passed Device Posture Check](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/#device-posture) selector.

## Validate the serial number

You can use the following commands to check the serial number of your device. The results can help you validate if the posture check is working as expected.

### macOS

  1. Open a terminal window.

  2. Use the `system_profiler` command to check for the value of `SPHardwareDataType` and retrieve the serial number.
         
         system_profiler SPHardwareDataType | grep 'Serial Number'




### Windows

  1. Open a PowerShell window.

  2. Use the `Get-CimInstance` command to get the SerialNumber property of the `Win32_BIOS` class.
         
         Get-CimInstance Win32_BIOS




### Linux

  1. Open a Terminal Window

  2. Use the `dmidecode` command to get the version property `system-serial-number`.
         
         sudo dmidecode -s system-serial-number




### iOS, Android and ChromeOS

Serial number checks are not supported on mobile devices. You can identify mobile devices by a [unique client ID](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/device-uuid) instead of by serial number.

[PreviousClient certificate](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/client-certificate/)[NextDevice UUID](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/device-uuid/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
