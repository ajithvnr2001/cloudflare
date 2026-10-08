---
url: https://developers.cloudflare.com/workers/ci-cd/builds/event-subscriptions/
title: Event subscriptions \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:12.386910+00:00
---

# Event subscriptions · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/builds/event-subscriptions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[CI/CD](https://developers.cloudflare.com/workers/ci-cd/)

  4. /[Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  5. /Event subscriptions



# Event subscriptions

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/builds/event-subscriptions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSend build notificationsAvailable Workers Builds events

[Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) allow you to receive messages when events occur across your Cloudflare account. Cloudflare products (e.g., [KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers](https://developers.cloudflare.com/workers/)) can publish structured events to a [queue](https://developers.cloudflare.com/queues/), which you can then consume with Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) to build custom workflows, integrations, or logic.

For more information on [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/), refer to the [management guide](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

## Send build notifications

You can deploy a Worker that consumes build events and sends notifications to Slack, Discord, or any webhook endpoint:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template)

The template sends notifications for:

  * Successful builds with preview or live deployment URLs
  * Failed builds with error messages
  * Cancelled builds

![Example Slack notifications for Workers Builds events](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1700,height=1088,format=webp/_astro/builds-notifications-slack.rcRiU95L.png)

You can customize the Worker to format messages for your webhook provider. For setup instructions, refer to the [template README ↗︎](https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme).

## Available Workers Builds events

#### `build.started`

Triggered when a build starts.

**Example:**
    
    
    {
      "type": "cf.workersBuilds.worker.build.started",
      "source": {
        "type": "workersBuilds.worker",
        "workerName": "my-worker"
      },
      "payload": {
        "buildUuid": "build-12345678-90ab-cdef-1234-567890abcdef",
        "status": "running",
        "buildOutcome": null,
        "createdAt": "2025-05-01T02:48:57.132Z",
        "initializingAt": "2025-05-01T02:48:58.132Z",
        "runningAt": "2025-05-01T02:48:59.132Z",
        "stoppedAt": null,
        "buildTriggerMetadata": {
          "buildTriggerSource": "push_event",
          "branch": "main",
          "commitHash": "abc123def456",
          "commitMessage": "Fix bug in authentication",
          "author": "developer@example.com",
          "buildCommand": "npm run build",
          "deployCommand": "wrangler deploy",
          "rootDirectory": "/",
          "repoName": "my-worker-repo",
          "providerAccountName": "github-user",
          "providerType": "github"
        }
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

#### `build.failed`

Triggered when a build fails.

**Example:**
    
    
    {
      "type": "cf.workersBuilds.worker.build.failed",
      "source": {
        "type": "workersBuilds.worker",
        "workerName": "my-worker"
      },
      "payload": {
        "buildUuid": "build-12345678-90ab-cdef-1234-567890abcdef",
        "status": "failed",
        "buildOutcome": "failure",
        "createdAt": "2025-05-01T02:48:57.132Z",
        "initializingAt": "2025-05-01T02:48:58.132Z",
        "runningAt": "2025-05-01T02:48:59.132Z",
        "stoppedAt": "2025-05-01T02:50:00.132Z",
        "buildTriggerMetadata": {
          "buildTriggerSource": "push_event",
          "branch": "main",
          "commitHash": "abc123def456",
          "commitMessage": "Fix bug in authentication",
          "author": "developer@example.com",
          "buildCommand": "npm run build",
          "deployCommand": "wrangler deploy",
          "rootDirectory": "/",
          "repoName": "my-worker-repo",
          "providerAccountName": "github-user",
          "providerType": "github"
        }
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

#### `build.canceled`

Triggered when a build is canceled.

**Example:**
    
    
    {
      "type": "cf.workersBuilds.worker.build.canceled",
      "source": {
        "type": "workersBuilds.worker",
        "workerName": "my-worker"
      },
      "payload": {
        "buildUuid": "build-12345678-90ab-cdef-1234-567890abcdef",
        "status": "canceled",
        "buildOutcome": "canceled",
        "createdAt": "2025-05-01T02:48:57.132Z",
        "initializingAt": "2025-05-01T02:48:58.132Z",
        "runningAt": "2025-05-01T02:48:59.132Z",
        "stoppedAt": "2025-05-01T02:49:30.132Z",
        "buildTriggerMetadata": {
          "buildTriggerSource": "push_event",
          "branch": "main",
          "commitHash": "abc123def456",
          "commitMessage": "Fix bug in authentication",
          "author": "developer@example.com",
          "buildCommand": "npm run build",
          "deployCommand": "wrangler deploy",
          "rootDirectory": "/",
          "repoName": "my-worker-repo",
          "providerAccountName": "github-user",
          "providerType": "github"
        }
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

#### `build.succeeded`

Triggered when a build succeeds.

**Example:**
    
    
    {
      "type": "cf.workersBuilds.worker.build.succeeded",
      "source": {
        "type": "workersBuilds.worker",
        "workerName": "my-worker"
      },
      "payload": {
        "buildUuid": "build-12345678-90ab-cdef-1234-567890abcdef",
        "status": "success",
        "buildOutcome": "success",
        "createdAt": "2025-05-01T02:48:57.132Z",
        "initializingAt": "2025-05-01T02:48:58.132Z",
        "runningAt": "2025-05-01T02:48:59.132Z",
        "stoppedAt": "2025-05-01T02:50:15.132Z",
        "buildTriggerMetadata": {
          "buildTriggerSource": "push_event",
          "branch": "main",
          "commitHash": "abc123def456",
          "commitMessage": "Fix bug in authentication",
          "author": "developer@example.com",
          "buildCommand": "npm run build",
          "deployCommand": "wrangler deploy",
          "rootDirectory": "/",
          "repoName": "my-worker-repo",
          "providerAccountName": "github-user",
          "providerType": "github"
        }
      },
      "metadata": {
        "accountId": "f9f79265f388666de8122cfb508d7776",
        "eventSubscriptionId": "1830c4bb612e43c3af7f4cada31fbf3f",
        "eventSchemaVersion": 1,
        "eventTimestamp": "2025-05-01T02:48:57.132Z"
      }
    }

[PreviousAdvanced setups](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/)[NextTroubleshooting builds](https://developers.cloudflare.com/workers/ci-cd/builds/troubleshoot/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/builds/event-subscriptions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
