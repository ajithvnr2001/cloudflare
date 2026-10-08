---
url: https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/
title: Deploy Hooks are now available for Workers Builds \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:44.037993+00:00
---

# Deploy Hooks are now available for Workers Builds · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 1, 2026

## Deploy Hooks are now available for Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-deploy-hooks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.

Each Deploy Hook is a unique URL tied to a specific branch. Send it a `POST` and your Worker builds and deploys.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/<DEPLOY_HOOK_ID>"

To create one, go to **Workers & Pages** > your Worker > **Settings** > **Builds** > **Deploy Hooks**.

Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/) can rebuild your project on a schedule:
    
    
    export default {
    	async scheduled(event, env, ctx) {
    		ctx.waitUntil(fetch(env.DEPLOY_HOOK_URL, { method: "POST" }));
    	},
    };
    
    
    export default {
      async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext): Promise<void> {
        ctx.waitUntil(fetch(env.DEPLOY_HOOK_URL, { method: "POST" }));
      },
    } satisfies ExportedHandler<Env>;

You can also use Deploy Hooks to [rebuild when your CMS publishes new content](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/#cms-integration) or [deploy from a Slack slash command](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command).

#### Built-in optimizations

  * **Automatic deduplication** : If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.
  * **Last triggered** : The dashboard shows when each hook was last triggered.
  * **Build source** : Your Worker's build history shows which Deploy Hook started each build by name.



Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see [Limits & pricing](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/).

To get started, read the [Deploy Hooks documentation](https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/).
