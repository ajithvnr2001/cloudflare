---
url: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/sentinelone/
title: SentinelOne - Posture checks \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:07.343958+00:00
---

# SentinelOne - Posture checks · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/sentinelone/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/)
  5. /SentinelOne



# SentinelOne

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/sentinelone/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSet up SentinelOne as a service provider 1\. Obtain SentinelOne settings 2\. Add SentinelOne as a service provider 3\. Configure the posture checkDevice posture attributes Detect user risk behavior

Cloudflare One can integrate with SentinelOne to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from SentinelOne. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.

## Prerequisites

  * SentinelOne agent is deployed on the device.
  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/).




## Set up SentinelOne as a service provider

### 1\. Obtain SentinelOne settings

The following SentinelOne values are needed to set up the SentinelOne posture check:

  * API Token
  * REST API URL



To retrieve those values:

  1. Log in to your SentinelOne Dashboard.
  2. Go to **Settings** > **Users** > **Create new Service User**.
  3. Select **Create New Service User**.
  4. Enter a **Name** and **Expiration Date** and select **Next**.
  5. Set **Scope of Access** to _Viewer_.
  6. Select **Create User**. SentinelOne will generate an API Token for this user.
  7. Copy the **API Token** to a safe location.
  8. Select **Close**.
  9. Copy the **Rest API URL** from your browser's address bar (for example, `https://<S1-DOMAIN>.sentinelone.net`).



### 2\. Add SentinelOne as a service provider

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Service providers**.
  2. Select **Add new**.
  3. Select **SentinelOne**.
  4. Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.


  5. In **Client Secret** , enter your **API Token**.
  6. In **Rest API URL** , enter `https://<S1-DOMAIN>.sentinelone.net`.
  7. Choose a **Polling frequency** for how often Cloudflare One should query SentinelOne for information.
  8. Select **Test and save**.



### 3\. Configure the posture check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks** > **Service provider checks**.
  2. Select **Add a check**.
  3. Select the SentinelOne provider.
  4. Enter any name for the posture check.
  5. Configure the attributes required for the device to pass the posture check.
  6. Select **Save**.
  7. To test, go to **Insight** > **Logs** > **Posture logs** and verify that the service provider posture check is returning the expected results.



You can now use this posture check in a [device posture policy](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy).

## Device posture attributes

Device posture data is gathered from the SentinelOne Management APIs. For more information, refer to `https://<S1-DOMAIN>.sentinelone.net/api-doc/overview`.

Selector | Description  
---|---  
Infected | Whether the device is infected  
Active Threats | Number of active threats on the device  
Is Active | Whether the SentinelOne Agent is active  
Network status | Whether the SentinelOne Agent is connected to the SentinelOne service  
Operational State | The [operational state ↗︎](https://community.sentinelone.com/s/login/?ec=302&startURL=%2Fs%2Farticle%2F000005285) of the SentinelOne Agent.  
  
### Detect user risk behavior

SentinelOne provides endpoint detection and response (EDR) signals to determine [user risk score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/). User risk scores allow you to detect users that present security risks to your organization. For more information, refer to [Predefined risk behaviors](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#predefined-risk-behaviors).

[PreviousMicrosoft Endpoint Manager](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/microsoft/)[NextTanium](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/taniums2s/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/service-providers/sentinelone.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
