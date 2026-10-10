---
url: https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/
title: New getByName() API to access Durable Objects \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:49.879903+00:00
---

# New getByName() API to access Durable Objects · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 21, 2025

## New getByName() API to access Durable Objects

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create a client (a [Durable Object stub](https://developers.cloudflare.com/durable-objects/api/stub/)) to a Durable Object with the new `getByName` method, removing the need to convert Durable Object names to IDs and then create a stub.
    
    
    // Before: (1) translate name to ID then (2) get a client 
    const objectId = env.MY_DURABLE_OBJECT.idFromName("foo"); // or .newUniqueId()
    const stub = env.MY_DURABLE_OBJECT.get(objectId); 
    
    // Now: retrieve client to Durable Object directly via its name 
    const stub = env.MY_DURABLE_OBJECT.getByName("foo");
    
    // Use client to send request to the remote Durable Object
    const rpcResponse = await stub.sayHello();

Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.

To learn more, visit the Durable Objects [API Documentation](https://developers.cloudflare.com/durable-objects/api/namespace/#getbyname) or the [getting started guide](https://developers.cloudflare.com/durable-objects/get-started/).
