---
url: https://developers.cloudflare.com/containers/examples/cron/
title: Cron container \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:34.874504+00:00
---

# Cron container · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/examples/cron/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Examples
  4. /Cron container



# Cron container

Running a container on a schedule using Cron Triggers

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/examples/cron/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the scheduleStart and await the taskDefine the taskTest the schedule locally

Run a short container task every two minutes with a Workers [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/). The task prints its scheduled time, then exits.

## Configure the schedule
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "cron-container",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "observability": {
        "enabled": true
      },
      "triggers": {
        "crons": [
          "*/2 * * * *"
        ]
      },
      "containers": [
        {
          "class_name": "CronContainer",
          "scheduling_policy": "durable_object",
          "images": {
            "base": {
              "dockerfile": "./Dockerfile"
            }
          }
        }
      ],
      "durable_objects": {
        "bindings": [
          {
            "name": "CRON_CONTAINER",
            "class_name": "CronContainer"
          }
        ]
      },
      "exports": {
        "CronContainer": {
          "type": "durable-object",
          "storage": "sqlite"
        }
      }
    }
    
    
    name = "cron-container"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [observability]
    enabled = true
    
    [triggers]
    crons = ["*/2 * * * *"]
    
    [[containers]]
    class_name = "CronContainer"
    scheduling_policy = "durable_object"
    
    [containers.images.base]
    dockerfile = "./Dockerfile"
    
    [[durable_objects.bindings]]
    name = "CRON_CONTAINER"
    class_name = "CronContainer"
    
    [exports.CronContainer]
    type = "durable-object"
    storage = "sqlite"

## Start and await the task

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class CronContainer extends DurableObject {
    	currentRun;
    
    	run(startTime) {
    		this.currentRun ??= this.runOnce(startTime).finally(() => {
    			this.currentRun = undefined;
    		});
    		return this.currentRun;
    	}
    
    	async runOnce(startTime) {
    		const container = this.ctx.container;
    		if (!container.running) {
    			container.start({
    				image: container.images.base,
    				instance: "lite",
    				enableInternet: false,
    				env: { MESSAGE: `Scheduled time: ${startTime}` },
    			});
    		}
    		await container.monitor();
    	}
    }
    
    export default {
    	fetch() {
    		return new Response("This Worker runs a scheduled Container task.");
    	},
    	async scheduled(controller, env) {
    		await env.CRON_CONTAINER.getByName("cron").run(
    			new Date(controller.scheduledTime).toISOString(),
    		);
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    interface Env {
    	CRON_CONTAINER: DurableObjectNamespace<CronContainer>;
    }
    
    export class CronContainer extends DurableObject<Env> {
    	private currentRun: Promise<void> | undefined;
    
    	run(startTime: string): Promise<void> {
    		this.currentRun ??= this.runOnce(startTime).finally(() => {
    			this.currentRun = undefined;
    		});
    		return this.currentRun;
    	}
    
    	private async runOnce(startTime: string): Promise<void> {
    		const container = this.ctx.container!;
    		if (!container.running) {
    			container.start({
    				image: container.images.base,
    				instance: "lite",
    				enableInternet: false,
    				env: { MESSAGE: `Scheduled time: ${startTime}` },
    			});
    		}
    		await container.monitor();
    	}
    }
    
    export default {
    	fetch(): Response {
    		return new Response("This Worker runs a scheduled Container task.");
    	},
    	async scheduled(controller: ScheduledController, env: Env): Promise<void> {
    		await env.CRON_CONTAINER.getByName("cron").run(
    			new Date(controller.scheduledTime).toISOString(),
    		);
    	},
    } satisfies ExportedHandler<Env>;

All triggers use the same Durable Object. If a run is still active, another trigger waits for that run instead of starting a second task. This example does not queue overlapping runs or guarantee exactly-once execution. Make tasks idempotent when they modify external data.

`monitor()` reports completion or failure, not HTTP readiness. Keep this task short enough to finish within the [Cron Trigger execution limits](https://developers.cloudflare.com/workers/platform/limits/#duration).

## Define the task

Dockerfiledockerfile
    
    
    FROM alpine:3.20
    CMD ["sh", "-c", "printf '%s\\n' \"$MESSAGE\""]

## Test the schedule locally

Start a Docker-compatible engine and use Wrangler 4.136.0 or later.

npmyarnpnpmbun
    
    
    npm i -D wrangler
    
    
    yarn add -D wrangler
    
    
    pnpm add -D wrangler
    
    
    bun add -d wrangler

npmyarnpnpm
    
    
    npx wrangler dev --test-scheduled
    
    
    yarn wrangler dev --test-scheduled
    
    
    pnpm wrangler dev --test-scheduled

In another terminal, trigger the scheduled handler:
    
    
    curl 'http://localhost:8787/__scheduled?cron=*/2+*+*+*+*'

Check the container logs for the scheduled time. After deployment, Cron Triggers invoke the handler automatically.

[PreviousStatic frontend, container backend](https://developers.cloudflare.com/containers/examples/container-backend/)[NextMonitor container lifecycle](https://developers.cloudflare.com/containers/examples/status-hooks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/examples/cron.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
