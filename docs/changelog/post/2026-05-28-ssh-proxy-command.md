---
url: https://developers.cloudflare.com/changelog/post/2026-05-28-ssh-proxy-command/
title: Wrangler supports SSH ProxyCommand for Containers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.604522+00:00
---

# Wrangler supports SSH ProxyCommand for Containers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-28-ssh-proxy-command/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## Wrangler supports SSH ProxyCommand for Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Wrangler](https://developers.cloudflare.com/workers/wrangler/) supports using `wrangler containers ssh` as an OpenSSH `ProxyCommand` for [Containers](https://developers.cloudflare.com/containers/). This lets your local SSH client connect to a running Container through Wrangler.
    
    
    ssh -o ProxyCommand="wrangler containers ssh %h" cloudchamber@<INSTANCE_ID>

When standard input and output are piped, Wrangler forwards data to the SSH server in the Container. You can also pass `--stdio` to force this mode.

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).
