---
url: https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/
title: Preview: @cloudflare/computer agent runtime \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:05.865617+00:00
---

# Preview: @cloudflare/computer agent runtime · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 3, 2026

## Preview: @cloudflare/computer agent runtime

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We're releasing an early preview of [`@cloudflare/computer` ↗︎](https://github.com/cloudflare/computer), an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.

`@cloudflare/computer` provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.

Install the package via npm:
    
    
    npm install @cloudflare/computer

Instantiate a `Workspace` inside any Durable Object to give your agent a filesystem and execution runtime:
    
    
    import { Workspace } from "@cloudflare/computer";
    
    export class Agent {
    	workspace = new Workspace({
    		storage: this.ctx.storage,
    	});
    }

Several execution backends are included or you can write your own:

  * **Isolate runtime** — fast, horizontally scalable execution via `just-bash` and Dynamic Workers, ideal for file manipulation and data processing.
  * **Container runtime** — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.



The AI SDK-compatible toolkit provides common agent tools (`read`, `write`, `edit`, `ls`, `exec`) and guides the model to choose the appropriate backend for each task.

For more examples, including a step-by-step tutorial, visit the [`@cloudflare/computer` repository ↗︎](https://github.com/cloudflare/computer).

Read the announcement blog post for more details: [Your agent needs a computer, not a container ↗︎](https://blog.cloudflare.com/cloudflare-computer/).
