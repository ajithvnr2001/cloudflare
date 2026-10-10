---
url: https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/
title: Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.603835+00:00
---

# Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-23-workers-preview-urls/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 22, 2025

## Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.

This works the same way that Cloudflare Pages does — every time you create a pull request, you'll automatically get a shareable preview link where you can see your changes running, without affecting production. The link stays the same, even as you add commits to the same branch. These preview URLs are named after your branch and are posted as a comment to each pull request. The URL stays the same with every commit and always points to the latest version of that branch.

![PR comment preview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2900,height=1064,format=webp/_astro/preview-urls-comment.0wQffFIq.png)

#### Preview URL types

Each comment includes **two preview URLs** as shown above:

  * **Commit Preview URL** : Unique to the specific version/commit (e.g., `<version-prefix>-<worker-name>.<subdomain>.workers.dev`)
  * **Branch Preview URL** : A stable alias based on the branch name (e.g., `<branch-name>-<worker-name>.<subdomain>.workers.dev`)



#### How it works

When you create a pull request:

  * **A preview alias is automatically created** based on the Git branch name (e.g., `<branch-name>` becomes `<branch-name>-<worker-name>.<subdomain>.workers.dev`)
  * **No configuration is needed** , the alias is generated for you
  * **The link stays the same** even as you add commits to the same branch
  * **Preview URLs are posted directly to your pull request as comments** (just like they are in Cloudflare Pages)



#### Custom alias name

You can also assign a custom preview alias using the [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/), by passing the `--preview-alias` flag when [uploading a version](https://developers.cloudflare.com/workers/wrangler/commands/general/#versions-upload) of your Worker:
    
    
    wrangler versions upload --preview-alias staging

#### Limitations while in beta

  * Only available on the **workers.dev** subdomain (custom domains not yet supported)
  * Requires **Wrangler v4.21.0+**
  * Preview URLs are not generated for Workers that use [Durable Objects](https://developers.cloudflare.com/durable-objects/)
  * Not yet supported for [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)


