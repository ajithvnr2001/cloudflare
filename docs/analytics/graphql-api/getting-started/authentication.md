---
url: https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/
title: Authentication \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:13.219493+00:00
---

# Authentication · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)

  4. /[Get started](https://developers.cloudflare.com/analytics/graphql-api/getting-started/)
  5. /Authentication



# Authentication

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare separates service configuration by zone. When there are multiple accounts, each with many zones, it is important to restrict GraphQL Analytics API access to only those account and zone resources that are relevant for the task at hand.

To secure access to your GraphQL Analytics data, use a Cloudflare API key or token to authenticate an API request.

This table outlines the differences between Cloudflare API keys and tokens:

Authentication Method| Description  
---|---  
[API Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)| Cloudflare recommends API Tokens as the preferred way to interact with Cloudflare APIs. You can configure the scope of tokens to limit access to account and zone resources, and you can define the Cloudflare APIs to which the token authorizes access.  
[API Keys](https://developers.cloudflare.com/fundamentals/api/get-started/keys/)| Unique to each Cloudflare user and used only for authentication. API keys do not authorize access to accounts or zones. Use the Global API Key for authentication.  
  
To create and configure GraphQL Analytics API tokens, refer to [Configure an Analytics API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/).

To find and retrieve API keys, as well as edit HTTP headers for authentication in GraphiQL, refer to [Authenticate with a Cloudflare API key](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-key-auth/).

[PreviousOverview](https://developers.cloudflare.com/analytics/graphql-api/getting-started/)[NextConfigure an Analytics API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/graphql-api/getting-started/authentication/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
