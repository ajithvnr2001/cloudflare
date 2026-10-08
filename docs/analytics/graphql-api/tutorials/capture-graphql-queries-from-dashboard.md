---
url: https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/
title: Capture GraphQL queries with Chrome DevTools \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:14.586602+00:00
---

# Capture GraphQL queries with Chrome DevTools · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /Tutorials
  5. /Capture GraphQL queries with Chrome DevTools



# Capture GraphQL queries with Chrome DevTools

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Using [Chrome DevTools ↗︎](https://developer.chrome.com/docs/devtools), you can capture the queries running behind the Cloudflare Dashboard analytics. In this example, we will focus on the Network Analytics dataset, but the same process can be applied to any other analytics available in your dashboard.

  1. In the Cloudflare dashboard, go to the **Network Analytics** page or any other analytics dashboard you are interested in seeing the GraphQL queries in.

[ Go to **Network analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/networking-insights/analytics/network-analytics/transport-analytics)

![Analytics tab](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2322,height=1090,format=webp/_astro/analytics-tab.sJIMwybT.png)

  2. Open the [Chrome Developer Tools ↗︎](https://developer.chrome.com/docs/devtools) and select **Inspect**.

![Chrome developer tools](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1470,height=960,format=webp/_astro/chrome-developer-tools.D4a36rnA.png)

  3. Select the **Network** tab in the Developer Tools panel.
  4. In the filter bar, type `graphql` to filter out the GraphQL requests. If no requests appear, try reloading the page. As the page reloads, several network requests will populate the **Network** tab. Look for requests that contain `graphql` in the name.

![Type graphql in the search field](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1258,height=1032,format=webp/_astro/search-field.BxHnt1F0.png)

  5. Select one of the GraphQL requests to open its details and go to the **Payload** tab. There you will find the GraphQL query. Select the query line and then **Copy value** to capture the query.

![Copy query value](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1110,height=740,format=webp/_astro/copy-value.BZMZMU5_.png)

  6. If you want to capture a new query, adjust the filters in the **Network analytics** dashboard and a new query will appear in the GraphQL requests.

![Create a new query](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1538,height=866,format=webp/_astro/new-query.TN7tG2lX.png)

You can now use this query as the basis for your API call. Refer to the [Get started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/) section for more information.

[PreviousUse GraphQL to create widgets](https://developers.cloudflare.com/analytics/graphql-api/tutorials/use-graphql-create-widgets/)[NextQuerying Access login events with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-access-login-events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
