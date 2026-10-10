---
url: https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/
title: Run and connect Workers in separate dev commands with the Cloudflare Vite plugin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.274948+00:00
---

# Run and connect Workers in separate dev commands with the Cloudflare Vite plugin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 26, 2025

## Run and connect Workers in separate dev commands with the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers can now talk to each other across separate dev commands using service bindings and tail consumers, whether started with `vite dev` or `wrangler dev`.

Simply start each Worker in its own terminal:
    
    
    # Terminal 1
    vite dev
    
    # Terminal 2
    wrangler dev

This is useful when different teams maintain different Workers, or when each Worker has its own build setup or tooling.

Check out the [Developing with multiple Workers](https://developers.cloudflare.com/workers/local-development/multi-workers) guide to learn more about the different approaches and when to use each one.
