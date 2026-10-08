---
url: https://developers.cloudflare.com/workers/testing/miniflare/core/variables-secrets/
title: Variables and Secrets \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:55.052434+00:00
---

# Variables and Secrets · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/testing/miniflare/core/variables-secrets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Testing](https://developers.cloudflare.com/workers/testing/)[Miniflare](https://developers.cloudflare.com/workers/testing/miniflare/)

  4. /Core
  5. /Variables and Secrets



# Variables and Secrets

Last updated Jan 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/variables-secrets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBindingsText and Data BlobsGlobals

## Bindings

Variables and secrets are bound as follows:
    
    
    const mf = new Miniflare({
    	bindings: {
    		KEY1: "value1",
    		KEY2: "value2",
    	},
    });

## Text and Data Blobs

Text and data blobs can be loaded from files. File contents will be read and bound as `string`s and `ArrayBuffer`s respectively.
    
    
    const mf = new Miniflare({
    	textBlobBindings: { TEXT: "text.txt" },
    	dataBlobBindings: { DATA: "data.bin" },
    });

## Globals

Injecting arbitrary globals is not supported by [workerd ↗︎](https://github.com/cloudflare/workerd). If you're using a service Worker, bindings will be injected as globals, but these must be JSON-serializable.

[PreviousScheduled Events](https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/)[NextWeb Standards](https://developers.cloudflare.com/workers/testing/miniflare/core/standards/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/testing/miniflare/core/variables-secrets.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
