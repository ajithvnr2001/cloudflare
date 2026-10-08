---
url: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/taniums2s/
title: Tanium - Posture checks \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:07.465573+00:00
---

# Tanium - Posture checks · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/taniums2s/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/)
  5. /Tanium



# Tanium

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/taniums2s/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSet up Tanium as a service provider 1\. Get Tanium settings 2\. Add Tanium as a service provider 3\. Configure the posture checkDevice posture attributes

Cloudflare One can integrate with Tanium to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Tanium. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.

## Prerequisites

  * Either Tanium Cloud or on-premise installations of Tanium with the Benchmark entitlement
  * Tanium agent is deployed on the device.
  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Service providers](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/).




## Set up Tanium as a service provider

### 1\. Get Tanium settings

The following Tanium values are needed to set up the Tanium posture check:

  * Client Secret
  * REST API URL



To retrieve the client secret, create an API token:

  1. Log in to your Tanium instance.
  2. Go to **Administration** > **API Tokens**.
  3. Select **New API Token**.
  4. Set **Expire in days** to an appropriate value for your organization. When this token expires, all device posture results will begin to fail unless updated.
  5. Set **Trusted IP addresses** to `0.0.0.0/0`.
  6. Select **Save**.
  7. Copy the **Client Secret** to a safe place.



To retrieve the API URL, determine your Tanium Gateway root endpoint:

  * Tanium Cloud: `https://<customerName>-api.cloud.tanium.com/plugin/products/gateway/graphql`
  * Tanium On Prem: `https://<server>/plugin/products/gateway/graphql`



### 2\. Add Tanium as a service provider

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Service providers**.
  2. Select **Add new**.
  3. Select **Tanium**.
  4. Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.


  5. Enter the **Client Secret** and **REST API URL** you noted down above.
  6. Choose a **Polling frequency** for how often Cloudflare One should query Tanium for information.
  7. Select **Test and save**.



### 3\. Configure the posture check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks** > **Service provider checks**.
  2. Select **Add a check**.
  3. Select the Tanium provider.
  4. Enter any name for the posture check.
  5. Configure the attributes required for the device to pass the posture check.
  6. Select **Save**.
  7. To test, go to **Insight** > **Logs** > **Posture logs** and verify that the service provider posture check is returning the expected results.



You can now use this posture check in a [device posture policy](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy).

## Device posture attributes

Device posture data is gathered from [Tanium's EndpointRisk API ↗︎](https://developer.tanium.com/site/global/apis/graphql/spectaql/index.gsp#definition-EndpointRisk). To learn more about how scores are calculated, refer to the [Tanium risk score documentation ↗︎](https://help.tanium.com/bundle/ug_benchmark_cloud/page/benchmark/risk_score.html).

Selector | Description | Value  
---|---|---  
Total score | `totalScore` of the device. | `1` to `1000`  
Risk level | `riskLevel` of the device. | Low, medium, high, or critical  
EID last seen | Elapsed time since the device was last seen, based on its `datetime` attribute. | In the last 1 hour, 3 hours, 6 hours, 12 hours, 24 hours, 7 days, 30 days, or more than 30 days  
  
[PreviousSentinelOne](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/sentinelone/)[NextUptycs](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/uptycs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/service-providers/taniums2s.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
