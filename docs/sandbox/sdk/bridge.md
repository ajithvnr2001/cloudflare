---
url: https://developers.cloudflare.com/sandbox/sdk/bridge/
title: Sandbox bridge (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:22.426772+00:00
---

# Sandbox bridge (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/bridge/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)
  4. /Sandbox bridge



# Sandbox bridge

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/bridge/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy use the bridgeDeploy Container imageUsage Create a sandbox and run a command Write and read filesKeep the bridge updatedSource code and examplesRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Sandboxes](https://developers.cloudflare.com/sandbox/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

The sandbox bridge is a reference-implementation Cloudflare Worker that exposes the [Sandbox SDK](https://developers.cloudflare.com/sandbox/sdk/api/) as an HTTP API. Any HTTP client — Python script, Node.js service, CI pipeline — can create and control sandboxes without writing a Worker. You deploy the Worker in **your** account; it is not a Cloudflare-hosted shared API.

## Why use the bridge

The Sandbox SDK is designed for use within Cloudflare Workers. If your application runs outside of the Workers ecosystem, it cannot interact with sandboxes directly.

The bridge exposes the Sandbox SDK as a standard HTTP API so you can create and control sandboxes from any language or platform.

Key [Sandbox SDK methods](https://developers.cloudflare.com/sandbox/sdk/api/) map to individual HTTP endpoints. The bridge adds authentication, input validation, workspace path containment, and an optional [warm pool](https://developers.cloudflare.com/sandbox/sdk/bridge/http-api/#warm-pool) for instant container boot.

## Deploy

Deploy the bridge Worker to your Cloudflare account:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/sandbox-sdk/tree/v0/bridge/worker)

The button deploys the Worker and generates a `SANDBOX_API_KEY` secret for authentication. When deployment finishes, note your Worker URL and API key — every example on this page uses them.

Manual deployment

If you prefer to deploy step by step, scaffold the project and deploy manually.

**Prerequisites:**

  * A [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages) with the Containers / Sandbox beta enabled.
  * [Node.js ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) and npm.
  * [Docker ↗︎](https://www.docker.com/) running locally — `wrangler deploy` builds a container image from the bridge `Dockerfile`.



**Steps:**

  1. Scaffold the bridge project:
         
         npm create cloudflare -- sandbox-bridge --template=cloudflare/sandbox-sdk/bridge/worker#v0
         cd sandbox-bridge

  2. Authenticate with Cloudflare:
         
         npx wrangler login

  3. Set the API key secret. Choose any strong token value — clients must send this as a Bearer token:
         
         openssl rand -hex 32 | tee /dev/stderr | npx wrangler secret put SANDBOX_API_KEY

The key is printed to your terminal and piped to Wrangler. Save it — you will need it to authenticate API requests.

  4. Deploy the Worker:
         
         npx wrangler deploy

  5. Verify the deployment:
         
         curl https://cloudflare-sandbox-bridge.<your-subdomain>.workers.dev/health

You should see `{"ok":true}`.




### Container image

The bridge `Dockerfile` extends the [`cloudflare/sandbox` ↗︎](https://hub.docker.com/r/cloudflare/sandbox) base image and pre-installs common agent tooling:

  * **Languages** : Python 3.13, Node.js, Bun
  * **Tools** : git, ripgrep, curl, wget, jq, tar, sed, gawk, procps



Customize the `Dockerfile` to add languages, system packages, or tools your workloads need.

## Usage

All examples assume the following environment variables are set:
    
    
    export SANDBOX_API_URL=https://cloudflare-sandbox-bridge.<your-subdomain>.workers.dev
    export SANDBOX_API_KEY=<your-token>

### Create a sandbox and run a command
    
    
    # Create a sandbox
    SANDBOX_ID=$(curl -s -X POST "$SANDBOX_API_URL/v1/sandbox" \
      -H "Authorization: Bearer $SANDBOX_API_KEY" | jq -r '.id')
    
    echo "Sandbox ID: $SANDBOX_ID"
    
    # Run a command
    curl -s -X POST "$SANDBOX_API_URL/v1/sandbox/$SANDBOX_ID/exec" \
      -H "Authorization: Bearer $SANDBOX_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"argv": ["sh", "-lc", "echo hello from the sandbox"], "timeout_ms": 10000}'
    
    # Destroy the sandbox when done
    curl -s -X DELETE "$SANDBOX_API_URL/v1/sandbox/$SANDBOX_ID" \
      -H "Authorization: Bearer $SANDBOX_API_KEY"
    
    
    const API_URL = process.env.SANDBOX_API_URL;
    const API_KEY = process.env.SANDBOX_API_KEY;
    
    const headers = {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    };
    
    // Create a sandbox
    const { id } = await fetch(`${API_URL}/v1/sandbox`, {
      method: "POST",
      headers,
    }).then((r) => r.json());
    
    console.log(`Sandbox ID: ${id}`);
    
    // Run a command
    // Response is a text/event-stream with the following SSE events:
    //   event: stdout  — data is a base64-encoded output chunk
    //   event: stderr  — data is a base64-encoded error chunk
    //   event: exit    — data is JSON: {"exit_code": 0}
    //   event: error   — data is JSON: {"error": "...", "code": "..."}
    const execRes = await fetch(`${API_URL}/v1/sandbox/${id}/exec`, {
      method: "POST",
      headers,
      body: JSON.stringify({
        argv: ["sh", "-lc", "echo hello from the sandbox"],
        timeout_ms: 10000,
      }),
    });
    
    console.log(await execRes.text());
    
    // Destroy the sandbox when done
    await fetch(`${API_URL}/v1/sandbox/${id}`, {
      method: "DELETE",
      headers,
    });
    
    
    # /// script
    # dependencies = ["httpx"]
    # ///
    import os
    import httpx
    
    API_URL = os.environ["SANDBOX_API_URL"]
    API_KEY = os.environ["SANDBOX_API_KEY"]
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    # Create a sandbox
    resp = httpx.post(f"{API_URL}/v1/sandbox", headers=headers)
    sandbox_id = resp.json()["id"]
    print(f"Sandbox ID: {sandbox_id}")
    
    # Run a command
    # Response is a text/event-stream with the following SSE events:
    #   event: stdout  — data is a base64-encoded output chunk
    #   event: stderr  — data is a base64-encoded error chunk
    #   event: exit    — data is JSON: {"exit_code": 0}
    #   event: error   — data is JSON: {"error": "...", "code": "..."}
    exec_resp = httpx.post(
        f"{API_URL}/v1/sandbox/{sandbox_id}/exec",
        headers=headers,
        json={
            "argv": ["sh", "-lc", "echo hello from the sandbox"],
            "timeout_ms": 10000,
        },
    )
    print(exec_resp.text)
    
    # Destroy the sandbox when done
    httpx.delete(f"{API_URL}/v1/sandbox/{sandbox_id}", headers=headers)

### Write and read files
    
    
    # Write a file
    curl -s -X PUT "$SANDBOX_API_URL/v1/sandbox/$SANDBOX_ID/file/workspace/hello.py" \
      -H "Authorization: Bearer $SANDBOX_API_KEY" \
      --data-binary 'print("hello world")'
    
    # Read a file
    curl -s "$SANDBOX_API_URL/v1/sandbox/$SANDBOX_ID/file/workspace/hello.py" \
      -H "Authorization: Bearer $SANDBOX_API_KEY"
    
    
    // Write a file
    await fetch(`${API_URL}/v1/sandbox/${id}/file/workspace/hello.py`, {
      method: "PUT",
      headers,
      body: 'print("hello world")',
    });
    
    // Read a file
    const content = await fetch(
      `${API_URL}/v1/sandbox/${id}/file/workspace/hello.py`,
      { headers },
    ).then((r) => r.text());
    
    console.log(content);
    
    
    # /// script
    # dependencies = ["httpx"]
    # ///
    import os
    import httpx
    
    API_URL = os.environ["SANDBOX_API_URL"]
    API_KEY = os.environ["SANDBOX_API_KEY"]
    SANDBOX_ID = os.environ["SANDBOX_ID"]  # from the "Create a sandbox" step
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    # Write a file
    httpx.put(
        f"{API_URL}/v1/sandbox/{SANDBOX_ID}/file/workspace/hello.py",
        headers=headers,
        content=b'print("hello world")',
    )
    
    # Read a file
    content = httpx.get(
        f"{API_URL}/v1/sandbox/{SANDBOX_ID}/file/workspace/hello.py",
        headers=headers,
    ).text
    print(content)

## Keep the bridge updated

The bulk of the bridge logic is in the `@cloudflare/sandbox` package. To pull in the latest improvements:

  1. Update the SDK dependency:
         
         npm update @cloudflare/sandbox

  2. Redeploy:
         
         npx wrangler deploy




Check the [sandbox-sdk releases ↗︎](https://github.com/cloudflare/sandbox-sdk/releases) for changes to the `Dockerfile` or bridge configuration that may require manual updates.

## Source code and examples

The bridge source code and examples are available on GitHub:

  * [Bridge source ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/v0/bridge) — Worker, Dockerfile, deploy script, and OpenAPI schema.
  * [Workspace chat example ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/v0/bridge/examples/workspace-chat) — Full-stack chat application with a file browser sidebar.
  * [Basic example ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/v0/bridge/examples/basic) — One-shot Python coding agent using the OpenAI Agents SDK.



## Related resources

  * [HTTP API reference](https://developers.cloudflare.com/sandbox/sdk/bridge/http-api/) — Complete route reference for the bridge API.
  * [Getting started](https://developers.cloudflare.com/sandbox/sdk/get-started/) — Build your first sandbox application directly on Workers.
  * [Architecture](https://developers.cloudflare.com/sandbox/sdk/concepts/architecture/) — How the Sandbox SDK layers Workers, Durable Objects, and Containers.
  * [API reference](https://developers.cloudflare.com/sandbox/sdk/api/) — Complete Sandbox SDK method reference.
  * [OpenAI Agents SDK tutorial](https://developers.cloudflare.com/sandbox/sdk/tutorials/openai-agents/) — Build a Python coding agent with the bridge.



[PreviousTransport modes](https://developers.cloudflare.com/sandbox/sdk/configuration/transport/)[NextHTTP API reference](https://developers.cloudflare.com/sandbox/sdk/bridge/http-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/bridge/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
