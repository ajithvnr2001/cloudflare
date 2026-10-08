---
url: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/
title: ReadableStreamBYOBReader \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:49.559938+00:00
---

# ReadableStreamBYOBReader · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  5. /ReadableStream BYOBReader



# ReadableStream BYOBReader

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundMethodsCommon issuesRelated resources

## Background

`BYOB` is an abbreviation of bring your own buffer. A `ReadableStreamBYOBReader` allows reading into a developer-supplied buffer, thus minimizing copies.

An instance of `ReadableStreamBYOBReader` is functionally identical to [`ReadableStreamDefaultReader`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/) with the exception of the `read` method.

A `ReadableStreamBYOBReader` is not instantiated via its constructor. Rather, it is retrieved from a [`ReadableStream`](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/):
    
    
    const { readable, writable } = new TransformStream();
    const reader = readable.getReader({ mode: 'byob' });

* * *

## Methods

  * `read(bufferArrayBufferView)` : Promise<ReadableStreamBYOBReadResult>

    * Returns a promise with the next available chunk of data read into a passed-in buffer.
  * `readAtLeast(minElements, bufferArrayBufferView)` : Promise<ReadableStreamBYOBReadResult>

    * Returns a promise with the next available chunk of data read into a passed-in buffer. The promise will not resolve until at least `minElements` elements have been read. The element size is determined by `bufferArrayBufferView`, for example 4 bytes per element for a `Uint32Array`. However, fewer than `minElements` elements may be returned if the end of the stream is reached or the underlying stream is closed. Specifically:

      * If `minElements` or more elements are available, the promise resolves with `{ value: <buffer view sized to bytes read>, done: false }`.
      * If the stream ends after some data has been read but fewer than `minElements` elements, the promise resolves with the partial data: `{ value: <buffer view sized to bytes actually read>, done: false }`. The next call to `read` or `readAtLeast` will then return `{ value: undefined, done: true }`.
      * If the stream ends with zero bytes available (that is, the stream is already at EOF), the promise resolves with `{ value: <zero-length view>, done: true }`.
      * If the stream errors, the promise rejects.
      * `minElements` must be at least 1, and `minElements * elementSize` must not exceed the byte length of `bufferArrayBufferView`, or the promise rejects with a `TypeError`. For a `Uint8Array`, element size is 1, so `minElements` is effectively a byte count.



* * *

## Common issues

Warning

`read` provides no control over the minimum number of bytes that should be read into the buffer. Even if you allocate a 1 MiB buffer, the kernel is perfectly within its rights to fulfill this read with a single byte, whether or not an EOF immediately follows.

In practice, the Workers team has found that `read` typically fills only 1% of the provided buffer.

`readAtLeast` is a non-standard extension to the Streams API which allows users to specify that at least `minElements` elements must be read into the buffer before resolving the read. For a `Uint8Array` (the most common case), each element is one byte, so `minElements` is effectively a byte count. If the stream ends before `minElements` elements are available, the partial data that was read is still returned rather than throwing an error — refer to the `readAtLeast` method documentation above for the full details.

* * *

## Related resources

  * [Streams](https://developers.cloudflare.com/workers/runtime-apis/streams/)
  * [Background about BYOB readers in the Streams API WHATWG specification ↗︎](https://streams.spec.whatwg.org/#byob-readers)



[PreviousReadableStream](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestream/)[NextReadableStream DefaultReader](https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/streams/readablestreambyobreader.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
