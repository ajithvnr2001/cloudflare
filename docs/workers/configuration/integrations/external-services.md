---
url: https://developers.cloudflare.com/workers/configuration/integrations/external-services/
title: External Services \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:15.008691+00:00
---

# External Services · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/configuration/integrations/external-services/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Configuration](https://developers.cloudflare.com/workers/configuration/)

  4. /[Integrations](https://developers.cloudflare.com/workers/configuration/integrations/)
  5. /External Services



# External Services

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/configuration/integrations/external-services/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthentication

Many external services provide libraries and SDKs to interact with their APIs. While many Node-compatible libraries work on Workers right out of the box, some, which implement `fs`, `http/net`, or access the browser `window` do not directly translate to the Workers runtime, which is v8-based.

## Authentication

If your service requires authentication, use Wrangler secrets to securely store your credentials. To do this, create a secret in your Cloudflare Workers project using the following [`wrangler secret`](https://developers.cloudflare.com/workers/wrangler/commands/general/#secret) command:
    
    
    wrangler secret put SECRET_NAME

Then, retrieve the secret value in your code using the following code snippet:
    
    
    const secretValue = env.SECRET_NAME;

Then use the secret value to authenticate with the external service. For example, if the external service requires an API key for authentication, include the secret in your library's configuration.

For services that require mTLS authentication, use [mTLS certificates](https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls) to present a client certificate.

Use [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) when communicating with external APIs, which treat your Worker as your core application.

[PreviousAPIs](https://developers.cloudflare.com/workers/configuration/integrations/apis/)[NextMultipart upload metadata](https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/configuration/integrations/external-services.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
