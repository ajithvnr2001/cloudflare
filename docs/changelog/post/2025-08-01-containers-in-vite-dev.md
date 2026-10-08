---
url: https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/
title: Develop locally with Containers and the Cloudflare Vite plugin \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:17.964272+00:00
---

# Develop locally with Containers and the Cloudflare Vite plugin · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 1, 2025

## Develop locally with Containers and the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-01-containers-in-vite-dev/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now configure and run [Containers](https://developers.cloudflare.com/containers) alongside your [Worker](https://developers.cloudflare.com/workers) during local development when using the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Previously, you could only develop locally when using [Wrangler](https://developers.cloudflare.com/workers/wrangler/) as your local development server.

#### Configuration

You can simply configure your Worker and your Container(s) in your Wrangler configuration file:
    
    
    {
      "name": "container-starter",
      "main": "src/index.js",
      "containers": [
        {
          "class_name": "MyContainer",
          "image": "./Dockerfile",
          "instances": 5
        }
      ],
      "durable_objects": {
        "bindings": [
          {
            "class_name": "MyContainer",
            "name": "MY_CONTAINER"
          }
        ]
      },
      "migrations": [
        {
          "new_sqlite_classes": [
            "MyContainer"
          ],
          "tag": "v1"
        }
      ],
    }
    
    
    name = "container-starter"
    main = "src/index.js"
    
    [[containers]]
    class_name = "MyContainer"
    image = "./Dockerfile"
    instances = 5
    
    [[durable_objects.bindings]]
    class_name = "MyContainer"
    name = "MY_CONTAINER"
    
    [[migrations]]
    new_sqlite_classes = [ "MyContainer" ]
    tag = "v1"

#### Worker Code

Once your Worker and Containers are configured, you can access the Container instances from your Worker code:
    
    
    import { Container, getContainer } from "@cloudflare/containers";
    
    export class MyContainer extends Container {
      defaultPort = 4000; // Port the container is listening on
      sleepAfter = "10m"; // Stop the instance if requests not sent for 10 minutes
    }
    
    async fetch(request, env) {
      const { "session-id": sessionId } = await request.json();
      // Get the container instance for the given session ID
      const containerInstance = getContainer(env.MY_CONTAINER, sessionId)
      // Pass the request to the container instance on its default port
      return containerInstance.fetch(request);
    }

#### Local development

To develop your Worker locally, start a local dev server by running
    
    
    vite dev

in your terminal.

#### Resources

Learn more about [Cloudflare Containers ↗︎](https://developers.cloudflare.com/containers/) or the [Cloudflare Vite plugin ↗︎](https://developers.cloudflare.com/workers/vite-plugin/) in our developer docs.
