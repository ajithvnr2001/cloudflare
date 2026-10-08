---
url: https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/
title: The best way to do MCP auth just got better: Workers OAuth Provider goes v1, with a new split API and full support for MCP 2026-07-28 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:18.605140+00:00
---

# The best way to do MCP auth just got better: Workers OAuth Provider goes v1, with a new split API and full support for MCP 2026-07-28 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2026

## The best way to do MCP auth just got better: Workers OAuth Provider goes v1, with a new split API and full support for MCP 2026-07-28

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cloudflare/workers-oauth-provider` ↗︎](https://github.com/cloudflare/workers-oauth-provider) is now v1, with a new split API. One Worker acts as the authorization server: it signs users in and issues tokens. Your MCP server acts as the resource server, and can run in another Worker. It validates each token with the authorization server over a [Service Binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/), without crossing the public Internet.

  * It supports the [MCP 2026-07-28 authorization specification ↗︎](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), including [Client ID Metadata Documents ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#client-id-metadata-documents) and [issuer identification ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#authorization-response-issuer). It still works with older clients, including those using [Dynamic Client Registration ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#dynamic-client-registration).
  * `insufficientScope()` gives you [step-up authorization ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#scopes-and-step-up-authorization) in one line.
  * The authorization server and the resource server can run in [different Workers ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/resource-servers.md#separate-workers) with different [WAF](https://developers.cloudflare.com/waf/) and [rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) rules.
  * One authorization server can issue tokens for [many MCP servers ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/authorization-server.md#resources-and-token-audiences).
  * A [migration skill ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/skills/migrate-to-1.0/SKILL.md) ships in the npm package so a coding agent can perform the upgrade.



#### The split API
    
    
    import {
    	OAuthAuthorizationServer,
    	OAuthResourceServer,
    	insufficientScope,
    } from "@cloudflare/workers-oauth-provider";
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    // auth-server Worker: signs users in and issues tokens for both MCP servers.
    const authorizationServer = new OAuthAuthorizationServer({
    	issuer: "https://auth.example.com",
    	resources: [
    		"https://calendar.example.com/mcp",
    		"https://drive.example.com/mcp",
    	],
    	scopesSupported: ["calendar:read", "calendar:write", "offline_access"],
    	clientIdMetadataDocumentEnabled: true,
    });
    
    export class AuthServer extends WorkerEntrypoint {
    	fetch(request) {
    		if (new URL(request.url).pathname === "/authorize") {
    			return showConsent(request, this.env);
    		}
    		return authorizationServer.fetch(request, this.env, this.ctx);
    	}
    
    	validateToken(resource, token) {
    		return authorizationServer.validateToken(resource, token, this.env);
    	}
    }
    
    // calendar MCP Worker: checks tokens with AuthServer over a Service Binding.
    export const calendar = new OAuthResourceServer({
    	resourceMetadata: {
    		resource: "https://calendar.example.com/mcp",
    		authorization_servers: ["https://auth.example.com"],
    	},
    	requiredScopes: ["calendar:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			if (
    				request.method === "POST" &&
    				!ctx.auth.scope.includes("calendar:write")
    			) {
    				return insufficientScope(ctx.auth, ["calendar:read", "calendar:write"]);
    			}
    			return handleMcp(request, ctx.props);
    		},
    	},
    });
    
    
    import {
    	OAuthAuthorizationServer,
    	OAuthResourceServer,
    	insufficientScope,
    } from "@cloudflare/workers-oauth-provider";
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    // auth-server Worker: signs users in and issues tokens for both MCP servers.
    const authorizationServer = new OAuthAuthorizationServer<Env>({
    	issuer: "https://auth.example.com",
    	resources: [
    		"https://calendar.example.com/mcp",
    		"https://drive.example.com/mcp",
    	],
    	scopesSupported: ["calendar:read", "calendar:write", "offline_access"],
    	clientIdMetadataDocumentEnabled: true,
    });
    
    export class AuthServer extends WorkerEntrypoint<Env> {
    	fetch(request: Request) {
    		if (new URL(request.url).pathname === "/authorize") {
    			return showConsent(request, this.env);
    		}
    		return authorizationServer.fetch(request, this.env, this.ctx);
    	}
    
    	validateToken(resource: string, token: string) {
    		return authorizationServer.validateToken(resource, token, this.env);
    	}
    }
    
    // calendar MCP Worker: checks tokens with AuthServer over a Service Binding.
    export const calendar = new OAuthResourceServer<Env, AuthProps>({
    	resourceMetadata: {
    		resource: "https://calendar.example.com/mcp",
    		authorization_servers: ["https://auth.example.com"],
    	},
    	requiredScopes: ["calendar:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			if (
    				request.method === "POST" &&
    				!ctx.auth.scope.includes("calendar:write")
    			) {
    				return insufficientScope(ctx.auth, ["calendar:read", "calendar:write"]);
    			}
    			return handleMcp(request, ctx.props);
    		},
    	},
    });

In the example, `env.AUTH_SERVER.validateToken` is that Service Binding call. The calendar Worker needs no KV namespace of its own.
    
    
    {
    	"name": "calendar-mcp",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"services": [
    		{
    			"binding": "AUTH_SERVER",
    			"service": "auth-server",
    			"entrypoint": "AuthServer",
    		},
    	],
    }
    
    
    name = "calendar-mcp"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[services]]
    binding = "AUTH_SERVER"
    service = "auth-server"
    entrypoint = "AuthServer"

`OAuthResourceServer` publishes the [RFC 9728 ↗︎](https://datatracker.ietf.org/doc/html/rfc9728) protected resource metadata that MCP clients use to find your authorization server. It answers requests without a token with a `401` challenge that points to that metadata. It also rejects tokens issued for any other resource.

You can still use `OAuthProvider` as both the authorization server and the MCP server. For most 0.x deployments, the only required change is to add `resourceMetadata: { resource }`.

#### Other updates and helpers

  * [Consent page ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/consent-page.md) and [upstream sign-in ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/upstream-sign-in.md) helpers implement the MCP confused deputy protections.
  * [Sliding refresh token expiry ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#sliding-expiry) with `refreshTokenIdleTTL`.
  * [Resumable KV cleanup ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#kv-cleanup) with `purgeExpiredData()`.
  * An [internal reason ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/advanced-configuration.md#the-internal-reason) on every error passed to `onError`.



#### Upgrade with the migration skill

npmyarnpnpmbun
    
    
    npm i @cloudflare/workers-oauth-provider@latest
    
    
    yarn add @cloudflare/workers-oauth-provider@latest
    
    
    pnpm add @cloudflare/workers-oauth-provider@latest
    
    
    bun add @cloudflare/workers-oauth-provider@latest

Point your coding agent at `node_modules/@cloudflare/workers-oauth-provider/skills/migrate-to-1.0/SKILL.md`, or follow the [migration guide ↗︎](https://github.com/cloudflare/workers-oauth-provider/blob/main/docs/migration-1.0.md).

For both Workers in full, refer to the [split Workers example ↗︎](https://github.com/cloudflare/workers-oauth-provider/tree/main/examples/split-workers).
