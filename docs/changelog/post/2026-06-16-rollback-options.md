---
url: https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/
title: Workflows rollback handlers now include step context \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:36.427418+00:00
---

# Workflows rollback handlers now include step context · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-16-rollback-options/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 23, 2026

## Workflows rollback handlers now include step context

[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) makes it easier to build reliable multi-step applications that can recover when downstream systems fail. Rollback handlers now receive the original [step context](https://developers.cloudflare.com/workflows/build/step-context/) via a `ctx` object for the step being rolled back. This includes `ctx.step.name`, `ctx.step.count`, `ctx.attempt`, and the step `config` with defaults applied.

The [step configuration](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig) includes the retry and timeout settings used for that step, so you can customize your step recovery logic according to those fields.
    
    
    await step.do(
    	"create charge",
    	async () => {
    		const charge = await createCharge();
    		return { chargeId: charge.id };
    	},
    	{
    		rollback: async ({ ctx, output, error }) => {
    			// `output` is the value returned by the step being rolled back.
    			const { chargeId } = output as { chargeId: string };
    			await refundCharge(chargeId, {
    				// `ctx` is the original step context, including step name, count, attempt, and config.
    				reason: `${ctx.step.name}: ${error.message}`,
    			});
    		},
    		rollbackConfig: {
    			// `rollbackConfig` controls retries and timeout for the rollback handler.
    			retries: { limit: 3, delay: "30 seconds", backoff: "linear" },
    			timeout: "5 minutes",
    		},
    	},
    );

Refer to [rollback options](https://developers.cloudflare.com/workflows/build/workers-api/#rollback-options) to learn more.
