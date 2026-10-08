---
url: https://developers.cloudflare.com/terraform/troubleshooting/authentication-error-dns-records/
title: 403 Authentication error when creating DNS records \u00b7 Cloudflare Terraform docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:01.112330+00:00
---

# 403 Authentication error when creating DNS records · Cloudflare Terraform docs

> Source: https://developers.cloudflare.com/terraform/troubleshooting/authentication-error-dns-records/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Terraform](https://developers.cloudflare.com/terraform/)
  3. /Troubleshooting
  4. /Create DNS records error



# 403 Authentication error when creating DNS records

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/terraform/troubleshooting/authentication-error-dns-records/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When creating DNS records using Terraform, the API returns the following error:

`Error: failed to create DNS record: HTTP status 403: Authentication error (10000)`

This is caused by an error in your code syntax, when you are not using index `[0]` for the zones. Find an example below and a more detailed thread on [GitHub ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare/issues/913).

Instead of this:
    
    
    zone_id = data.cloudflare_zones.example_com.id

Use this:
    
    
    zone_id = data.cloudflare_zones.example_com.zones[0].id`

[PreviousRemote R2 backend](https://developers.cloudflare.com/terraform/advanced-topics/remote-backend/)[NextRule IDs change when making updates](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/terraform/troubleshooting/authentication-error-dns-records.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
