---
url: https://developers.cloudflare.com/email-service/local-development/sending/
title: Email sending \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:14.896424+00:00
---

# Email sending · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/local-development/sending/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Local development
  4. /Email sending



# Email sending

Test email sending Workers locally using wrangler dev with simulated email delivery

Last updated Jun 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/local-development/sending/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesConfigurationRemote bindings (recommended)Local simulationBasic sending workerTesting locallyKnown limitations Binary attachmentsNext steps

Test email sending functionality locally using `wrangler dev` to simulate email delivery and verify your sending logic before deploying.

Note

If you are using the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) instead of Workers, you can test by sending requests directly with `curl` or any HTTP client without a local development server. The rest of this page covers the Workers local development flow.

## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

## Configuration

Configure your Wrangler file with the email binding:
    
    
    {
    	"name": "email-sending-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"send_email": [{ "name": "EMAIL" }],
    }
    
    
    name = "email-sending-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[send_email]]
    name = "EMAIL"

## Remote bindings (recommended)

Using [remote bindings](https://developers.cloudflare.com/workers/local-development/#remote-bindings) is the recommended way to develop with Email Service locally. By default, `wrangler dev` simulates the email binding locally -- emails are logged to the console but not actually sent. With remote bindings, your Worker runs locally but sends real emails through Email Service.

Set `remote: true` on the email binding in your Wrangler configuration:
    
    
    {
    	"name": "email-sending-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"send_email": [
    		{
    			"name": "EMAIL",
    			"remote": true,
    		},
    	],
    }
    
    
    name = "email-sending-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[send_email]]
    name = "EMAIL"
    remote = true

Then run `wrangler dev` as usual. Calls to `env.EMAIL.send()` will send actual emails through Email Service while your Worker code runs locally.

Caution

Remote bindings send real emails to real recipients. Use test email addresses to avoid sending unintended emails during development.

## Local simulation

When running `wrangler dev` without remote bindings, the email binding is simulated locally. Emails are not sent -- instead, the email content is logged to the console and saved to local files for inspection.

## Basic sending worker
    
    
    export default {
    	async fetch(request, env, ctx) {
    		if (request.method !== "POST") {
    			return new Response("Method not allowed", { status: 405 });
    		}
    
    		try {
    			const emailData = await request.json();
    
    			console.log("Sending email:", {
    				to: emailData.to,
    				from: emailData.from,
    				subject: emailData.subject,
    			});
    
    			const response = await env.EMAIL.send(emailData);
    
    			return new Response(
    				JSON.stringify({
    					success: true,
    					id: response.messageId,
    				}),
    				{
    					headers: { "Content-Type": "application/json" },
    				},
    			);
    		} catch (error) {
    			return new Response(
    				JSON.stringify({
    					success: false,
    					error: error.message,
    				}),
    				{
    					status: 500,
    					headers: { "Content-Type": "application/json" },
    				},
    			);
    		}
    	},
    };

## Testing locally

Start your development server:
    
    
    npx wrangler dev

Send a test email:
    
    
    curl -X POST http://localhost:8787/ \
      -H "Content-Type: application/json" \
      -d '{
        "to": "recipient@example.com",
        "from": "sender@yourdomain.com",
        "subject": "Test Email",
        "html": "<h1>Hello from Wrangler!</h1>",
        "text": "Hello from Wrangler!"
      }'

Wrangler will show output like:
    
    
    [wrangler:info] send_email binding called with MessageBuilder:
    From: sender@yourdomain.com
    To: recipient@example.com
    Subject: Test Email
    
    Text: /tmp/miniflare-.../files/email-text/<message-id>.txt

The email content (text and HTML) is saved to local files that you can inspect to verify your email structure before deploying.

## Known limitations

### Binary attachments

Local development simulates the `send_email` binding locally, but `ArrayBuffer` values in attachment `content` cannot be serialized by the local simulator. If you pass an `ArrayBuffer` (for example, for image or PDF attachments), you will see an error like:
    
    
    Cannot serialize value: [object ArrayBuffer]

**Workaround:** Use string content for text-based attachments during local development. To test binary attachments (images, PDFs), deploy your Worker with `npx wrangler deploy` and test against the deployed version.

This limitation only affects local development — `ArrayBuffer` content works correctly on deployed Workers.

## Next steps

  * Deploy your sending worker: [Send emails get started](https://developers.cloudflare.com/email-service/get-started/send-emails/)
  * See advanced patterns: [Email sending examples](https://developers.cloudflare.com/email-service/examples/email-sending/)



[PreviousHandle hard bounce emails](https://developers.cloudflare.com/email-service/examples/email-routing/hard-bounce-handling/)[NextEmail routing](https://developers.cloudflare.com/email-service/local-development/routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/local-development/sending.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
