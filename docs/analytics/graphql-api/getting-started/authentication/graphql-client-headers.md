---
url: https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/
title: Configure GraphQL client endpoint and HTTP headers \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:13.256809+00:00
---

# Configure GraphQL client endpoint and HTTP headers · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)[Get started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/)

  4. /[Authentication](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/)
  5. /Configure GraphQL client endpoint and HTTP headers



# Configure GraphQL client endpoint and HTTP headers

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/graphql-client-headers/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

  1. Launch [GraphiQL ↗︎](https://www.gatsbyjs.com/docs/how-to/querying-data/running-queries-with-graphiql/).

  2. Select **Edit HTTP Headers**. ![Clicking Edit HTTP Headers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1018,height=721,format=webp/_astro/GraphiQL-edit-http-headers.Cc0SaBrH.png) The **Edit HTTP Headers** window appears. ![Editing HTTP Headers Window](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=921,height=212,format=webp/_astro/GraphiQL-edit-http-headers-window.D6rNIUCL.png)

  3. Select **Add Header** to configure authentication. You can use Cloudflare Analytics API token authentication (recommended) or Cloudflare API key authentication.

     * **Token authentication** :

Enter **Authorization** in the **Header Name** field, and enter `Bearer {your-analytics-token}` in the **Header value** field, then select **Save**.

![Editing HTTP Headers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=606,height=148,format=webp/_astro/GraphiQL-edit-http-headers-token.BRr3JTFE.png)
     * **Key authentication** :

Enter `X-AUTH-EMAIL` in the **Header name** field and your email address registered with Cloudflare in the **Header value** field, and select **Save**.  


Select **Add Header** to add a second header. Enter `X-AUTH-KEY` in the **Header Name** field, and paste your Global API Key in the **Header value** field, then select **Save**.  


  4. Select anywhere outside the **Edit HTTP Headers** window in GraphiQL to close it and return to the main GraphiQL display.

  5. Enter `https://api.cloudflare.com/client/v4/graphql` in the **GraphQL Endpoint** field. ![Editing GraphQL Endpoint](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1007,height=712,format=webp/_astro/GraphiQL-response-pane.jm8FGlXL.png)




Note

The right-side response pane is empty when you enter your information correctly. An error displays when there are problems with your header credentials.

Now that you have configured authentication, you are ready to run queries using GraphiQL.

[PreviousAuthenticate with a Cloudflare API key](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-key-auth/)[NextQuerying basics](https://developers.cloudflare.com/analytics/graphql-api/getting-started/querying-basics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/getting-started/authentication/graphql-client-headers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
