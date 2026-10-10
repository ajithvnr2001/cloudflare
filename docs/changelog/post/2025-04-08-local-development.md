---
url: https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/
title: Local development support for Email Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.173357+00:00
---

# Local development support for Email Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 8, 2025

## Local development support for Email Workers

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Email Workers enables developers to programmatically take action on anything that hits their email inbox. If you're building with Email Workers, you can now test the behavior of an Email Worker script, receiving, replying and sending emails in your local environment using `wrangler dev`.

Below is an example that shows you how you can receive messages using the `email()` handler and parse them using [postal-mime ↗︎](https://www.npmjs.com/package/postal-mime):
    
    
    import * as PostalMime from "postal-mime";
    
    export default {
    	async email(message, env, ctx) {
    		const parser = new PostalMime.default();
    		const rawEmail = new Response(message.raw);
    		const email = await parser.parse(await rawEmail.arrayBuffer());
    		console.log(email);
    	},
    };

Now when you run `npx wrangler dev`, wrangler will expose a local `/cdn-cgi/local/email` endpoint that you can `POST` email messages to and trigger your Worker's `email()` handler:
    
    
    curl -X POST 'http://localhost:8787/cdn-cgi/local/email' \
      --url-query 'from=sender@example.com' \
      --url-query 'to=recipient@example.com' \
      --header 'Content-Type: application/json' \
      --data-raw 'Received: from smtp.example.com (127.0.0.1)
            by cloudflare-email.com (unknown) id 4fwwffRXOpyR
            for <recipient@example.com>; Tue, 27 Aug 2024 15:50:20 +0000
    From: "John" <sender@example.com>
    Reply-To: sender@example.com
    To: recipient@example.com
    Subject: Testing Email Workers Local Dev
    Content-Type: text/html; charset="windows-1252"
    X-Mailer: Curl
    Date: Tue, 27 Aug 2024 08:49:44 -0700
    Message-ID: <6114391943504294873000@ZSH-GHOSTTY>
    
    Hi there'

This is what you get in the console:
    
    
    {
    	"headers": [
    		{
    			"key": "received",
    			"value": "from smtp.example.com (127.0.0.1) by cloudflare-email.com (unknown) id 4fwwffRXOpyR for <recipient@example.com>; Tue, 27 Aug 2024 15:50:20 +0000"
    		},
    		{ "key": "from", "value": "\"John\" <sender@example.com>" },
    		{ "key": "reply-to", "value": "sender@example.com" },
    		{ "key": "to", "value": "recipient@example.com" },
    		{ "key": "subject", "value": "Testing Email Workers Local Dev" },
    		{ "key": "content-type", "value": "text/html; charset=\"windows-1252\"" },
    		{ "key": "x-mailer", "value": "Curl" },
    		{ "key": "date", "value": "Tue, 27 Aug 2024 08:49:44 -0700" },
    		{
    			"key": "message-id",
    			"value": "<6114391943504294873000@ZSH-GHOSTTY>"
    		}
    	],
    	"from": { "address": "sender@example.com", "name": "John" },
    	"to": [{ "address": "recipient@example.com", "name": "" }],
    	"replyTo": [{ "address": "sender@example.com", "name": "" }],
    	"subject": "Testing Email Workers Local Dev",
    	"messageId": "<6114391943504294873000@ZSH-GHOSTTY>",
    	"date": "2024-08-27T15:49:44.000Z",
    	"html": "Hi there\n",
    	"attachments": []
    }

Local development is a critical part of the development flow, and also works for sending, replying and forwarding emails. See [our documentation](https://developers.cloudflare.com/email-service/local-development/routing/) for more information.
