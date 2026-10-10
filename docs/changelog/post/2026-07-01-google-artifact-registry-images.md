---
url: https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/
title: Use Google Artifact Registry images with Containers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.738963+00:00
---

# Use Google Artifact Registry images with Containers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-01-google-artifact-registry-images/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 1, 2026

## Use Google Artifact Registry images with Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Containers now support [Google Artifact Registry ↗︎](https://cloud.google.com/artifact-registry) images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) instead of first pushing the image to Cloudflare Registry.

Provide the service account email with `--gar-email` and pipe the service account JSON key through `stdin`:
    
    
    cat <PATH_TO_KEY> | npx wrangler containers registries configure <REGION>-docker.pkg.dev --gar-email=<SERVICE_ACCOUNT_EMAIL> --secret-name=<SECRET_NAME>
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "containers": [
        {
          "image": "<REGION>-docker.pkg.dev/<PROJECT_ID>/<REPOSITORY>/<IMAGE>:<TAG>"
        }
      ]
    }
    
    
    # Example: us-central1-docker.pkg.dev/my-project/my-repo/my-image:latest
    [[containers]]
    image = "<REGION>-docker.pkg.dev/<PROJECT_ID>/<REPOSITORY>/<IMAGE>:<TAG>"

Only `*-docker.pkg.dev` hosts are supported. To configure credentials, refer to [Use private Google Artifact Registry images](https://developers.cloudflare.com/containers/guides/image-management/#use-private-google-artifact-registry-images).

For more information, refer to [Image management](https://developers.cloudflare.com/containers/guides/image-management/).
