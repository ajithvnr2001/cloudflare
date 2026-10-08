---
url: https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/
title: Control which hostnames Browser Run sessions can access \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:13.612187+00:00
---

# Control which hostnames Browser Run sessions can access · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 14, 2026

## Control which hostnames Browser Run sessions can access

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-14-guardrails/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) now supports [guardrails](https://developers.cloudflare.com/browser-run/features/guardrails/), which limit a browser session's HTTP and HTTPS requests to permitted hostnames.

Use guardrails when you need to:

  * Keep a browser workflow limited to a specific website and its subdomains.
  * Load only known third-party APIs, scripts, images, and fonts.
  * Generate a screenshot or PDF from HTML you provide while preventing it from loading external content.



Set guardrails when starting a session with Puppeteer, Playwright, or the REST API. With a browser binding named `MYBROWSER`, pass `guardrails` when launching Puppeteer:
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    export async function startGuardedSession(env) {
    	return puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com", "*.example.com"],
    		},
    	});
    }
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    interface Env {
    	MYBROWSER: Fetcher;
    }
    
    export async function startGuardedSession(env: Env) {
    	return puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com", "*.example.com"],
    		},
    	});
    }

In addition to session guardrails, Browser Run now supports a read-only mode for [Live View](https://developers.cloudflare.com/browser-run/features/live-view/). Live View lets you watch and interact with an active Browser Run session in real time. A read-only link lets someone watch without clicking, typing, navigating, or running JavaScript.

To create a read-only link, set `{ mode: "readonly" }` when generating the Live View URL. This setting affects only the person using that link. The session's hostname restrictions remain unchanged.

Refer to the [guardrails documentation](https://developers.cloudflare.com/browser-run/features/guardrails/) for more information.
