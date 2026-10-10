---
url: https://developers.cloudflare.com/email-service/
title: Cloudflare Email Service \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:29.538468+00:00
---

# Cloudflare Email Service · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/

  1. [Home](https://developers.cloudflare.com/)
  2. /Email Service



# Cloudflare Email Service

Last updated Oct 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesRelated productsMore resources

Send transactional emails and route incoming emails to Workers or email addresses

Cloudflare Email Service provides powerful email capabilities:

  * **Email Sending** Beta for outbound transactional emails 

Available on Workers Paid plan

  * **Email Routing** for handling incoming emails with Workers or routing to email addresses 

Available on Free and Paid plans




Note

Sending to [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#destination-addresses) in your account is free on all plans, even when only Email Routing is configured.

Together, these two features make it possible for you to send and receive emails from your applications. For example, you can use Email Service for:

  * Transactional emails (welcome messages, password resets, order confirmations)
  * Authentication flows (magic links, email verification, two-factor authentication)
  * Notifications and alerts
  * Custom email addresses (support@, contact@, orders@)
  * Emails as a mode of interaction for agents, such as send an email to create an issue in ticket tracking



Access Email Service directly from Cloudflare Workers using [bindings](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/), from any platform using the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/), or over [authenticated SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/):

Send emails with the `EMAIL` binding and handle incoming emails with the `email()` handler in `src/index.ts`:
    
    
    interface Env {
    	EMAIL: SendEmail;
    }
    
    export default {
    	// Handle HTTP requests (Email Sending)
    	async fetch(request, env, ctx): Promise<Response> {
    		// Send a welcome email
    		await env.EMAIL.send({
    			to: "user@example.com",
    			from: "welcome@yourdomain.com",
    			subject: "Welcome to our service!",
    			html: "<h1>Welcome!</h1><p>Thanks for signing up.</p>",
    			text: "Welcome! Thanks for signing up.",
    		});
    
    		return new Response("Email sent successfully");
    	},
    
    	// Handle incoming emails (Email Routing)
    	async email(message, env, ctx): Promise<void> {
    		// Forward to support team
    		if (message.to.includes("support@yourdomain.com")) {
    			await message.forward("team@yourdomain.com");
    		}
    
    		// Send auto-reply
    		await env.EMAIL.send({
    			to: message.from,
    			from: "noreply@yourdomain.com",
    			subject: "We received your message",
    			html: "<h1>Thank you!</h1><p>We'll get back to you soon.</p>",
    		});
    	},
    } satisfies ExportedHandler<Env>;

Add the bindings to your Wrangler configuration file:
    
    
    {
    	"$schema": "node_modules/wrangler/config-schema.json",
    	"name": "<ENTER_WORKER_NAME>",
    	"main": "src/index.ts",
    	"compatibility_date": "$today",
    
    	// Email sending
    	"send_email": [
    		{
    			"name": "EMAIL"
    		}
    	],
    
    	// Email routing
    	"addresses": ["support@yourdomain.com"]
    }
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": "user@example.com",
        "from": "welcome@yourdomain.com",
        "subject": "Welcome to our service!",
        "html": "<h1>Welcome!</h1><p>Thanks for signing up.</p>",
        "text": "Welcome! Thanks for signing up."
      }'

Cloudflare also provides official SDKs for the REST API: [Node](https://developers.cloudflare.com/api/node/), [Python](https://developers.cloudflare.com/api/python/), and [Go](https://developers.cloudflare.com/api/go/).
    
    
    cat > mail.txt <<EOF
    From: welcome@yourdomain.com
    To: user@example.com
    Subject: Welcome to our service!
    
    Thanks for signing up.
    EOF
    
    curl --ssl-reqd \
      --url "smtps://smtp.mx.cloudflare.net:465" \
      --user "api_token:<API_TOKEN>" \
      --mail-from "welcome@yourdomain.com" \
      --mail-rcpt "user@example.com" \
      --upload-file mail.txt

See the full [API reference](https://developers.cloudflare.com/email-service/api/send-emails/) for the REST API, Workers binding, and SMTP.

[Get started](https://developers.cloudflare.com/email-service/get-started/)

* * *

## Features

[Email Sending](https://developers.cloudflare.com/email-service/get-started/send-emails/)

Send transactional emails with high deliverability and global performance.

Use Email Sending

[Email Routing](https://developers.cloudflare.com/email-service/get-started/route-emails/)

Route incoming emails to custom addresses, Workers, or external destinations.

Use Email Routing

[Deliverability](https://developers.cloudflare.com/email-service/concepts/deliverability/)

Automatic IP reputation management and deliverability optimization.

Use Deliverability

[Analytics & Observability](https://developers.cloudflare.com/email-service/observability/)

Monitor email performance with comprehensive metrics and alerting.

Use Analytics & Observability

[API](https://developers.cloudflare.com/email-service/api/)

Send and route emails using the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/), [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/), or [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/).

Use API

* * *

## Related products

[Workers](https://developers.cloudflare.com/workers/)

Build serverless applications that can send emails directly from the edge.

[Queues](https://developers.cloudflare.com/queues/)

Process email events asynchronously with Workers Queues integration.

[Analytics Engine](https://developers.cloudflare.com/analytics/)

Store and analyze custom email metrics with Workers Analytics Engine.

* * *

## More resources

### [Platform limits](https://developers.cloudflare.com/email-service/platform/limits/)

Learn about Email Service limits and quotas.

### [Pricing](https://developers.cloudflare.com/email-service/platform/pricing/)

Understand Email Service pricing and plans.

### [Examples](https://developers.cloudflare.com/email-service/examples/)

Explore practical examples and implementation patterns.

### [Discord](https://discord.cloudflare.com)

Ask questions and discuss Email Service with other developers.

### [Twitter](https://x.com/cloudflaredev)

Follow product announcements and developer updates.

[NextSend emails](https://developers.cloudflare.com/email-service/get-started/send-emails/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
