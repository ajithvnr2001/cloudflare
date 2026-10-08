---
url: https://developers.cloudflare.com/flagship/sdk/server-provider/
title: TypeScript Server SDK \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:19.429523+00:00
---

# TypeScript Server SDK · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/sdk/server-provider/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /[OpenFeature SDK](https://developers.cloudflare.com/flagship/sdk/)
  4. /TypeScript Server SDK



# TypeScript Server SDK

Last updated Aug 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/flagship/sdk/server-provider/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupConfiguration optionsResponse cachingEvaluation contextAvailable hooksMigrate from another provider

The `FlagshipServerProvider` implements the OpenFeature server provider interface. The provider works in [Cloudflare Workers](https://developers.cloudflare.com/workers/), Node.js, and any server-side JavaScript runtime that supports the Fetch API.

Inside a Cloudflare Worker, you can pass the Flagship [binding](https://developers.cloudflare.com/flagship/binding/) directly to the provider. This avoids HTTP overhead and is the recommended approach. Outside of Workers, initialize the provider with an app ID and account ID.

## Setup

Pass the Flagship binding directly to the provider. This is the recommended approach inside a Worker.
    
    
    import { OpenFeature } from "@openfeature/server-sdk";
    import { FlagshipServerProvider } from "@cloudflare/flagship/server";
    
    export default {
    	async fetch(request, env) {
    		await OpenFeature.setProviderAndWait(
    			new FlagshipServerProvider({ binding: env.FLAGS }),
    		);
    
    		const client = OpenFeature.getClient();
    
    		const showNewCheckout = await client.getBooleanValue(
    			"new-checkout",
    			false,
    			{ targetingKey: "user-42", plan: "enterprise" },
    		);
    
    		if (showNewCheckout) {
    			return new Response("New checkout enabled!");
    		}
    
    		return new Response("Standard checkout.");
    	},
    };
    
    
    import { OpenFeature } from "@openfeature/server-sdk";
    import { FlagshipServerProvider } from "@cloudflare/flagship/server";
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		await OpenFeature.setProviderAndWait(
    			new FlagshipServerProvider({ binding: env.FLAGS }),
    		);
    
    		const client = OpenFeature.getClient();
    
    		const showNewCheckout = await client.getBooleanValue(
    			"new-checkout",
    			false,
    			{ targetingKey: "user-42", plan: "enterprise" },
    		);
    
    		if (showNewCheckout) {
    			return new Response("New checkout enabled!");
    		}
    
    		return new Response("Standard checkout.");
    	},
    };

Use an app ID, account ID, and an API token when running outside of a Worker (for example, in Node.js). Generate an [API token](https://developers.cloudflare.com/flagship/api-tokens/) from your Cloudflare account with Flagship Evaluate or Flagship App Evaluate permission.
    
    
    import { OpenFeature } from "@openfeature/server-sdk";
    import { FlagshipServerProvider } from "@cloudflare/flagship/server";
    
    await OpenFeature.setProviderAndWait(
    	new FlagshipServerProvider({
    		appId: "<APP_ID>",
    		accountId: "<ACCOUNT_ID>",
    		authToken: "<API_TOKEN>",
    	}),
    );
    
    const client = OpenFeature.getClient();
    
    const showNewCheckout = await client.getBooleanValue("new-checkout", false, {
    	targetingKey: "user-42",
    	plan: "enterprise",
    });
    
    
    import { OpenFeature } from "@openfeature/server-sdk";
    import { FlagshipServerProvider } from "@cloudflare/flagship/server";
    
    await OpenFeature.setProviderAndWait(
    	new FlagshipServerProvider({
    		appId: "<APP_ID>",
    		accountId: "<ACCOUNT_ID>",
    		authToken: "<API_TOKEN>",
    	}),
    );
    
    const client = OpenFeature.getClient();
    
    const showNewCheckout = await client.getBooleanValue("new-checkout", false, {
    	targetingKey: "user-42",
    	plan: "enterprise",
    });

## Configuration options

Option | Type | Required | Description  
---|---|---|---  
`binding` | `Flagship` | No | The Flagship binding from `env.FLAGS`. Use this inside a Worker for best performance. The binding handles authentication automatically.  
`appId` | `string` | No | The Flagship app ID from the Cloudflare dashboard. Required when not using a binding.  
`accountId` | `string` | No | Your Cloudflare account ID. Required when using `appId`.  
`authToken` | `string` | No | A Cloudflare [API token](https://developers.cloudflare.com/flagship/api-tokens/) with Flagship Evaluate or Flagship App Evaluate permission. Required when not using a binding.  
`fetchOptions` | `RequestInit` | No | Custom fetch options applied to HTTP requests.  
`timeout` | `number` | No | Request timeout in milliseconds. Defaults to `5000`.  
`retries` | `number` | No | Retry attempts on transient errors. Defaults to `1` and is capped at `10`.  
`retryDelay` | `number` | No | Delay between retries in milliseconds. Defaults to `1000` and is capped at `30000`.  
`cacheTtl` | `number` | No | Cache TTL in milliseconds. Enables response caching when greater than `0`.  
`cacheMaxSize` | `number` | No | Maximum cached entries. Defaults to `1000` when `cacheTtl` is set.  
  
Provide either `binding` or `appId`, `accountId`, and `authToken`.

## Response caching

Server-side response caching is off by default. Enable it with `cacheTtl` when you want repeated evaluations for the same flag, type, and evaluation context to reuse a recent result.
    
    
    new FlagshipServerProvider({
    	appId: "<APP_ID>",
    	accountId: "<ACCOUNT_ID>",
    	authToken: "<API_TOKEN>",
    	cacheTtl: 30_000,
    	cacheMaxSize: 1000,
    });

Use caching for high-traffic server applications that repeatedly evaluate the same flags for the same contexts. Cached values may be stale until the TTL expires, so keep the TTL short for flags that you expect to change during active rollouts. The provider does not cache disabled flags or errors.

## Evaluation context

OpenFeature uses an evaluation context to pass user attributes to the flag provider. The `targetingKey` field is the primary user identifier.

Pass additional attributes alongside `targetingKey` to match [targeting rules](https://developers.cloudflare.com/flagship/targeting/). For example, you can include `plan`, `country`, or any custom attribute your rules reference.

Use primitive context values such as strings, numbers, booleans, and `Date` objects. The provider rejects objects and arrays as invalid context.
    
    
    const value = await client.getBooleanValue("new-checkout", false, {
    	targetingKey: "user-42",
    	plan: "enterprise",
    	country: "US",
    });
    
    
    const value = await client.getBooleanValue("new-checkout", false, {
    	targetingKey: "user-42",
    	plan: "enterprise",
    	country: "US",
    });

## Available hooks

The SDK ships with two hooks that you can attach to the OpenFeature client.

  * **LoggingHook** — Logs structured information for every evaluation.
  * **TelemetryHook** — Captures timing and event data for observability.


    
    
    import { LoggingHook, TelemetryHook } from "@cloudflare/flagship/server";
    
    OpenFeature.addHooks(new LoggingHook(), new TelemetryHook());
    
    
    import { LoggingHook, TelemetryHook } from "@cloudflare/flagship/server";
    
    OpenFeature.addHooks(new LoggingHook(), new TelemetryHook());

## Migrate from another provider

If you use another OpenFeature-compatible provider (for example, LaunchDarkly or Flagsmith), switch to Flagship by replacing the provider initialization. No changes are needed at evaluation call sites.
    
    
    // Before
    await OpenFeature.setProviderAndWait(
    	new LaunchDarklyProvider({ sdkKey: "..." }),
    );
    
    // After
    await OpenFeature.setProviderAndWait(
    	new FlagshipServerProvider({
    		appId: "<APP_ID>",
    		accountId: "<ACCOUNT_ID>",
    		authToken: "<API_TOKEN>",
    	}),
    );
    
    
    // Before
    await OpenFeature.setProviderAndWait(
    	new LaunchDarklyProvider({ sdkKey: "..." }),
    );
    
    // After
    await OpenFeature.setProviderAndWait(
    	new FlagshipServerProvider({
    		appId: "<APP_ID>",
    		accountId: "<ACCOUNT_ID>",
    		authToken: "<API_TOKEN>",
    	}),
    );

[PreviousOverview](https://developers.cloudflare.com/flagship/sdk/)[NextTypeScript Client SDK](https://developers.cloudflare.com/flagship/sdk/client-provider/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/sdk/server-provider.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
