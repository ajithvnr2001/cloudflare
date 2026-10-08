---
url: https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/
title: Custom Container instance types no longer have a disk to memory ratio limit \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:16.965731+00:00
---

# Custom Container instance types no longer have a disk to memory ratio limit · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 29, 2026

## Custom Container instance types no longer have a disk to memory ratio limit

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-remove-disk-to-memory-ratio/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) custom instance types no longer limit disk based on memory. Previously, a custom instance type could have a maximum of 2 GB of disk for each 1 GiB of memory. You can now allocate up to the 20 GB disk maximum to any custom instance type.

Use this to run workloads that need more disk than memory, such as workloads with large container images, datasets, or build caches. The maximum image size is the same as the instance disk space, so more disk also lets you deploy larger images.

For example, a custom instance type with 1 vCPU and 3 GiB of memory was previously limited to 6 GB of disk. It can now use 20 GB:
    
    
    {
    	"containers": [
    		{
    			"image": "./Dockerfile",
    			"instance_type": {
    				"vcpu": 1,
    				"memory_mib": 3072,
    				"disk_mb": 20000,
    			},
    		},
    	],
    }
    
    
    [[containers]]
    image = "./Dockerfile"
    
      [containers.instance_type]
      vcpu = 1
      memory_mib = 3_072
      disk_mb = 20_000

The other custom instance type constraints do not change, including the minimum of 3 GiB of memory per vCPU. For the full list, refer to [Custom Instance Types](https://developers.cloudflare.com/containers/platform/limits/#custom-instance-types).
