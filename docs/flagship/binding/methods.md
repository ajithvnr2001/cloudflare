---
url: https://developers.cloudflare.com/flagship/binding/methods/
title: Methods \u00b7 Cloudflare Flagship docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:17.484115+00:00
---

# Methods · Cloudflare Flagship docs

> Source: https://developers.cloudflare.com/flagship/binding/methods/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Flagship](https://developers.cloudflare.com/flagship/)
  3. /[Binding API](https://developers.cloudflare.com/flagship/binding/)
  4. /Methods



# Methods

Last updated Jun 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/flagship/binding/methods/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overviewget()getBooleanValue()getStringValue()getNumberValue()getObjectValue()getBooleanDetails()getStringDetails()getNumberDetails()getObjectDetails()Error handling Type mismatch Evaluation failureParameters reference

The Flagship binding provides the following methods for evaluating feature flags. All methods are asynchronous and return a `Promise`. For known evaluation failures, typed methods return the `defaultValue` you provide.

Refer to the [types reference](https://developers.cloudflare.com/flagship/binding/types/) for the definitions of `FlagshipEvaluationContext` and `FlagshipEvaluationDetails`.

## `get()`

Returns the raw flag value without type checking. Use this method when the flag type is not known at compile time.

If you provide `defaultValue`, `get()` returns that value for known evaluation failures, such as a missing flag. If you omit `defaultValue`, known evaluation failures are thrown.
    
    
    get(flagKey: string, defaultValue?: unknown, context?: FlagshipEvaluationContext): Promise<unknown>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `unknown` | No | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    const value = await env.FLAGS.get("checkout-flow", "v1", {
    	userId: "user-42",
    });

## `getBooleanValue()`

Returns the flag value as a `boolean`.
    
    
    getBooleanValue(flagKey: string, defaultValue: boolean, context?: FlagshipEvaluationContext): Promise<boolean>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `boolean` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    const enabled = await env.FLAGS.getBooleanValue("dark-mode", false, {
    	userId: "user-42",
    });

## `getStringValue()`

Returns the flag value as a `string`.
    
    
    getStringValue(flagKey: string, defaultValue: string, context?: FlagshipEvaluationContext): Promise<string>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `string` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    const variant = await env.FLAGS.getStringValue("checkout-flow", "v1", {
    	userId: "user-42",
    	country: "US",
    });

## `getNumberValue()`

Returns the flag value as a `number`.
    
    
    getNumberValue(flagKey: string, defaultValue: number, context?: FlagshipEvaluationContext): Promise<number>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `number` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    const maxRetries = await env.FLAGS.getNumberValue("max-retries", 3, {
    	plan: "enterprise",
    });

## `getObjectValue()`

Returns the flag value as a typed object. Use the generic parameter `T` to specify the expected shape.
    
    
    getObjectValue<T extends object>(flagKey: string, defaultValue: T, context?: FlagshipEvaluationContext): Promise<T>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `T` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    interface ThemeConfig {
    	primaryColor: string;
    	fontSize: number;
    }
    
    const theme = await env.FLAGS.getObjectValue<ThemeConfig>(
    	"theme-config",
    	{ primaryColor: "#000", fontSize: 14 },
    	{ userId: "user-42" },
    );

## `getBooleanDetails()`

Returns the flag value as a `boolean` with evaluation metadata.
    
    
    getBooleanDetails(flagKey: string, defaultValue: boolean, context?: FlagshipEvaluationContext): Promise<FlagshipEvaluationDetails<boolean>>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `boolean` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    const details = await env.FLAGS.getBooleanDetails("dark-mode", false, {
    	userId: "user-42",
    });
    console.log(details.value); // true
    console.log(details.reason); // "TARGETING_MATCH"

## `getStringDetails()`

Returns the flag value as a `string` with evaluation metadata.
    
    
    getStringDetails(flagKey: string, defaultValue: string, context?: FlagshipEvaluationContext): Promise<FlagshipEvaluationDetails<string>>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `string` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    const details = await env.FLAGS.getStringDetails("checkout-flow", "v1", {
    	userId: "user-42",
    });
    console.log(details.value); // "v2"
    console.log(details.variant); // "new"
    console.log(details.reason); // "TARGETING_MATCH"

## `getNumberDetails()`

Returns the flag value as a `number` with evaluation metadata.
    
    
    getNumberDetails(flagKey: string, defaultValue: number, context?: FlagshipEvaluationContext): Promise<FlagshipEvaluationDetails<number>>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `number` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    const details = await env.FLAGS.getNumberDetails("max-retries", 3, {
    	plan: "enterprise",
    });
    console.log(details.value); // 5
    console.log(details.reason); // "TARGETING_MATCH"

## `getObjectDetails()`

Returns the flag value as a typed object with evaluation metadata. Use the generic parameter `T` to specify the expected shape.
    
    
    getObjectDetails<T extends object>(flagKey: string, defaultValue: T, context?: FlagshipEvaluationContext): Promise<FlagshipEvaluationDetails<T>>

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | `T` | Yes | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules.  
      
    
    interface ThemeConfig {
    	primaryColor: string;
    	fontSize: number;
    }
    
    const details = await env.FLAGS.getObjectDetails<ThemeConfig>(
    	"theme-config",
    	{ primaryColor: "#000", fontSize: 14 },
    	{ userId: "user-42" },
    );
    console.log(details.value); // { primaryColor: "#0051FF", fontSize: 16 }
    console.log(details.variant); // "brand-refresh"

## Error handling

Typed evaluation methods return the `defaultValue` you provided for known evaluation failures, such as a missing flag or type mismatch. Unexpected runtime failures can still throw. Use the `*Details` methods to inspect known evaluation failures.

### Type mismatch

If you call a typed method on a flag with a different type (for example, `getBooleanValue` on a string flag), the method returns the default value. The `*Details` methods set `errorCode` to `"TYPE_MISMATCH"`.
    
    
    // Flag "checkout-flow" is a string flag, but you call getBooleanDetails.
    const details = await env.FLAGS.getBooleanDetails("checkout-flow", false);
    console.log(details.value); // false (the default value)
    console.log(details.errorCode); // "TYPE_MISMATCH"

### Evaluation failure

If evaluation fails for another reason, the method returns the default value. The `*Details` methods include an `errorCode` such as `"FLAG_NOT_FOUND"`, `"INVALID_CONTEXT"`, `"PARSE_ERROR"`, or `"GENERAL"`.
    
    
    const details = await env.FLAGS.getStringDetails(
    	"nonexistent-flag",
    	"fallback",
    );
    console.log(details.value); // "fallback"
    console.log(details.errorCode); // "FLAG_NOT_FOUND"

## Parameters reference

The following table summarizes the parameters shared across all evaluation methods.

Parameter | Type | Required | Description  
---|---|---|---  
`flagKey` | `string` | Yes | The key of the flag to evaluate.  
`defaultValue` | varies | Yes (except `get`) | The fallback value returned if evaluation fails or the flag is not found.  
`context` | `FlagshipEvaluationContext` | No | Key-value attributes for targeting rules (for example, `{ userId: "user-42", country: "US" }`).  
  
[PreviousTypes](https://developers.cloudflare.com/flagship/binding/types/)[NextOverview](https://developers.cloudflare.com/flagship/sdk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/flagship/binding/methods.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
