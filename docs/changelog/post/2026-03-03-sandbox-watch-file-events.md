---
url: https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/
title: Real-time file watching in Sandboxes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:39.530002+00:00
---

# Real-time file watching in Sandboxes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 3, 2026

## Real-time file watching in Sandboxes

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) now support real-time filesystem watching via `sandbox.watch()`. The method returns a [Server-Sent Events ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) stream backed by native inotify, so your Worker receives `create`, `modify`, `delete`, and `move` events as they happen inside the container.

#### `sandbox.watch(path, options)`

Pass a directory path and optional filters. The returned stream is a standard `ReadableStream` you can proxy directly to a browser client or consume server-side.
    
    
    // Stream events to a browser client
    const stream = await sandbox.watch("/workspace/src", {
    	recursive: true,
    	include: ["*.ts", "*.js"],
    });
    
    return new Response(stream, {
    	headers: { "Content-Type": "text/event-stream" },
    });
    
    
    // Stream events to a browser client
    const stream = await sandbox.watch("/workspace/src", {
    	recursive: true,
    	include: ["*.ts", "*.js"],
    });
    
    return new Response(stream, {
    	headers: { "Content-Type": "text/event-stream" },
    });

#### Server-side consumption with `parseSSEStream`

Use `parseSSEStream` to iterate over events inside a Worker without forwarding them to a client.
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src", { recursive: true });
    
    for await (const event of parseSSEStream(stream)) {
    	console.log(event.type, event.path);
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src", { recursive: true });
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	console.log(event.type, event.path);
    }

Each event includes a `type` field (`create`, `modify`, `delete`, or `move`) and the affected `path`. Move events also include a `from` field with the original path.

#### Options

Option | Type | Description  
---|---|---  
`recursive` | `boolean` | Watch subdirectories. Defaults to `false`.  
`include` | `string[]` | Glob patterns to filter events. Omit to receive all events.  
  
#### Upgrade

To update to the latest version:
    
    
    npm i @cloudflare/sandbox@latest

For full API details, refer to the [Sandbox file watching reference](https://developers.cloudflare.com/sandbox/api/file-watching/).
