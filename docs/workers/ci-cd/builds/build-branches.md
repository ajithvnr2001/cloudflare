---
url: https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/
title: Build branches \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:12.060801+00:00
---

# Build branches · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[CI/CD](https://developers.cloudflare.com/workers/ci-cd/)

  4. /[Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  5. /Build branches



# Build branches

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChange production branchConfigure preview builds Existing Workers connected to Builds

When you connect a git repository to Workers, commits made on the production branch produce a production build. To create [Previews](https://developers.cloudflare.com/workers/previews/) and, for GitHub and GitLab repositories, [pull request comments](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment) for branches that are not your production branch, enable preview builds.

## Change production branch

To change the production branch of your project:

  1. In **Overview** , select your Workers project.
  2. Go to **Settings** > **Build** > **Branch control**. Workers will default to the default branch of your git repository, but this can be changed in the dropdown.



Every push event made to this branch will trigger a build and execute the [build command](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings), followed by the [deploy command](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#deploy-command).

## Configure preview builds

Preview builds are builds for branches that are not your production branch.

New Workers use Worker Previews for preview builds by default. Their Preview command is `npx wrangler preview`.

To enable or disable preview builds:

  1. In **Overview** , select your Workers project.
  2. Go to **Settings** > **Build** > **Branch control**. The checkbox **Enable Preview Builds** allows you to enable or disable Preview Builds.



When enabled, every push to a branch that is not your production branch triggers a preview build. Workers Builds runs the [build command](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings), followed by the [Preview command](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#preview-command).

### Existing Workers connected to Builds

Workers that were connected to Builds before [Worker Previews](https://developers.cloudflare.com/workers/previews/) keep the previous preview model until you complete a one-time switch.

The switch cannot be reversed

After switching, you cannot return to the previous preview model, which uses production settings.

  1. In the Cloudflare dashboard, go to **Workers & Pages** > your Worker > **Settings** > **Builds**. In the **Set up Worker Previews** banner, select **Set up**.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages) ![Dialog showing Preview settings confirmation and the new Worker Previews command](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1034,height=1264,format=webp/_astro/switch-to-worker-previews.X2uOGKZ3.png)
  2. Configure the variables, secrets, and bindings your Worker needs for Previews. Previews do not use production settings. For instructions, refer to [Get started](https://developers.cloudflare.com/workers/previews/get-started/#step-1-configure-preview-settings).

  3. Review the new Preview command. Workers Builds replaces the current command with `npx wrangler preview`. Custom commands must invoke `npx wrangler preview`.

  4. Select **Switch to Worker Previews**.




After switching, pushes to branches that are not your production branch use Worker Previews.

[PreviousBuild caching](https://developers.cloudflare.com/workers/ci-cd/builds/build-caching/)[NextBuild watch paths](https://developers.cloudflare.com/workers/ci-cd/builds/build-watch-paths/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/builds/build-branches.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
