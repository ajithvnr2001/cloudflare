---
url: https://developers.cloudflare.com/flagship/sdk/client-provider/
title: TypeScript Client SDK \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:18.662046+00:00
---

# TypeScript Client SDK · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/sdk/client-provider/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /[OpenFeature SDK](https://developers.cloudflare.com/flagship/sdk/)
  4. /TypeScript Client SDK



# TypeScript Client SDK

Last updated Aug 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/flagship/sdk/client-provider/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewprefetchFlagsSetupConfiguration optionsWhen to use the client provider

The `FlagshipClientProvider` implements the OpenFeature web provider interface for browser applications. It pre-fetches a declared set of flag values on initialization and resolves evaluations synchronously from an in-memory cache.

This makes the provider suitable for client-side rendering where synchronous access to flag values is required.

Caution

We do not recommend using the client provider in public-facing apps right now. It requires a Cloudflare API token, which would be exposed in client-side code and visible to anyone who inspects your application. We are working on a safer solution for client-side flag evaluation — in the meantime, use the [Worker binding](https://developers.cloudflare.com/flagship/binding/) or the [TypeScript server SDK](https://developers.cloudflare.com/flagship/sdk/server-provider/).

## prefetchFlags

`prefetchFlags` is a required array of flag keys that the provider fetches during initialization and on every context change. Only flags listed in this array are available for synchronous evaluation — any flag key not included returns a `FLAG_NOT_FOUND` error at resolution time.

**Fetch behavior:**

  * **On initialization** — all flags in `prefetchFlags` are fetched in parallel and stored in an in-memory cache. The provider transitions to `READY` once all fetches complete (individual failures are non-fatal).
  * **On context change** — the cache is invalidated and all flags are re-fetched for the new context. This is required by the [static context paradigm ↗︎](https://openfeature.dev/specification/glossary/#static-context-paradigm) used by the OpenFeature web SDK, where context is set globally and providers are expected to re-evaluate when it changes.
  * **At resolution time** — evaluations are served synchronously from the cache. No network request is made during `getBooleanValue`, `getStringValue`, etc.



## Setup

The following example initializes the provider with a set of pre-fetched flags and evaluates them in a browser application.
    
    
    import { OpenFeature } from "@openfeature/web-sdk";
    import { FlagshipClientProvider } from "@cloudflare/flagship/web";
    
    await OpenFeature.setProviderAndWait(
    	new FlagshipClientProvider({
    		appId: "<APP_ID>",
    		accountId: "<ACCOUNT_ID>",
    		authToken: "<API_TOKEN>",
    		prefetchFlags: ["promo-banner", "dark-mode", "max-uploads"],
    	}),
    );
    
    // Set evaluation context globally. The provider re-fetches all prefetchFlags
    // whenever the context changes.
    await OpenFeature.setContext({ targetingKey: "user-42", plan: "enterprise" });
    
    const client = OpenFeature.getClient();
    
    // Synchronous — served from the in-memory cache.
    const showBanner = client.getBooleanValue("promo-banner", false);
    
    if (showBanner) {
    	document.getElementById("banner").style.display = "block";
    }
    
    
    import { OpenFeature } from "@openfeature/web-sdk";
    import { FlagshipClientProvider } from "@cloudflare/flagship/web";
    
    await OpenFeature.setProviderAndWait(
    	new FlagshipClientProvider({
    		appId: "<APP_ID>",
    		accountId: "<ACCOUNT_ID>",
    		authToken: "<API_TOKEN>",
    		prefetchFlags: ["promo-banner", "dark-mode", "max-uploads"],
    	}),
    );
    
    // Set evaluation context globally. The provider re-fetches all prefetchFlags
    // whenever the context changes.
    await OpenFeature.setContext({ targetingKey: "user-42", plan: "enterprise" });
    
    const client = OpenFeature.getClient();
    
    // Synchronous — served from the in-memory cache.
    const showBanner = client.getBooleanValue("promo-banner", false);
    
    if (showBanner) {
    	document.getElementById("banner").style.display = "block";
    }

Note

`getBooleanValue` on the client provider is synchronous and does not require `await`, unlike the [TypeScript server SDK](https://developers.cloudflare.com/flagship/sdk/server-provider/).

## Configuration options

Option | Type | Required | Description  
---|---|---|---  
`appId` | `string` | Yes | The Flagship app ID from the Cloudflare dashboard.  
`accountId` | `string` | Yes | Your Cloudflare account ID.  
`authToken` | `string` | Yes | A Cloudflare [API token](https://developers.cloudflare.com/flagship/api-tokens/) with Flagship Evaluate or Flagship App Evaluate permission.  
`fetchOptions` | `RequestInit` | No | Custom fetch options applied to HTTP requests.  
`timeout` | `number` | No | Request timeout in milliseconds. Defaults to `5000`.  
`retries` | `number` | No | Retry attempts on transient errors. Defaults to `1` and is capped at `10`.  
`retryDelay` | `number` | No | Delay between retries in milliseconds. Defaults to `1000` and is capped at `30000`.  
`prefetchFlags` | `string[]` | Yes | Flag keys to fetch on initialization and on every context change. Flags not in this list return `FLAG_NOT_FOUND` at evaluation time.  
  
## When to use the client provider

Use the client provider in browser applications, single-page apps, or any client-side JavaScript environment.

Evaluations are synchronous, so they do not block rendering. Flag values are fetched once during initialization and re-fetched whenever the evaluation context changes. To force a refresh, update the context via `OpenFeature.setContext(...)`.

[PreviousTypeScript Server SDK](https://developers.cloudflare.com/flagship/sdk/server-provider/)[NextGo SDK](https://developers.cloudflare.com/flagship/sdk/go/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/sdk/client-provider.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
