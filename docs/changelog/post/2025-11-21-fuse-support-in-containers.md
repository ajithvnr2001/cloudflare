---
url: https://developers.cloudflare.com/changelog/post/2025-11-21-fuse-support-in-containers/
title: Mount R2 buckets in Containers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:46.409285+00:00
---

# Mount R2 buckets in Containers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-21-fuse-support-in-containers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 21, 2025

## Mount R2 buckets in Containers

[Containers](https://developers.cloudflare.com/containers/)[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) now support mounting R2 buckets as FUSE (Filesystem in Userspace) volumes, allowing applications to interact with [R2](https://developers.cloudflare.com/r2/) using standard filesystem operations.

Common use cases include:

  * Bootstrapping containers with datasets, models, or dependencies for [sandboxes](https://developers.cloudflare.com/sandbox/) and [agent](https://developers.cloudflare.com/agents/) environments
  * Persisting user configuration or application state without managing downloads
  * Accessing large static files without bloating container images or downloading at startup



FUSE adapters like [tigrisfs ↗︎](https://github.com/tigrisdata/tigrisfs), [s3fs ↗︎](https://github.com/s3fs-fuse/s3fs-fuse), and [gcsfuse ↗︎](https://github.com/GoogleCloudPlatform/gcsfuse) can be installed in your container image and configured to mount buckets at startup.
    
    
    FROM alpine:3.20
    
    # Install FUSE and dependencies
    RUN apk update && \
        apk add --no-cache ca-certificates fuse curl bash
    
    # Install tigrisfs
    RUN ARCH=$(uname -m) && \
        if [ "$ARCH" = "x86_64" ]; then ARCH="amd64"; fi && \
        if [ "$ARCH" = "aarch64" ]; then ARCH="arm64"; fi && \
        VERSION=$(curl -s https://api.github.com/repos/tigrisdata/tigrisfs/releases/latest | grep -o '"tag_name": "[^"]*' | cut -d'"' -f4) && \
        curl -L "https://github.com/tigrisdata/tigrisfs/releases/download/${VERSION}/tigrisfs_${VERSION#v}_linux_${ARCH}.tar.gz" -o /tmp/tigrisfs.tar.gz && \
        tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ && \
        rm /tmp/tigrisfs.tar.gz && \
        chmod +x /usr/local/bin/tigrisfs
    
    # Create startup script that mounts bucket
    RUN printf '#!/bin/sh\n\
        set -e\n\
        mkdir -p /mnt/r2\n\
        R2_ENDPOINT="https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com"\n\
        /usr/local/bin/tigrisfs --endpoint "${R2_ENDPOINT}" -f "${BUCKET_NAME}" /mnt/r2 &\n\
        sleep 3\n\
        ls -lah /mnt/r2\n\
        ' > /startup.sh && chmod +x /startup.sh
    
    CMD ["/startup.sh"]

See the [Mount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/) example for a complete guide on mounting R2 buckets and/or other S3-compatible storage buckets within your containers.
