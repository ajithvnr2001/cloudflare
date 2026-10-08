---
url: https://developers.cloudflare.com/pages/functions/plugins/graphql/
title: GraphQL \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:34.129353+00:00
---

# GraphQL · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/functions/plugins/graphql/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /…

[Functions](https://developers.cloudflare.com/pages/functions/)

  4. /[Pages Plugins](https://developers.cloudflare.com/pages/functions/plugins/)
  5. /GraphQL



# GraphQL

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/functions/plugins/graphql/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationUsage

The GraphQL Pages Plugin creates a GraphQL server which can respond to `application/json` and `application/graphql` `POST` requests. It responds with [the GraphQL Playground ↗︎](https://github.com/graphql/graphql-playground) for `GET` requests.

## Installation

npmyarnpnpmbun
    
    
    npm i @cloudflare/pages-plugin-graphql
    
    
    yarn add @cloudflare/pages-plugin-graphql
    
    
    pnpm add @cloudflare/pages-plugin-graphql
    
    
    bun add @cloudflare/pages-plugin-graphql

## Usage
    
    
    import graphQLPlugin from "@cloudflare/pages-plugin-graphql";
    import {
    	graphql,
    	GraphQLSchema,
    	GraphQLObjectType,
    	GraphQLString,
    } from "graphql";
    
    const schema = new GraphQLSchema({
    	query: new GraphQLObjectType({
    		name: "RootQueryType",
    		fields: {
    			hello: {
    				type: GraphQLString,
    				resolve() {
    					return "Hello, world!";
    				},
    			},
    		},
    	}),
    });
    
    export const onRequest: PagesFunction = graphQLPlugin({
    	schema,
    	graphql,
    });

This Plugin only exposes a single route, so wherever it is mounted is wherever it will be available. In the above example, because it is mounted in `functions/graphql.ts`, the server will be available on `/graphql` of your Pages project.

[PreviousGoogle Chat](https://developers.cloudflare.com/pages/functions/plugins/google-chat/)[NexthCaptcha](https://developers.cloudflare.com/pages/functions/plugins/hcaptcha/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/functions/plugins/graphql.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
