---
url: https://developers.cloudflare.com/workers/runtime-apis/eventsource/
title: EventSource \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:43.938956+00:00
---

# EventSource · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/eventsource/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)
  4. /EventSource



# EventSource

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/eventsource/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackground Constructor Properties Methods Events Class Methods

## Background

The [`EventSource` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) interface is a server-sent event API that allows a server to push events to a client. The `EventSource` object is used to receive server-sent events. It connects to a server over HTTP and receives events in a text-based format.

### Constructor
    
    
    let eventSource = new EventSource(url, options);

  * `url` USVString - The URL to which to connect.
  * `options` EventSourceInit - An optional dictionary containing any optional settings.



By default, the `EventSource` will use the global `fetch()` function under the covers to make requests. If you need to use a different fetch implementation as provided by a Cloudflare Workers binding, you can pass the `fetcher` option:
    
    
    export default {
      async fetch(req, env) {
        let eventSource = new EventSource(url, { fetcher: env.MYFETCHER });
        // ...
      }
    };

Note that the `fetcher` option is a Cloudflare Workers specific extension.

### Properties

  * `eventSource.url` USVString read-only 
    * The URL of the event source.
  * `eventSource.readyState` USVString read-only 
    * The state of the connection.
  * `eventSource.withCredentials` Boolean read-only 
    * A Boolean indicating whether the `EventSource` object was instantiated with cross-origin (CORS) credentials set (`true`), or not (`false`).



### Methods

  * `eventSource.close()`
    * Closes the connection.
  * `eventSource.onopen`
    * An event handler called when a connection is opened.
  * `eventSource.onmessage`
    * An event handler called when a message is received.
  * `eventSource.onerror`
    * An event handler called when an error occurs.



### Events

  * `message`
    * Fired when a message is received.
  * `open`
    * Fired when the connection is opened.
  * `error`
    * Fired when an error occurs.



### Class Methods

  * `EventSource.from(readableStreamReadableStream) : EventSource`
    * This is a Cloudflare Workers specific extension that creates a new `EventSource` object from an existing `ReadableStream`. Such an instance does not initiate a new connection but instead attaches to the provided stream.



[PreviousEncoding](https://developers.cloudflare.com/workers/runtime-apis/encoding/)[NextFetch](https://developers.cloudflare.com/workers/runtime-apis/fetch/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/eventsource.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
