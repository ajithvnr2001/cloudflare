---
url: https://developers.cloudflare.com/basin-pipelines/reference/legacy-pipelines/
title: Legacy pipelines \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:25.196879+00:00
---

# Legacy pipelines · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/reference/legacy-pipelines/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /Reference
  4. /Legacy pipelines



# Legacy pipelines

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-pipelines/reference/legacy-pipelines/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNotable changesMoving to new pipelines

Legacy pipelines, those created before September 25, 2025 via the legacy API, are on a deprecation path.

To check if your pipelines are legacy pipelines, view them in the dashboard under **Basin Pipelines** > **Pipelines** or run the `basin pipelines list` command in [Wrangler](https://developers.cloudflare.com/workers/wrangler/). Legacy pipelines are labeled "legacy" in both locations.

New pipelines offer SQL transformations, multiple output formats, and improved architecture.

## Notable changes

  * New pipelines support SQL transformations for data processing.
  * New pipelines write to JSON, Parquet, and Apache Iceberg formats instead of JSON only.
  * New pipelines separate streams, pipelines, and sinks into distinct resources.
  * New pipelines support optional structured schemas with validation.
  * New pipelines offer configurable rolling policies and customizable partitioning.



## Moving to new pipelines

Legacy pipelines continue to work, but new features and improvements are only available in the new pipeline architecture. To migrate:

  1. Create a new pipeline using the interactive setup:

npmyarnpnpm
         
         npx wrangler basin pipelines setup
         
         yarn wrangler basin pipelines setup
         
         pnpm wrangler basin pipelines setup

  2. Configure your new pipeline with the desired streams, SQL transformations, and sinks.

  3. Update your applications to send data to the new stream endpoints.

  4. Once verified, delete your legacy pipeline.




For detailed guidance, refer to the [getting started guide](https://developers.cloudflare.com/basin-pipelines/getting-started/).

[PreviousFan out a stream to multiple Iceberg tables](https://developers.cloudflare.com/basin-pipelines/examples/bluesky-firehose-fanout/)[NextTerraform](https://developers.cloudflare.com/basin-pipelines/reference/terraform/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/reference/legacy-pipelines.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
