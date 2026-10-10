---
url: https://developers.cloudflare.com/changelog/post/2025-03-11-process-env-support/
title: Access your Worker's environment variables from process.env \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.083998+00:00
---

# Access your Worker's environment variables from process.env · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-11-process-env-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 11, 2025

## Access your Worker's environment variables from process.env

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now access [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/) and [secrets](https://developers.cloudflare.com/workers/configuration/secrets/) on [`process.env`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/process/#processenv) when using the [`nodejs_compat` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag).
    
    
    const apiClient = ApiClient.new({ apiKey: process.env.API_KEY });
    const LOG_LEVEL = process.env.LOG_LEVEL || "info";

In Node.js, environment variables are exposed via the global `process.env` object. Some libraries assume that this object will be populated, and many developers may be used to accessing variables in this way.

Previously, the `process.env` object was always empty unless written to in Worker code. This could cause unexpected errors or friction when developing Workers using code previously written for Node.js.

Now, [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), and [version metadata](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/) can all be accessed on `process.env`.

To opt-in to the new `process.env` behaviour now, add the [`nodejs_compat_populate_process_env`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-auto-populating-processenv) compatibility flag to your `wrangler.json` configuration:
    
    
    {
    	// Rest of your configuration
    	// Add "nodejs_compat_populate_process_env" to your compatibility_flags array
    	"compatibility_flags": ["nodejs_compat", "nodejs_compat_populate_process_env"],
    	// Rest of your configuration
    
    
    compatibility_flags = [ "nodejs_compat", "nodejs_compat_populate_process_env" ]

After April 1, 2025, populating `process.env` will become the default behavior when both `nodejs_compat` is enabled and your Worker's `compatibility_date` is after "2025-04-01".
