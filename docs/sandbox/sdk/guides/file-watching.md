---
url: https://developers.cloudflare.com/sandbox/sdk/guides/file-watching/
title: Watch filesystem changes (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:25.236620+00:00
---

# Watch filesystem changes (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/file-watching/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /Watch filesystem changes



# Watch filesystem changes

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/file-watching/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic file watchingFilter by file typeExclude directoriesBuild responsive development tools Auto-rebuild on changes Auto-run tests on change Incremental indexingAdvanced patterns Process events with a helper function Debounced file operations Watch with non-recursive modeStop a watch Use an AbortController Break out of the loopBest practices Use server-side filtering Handle errors in event processing Ensure directories exist before watchingTroubleshooting High CPU usage Path not found errorsRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

This guide shows you how to monitor filesystem changes in real-time using the Sandbox SDK's file watching API. File watching is useful for building development tools, automated workflows, and applications that react to file changes as they happen.

The `watch()` method returns an SSE (Server-Sent Events) stream that you consume with `parseSSEStream()`. Each event in the stream describes a filesystem change.

## Basic file watching

Start by watching a directory for any changes:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    		console.log(`Is directory: ${event.isDirectory}`);
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    		console.log(`Is directory: ${event.isDirectory}`);
    	}
    }

The stream emits four lifecycle event types:

  * **`watching`** — Watch established, includes the `watchId`
  * **`event`** — A filesystem change occurred
  * **`error`** — The watch encountered an error
  * **`stopped`** — The watch was stopped



Filesystem change events (`event.eventType`) include:

  * **`create`** — File or directory was created
  * **`modify`** — File content changed
  * **`delete`** — File or directory was removed
  * **`move_from`** / **`move_to`** — File or directory was moved or renamed
  * **`attrib`** — File attributes changed (permissions, timestamps)



## Filter by file type

Use `include` patterns to watch only specific file types:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    // Only watch TypeScript and JavaScript files
    const stream = await sandbox.watch("/workspace/src", {
    	include: ["*.ts", "*.tsx", "*.js", "*.jsx"],
    });
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    // Only watch TypeScript and JavaScript files
    const stream = await sandbox.watch("/workspace/src", {
    	include: ["*.ts", "*.tsx", "*.js", "*.jsx"],
    });
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    	}
    }

Common include patterns:

  * `*.ts` — TypeScript files
  * `*.js` — JavaScript files
  * `*.json` — JSON configuration files
  * `*.md` — Markdown documentation
  * `package*.json` — Package files specifically



## Exclude directories

Use `exclude` patterns to skip certain directories or files:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace", {
    	exclude: ["node_modules", "dist", "*.log", ".git", "*.tmp"],
    });
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		console.log(`Change detected: ${event.path}`);
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace", {
    	exclude: ["node_modules", "dist", "*.log", ".git", "*.tmp"],
    });
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		console.log(`Change detected: ${event.path}`);
    	}
    }

Default exclusions

The following patterns are excluded by default: `.git`, `node_modules`, `.DS_Store`. You can override this by providing your own `exclude` array.

## Build responsive development tools

### Auto-rebuild on changes

Trigger builds automatically when source files are modified:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src", {
    	include: ["*.ts", "*.tsx"],
    });
    
    let buildInProgress = false;
    
    for await (const event of parseSSEStream(stream)) {
    	if (
    		event.type === "event" &&
    		event.eventType === "modify" &&
    		!buildInProgress
    	) {
    		buildInProgress = true;
    		console.log(`File changed: ${event.path}, rebuilding...`);
    
    		try {
    			const result = await sandbox.exec("npm run build");
    			if (result.success) {
    				console.log("Build completed successfully");
    			} else {
    				console.error("Build failed:", result.stderr);
    			}
    		} catch (error) {
    			console.error("Build error:", error);
    		} finally {
    			buildInProgress = false;
    		}
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src", {
    	include: ["*.ts", "*.tsx"],
    });
    
    let buildInProgress = false;
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (
    		event.type === "event" &&
    		event.eventType === "modify" &&
    		!buildInProgress
    	) {
    		buildInProgress = true;
    		console.log(`File changed: ${event.path}, rebuilding...`);
    
    		try {
    			const result = await sandbox.exec("npm run build");
    			if (result.success) {
    				console.log("Build completed successfully");
    			} else {
    				console.error("Build failed:", result.stderr);
    			}
    		} catch (error) {
    			console.error("Build error:", error);
    		} finally {
    			buildInProgress = false;
    		}
    	}
    }

### Auto-run tests on change

Re-run tests when test files are modified:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/tests", {
    	include: ["*.test.ts", "*.spec.ts"],
    });
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event" && event.eventType === "modify") {
    		console.log(`Test file changed: ${event.path}`);
    		const result = await sandbox.exec(`npm test -- ${event.path}`);
    		console.log(result.success ? "Tests passed" : "Tests failed");
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/tests", {
    	include: ["*.test.ts", "*.spec.ts"],
    });
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event" && event.eventType === "modify") {
    		console.log(`Test file changed: ${event.path}`);
    		const result = await sandbox.exec(`npm test -- ${event.path}`);
    		console.log(result.success ? "Tests passed" : "Tests failed");
    	}
    }

### Incremental indexing

Re-index only changed files instead of rescanning an entire directory tree:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/docs", {
    	include: ["*.md", "*.mdx"],
    });
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		switch (event.eventType) {
    			case "create":
    			case "modify":
    				console.log(`Indexing ${event.path}...`);
    				await indexFile(event.path);
    				break;
    			case "delete":
    				console.log(`Removing ${event.path} from index...`);
    				await removeFromIndex(event.path);
    				break;
    		}
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/docs", {
    	include: ["*.md", "*.mdx"],
    });
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		switch (event.eventType) {
    			case "create":
    			case "modify":
    				console.log(`Indexing ${event.path}...`);
    				await indexFile(event.path);
    				break;
    			case "delete":
    				console.log(`Removing ${event.path} from index...`);
    				await removeFromIndex(event.path);
    				break;
    		}
    	}
    }

## Advanced patterns

### Process events with a helper function

Extract event processing into a reusable function that handles stream lifecycle:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    async function watchFiles(sandbox, path, options, handler) {
    	const stream = await sandbox.watch(path, options);
    
    	for await (const event of parseSSEStream(stream)) {
    		switch (event.type) {
    			case "watching":
    				console.log(`Watching ${event.path}`);
    				break;
    			case "event":
    				await handler(event.eventType, event.path, event.isDirectory);
    				break;
    			case "error":
    				console.error(`Watch error: ${event.error}`);
    				break;
    			case "stopped":
    				console.log(`Watch stopped: ${event.reason}`);
    				return;
    		}
    	}
    }
    
    // Usage
    await watchFiles(
    	sandbox,
    	"/workspace/src",
    	{ include: ["*.ts"] },
    	async (eventType, filePath) => {
    		console.log(`${eventType}: ${filePath}`);
    	},
    );
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    async function watchFiles(
    	sandbox: any,
    	path: string,
    	options: { include?: string[]; exclude?: string[] },
    	handler: (
    		eventType: string,
    		filePath: string,
    		isDirectory: boolean,
    	) => Promise<void>,
    ) {
    	const stream = await sandbox.watch(path, options);
    
    	for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    		switch (event.type) {
    			case "watching":
    				console.log(`Watching ${event.path}`);
    				break;
    			case "event":
    				await handler(event.eventType, event.path, event.isDirectory);
    				break;
    			case "error":
    				console.error(`Watch error: ${event.error}`);
    				break;
    			case "stopped":
    				console.log(`Watch stopped: ${event.reason}`);
    				return;
    		}
    	}
    }
    
    // Usage
    await watchFiles(
    	sandbox,
    	"/workspace/src",
    	{ include: ["*.ts"] },
    	async (eventType, filePath) => {
    		console.log(`${eventType}: ${filePath}`);
    	},
    );

### Debounced file operations

Avoid excessive operations by collecting changes before processing:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    const changedFiles = new Set();
    let debounceTimeout = null;
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		changedFiles.add(event.path);
    
    		if (debounceTimeout) {
    			clearTimeout(debounceTimeout);
    		}
    
    		debounceTimeout = setTimeout(async () => {
    			console.log(`Processing ${changedFiles.size} changed files...`);
    			for (const filePath of changedFiles) {
    				await processFile(filePath);
    			}
    			changedFiles.clear();
    			debounceTimeout = null;
    		}, 1000);
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    const changedFiles = new Set<string>();
    let debounceTimeout: ReturnType<typeof setTimeout> | null = null;
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		changedFiles.add(event.path);
    
    		if (debounceTimeout) {
    			clearTimeout(debounceTimeout);
    		}
    
    		debounceTimeout = setTimeout(async () => {
    			console.log(`Processing ${changedFiles.size} changed files...`);
    			for (const filePath of changedFiles) {
    				await processFile(filePath);
    			}
    			changedFiles.clear();
    			debounceTimeout = null;
    		}, 1000);
    	}
    }

### Watch with non-recursive mode

Watch only the top level of a directory, without descending into subdirectories:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    // Only watch root-level config files
    const stream = await sandbox.watch("/workspace", {
    	include: ["package.json", "tsconfig.json", "vite.config.ts"],
    	recursive: false,
    });
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		console.log("Configuration changed, rebuilding project...");
    		await sandbox.exec("npm run build");
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    // Only watch root-level config files
    const stream = await sandbox.watch("/workspace", {
    	include: ["package.json", "tsconfig.json", "vite.config.ts"],
    	recursive: false,
    });
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		console.log("Configuration changed, rebuilding project...");
    		await sandbox.exec("npm run build");
    	}
    }

## Stop a watch

The stream ends naturally when the container sleeps or shuts down. There are two ways to stop a watch early:

### Use an AbortController

Pass an `AbortSignal` to `parseSSEStream`. Aborting the signal cancels the stream reader, which propagates cleanup to the server. This is the recommended approach when you need to cancel the watch from outside the consuming loop:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    const controller = new AbortController();
    
    // Cancel after 60 seconds
    setTimeout(() => controller.abort(), 60_000);
    
    for await (const event of parseSSEStream(stream, controller.signal)) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    	}
    }
    
    console.log("Watch stopped");
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    const controller = new AbortController();
    
    // Cancel after 60 seconds
    setTimeout(() => controller.abort(), 60_000);
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(
    	stream,
    	controller.signal,
    )) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    	}
    }
    
    console.log("Watch stopped");

### Break out of the loop

Breaking out of the `for await` loop also cancels the stream:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    let eventCount = 0;
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    		eventCount++;
    
    		// Stop after 100 events
    		if (eventCount >= 100) {
    			break; // Breaking out of the loop cancels the stream
    		}
    	}
    }
    
    console.log("Watch stopped");
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    let eventCount = 0;
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		console.log(`${event.eventType}: ${event.path}`);
    		eventCount++;
    
    		// Stop after 100 events
    		if (eventCount >= 100) {
    			break; // Breaking out of the loop cancels the stream
    		}
    	}
    }
    
    console.log("Watch stopped");

## Best practices

### Use server-side filtering

Filter with `include` or `exclude` patterns rather than filtering events in JavaScript. Server-side filtering happens at the inotify level, which reduces the number of events sent over the network.

Note

`include` and `exclude` are mutually exclusive. Use one or the other, not both. If you need to watch specific file types while ignoring certain directories, use `include` patterns that match the files you want.
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    // Efficient: filtering happens at the inotify level
    const stream = await sandbox.watch("/workspace/src", {
    	include: ["*.ts"],
    });
    
    // Less efficient: all events are sent and then filtered in JavaScript
    const stream2 = await sandbox.watch("/workspace/src");
    for await (const event of parseSSEStream(stream2)) {
    	if (event.type === "event") {
    		if (!event.path.endsWith(".ts")) continue;
    		// Handle event
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    // Efficient: filtering happens at the inotify level
    const stream = await sandbox.watch("/workspace/src", {
    	include: ["*.ts"],
    });
    
    // Less efficient: all events are sent and then filtered in JavaScript
    const stream2 = await sandbox.watch("/workspace/src");
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream2)) {
    	if (event.type === "event") {
    		if (!event.path.endsWith(".ts")) continue;
    		// Handle event
    	}
    }

### Handle errors in event processing

Errors in your event handler do not stop the watch stream. Wrap handler logic in `try...catch` to prevent unhandled exceptions:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    
    for await (const event of parseSSEStream(stream)) {
    	if (event.type === "event") {
    		try {
    			await handleFileChange(event.eventType, event.path);
    		} catch (error) {
    			console.error(
    				`Failed to handle ${event.eventType} for ${event.path}:`,
    				error,
    			);
    			// Continue processing events
    		}
    	}
    
    	if (event.type === "error") {
    		console.error("Watch error:", event.error);
    	}
    }
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    import type { FileWatchSSEEvent } from "@cloudflare/sandbox";
    
    const stream = await sandbox.watch("/workspace/src");
    
    for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
    	if (event.type === "event") {
    		try {
    			await handleFileChange(event.eventType, event.path);
    		} catch (error) {
    			console.error(
    				`Failed to handle ${event.eventType} for ${event.path}:`,
    				error,
    			);
    			// Continue processing events
    		}
    	}
    
    	if (event.type === "error") {
    		console.error("Watch error:", event.error);
    	}
    }

### Ensure directories exist before watching

Watching a non-existent path returns an error. Verify the path exists before starting a watch:
    
    
    const watchPath = "/workspace/src";
    const result = await sandbox.exists(watchPath);
    
    if (!result.exists) {
    	await sandbox.mkdir(watchPath, { recursive: true });
    }
    
    const stream = await sandbox.watch(watchPath, {
    	include: ["*.ts"],
    });
    
    
    const watchPath = "/workspace/src";
    const result = await sandbox.exists(watchPath);
    
    if (!result.exists) {
    	await sandbox.mkdir(watchPath, { recursive: true });
    }
    
    const stream = await sandbox.watch(watchPath, {
    	include: ["*.ts"],
    });

## Troubleshooting

### High CPU usage

If watching large directories causes performance issues:

  1. Use specific `include` patterns instead of watching everything
  2. Exclude large directories like `node_modules` and `dist`
  3. Watch specific subdirectories instead of the entire project
  4. Use `recursive: false` for shallow monitoring



### Path not found errors

All paths must exist and resolve to within `/workspace`. Relative paths are resolved from `/workspace`.

Container lifecycle

File watchers are automatically stopped when the sandbox sleeps or shuts down. If the sandbox wakes up, you must re-establish watches in your application logic.

## Related resources

  * [File Watching API reference](https://developers.cloudflare.com/sandbox/sdk/api/file-watching/) — Complete API documentation and types
  * [Manage files guide](https://developers.cloudflare.com/sandbox/sdk/guides/manage-files/) — File operations
  * [Background processes guide](https://developers.cloudflare.com/sandbox/sdk/guides/background-processes/) — Long-running processes
  * [Stream output guide](https://developers.cloudflare.com/sandbox/sdk/guides/streaming-output/) — Real-time output handling



[PreviousRun background processes](https://developers.cloudflare.com/sandbox/sdk/guides/background-processes/)[NextExpose services](https://developers.cloudflare.com/sandbox/sdk/guides/expose-services/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/file-watching.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
