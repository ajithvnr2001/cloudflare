---
url: https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/
title: Sandbox SDK + Artifacts \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:21.371626+00:00
---

# Sandbox SDK + Artifacts · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Examples
  4. /Sandbox SDK + Artifacts



# Sandbox SDK + Artifacts

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate your project1\. Create or reuse the repo2\. Create or reuse the sandbox3\. Pass the repo into the sandbox

This example uses the `git-repo-per-sandbox` Sandbox SDK template and highlights the Artifacts-specific pieces.

Start from the template with `create cloudflare`, as shown in Create your project. Then adapt the Artifacts flow with the snippets in steps 1 to 3.

  * Creates or reuses a sandbox by ID.
  * Creates or reuses an Artifacts repo with the same ID.
  * Passes an authenticated Git remote into the sandbox as `ARTIFACTS_GIT_REMOTE`.



## Create your project

npmyarnpnpm
    
    
    npm create cloudflare@latest -- repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox#v0
    
    
    yarn create cloudflare repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox#v0
    
    
    pnpm create cloudflare@latest repo-per-sandbox --template=cloudflare/sandbox-sdk/examples/git-repo-per-sandbox#v0
    
    
    cd repo-per-sandbox

## 1\. Create or reuse the repo

The template keeps one Artifacts repo per sandbox ID. Use your own source of truth to decide whether this request should create a new repo or load an existing one.

src/index.jsjs
    
    
    let defaultBranch;
    let remote;
    let token;
    const sandboxWasJustCreated = true; // for example, set this when you create a new sandbox record
    
    if (sandboxWasJustCreated) {
    	const created = await env.ARTIFACTS.create(sandboxId);
    
    	defaultBranch = created.defaultBranch;
    	remote = created.remote;
    	token = created.token;
    } else {
    	const repo = await env.ARTIFACTS.get(sandboxId);
    
    	defaultBranch = repo.defaultBranch;
    	remote = repo.remote;
    	token = (await repo.createToken("write", 3600)).plaintext;
    }

src/index.tsts
    
    
    let defaultBranch: string;
    let remote: string;
    let token: string;
    const sandboxWasJustCreated = true; // for example, set this when you create a new sandbox record
    
    if (sandboxWasJustCreated) {
    	const created = await env.ARTIFACTS.create(sandboxId);
    
    	defaultBranch = created.defaultBranch;
    	remote = created.remote;
    	token = created.token;
    } else {
    	const repo = await env.ARTIFACTS.get(sandboxId);
    
    	defaultBranch = repo.defaultBranch;
    	remote = repo.remote;
    	token = (await repo.createToken("write", 3600)).plaintext;
    }

The template already knows the repo name, so start with direct lookup instead of scanning `list()` pages. Avoid broad `catch` blocks here. They can hide missing-repo, auth, and validation failures behind the same retry message.

If your flow can race with repo creation, handle that retry at the application level after you inspect the thrown error.

## 2\. Create or reuse the sandbox

Use the same ID for the sandbox:

src/index.jsjs
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, sandboxId);

src/index.tsts
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, sandboxId);

## 3\. Pass the repo into the sandbox

Convert the write token into an authenticated Git remote, then store it as an environment variable inside the sandbox.

Use a short-lived token and pass it into the sandbox only after the sandbox session is authorized to push changes.

src/index.jsjs
    
    
    function toAuthenticatedRemote(remote, token) {
    	const tokenSecret = token.split("?expires=")[0];
    	return `https://x:${tokenSecret}@${remote.slice("https://".length)}`;
    }
    
    await sandbox.setEnvVars({
    	ARTIFACTS_GIT_REMOTE: toAuthenticatedRemote(remote, token),
    });

src/index.tsts
    
    
    function toAuthenticatedRemote(remote: string, token: string) {
    	const tokenSecret = token.split("?expires=")[0];
    	return `https://x:${tokenSecret}@${remote.slice("https://".length)}`;
    }
    
    await sandbox.setEnvVars({
    	ARTIFACTS_GIT_REMOTE: toAuthenticatedRemote(remote, token),
    });

Code running inside the sandbox can then use `ARTIFACTS_GIT_REMOTE` with `git clone`, `git fetch`, `git pull`, or `git push`.

[Previousisomorphic-git](https://developers.cloudflare.com/artifacts/examples/isomorphic-git/)[NextPricing](https://developers.cloudflare.com/artifacts/platform/pricing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/examples/sandbox-sdk-artifacts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
