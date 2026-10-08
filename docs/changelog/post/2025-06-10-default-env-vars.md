---
url: https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/
title: Access git commit sha and branch name as environment variables in Workers Builds \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:13.841024+00:00
---

# Access git commit sha and branch name as environment variables in Workers Builds · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 10, 2025

## Access git commit sha and branch name as environment variables in Workers Builds

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) connects your Worker to a [Git repository](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/), and automates building and deploying your code on each pushed change.

To make CI/CD pipelines even more flexible, Workers Builds now automatically injects [default environment variables](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#environment-variables) into your build process (much like the defaults in [Cloudflare Pages projects](https://developers.cloudflare.com/pages/configuration/build-configuration/#environment-variables)). You can use these variables to customize your build process based on the deployment context, such as the branch or commit.

The following environment variables are injected by default:

Environment Variable | Injected value | Example use-case  
---|---|---  
`CI` | `true` | Changing build behavior when run on CI versus locally  
`WORKERS_CI` | `1` | Changing build behavior when run on Workers Builds versus locally  
`WORKERS_CI_BUILD_UUID` | `<build-uuid-of-current-build>` | Passing the Build UUID along to custom workflows  
`WORKERS_CI_COMMIT_SHA` | `<sha1-hash-of-current-commit>` | Passing current commit ID to error reporting, for example, Sentry  
`WORKERS_CI_BRANCH` | `<branch-name-from-push-event` | Customizing build based on branch, for example, disabling debug logging on `production`  
  
You can override these default values and add your own custom environment variables by navigating to **your Worker** > **Settings** > **Environment variables**.

Learn more in the [Build configuration documentation](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#environment-variables).
