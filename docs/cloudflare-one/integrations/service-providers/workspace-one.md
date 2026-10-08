---
url: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/
title: Workspace ONE \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:08.020790+00:00
---

# Workspace ONE · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/)
  5. /Workspace ONE



# Workspace ONE

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/workspace-one/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Obtain Workspace ONE Settings2\. Add Workspace ONE as a service provider3\. Configure the posture checkDevice posture attributes

Cloudflare One can integrate with Workspace ONE to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Workspace ONE. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.

## Prerequisites

  * Workspace ONE agent is deployed on the device.
  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/).




## 1\. Obtain Workspace ONE Settings

The following Workspace ONE values are needed to set up the Workspace ONE posture check:

  * ClientID
  * Client Secret
  * REST API URL
  * Region-Specific token URL



To retrieve those values:

  1. Log in to your Workspace ONE dashboard.
  2. Go to **Groups & Settings** > **Configurations**.
  3. Enter `OAuth` in the search bar labeled **Enter a name or category**.
  4. Select **OAuth Client Management** in the results. The OAuth Client Management screen displays.
  5. Select **Add**.
  6. Enter values for the **Name** , **Description** , **Organization Group** , and **Role**.
  7. Ensure that the **Status** is **Enabled**.
  8. Select **Save**.
  9. Copy the **Client ID** and **Client Secret** to a safe place.
  10. To obtain your REST API URL, gp tp **Groups & Settings** > **All Settings** > **System** > **Advance** > **Site URLs** > **REST API URL**.
  11. Retrieve the Region-Specific Token URL from Workspace ONE and copy it to a safe place.



## 2\. Add Workspace ONE as a service provider

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Service providers**.
  2. Select **Add new**.
  3. Select **Workspace ONE**.
  4. Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.


  5. Enter the **Client ID** and **Client secret** you noted down above.
  6. Select a **Polling frequency** for how often Cloudflare One should query Workspace ONE for information.
  7. Enter the **Region-specific token URL** and **REST API URL** you noted down above.
  8. Select **Test and save**.



## 3\. Configure the posture check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks** > **Service provider checks**.
  2. Select **Add a check**.
  3. Select the Workspace ONE provider.
  4. Enter any name for the posture check.
  5. Configure the attributes required for the device to pass the posture check.
  6. Select **Save**.
  7. To test, go to **Insight** > **Logs** > **Posture logs** and verify that the service provider posture check is returning the expected results.



You can now use this posture check in a [device posture policy](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy).

## Device posture attributes

Workspace ONE posture checks work with the [Compliance flags ↗︎](https://docs.vmware.com/en/VMware-Workspace-ONE-UEM/services/UEM_Managing_Devices/GUID-CompliancePolicies.html) in Workspace ONE. All compliance tests must pass for the device to be considered compliant.

[PreviousUptycs](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/uptycs/)[NextRoles and permissions](https://developers.cloudflare.com/cloudflare-one/roles-permissions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/service-providers/workspace-one.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
