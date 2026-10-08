---
url: https://developers.cloudflare.com/api-shield/management-and-monitoring/api-routing/
title: API Routing \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:17.781191+00:00
---

# API Routing · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/management-and-monitoring/api-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /Management and Monitoring
  4. /API Routing



# API Routing

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/management-and-monitoring/api-routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProcess Create a route Verify a routeAvailabilityLimitations

API Shield Routing allows you to expose a single external API that routes requests to different back-end services, even when those services use different paths or hostnames than your zone.

Note

The term **Source Endpoint** refers to the endpoint managed by API Shield in Endpoint Management. The term **Target Endpoint** refers to the ultimate destination the request is sent to by the Routing feature.

## Process

You must add Source Endpoints to Endpoint Management through established methods, including [uploading a schema](https://developers.cloudflare.com/api-shield/security/schema-validation/#add-validation-by-uploading-a-schema), via [API Discovery](https://developers.cloudflare.com/api-shield/security/api-discovery/), or by [adding manually](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/#add-endpoints-manually), before creating a route.

To create a route, you will need the operation ID of the Source Endpoint. To find the operation ID in the dashboard:

  1. In the Cloudflare dashboard, go to the **Web Assets** page.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. In the **Operations** tab, filter the operations to find your **Source Endpoint**.

  3. Expand the row for your Source Endpoint and note the **operation ID** field.

  4. Select the copy icon to copy the operation ID to your clipboard.




Once your Source Endpoints are added to Endpoint Management, use the following steps to create and verify routes on any given operation ID:

### Create a route

  1. In the Cloudflare dashboard, go to the **Web Assets** page.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. In the operations list, select an existing endpoint and expand its details.

  3. Under **Routing** , select **Create route**.

  4. Enter the target URL or IP address to route your endpoint to.

  5. Select **Deploy route**.




Note

You can reorder path variables if they are present. For example, you can route `/api/{var1}/users/{var2}` to `/{var2}/users/{var1}`. Segments of the path that are not variables may be added or omitted entirely.

You can also edit or delete a route by selecting **Edit route** on an existing route.

### Verify a route

After sending a request to your Source Endpoint, you should see the contents of the back-end service as if you called the Target Endpoint directly.

If API Shield returns unexpected results, check your Source Endpoint host, method, and path and [verify the Route](https://developers.cloudflare.com/api-shield/management-and-monitoring/api-routing/#verify-a-route) to ensure the Target Endpoint value is correct.

## Availability

API Shield Routing is currently in an open beta and is only available for Enterprise customers subscribed to API Shield. Enterprise customers who have not purchased API Shield can preview [API Shield as a non-contract service ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield) in the Cloudflare dashboard or by contacting your account team.

## Limitations

The Target Endpoint cannot be routed to a Worker if the route is to the same zone.

You cannot change the method of a request. For example, a `GET` Source Endpoint will always send a `GET` request to the Target Endpoint.

You must use all of the variables in the Target Endpoint that appear in the Source Endpoint. For example, routing `/api/{var1}/users/{var2}` to `/api/users/{var2}` is not allowed and will result in an error since `{var1}` is present in the Source Endpoint but not in the Target Endpoint.

[PreviousSession identifiers](https://developers.cloudflare.com/api-shield/management-and-monitoring/session-identifiers/)[NextBuild developer portals](https://developers.cloudflare.com/api-shield/management-and-monitoring/developer-portal/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/management-and-monitoring/api-routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
