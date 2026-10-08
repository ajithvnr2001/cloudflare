---
url: https://developers.cloudflare.com/email-service/examples/email-sending/signup-flow/
title: User signup flow \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:14.305375+00:00
---

# User signup flow · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/examples/email-sending/signup-flow/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /…

Examples

  4. /Email sending
  5. /User signup flow



# User signup flow

Send welcome and verification emails during user signup with secure token-based email verification.

Last updated Jun 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/email-service/examples/email-sending/signup-flow/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNext steps

This example demonstrates a complete user registration system with welcome emails and email verification.

Configure the email binding and KV namespaces in your Wrangler configuration file:
    
    
    {
    	"send_email": [{ "name": "EMAIL" }],
    	"kv_namespaces": [
    		{ "binding": "USERS", "id": "<USERS_KV_NAMESPACE_ID>" },
    		{
    			"binding": "VERIFICATION_TOKENS",
    			"id": "<VERIFICATION_TOKENS_KV_NAMESPACE_ID>",
    		},
    	],
    	"vars": {
    		"DOMAIN": "yourdomain.com",
    		"COMPANY_NAME": "Acme Inc.",
    	},
    }
    
    
    [[send_email]]
    name = "EMAIL"
    
    [[kv_namespaces]]
    binding = "USERS"
    id = "<USERS_KV_NAMESPACE_ID>"
    
    [[kv_namespaces]]
    binding = "VERIFICATION_TOKENS"
    id = "<VERIFICATION_TOKENS_KV_NAMESPACE_ID>"
    
    [vars]
    DOMAIN = "yourdomain.com"
    COMPANY_NAME = "Acme Inc."

The Worker exposes two routes: `POST /signup` creates a user, stores it in KV, and sends both a welcome email and a verification email containing a tokenized link; `GET /verify` validates that token and marks the user verified. The following code implements both handlers.
    
    
    interface Env {
    	EMAIL: SendEmail;
    	USERS: KVNamespace;
    	VERIFICATION_TOKENS: KVNamespace;
    	DOMAIN: string;
    	COMPANY_NAME: string;
    }
    
    interface User {
    	id: string;
    	email: string;
    	firstName: string;
    	verified: boolean;
    	createdAt: string;
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (url.pathname === "/signup" && request.method === "POST") {
    			return handleSignup(request, env);
    		}
    
    		if (url.pathname === "/verify" && request.method === "GET") {
    			return handleVerification(request, env);
    		}
    
    		return new Response("Not Found", { status: 404 });
    	},
    };
    
    async function handleSignup(request: Request, env: Env): Promise<Response> {
    	const { email, firstName } = await request.json();
    
    	// Validate and check for existing user
    	if (!email || !firstName || !isValidEmail(email)) {
    		return new Response(JSON.stringify({ error: "Invalid input" }), {
    			status: 400,
    		});
    	}
    
    	if (await env.USERS.get(email)) {
    		return new Response(JSON.stringify({ error: "User already exists" }), {
    			status: 409,
    		});
    	}
    
    	// Create user
    	const userId = crypto.randomUUID();
    	const user: User = {
    		id: userId,
    		email,
    		firstName,
    		verified: false,
    		createdAt: new Date().toISOString(),
    	};
    
    	await env.USERS.put(email, JSON.stringify(user));
    
    	// Generate verification token (expires in 1 hour)
    	const verificationToken = crypto.randomUUID();
    	await env.VERIFICATION_TOKENS.put(verificationToken, email, {
    		expirationTtl: 3600,
    	});
    
    	// Send welcome email
    	await env.EMAIL.send({
    		to: email,
    		from: `noreply@${env.DOMAIN}`,
    		subject: `Welcome to ${env.COMPANY_NAME}!`,
    		html: `
          <h1>Welcome ${firstName}!</h1>
          <p>Thanks for joining ${env.COMPANY_NAME}. Please verify your email to get started.</p>
        `,
    	});
    
    	// Send verification email
    	const verificationUrl = `https://${env.DOMAIN}/verify?token=${verificationToken}`;
    	await env.EMAIL.send({
    		to: email,
    		from: `noreply@${env.DOMAIN}`,
    		subject: "Please verify your email address",
    		html: `
          <h1>Verify Your Email</h1>
          <p>Hi ${firstName}! Click the link below to verify your email:</p>
          <a href="${verificationUrl}" style="background: #007bff; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px;">Verify Email</a>
          <p>This link expires in 1 hour.</p>
        `,
    	});
    
    	return new Response(
    		JSON.stringify({
    			success: true,
    			message: "Account created. Please check your email.",
    			userId,
    		}),
    		{ status: 201 },
    	);
    }
    
    async function handleVerification(
    	request: Request,
    	env: Env,
    ): Promise<Response> {
    	const url = new URL(request.url);
    	const token = url.searchParams.get("token");
    
    	if (!token) {
    		return new Response("Missing token", { status: 400 });
    	}
    
    	// Verify token
    	const userEmail = await env.VERIFICATION_TOKENS.get(token);
    	if (!userEmail) {
    		return new Response("Invalid or expired token", { status: 400 });
    	}
    
    	// Get and update user
    	const userData = await env.USERS.get(userEmail);
    	if (!userData) {
    		return new Response("User not found", { status: 404 });
    	}
    
    	const user: User = JSON.parse(userData);
    	user.verified = true;
    
    	await env.USERS.put(user.email, JSON.stringify(user));
    	await env.VERIFICATION_TOKENS.delete(token);
    
    	return new Response(
    		`
        <html>
          <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
            <h1>Email Verified!</h1>
            <p>Welcome ${user.firstName}! Your account is now active.</p>
            <a href="/" style="background: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px;">Continue</a>
          </body>
        </html>
      `,
    		{
    			headers: { "Content-Type": "text/html" },
    		},
    	);
    }
    
    function isValidEmail(email: string): boolean {
    	return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

## Next steps

  * [Magic link authentication](https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/) — passwordless login flow using a similar token pattern.
  * [Send method](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) — full reference for the `send()` method.
  * [Deliverability](https://developers.cloudflare.com/email-service/concepts/deliverability/) — keep verification emails out of spam folders.



[PreviousSpecify recipients](https://developers.cloudflare.com/email-service/examples/email-sending/recipients/)[NextMagic link authentication](https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/examples/email-sending/signup-flow.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
