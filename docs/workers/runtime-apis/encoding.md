---
url: https://developers.cloudflare.com/workers/runtime-apis/encoding/
title: Encoding \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:43.657071+00:00
---

# Encoding · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/encoding/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)
  4. /Encoding



# Encoding

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/encoding/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTextEncoder Background Constructor Properties MethodsTextDecoder Background Constructor Properties Methods

## TextEncoder

### Background

The `TextEncoder` takes a stream of code points as input and emits a stream of bytes. Encoding types passed to the constructor are ignored and a UTF-8 `TextEncoder` is created.

[`TextEncoder()` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder/TextEncoder) returns a newly constructed `TextEncoder` that generates a byte stream with UTF-8 encoding. `TextEncoder` takes no parameters and throws no exceptions.

### Constructor
    
    
    let encoder = new TextEncoder();

### Properties

  * `encoder.encoding` DOMString read-only 
    * The name of the encoder as a string describing the method the `TextEncoder` uses (always `utf-8`).



### Methods

  * `encode(inputUSVString)` : Uint8Array

    * Encodes a string input.



* * *

## TextDecoder

### Background

The `TextDecoder` interface represents a UTF-8 decoder. Decoders take a stream of bytes as input and emit a stream of code points.

[`TextDecoder()` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/TextDecoder) returns a newly constructed `TextDecoder` that generates a code-point stream.

### Constructor
    
    
    let decoder = new TextDecoder();

### Properties

  * `decoder.encoding` DOMString read-only

    * The name of the decoder that describes the method the `TextDecoder` uses.
  * `decoder.fatal` boolean read-only

    * Indicates if the error mode is fatal.
  * `decoder.ignoreBOM` boolean read-only

    * Indicates if the byte-order marker is ignored.



### Methods

  * `decode()` : DOMString 
    * Decodes using the method specified in the `TextDecoder` object. Learn more at [MDN’s `TextDecoder` documentation ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder/decode).



[PreviousContext (ctx)](https://developers.cloudflare.com/workers/runtime-apis/context/)[NextEventSource](https://developers.cloudflare.com/workers/runtime-apis/eventsource/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/encoding.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
