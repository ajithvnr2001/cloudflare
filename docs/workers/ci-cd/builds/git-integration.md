---
url: https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/
title: Git integration \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:12.585691+00:00
---

# Git integration · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[CI/CD](https://developers.cloudflare.com/workers/ci-cd/)

  4. /[Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  5. /Git integration



# Git integration

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported Git ProvidersAdd a Git IntegrationManage a Git Integration

Cloudflare supports connecting your [Cloudflare Artifacts](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/), [GitHub](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/), [GitLab](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/), or [Cursor Origin](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/) (Cursor's Git hosting platform) repository to your Cloudflare Worker, and will automatically deploy your code every time you push a change.

Adding a Git integration also lets you monitor build statuses directly in your Git provider. [GitHub](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/#features) and [Cursor Origin](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/#features) use pull request comments and check runs, while [GitLab](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/#features) uses commit statuses, so you can manage deployments without leaving your workflow.

## Supported Git Providers

Cloudflare supports connecting Cloudflare Workers to your Artifacts, GitHub, GitLab, and Cursor Origin repositories. Workers Builds does not currently support connecting self-hosted instances of GitHub or GitLab.

If you are using a different Git provider (e.g. Bitbucket), you can use an [external CI/CD provider (e.g. GitHub Actions)](https://developers.cloudflare.com/workers/ci-cd/external-cicd/) and deploy using [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy).

## Add a Git Integration

Workers Builds provides direct integration with Artifacts repositories, GitHub and GitLab accounts that are _not_ self-hosted, and Cursor Origin user and team repositories.

To connect an Artifacts repository, refer to the [Cloudflare Artifacts integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/).

When connecting a GitHub or GitLab repository for the first time, follow the prompts in the Cloudflare dashboard to authorize the Git provider. To connect Cursor Origin, install the [Cloudflare app in Cursor ↗︎](https://cursor.com/codebase/settings/apps/public/cloudflare) and follow the installation prompts.

![Connect a Git repository in Workers Builds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1354,height=318,format=webp/_astro/builds-git-repo-connect.Do4CyWZv.png)

You can check the following pages to see if your Git integration has been installed:

  * [GitHub Applications page ↗︎](https://github.com/settings/installations) (if you are in an organization, select **Switch settings context** to access your GitHub organization settings)
  * [GitLab Authorized Applications page ↗︎](https://gitlab.com/-/profile/applications)
  * [Cursor codebase settings ↗︎](https://cursor.com/codebase/settings/apps)



For details on managing provider access, refer to the [GitHub](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/#organizational-access), [GitLab](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/#organizational-access), and [Cursor Origin](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/#team-access) integration guides.

## Manage a Git Integration

To manage your Git installation:

  1. Go to the **Workers & Pages** page in the Cloudflare dashboard.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select your Worker.

  3. Go to **Settings** > **Builds**.

  4. Under **Git Repository** , select **Manage**.




This can be useful for managing repository access or troubleshooting installation issues by reinstalling. For more details on how to manage your installation, refer to the [GitHub](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/), [GitLab](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/), and [Cursor Origin](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/cursor-origin-integration/) guides.

[PreviousAutomatic pull requests](https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/)[NextArtifacts integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/builds/git-integration/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
