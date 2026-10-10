---
url: https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/
title: Preserve exception details in console logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.377288+00:00
---

# Preserve exception details in console logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-24-preserve-exception-info/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 24, 2026

## Preserve exception details in console logs

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Console methods now preserve exception details in your Worker's logs. When your Worker logs an exception, the corresponding log entry includes the exception name, message, and stack.

For example, your Worker can catch and log an exception:
    
    
    try {
    	throw new Error("Deliberately created exception");
    } catch (error) {
    	console.error("caught exception:", error);
    }
    
    
    try {
    	throw new Error("Deliberately created exception");
    } catch (error) {
    	console.error("caught exception:", error);
    }

If you use [Workers Observability](https://developers.cloudflare.com/workers/observability/), your log is automatically enriched with structured error information. The following example shows how the enriched log appears in the Cloudflare dashboard:

![Workers Observability log entry showing a caught exception and its stack trace](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1200,height=212,format=webp/_astro/2026-08-24-error-info.Be4rAN4i.png)

The exception's stack trace appears directly in the log message.

If you send telemetry to a [Tail Worker](https://developers.cloudflare.com/workers/observability/logs/tail-workers/), the Tail Worker now receives a log entry with an `errorInfo` array:
    
    
    {
    	"message": ["Request failed:", "RangeError: Value out of range"],
    	"errorInfo": [
    		null,
    		{
    			"name": "RangeError",
    			"message": "Value out of range",
    			"stack": "RangeError: Value out of range\n    at ..."
    		}
    	],
    	"level": "error",
    	"timestamp": 1784851200000
    }

Each `errorInfo` item corresponds to the console argument at the same index in `message`. Arguments that are not exceptions have a `null` entry.
