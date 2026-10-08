---
url: https://developers.cloudflare.com/containers/examples/r2-fuse-mount/
title: Mount R2 buckets with FUSE \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:35.133897+00:00
---

# Mount R2 buckets with FUSE · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/examples/r2-fuse-mount/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Examples
  4. /Mount R2 buckets with FUSE



# Mount R2 buckets with FUSE

Mount R2 buckets as filesystems using FUSE in Containers

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerDefine the containerStart the taskTest the mountAccess a bucket prefixAllow writes

Mount an [R2 bucket](https://developers.cloudflare.com/r2/) with Filesystem in Userspace (FUSE). This example starts a Container, mounts the bucket read-only, lists its contents, and exits. The Durable Object awaits completion with `monitor()`.

FUSE provides filesystem access to object storage. It does not provide local-disk performance or full POSIX filesystem semantics. It is useful for reading datasets, models, and shared assets.

## Configure the Worker

Create a bucket and [R2 API credentials](https://developers.cloudflare.com/r2/api/tokens/) with Object Read access scoped to that bucket. Replace the bucket name and account ID in this configuration:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "r2-fuse-container",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "observability": {
        "enabled": true
      },
      "containers": [
        {
          "class_name": "FUSEDemo",
          "scheduling_policy": "durable_object",
          "images": {
            "base": {
              "dockerfile": "./Dockerfile"
            }
          }
        }
      ],
      "durable_objects": {
        "bindings": [
          {
            "name": "FUSE_DEMO",
            "class_name": "FUSEDemo"
          }
        ]
      },
      "exports": {
        "FUSEDemo": {
          "type": "durable-object",
          "storage": "sqlite"
        }
      },
      "vars": {
        "R2_BUCKET_NAME": "<BUCKET_NAME>",
        "R2_ACCOUNT_ID": "<ACCOUNT_ID>"
      }
    }
    
    
    name = "r2-fuse-container"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [observability]
    enabled = true
    
    [[containers]]
    class_name = "FUSEDemo"
    scheduling_policy = "durable_object"
    
    [containers.images.base]
    dockerfile = "./Dockerfile"
    
    [[durable_objects.bindings]]
    name = "FUSE_DEMO"
    class_name = "FUSEDemo"
    
    [exports.FUSEDemo]
    type = "durable-object"
    storage = "sqlite"
    
    [vars]
    R2_BUCKET_NAME = "<BUCKET_NAME>"
    R2_ACCOUNT_ID = "<ACCOUNT_ID>"

Store the credentials as Worker secrets:

npmyarnpnpm
    
    
    npx wrangler secret put AWS_ACCESS_KEY_ID
    
    
    yarn wrangler secret put AWS_ACCESS_KEY_ID
    
    
    pnpm wrangler secret put AWS_ACCESS_KEY_ID

npmyarnpnpm
    
    
    npx wrangler secret put AWS_SECRET_ACCESS_KEY
    
    
    yarn wrangler secret put AWS_SECRET_ACCESS_KEY
    
    
    pnpm wrangler secret put AWS_SECRET_ACCESS_KEY

## Define the container

Save the Dockerfile and startup script in the project root. This image installs [tigrisfs ↗︎](https://github.com/tigrisdata/tigrisfs), an adapter for S3-compatible storage.

Dockerfiledockerfile
    
    
    FROM alpine:3.20
    RUN apk add --no-cache ca-certificates fuse curl
    
    ARG TIGRISFS_VERSION=1.2.1
    RUN ARCH=$(uname -m) && \
        case "$ARCH" in x86_64) ARCH=amd64 ;; aarch64) ARCH=arm64 ;; esac && \
        curl -fL "https://github.com/tigrisdata/tigrisfs/releases/download/v${TIGRISFS_VERSION}/tigrisfs_${TIGRISFS_VERSION}_linux_${ARCH}.tar.gz" -o /tmp/tigrisfs.tar.gz && \
        tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ && \
        rm /tmp/tigrisfs.tar.gz && \
        chmod +x /usr/local/bin/tigrisfs
    
    COPY startup.sh /startup.sh
    CMD ["sh", "/startup.sh"]

startup.shsh
    
    
    set -eu
    mkdir -p /mnt/r2
    
    /usr/local/bin/tigrisfs \
      --endpoint "https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com" \
      --region auto -o ro -f "$R2_BUCKET_NAME" /mnt/r2 &
    fuse_pid=$!
    trap 'fusermount -u /mnt/r2 2>/dev/null || true; kill "$fuse_pid" 2>/dev/null || true' EXIT
    
    # Wait for the mount instead of reading an empty local directory.
    attempt=0
    until mountpoint -q /mnt/r2; do
      if ! kill -0 "$fuse_pid" 2>/dev/null; then
        echo "FUSE process exited before mounting" >&2
        exit 1
      fi
      attempt=$((attempt + 1))
      if [ "$attempt" -ge 30 ]; then
        echo "Timed out mounting R2" >&2
        exit 1
      fi
      sleep 1
    done
    
    ls -lah /mnt/r2

The main process exits after listing the bucket. For a long-running application, run its process after the mount is ready and keep the mount alive for the application's lifetime.

## Start the task

Pass credentials through `env` when starting the Container. Set `enableInternet: true` so tigrisfs can reach the R2 endpoint.

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class FUSEDemo extends DurableObject {
    	currentRun;
    
    	run() {
    		this.currentRun ??= this.runOnce().finally(() => {
    			this.currentRun = undefined;
    		});
    		return this.currentRun;
    	}
    
    	async runOnce() {
    		const container = this.ctx.container;
    		if (!container.running) {
    			container.start({
    				image: container.images.base,
    				instance: "lite",
    				enableInternet: true,
    				env: {
    					AWS_ACCESS_KEY_ID: this.env.AWS_ACCESS_KEY_ID,
    					AWS_SECRET_ACCESS_KEY: this.env.AWS_SECRET_ACCESS_KEY,
    					R2_BUCKET_NAME: this.env.R2_BUCKET_NAME,
    					R2_ACCOUNT_ID: this.env.R2_ACCOUNT_ID,
    				},
    			});
    		}
    		await container.monitor();
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		if (new URL(request.url).pathname !== "/run") {
    			return new Response("Not found", { status: 404 });
    		}
    		if (request.method !== "POST") {
    			return new Response("Use POST /run", {
    				status: 405,
    				headers: { Allow: "POST" },
    			});
    		}
    		await env.FUSE_DEMO.getByName("demo").run();
    		return new Response("Bucket listing complete. Check the container logs.");
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    interface Env {
    	FUSE_DEMO: DurableObjectNamespace<FUSEDemo>;
    	AWS_ACCESS_KEY_ID: string;
    	AWS_SECRET_ACCESS_KEY: string;
    	R2_BUCKET_NAME: string;
    	R2_ACCOUNT_ID: string;
    }
    
    export class FUSEDemo extends DurableObject<Env> {
    	private currentRun: Promise<void> | undefined;
    
    	run(): Promise<void> {
    		this.currentRun ??= this.runOnce().finally(() => {
    			this.currentRun = undefined;
    		});
    		return this.currentRun;
    	}
    
    	private async runOnce(): Promise<void> {
    		const container = this.ctx.container!;
    		if (!container.running) {
    			container.start({
    				image: container.images.base,
    				instance: "lite",
    				enableInternet: true,
    				env: {
    					AWS_ACCESS_KEY_ID: this.env.AWS_ACCESS_KEY_ID,
    					AWS_SECRET_ACCESS_KEY: this.env.AWS_SECRET_ACCESS_KEY,
    					R2_BUCKET_NAME: this.env.R2_BUCKET_NAME,
    					R2_ACCOUNT_ID: this.env.R2_ACCOUNT_ID,
    				},
    			});
    		}
    		await container.monitor();
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		if (new URL(request.url).pathname !== "/run") {
    			return new Response("Not found", { status: 404 });
    		}
    		if (request.method !== "POST") {
    			return new Response("Use POST /run", {
    				status: 405,
    				headers: { Allow: "POST" },
    			});
    		}
    		await env.FUSE_DEMO.getByName("demo").run();
    		return new Response("Bucket listing complete. Check the container logs.");
    	},
    } satisfies ExportedHandler<Env>;

Concurrent calls share the active task. A later call starts another run after completion. Protect the route with authentication before exposing it to users.

## Test the mount

For local development, put the R2 credentials in `.dev.vars` as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Do not commit that file. The local container connects to the configured R2 bucket.

Start a Docker-compatible engine that supports [FUSE during local development](https://developers.cloudflare.com/containers/guides/local-dev/#fuse-support). Use Wrangler 4.136.0 or later.

npmyarnpnpmbun
    
    
    npm i -D wrangler
    
    
    yarn add -D wrangler
    
    
    pnpm add -D wrangler
    
    
    bun add -d wrangler

npmyarnpnpm
    
    
    npx wrangler dev
    
    
    yarn wrangler dev
    
    
    pnpm wrangler dev

In another terminal, start the task:
    
    
    curl -X POST http://localhost:8787/run

Check the container logs for the bucket listing. A mount failure makes `monitor()` reject instead of returning a successful response.

## Access a bucket prefix

After mounting, access a prefix through its filesystem path, such as `/mnt/r2/datasets`. A path within a mount does not restrict credentials to that prefix.

## Allow writes

To write through the mount, remove `-o ro` and use R2 credentials with Object Read and Write access. Wait for your application's writes and unmount cleanly before the container exits.

[PreviousWebSocket to container](https://developers.cloudflare.com/containers/examples/websocket/)[NextMore examples](https://developers.cloudflare.com/containers/examples/durable-object-interface/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/examples/r2-fuse-mount.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
