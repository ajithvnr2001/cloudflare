---
url: https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/
title: Share a local dev server \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:33.865140+00:00
---

# Share a local dev server · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Local development](https://developers.cloudflare.com/workers/local-development/)
  4. /Share a local dev server



# Share a local dev server

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/local-development/local-dev-tunnels/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStart a tunnelSecurity considerationsRelated docs

You can expose your local dev server over a [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) when you need to share a preview, test a webhook, or access your app from another device.

This page covers tunnel support in [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev) and the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/).

## Start a tunnel

You can start a tunnel with Wrangler or the Cloudflare Vite plugin for the current session. This gives you either a random `*.trycloudflare.com` hostname via a [Quick Tunnel](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/), or a stable hostname via a [named tunnel](https://developers.cloudflare.com/tunnel/get-started/#create-a-tunnel).

**Wrangler**

Run `wrangler dev`, then press `[t]` to start or close the tunnel. Wrangler will print the public tunnel URL or URLs for the current session.

To use a named tunnel, run:

npmyarnpnpm
    
    
    npx wrangler dev --tunnel-name=my-tunnel
    
    
    yarn wrangler dev --tunnel-name=my-tunnel
    
    
    pnpm wrangler dev --tunnel-name=my-tunnel

Use `--tunnel` if you want the tunnel to open automatically when Wrangler starts.

npmyarnpnpm
    
    
    npx wrangler dev --tunnel
    
    
    yarn wrangler dev --tunnel
    
    
    pnpm wrangler dev --tunnel

**Cloudflare Vite plugin**

Run `vite dev`, then press `t + Enter` to start or close the tunnel. Add `tunnel` to the plugin config if you want to configure a named tunnel or have the tunnel open automatically when Vite starts.

To use a named tunnel with stable hostnames:

vite.config.jsjs
    
    
    import { defineConfig } from "vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    
    export default defineConfig({
    	plugins: [
    		cloudflare({
    			tunnel: { name: "my-tunnel" },
    		}),
    	],
    });

vite.config.tsts
    
    
    import { defineConfig } from "vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    
    export default defineConfig({
    	plugins: [
    		cloudflare({
    			tunnel: { name: "my-tunnel" },
    		}),
    	],
    });

If you want the tunnel to open automatically when Vite starts, set `tunnel.autoStart` to `true`.

When using `vite preview`, Vite's preview host validation still applies:

  * For Quick tunnel, add `.trycloudflare.com` to `preview.allowedHosts`.
  * For named tunnel, add the resolved hostnames or a matching domain suffix such as `.my-domain.com` to `preview.allowedHosts`.



For example:

vite.config.jsjs
    
    
    import { defineConfig } from "vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    
    export default defineConfig({
    	preview: {
    		allowedHosts: [
    			// For Quick tunnels:
    			".trycloudflare.com",
    			// For named tunnels:
    			".my-domain.com",
    		],
    	},
    	plugins: [
    		cloudflare({
    			tunnel: { name: "my-tunnel" },
    		}),
    	],
    });

vite.config.tsts
    
    
    import { defineConfig } from "vite";
    import { cloudflare } from "@cloudflare/vite-plugin";
    
    export default defineConfig({
    	preview: {
    		allowedHosts: [
    			// For Quick tunnels:
    			".trycloudflare.com",
    			// For named tunnels:
    			".my-domain.com"
    		],
    	},
    	plugins: [
    		cloudflare({
    			tunnel: { name: "my-tunnel" },
    		}),
    	],
    });

## Security considerations

Anyone with the tunnel URL can reach your dev server, so review what your app exposes before enabling a tunnel.

  * Pay special attention to ungated preview or admin endpoints.
  * Review any [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) connected to real resources.
  * Review any code that proxies requests to private or internal services.
  * If you are using the Cloudflare Vite plugin with `vite dev`, HMR and module serving may expose source files, file paths, or project structure over the tunnel. If you only need to share a built preview, prefer `vite preview` for public sharing.
  * Local dev-related routes, such as `/cdn-cgi/*`, remain restricted and are not exposed over the tunnel.
  * If you need a stable hostname or stricter access control, use a named tunnel protected by Cloudflare Access.



## Related docs

  * [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)



[PreviousLocal Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/)[NextPlayground](https://developers.cloudflare.com/workers/playground/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/local-development/local-dev-tunnels.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
