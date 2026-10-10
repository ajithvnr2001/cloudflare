---
url: https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/
title: Work across multiple accounts with Wrangler auth profiles \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.484359+00:00
---

# Work across multiple accounts with Wrangler auth profiles · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 2, 2026

## Work across multiple accounts with Wrangler auth profiles

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) now supports auth profiles: named logins that you scope to specific Cloudflare accounts and switch between automatically, based on the directory you are working in.

A profile is a named OAuth login bound to a directory. Commands run in that directory, and its subdirectories, use the matching account — so you can move between accounts without re-running `wrangler login`.

Use profiles to keep a separate login for each client when working at an agency, or to separate staging and production into different accounts. Pair a profile with an `account_id` in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) so a command cannot reach the wrong account.
    
    
    # Create a profile for each account, choosing which accounts it can reach
    wrangler auth create client-a
    wrangler auth activate client-a ~/clients/client-a
    
    wrangler auth create client-b
    wrangler auth activate client-b ~/clients/client-b

Use the `--profile` flag to run a single command with a specific profile:
    
    
    wrangler deploy --profile personal

In CI and other automated environments, `CLOUDFLARE_API_TOKEN` still takes precedence over all profiles.

For setup, the resolution order, and the full command reference, refer to [Authentication profiles](https://developers.cloudflare.com/workers/wrangler/profiles/).
