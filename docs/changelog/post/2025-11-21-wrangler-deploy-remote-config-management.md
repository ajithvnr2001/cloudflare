---
url: https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/
title: Better local deployment flow for Cloudflare Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:30.245074+00:00
---

# Better local deployment flow for Cloudflare Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 21, 2025

## Better local deployment flow for Cloudflare Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Until now, if a Worker had been previously deployed via the [Cloudflare Dashboard ↗︎](https://dash.cloudflare.com), a subsequent deployment done via the Cloudflare Workers CLI, [**Wrangler**](https://developers.cloudflare.com/workers/wrangler/) (through the [`deploy` command](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy)), would allow the user to override the Worker's dashboard settings without providing details on what dashboard settings would be lost.

Now instead, `wrangler deploy` presents a helpful representation of the differences between the [local configuration](https://developers.cloudflare.com/workers/wrangler/configuration/) and the remote dashboard settings, and offers to update your local configuration file for you.

See example below showing a before and after for `wrangler deploy` when a local configuration is expected to override a Worker's dashboard settings:

### Before

![wrangler deploy run before the improved workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=785,height=257,format=webp/_astro/before.Bz-MOePT.png)

### After

![wrangler deploy run after the improved workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=788,height=492,format=webp/_astro/after.BrkkBaRL.png)

Also, if instead Wrangler detects that a deployment would override remote dashboard settings but in an additive way, without modifying or removing any of them, it will simply proceed with the deployment without requesting any user interaction.

Update to [Wrangler](https://developers.cloudflare.com/workers/wrangler/) v4.50.0 or greater to take advantage of this improved deploy flow.
