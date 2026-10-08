---
url: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/
title: ReadableStreamDefaultReader \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:49.843579+00:00
---

# ReadableStreamDefaultReader · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  5. /ReadableStream DefaultReader



# ReadableStream DefaultReader

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundPropertiesMethodsRelated resources

## Background

A reader is used when you want to read from a [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/), rather than piping its output to a [`WritableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/).

A `ReadableStreamDefaultReader` is not instantiated via its constructor. Rather, it is retrieved from a [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/):
    
    
    const { readable, writable } = new TransformStream();
    const reader = readable.getReader();

* * *

## Properties

  * `reader.closed` : Promise

    * A promise indicating if the reader is closed. The promise is fulfilled when the reader stream closes and is rejected if there is an error in the stream.



## Methods

  * `read()` : Promise

    * A promise that returns the next available chunk of data being passed through the reader queue.
  * `cancel(reasonstringoptional)` : void

    * Cancels the stream. `reason` is an optional human-readable string indicating the reason for cancellation. `reason` will be passed to the underlying source’s cancel algorithm -- if this readable stream is one side of a [`TransformStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/), then its cancel algorithm causes the transform’s writable side to become errored with `reason`.

Warning

Any data not yet read is lost.

  * `releaseLock()` : void

    * Releases the lock on the readable stream. A lock cannot be released if the reader has pending read operations. A `TypeError` is thrown and the reader remains locked.



* * *

## Related resources

  * [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  * [Readable streams in the WHATWG Streams API specification ↗︎](https://streams.spec.whatwg.org/#rs-model)



[PreviousReadableStream BYOBReader](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/)[NextTransformStream](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/streams/readablestreamdefaultreader.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
