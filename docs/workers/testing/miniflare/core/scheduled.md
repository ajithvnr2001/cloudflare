---
url: https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/
title: Scheduled Events \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:54.877278+00:00
---

# Scheduled Events · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Core
  5. /Scheduled Events



# Scheduled Events

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCron TriggersHTTP TriggersDispatching Events

  * [`ScheduledEvent` Reference](https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/)



## Cron Triggers

`scheduled` events are automatically dispatched according to the specified cron triggers:
    
    
    const mf = new Miniflare({
    	crons: ["15 * * * *", "45 * * * *"],
    });

## HTTP Triggers

Because waiting for cron triggers is annoying, you can also make HTTP requests to `/cdn-cgi/local/scheduled` to trigger `scheduled` events:
    
    
    $ curl "http://localhost:8787/cdn-cgi/local/scheduled"

To simulate different values of `scheduledTime` and `cron` in the dispatched event, use the `time` and `cron` query parameters:
    
    
    $ curl "http://localhost:8787/cdn-cgi/local/scheduled?time=1000"
    $ curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*"

## Dispatching Events

When using the API, the `getWorker` function can be used to dispatch `scheduled` events to your Worker. This can be used for testing responses. It takes optional `scheduledTime` and `cron` parameters, which default to the current time and the empty string respectively. It will return a promise which resolves to an array containing data returned by all waited promises:
    
    
    import { Miniflare } from "miniflare";
    
    const mf = new Miniflare({
    	modules: true,
    	script: `
      export default {
        async scheduled(controller, env, ctx) {
          const lastScheduledController = controller;
          if (controller.cron === "* * * * *") controller.noRetry();
        }
      }
      `,
    });
    
    const worker = await mf.getWorker();
    
    let scheduledResult = await worker.scheduled({
    	cron: "* * * * *",
    });
    console.log(scheduledResult); // { outcome: 'ok', noRetry: true }
    
    scheduledResult = await worker.scheduled({
    	scheduledTime: new Date(1000),
    	cron: "30 * * * *",
    });
    
    console.log(scheduledResult); // { outcome: 'ok', noRetry: false }

[PreviousQueues](https://developers.cloudflare.com/workers/testing/miniflare/core/queues/)[NextVariables and Secrets](https://developers.cloudflare.com/workers/testing/miniflare/core/variables-secrets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/core/scheduled.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
