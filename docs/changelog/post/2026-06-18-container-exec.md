---
url: https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/
title: exec() is now available for Containers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:58.706053+00:00
---

# exec() is now available for Containers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 18, 2026

## exec() is now available for Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`exec()` is now available for [Containers](https://developers.cloudflare.com/containers/). Use `this.ctx.container.exec()` to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.

Call `exec()` from a class extending `Container`, or from another Durable Object through `this.ctx.container`. The associated Container must already be running.

This example starts the Container when needed, then reads its Node.js version:

src/index.jsjs
    
    
    import { Container } from "@cloudflare/containers";
    
    export class MyContainer extends Container {
    	async readVersion() {
    		if (!this.ctx.container.running) {
    			await this.start();
    		}
    
    		const process = await this.ctx.container.exec(["node", "--version"]);
    		const output = await process.output();
    		const decoder = new TextDecoder();
    
    		return {
    			exitCode: output.exitCode,
    			stdout: decoder.decode(output.stdout),
    			stderr: decoder.decode(output.stderr),
    		};
    	}
    }

src/index.tsts
    
    
    import { Container } from "@cloudflare/containers";
    
    export class MyContainer extends Container {
    	async readVersion() {
    		if (!this.ctx.container.running) {
    			await this.start();
    		}
    
    		const process = await this.ctx.container.exec(["node", "--version"]);
    		const output = await process.output();
    		const decoder = new TextDecoder();
    
    		return {
    			exitCode: output.exitCode,
    			stdout: decoder.decode(output.stdout),
    			stderr: decoder.decode(output.stderr),
    		};
    	}
    }

The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.

One RPC method can coordinate multiple `exec()` calls in one caller-to-Durable Object round trip. It can also pass byte-oriented `ReadableStream` input or return streamed output with flow control.

For options and streaming examples, refer to [Execute commands](https://developers.cloudflare.com/containers/guides/execute-commands/).
