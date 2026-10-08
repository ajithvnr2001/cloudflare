---
url: https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/
title: Delete Log Explorer datasets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:10.831692+00:00
---

# Delete Log Explorer datasets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 26, 2026

## Delete Log Explorer datasets

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-dataset-deletion/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.

Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to [Manage datasets](https://developers.cloudflare.com/log-explorer/manage-datasets/), disable deletion protection for the dataset, select **Delete** , and enter the dataset name to confirm.

To delete a dataset through the API, first set `deletion_protection` to `false` with the [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/) method. Then use the [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/) method.

Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.
