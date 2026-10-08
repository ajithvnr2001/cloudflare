---
url: https://developers.cloudflare.com/workers/ci-cd/
title: CI/CD \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:11.044716+00:00
---

# CI/CD · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /CI/CD



# CI/CD

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhy use CI/CD?Which CI/CD should I use?Workers BuildsExternal CI/CD

You can set up continuous integration and continuous deployment (CI/CD) for your Workers by using either the integrated build system, Workers Builds, or using external providers to optimize your development workflow.

## Why use CI/CD?

Using a CI/CD pipeline to deploy your Workers is a best practice because it:

  * Automates the build and deployment process, removing the need for manual `wrangler deploy` commands.
  * Ensures consistent builds and deployments across your team by using the same source control management (SCM) system.
  * Reduces variability and errors by deploying in a uniform environment.
  * Simplifies managing access to production credentials.



## Which CI/CD should I use?

Choose [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds) if you want a fully integrated solution within Cloudflare's ecosystem for Artifacts, GitHub, or GitLab repositories.

We recommend using [external CI/CD providers](https://developers.cloudflare.com/workers/ci-cd/external-cicd) if:

  * You have a self-hosted instance of GitHub or GitLab, which is currently not supported in Workers Builds' [Git integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/)
  * You are using a Git provider other than Artifacts, GitHub, or GitLab



## Workers Builds

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds) is Cloudflare's native CI/CD system that allows you to integrate with Artifacts, GitHub, or GitLab to automatically deploy changes with each new push to a selected branch (e.g. `main`).

![Workers Builds Workflow Diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=923,height=203,format=webp/_astro/workers-builds-workflow.DzGN9FAh.png)

Ready to streamline your Workers deployments? Get started with [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/#get-started).

## External CI/CD

You can also choose to set up your CI/CD pipeline with an external provider.

  * [GitHub Actions](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/)
  * [GitLab CI/CD](https://developers.cloudflare.com/workers/ci-cd/external-cicd/gitlab-cicd/)



[PreviousVersion URLs](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/)[NextOverview](https://developers.cloudflare.com/workers/ci-cd/builds/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
