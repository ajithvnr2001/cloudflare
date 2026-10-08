---
url: https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls/
title: mTLS \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:41.611061+00:00
---

# mTLS · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Bindings (env)](https://developers.cloudflare.com/workers/runtime-apis/bindings/)
  5. /mTLS



# mTLS

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Interface

When using [HTTPS ↗︎](https://www.cloudflare.com/learning/ssl/what-is-https/), a server presents a certificate for the client to authenticate in order to prove their identity. For even tighter security, some services require that the client also present a certificate.

This process - known as [mTLS ↗︎](https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/) \- moves authentication to the protocol of TLS, rather than managing it in application code. Connections from unauthorized clients are rejected during the TLS handshake instead.

To present a client certificate when communicating with a service, create a mTLS certificate [binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/) in your Worker project's Wrangler file. This will allow your Worker to present a client certificate to a service on your behalf.

Caution

Currently, mTLS for Workers cannot be used for requests made to a service that is a [proxied zone](https://developers.cloudflare.com/dns/proxy-status/) on Cloudflare. If your Worker presents a client certificate to a service proxied by Cloudflare, Cloudflare will return a `520` error.

First, upload a certificate and its private key to your account using the [`wrangler mtls-certificate`](https://developers.cloudflare.com/workers/wrangler/commands/certificates/#mtls-certificate) command:

Caution

The `wrangler mtls-certificate upload` command requires the [SSL and Certificates Edit API token scope](https://developers.cloudflare.com/fundamentals/api/reference/permissions/). If you are using the OAuth flow triggered by `wrangler login`, the correct scope is set automatically. If you are using API tokens, refer to [Create an API token ↗︎](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) to set the right scope for your API token.
    
    
    npx wrangler mtls-certificate upload --cert cert.pem --key key.pem --name my-client-cert

Then, update your Worker project's Wrangler file to create an mTLS certificate binding:
    
    
    {
    	"mtls_certificates": [
    		{
    			"binding": "MY_CERT",
    			"certificate_id": "<CERTIFICATE_ID>"
    		}
    	]
    }
    
    
    [[mtls_certificates]]
    binding = "MY_CERT"
    certificate_id = "<CERTIFICATE_ID>"

Note

Certificate IDs are displayed after uploading, and can also be viewed with the command `wrangler mtls-certificate list`.

Adding an mTLS certificate binding includes a variable in the Worker's environment on which the `fetch()` method is available. This `fetch()` method uses the standard [Fetch](https://developers.cloudflare.com/workers/runtime-apis/fetch/) API and has the exact same signature as the global `fetch`, but always presents the client certificate when establishing the TLS connection.

Note

mTLS certificate bindings present an API similar to [service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings).

### Interface
    
    
    export default {
    	async fetch(request, environment) {
    		return await environment.MY_CERT.fetch("https://a-secured-origin.com");
    	},
    };
    
    
    interface Env {
      MY_CERT: Fetcher;
    }
    
    export default {
        async fetch(request, environment): Promise<Response> {
            return await environment.MY_CERT.fetch("https://a-secured-origin.com")
        }
    } satisfies ExportedHandler<Env>;

[PreviousMedia Transformations ↗︎](https://developers.cloudflare.com/stream/transform-videos/bindings/)[NextQueues ↗︎](https://developers.cloudflare.com/queues/configuration/javascript-apis/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/bindings/mTLS.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
