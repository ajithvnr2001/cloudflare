---
url: https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/
title: Magic link authentication \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:14.162173+00:00
---

# Magic link authentication · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /…

Examples

  4. /Email sending
  5. /Magic link authentication



# Magic link authentication

Implement passwordless authentication by sending secure, time-limited login links via email.

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNext steps

This example demonstrates how to send a magic link email for passwordless authentication using Cloudflare Email Service.

Configure the email binding in your Wrangler configuration file:
    
    
    {
    	"send_email": [{ "name": "EMAIL" }],
    	"vars": {
    		"DOMAIN": "yourdomain.com",
    	},
    }
    
    
    [[send_email]]
    name = "EMAIL"
    
    [vars]
    DOMAIN = "yourdomain.com"

The Worker exposes a `POST /send-magic-link` route that validates the submitted email address, generates a single-use token, and emails the recipient a time-limited login link. The following code implements that handler.
    
    
    interface Env {
    	EMAIL: SendEmail;
    	DOMAIN: string;
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (url.pathname === "/send-magic-link" && request.method === "POST") {
    			return handleSendMagicLink(request, env);
    		}
    
    		return new Response("Not Found", { status: 404 });
    	},
    };
    
    async function handleSendMagicLink(
    	request: Request,
    	env: Env,
    ): Promise<Response> {
    	const { email } = await request.json();
    
    	if (!email || !isValidEmail(email)) {
    		return new Response(JSON.stringify({ error: "Invalid email" }), {
    			status: 400,
    		});
    	}
    
    	// Generate a simple secure token (you would implement proper JWT/token handling)
    	const token = crypto.randomUUID();
    	const magicUrl = `https://${env.DOMAIN}/login?token=${token}`;
    
    	// Send magic link email
    	await env.EMAIL.send({
    		to: email,
    		from: `noreply@${env.DOMAIN}`,
    		subject: "Your login link",
    		html: `
    			<h1>Login to your account</h1>
    			<p>Click the link below to log in:</p>
    			<p><a href="${magicUrl}">Login Now</a></p>
    			<p>This link expires in 15 minutes.</p>
    		`,
    		text: `
    			Login to your account
    			
    			Click this link to log in: ${magicUrl}
    			
    			This link expires in 15 minutes.
    		`,
    	});
    
    	return new Response(
    		JSON.stringify({
    			success: true,
    			message: "Magic link sent to your email",
    		}),
    	);
    }
    
    function isValidEmail(email: string): boolean {
    	return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

## Next steps

  * [User signup flow](https://developers.cloudflare.com/email-service/examples/email-sending/signup-flow/) — combine magic links with account verification.
  * [Send method](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) — full reference for the `send()` method.
  * [Email headers](https://developers.cloudflare.com/email-service/reference/headers/) — add tracking or list-management headers.



[PreviousUser signup flow](https://developers.cloudflare.com/email-service/examples/email-sending/signup-flow/)[NextEmail attachments](https://developers.cloudflare.com/email-service/examples/email-sending/email-attachments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/examples/email-sending/magic-link.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
