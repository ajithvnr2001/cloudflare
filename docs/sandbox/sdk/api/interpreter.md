---
url: https://developers.cloudflare.com/sandbox/sdk/api/interpreter/
title: Code interpreter (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:21.676013+00:00
---

# Code interpreter (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/api/interpreter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[API reference](https://developers.cloudflare.com/sandbox/sdk/api/)
  5. /Code interpreter



# Code interpreter

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethods createCodeContext() runCode() deleteCodeContext()Rich Output Formats

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Execute Python, JavaScript, and TypeScript code with support for data visualizations, tables, and rich output formats. Contexts maintain state (variables, imports, functions) across executions.

## Methods

### `createCodeContext()`

Create a persistent execution context for running code.
    
    
    const context = await sandbox.createCodeContext(options?: CreateContextOptions): Promise<CodeContext>

**Parameters** :

  * `options` (optional): 
    * `language` \- `"python" | "javascript" | "typescript"` (default: `"python"`)
    * `cwd` \- Working directory (default: `"/workspace"`)
    * `envVars` \- Environment variables
    * `timeout` \- Request timeout in milliseconds (default: 30000)



**Returns** : `Promise<CodeContext>` with `id`, `language`, `cwd`, `createdAt`, `lastUsed`
    
    
    const ctx = await sandbox.createCodeContext({
    	language: "python",
    	envVars: { API_KEY: env.API_KEY },
    });
    
    
    const ctx = await sandbox.createCodeContext({
      language: 'python',
      envVars: { API_KEY: env.API_KEY }
    });

### `runCode()`

Execute code in a context and return the complete result.
    
    
    const result = await sandbox.runCode(code: string, options?: RunCodeOptions): Promise<ExecutionResult>

**Parameters** :

  * `code` \- The code to execute (required)
  * `options` (optional): 
    * `context` \- Context to run in (recommended - see below)
    * `language` \- `"python" | "javascript" | "typescript"` (default: `"python"`)
    * `timeout` \- Execution timeout in milliseconds (default: 60000)
    * `onStdout`, `onStderr`, `onResult`, `onError` \- Streaming callbacks



**Returns** : `Promise<ExecutionResult>` with:

  * `code` \- The executed code
  * `logs` \- `stdout` and `stderr` arrays
  * `results` \- Array of rich outputs (see Rich Output Formats)
  * `error` \- Execution error if any
  * `executionCount` \- Execution counter



**Recommended usage - create explicit context** :
    
    
    const ctx = await sandbox.createCodeContext({ language: "python" });
    
    await sandbox.runCode("import math; radius = 5", { context: ctx });
    const result = await sandbox.runCode("math.pi * radius ** 2", { context: ctx });
    
    console.log(result.results[0].text); // "78.53981633974483"
    
    
    const ctx = await sandbox.createCodeContext({ language: 'python' });
    
    await sandbox.runCode('import math; radius = 5', { context: ctx });
    const result = await sandbox.runCode('math.pi * radius ** 2', { context: ctx });
    
    console.log(result.results[0].text); // "78.53981633974483"

Default context behavior

If no `context` is provided, a default context is automatically created/reused for the specified `language`. While convenient for quick tests, **explicitly creating contexts is recommended** for production use to maintain predictable state.
    
    
    const result = await sandbox.runCode(
    	`
    data = [1, 2, 3, 4, 5]
    print(f"Sum: {sum(data)}")
    sum(data)
    `,
    	{ language: "python" },
    );
    
    console.log(result.logs.stdout); // ["Sum: 15"]
    console.log(result.results[0].text); // "15"
    
    
    const result = await sandbox.runCode(`
    data = [1, 2, 3, 4, 5]
    print(f"Sum: {sum(data)}")
    sum(data)
    `, { language: 'python' });
    
    console.log(result.logs.stdout); // ["Sum: 15"]
    console.log(result.results[0].text); // "15"

**Error handling** :
    
    
    const result = await sandbox.runCode("x = 1 / 0", { language: "python" });
    
    if (result.error) {
    	console.error(result.error.name); // "ZeroDivisionError"
    	console.error(result.error.value); // "division by zero"
    	console.error(result.error.traceback); // Stack trace array
    }
    
    
    const result = await sandbox.runCode('x = 1 / 0', { language: 'python' });
    
    if (result.error) {
      console.error(result.error.name);      // "ZeroDivisionError"
      console.error(result.error.value);     // "division by zero"
      console.error(result.error.traceback); // Stack trace array
    }

**JavaScript and TypeScript features** :

JavaScript and TypeScript code execution supports top-level `await` and persistent variables across executions within the same context.
    
    
    const ctx = await sandbox.createCodeContext({ language: "javascript" });
    
    // Execution 1: Fetch data with top-level await
    await sandbox.runCode(
    	`
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    `,
    	{ context: ctx },
    );
    
    // Execution 2: Use the data from previous execution
    const result = await sandbox.runCode("console.log(data)", { context: ctx });
    console.log(result.logs.stdout); // Data persists across executions
    
    
    const ctx = await sandbox.createCodeContext({ language: 'javascript' });
    
    // Execution 1: Fetch data with top-level await
    await sandbox.runCode(`
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    `, { context: ctx });
    
    // Execution 2: Use the data from previous execution
    const result = await sandbox.runCode('console.log(data)', { context: ctx });
    console.log(result.logs.stdout); // Data persists across executions

Variables declared with `const`, `let`, or `var` persist across executions, enabling multi-step workflows:
    
    
    const ctx = await sandbox.createCodeContext({ language: "javascript" });
    
    await sandbox.runCode("const x = 10", { context: ctx });
    await sandbox.runCode("let y = 20", { context: ctx });
    const result = await sandbox.runCode("x + y", { context: ctx });
    
    console.log(result.results[0].text); // "30"
    
    
    const ctx = await sandbox.createCodeContext({ language: 'javascript' });
    
    await sandbox.runCode('const x = 10', { context: ctx });
    await sandbox.runCode('let y = 20', { context: ctx });
    const result = await sandbox.runCode('x + y', { context: ctx });
    
    console.log(result.results[0].text); // "30"

### `listCodeContexts()`

List all active code execution contexts.
    
    
    const contexts = await sandbox.listCodeContexts(): Promise<CodeContext[]>
    
    
    const contexts = await sandbox.listCodeContexts();
    console.log(`Found ${contexts.length} contexts`);
    
    
    const contexts = await sandbox.listCodeContexts();
    console.log(`Found ${contexts.length} contexts`);

### `deleteCodeContext()`

Delete a code execution context and free its resources.
    
    
    await sandbox.deleteCodeContext(contextId: string): Promise<void>
    
    
    const ctx = await sandbox.createCodeContext({ language: "python" });
    await sandbox.runCode('print("Hello")', { context: ctx });
    await sandbox.deleteCodeContext(ctx.id);
    
    
    const ctx = await sandbox.createCodeContext({ language: 'python' });
    await sandbox.runCode('print("Hello")', { context: ctx });
    await sandbox.deleteCodeContext(ctx.id);

## Rich Output Formats

Results include: `text`, `html`, `png`, `jpeg`, `svg`, `latex`, `markdown`, `json`, `chart`, `data`

**Charts (matplotlib)** :
    
    
    const result = await sandbox.runCode(
    	`
    import matplotlib.pyplot as plt
    import numpy as np
    
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.show()
    `,
    	{ language: "python" },
    );
    
    if (result.results[0]?.png) {
    	const imageBuffer = Buffer.from(result.results[0].png, "base64");
    	return new Response(imageBuffer, {
    		headers: { "Content-Type": "image/png" },
    	});
    }
    
    
    const result = await sandbox.runCode(`
    import matplotlib.pyplot as plt
    import numpy as np
    
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.show()
    `, { language: 'python' });
    
    if (result.results[0]?.png) {
      const imageBuffer = Buffer.from(result.results[0].png, 'base64');
      return new Response(imageBuffer, {
        headers: { 'Content-Type': 'image/png' }
      });
    }

**Tables (pandas)** :
    
    
    const result = await sandbox.runCode(
    	`
    import pandas as pd
    df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    df
    `,
    	{ language: "python" },
    );
    
    if (result.results[0]?.html) {
    	return new Response(result.results[0].html, {
    		headers: { "Content-Type": "text/html" },
    	});
    }
    
    
    const result = await sandbox.runCode(`
    import pandas as pd
    df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    df
    `, { language: 'python' });
    
    if (result.results[0]?.html) {
      return new Response(result.results[0].html, {
        headers: { 'Content-Type': 'text/html' }
      });
    }

## Related resources

  * [Build an AI Code Executor](https://developers.cloudflare.com/sandbox/sdk/tutorials/ai-code-executor/) \- Complete tutorial
  * [Commands API](https://developers.cloudflare.com/sandbox/sdk/api/commands/) \- Lower-level command execution
  * [Files API](https://developers.cloudflare.com/sandbox/sdk/api/files/) \- File operations



[PreviousFiles](https://developers.cloudflare.com/sandbox/sdk/api/files/)[NextFile watching](https://developers.cloudflare.com/sandbox/sdk/api/file-watching/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/api/interpreter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
