---
url: https://developers.cloudflare.com/changelog/post/2025-04-08-deploy-to-cloudflare-button/
title: Deploy a Workers application in seconds with one-click \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.235240+00:00
---

# Deploy a Workers application in seconds with one-click · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-08-deploy-to-cloudflare-button/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 8, 2025

## Deploy a Workers application in seconds with one-click

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now add a [Deploy to Cloudflare](https://developers.cloudflare.com/workers/platform/deploy-buttons/) button to the README of your Git repository containing a Workers application — making it simple for other developers to quickly set up and deploy your project!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/saas-admin-template)

The Deploy to Cloudflare button:

  1. **Creates a new Git repository on your GitHub/ GitLab account** : Cloudflare will automatically clone and create a new repository on your account, so you can continue developing.
  2. **Automatically provisions resources the app needs** : If your repository requires Cloudflare primitives like a [Workers KV namespace](https://developers.cloudflare.com/kv/), a [D1 database](https://developers.cloudflare.com/d1/), or an [R2 bucket](https://developers.cloudflare.com/r2/), Cloudflare will automatically provision them on your account and bind them to your Worker upon deployment.
  3. **Configures Workers Builds (CI/CD)** : Every new push to your production branch on your newly created repository will automatically build and deploy courtesy of [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/).
  4. **Adds preview URLs to each pull request** : If you'd like to test your changes before deploying, you can push changes to a [non-production branch](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds) and [preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) will be generated and [posted back to GitHub as a comment](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment).

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=4306,height=1344,format=webp/_astro/dtw-user-flow.zgS3Y8iK.png)

To create a Deploy to Cloudflare button in your README, you can add the following snippet, including your Git repository URL:
    
    
    [![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=<YOUR_GIT_REPO_URL>)

Check out our [documentation](https://developers.cloudflare.com/workers/platform/deploy-buttons/) for more information on how to set up a deploy button for your application and best practices to ensure a successful deployment for other developers.
