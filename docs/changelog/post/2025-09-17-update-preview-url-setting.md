---
url: https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/
title: Preview URLs now default to opt-in \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:48.778692+00:00
---

# Preview URLs now default to opt-in · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-09-17-update-preview-url-setting/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 17, 2025

## Preview URLs now default to opt-in

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To prevent the accidental exposure of applications, we've updated how [Worker preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) (`<PREVIEW>-<WORKER_NAME>.<SUBDOMAIN>.workers.dev`) are handled. We made this change to ensure preview URLs are only active when intentionally configured, improving the default security posture of your Workers.

#### One-Time Update for Workers with workers.dev Disabled

We performed a one-time update to disable preview URLs for existing Workers where the [workers.dev subdomain](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/) was also disabled.

Because preview URLs were historically enabled by default, users who had intentionally disabled their workers.dev route may not have realized their Worker was still accessible at a separate preview URL. This update was performed to ensure that using a preview URL is always an intentional, opt-in choice.

If your Worker was affected, its preview URL (`<PREVIEW>-<WORKER_NAME>.<SUBDOMAIN>.workers.dev`) will now direct to an informational page explaining this change.

**How to Re-enable Your Preview URL**

If your preview URL was disabled, you can re-enable it [via the Cloudflare dashboard](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable) by navigating to your Worker's Settings page and toggling on the Preview URL.

Alternatively, you can use Wrangler by adding the `preview_urls = true` setting to your Wrangler file and redeploying the Worker.
    
    
    {
      "preview_urls": true
    }
    
    
    preview_urls = true

**Note:** You can set `preview_urls = true` with any Wrangler version that supports the preview URL flag (v3.91.0+). However, we recommend updating to v4.34.0 or newer, as this version defaults `preview_urls` to false, ensuring preview URLs are always enabled by explicit choice.
