---
url: https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/
title: Dozens of Cloudflare Terraform Provider resources now have proper drift detection \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.776899+00:00
---

# Dozens of Cloudflare Terraform Provider resources now have proper drift detection · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-21-resource-force-replacement-bug/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 21, 2025

## Dozens of Cloudflare Terraform Provider resources now have proper drift detection

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your `terraform plan` to only show what resources are expected to change.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

  * API Shield
  * Argo Smart Routing
  * Argo Tiered Caching
  * Bot Management
  * BYOIP
  * D1
  * DNS
  * Email Routing
  * Hyperdrive
  * Observatory
  * Pages
  * R2
  * Rules
  * SSL/TLS
  * Waiting Room
  * Workers
  * Zero Trust


