---
url: https://developers.cloudflare.com/sandbox/sdk/guides/git-workflows/
title: Work with Git (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:25.308177+00:00
---

# Work with Git (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/guides/git-workflows/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[How-to guides](https://developers.cloudflare.com/sandbox/sdk/guides/)
  5. /Work with Git



# Work with Git

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/guides/git-workflows/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewClone repositories

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Run tests from a Git repository](https://developers.cloudflare.com/sandbox/commands/run-tests-from-a-git-repository/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

This guide shows you how to clone repositories, manage branches, and automate Git operations in the sandbox.

## Clone repositories
    
    
    import { getSandbox } from "@cloudflare/sandbox";
    
    const sandbox = getSandbox(env.Sandbox, "my-sandbox");
    
    // Basic clone
    await sandbox.gitCheckout("https://github.com/user/repo");
    
    // Clone specific branch
    await sandbox.gitCheckout("https://github.com/user/repo", {
    	branch: "develop",
    });
    
    // Shallow clone (faster for large repos)
    await sandbox.gitCheckout("https://github.com/user/large-repo", {
    	depth: 1,
    });
    
    // Clone to specific directory
    await sandbox.gitCheckout("https://github.com/user/my-app", {
    	targetDir: "/workspace/project",
    });
    
    
    import { getSandbox } from '@cloudflare/sandbox';
    
    const sandbox = getSandbox(env.Sandbox, 'my-sandbox');
    
    // Basic clone
    await sandbox.gitCheckout('https://github.com/user/repo');
    
    // Clone specific branch
    await sandbox.gitCheckout('https://github.com/user/repo', {
      branch: 'develop'
    });
    
    // Shallow clone (faster for large repos)
    await sandbox.gitCheckout('https://github.com/user/large-repo', {
      depth: 1
    });
    
    // Clone to specific directory
    await sandbox.gitCheckout('https://github.com/user/my-app', {
      targetDir: '/workspace/project'
    });

## Clone private repositories

Use a personal access token in the URL:
    
    
    const token = env.GITHUB_TOKEN;
    const repoUrl = `https://${token}@github.com/user/private-repo.git`;
    
    await sandbox.gitCheckout(repoUrl);
    
    
    const token = env.GITHUB_TOKEN;
    const repoUrl = `https://${token}@github.com/user/private-repo.git`;
    
    await sandbox.gitCheckout(repoUrl);

More secure alternative

Embedding a token in the URL passes the credential directly into the sandbox. For better access control, use an outbound handler that injects the real token at request time — the sandbox never holds the credential. Refer to [Handle outbound traffic](https://developers.cloudflare.com/sandbox/sdk/guides/outbound-traffic/).

## Clone and build

Clone a repository and run build steps:
    
    
    await sandbox.gitCheckout("https://github.com/user/my-app");
    
    const repoName = "my-app";
    
    // Install and build
    await sandbox.exec(`cd ${repoName} && npm install`);
    await sandbox.exec(`cd ${repoName} && npm run build`);
    
    console.log("Build complete");
    
    
    await sandbox.gitCheckout('https://github.com/user/my-app');
    
    const repoName = 'my-app';
    
    // Install and build
    await sandbox.exec(`cd ${repoName} && npm install`);
    await sandbox.exec(`cd ${repoName} && npm run build`);
    
    console.log('Build complete');

## Work with branches
    
    
    await sandbox.gitCheckout("https://github.com/user/repo");
    
    // Switch branches
    await sandbox.exec("cd repo && git checkout feature-branch");
    
    // Create new branch
    await sandbox.exec("cd repo && git checkout -b new-feature");
    
    
    await sandbox.gitCheckout('https://github.com/user/repo');
    
    // Switch branches
    await sandbox.exec('cd repo && git checkout feature-branch');
    
    // Create new branch
    await sandbox.exec('cd repo && git checkout -b new-feature');

## Make changes and commit
    
    
    await sandbox.gitCheckout("https://github.com/user/repo");
    
    // Modify a file
    const readme = await sandbox.readFile("/workspace/repo/README.md");
    await sandbox.writeFile(
    	"/workspace/repo/README.md",
    	readme.content + "\n\n## New Section",
    );
    
    // Commit changes
    await sandbox.exec('cd repo && git config user.name "Sandbox Bot"');
    await sandbox.exec('cd repo && git config user.email "bot@example.com"');
    await sandbox.exec("cd repo && git add README.md");
    await sandbox.exec('cd repo && git commit -m "Update README"');
    
    
    await sandbox.gitCheckout('https://github.com/user/repo');
    
    // Modify a file
    const readme = await sandbox.readFile('/workspace/repo/README.md');
    await sandbox.writeFile('/workspace/repo/README.md', readme.content + '\n\n## New Section');
    
    // Commit changes
    await sandbox.exec('cd repo && git config user.name "Sandbox Bot"');
    await sandbox.exec('cd repo && git config user.email "bot@example.com"');
    await sandbox.exec('cd repo && git add README.md');
    await sandbox.exec('cd repo && git commit -m "Update README"');

## Best practices

  * **Use shallow clones** \- Faster for large repos with `depth: 1`
  * **Store credentials securely** \- Use environment variables for tokens
  * **Clean up** \- Delete unused repositories to save space



## Troubleshooting

### Authentication fails

Verify your token is set:
    
    
    if (!env.GITHUB_TOKEN) {
    	throw new Error("GITHUB_TOKEN not configured");
    }
    
    const repoUrl = `https://${env.GITHUB_TOKEN}@github.com/user/private-repo.git`;
    await sandbox.gitCheckout(repoUrl);
    
    
    if (!env.GITHUB_TOKEN) {
      throw new Error('GITHUB_TOKEN not configured');
    }
    
    const repoUrl = `https://${env.GITHUB_TOKEN}@github.com/user/private-repo.git`;
    await sandbox.gitCheckout(repoUrl);

### Large repository timeout

Use shallow clone:
    
    
    await sandbox.gitCheckout("https://github.com/user/large-repo", {
    	depth: 1,
    });
    
    
    await sandbox.gitCheckout('https://github.com/user/large-repo', {
      depth: 1
    });

## Related resources

  * [Files API reference](https://developers.cloudflare.com/sandbox/sdk/api/files/) \- File operations after cloning
  * [Execute commands guide](https://developers.cloudflare.com/sandbox/sdk/guides/execute-commands/) \- Run git commands
  * [Manage files guide](https://developers.cloudflare.com/sandbox/sdk/guides/manage-files/) \- Work with cloned files



[PreviousWebSocket connections](https://developers.cloudflare.com/sandbox/sdk/guides/websocket-connections/)[NextStream output](https://developers.cloudflare.com/sandbox/sdk/guides/streaming-output/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/guides/git-workflows.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
