---
url: https://developers.cloudflare.com/sandbox/sdk/guides/code-execution/
title: Use code interpreter (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:24.591490+00:00
---

# Use code interpreter (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/code-execution/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /Use code interpreter



# Use code interpreter

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/code-execution/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhen to use code interpreterCreate an execution context

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

This guide shows you how to execute Python and JavaScript code with rich outputs using the Code Interpreter API.

## When to use code interpreter

Use the Code Interpreter API for **simple, direct code execution** with minimal setup:

  * **Quick code execution** \- Run Python/JS code without environment setup
  * **Rich outputs** \- Get charts, tables, images, HTML automatically
  * **AI-generated code** \- Execute LLM-generated code with structured results
  * **Persistent state** \- Variables preserved between executions in the same context



Use `exec()` for **advanced or custom workflows** :

  * **System operations** \- Install packages, manage files, run builds
  * **Custom environments** \- Configure specific versions, dependencies
  * **Shell commands** \- Git operations, system utilities, complex pipelines
  * **Long-running processes** \- Background services, servers



## Create an execution context

Code contexts maintain state between executions:
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    
    // Create a Python context
    const pythonContext = await sandbox.createCodeContext({
    	language: "python",
    });
    
    console.log("Context ID:", pythonContext.id);
    console.log("Language:", pythonContext.language);
    
    // Create a JavaScript context
    const jsContext = await sandbox.createCodeContext({
    	language: "javascript",
    });
    
    
    import { getSandbox } from '@cloudflare/sandbox';
    
    const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
    
    // Create a Python context
    const pythonContext = await sandbox.createCodeContext({
      language: 'python'
    });
    
    console.log('Context ID:', pythonContext.id);
    console.log('Language:', pythonContext.language);
    
    // Create a JavaScript context
    const jsContext = await sandbox.createCodeContext({
      language: 'javascript'
    });

## Execute code

### Simple execution
    
    
    // Create context
    const context = await sandbox.createCodeContext({
    	language: "python",
    });
    
    // Execute code
    const result = await sandbox.runCode(
    	`
    print("Hello from Code Interpreter!")
    result = 2 + 2
    print(f"2 + 2 = {result}")
    `,
    	{ context: context.id },
    );
    
    console.log("Output:", result.output);
    console.log("Success:", result.success);
    
    
    // Create context
    const context = await sandbox.createCodeContext({
      language: 'python'
    });
    
    // Execute code
    const result = await sandbox.runCode(`
    print("Hello from Code Interpreter!")
    result = 2 + 2
    print(f"2 + 2 = {result}")
    `, { context: context.id });
    
    console.log('Output:', result.output);
    console.log('Success:', result.success);

### State within a context

Variables and imports remain available between executions in the same context, as long as the container stays active:
    
    
    const context = await sandbox.createCodeContext({
    	language: "python",
    });
    
    // First execution - import and define variables
    await sandbox.runCode(
    	`
    import pandas as pd
    import numpy as np
    
    data = [1, 2, 3, 4, 5]
    print("Data initialized")
    `,
    	{ context: context.id },
    );
    
    // Second execution - use previously defined variables
    const result = await sandbox.runCode(
    	`
    mean = np.mean(data)
    print(f"Mean: {mean}")
    `,
    	{ context: context.id },
    );
    
    console.log(result.output); // "Mean: 3.0"
    
    
    const context = await sandbox.createCodeContext({
      language: 'python'
    });
    
    // First execution - import and define variables
    await sandbox.runCode(`
    import pandas as pd
    import numpy as np
    
    data = [1, 2, 3, 4, 5]
    print("Data initialized")
    `, { context: context.id });
    
    // Second execution - use previously defined variables
    const result = await sandbox.runCode(`
    mean = np.mean(data)
    print(f"Mean: {mean}")
    `, { context: context.id });
    
    console.log(result.output); // "Mean: 3.0"

Note

Context state is lost if the container restarts due to inactivity. For critical data, store results outside the sandbox or design your code to reinitialize as needed.

## Handle rich outputs

The code interpreter returns multiple output formats:
    
    
    const result = await sandbox.runCode(
    	`
    import matplotlib.pyplot as plt
    
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title('Simple Chart')
    plt.show()
    `,
    	{ context: context.id },
    );
    
    // Check available formats
    console.log("Formats:", result.formats); // ['text', 'png']
    
    // Access outputs
    if (result.outputs.png) {
    	// Return as image
    	return new Response(atob(result.outputs.png), {
    		headers: { "Content-Type": "image/png" },
    	});
    }
    
    if (result.outputs.html) {
    	// Return as HTML (pandas DataFrames)
    	return new Response(result.outputs.html, {
    		headers: { "Content-Type": "text/html" },
    	});
    }
    
    if (result.outputs.json) {
    	// Return as JSON
    	return Response.json(result.outputs.json);
    }
    
    
    const result = await sandbox.runCode(`
    import matplotlib.pyplot as plt
    
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title('Simple Chart')
    plt.show()
    `, { context: context.id });
    
    // Check available formats
    console.log('Formats:', result.formats);  // ['text', 'png']
    
    // Access outputs
    if (result.outputs.png) {
      // Return as image
      return new Response(atob(result.outputs.png), {
        headers: { 'Content-Type': 'image/png' }
      });
    }
    
    if (result.outputs.html) {
      // Return as HTML (pandas DataFrames)
      return new Response(result.outputs.html, {
        headers: { 'Content-Type': 'text/html' }
      });
    }
    
    if (result.outputs.json) {
      // Return as JSON
      return Response.json(result.outputs.json);
    }

## Stream execution output

For long-running code, stream output in real-time:
    
    
    const context = await sandbox.createCodeContext({
    	language: "python",
    });
    
    const result = await sandbox.runCode(
    	`
    import time
    
    for i in range(10):
        print(f"Processing item {i+1}/10...")
        time.sleep(0.5)
    
    print("Done!")
    `,
    	{
    		context: context.id,
    		stream: true,
    		onOutput: (data) => {
    			console.log("Output:", data);
    		},
    		onResult: (result) => {
    			console.log("Result:", result);
    		},
    		onError: (error) => {
    			console.error("Error:", error);
    		},
    	},
    );
    
    
    const context = await sandbox.createCodeContext({
      language: 'python'
    });
    
    const result = await sandbox.runCode(
      `
    import time
    
    for i in range(10):
        print(f"Processing item {i+1}/10...")
        time.sleep(0.5)
    
    print("Done!")
    `,
      {
        context: context.id,
        stream: true,
        onOutput: (data) => {
          console.log('Output:', data);
        },
        onResult: (result) => {
          console.log('Result:', result);
        },
        onError: (error) => {
          console.error('Error:', error);
        }
      }
    );

## Execute AI-generated code

Run LLM-generated code safely in a sandbox:
    
    
    // 1. Generate code with Claude
    const response = await fetch("https://api.anthropic.com/v1/messages", {
    	method: "POST",
    	headers: {
    		"Content-Type": "application/json",
    		"x-api-key": env.ANTHROPIC_API_KEY,
    		"anthropic-version": "2023-06-01",
    	},
    	body: JSON.stringify({
    		model: "claude-3-5-sonnet-20241022",
    		max_tokens: 1024,
    		messages: [
    			{
    				role: "user",
    				content: "Write Python code to calculate fibonacci sequence up to 100",
    			},
    		],
    	}),
    });
    
    const { content } = await response.json();
    const code = content[0].text;
    
    // 2. Execute in sandbox
    const context = await sandbox.createCodeContext({ language: "python" });
    const result = await sandbox.runCode(code, { context: context.id });
    
    console.log("Generated code:", code);
    console.log("Output:", result.output);
    console.log("Success:", result.success);
    
    
    // 1. Generate code with Claude
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-3-5-sonnet-20241022',
        max_tokens: 1024,
        messages: [{
          role: 'user',
          content: 'Write Python code to calculate fibonacci sequence up to 100'
        }]
      })
    });
    
    const { content } = await response.json();
    const code = content[0].text;
    
    // 2. Execute in sandbox
    const context = await sandbox.createCodeContext({ language: 'python' });
    const result = await sandbox.runCode(code, { context: context.id });
    
    console.log('Generated code:', code);
    console.log('Output:', result.output);
    console.log('Success:', result.success);

## Manage contexts

### List all contexts
    
    
    const contexts = await sandbox.listCodeContexts();
    
    console.log(`${contexts.length} active contexts:`);
    
    for (const ctx of contexts) {
    	console.log(`  ${ctx.id} (${ctx.language})`);
    }
    
    
    const contexts = await sandbox.listCodeContexts();
    
    console.log(`${contexts.length} active contexts:`);
    
    for (const ctx of contexts) {
      console.log(`  ${ctx.id} (${ctx.language})`);
    }

### Delete contexts
    
    
    // Delete specific context
    await sandbox.deleteCodeContext(context.id);
    console.log("Context deleted");
    
    // Clean up all contexts
    const contexts = await sandbox.listCodeContexts();
    for (const ctx of contexts) {
    	await sandbox.deleteCodeContext(ctx.id);
    }
    console.log("All contexts deleted");
    
    
    // Delete specific context
    await sandbox.deleteCodeContext(context.id);
    console.log('Context deleted');
    
    // Clean up all contexts
    const contexts = await sandbox.listCodeContexts();
    for (const ctx of contexts) {
      await sandbox.deleteCodeContext(ctx.id);
    }
    console.log('All contexts deleted');

## Best practices

  * **Clean up contexts** \- Delete contexts when done to free resources
  * **Handle errors** \- Always check `result.success` and `result.error`
  * **Stream long operations** \- Use streaming for code that takes >2 seconds
  * **Validate AI code** \- Review generated code before execution



## Related resources

  * [Code Interpreter API reference](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/) \- Complete API documentation
  * [AI code executor tutorial](https://developers.cloudflare.com/sandbox/sdk/tutorials/ai-code-executor/) \- Build complete AI executor
  * [Execute commands guide](https://developers.cloudflare.com/sandbox/sdk/guides/execute-commands/) \- Lower-level command execution



[PreviousExpose services](https://developers.cloudflare.com/sandbox/sdk/guides/expose-services/)[NextWebSocket connections](https://developers.cloudflare.com/sandbox/sdk/guides/websocket-connections/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/code-execution.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
