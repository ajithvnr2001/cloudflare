---
url: https://developers.cloudflare.com/changelog/product/email-service/
title: Email Service Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:08.225093+00:00
---

# Email Service Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/email-service/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Sep 25, 2026

## [Suppress recipients for one sending domain](https://developers.cloudflare.com/changelog/post/2026-09-25-sending-domain-suppressions/)

[Email Service](https://developers.cloudflare.com/email-service/)

[Email Sending suppressions](https://developers.cloudflare.com/email-service/concepts/suppressions/) now have a **scope** :

  * **`account`** : The suppression applies to every sending domain and subdomain in your account. This is the default.
  * **`sending_domain`** : The suppression applies to one sending domain only. A suppression for `mail.myappexample.com` does not block mail from `myappexample.com`.



Most importantly, Email Sending now automatically creates bounce and complaint suppressions at the sending-domain level. This provides greater granularity by preventing an issue with one sending domain from suppressing the recipient across your entire account.

To add a suppression for one sending domain in the dashboard, go to **Email Sending** > **Suppressions** and select **Sending domain** in **Scope**. Imports can also set a scope for each row or a default scope.

In the API, pass `scope` when you create the suppression:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/email/sending/suppressions \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "email": "user@example.net",
        "scope": { "type": "sending_domain", "value": "mail.myappexample.com" }
      }'

The [suppressions API](https://developers.cloudflare.com/api/resources/email_sending/subresources/suppressions/) returns `scope` on every suppression. To list the suppressions for one domain, use `scope_type=sending_domain&scope_value=mail.myappexample.com`. If you omit `scope`, the API creates an `account` suppression, so existing integrations continue to work.

Refer to [Suppression lists](https://developers.cloudflare.com/email-service/concepts/suppressions/#suppression-scope) and [Manage suppressions](https://developers.cloudflare.com/email-service/configuration/suppressions/) for details.

Sep 4, 2026

## [Manage Email Routing rules with Wrangler](https://developers.cloudflare.com/changelog/post/2026-09-04-email-routing-rules-wrangler/)

[Email Service](https://developers.cloudflare.com/email-service/)[Workers](https://developers.cloudflare.com/workers/)

You can now manage Email Routing rules that route emails to Workers from your Wrangler configuration. Add literal addresses or a catch-all address to the top-level `addresses` field:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "invoice-handler",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-10",
      "addresses": [
        "invoice@yourdomain.com"
      ]
    }
    
    
    name = "invoice-handler"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-10"
    addresses = ["invoice@yourdomain.com"]

When you run `wrangler deploy`, Wrangler creates rules for new addresses, updates existing rules managed by the Worker, and removes managed rules that are no longer in the configuration. Wrangler shows the planned changes and asks for confirmation before applying potentially destructive changes.

Email Routing rules created by Wrangler also appear in the dashboard but with an icon that identifies them.

![Email Routing rule created by Wrangler in dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2440,height=526,format=webp/_astro/wrangler-email-routing-rules-dash.BZQZlAJI.png)

Refer to [Configure rules with Wrangler](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#configure-rules-with-wrangler) for more information.

Jul 17, 2026

## [Preview sent emails in the Activity log](https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/)

[Email Service](https://developers.cloudflare.com/email-service/)

You can now preview the content of sent emails directly from the Email Service Activity log. Expand a sent email and open the new **Preview** section to inspect the message as it was sent, across tabs for the rendered **HTML** body, the **Text** body, the **Headers** , the **Attachments** , and the full **Raw** [RFC 5322 ↗︎](https://datatracker.ietf.org/doc/html/rfc5322) source.

![The rendered HTML preview of a sent email in the Email Service Activity log](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2864,height=1172,format=webp/_astro/email-message-preview.Bj6Lk8Y6.png)

Previously, the Activity log surfaced delivery and authentication metadata but not the message content, making rendering and content issues harder to debug. Message preview closes that gap.

To make messages previewable, turn on **Email preview** in your sending domain's settings. Previews cover messages sent while the setting is turned on and are retained for about seven days. Sending domains onboarded on or after 2026-07-02 have **Email preview** turned on automatically.

![The Email preview setting in a sending domain's settings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2256,height=264,format=webp/_astro/email-preview-setting.XEd1WIiO.png)

Refer to [Email logs](https://developers.cloudflare.com/email-service/observability/logs/#message-preview) for more information.

Jul 15, 2026

## [Subscribe to Email Sending events with Queues](https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/)

[Email Service](https://developers.cloudflare.com/email-service/)[Queues](https://developers.cloudflare.com/queues/)

You can now subscribe to **[Email Sending](https://developers.cloudflare.com/email-service/api/send-emails/) events** through [Queues event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as `example.com`, or a verified sending subdomain, such as `send.example.com`.

Six event types are published: `message.delivered`, `message.deferred`, `message.bounced`, `message.failed`, `message.rejected`, and `message.complained`. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.

Each event includes the message details, delivery status, and SMTP response:
    
    
    {
    	"type": "cf.email.sending.message.delivered",
    	"source": {
    		"type": "email.sending",
    		"zoneId": "023e105f4ecef8ad9ca31a8372d0c353",
    		"domain": "example.com"
    	},
    	"payload": {
    		"messageId": "0101018f7d0c4d9a-msg-deadbeef",
    		"recipient": "user@example.net",
    		"terminal": true,
    		"delivery": {
    			"status": "delivered",
    			"smtpStatusCode": "250"
    		}
    	}
    }

Refer to [Event subscriptions](https://developers.cloudflare.com/email-service/platform/event-subscriptions/) to see all event types and example payloads.

Jun 8, 2026

## [Authenticated SMTP submission now available in beta](https://developers.cloudflare.com/changelog/post/2026-06-08-smtp-submission/)

[Email Service](https://developers.cloudflare.com/email-service/)

You can now send emails through **Cloudflare Email Service** using authenticated [SMTP submission](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) on `smtp.mx.cloudflare.net:465`. SMTP joins the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) and the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, `smtplib`, PHPMailer, JavaMail).

Setting | Value  
---|---  
Host | `smtp.mx.cloudflare.net`  
Port | `465` (implicit TLS)  
AUTH | `PLAIN` or `LOGIN`  
Username | `api_token`  
Password | A Cloudflare API token (account-owned or user-owned) with **Email Sending: Edit**  
  
Submissions enter the same delivery pipeline as the REST API and Workers binding: identical [limits](https://developers.cloudflare.com/email-service/platform/limits/), automatic DKIM and ARC signing, and shared dashboard logs.

Send your first email with a single command:
    
    
    curl --ssl-reqd \
      --url "smtps://smtp.mx.cloudflare.net:465" \
      --user "api_token:<API_TOKEN>" \
      --mail-from "welcome@yourdomain.com" \
      --mail-rcpt "user@example.com" \
      --upload-file mail.txt

Refer to the [SMTP reference](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) for authentication details, response codes, and language-specific examples.

May 28, 2026

## [Send emails with named recipient addresses](https://developers.cloudflare.com/changelog/post/2026-05-28-named-email-recipients/)

[Email Service](https://developers.cloudflare.com/email-service/)

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

Apr 16, 2026

## [Email Sending now in public beta](https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/)

[Email Service](https://developers.cloudflare.com/email-service/)

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

Jul 21, 2025

## [Subaddressing support in Email Routing](https://developers.cloudflare.com/changelog/post/2025-07-21-subaddressing/)

[Email Service](https://developers.cloudflare.com/email-service/)

Subaddressing, as defined in [RFC 5233 ↗︎](https://www.rfc-editor.org/rfc/rfc5233), also known as plus addressing, is now supported in Email Routing. This enables using the "+" separator to augment your custom addresses with arbitrary detail information.

Now you can send an email to `user+detail@example.com` and it will be captured by the `user@example.com` custom address. The `+detail` part is ignored by Email Routing, but it can be captured next in the processing chain in the logs, an [Email Worker](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) or an [Agent application ↗︎](https://github.com/cloudflare/agents/tree/main/examples/email-agent).

Customers can use this feature to dynamically add context to their emails, such as tracking the source of an email or categorizing emails without needing to create multiple custom addresses.

![Subaddressing](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1316,height=678,format=webp/_astro/subaddressing.x65bljxx.png)

Check our [Developer Docs](https://developers.cloudflare.com/email-service/configuration/email-routing-addresses/#subaddressing) to learn how to enable subaddressing in Email Routing.

Jun 30, 2025

## [Mail authentication requirements for Email Routing](https://developers.cloudflare.com/changelog/post/2025-06-30-mail-authentication/)

[Email Service](https://developers.cloudflare.com/email-service/)

The Email Routing platform supports [SPF ↗︎](https://datatracker.ietf.org/doc/html/rfc7208) records and [DKIM (DomainKeys Identified Mail) ↗︎](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) signatures and honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them, we still forward the emails to upstream mailbox providers.

Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to forward them. We also strongly recommend that all senders implement the DMARC protocol.

If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where the forward action may fail due to missing authentication on the incoming email.

SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking bad emails. If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure you have them properly configured.

Apr 8, 2025

## [Local development support for Email Workers](https://developers.cloudflare.com/changelog/post/2025-04-08-local-development/)

[Email Service](https://developers.cloudflare.com/email-service/)

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

Mar 12, 2025

## [Threaded replies now possible in Email Workers](https://developers.cloudflare.com/changelog/post/2025-03-12-reply-limits/)

[Email Service](https://developers.cloudflare.com/email-service/)

We’re removing some of the restrictions in Email Routing so that AI Agents and task automation can better handle email workflows, including how Workers can [reply](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/#reply-to-emails) to incoming emails.

It's now possible to keep a threaded email conversation with an [Email Worker](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/) script as long as:

  * The incoming email has to have valid [DMARC ↗︎](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/).
  * The email can only be replied to once in the same `EmailMessage` event.
  * The recipient in the reply must match the incoming sender.
  * The outgoing sender domain must match the same domain that received the email.
  * Every time an email passes through Email Routing or another MTA, an entry is added to the `References` list. We stop accepting replies to emails with more than 100 `References` entries to prevent abuse or accidental loops.



Here's an example of a Worker responding to Emails using a Workers AI model:

AI model responding to emailsts
    
    
    import PostalMime from "postal-mime";
    import { createMimeMessage } from "mimetext";
    import { EmailMessage } from "cloudflare:email";
    
    export default {
    	async email(message, env, ctx) {
    		const email = await PostalMime.parse(message.raw);
    		const res = await env.AI.run("@cf/meta/llama-2-7b-chat-fp16", {
    			messages: [
    				{
    					role: "user",
    					content: email.text ?? "",
    				},
    			],
    		});
    
    		// message-id is generated by mimetext
    		const response = createMimeMessage();
    		response.setHeader("In-Reply-To", message.headers.get("Message-ID")!);
    		response.setSender("agent@example.com");
    		response.setRecipient(message.from);
    		response.setSubject("Llama response");
    		response.addMessage({
    			contentType: "text/plain",
    			data:
    				res instanceof ReadableStream
    					? await new Response(res).text()
    					: res.response!,
    		});
    
    		const replyMessage = new EmailMessage(
    			"<email>",
    			message.from,
    			response.asRaw(),
    		);
    		await message.reply(replyMessage);
    	},
    } satisfies ExportedHandler<Env>;

See [Reply to emails from Workers](https://developers.cloudflare.com/email-service/api/route-emails/email-handler/#reply-to-emails) for more information.
