---
url: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/
title: ReadableStream \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:49.456632+00:00
---

# ReadableStream · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  5. /ReadableStream



# ReadableStream

Last updated Sep 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundPropertiesMethods PipeToOptionsStatic methodsRelated resources

## Background

A `ReadableStream` is returned by the `readable` property inside [`TransformStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/).

## Properties

  * `locked` boolean 
    * A Boolean value that indicates if the readable stream is locked to a reader.



## Methods

  * `pipeTo(destinationWritableStream, optionsPipeToOptions)` : Promise<void>

    * Pipes the readable stream to a given writable stream `destination` and returns a promise that is fulfilled when the `write` operation succeeds or rejects it if the operation fails.
  * `pipeThrough(transformStream, optionsPipeToOptions)` : ReadableStream

    * Pipes the readable stream to the writable side of a given [`TransformStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/) and returns the transform's readable side, so that calls can be chained. `options` accepts the same values as `pipeTo()`.
  * `getReader(optionsObject)` : ReadableStreamDefaultReader

    * Gets an instance of `ReadableStreamDefaultReader` and locks the `ReadableStream` to that reader instance. This method accepts an object argument indicating options. The only supported option is `mode`, which can be set to `byob` to create a [`ReadableStreamBYOBReader`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/), as shown here:


    
    
    let reader = readable.getReader({ mode: 'byob' });

  * `cancel(reasonstringoptional)` : Promise<void>

    * Cancels the stream. `reason` is an optional human-readable string indicating the reason for cancellation. `reason` will be passed to the underlying source’s cancel algorithm. Any data not yet read is lost.
  * `tee()` : [ReadableStream, ReadableStream]

    * Locks the stream and returns an array of two new `ReadableStream` instances, each of which reads the same data as the original stream. Backpressure to the underlying source follows the branch with the most unread data, which avoids unbounded buffering when one branch reads more slowly than the other, as long as the underlying source responds to backpressure. Refer to [workerd's streams documentation ↗︎](https://github.com/cloudflare/workerd/blob/main/src/workerd/api/streams/README.md#tee-behavior) for implementation details.
  * `values(optionsObject)` : AsyncIterableIterator

    * Returns an async iterator that reads and consumes the chunks of the stream. This method accepts an object argument indicating options. The only supported option is `preventCancel`, which, when `true`, prevents the stream from being canceled when the iterator exits early (for example, from a `break` statement). A `ReadableStream` is also async iterable directly:


    
    
    for await (const chunk of readable) {
    	console.log(chunk);
    }
    
    
    for await (const chunk of readable) {
      console.log(chunk);
    }

### `PipeToOptions`

  * `preventClose` bool

    * When `true`, closure of the source `ReadableStream` will not cause the destination `WritableStream` to be closed.
  * `preventAbort` bool

    * When `true`, errors in the source `ReadableStream` will no longer abort the destination `WritableStream`. `pipeTo` will return a rejected promise with the error from the source or any error that occurred while aborting the destination.



## Static methods

  * `ReadableStream.from(asyncIterable)` : ReadableStream

    * Creates a new `ReadableStream` whose chunks are the values yielded by `asyncIterable`, which may be any iterable or async iterable, including an async generator.


    
    
    const stream = ReadableStream.from(
    	(async function* () {
    		yield "hello ";
    		yield "world";
    	})(),
    );
    
    
    const stream = ReadableStream.from(
      (async function* () {
        yield 'hello ';
        yield 'world';
      })()
    );

* * *

## Related resources

  * [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  * [Readable streams in the WHATWG Streams API specification ↗︎](https://streams.spec.whatwg.org/#rs-model)
  * [MDN’s `ReadableStream` documentation ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream)



[PreviousOverview](https://developers.cloudflare.com/workers/runtime-apis/streams/)[NextReadableStream BYOBReader](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/streams/readablestream.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
