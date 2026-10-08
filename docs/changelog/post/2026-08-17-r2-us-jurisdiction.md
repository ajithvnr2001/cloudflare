---
url: https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/
title: New `us` jurisdiction for R2 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:08.918386+00:00
---

# New `us` jurisdiction for R2 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 17, 2026

## New `us` jurisdiction for R2

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-17-r2-us-jurisdiction/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 now supports a `us` [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions), which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees.

Use the jurisdiction-specific S3 endpoint to create and access buckets in the `us` jurisdiction:

`https://<ACCOUNT_ID>.us.r2.cloudflarestorage.com`

To access a bucket in the `us` jurisdiction from Workers, set `jurisdiction` in your R2 binding:
    
    
    {
    	"r2_buckets": [
    		{
    			"binding": "MY_BUCKET",
    			"bucket_name": "<YOUR_BUCKET_NAME>",
    			"jurisdiction": "us"
    		}
    	]
    }
    
    
    [[r2_buckets]]
    binding = "MY_BUCKET"
    bucket_name = "<YOUR_BUCKET_NAME>"
    jurisdiction = "us"

Once an R2 bucket is created, its jurisdiction cannot be changed.

For setup instructions and the full list of supported jurisdictions, refer to [R2 data location](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions).
