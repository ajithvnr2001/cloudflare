---
url: https://developers.cloudflare.com/changelog/product/queues/
title: Queues Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:48.441625+00:00
---

# Queues Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/queues/

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

## [Subscribe to Browser Run crawl events](https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/)

[Browser Run](https://developers.cloudflare.com/browser-run/)[Queues](https://developers.cloudflare.com/queues/)

[Browser Run crawl jobs](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) can publish lifecycle events to [Cloudflare Queues](https://developers.cloudflare.com/queues/). Subscribe to started, updated, and finished events to track progress or trigger downstream processing without polling.

To create an account-level subscription, run the following command:

npmyarnpnpm
    
    
    npx wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
    
    
    yarn wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
    
    
    pnpm wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished

For payload examples, refer to the [Browser Run event schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/#browser-run).

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

Jun 4, 2026

## [Billable usage and budget alerts now in product sidebars](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)[D1](https://developers.cloudflare.com/d1/)[R2](https://developers.cloudflare.com/r2/)[KV](https://developers.cloudflare.com/kv/)[Queues](https://developers.cloudflare.com/queues/)[Vectorize](https://developers.cloudflare.com/vectorize/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Containers](https://developers.cloudflare.com/containers/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

May 19, 2026

## [Event subscriptions for Artifacts lifecycle events](https://developers.cloudflare.com/changelog/post/2026-05-19-event-subscriptions/)

[Artifacts](https://developers.cloudflare.com/artifacts/)[Queues](https://developers.cloudflare.com/queues/)

You can now receive [event notifications](https://developers.cloudflare.com/queues/event-subscriptions/) for [Artifacts](https://developers.cloudflare.com/artifacts/) repository changes and consume them from a Worker to build commit-driven automation.

This allows you to:

  * Run custom workflows when a repository is created or imported
  * Kick off a build and deploy a change when an agent pushes to a repo
  * Trigger a review agent on every push



Available events include:

  * **Account-level events** (`artifacts` source) — `repo.created`, `repo.deleted`, `repo.forked`, `repo.imported`
  * **Repository-level events** (`artifacts.repo` source) — `pushed`, `cloned`, `fetched`



To learn more, refer to [Artifacts documentation](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/).

Apr 28, 2026

## [Realtime backlog metrics now available for Queues](https://developers.cloudflare.com/changelog/post/2026-04-28-improved-queues-metrics/)

[Queues](https://developers.cloudflare.com/queues/)

[Queues](https://developers.cloudflare.com/queues/), Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:

  * **`backlog_count`** — the number of unacknowledged messages in the queue
  * **`backlog_bytes`** — the total size of those messages in bytes
  * **`oldest_message_timestamp_ms`** — the timestamp of the oldest unacknowledged message



The following endpoints also now include a `metadata.metrics` object on the result field after successful message consumption:

  * `/accounts/{account_id}/queues/{queue_id}/messages/pull`
  * `/accounts/{account_id}/queues/{queue_id}/messages`
  * `/accounts/{account_id}/queues/{queue_id}/messages/batch`



#### Javascript APIs

Call `env.QUEUE.metrics()` to get realtime backlog metrics:
    
    
    const {
    	backlogCount, // number
    	backlogBytes, // number
    	oldestMessageTimestamp, // Date | undefined
    } = await env.QUEUE.metrics();

`env.QUEUE.send()` and `env.QUEUE.sendBatch()` also now return a metrics object on the response.

You can also query these fields via the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) or view realtime backlog on the [dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/queues).

![Queues realtime backlog](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1402,height=494,format=webp/_astro/2026-04-28-queues-metrics.BYi0hgrD.png)

For more information, refer to [Queues metrics](https://developers.cloudflare.com/queues/observability/metrics/).

Feb 4, 2026

## [Cloudflare Queues now available on Workers Free plan](https://developers.cloudflare.com/changelog/post/2026-02-04-queues-free-plan/)

[Queues](https://developers.cloudflare.com/queues/)

[Cloudflare Queues](https://developers.cloudflare.com/queues) is now part of the Workers free plan, offering guaranteed message delivery across up to **10,000 queues** to either [Cloudflare Workers](https://developers.cloudflare.com/workers) or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers). Every Cloudflare account now includes **10,000 operations per day** across reads, writes, and deletes. For more details on how each operation is defined, refer to [Queues pricing ↗︎](https://developers.cloudflare.com/workers/platform/pricing/#queues).

All features of the existing Queues functionality are available on the free plan, including unlimited [event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/). Note that the maximum retention period on the free tier, however, is 24 hours rather than 14 days.

If you are new to Cloudflare Queues, follow [this guide ↗︎](https://developers.cloudflare.com/queues/get-started/) or try one of our [tutorials](https://developers.cloudflare.com/queues/tutorials/) to get started.

Jan 9, 2026

## [Get notified when your Workers builds succeed or fail](https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/)

[Workers](https://developers.cloudflare.com/workers/)[Queues](https://developers.cloudflare.com/queues/)

You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/).

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) publishes events to a [Queue](https://developers.cloudflare.com/queues/) that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.

You can deploy [this Worker ↗︎](https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template) to your own Cloudflare account to send build notifications to Slack:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template)

The template includes:

  * Build status with Preview/Live URLs for successful deployments
  * Inline error messages for failed builds
  * Branch, commit hash, and author name

![Slack notifications showing build events](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1700,height=1088,format=webp/_astro/builds-notifications-slack.rcRiU95L.png)

For setup instructions, refer to the [template README ↗︎](https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme) or the [Event Subscriptions documentation](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

Aug 19, 2025

## [Subscribe to events from Cloudflare services with Queues](https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/)

[Queues](https://developers.cloudflare.com/queues/)

You can now subscribe to events from other Cloudflare services (for example, [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai), [Workers](https://developers.cloudflare.com/workers)) and consume those events via [Queues](https://developers.cloudflare.com/queues/), allowing you to build custom workflows, integrations, and logic in response to account activity.

![Event subscriptions architecture](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=924,height=403,format=webp/_astro/queues-event-subscriptions.3aVidnXJ.png)

Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products can publish structured events to a queue, which you can then consume with [Workers](https://developers.cloudflare.com/workers/) or [pull via HTTP from anywhere](https://developers.cloudflare.com/queues/configuration/pull-consumers/).

To create a subscription, use the dashboard or [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/queues/#queues-subscription-create):
    
    
    npx wrangler queues subscription create my-queue --source r2 --events bucket.created

An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. Events follow a consistent structure:

Example R2 bucket created eventjson
    
    
    {
      "type": "cf.r2.bucket.created",
      "source": {
        "type": "r2"
      },
      "payload": {
        "name": "my-bucket",
        "location": "WNAM"
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventTimestamp": "2025-07-28T10:30:00Z"
      }
    }

Current [event sources](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/) include [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/), and [Workflows](https://developers.cloudflare.com/workflows/). More sources and events are on the way.

For more information on event subscriptions, available events, and how to get started, refer to our [documentation](https://developers.cloudflare.com/queues/event-subscriptions/).

May 9, 2025

## [Publish messages to Queues directly via HTTP](https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/)

[Queues](https://developers.cloudflare.com/queues/)

You can now publish messages to [Cloudflare Queues](https://developers.cloudflare.com/queues/) directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within [Cloudflare Workers](https://developers.cloudflare.com/workers/). You can already consume from queues via Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/), and now publishing is just as flexible.

Publishing via HTTP requires a [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `Queues Edit` permissions for authentication. Here's a simple example:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<account_id>/queues/<queue_id>/messages" \
      -X POST \
      -H 'Authorization: Bearer <api_token>' \
      --data '{ "body": { "greeting": "hello", "timestamp":  "2025-07-24T12:00:00Z"} }'

You can also use our [SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) for TypeScript, Python, and Go.

To get started with HTTP publishing, check out our [step-by-step example](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/) and the full API documentation in our [API reference](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/push/).

Apr 17, 2025

## [Increased limits for Queues pull consumers](https://developers.cloudflare.com/changelog/post/2025-04-17-pull-consumer-limits/)

[Queues](https://developers.cloudflare.com/queues/)

[Queues pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) can now pull and acknowledge up to **5,000 messages / second per queue**. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.

Pull consumers allow you to consume messages over HTTP from any environment—including outside of [Cloudflare Workers](https://developers.cloudflare.com/workers). They’re also useful when you need fine-grained control over how quickly messages are consumed.

To setup a new queue with a pull based consumer using [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run:

Create a queue with a pull based consumersh
    
    
    npx wrangler queues create my-queue
    npx wrangler queues consumer http add my-queue

You can also configure a pull consumer using the [REST API](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/create/) or the Queues dashboard.

Once configured, you can pull messages from the queue using any HTTP client. You'll need a [Cloudflare API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `queues_read` and `queues_write` permissions. For example:

Pull messages from a queuebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull" \
    --header "Authorization: Bearer ${API_TOKEN}" \
    --header "Content-Type: application/json" \
    --data '{ "visibility_timeout": 10000, "batch_size": 2 }'

To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the [pull consumer documentation](https://developers.cloudflare.com/queues/configuration/pull-consumers).

As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the [existing rate](https://developers.cloudflare.com/queues/platform/pricing), of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

Mar 27, 2025

## [New Pause & Purge APIs for Queues](https://developers.cloudflare.com/changelog/post/2025-03-25-pause-purge-queues/)

[Queues](https://developers.cloudflare.com/queues/)

[Queues](https://developers.cloudflare.com/queues/) now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:

  * Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug
  * You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog
  * Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed



To pause a queue using [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run the `pause-delivery` command. Paused queues continue to receive messages. And you can easily unpause a queue using the `resume-delivery` command.

Pause and resume a queuebash
    
    
    $ wrangler queues pause-delivery my-queue
    Pausing message delivery for queue my-queue.
    Paused message delivery for queue my-queue.
    
    $ wrangler queues resume-delivery my-queue
    Resuming message delivery for queue my-queue.
    Resumed message delivery for queue my-queue.

Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:

Purge a queuebash
    
    
    $ wrangler queues purge my-queue
    ✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue
    Purged queue 'my-queue'

You can also do these operations using the [Queues REST API](https://developers.cloudflare.com/api/resources/queues/), or the dashboard page for a queue.

![Pause and purge using the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2200,height=574,format=webp/_astro/pause-purge.SQ7B3RCF.png)

This feature is available on all new and existing queues. Head over to the [pause and purge documentation](https://developers.cloudflare.com/queues/configuration/pause-purge) to learn more. And if you haven't used Cloudflare Queues before, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

Feb 14, 2025

## [Customize queue message retention periods](https://developers.cloudflare.com/changelog/post/2025-02-14-customize-queue-retention-period/)

[Queues](https://developers.cloudflare.com/queues/)

You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.

![Customize a queue's message retention period](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1898,height=986,format=webp/_astro/customize-retention-period.CpK7s10q.png)

You can customize the retention period on the settings page for your queue, or using Wrangler:

Update message retention periodbash
    
    
    $ wrangler queues update my-queue --message-retention-period-secs 600

This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).
