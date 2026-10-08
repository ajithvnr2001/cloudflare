---
url: https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/
title: Improved React Server Components support in the Cloudflare Vite plugin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:36.544114+00:00
---

# Improved React Server Components support in the Cloudflare Vite plugin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 11, 2026

## Improved React Server Components support in the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare Vite plugin now integrates seamlessly [@vitejs/plugin-rsc ↗︎](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc), the official Vite plugin for [React Server Components ↗︎](https://react.dev/reference/rsc/server-components).

A `childEnvironments` option has been added to the plugin config to enable using multiple environments within a single Worker. The parent environment can then import modules from a child environment in order to access a separate module graph. For a typical RSC use case, the plugin might be configured as in the following example:

vite.config.tsts
    
    
    export default defineConfig({
    	plugins: [
    		cloudflare({
    			viteEnvironment: {
    				name: "rsc",
    				childEnvironments: ["ssr"],
    			},
    		}),
    	],
    });

`@vitejs/plugin-rsc` provides the lower level functionality that frameworks, such as [React Router ↗︎](https://reactrouter.com/how-to/react-server-components), build upon. The GitHub repository includes a [basic Cloudflare example ↗︎](https://github.com/vitejs/vite-plugin-react/tree/f066114c3e6bf18f5209ff3d3ef6bf1ab46d3866/packages/plugin-rsc/examples/starter-cf-single).
