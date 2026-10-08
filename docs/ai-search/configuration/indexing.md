---
url: https://developers.cloudflare.com/ai-search/configuration/indexing/
title: Syncing \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:39.355969+00:00
---

# Syncing · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/indexing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)

  4. /Indexing
  5. /Syncing



# Syncing

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/configuration/indexing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExternal data sources Sync interval Trigger syncs from automated pipelinesBuilt-in storageControlsPerformanceAutomatic pausing for inactive instancesBest practices

AI Search automatically indexes your content for search. How indexing works depends on your data source.

## External data sources

For instances connected to a [website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/) or [R2 bucket](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/), AI Search creates jobs to sync your data source. Jobs run automatically on a schedule, every 6 hours by default, and process new, modified, or deleted files to keep your search index up to date.

You can view job status and history in the **Jobs** tab in the dashboard or using the [Instances API](https://developers.cloudflare.com/ai-search/api/instances/rest-api/).

### Sync interval

By default, AI Search runs a sync job every 6 hours. To change how often scheduled syncs run, use the **Sync interval** setting in the dashboard, or set the `sync_interval` field when you [create](https://developers.cloudflare.com/ai-search/api/instances/workers-binding/#create) or [update](https://developers.cloudflare.com/ai-search/api/instances/workers-binding/#update) an instance through the Workers binding or [REST API](https://developers.cloudflare.com/ai-search/api/instances/rest-api/).

The interval can be 15 minutes, 30 minutes, 1 hour, 2 hours, 4 hours, 6 hours, 12 hours, or 24 hours. In the API, `sync_interval` is specified in seconds. The allowed values are `900`, `1800`, `3600`, `7200`, `14400`, `21600` (the default), `43200`, and `86400`.

### Trigger syncs from automated pipelines

Sync jobs normally run on a schedule, but you can also start one programmatically whenever your source content changes. This is useful for connecting AI Search to a CMS or a content pipeline: when a publish event or a build step completes, have it trigger a sync so the index reflects the change without waiting for the next scheduled run.

Trigger a sync job with the Wrangler CLI, for example from a CI/CD step or deploy hook:
    
    
    npx wrangler ai-search jobs create <INSTANCE_NAME>

Or call the [Create job REST API](https://developers.cloudflare.com/ai-search/api/instances/rest-api/#jobs) from a CMS webhook or a Worker. Sync jobs can be triggered at most once every 30 seconds.

## Built-in storage

Files uploaded to [built-in storage](https://developers.cloudflare.com/ai-search/configuration/data-source/built-in-storage/) are indexed immediately. There are no sync jobs. Each file is processed individually as it is uploaded.

## Controls

Action | Description  
---|---  
Trigger sync | Manually start a sync job to scan your external data source for changes. Can be triggered every 30 seconds.  
Cancel job | Cancel a running sync job.  
Pause indexing | Temporarily stop all scheduled sync jobs.  
Resume indexing | Resume scheduled sync jobs, including jobs paused automatically after inactivity.  
Sync individual file | Re-index a specific file.  
  
You can perform these actions from the dashboard, the [REST API](https://developers.cloudflare.com/ai-search/api/instances/rest-api/), or the [Workers binding](https://developers.cloudflare.com/ai-search/api/instances/workers-binding/).

## Performance

The total time to index depends on the number and type of files. Factors that affect performance include:

  * Total number of files and their sizes
  * File formats (for example, images take longer than plain text)
  * Latency of Workers AI models used for embedding and image processing



## Automatic pausing for inactive instances

If an instance receives no search request for 31 days, AI Search automatically pauses its scheduled sync jobs. This applies only to external data sources (website or R2), since built-in storage has no sync jobs. This avoids unnecessary requests to your data source to rescan and sync your instance when it is not being used.

A paused instance stays fully searchable, but source changes are not picked up while sync jobs are paused. After the instance receives search or chat traffic again, AI Search automatically resumes scheduled sync jobs during its activity checks. You can also resume manually with the **Resume indexing** control. Refer to Controls.

## Best practices

To ensure smooth and reliable indexing:

  * Make sure your files are within the [size limit](https://developers.cloudflare.com/ai-search/configuration/data-source/#file-limits) and in a [supported format](https://developers.cloudflare.com/ai-search/configuration/data-source/#supported-file-types) to avoid being skipped.
  * For R2-backed instances, keep your [service API token](https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/) valid to prevent indexing failures.
  * Regularly clean up outdated or unnecessary content to stay within [instance limits](https://developers.cloudflare.com/ai-search/platform/limits-pricing/).



[PreviousHybrid search](https://developers.cloudflare.com/ai-search/configuration/indexing/hybrid-search/)[NextPath filtering](https://developers.cloudflare.com/ai-search/configuration/indexing/path-filtering/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/indexing/syncing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
