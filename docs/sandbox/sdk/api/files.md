---
url: https://developers.cloudflare.com/sandbox/sdk/api/files/
title: Files (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:21.386251+00:00
---

# Files (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/api/files/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[API reference](https://developers.cloudflare.com/sandbox/sdk/api/)
  5. /Files



# Files

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/api/files/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethods writeFile() readFile() renameFile() moveFile() gitCheckout()

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Files API](https://developers.cloudflare.com/sandbox/reference/files/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Read, write, and manage files in the sandbox filesystem. All paths are absolute (e.g., `/workspace/app.js`).

## Methods

### `writeFile()`

Write content to a file.
    
    
    await sandbox.writeFile(path: string, content: string, options?: WriteFileOptions): Promise<void>

**Parameters** :

  * `path` \- Absolute path to the file
  * `content` \- Content to write
  * `options` (optional): 
    * `encoding` \- File encoding (`"utf-8"` or `"base64"`, default: `"utf-8"`)


    
    
    await sandbox.writeFile("/workspace/app.js", `console.log('Hello!');`);
    
    // Binary data
    await sandbox.writeFile("/tmp/image.png", base64Data, { encoding: "base64" });
    
    
    await sandbox.writeFile('/workspace/app.js', `console.log('Hello!');`);
    
    // Binary data
    await sandbox.writeFile('/tmp/image.png', base64Data, { encoding: 'base64' });

Base64 validation

When using `encoding: 'base64'`, content must contain only valid base64 characters (A-Z, a-z, 0-9, +, /, =). Invalid base64 content returns a validation error.

#### Large files and binary data

When using the [`rpc` transport](https://developers.cloudflare.com/sandbox/sdk/configuration/transport/) the `writeFile()` method supports passing a `ReadableStream` as the `content` parameter. This allows binary data and files greater than [32 MiB](https://developers.cloudflare.com/workers/runtime-apis/rpc/#limitations) to be written to the sandbox. It replaces the `"base64"` encoding option.
    
    
    // Requires SANDBOX_TRANSPORT to be "rpc" in wrangler.jsonc
    const req = await fetch("https://example.com/archive.tar.gz");
    await sandbox.writeFile('/workspace/archive.tar.gz', req.body);

### `readFile()`

Read a file from the sandbox. By default returns the content as a string. This is useful for small text files. For larger files and binary data use `encoding: "none"` to get back a `ReadableStream` with the file data.
    
    
    const file = await sandbox.readFile(path: string, options?: ReadFileOptions): Promise<ReadFileResult | ReadFileStreamResult>

**Parameters** :

  * `path` \- Absolute path to the file
  * `options` (optional): 
    * `encoding` \- File encoding (`"utf-8"`, `"base64"` or `"none"`, default: auto-detected from MIME type)



**Returns** : `Promise<ReadFileResult | ReadFileStreamResult>`.

Encoding

The `"none"` encoding property was added in 0.10.1 and aims to improve support for streaming binary data. When `encoding: "none"` is provided the `content` field will be a `ReadableStream<Uint8Array>`. It is only supported with the [RPC transport](https://developers.cloudflare.com/sandbox/sdk/configuration/transport/).
    
    
    const file = await sandbox.readFile("/workspace/package.json");
    const pkg = JSON.parse(file.content);
    
    // Binary data (since 0.10.1 using `rpc` transport)
    const { content, size, mimeType } = await sandbox.readFile(
    	"/workspace/archive.tar.gz",
    	{
    		encoding: "none",
    	},
    );
    
    // Example 1: Store on R2:
    const stream = request.body.pipeThrough(new FixedLengthStream(size));
    await env.MY_BUCKET.put("/bucket/archive.tar.gz", stream, {
    	httpMetadata: { contentType: mimeType },
    });
    
    // Example 2: Stream an HTTP response:
    return new Response(content, { headers: { "Content-Type": mimeType } });
    
    // Older versions/transports used the base64 encoding for binary data:
    const archive = await sandbox.readFile("/workspace/archive.tar.gz", {
    	encoding: "base64",
    });
    console.log(archive.content); // => "<base64 encoded string>";
    
    
    const file = await sandbox.readFile('/workspace/package.json');
    const pkg = JSON.parse(file.content);
    
    // Binary data (since 0.10.1 using `rpc` transport)
    const { content, size, mimeType } = await sandbox.readFile("/workspace/archive.tar.gz", {
      encoding: "none"
    });
    
    // Example 1: Store on R2:
    const stream = request.body.pipeThrough(new FixedLengthStream(size));
    await env.MY_BUCKET.put('/bucket/archive.tar.gz', stream, {
      httpMetadata: { contentType: mimeType }
    });
    
    // Example 2: Stream an HTTP response:
    return new Response(content, { headers: { "Content-Type": mimeType } });
    
    // Older versions/transports used the base64 encoding for binary data:
    const archive = await sandbox.readFile("/workspace/archive.tar.gz", {
      encoding: "base64"
    });
    console.log(archive.content); // => "<base64 encoded string>";

Encoding behavior

When `encoding` is specified, it overrides MIME-based auto-detection. Without `encoding`, the SDK detects the appropriate encoding from the file's MIME type.

### `exists()`

Check if a file or directory exists.
    
    
    const result = await sandbox.exists(path: string): Promise<FileExistsResult>

**Parameters** :

  * `path` \- Absolute path to check



**Returns** : `Promise<FileExistsResult>` with `exists` boolean
    
    
    const result = await sandbox.exists("/workspace/package.json");
    if (result.exists) {
    	const file = await sandbox.readFile("/workspace/package.json");
    	// process file
    }
    
    // Check directory
    const dirResult = await sandbox.exists("/workspace/src");
    if (!dirResult.exists) {
    	await sandbox.mkdir("/workspace/src");
    }
    
    
    const result = await sandbox.exists('/workspace/package.json');
    if (result.exists) {
      const file = await sandbox.readFile('/workspace/package.json');
      // process file
    }
    
    // Check directory
    const dirResult = await sandbox.exists('/workspace/src');
    if (!dirResult.exists) {
      await sandbox.mkdir('/workspace/src');
    }

Available on sessions

Both `sandbox.exists()` and `session.exists()` are supported.

### `mkdir()`

Create a directory.
    
    
    await sandbox.mkdir(path: string, options?: MkdirOptions): Promise<void>

**Parameters** :

  * `path` \- Absolute path to the directory
  * `options` (optional): 
    * `recursive` \- Create parent directories if needed (default: `false`)


    
    
    await sandbox.mkdir("/workspace/src");
    
    // Nested directories
    await sandbox.mkdir("/workspace/src/components/ui", { recursive: true });
    
    
    await sandbox.mkdir('/workspace/src');
    
    // Nested directories
    await sandbox.mkdir('/workspace/src/components/ui', { recursive: true });

### `deleteFile()`

Delete a file.
    
    
    await sandbox.deleteFile(path: string): Promise<void>

**Parameters** :

  * `path` \- Absolute path to the file


    
    
    await sandbox.deleteFile("/workspace/temp.txt");
    
    
    await sandbox.deleteFile('/workspace/temp.txt');

### `renameFile()`

Rename a file.
    
    
    await sandbox.renameFile(oldPath: string, newPath: string): Promise<void>

**Parameters** :

  * `oldPath` \- Current file path
  * `newPath` \- New file path


    
    
    await sandbox.renameFile("/workspace/draft.txt", "/workspace/final.txt");
    
    
    await sandbox.renameFile('/workspace/draft.txt', '/workspace/final.txt');

### `moveFile()`

Move a file to a different directory.
    
    
    await sandbox.moveFile(sourcePath: string, destinationPath: string): Promise<void>

**Parameters** :

  * `sourcePath` \- Current file path
  * `destinationPath` \- Destination path


    
    
    await sandbox.moveFile("/tmp/download.txt", "/workspace/data.txt");
    
    
    await sandbox.moveFile('/tmp/download.txt', '/workspace/data.txt');

### `gitCheckout()`

Clone a git repository.
    
    
    await sandbox.gitCheckout(repoUrl: string, options?: GitCheckoutOptions): Promise<void>

**Parameters** :

  * `repoUrl` \- Git repository URL
  * `options` (optional): 
    * `branch` \- Branch to checkout (default: repository default branch)
    * `targetDir` \- Directory to clone into (default: `/workspace/{repoName}`)
    * `depth` \- Clone depth for shallow clones (e.g., `1` for latest commit only)


    
    
    await sandbox.gitCheckout("https://github.com/user/repo");
    
    // Specific branch
    await sandbox.gitCheckout("https://github.com/user/repo", {
    	branch: "develop",
    	targetDir: "/workspace/my-project",
    });
    
    // Shallow clone (faster for large repositories)
    await sandbox.gitCheckout("https://github.com/facebook/react", {
    	depth: 1,
    });
    
    
    await sandbox.gitCheckout('https://github.com/user/repo');
    
    // Specific branch
    await sandbox.gitCheckout('https://github.com/user/repo', {
      branch: 'develop',
      targetDir: '/workspace/my-project'
    });
    
    // Shallow clone (faster for large repositories)
    await sandbox.gitCheckout('https://github.com/facebook/react', {
      depth: 1
    });

## Related resources

  * [Manage files guide](https://developers.cloudflare.com/sandbox/sdk/guides/manage-files/) \- Detailed guide with best practices
  * [Commands API](https://developers.cloudflare.com/sandbox/sdk/api/commands/) \- Execute commands



[PreviousCommands](https://developers.cloudflare.com/sandbox/sdk/api/commands/)[NextCode interpreter](https://developers.cloudflare.com/sandbox/sdk/api/interpreter/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/api/files.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
