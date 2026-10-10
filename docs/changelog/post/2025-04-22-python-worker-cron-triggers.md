---
url: https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/
title: Cron triggers are now supported in Python Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.751952+00:00
---

# Cron triggers are now supported in Python Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 24, 2025

## Cron triggers are now supported in Python Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create Python Workers which are executed via a cron trigger.

This is similar to how it's done in JavaScript Workers, simply define a scheduled event listener in your Worker:
    
    
    from workers import handler
    
    @handler
    async def on_scheduled(event, env, ctx):
      print("cron processed")

Define a cron trigger configuration in your Wrangler configuration file:
    
    
    {
    	"triggers": {
    		// Schedule cron triggers:
    		// - At every 3rd minute
    		// - At 15:00 (UTC) on first day of the month
    		// - At 23:59 (UTC) on the last weekday of the month
    		"crons": [
    			"*/3 * * * *",
    			"0 15 1 * *",
    			"59 23 LW * *"
    		]
    	}
    }
    
    
    [triggers]
    crons = [ "*/3 * * * *", "0 15 1 * *", "59 23 LW * *" ]

Then test your new handler by using Wrangler with the `--test-scheduled` flag and making a request to `/cdn-cgi/local/scheduled?cron=*+*+*+*+*`:
    
    
    npx wrangler dev --test-scheduled
    
    curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*"

Consult the [Workers Cron Triggers page](https://developers.cloudflare.com/workers/configuration/cron-triggers/) for full details on cron triggers in Workers.
