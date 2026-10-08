---
url: https://developers.cloudflare.com/sandbox/sdk/guides/background-processes/
title: Run background processes (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:24.069119+00:00
---

# Run background processes (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/background-processes/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /Run background processes



# Run background processes

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/background-processes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use background processesStart a background processBest practicesTroubleshooting Process exits immediately

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

This guide shows you how to start, monitor, and manage long-running background processes in the sandbox.

## When to use background processes

Use `startProcess()` instead of `exec()` when:

  * **Running web servers** \- HTTP servers, APIs, WebSocket servers
  * **Long-running services** \- Database servers, caches, message queues
  * **Development servers** \- Hot-reloading dev servers, watch modes
  * **Continuous monitoring** \- Log watchers, health checkers
  * **Parallel execution** \- Multiple services running simultaneously



Note

For **one-time commands, builds, or scripts that complete and exit** , use `exec()` instead. See the [Execute commands guide](https://developers.cloudflare.com/sandbox/sdk/guides/execute-commands/).

## Start a background process
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    
    // Start a web server
    const server = await sandbox.startProcess("python -m http.server 8000");
    
    console.log("Server started");
    console.log("Process ID:", server.id);
    console.log("PID:", server.pid);
    console.log("Status:", server.status); // 'running'
    
    // Process runs in background - your code continues
    
    
    import { getSandbox } from '@cloudflare/sandbox';
    
    const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
    
    // Start a web server
    const server = await sandbox.startProcess('python -m http.server 8000');
    
    console.log('Server started');
    console.log('Process ID:', server.id);
    console.log('PID:', server.pid);
    console.log('Status:', server.status); // 'running'
    
    // Process runs in background - your code continues

## Configure process environment

Set working directory and environment variables:
    
    
    const process = await sandbox.startProcess("node server.js", {
    	cwd: "/workspace/api",
    	env: {
    		NODE_ENV: "production",
    		PORT: "8080",
    		API_KEY: env.API_KEY,
    		DATABASE_URL: env.DATABASE_URL,
    	},
    });
    
    console.log("API server started");
    
    
    const process = await sandbox.startProcess('node server.js', {
      cwd: '/workspace/api',
      env: {
        NODE_ENV: 'production',
        PORT: '8080',
        API_KEY: env.API_KEY,
        DATABASE_URL: env.DATABASE_URL
      }
    });
    
    console.log('API server started');

## Monitor process status

List and check running processes:
    
    
    const processes = await sandbox.listProcesses();
    
    console.log(`Running ${processes.length} processes:`);
    
    for (const proc of processes) {
    	console.log(`${proc.id}: ${proc.command} (${proc.status})`);
    }
    
    // Check if specific process is running
    const isRunning = processes.some(
    	(p) => p.id === processId && p.status === "running",
    );
    
    
    const processes = await sandbox.listProcesses();
    
    console.log(`Running ${processes.length} processes:`);
    
    for (const proc of processes) {
      console.log(`${proc.id}: ${proc.command} (${proc.status})`);
    }
    
    // Check if specific process is running
    const isRunning = processes.some(p => p.id === processId && p.status === 'running');

## Wait for process readiness

Wait for a process to be ready before proceeding:
    
    
    const server = await sandbox.startProcess("node server.js");
    
    // Wait for server to respond on port 3000
    await server.waitForPort(3000);
    
    console.log("Server is ready");
    
    
    const server = await sandbox.startProcess('node server.js');
    
    // Wait for server to respond on port 3000
    await server.waitForPort(3000);
    
    console.log('Server is ready');

Or wait for specific log patterns:
    
    
    const server = await sandbox.startProcess("node server.js");
    
    // Wait for log message
    const result = await server.waitForLog("Server listening");
    console.log("Server is ready:", result.line);
    
    
    const server = await sandbox.startProcess('node server.js');
    
    // Wait for log message
    const result = await server.waitForLog('Server listening');
    console.log('Server is ready:', result.line);

## Monitor process logs

Stream logs in real-time:
    
    
    import { parseSSEStream } from "@cloudflare/sandbox";
    
    const server = await sandbox.startProcess("node server.js");
    
    // Stream logs
    const logStream = await sandbox.streamProcessLogs(server.id);
    
    for await (const log of parseSSEStream(logStream)) {
    	console.log(log.data);
    }
    
    
    import { parseSSEStream, type LogEvent } from '@cloudflare/sandbox';
    
    const server = await sandbox.startProcess('node server.js');
    
    // Stream logs
    const logStream = await sandbox.streamProcessLogs(server.id);
    
    for await (const log of parseSSEStream<LogEvent>(logStream)) {
      console.log(log.data);
    }

Or get accumulated logs:
    
    
    const logs = await sandbox.getProcessLogs(server.id);
    console.log("Logs:", logs);
    
    
    const logs = await sandbox.getProcessLogs(server.id);
    console.log('Logs:', logs);

## Stop processes

Stop background processes and their children:
    
    
    // Stop specific process (terminates entire process tree)
    await sandbox.killProcess(server.id);
    
    // Force kill if needed
    await sandbox.killProcess(server.id, "SIGKILL");
    
    // Stop all processes
    await sandbox.killAllProcesses();
    
    
    // Stop specific process (terminates entire process tree)
    await sandbox.killProcess(server.id);
    
    // Force kill if needed
    await sandbox.killProcess(server.id, 'SIGKILL');
    
    // Stop all processes
    await sandbox.killAllProcesses();

`killProcess()` terminates the specified process and all child processes it spawned. This ensures that processes running in the background do not leave orphaned child processes when terminated.

For example, if your process spawns multiple worker processes or background tasks, `killProcess()` will clean up the entire process tree:
    
    
    // This script spawns multiple child processes
    const batch = await sandbox.startProcess(
    	'bash -c "process1 & process2 & process3 & wait"',
    );
    
    // killProcess() terminates the bash process AND all three child processes
    await sandbox.killProcess(batch.id);
    
    
    // This script spawns multiple child processes
    const batch = await sandbox.startProcess(
      'bash -c "process1 & process2 & process3 & wait"'
    );
    
    // killProcess() terminates the bash process AND all three child processes
    await sandbox.killProcess(batch.id);

## Run multiple processes

Start services in sequence, waiting for dependencies:
    
    
    // Start database first
    const db = await sandbox.startProcess("redis-server");
    
    // Wait for database to be ready
    await db.waitForPort(6379, { mode: "tcp" });
    
    // Now start API server (depends on database)
    const api = await sandbox.startProcess("node api-server.js", {
    	env: { DATABASE_URL: "redis://localhost:6379" },
    });
    
    // Wait for API to be ready
    await api.waitForPort(8080, { path: "/health" });
    
    console.log("All services running");
    
    
    // Start database first
    const db = await sandbox.startProcess('redis-server');
    
    // Wait for database to be ready
    await db.waitForPort(6379, { mode: 'tcp' });
    
    // Now start API server (depends on database)
    const api = await sandbox.startProcess('node api-server.js', {
      env: { DATABASE_URL: 'redis://localhost:6379' }
    });
    
    // Wait for API to be ready
    await api.waitForPort(8080, { path: '/health' });
    
    console.log('All services running');

## Keep containers alive for long-running processes

By default, containers automatically shut down after 10 minutes of inactivity. For long-running processes that may have idle periods (like CI/CD pipelines, batch jobs, or monitoring tasks), use the [`keepAlive` option](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/#keepalive):
    
    
    import { getSandbox, parseSSEStream } from "@cloudflare/sandbox";
    
    export { Sandbox } from "@cloudflare/sandbox";
    
    export default {
    	async fetch(request, env) {
    		// Enable keepAlive for long-running processes
    		const sandbox = getSandbox(env.Sandbox, "build-job-123", {
    			keepAlive: true,
    		});
    
    		try {
    			// Start a long-running build process
    			const build = await sandbox.startProcess("npm run build:production");
    
    			// Monitor progress
    			const logs = await sandbox.streamProcessLogs(build.id);
    
    			// Process can run indefinitely without container shutdown
    			for await (const log of parseSSEStream(logs)) {
    				console.log(log.data);
    				if (log.data.includes("Build complete")) {
    					break;
    				}
    			}
    
    			return new Response("Build completed");
    		} finally {
    			// Important: Must explicitly destroy when done
    			await sandbox.destroy();
    		}
    	},
    };
    
    
    import { getSandbox, parseSSEStream, type LogEvent } from '@cloudflare/sandbox';
    
    export { Sandbox } from '@cloudflare/sandbox';
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        // Enable keepAlive for long-running processes
        const sandbox = getSandbox(env.Sandbox, 'build-job-123', {
          keepAlive: true
        });
    
        try {
          // Start a long-running build process
          const build = await sandbox.startProcess('npm run build:production');
    
          // Monitor progress
          const logs = await sandbox.streamProcessLogs(build.id);
    
          // Process can run indefinitely without container shutdown
          for await (const log of parseSSEStream<LogEvent>(logs)) {
            console.log(log.data);
            if (log.data.includes('Build complete')) {
              break;
            }
          }
    
          return new Response('Build completed');
        } finally {
          // Important: Must explicitly destroy when done
          await sandbox.destroy();
        }
      }
    };

Always destroy with keepAlive

When using `keepAlive: true`, containers will not automatically timeout. You **must** call `sandbox.destroy()` when finished to prevent containers running indefinitely and counting toward your account limits.

## Best practices

  * **Wait for readiness** \- Use `waitForPort()` or `waitForLog()` to detect when services are ready
  * **Clean up** \- Always stop processes when done
  * **Handle failures** \- Monitor logs for errors and restart if needed
  * **Use try/finally** \- Ensure cleanup happens even on errors
  * **Use`keepAlive` for long-running tasks** \- Prevent container shutdown during processes with idle periods



## Troubleshooting

### Process exits immediately

Check logs to see why:
    
    
    const process = await sandbox.startProcess("node server.js");
    await new Promise((resolve) => setTimeout(resolve, 1000));
    
    const processes = await sandbox.listProcesses();
    if (!processes.find((p) => p.id === process.id)) {
    	const logs = await sandbox.getProcessLogs(process.id);
    	console.error("Process exited:", logs);
    }
    
    
    const process = await sandbox.startProcess('node server.js');
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    const processes = await sandbox.listProcesses();
    if (!processes.find(p => p.id === process.id)) {
      const logs = await sandbox.getProcessLogs(process.id);
      console.error('Process exited:', logs);
    }

### Port already in use

Kill existing processes before starting:
    
    
    await sandbox.killAllProcesses();
    const server = await sandbox.startProcess("node server.js");
    
    
    await sandbox.killAllProcesses();
    const server = await sandbox.startProcess('node server.js');

## Related resources

  * [Commands API reference](https://developers.cloudflare.com/sandbox/sdk/api/commands/) \- Complete process management API
  * [Sandbox options configuration](https://developers.cloudflare.com/sandbox/sdk/configuration/sandbox-options/) \- Configure `keepAlive` and other options
  * [Lifecycle API](https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/) \- Create and manage sandboxes
  * [Sessions API reference](https://developers.cloudflare.com/sandbox/sdk/api/sessions/) \- Create isolated execution contexts
  * [Execute commands guide](https://developers.cloudflare.com/sandbox/sdk/guides/execute-commands/) \- One-time command execution
  * [Expose services guide](https://developers.cloudflare.com/sandbox/sdk/guides/expose-services/) \- Make processes accessible
  * [Streaming output guide](https://developers.cloudflare.com/sandbox/sdk/guides/streaming-output/) \- Monitor process output



[PreviousManage files](https://developers.cloudflare.com/sandbox/sdk/guides/manage-files/)[NextWatch filesystem changes](https://developers.cloudflare.com/sandbox/sdk/guides/file-watching/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/background-processes.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
