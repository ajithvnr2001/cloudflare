---
url: https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/
title: Cloudflare Terraform Provider now properly redacts sensitive values \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.720704+00:00
---

# Cloudflare Terraform Provider now properly redacts sensitive values · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-03-21-sensitive-values-redacted/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 21, 2025

## Cloudflare Terraform Provider now properly redacts sensitive values

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Terraform](https://developers.cloudflare.com/terraform/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In the [Cloudflare Terraform Provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare) versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in [Cloudflare's OpenAPI Schema ↗︎](https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml) are now annotated with `x-sensitive: true`. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.

This issue affected [resources ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) related to these products and features:

  * Alerts and Audit Logs
  * Device API
  * DLP
  * DNS
  * Magic Visibility
  * Magic WAN
  * TLS Certs and Hostnames
  * Tunnels
  * Turnstile
  * Workers
  * Zaraz


