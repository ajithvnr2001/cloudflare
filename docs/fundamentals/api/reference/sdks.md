---
url: https://developers.cloudflare.com/fundamentals/api/reference/sdks/
title: SDKs \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:21.762590+00:00
---

# SDKs · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/reference/sdks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /Reference
  5. /SDKs



# SDKs

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/api/reference/sdks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use cURL vs SDKExample With cURL: With the TypeScript SDK:

Cloudflare offers language software development kits (SDKs) as well as `curl` examples to demonstrate how to use the Cloudflare API. The SDK libraries allow you to interact with the Cloudflare API in language-specific syntax and more easily integrate with your existing applications.

Cloudflare currently offers the following SDKs:

  * [Go ↗︎](https://github.com/cloudflare/cloudflare-go)
  * [TypeScript ↗︎](https://github.com/cloudflare/cloudflare-typescript)
  * [Python ↗︎](https://github.com/cloudflare/cloudflare-python)



## When to use cURL vs SDK

There is no definite answer on which you should use. Instead, consider your use case and determine whether cURL or an SDK is the best fit.

Use case | cURL | SDK  
---|---|---  
Quick testing within the CLI | ✅ | ❌  
Use within bash scripts or CI | ✅ | ❌*  
Usage from within an existing application or framework | ❌ | ✅  
More complex usage where you need to chain together outputs | ❌ | ✅  
  
* It is possible, although not straight forward, to use the SDKs within bash scripts or CI environments with additional runtime dependencies and setup.

## Example

The following are examples of how you would query all of the Cloudflare zones you have access to.

### With cURL:
    
    
    curl "https://api.cloudflare.com/client/v4/zones" \
    --header "Authorization: Bearer <API_TOKEN>"

### With the TypeScript SDK:
    
    
    const client = new Cloudflare({
    	apiToken: process.env["CLOUDFLARE_API_TOKEN"],
    });
    
    const zones = await client.zones.list();
    
    console.log(zones);

[PreviousRate limits](https://developers.cloudflare.com/fundamentals/api/reference/limits/)[NextTroubleshooting](https://developers.cloudflare.com/fundamentals/api/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/reference/sdks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
