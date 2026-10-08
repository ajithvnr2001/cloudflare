---
url: https://developers.cloudflare.com/sandbox/concepts/
title: Choose a sandbox environment \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:17.470339+00:00
---

# Choose a sandbox environment · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/concepts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /Concepts



# Choose a sandbox environment

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/concepts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat the code can useUse a Container when the code expects LinuxUse a Dynamic Worker when the code calls known methodsHow each environment isolates codeWhat you maintainUse both in one application

A sandbox runs code that you did not write and do not trust, such as code that a model generates or the test suite of a repository. Cloudflare runs it in one of two environments: a [Container](https://developers.cloudflare.com/containers/), which runs a Linux image, or a [Dynamic Worker](https://developers.cloudflare.com/dynamic-workers/), which runs JavaScript against methods that your [Worker](https://developers.cloudflare.com/workers/) provides. Your Worker starts either one, and one Worker can use both.

## What the code can use

Code in a Container can use everything in its Linux image: runtimes, packages, files, and the processes it starts.

Code in a Dynamic Worker can use only the modules, methods, and values that your Worker passes to it. It does not inherit the bindings, credentials, or data of your Worker. Set `globalOutbound` to `null` to block its direct access to the Internet.

Your Worker keeps credentials and policy. It starts a Container, which runs a command in your Linux image and can use runtimes, packages, files, and processes. It also passes methods and values to a Dynamic Worker, which runs generated code and does not inherit your bindings, data, or credentials.

## Use a Container when the code expects Linux

Most existing tools expect an operating system as well as a language runtime. `npm test` needs Node.js, dependencies on a filesystem, and child processes. A preview server keeps a process running and listens on a port. A compiler may need a toolchain or native binaries.

JavaScript code can need Linux too. A Dynamic Worker cannot start child processes or load native add-ons, and Workers implements some Node.js modules only in part. For what Workers supports, refer to [Node.js compatibility](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).

Your Worker decides when the container starts, whether it can reach the Internet, and which HTTP requests reach it. The [Agents sandbox tool](https://developers.cloudflare.com/agents/tools/sandbox/) uses a Container to run commands for an agent.

## Use a Dynamic Worker when the code calls known methods

When code only needs to call methods that you define, such as a script against a known API, run it in a Dynamic Worker. Your Worker decides what each method can reach before it passes the method in.

For example, your Worker can pass a `listPullRequests()` method that works for one repository and keeps the API token. Generated code can filter the pull requests, but it cannot reach another repository or read the token. For more information, refer to [Bindings](https://developers.cloudflare.com/dynamic-workers/usage/bindings/).

[Code Mode](https://developers.cloudflare.com/agents/tools/codemode/) uses this for agents. The model writes JavaScript against typed methods, a Dynamic Worker runs it, and only the result returns to the model context.

`load()` creates a new Dynamic Worker. `get()` with a stable ID lets the runtime reuse a warm Dynamic Worker when the same code runs again. To give a generated application its own storage, use [Durable Object facets](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/). That storage does not give the application access to your other resources.

## How each environment isolates code

A Container runs in a [Firecracker](https://developers.cloudflare.com/containers/concepts/architecture/#container-runtime) microVM with its own kernel and network, which no other workload shares. Your image runs as a Linux container inside that VM.

V8, the JavaScript engine in Chrome, runs each Dynamic Worker in a sandbox that cannot read memory outside itself. The Workers runtime adds a process-level sandbox around it. For more information, refer to the [Workers security model](https://developers.cloudflare.com/workers/reference/security-model/).

## What you maintain

With a Container, you build and update the image. Existing tools run without changes, but the container must start before the first command runs. For more information, refer to [Container cold starts](https://developers.cloudflare.com/containers/concepts/architecture/#cold-starts).

With a Dynamic Worker, you write each method and decide what it returns. When generated code needs another operation, you add a method. The code that loads the Dynamic Worker lists everything the generated code can reach.

## Use both in one application

A coding agent can answer questions about a repository through scoped methods in a Dynamic Worker. When the agent proposes a patch, the same Worker starts a Container and runs the test suite of the repository.

### [Run a Linux command](https://developers.cloudflare.com/sandbox/get-started/)

Post a command to a Worker and read stdout from Linux.

### [Run JavaScript](https://developers.cloudflare.com/sandbox/get-started/dynamic-workers/)

Post JavaScript to a Worker and read the sandboxed result.

[PreviousBuild a coding agent runner](https://developers.cloudflare.com/sandbox/get-started/build-a-coding-agent-runner/)[NextLifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/concepts/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
