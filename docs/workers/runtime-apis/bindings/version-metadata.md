---
url: https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/
title: Version metadata binding \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:42.693575+00:00
---

# Version metadata binding · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Bindings (env)](https://developers.cloudflare.com/workers/runtime-apis/bindings/)
  5. /Version metadata



# Version metadata

Last updated Jul 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Interface

The version metadata binding can be used to access metadata associated with a [version](https://developers.cloudflare.com/workers/versions-and-deployments/#versions) from inside the Workers runtime.

Worker version ID, version tag and timestamp of when the version was created are available through the version metadata binding. They can be used in events sent to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) or to any third-party analytics/metrics service in order to aggregate by Worker version.

To use the version metadata binding, update your Worker's Wrangler file:
    
    
    {
    	"version_metadata": {
    		"binding": "CF_VERSION_METADATA"
    	}
    }
    
    
    [version_metadata]
    binding = "CF_VERSION_METADATA"

### Interface

An example of how to access the version ID and version tag from within a Worker to send events to [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/):
    
    
    export default {
      async fetch(request, env, ctx) {
        const { id: versionId, tag: versionTag, timestamp: versionTimestamp } = env.CF_VERSION_METADATA;
        env.WAE.writeDataPoint({
          indexes: [versionId],
          blobs: [versionTag, versionTimestamp],
          //...
        });
        //...
      },
    };
    
    
    interface Environment {
      CF_VERSION_METADATA: WorkerVersionMetadata;
      WAE: AnalyticsEngineDataset;
    }
    
    export default {
      async fetch(request, env, ctx) {
        const { id: versionId, tag: versionTag } = env.CF_VERSION_METADATA;
        env.WAE.writeDataPoint({
          indexes: [versionId],
          blobs: [versionTag],
          //...
        });
        //...
      },
    } satisfies ExportedHandler<Env>;

[PreviousVectorize ↗︎](https://developers.cloudflare.com/vectorize/reference/client-api/)[NextWorkflows ↗︎](https://developers.cloudflare.com/workflows/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/bindings/version-metadata.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
