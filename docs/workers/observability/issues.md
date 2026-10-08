---
url: https://developers.cloudflare.com/workers/observability/issues/
title: Issues \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:35.242495+00:00
---

# Issues · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/observability/issues/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Observability](https://developers.cloudflare.com/workers/observability/)
  4. /Issues



# Issues

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/observability/issues/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow Issues worksEnable Issues Report handled errorsRelated resourcesPricingLimits

Issues provides built-in error monitoring for Cloudflare Workers. It detects production failures and groups related failures into issues without an SDK or application wrapper.

![Issues overview showing occurrence totals and active and resolved issues.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1856,height=864,format=webp/_astro/issues-overview.Dim3BiE9.png)

## How Issues works

When a Worker throws an uncaught exception, fails an invocation, returns a `5xx` response, or logs an error, Issues records the failure as an occurrence. It groups related occurrences from the same Worker into one issue.

Use the Issues overview to identify recurring failures and changes in activity. To review the diagnostic context for a failure, refer to [Investigate issues](https://developers.cloudflare.com/workers/observability/issues/investigate/).

You can also create an [automation](https://developers.cloudflare.com/workers/observability/issues/automations/) to automatically send an issue to a coding agent, webhook, chat service, or incident-management tool.

## Enable Issues

You can enable Issues through Wrangler, the dashboard, or the Cloudflare CLI (`cf`).

Requires Wrangler 4.134.0 or later.

  1. In your Worker's Wrangler configuration file, set `observability.issues.enabled` to `true`.
         
         {
           "$schema": "./node_modules/wrangler/config-schema.json",
           "observability": {
             "issues": {
               "enabled": true
             }
           }
         }
         
         [observability.issues]
         enabled = true

  2. Deploy your Worker.

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy




  1. Go to the **Issues** page.

[ Go to **Issues** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/issues?status=active)
  2. Select **Enable issues**.




Note

If you deploy with Wrangler, also set `observability.issues.enabled` to `true` in your Wrangler configuration file. Otherwise, the next deployment turns off Issues.

  1. In your `cloudflare.config.ts` file, set `worker.observability.issues.enabled` to `true`.

cloudflare.config.tsts
         
         import { defineConfig } from "cf/config";
         import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };
         
         export default defineConfig({
           worker: {
             name: "example-worker",
             entrypoint,
             compatibilityDate: "<COMPATIBILITY_DATE>",
             observability: {
               issues: {
                 enabled: true,
               },
             },
           },
         });

  2. Deploy your Worker.
         
         cf deploy




Issues processes new traffic after you enable it. It does not process historical failures. Send production traffic to the Worker, then open a detected issue in the Issues dashboard.

### Report handled errors

To record an error that your application catches, pass the caught value to `console.error()` before returning a fallback response.

src/index.jsjs
    
    
    try {
    	return await handleRequest(request);
    } catch (error) {
    	console.error(error);
    	return new Response("Service unavailable", { status: 503 });
    }

src/index.tsts
    
    
    try {
    	return await handleRequest(request);
    } catch (error) {
    	console.error(error);
    	return new Response("Service unavailable", { status: 503 });
    }

## Related resources

  * [Investigate issues](https://developers.cloudflare.com/workers/observability/issues/investigate/)
  * [Set up an automation](https://developers.cloudflare.com/workers/observability/issues/automations/)



## Pricing

Issues is available to all Workers accounts in open beta. It is free to use during the beta period.

## Limits

Limit | Value  
---|---  
Automations per account | 50  
Minimum occurrence threshold | 1  
Recurrence inactivity period | 1 hour to 365 days  
Completed automation-run history | 30 days  
  
[PreviousQuery Builder](https://developers.cloudflare.com/workers/observability/query-builder/)[NextInvestigate issues](https://developers.cloudflare.com/workers/observability/issues/investigate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/observability/issues/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
