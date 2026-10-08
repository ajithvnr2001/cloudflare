---
url: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/kolide/
title: Kolide \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:06.902886+00:00
---

# Kolide · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/kolide/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/)
  5. /Kolide



# Kolide

Last updated Aug 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/kolide/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSet up Kolide as a service provider 1\. Create a Client Secret in Kolide 2\. Add Kolide as a service provider 3\. Configure the posture checkDevice posture attributes

Cloudflare One can integrate with Kolide to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Kolide. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.

## Prerequisites

  * Kolide agent is deployed on the device.
  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/).




## Set up Kolide as a service provider

### 1\. Create a Client Secret in Kolide

  1. Log in to your Kolide dashboard.
  2. Select your profile and go to **Settings** > **Developers**.
  3. Select **Create New Key**.
  4. Enter a **Key Name** and select **Save**.
  5. Copy the **Secret token** to a safe place. This will be your Client Secret.



### 2\. Add Kolide as a service provider

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Service providers**.
  2. Select **Add new**.
  3. Select **Kolide**.
  4. Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.


  5. Enter the **Client secret** you noted down above.
  6. Choose a **Polling frequency** for how often Cloudflare One should query Kolide for information.
  7. Select **Test and save**.



### 3\. Configure the posture check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks** > **Service provider checks**.
  2. Select **Add a check**.
  3. Select the Kolide provider.
  4. Enter any name for the posture check.
  5. Configure the attributes required for the device to pass the posture check.
  6. Select **Save**.
  7. To test, go to **Insight** > **Logs** > **Posture logs** and verify that the service provider posture check is returning the expected results.



You can now use this posture check in a [device posture policy](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy).

## Device posture attributes

Device posture data is gathered from the [Kolide API ↗︎](https://kolideapi.readme.io/reference/get_devices-id).

Selector | Description  
---|---  
Auth state | The authorization status of the device, one of: 'Good', 'Notified', 'Will Block', or 'Blocked'  
  
[PreviousCrowdStrike](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/crowdstrike/)[NextMicrosoft Endpoint Manager](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/service-providers/kolide.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
