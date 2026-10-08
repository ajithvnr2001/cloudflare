---
url: https://developers.cloudflare.com/sandbox/sdk/api/storage/
title: Storage (Sandbox SDK 0.x) \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:22.213127+00:00
---

# Storage (Sandbox SDK 0.x) · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/sdk/api/storage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /…

[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)

  4. /[API reference](https://developers.cloudflare.com/sandbox/sdk/api/)
  5. /Storage



# Storage

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/sdk/api/storage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethods mountBucket() BucketProviderRelated resources

Note

This page documents Sandbox SDK 0.x for existing applications. For new applications, refer to [Mount an R2 bucket](https://developers.cloudflare.com/sandbox/files/mount-an-r2-bucket/). To move an existing application to `@cloudflare/sandbox` 1.0, refer to [Migrate from Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/migrate/).

Mount S3-compatible storage buckets (R2, S3, GCS) into the sandbox filesystem for persistent data access. `mountBucket()` supports R2 binding mounts, local R2 binding sync during development, and remote S3-compatible endpoint mounts.

## Methods

### `mountBucket()`

Mount an S3-compatible bucket to a local path in the sandbox.
    
    
    await sandbox.mountBucket(
      bucket: string,
      mountPath: string,
      options?: MountBucketOptions
    ): Promise<void>

**Parameters** :

  * `bucket` \- Bucket identifier 
    * When `options.endpoint` is omitted, pass the Worker R2 binding name (for example, `"MY_BUCKET"`)
    * When `options.endpoint` is provided, pass the remote bucket name (for example, `"my-r2-bucket"`)
  * `mountPath` \- Local filesystem path to mount at (e.g., `"/data"`)
  * `options` (optional) - Mount configuration (see `MountBucketOptions`)


    
    
    // Mount an R2 bucket by Worker binding name
    await sandbox.mountBucket("MY_BUCKET", "/data");
    
    // Read/write files directly
    const data = await sandbox.readFile("/data/config.json");
    await sandbox.writeFile("/data/results.json", JSON.stringify(data));
    
    // Mount a remote S3-compatible bucket, including explicit R2 endpoints
    await sandbox.mountBucket("my-bucket", "/storage", {
    	endpoint: "https://s3.amazonaws.com",
    	credentials: {
    		accessKeyId: env.AWS_ACCESS_KEY_ID,
    		secretAccessKey: env.AWS_SECRET_ACCESS_KEY,
    	},
    });
    
    // Mount an R2 bucket during local development with wrangler dev
    await sandbox.mountBucket("MY_BUCKET", "/local-data", {
    	localBucket: true,
    });
    
    // Mount a prefix from an R2 binding
    await sandbox.mountBucket("MY_BUCKET", "/user-data", {
    	prefix: "/users/user-123",
    	readOnly: true,
    });
    
    
    // Mount an R2 bucket by Worker binding name
    await sandbox.mountBucket('MY_BUCKET', '/data');
    
    // Read/write files directly
    const data = await sandbox.readFile('/data/config.json');
    await sandbox.writeFile('/data/results.json', JSON.stringify(data));
    
    // Mount a remote S3-compatible bucket, including explicit R2 endpoints
    await sandbox.mountBucket('my-bucket', '/storage', {
      endpoint: 'https://s3.amazonaws.com',
      credentials: {
        accessKeyId: env.AWS_ACCESS_KEY_ID,
        secretAccessKey: env.AWS_SECRET_ACCESS_KEY
      }
    });
    
    // Mount an R2 bucket during local development with wrangler dev
    await sandbox.mountBucket('MY_BUCKET', '/local-data', {
      localBucket: true
    });
    
    // Mount a prefix from an R2 binding
    await sandbox.mountBucket('MY_BUCKET', '/user-data', {
      prefix: '/users/user-123',
      readOnly: true
    });

**Throws** :

  * `InvalidMountPointError` \- Invalid mount path or conflicts with existing mounts
  * `BucketAccessError` \- Bucket does not exist or insufficient permissions



Authentication

Authentication depends on the mount mode:

  1. Omit `endpoint` to mount an R2 bucket by Worker binding name in production
  2. Set `localBucket: true` to use the same R2 binding during local development
  3. Set `endpoint` to mount a remote S3-compatible bucket, then provide explicit `credentials` or rely on environment variables (`R2_ACCESS_KEY_ID` / `R2_SECRET_ACCESS_KEY` or `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`)



Endpoint-based mounts remain supported for explicit R2 endpoint configuration and for other S3-compatible providers.

See the [Mount Buckets guide](https://developers.cloudflare.com/sandbox/sdk/guides/mount-buckets/) for detailed authentication options.

### `unmountBucket()`

Unmount a previously mounted bucket.
    
    
    await sandbox.unmountBucket(mountPath: string): Promise<void>

**Parameters** :

  * `mountPath` \- Path where the bucket is mounted (e.g., `"/data"`)


    
    
    // Mount, process, unmount
    await sandbox.mountBucket("MY_BUCKET", "/data");
    await sandbox.exec("python process.py");
    
    // Unmount
    await sandbox.unmountBucket("/data");
    
    
    // Mount, process, unmount
    await sandbox.mountBucket('MY_BUCKET', '/data');
    await sandbox.exec('python process.py');
    
    // Unmount
    await sandbox.unmountBucket('/data');

Automatic cleanup

Mounted buckets are automatically unmounted when the container is destroyed.

## Types

### `MountBucketOptions`
    
    
    interface RemoteMountBucketOptions {
      endpoint: string;
      provider?: BucketProvider;
      credentials?: BucketCredentials;
      credentialProxy?: boolean;
      readOnly?: boolean;
      s3fsOptions?: string[];
      prefix?: string;
    }
    
    interface LocalMountBucketOptions {
      localBucket: true;
      prefix?: string;
      readOnly?: boolean;
    }
    
    interface R2BindingMountBucketOptions {
      endpoint?: never;
      prefix?: string;
      readOnly?: boolean;
      s3fsOptions?: string[];
    }
    
    type MountBucketOptions =
      | RemoteMountBucketOptions
      | LocalMountBucketOptions
      | R2BindingMountBucketOptions;

`mountBucket()` supports these three modes:

  * **R2 binding mount** \- Omit `endpoint` to mount by Worker binding name in production

    * Uses credential-less egress interception for R2
    * Supports `prefix`, `readOnly`, and `s3fsOptions`
  * **Local R2 binding mount** \- Set `localBucket: true` during `wrangler dev`

    * Uses the Worker R2 binding directly through local synchronization
    * Supports `prefix` and `readOnly`
  * **Remote endpoint mount** \- Set `endpoint` to mount any S3-compatible provider

    * Supports explicit `credentials` or environment variable auto-detection
    * Set `credentialProxy: true` to keep credentials out of the container (egress interception)
    * Supports `provider`, `prefix`, `readOnly`, and `s3fsOptions`



**Field details** :

  * `endpoint` (remote endpoint mode only) - S3-compatible endpoint URL

    * R2: `'https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com'`
    * S3: `'https://s3.amazonaws.com'`
    * GCS: `'https://storage.googleapis.com'`
  * `localBucket` (local development mode only) - Mount an R2 bucket using the Worker's R2 binding during local development with `wrangler dev`

    * When `true`, the SDK syncs the R2 binding directly instead of using an S3 endpoint
  * `provider` (remote endpoint mode only) - Storage provider hint

    * Enables provider-specific optimizations
    * Values: `'r2'`, `'s3'`, `'gcs'`
  * `credentials` (remote endpoint mode only) - API credentials

    * Contains `accessKeyId` and `secretAccessKey`
    * If not provided, uses environment variables
  * `credentialProxy` (remote endpoint mode only) - Route S3 requests through the Durable Object for signing

    * When `true`, credentials are never written to the container's disk. The Durable Object intercepts and re-signs all outbound S3 requests at the network layer before forwarding them upstream.
    * Supports [AWS SigV4 ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) signing for S3-compatible endpoints (including R2) and HMAC signing for Google Cloud Storage
    * Requires `ContainerProxy` to be exported from your Worker entrypoint
    * Default: `false` (backwards compatibility — recommended to set to `true`; will become the default in a future version)
  * `readOnly` (optional) - Mount in read-only mode

    * Default: `false`
  * `prefix` (optional) - Subdirectory within the bucket to mount

    * When specified, only contents under this prefix are visible at the mount point
    * Must start with `/` (for example, `/data/uploads` or `/data/uploads/`)
    * Default: Mount entire bucket
  * `s3fsOptions` (R2 binding and remote endpoint modes only) - Advanced s3fs mount flags

    * Type: `string[]`
    * Example: `['use_cache=/tmp/cache', 'stat_cache_expire=1']`



### `BucketProvider`

Storage provider hint for automatic s3fs flag optimization.
    
    
    type BucketProvider = "r2" | "s3" | "gcs";

  * `'r2'` \- Cloudflare R2 (recommended, applies `nomixupload` flag)
  * `'s3'` \- Amazon S3
  * `'gcs'` \- Google Cloud Storage



## Related resources

  * [Mount Buckets guide](https://developers.cloudflare.com/sandbox/sdk/guides/mount-buckets/) \- Complete bucket mounting walkthrough
  * [Files API](https://developers.cloudflare.com/sandbox/sdk/api/files/) \- Read and write files



[PreviousFile watching](https://developers.cloudflare.com/sandbox/sdk/api/file-watching/)[NextBackups](https://developers.cloudflare.com/sandbox/sdk/api/backups/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/api/storage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
