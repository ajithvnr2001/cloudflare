---
url: https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/
title: Send emails with named recipient addresses \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:54.916887+00:00
---

# Send emails with named recipient addresses · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 28, 2026

## Send emails with named recipient addresses

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now send emails with display names on recipient addresses in addition to the existing `from` support. Pass an object with `email` and an optional `name` field for `to`, `cc`, `bcc`, `replyTo`, or `from`:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const response = await env.EMAIL.send({
    			from: { email: "support@example.com", name: "Support Team" },
    			to: { email: "jane@example.com", name: "Jane Doe" },
    			cc: [
    				"manager@company.com",
    				{ email: "team@company.com", name: "Engineering Team" },
    			],
    			subject: "Welcome!",
    			html: "<h1>Thanks for joining!</h1>",
    			text: "Thanks for joining!",
    		});
    
    		return Response.json({ messageId: response.messageId });
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const response = await env.EMAIL.send({
    			from: { email: "support@example.com", name: "Support Team" },
    			to: { email: "jane@example.com", name: "Jane Doe" },
    			cc: [
    				"manager@company.com",
    				{ email: "team@company.com", name: "Engineering Team" },
    			],
    			subject: "Welcome!",
    			html: "<h1>Thanks for joining!</h1>",
    			text: "Thanks for joining!",
    		});
    
    		return Response.json({ messageId: response.messageId });
    	},
    } satisfies ExportedHandler<Env>;

Plain strings remain fully supported for backward compatibility, and you can mix strings and named objects in the same array.

Refer to the [Workers API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) and [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) documentation for full request examples.
