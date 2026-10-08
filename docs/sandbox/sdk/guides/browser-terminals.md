---
url: https://developers.cloudflare.com/sandbox/sdk/guides/browser-terminals/
title: Browser terminals (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:24.435448+00:00
---

# Browser terminals (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/browser-terminals/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /Browser terminals



# Browser terminals

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/browser-terminals/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesHandle WebSocket upgrades in the WorkerConnect with xterm.js and SandboxAddonConnect without xterm.jsBest practicesRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Open a terminal in the browser](https://developers.cloudflare.com/sandbox/commands/open-a-terminal-in-the-browser/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

This guide shows you how to connect a browser-based terminal to a sandbox shell. You can use the `SandboxAddon` with xterm.js, or connect directly over WebSockets.

## Prerequisites

You need an existing Cloudflare Worker with a sandbox binding. Refer to [Getting started](https://developers.cloudflare.com/sandbox/sdk/get-started/) if you do not have one.

Install the terminal dependencies in your frontend project:

npmyarnpnpmbun
    
    
    npm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox
    
    
    yarn install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox
    
    
    pnpm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox
    
    
    bun install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox

If you are not using xterm.js, you only need `@cloudflare/sandbox` for types.

## Handle WebSocket upgrades in the Worker

Add a route that proxies WebSocket connections to the sandbox terminal. The example below supports both the default session and named sessions via a query parameter:
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    
    		if (
    			url.pathname === "/ws/terminal" &&
    			request.headers.get("Upgrade") === "websocket"
    		) {
    			const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    			const sessionId = url.searchParams.get("session");
    
    			if (sessionId) {
    				const session = await sandbox.getSession(sessionId);
    				return await session.terminal(request);
    			}
    
    			return await sandbox.terminal(request, { cols: 80, rows: 24 });
    		}
    
    		return new Response("Not found", { status: 404 });
    	},
    };
    
    
    import { getSandbox } from '@cloudflare/sandbox';
    
    export { Sandbox } from '@cloudflare/sandbox';
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        const url = new URL(request.url);
    
        if (url.pathname === '/ws/terminal' && request.headers.get('Upgrade') === 'websocket') {
          const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
          const sessionId = url.searchParams.get('session');
    
          if (sessionId) {
            const session = await sandbox.getSession(sessionId);
            return await session.terminal(request);
          }
    
          return await sandbox.terminal(request, { cols: 80, rows: 24 });
        }
    
        return new Response('Not found', { status: 404 });
      }
    };

## Connect with xterm.js and SandboxAddon

Create the terminal in your browser code and attach the `SandboxAddon`. The addon manages the WebSocket connection, automatic reconnection, and resize forwarding.
    
    
    import { Terminal } from "@xterm/xterm";
    import { FitAddon } from "@xterm/addon-fit";
    import { SandboxAddon } from "@cloudflare/sandbox/xterm";
    import "@xterm/xterm/css/xterm.css";
    
    const terminal = new Terminal({ cursorBlink: true });
    const fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    
    const addon = new SandboxAddon({
    	getWebSocketUrl: ({ sandboxId, sessionId, origin }) => {
    		const params = new URLSearchParams({ id: sandboxId });
    		if (sessionId) params.set("session", sessionId);
    		return `${origin}/ws/terminal?${params}`;
    	},
    	onStateChange: (state, error) => {
    		console.log(`Terminal ${state}`, error ?? "");
    	},
    });
    
    terminal.loadAddon(addon);
    terminal.open(document.getElementById("terminal"));
    fitAddon.fit();
    
    // Connect to the default session
    addon.connect({ sandboxId: "my-sandbox" });
    
    // Or connect to a specific session
    // addon.connect({ sandboxId: 'my-sandbox', sessionId: 'development' });
    
    window.addEventListener("resize", () => fitAddon.fit());
    
    
    import { Terminal } from '@xterm/xterm';
    import { FitAddon } from '@xterm/addon-fit';
    import { SandboxAddon } from '@cloudflare/sandbox/xterm';
    import '@xterm/xterm/css/xterm.css';
    
    const terminal = new Terminal({ cursorBlink: true });
    const fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    
    const addon = new SandboxAddon({
      getWebSocketUrl: ({ sandboxId, sessionId, origin }) => {
        const params = new URLSearchParams({ id: sandboxId });
        if (sessionId) params.set('session', sessionId);
        return `${origin}/ws/terminal?${params}`;
      },
      onStateChange: (state, error) => {
        console.log(`Terminal ${state}`, error ?? '');
      }
    });
    
    terminal.loadAddon(addon);
    terminal.open(document.getElementById('terminal'));
    fitAddon.fit();
    
    // Connect to the default session
    addon.connect({ sandboxId: 'my-sandbox' });
    
    // Or connect to a specific session
    // addon.connect({ sandboxId: 'my-sandbox', sessionId: 'development' });
    
    window.addEventListener('resize', () => fitAddon.fit());

For the full addon API, refer to the [Terminal API reference](https://developers.cloudflare.com/sandbox/sdk/api/terminal/).

## Connect without xterm.js

If you are building a custom terminal UI or running in an environment without xterm.js, connect directly over WebSockets. The protocol uses binary frames for terminal data and JSON text frames for control messages.
    
    
    const ws = new WebSocket("wss://example.com/ws/terminal?id=my-sandbox");
    ws.binaryType = "arraybuffer";
    
    const decoder = new TextDecoder();
    const encoder = new TextEncoder();
    
    ws.addEventListener("message", (event) => {
    	if (event.data instanceof ArrayBuffer) {
    		// Terminal output (binary) — includes ANSI escape sequences
    		const text = decoder.decode(event.data);
    		appendToDisplay(text);
    		return;
    	}
    
    	// Control message (JSON text)
    	const msg = JSON.parse(event.data);
    
    	switch (msg.type) {
    		case "ready":
    			// Terminal is accepting input — send initial resize
    			ws.send(JSON.stringify({ type: "resize", cols: 80, rows: 24 }));
    			break;
    
    		case "exit":
    			console.log(`Shell exited: code ${msg.code}`);
    			break;
    
    		case "error":
    			console.error("Terminal error:", msg.message);
    			break;
    	}
    });
    
    // Send keystrokes as binary
    function sendInput(text) {
    	if (ws.readyState === WebSocket.OPEN) {
    		ws.send(encoder.encode(text));
    	}
    }
    
    
    const ws = new WebSocket('wss://example.com/ws/terminal?id=my-sandbox');
    ws.binaryType = 'arraybuffer';
    
    const decoder = new TextDecoder();
    const encoder = new TextEncoder();
    
    ws.addEventListener('message', (event) => {
      if (event.data instanceof ArrayBuffer) {
        // Terminal output (binary) — includes ANSI escape sequences
        const text = decoder.decode(event.data);
        appendToDisplay(text);
        return;
      }
    
      // Control message (JSON text)
      const msg = JSON.parse(event.data);
    
      switch (msg.type) {
        case 'ready':
          // Terminal is accepting input — send initial resize
          ws.send(JSON.stringify({ type: 'resize', cols: 80, rows: 24 }));
          break;
    
        case 'exit':
          console.log(`Shell exited: code ${msg.code}`);
          break;
    
        case 'error':
          console.error('Terminal error:', msg.message);
          break;
      }
    });
    
    // Send keystrokes as binary
    function sendInput(text: string): void {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(encoder.encode(text));
      }
    }

Key protocol details:

  * Set `binaryType` to `arraybuffer` before connecting.
  * Buffered output from a previous connection arrives as binary frames before the `ready` message.
  * Send keystrokes as binary (UTF-8). Send control messages (`resize`) as JSON text.
  * The PTY stays alive when a client disconnects. Reconnecting replays buffered output.



For the full protocol specification, refer to the [WebSocket protocol section](https://developers.cloudflare.com/sandbox/sdk/api/terminal/#websocket-protocol) in the API reference.

## Best practices

  * **Always use FitAddon** — Without it, terminal dimensions do not match the container and text wraps incorrectly.
  * **Handle resize events** — Call `fitAddon.fit()` on window resize so the terminal and PTY stay in sync.
  * **Clean up on unmount** — Call `addon.disconnect()` when removing the terminal from the page.
  * **Scope terminals to a user sandbox** — Use sessions for multiple terminal contexts in the same workspace. Use separate sandboxes for separate users.



## Related resources

  * [Terminal API reference](https://developers.cloudflare.com/sandbox/sdk/api/terminal/) — Method signatures, addon API, and WebSocket protocol
  * [Terminal connections](https://developers.cloudflare.com/sandbox/sdk/concepts/terminal/) — How terminal connections work
  * [Session management](https://developers.cloudflare.com/sandbox/sdk/concepts/sessions/) — How sessions work



[PreviousStream output](https://developers.cloudflare.com/sandbox/sdk/guides/streaming-output/)[NextDeploy a Sandbox application](https://developers.cloudflare.com/sandbox/sdk/guides/deploy/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/browser-terminals.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
