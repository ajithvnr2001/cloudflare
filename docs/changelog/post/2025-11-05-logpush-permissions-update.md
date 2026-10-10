---
url: https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/
title: Logpush Permission Update for Zero Trust Datasets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:47.151723+00:00
---

# Logpush Permission Update for Zero Trust Datasets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-05-logpush-permissions-update/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 5, 2025

## Logpush Permission Update for Zero Trust Datasets

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Permissions](https://developers.cloudflare.com/logs/logpush/permissions/) for managing Logpush jobs related to [Zero Trust datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) (Access, Gateway, and DEX) have been updated to improve data security and enforce appropriate access controls.

To view, create, update, or delete Logpush jobs for Zero Trust datasets, users must now have both of the following permissions:

  * Logs Edit
  * Zero Trust: PII Read



Note

Update your UI, API or Terraform configurations to include the new permissions. Requests to Zero Trust datasets will fail due to insufficient access without the additional permission.
