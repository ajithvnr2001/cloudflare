---
url: https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/
title: New Placement Hints for Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:34.472908+00:00
---

# New Placement Hints for Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 22, 2026

## New Placement Hints for Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure Workers to run close to infrastructure in legacy cloud regions to minimize latency to existing services and databases. This is most useful when your Worker makes multiple round trips.

To [set a placement hint](https://developers.cloudflare.com/workers/configuration/placement/#configure-explicit-placement-hints), set the `placement.region` property in your Wrangler configuration file:
    
    
    {
    	"placement": {
    		"region": "aws:us-east-1",
    	},
    }
    
    
    [placement]
    region = "aws:us-east-1"

Placement hints support Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure region identifiers. Workers run in the [Cloudflare data center ↗︎](https://www.cloudflare.com/network/) with the lowest latency to the specified cloud region.

If your existing infrastructure is not in these cloud providers, expose it to placement probes with `placement.host` for layer 4 checks or `placement.hostname` for layer 7 checks. These probes are designed to locate single-homed infrastructure and are not suitable for anycasted or multicasted resources.
    
    
    {
    	"placement": {
    		"host": "my_database_host.com:5432",
    	},
    }
    
    
    [placement]
    host = "my_database_host.com:5432"
    
    
    {
    	"placement": {
    		"hostname": "my_api_server.com",
    	},
    }
    
    
    [placement]
    hostname = "my_api_server.com"

This is an extension of [Smart Placement](https://developers.cloudflare.com/workers/configuration/placement/#enable-smart-placement), which automatically places your Workers closer to back-end APIs based on measured latency. When you do not know the location of your back-end APIs or have multiple back-end APIs, set `mode: "smart"`:
    
    
    {
    	"placement": {
    		"mode": "smart",
    	},
    }
    
    
    [placement]
    mode = "smart"
