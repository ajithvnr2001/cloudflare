---
url: https://developers.cloudflare.com/sandbox/previews/serve-previews-on-their-own-hostnames/
title: Serve previews on their own hostnames \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:20.379094+00:00
---

# Serve previews on their own hostnames · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/previews/serve-previews-on-their-own-hostnames/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Preview applications](https://developers.cloudflare.com/sandbox/previews/)
  4. /Preview on separate hostnames



# Serve previews on their own hostnames

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/previews/serve-previews-on-their-own-hostnames/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesRoute preview hostnames to your WorkerServe previews under a subdomainSet cookies on preview hostnamesRelated resources

Serve each sandbox preview from its own hostname, such as `ada.example-previews.com`. Code in a preview runs in the visitor's browser, and each preview hostname is a separate origin. Code in one preview cannot read your application pages or the storage of another preview. Paths reach the server unchanged, so applications do not need a base path.

.example-previews.comhttps://ada.example-previews.com/app/
    A wildcard DNS record and the route `*.example-previews.com/*` send every preview hostname to your Worker.

adahttps://ada.example-previews.com/app/
    Your Worker reads the sandbox name and calls `getByName("ada")`. A name that is not a valid DNS label gets a `404`.

/app/https://ada.example-previews.com/app/
    The path reaches the web server in the container unchanged, with the preview hostname in the `Host` header.

## Prerequisites

  * A Durable Object whose `fetch()` handler forwards requests to a web server in its container. To build one, refer to [Preview a web application](https://developers.cloudflare.com/sandbox/previews/).
  * A domain for previews on Cloudflare, such as `example-previews.com`, with Cloudflare managing its DNS. Use a domain that your application does not use.



## Route preview hostnames to your Worker

  1. In the DNS settings of the preview domain, add a proxied [wildcard record](https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/). For example, add an `AAAA` record with the name `*` and the content `100::`, with the proxy status **Proxied**.

The record lets Cloudflare receive requests for every preview hostname. The Worker route handles those requests, so Cloudflare never contacts the address in the record.

  2. In `wrangler.jsonc`, add the preview domain as a variable and route its subdomains to your Worker. Replace `example-previews.com` with your preview domain:
         
         {
         	"vars": {
         		"PREVIEW_DOMAIN": "example-previews.com",
         	},
         	"routes": [
         		{
         			"pattern": "*.example-previews.com/*",
         			"zone_name": "example-previews.com",
         		},
         	],
         	"workers_dev": true,
         }
         
         workers_dev = true
         
         [vars]
         PREVIEW_DOMAIN = "example-previews.com"
         
         [[routes]]
         pattern = "*.example-previews.com/*"
         zone_name = "example-previews.com"

Wrangler turns off the `workers.dev` URL when `routes` is set. `workers_dev: true` keeps it for requests that manage previews.

  3. Generate types for the new variable:

npmyarnpnpm
         
         npx wrangler types
         
         yarn wrangler types
         
         pnpm wrangler types

  4. In the `fetch()` handler of your Worker, send each preview hostname to the Durable Object with the same name:

src/index.jsjs
         
         export default {
         	async fetch(request, env) {
         		const url = new URL(request.url);
         		const suffix = `.${env.PREVIEW_DOMAIN}`;
         
         		// A preview hostname reaches only the sandbox with the same name.
         		if (url.hostname.endsWith(suffix)) {
         			const name = url.hostname.slice(0, -suffix.length);
         
         			// Accept only sandbox names that are valid DNS labels
         			if (!/^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/.test(name)) {
         				return new Response("Not found", { status: 404 });
         			}
         
         			// Forward with the `http:` scheme, because `getTcpPort().fetch()`
         			// does not accept `https:` URLs
         			url.protocol = "http:";
         			return env.MY_CONTAINER.getByName(name).fetch(new Request(url, request));
         		}
         
         		// Other hostnames manage previews.
         		return new Response("Not found", { status: 404 });
         	},
         };

src/index.tsts
         
         export default {
         	async fetch(request: Request, env: Env): Promise<Response> {
         		const url = new URL(request.url);
         		const suffix = `.${env.PREVIEW_DOMAIN}`;
         
         		// A preview hostname reaches only the sandbox with the same name.
         		if (url.hostname.endsWith(suffix)) {
         			const name = url.hostname.slice(0, -suffix.length);
         
         			// Accept only sandbox names that are valid DNS labels
         			if (!/^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/.test(name)) {
         				return new Response("Not found", { status: 404 });
         			}
         
         			// Forward with the `http:` scheme, because `getTcpPort().fetch()`
         			// does not accept `https:` URLs
         			url.protocol = "http:";
         			return env.MY_CONTAINER.getByName(name).fetch(new Request(url, request));
         		}
         
         		// Other hostnames manage previews.
         		return new Response("Not found", { status: 404 });
         	},
         } satisfies ExportedHandler<Env>;

The server receives the full path and the preview hostname in the `Host` header.

Every request to a preview hostname goes to the preview. Keep routes that manage previews, such as stopping one, on other hostnames, so code in a preview cannot call them from its own origin. Authenticate preview visitors on the preview hostname, and do not send your application session cookie there.

  5. Deploy your Worker:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  6. Open the preview named `ada` in your browser, and store a value in its browser console. Replace `example-previews.com` with your preview domain:
         
         https://ada.example-previews.com/
         
         localStorage.setItem("name", "ada");

  7. Open the preview named `grace`, and read the value in its browser console:
         
         https://grace.example-previews.com/
         
         localStorage.getItem("name");

The console prints `null`. Each preview hostname is a separate origin, so `grace` cannot read the storage of `ada`.




## Serve previews under a subdomain

[Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/) covers a domain and its first-level subdomains, such as `ada.example-previews.com`. It does not cover deeper hostnames such as `ada.previews.example.com`. To serve previews under a subdomain, add [Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/) or an [advanced certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) for it.

Previews under a domain that your application also uses share cookies with your application. Browsers send a cookie set with `Domain=example.com` to every subdomain, including every preview under `previews.example.com`.

## Set cookies on preview hostnames

Code in one preview can set a cookie with `Domain=example-previews.com`, and every other preview then receives that cookie. Set cookies on preview hostnames without a `Domain` attribute, and do not trust a cookie because it arrived on a preview hostname.

## Related resources

  * [Preview a web application](https://developers.cloudflare.com/sandbox/previews/)
  * [Preview workspace example ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/main/examples/preview-workspace): a deployable Worker that runs a Vite development server on a separate hostname for each sandbox.
  * [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/#output-carries-the-same-risk)
  * [Routes](https://developers.cloudflare.com/workers/configuration/routing/routes/)



[PreviousPreview a web application](https://developers.cloudflare.com/sandbox/previews/)[NextOverview](https://developers.cloudflare.com/sandbox/network/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/previews/serve-previews-on-their-own-hostnames.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
