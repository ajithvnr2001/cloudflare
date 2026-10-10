---
url: https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/
title: Run AI-generated code on-demand with Code Sandboxes (new) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:51.399476+00:00
---

# Run AI-generated code on-demand with Code Sandboxes (new) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-24-announcing-sandboxes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 25, 2025

## Run AI-generated code on-demand with Code Sandboxes (new)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)[Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing [Sandboxes ↗︎](https://www.npmjs.com/package/@cloudflare/sandbox), which let your Worker run actual processes in a secure, container-based environment.
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    		return sandbox.exec("ls", ["-la"]);
    	},
    };

#### Methods

  * `exec(command: string, args: string[], options?: { stream?: boolean })`:Execute a command in the sandbox.
  * `gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })`: Checkout a git repository in the sandbox.
  * `mkdir(path: string, options: { recursive?: boolean; stream?: boolean })`: Create a directory in the sandbox.
  * `writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })`: Write content to a file in the sandbox.
  * `readFile(path: string, options: { encoding?: string; stream?: boolean })`: Read content from a file in the sandbox.
  * `deleteFile(path: string, options?: { stream?: boolean })`: Delete a file from the sandbox.
  * `renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })`: Rename a file in the sandbox.
  * `moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })`: Move a file from one location to another in the sandbox.
  * `ping()`: Ping the sandbox.



Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.

You can try it today from your Worker, with just a few lines of code. Let us know what you build.
