---
url: https://developers.cloudflare.com/agents/communication-channels/email/
title: Email \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:07.487868+00:00
---

# Email · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/communication-channels/email/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Communication channels
  4. /Email



# Email

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/communication-channels/email/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksBasic patternConfigurationBuild an email agentRelated resources

Email is a communication channel for agents that need to interact with users or systems through inboxes instead of chat UIs. Agents can send outbound email, receive inbound email, route replies back to an existing session, and use email content as part of an agent workflow.

Use email when you want an agent to:

  * Send notifications, summaries, receipts, or follow-up messages.
  * Process inbound messages through [Cloudflare Email Service](https://developers.cloudflare.com/email-service/).
  * Continue a conversation from a reply.
  * Route support, sales, or operational workflows through an agent.



## How it works

Outbound email uses a `send_email` binding in your Worker. Inbound email uses an Email Service routing rule that sends messages to your Worker, where the agent can parse the sender, recipients, headers, and body before deciding how to respond.

For reply handling, include a stable identifier in the reply address, message metadata, or headers so the Worker can route follow-up messages to the right agent instance.

## Basic pattern

Implement `onEmail()` to handle inbound email, and use `sendEmail()` or `replyToEmail()` when the agent needs to send a response.
    
    
    import { Agent, callable, routeAgentEmail } from "agents";
    import { createAddressBasedEmailResolver } from "agents/email";
    
    export class EmailAgent extends Agent {
    	@callable()
    	async sendWelcomeEmail(to) {
    		await this.sendEmail({
    			binding: this.env.EMAIL,
    			to,
    			from: "support@yourdomain.com",
    			replyTo: "support@yourdomain.com",
    			subject: "Welcome",
    			text: "Thanks for signing up. Reply to this email if you need help.",
    		});
    	}
    
    	async onEmail(email) {
    		await this.replyToEmail(email, {
    			fromName: "Support Agent",
    			body: "Thanks for your email. We received it.",
    		});
    	}
    }
    
    export default {
    	async email(message, env) {
    		await routeAgentEmail(message, env, {
    			resolver: createAddressBasedEmailResolver("EmailAgent"),
    		});
    	},
    };
    
    
    import { Agent, callable, routeAgentEmail } from "agents";
    import { createAddressBasedEmailResolver, type AgentEmail } from "agents/email";
    
    export class EmailAgent extends Agent {
    	@callable()
    	async sendWelcomeEmail(to: string) {
    		await this.sendEmail({
    			binding: this.env.EMAIL,
    			to,
    			from: "support@yourdomain.com",
    			replyTo: "support@yourdomain.com",
    			subject: "Welcome",
    			text: "Thanks for signing up. Reply to this email if you need help.",
    		});
    	}
    
    	async onEmail(email: AgentEmail) {
    		await this.replyToEmail(email, {
    			fromName: "Support Agent",
    			body: "Thanks for your email. We received it.",
    		});
    	}
    }
    
    export default {
    	async email(message, env) {
    		await routeAgentEmail(message, env, {
    			resolver: createAddressBasedEmailResolver("EmailAgent"),
    		});
    	},
    } satisfies ExportedHandler<Env>;

## Configuration

Add a `send_email` binding for outbound email, then configure an Email Service routing rule to send inbound mail to your Worker.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "send_email": [
        {
          "name": "EMAIL",
          "remote": true
        }
      ]
    }
    
    
    [[send_email]]
    name = "EMAIL"
    remote = true

The `remote = true` option lets you call the real Email Service API during local development with `wrangler dev`.

## Build an email agent

For a complete walkthrough, including domain setup, bindings, inbound routing, and secure replies, use the email agent example.

### [Email agent](https://developers.cloudflare.com/agents/examples/email-agent/)

Build an agent that sends, receives, routes, and replies to email using Cloudflare Email Service and the Agents SDK.

## Related resources

### [Email Service](https://developers.cloudflare.com/email-service/)

Route, receive, and send email with Cloudflare Email Service.

### [Send email from Workers](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/)

Use the Workers API to send outbound email.

[PreviousVoice](https://developers.cloudflare.com/agents/communication-channels/voice/)[NextSlack](https://developers.cloudflare.com/agents/communication-channels/slack/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/communication-channels/email.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
