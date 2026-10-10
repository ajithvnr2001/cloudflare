---
url: https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/
title: Custom container instance types now available for all users \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.383364+00:00
---

# Custom container instance types now available for all users · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-05-custom-instance-types/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 5, 2026

## Custom container instance types now available for all users

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Custom instance types are now enabled for all [Cloudflare Containers](https://developers.cloudflare.com/containers) users. You can now specify specific vCPU, memory, and disk amounts, rather than being limited to pre-defined [instance types](https://developers.cloudflare.com/containers/platform/limits/#instance-types). Previously, only select Enterprise customers were able to customize their instance type.

To use a custom instance type, specify the `instance_type` property as an object with `vcpu`, `memory_mib`, and `disk_mb` fields in your Wrangler configuration:
    
    
    [[containers]]
    image = "./Dockerfile"
    instance_type = { vcpu = 2, memory_mib = 6144, disk_mb = 12000 }

Individual limits for custom instance types are based on the `standard-4` instance type (4 vCPU, 12 GiB memory, 20 GB disk). You must allocate at least 1 vCPU for custom instance types. For workloads requiring less than 1 vCPU, use the predefined instance types like `lite` or `basic`.

See the [limits documentation](https://developers.cloudflare.com/containers/platform/limits/#custom-instance-types) for the full list of constraints on custom instance types. See the [getting started guide](https://developers.cloudflare.com/containers/get-started/) to deploy your first Container,
