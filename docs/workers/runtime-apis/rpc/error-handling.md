---
url: https://developers.cloudflare.com/workers/runtime-apis/rpc/error-handling/
title: Workers RPC \u2014 Error Handling \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:48.013024+00:00
---

# Workers RPC — Error Handling · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/rpc/error-handling/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Remote-procedure call (RPC)](https://developers.cloudflare.com/workers/runtime-apis/rpc/)
  5. /Error handling



# Error handling

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/rpc/error-handling/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExceptionsAdditional properties

## Exceptions

An error thrown by an RPC method, or used to reject the method's returned Promise, propagates to the caller as a new error object. With enhanced error serialization, Workers preserves the effective `name` and `message` and serializable own properties, including non-enumerable properties such as [`cause` ↗︎](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause).

[Enhanced error serialization](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enhanced-error-serialization) uses the `enhanced_error_serialization` compatibility flag. It is on by default for compatibility dates on or after `2026-04-21`. For earlier compatibility dates, add the flag to both the RPC provider and consumer. A Worker can opt out with `legacy_error_serialization`. Without enhanced error serialization, RPC uses legacy error reconstruction and does not preserve custom own properties.

The provider must be able to serialize the error and its own property values. Keep public error properties small and serializable. If an own property contains a non-serializable value, Workers does not guarantee that the enhanced error details will reach the consumer.

On the consumer, treat the error's serializable fields as the RPC contract. Workers does not preserve or guarantee:

  * The source object's identity, custom prototype, or constructor.
  * The results of `instanceof` checks, especially for custom error classes.
  * Prototype methods or property descriptors.
  * The provider's original stack trace. The consumer may see a new stack from error reconstruction instead.
  * Non-serializable property values.



For example, an instance of `ProviderError extends Error` can arrive with `name` set to `"ProviderError"` and with serializable own fields such as `code`, but it is not an instance of a consumer-side `ProviderError` class. Check documented fields such as `name` and `code` instead of relying on class identity.

## Additional properties

For some remote exceptions, the runtime may add properties to the propagated exception, such as retry or Durable Object metadata. These properties are separate from the provider's custom properties. Refer to [Durable Object error handling](https://developers.cloudflare.com/durable-objects/best-practices/error-handling) for more details.

[PreviousTypeScript](https://developers.cloudflare.com/workers/runtime-apis/rpc/typescript/)[NextOverview](https://developers.cloudflare.com/workers/runtime-apis/webassembly/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/rpc/error-handling.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
