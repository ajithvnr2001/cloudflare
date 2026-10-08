---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/
title: Antivirus \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:48.452814+00:00
---

# Antivirus · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Reusable components[Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/)

  4. /[Cloudflare One Client checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)
  5. /Antivirus



# Antivirus

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesEnable the antivirus checkValidate antivirus status Windows

The Antivirus device posture attribute checks if any antivirus software is installed and active on a device. The Cloudflare One Client queries the [Windows Security Center API ↗︎](https://learn.microsoft.com/en-us/windows/win32/api/iwscapi/ne-iwscapi-wsc_security_product_state) to determine the state of registered security products. For the posture check to pass, Windows Security Center must report that a security product is turned on and up to date.

## Prerequisites

  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Cloudflare One Client Checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/).




## Enable the antivirus check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks**.
  2. Go to **Cloudflare One Client checks** and select **Add a check**.
  3. Select **Antivirus**.
  4. Enter a descriptive name for the check.
  5. Select your operating system.
  6. (Optional) Set the maximum number of days allowed since the last antivirus signature update. If the device exceeds this limit (for example, you set 30 days but it has been 31 days since the last update), the device will fail the posture check.
  7. Select **Save**.



Next, go to **Insights** > **Logs** > **Posture logs** and verify that the antivirus check is returning the expected results.

## Validate antivirus status

You can use the following commands to validate if the posture check is working as expected.

### Windows

  1. Open a PowerShell window.

  2. List all installed antivirus products registered with Windows Security Center:
         
         Get-WmiObject -Namespace "root\SecurityCenter2" -ClassName "AntiVirusProduct"
         
         <redacted>
         displayName              : Windows Defender
         instanceGuid             : {00000000-0000-0000-0000-000000000000}
         pathToSignedProductExe   : windowsdefender://
         pathToSignedReportingExe : %ProgramFiles%\Windows Defender\MsMpeng.exe
         productState             : 397568
         timestamp                : Fri, 09 Jan 2026 12:00:00 GMT
         PSComputerName           : ENDPOINT-01

  3. Microsoft does not support decoding the `productState` from the `SecurityCenter2` namespace. To verify that an antivirus product is active, open the [Windows Security app ↗︎](https://support.microsoft.com/en-us/windows/stay-protected-with-the-windows-security-app-2ae0363d-0ada-c064-8b56-6a39afb6a963). The **Virus & threat protection** panel should say `No action needed` with a green checkmark.

To determine which antivirus product is running, select **Virus & threat protection** > **Manage providers**. You will see the name of the antivirus product (for example, `Windows Defender Antivirus`) and its current state.

  4. If you configured a maximum antivirus signature age in your posture check, compare the `timestamp` in the PowerShell output against the current system time. If the difference exceeds the configured number of days, the posture check will fail.




[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)[NextApplication check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/posture-checks/client-checks/antivirus.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
