---
url: https://developers.cloudflare.com/email-service/local-development/routing/
title: Email routing \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:14.837578+00:00
---

# Email routing · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/local-development/routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Local development
  4. /Email routing



# Email routing

Test email routing Workers locally using wrangler dev with simulated incoming emails

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/local-development/routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesConfigurationBasic routing workerTestingNext steps

Test email routing behavior locally using `wrangler dev` to simulate incoming emails and verify your routing logic before deploying.

## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

## Configuration

Configure your Wrangler file:
    
    
    {
    	"name": "email-routing-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    }
    
    
    name = "email-routing-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"

## Basic routing worker
    
    
    import * as PostalMime from "postal-mime";
    
    export default {
    	async email(message, env, ctx) {
    		// Parse the raw email message
    		const parser = new PostalMime.default();
    		const rawEmail = new Response(message.raw);
    		const email = await parser.parse(await rawEmail.arrayBuffer());
    
    		console.log("Received email:", {
    			from: message.from,
    			to: message.to,
    			subject: email.subject,
    			text: email.text,
    			html: email.html,
    		});
    
    		// Route based on recipient
    		if (message.to.includes("support@")) {
    			await message.forward("support-team@example.com");
    		} else {
    			await message.forward("general@example.com");
    		}
    	},
    };

## Testing

Start your development server:
    
    
    npx wrangler dev

Send a test email using the local endpoint. The request body must be a raw email message in [RFC 5322 ↗︎](https://datatracker.ietf.org/doc/html/rfc5322) format, and the message must include a `Message-ID` header:
    
    
    curl --request POST 'http://localhost:8787/cdn-cgi/local/email' \
      --url-query 'from=sender@example.com' \
      --url-query 'to=recipient@example.com' \
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

This will output the parsed email structure in the console:
    
    
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

## Next steps

  * Deploy your routing worker: [Route emails get started](https://developers.cloudflare.com/email-service/get-started/route-emails/)
  * See advanced patterns: [Email routing examples](https://developers.cloudflare.com/email-service/examples/email-routing/)



[PreviousEmail sending](https://developers.cloudflare.com/email-service/local-development/sending/)[NextMetrics and analytics](https://developers.cloudflare.com/email-service/observability/metrics-analytics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/local-development/routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
