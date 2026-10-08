---
url: https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/
title: SSH into running Container instances \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:40.543173+00:00
---

# SSH into running Container instances · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 12, 2026

## SSH into running Container instances

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-12-ssh-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now SSH into running Container instances using Wrangler. This is useful for debugging, inspecting running processes, or executing one-off commands inside a Container.

To connect, enable `wrangler_ssh` in your Container configuration and add your `ssh-ed25519` public key to `authorized_keys`:
    
    
    {
    	"containers": [
    		{
    			"wrangler_ssh": {
    				"enabled": true
    			},
    			"authorized_keys": [
    				{
    					"name": "<NAME>",
    					"public_key": "<YOUR_PUBLIC_KEY_HERE>"
    				}
    			]
    		}
    	]
    }
    
    
    [[containers]]
    [containers.wrangler_ssh]
    enabled = true
    
    [[containers.authorized_keys]]
    name = "<NAME>"
    public_key = "<YOUR_PUBLIC_KEY_HERE>"

Then connect with:
    
    
    wrangler containers ssh <INSTANCE_ID>

You can also run a single command without opening an interactive shell:
    
    
    wrangler containers ssh <INSTANCE_ID> -- ls -al

Use `wrangler containers instances <APPLICATION>` to find the instance ID for a running Container.

For more information, refer to the [SSH documentation](https://developers.cloudflare.com/containers/guides/ssh/).
