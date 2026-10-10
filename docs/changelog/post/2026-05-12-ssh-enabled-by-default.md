---
url: https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/
title: SSH through Wrangler is now enabled by default for Containers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.337725+00:00
---

# SSH through Wrangler is now enabled by default for Containers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-12-ssh-enabled-by-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 12, 2026

## SSH through Wrangler is now enabled by default for Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

SSH through Wrangler is now enabled by default for [Containers](https://developers.cloudflare.com/containers/). Previously, you had to set `ssh.enabled` to `true` in your Container configuration before you could connect.

This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through [`wrangler containers ssh`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-ssh), which authenticates against your Cloudflare account. You also need to add an `ssh-ed25519` public key to `authorized_keys` before anyone can connect, so enabling SSH alone does not grant access.

To connect, add a public key to your Container configuration and run `wrangler containers ssh <INSTANCE_ID>`:
    
    
    {
    	"containers": [
    		{
    			"authorized_keys": [
    				{
    					"name": "<NAME>",
    					"public_key": "<YOUR_PUBLIC_KEY_HERE>",
    				},
    			],
    		},
    	],
    }
    
    
    [[containers]]
    [[containers.authorized_keys]]
    name = "<NAME>"
    public_key = "<YOUR_PUBLIC_KEY_HERE>"

To disable SSH, set `ssh.enabled` to `false` in your Container configuration:
    
    
    {
    	"containers": [
    		{
    			"ssh": {
    				"enabled": false,
    			},
    		},
    	],
    }
    
    
    [[containers]]
    [containers.ssh]
    enabled = false

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).
