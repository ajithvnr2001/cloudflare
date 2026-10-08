---
url: https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/
title: WritableStream \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:49.975131+00:00
---

# WritableStream · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  5. /WritableStream



# WritableStream

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/streams/writablestream/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundPropertiesMethodsRelated resources

## Background

A `WritableStream` is the `writable` property of a [`TransformStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/). On the Workers platform, `WritableStream` cannot be directly created using the `WritableStream` constructor.

A typical way to write to a `WritableStream` is to pipe a [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/) to it.
    
    
    readableStream
      .pipeTo(writableStream)
      .then(() => console.log('All data successfully written!'))
      .catch(e => console.error('Something went wrong!', e));

To write to a `WritableStream` directly, you must use its writer.
    
    
    const writer = writableStream.getWriter();
    writer.write(data);

Refer to the [WritableStreamDefaultWriter](https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/) documentation for further detail.

## Properties

  * `locked` boolean

    * A Boolean value to indicate if the writable stream is locked to a writer.



## Methods

  * `abort(reasonstringoptional)` : Promise<void>

    * Aborts the stream. This method returns a promise that fulfills with a response `undefined`. `reason` is an optional human-readable string indicating the reason for cancellation. `reason` will be passed to the underlying sink’s abort algorithm. If this writable stream is one side of a [TransformStream](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/), then its abort algorithm causes the transform’s readable side to become errored with `reason`.

Warning

Any data not yet written is lost upon abort.

  * `getWriter()` : WritableStreamDefaultWriter

    * Gets an instance of `WritableStreamDefaultWriter` and locks the `WritableStream` to that writer instance.



* * *

## Related resources

  * [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  * [Writable streams in the WHATWG Streams API specification ↗︎](https://streams.spec.whatwg.org/#ws-model)



[PreviousTransformStream](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/)[NextWritableStream DefaultWriter](https://developers.cloudflare.com/workers/runtime-apis/streams/writablestreamdefaultwriter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/streams/writablestream.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
