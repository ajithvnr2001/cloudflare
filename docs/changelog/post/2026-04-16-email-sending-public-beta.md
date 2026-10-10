---
url: https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/
title: Email Sending now in public beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.250569+00:00
---

# Email Sending now in public beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 16, 2026

## Email Sending now in public beta

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

**[Email Sending](https://developers.cloudflare.com/email-service/api/send-emails/)** is now in public beta. Send transactional emails directly from Workers (`env.EMAIL.send()`) or the REST API, with support for HTML, plain text, attachments, inline images, and custom headers. Email Sending joins [Email Routing ↗︎](https://blog.cloudflare.com/introducing-email-routing/) under the new **Cloudflare Email Service** — a single service for sending and receiving email on the Cloudflare developer platform.

Send an email from a Worker in a few lines of code:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const response = await env.EMAIL.send({
    			from: "notifications@yourdomain.com",
    			to: "user@example.com",
    			subject: "Order confirmed",
    			html: "<h1>Your order has been confirmed</h1>",
    			text: "Your order has been confirmed.",
    		});
    
    		return Response.json({ messageId: response.messageId });
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const response = await env.EMAIL.send({
    			from: "notifications@yourdomain.com",
    			to: "user@example.com",
    			subject: "Order confirmed",
    			html: "<h1>Your order has been confirmed</h1>",
    			text: "Your order has been confirmed.",
    		});
    
    		return Response.json({ messageId: response.messageId });
    	},
    } satisfies ExportedHandler<Env>;

Email Service also integrates with the [Agents SDK](https://developers.cloudflare.com/agents/), giving your agents a native `onEmail` hook to receive, process, and reply to emails. Combined with the new [Email MCP server ↗︎](https://github.com/cloudflare/mcp-server-cloudflare) and Wrangler CLI email commands, any agent can send email regardless of where it runs.

Start sending and receiving emails from Workers and agents today. Email Sending is available on the Workers paid plan. Refer to the [Email Service documentation](https://developers.cloudflare.com/email-service/) to get started.
