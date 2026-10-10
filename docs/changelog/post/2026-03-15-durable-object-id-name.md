---
url: https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/
title: Access Durable Object name via `ctx.id.name` \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.376380+00:00
---

# Access Durable Object name via `ctx.id.name` · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-15-durable-object-id-name/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 15, 2026

## Access Durable Object name via `ctx.id.name`

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When your Worker accesses a Durable Object via `idFromName()` or `getByName()`, the same name is now available on `ctx.id.name` inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the [Workers runtime types](https://developers.cloudflare.com/workers/languages/typescript/).

This is especially useful for [alarms](https://developers.cloudflare.com/durable-objects/api/alarms/), where there is no calling client to pass the name as an argument. When an alarm handler runs, `ctx.id.name` will hold the same name the object was originally accessed with.
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class ChatRoom extends DurableObject {
      async getRoomName() {
        // ctx.id.name returns the name passed to getByName() or idFromName()
        return this.ctx.id.name;
      }
    }
    
    // Worker
    export default {
      async fetch(request, env) {
        const stub = env.CHAT_ROOM.getByName("general");
        const roomName = await stub.getRoomName();
        return new Response(`Welcome to ${roomName}!`);
      },
    };

`ctx.id.name` is `undefined` in the following cases:

  * For Durable Objects created with `newUniqueId()`.
  * When accessed via `idFromString()`, even if the ID was originally created from a name.
  * For [names longer than 1,024 bytes](https://developers.cloudflare.com/durable-objects/api/id/#name).



This works the same way in local development with `wrangler dev` as it does in production. Run `npm update wrangler` to ensure you are on a version with this support.

For more information, refer to the [Durable Object ID documentation](https://developers.cloudflare.com/durable-objects/api/id/#name).
