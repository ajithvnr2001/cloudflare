---
url: https://developers.cloudflare.com/sandbox/sdk/api/sessions/
title: Sessions (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:22.035942+00:00
---

# Sessions (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/api/sessions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[API reference](https://developers.cloudflare.com/sandbox/sdk/api/)
  5. /Sessions



# Sessions

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/api/sessions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethods createSession()

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Create shell sessions within a sandbox. Each session maintains its own shell state, environment variables, and working directory, while sharing the sandbox filesystem and process space. For more information, refer to [Session management](https://developers.cloudflare.com/sandbox/sdk/concepts/sessions/).

Note

By default, for backwards compatibility, every sandbox has a default session that maintains shell state. It is recommended to set `enableDefaultSession` to `false` on `getSandbox()` so operations without an explicit `sessionId` run in isolation. Create additional sessions for separate workflows inside the same user workspace, such as development and runtime processes using the `createSession()` method. Use separate sandboxes for separate users. For sandbox-level operations like creating containers or destroying the entire sandbox, refer to the [Lifecycle API](https://developers.cloudflare.com/sandbox/sdk/api/lifecycle/).

## Methods

### `createSession()`

Create a new shell session.
    
    
    const session = await sandbox.createSession(options?: SessionOptions): Promise<ExecutionSession>

**Parameters** :

  * `options` (optional): 
    * `id` \- Custom session ID (auto-generated if not provided)
    * `env` \- Environment variables for this session: `Record<string, string | undefined>`
    * `cwd` \- Working directory (default: `"/workspace"`)
    * `commandTimeoutMs` \- Maximum time in milliseconds that any command in this session can run before timing out. Individual commands can override this with the `timeout` option on `exec()`.



**Returns** : `Promise<ExecutionSession>` with all sandbox methods bound to this session
    
    
    // Separate workflow environments
    const prodSession = await sandbox.createSession({
    	id: "prod",
    	env: { NODE_ENV: "production", API_URL: "https://api.example.com" },
    	cwd: "/workspace/prod",
    });
    
    const testSession = await sandbox.createSession({
    	id: "test",
    	env: {
    		NODE_ENV: "test",
    		API_URL: "http://localhost:3000",
    		DEBUG_MODE: undefined, // Skipped, not set in this session
    	},
    	cwd: "/workspace/test",
    });
    
    // Run in parallel
    const [prodResult, testResult] = await Promise.all([
    	prodSession.exec("npm run build"),
    	testSession.exec("npm run build"),
    ]);
    
    // Session with a default command timeout
    const session = await sandbox.createSession({
    	commandTimeoutMs: 5000, // 5s timeout for all commands
    });
    
    await session.exec("sleep 10"); // Times out after 5s
    
    // Per-command timeout overrides session-level timeout
    await session.exec("sleep 10", { timeout: 3000 }); // Times out after 3s
    
    
    // Separate workflow environments
    const prodSession = await sandbox.createSession({
      id: 'prod',
      env: { NODE_ENV: 'production', API_URL: 'https://api.example.com' },
      cwd: '/workspace/prod'
    });
    
    const testSession = await sandbox.createSession({
      id: 'test',
      env: {
        NODE_ENV: 'test',
        API_URL: 'http://localhost:3000',
        DEBUG_MODE: undefined // Skipped, not set in this session
      },
      cwd: '/workspace/test'
    });
    
    // Run in parallel
    const [prodResult, testResult] = await Promise.all([
      prodSession.exec('npm run build'),
      testSession.exec('npm run build')
    ]);
    
    // Session with a default command timeout
    const session = await sandbox.createSession({
      commandTimeoutMs: 5000 // 5s timeout for all commands
    });
    
    await session.exec('sleep 10'); // Times out after 5s
    
    // Per-command timeout overrides session-level timeout
    await session.exec('sleep 10', { timeout: 3000 }); // Times out after 3s

### `getSession()`

Retrieve an existing session by ID.
    
    
    const session = await sandbox.getSession(sessionId: string): Promise<ExecutionSession>

**Parameters** :

  * `sessionId` \- ID of an existing session



**Returns** : `Promise<ExecutionSession>` bound to the specified session
    
    
    // First request - create a task-specific session
    const session = await sandbox.createSession({ id: "build" });
    await session.exec("git clone https://github.com/user/repo.git");
    await session.exec("cd repo && npm install");
    
    // Second request - resume session (environment and cwd preserved)
    const session = await sandbox.getSession("build");
    const result = await session.exec("cd repo && npm run build");
    
    
    // First request - create a task-specific session
    const session = await sandbox.createSession({ id: 'build' });
    await session.exec('git clone https://github.com/user/repo.git');
    await session.exec('cd repo && npm install');
    
    // Second request - resume session (environment and cwd preserved)
    const session = await sandbox.getSession('build');
    const result = await session.exec('cd repo && npm run build');

* * *

### `deleteSession()`

Delete a session and clean up its resources.
    
    
    const result = await sandbox.deleteSession(sessionId: string): Promise<SessionDeleteResult>

**Parameters** :

  * `sessionId` \- ID of the session to delete (cannot be `"default"`)



**Returns** : `Promise<SessionDeleteResult>` containing:

  * `success` \- Whether deletion succeeded
  * `sessionId` \- ID of the deleted session
  * `timestamp` \- Deletion timestamp


    
    
    // Create a temporary session for a specific task
    const tempSession = await sandbox.createSession({ id: "temp-task" });
    
    try {
    	await tempSession.exec("npm run heavy-task");
    } finally {
    	// Clean up the session when done
    	await sandbox.deleteSession("temp-task");
    }
    
    
    // Create a temporary session for a specific task
    const tempSession = await sandbox.createSession({ id: 'temp-task' });
    
    try {
      await tempSession.exec('npm run heavy-task');
    } finally {
      // Clean up the session when done
      await sandbox.deleteSession('temp-task');
    }

Caution

Deleting a session immediately terminates all running commands. The default session cannot be deleted.

* * *

### `setEnvVars()`

Set environment variables in the sandbox.
    
    
    await sandbox.setEnvVars(envVars: Record<string, string | undefined>): Promise<void>

**Parameters** :

  * `envVars` \- Key-value pairs of environment variables to set or unset 
    * `string` values: Set the environment variable
    * `undefined` or `null` values: Unset the environment variable



Caution

Call `setEnvVars()` **before** any other sandbox operations to ensure environment variables are available from the start.
    
    
    const sandbox = getSandbox(env.Sandbox, "user-123");
    
    // Set environment variables first
    await sandbox.setEnvVars({
    	API_KEY: env.OPENAI_API_KEY,
    	DATABASE_URL: env.DATABASE_URL,
    	NODE_ENV: "production",
    	OLD_TOKEN: undefined, // Unsets OLD_TOKEN if previously set
    });
    
    // Now commands can access these variables
    await sandbox.exec("python script.py");
    
    
    const sandbox = getSandbox(env.Sandbox, 'user-123');
    
    // Set environment variables first
    await sandbox.setEnvVars({
      API_KEY: env.OPENAI_API_KEY,
      DATABASE_URL: env.DATABASE_URL,
      NODE_ENV: 'production',
      OLD_TOKEN: undefined // Unsets OLD_TOKEN if previously set
    });
    
    // Now commands can access these variables
    await sandbox.exec('python script.py');

* * *

## ExecutionSession methods

The `ExecutionSession` object has all sandbox methods bound to the specific session:

Category | Methods  
---|---  
**Commands** | [`exec()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#exec), [`execStream()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#execstream)  
**Processes** | [`startProcess()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#startprocess), [`listProcesses()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#listprocesses), [`killProcess()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#killprocess), [`killAllProcesses()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#killallprocesses), [`getProcessLogs()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#getprocesslogs), [`streamProcessLogs()`](https://developers.cloudflare.com/sandbox/sdk/api/commands/#streamprocesslogs)  
**Files** | [`writeFile()`](https://developers.cloudflare.com/sandbox/sdk/api/files/#writefile), [`readFile()`](https://developers.cloudflare.com/sandbox/sdk/api/files/#readfile), [`mkdir()`](https://developers.cloudflare.com/sandbox/sdk/api/files/#mkdir), [`deleteFile()`](https://developers.cloudflare.com/sandbox/sdk/api/files/#deletefile), [`renameFile()`](https://developers.cloudflare.com/sandbox/sdk/api/files/#renamefile), [`moveFile()`](https://developers.cloudflare.com/sandbox/sdk/api/files/#movefile), [`gitCheckout()`](https://developers.cloudflare.com/sandbox/sdk/api/files/#gitcheckout)  
**Environment** | [`setEnvVars()`](https://developers.cloudflare.com/sandbox/sdk/api/sessions/#setenvvars)  
**Terminal** | [`terminal()`](https://developers.cloudflare.com/sandbox/sdk/api/terminal/#terminal)  
**Code Interpreter** | [`createCodeContext()`](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/#createcodecontext), [`runCode()`](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/#runcode), [`listCodeContexts()`](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/#listcodecontexts), [`deleteCodeContext()`](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/#deletecodecontext)  
  
## Related resources

  * [Session management concept](https://developers.cloudflare.com/sandbox/sdk/concepts/sessions/) \- How sessions work
  * [Commands API](https://developers.cloudflare.com/sandbox/sdk/api/commands/) \- Execute commands



[PreviousPorts](https://developers.cloudflare.com/sandbox/sdk/api/ports/)[NextTunnels](https://developers.cloudflare.com/sandbox/sdk/api/tunnels/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/api/sessions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
