---
url: https://developers.cloudflare.com/browser-run/features/guardrails/
title: Guardrails \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:36.124985+00:00
---

# Guardrails · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/features/guardrails/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Additional features
  4. /Guardrails



# Guardrails

Last updated Sep 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/features/guardrails/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up guardrails Check policy requirements Start a guarded session with Puppeteer REST APIAdd allowed hostnamesUse a domain set Allow common CDN hostnames Use a hosted hostname listBlock all web requestsVerify blocked requestsUse guardrails with Live View

Guardrails limit a Browser Run session's HTTP and HTTPS requests to permitted hostnames.

This allows you to:

  * **Keep automation focused** — Limit each session to hostnames needed for its task.
  * **Support page dependencies** — Include required third-party APIs, scripts, images, and fonts.
  * **Run self-contained pages** — Prevent external HTTP and HTTPS requests.



Session guardrails apply to browser sessions created with [Puppeteer](https://developers.cloudflare.com/browser-run/puppeteer/), [Playwright](https://developers.cloudflare.com/browser-run/playwright/), or [Chrome DevTools Protocol (CDP)](https://developers.cloudflare.com/browser-run/cdp/). They are unavailable for [Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/).

## Set up guardrails

Add the hostname the browser will visit and any hostnames required for redirects, APIs, scripts, images, or fonts. For common or shared hostnames, use a domain set instead of listing each hostname individually.

Set guardrails when you start a new session. The policy remains fixed for the lifetime of that session.

Choose a property based on how you maintain the allowlist:

Property | Type | Use when | Limit  
---|---|---|---  
`allowedDomains` | `string[]` | Your workflow needs a short, stable list with exact hostname control. | 50 entries  
`allowedDomainSets` | `string[]` | Many sessions share a longer list, or your team maintains one centrally. | Four entries  
  
Both properties are optional and form one allowlist. If you omit both, HTTP and HTTPS requests remain unrestricted.

### Check policy requirements

Before starting a session, make sure your guardrail policy meets these requirements:

  * Add no more than 50 entries to `allowedDomains`.
  * Add no more than four entries to `allowedDomainSets`.
  * Write hostname patterns without a scheme, port, or path.
  * Use no more than one wildcard in each hostname pattern.



If a policy does not meet these requirements, Browser Run rejects the session request with a `400` response.

### Start a guarded session with Puppeteer

This function starts a session that permits `example.com`, its subdomains, and hostnames from the `common-cdns` domain set.

The example assumes a browser binding named `MYBROWSER`.

src/index.jsjs
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    export async function startGuardedSession(env) {
    	const browser = await puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com", "*.example.com"],
    			allowedDomainSets: ["common-cdns"],
    		},
    	});
    
    	return browser;
    }

src/index.tsts
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    interface Env {
    	MYBROWSER: Fetcher;
    }
    
    export async function startGuardedSession(env: Env) {
    	const browser = await puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com", "*.example.com"],
    			allowedDomainSets: ["common-cdns"],
    		},
    	});
    
    	return browser;
    }

[Playwright](https://developers.cloudflare.com/browser-run/playwright/) accepts the same `guardrails` object through its `launch()` options.

### REST API

Use the REST API to acquire a guarded session outside Workers. This request assumes `$ACCOUNT_ID` is set and `$CLOUDFLARE_API_TOKEN` has Browser Rendering Write permission.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/browser-run/devtools/browser" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"guardrails": {
    				"allowedDomains": [
    						"example.com",
    						"*.example.com"
    				],
    				"allowedDomainSets": [
    						"common-cdns"
    				]
    		}
    	}'

Compatibility

Use `@cloudflare/puppeteer` 1.4.0 or later. Use `@cloudflare/playwright` 1.3.6 or later.

Guardrails are not supported with [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/).

## Add allowed hostnames

Use `allowedDomains` to specify which hostnames the browser can request.

Each entry must contain only a hostname. Do not include a protocol such as `https://`, a port such as `:443`, or a path such as `/api`.

  * `example.com` allows only `example.com`.
  * `*.example.com` allows subdomains such as `www.example.com` and `api.example.com`, but not `example.com`.



You can use one `*` wildcard in each entry to match variations of a hostname:

Pattern | Matches | Does not match  
---|---|---  
`example.com` | `example.com` | `www.example.com`, `evil-example.com`  
`*.example.com` | `www.example.com`, `api.v1.example.com` | `example.com`, `evilexample.com`  
`*example.com` | `example.com`, `www.example.com`, `evilexample.com` | `example.net`  
`api.*.example.com` | `api.v1.example.com`, `api.staging.example.com` | `api.example.com`  
  
Prefer subdomain wildcards

A prefix wildcard such as `*example.com` also matches lookalike hostnames that an attacker can register, such as `evilexample.com`. Use `*.example.com` instead, and list the apex domain separately if you need it.

## Use a domain set

Domain sets help you reuse shared hostname lists across sessions. The `allowedDomainSets` property accepts the `common-cdns` set name and HTTPS URLs.

### Allow common CDN hostnames

Use the Cloudflare-maintained `common-cdns` set when your page depends on assets served by common content delivery network (CDN) hostnames:
    
    
    {
    	"allowedDomains": ["example.com"],
    	"allowedDomainSets": ["common-cdns"]
    }

Cloudflare maintains the `common-cdns` set and may change it over time. Use `allowedDomains` or a hosted hostname list when you need a fixed set of permitted hostnames.

### Use a hosted hostname list

Use an HTTPS URL for hostname patterns specific to your pages and dependencies:
    
    
    {
    	"allowedDomainSets": ["https://example.com/browser-run-hostnames.txt"]
    }

For example, `browser-run-hostnames.txt` could contain:
    
    
    example.com
    *.example.com
    
    # Third-party API
    api.example.net

The hosted list must meet these requirements:

Requirement | Value  
---|---  
Protocol | HTTPS  
Content type | `text/plain`  
Line format | One hostname pattern per line  
Comments | Lines starting with `#` and blank lines are ignored  
Validation | One invalid line rejects the entire hosted list  
  
Cloudflare caches a hosted list for up to one hour. Updates after the cache refresh affect only newly started sessions, not existing sessions.

## Block all web requests

An empty `allowedDomains` array blocks all HTTP and HTTPS requests. Use it for self-contained pages, such as rendering inline HTML to a screenshot or PDF.

Inline content can render, but the browser cannot request external APIs or assets. Do not include any domain sets with this policy.

Use this policy object as the `guardrails` value across supported integrations:
    
    
    {
    	"allowedDomains": []
    }

## Verify blocked requests

Use Puppeteer to request a hostname outside the allowlist. This example checks the response status and guardrail headers.
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    export async function verifyGuardrails(env) {
    	const browser = await puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com"],
    		},
    	});
    
    	try {
    		const page = await browser.newPage();
    		const response = await page.goto("https://example.org");
    		const status = response?.status();
    		const headers = response?.headers() ?? {};
    
    		if (
    			status !== 403 ||
    			headers["cf-mitigated"] !== "guardrails" ||
    			headers["cf-brapi-guardrails-reason"] !== "not-in-allowlist"
    		) {
    			throw new Error("Expected Browser Run guardrails to block the request");
    		}
    	} finally {
    		await browser.close();
    	}
    }
    
    
    import puppeteer from "@cloudflare/puppeteer";
    
    interface Env {
    	MYBROWSER: Fetcher;
    }
    
    export async function verifyGuardrails(env: Env) {
    	const browser = await puppeteer.launch(env.MYBROWSER, {
    		guardrails: {
    			allowedDomains: ["example.com"],
    		},
    	});
    
    	try {
    		const page = await browser.newPage();
    		const response = await page.goto("https://example.org");
    		const status = response?.status();
    		const headers = response?.headers() ?? {};
    
    		if (
    			status !== 403 ||
    			headers["cf-mitigated"] !== "guardrails" ||
    			headers["cf-brapi-guardrails-reason"] !== "not-in-allowlist"
    		) {
    			throw new Error("Expected Browser Run guardrails to block the request");
    		}
    	} finally {
    		await browser.close();
    	}
    }

A blocked request returns a `403` response with these headers:

Header | Value | Meaning  
---|---|---  
`cf-mitigated` | `guardrails` | Confirms guardrails blocked the request  
`cf-brapi-guardrails-reason` | `not-in-allowlist` | Requested hostname was not permitted  
  
## Use guardrails with Live View

Session guardrails remain active when you use [Live View](https://developers.cloudflare.com/browser-run/features/live-view/). The `{ mode: "readonly" }` Live View setting controls viewer interaction and does not change the session hostname allowlist.

[PreviousReuse sessions](https://developers.cloudflare.com/browser-run/features/reuse-sessions/)[NextOutbound Workers](https://developers.cloudflare.com/browser-run/features/outbound-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/features/guardrails.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
