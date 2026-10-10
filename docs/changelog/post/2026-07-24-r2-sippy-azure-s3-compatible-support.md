---
url: https://developers.cloudflare.com/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/
title: Sippy now supports Azure Blob Storage and S3-compatible storage providers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:34.333207+00:00
---

# Sippy now supports Azure Blob Storage and S3-compatible storage providers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 24, 2026

## Sippy now supports Azure Blob Storage and S3-compatible storage providers

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Sippy](https://developers.cloudflare.com/r2/data-migration/sippy/) can now incrementally migrate data from Azure Blob Storage and any S3-compatible object storage provider to [Cloudflare R2](https://developers.cloudflare.com/r2/), in addition to Amazon S3 and Google Cloud Storage. Sippy copies objects to R2 as your application requests them, so you can start serving data from R2 without first moving your entire dataset or paying migration-specific egress fees.

#### Enable Sippy

Run the following command and follow the prompts to select and configure your source storage provider:
    
    
    npx wrangler r2 bucket sippy enable "<BUCKET_NAME>"

For Azure Blob Storage, provide your storage account name, container name, and either an account key or a shared access signature (SAS) token with read and list permissions. For an S3-compatible provider, provide the S3 API endpoint URL and read-only Access Key ID and Secret Access Key.

![Azure Blob Storage source configuration in the R2 dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=400,height=650,format=webp/_astro/sippy-azure-source-configuration.j9uacYgX.png)

After you enable Sippy, requests for objects that are not yet in R2 are served from your source bucket and copied to R2. Subsequent requests for those objects are served from R2.

For setup instructions and credential requirements, refer to the [Sippy documentation](https://developers.cloudflare.com/r2/data-migration/sippy/).
