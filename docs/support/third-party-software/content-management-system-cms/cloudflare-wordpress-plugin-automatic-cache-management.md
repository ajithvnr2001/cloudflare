---
url: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/
title: Cloudflare WordPress Plugin Automatic Cache Management \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:51.631967+00:00
---

# Cloudflare WordPress Plugin Automatic Cache Management · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Third-Party Software](https://developers.cloudflare.com/support/third-party-software/)

  4. /[Content Management System (CMS)](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/)
  5. /Cloudflare WordPress Plugin Automatic Cache Management



# Cloudflare WordPress Plugin Automatic Cache Management

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOverviewEnable Automatic Cache Management

## Overview

The Cloudflare WordPress plugin contains a feature called Automatic Cache Management. When a user adds, edits, or deletes a post, page, attachment, or comment - any associated URLs are purged from the Cloudflare cache.

When you switch a theme or customise a theme within the WordPress admin panel, the cache will automatically be cleared too.

Automatic Cache Management uses native hooks built into WordPress. The Cloudflare WordPress plugin purges the following cache URLs:

  * deleted_post
  * edit_post
  * delete_attachment
  * autoptimize_action_cachepurged (for compatibility with the Autoptimize WordPress plugin)
  * switch_theme
  * customize_save_after



* * *

## Enable Automatic Cache Management

To enable Automatic Cache Management after [installing the WordPress plugin](https://developers.cloudflare.com/automatic-platform-optimization/):

  1. Log in to your WordPress account.
  2. Click **Settings** and choose the Cloudflare plugin. The Cloudflare plugin home page appears.
  3. Click **Enable** to the right of the **Automatic Cache** feature. A confirmation dialog appears.
  4. Click **I'm sure** in the confirmation dialog to confirm.



[PreviousOverview](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/)[NextHow do I enable HTTP2 Server Push in WordPress](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/how-do-i-enable-http2-server-push-in-wordpress/)

Was this helpful?

YesNo
