---
url: https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/
title: Cloudflare Artifacts integration \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:12.663052+00:00
---

# Cloudflare Artifacts integration · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[CI/CD](https://developers.cloudflare.com/workers/ci-cd/)[Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)

  4. /[Git integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/)
  5. /Artifacts integration



# Cloudflare Artifacts integration

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRequirementsConnect a new WorkerConnect an existing WorkerBuild production and Preview branchesManage the connection

[Cloudflare Artifacts](https://developers.cloudflare.com/artifacts/) provides Git-compatible storage within Cloudflare. Workers Builds can build and deploy a Worker directly from an Artifacts repository.

With Artifacts and Workers Builds, you can host source code, run builds, test changes with Worker Previews, and deploy Workers entirely within Cloudflare.

## Requirements

Your Cloudflare account role must include Artifacts Read and Artifacts Edit permissions. Your repository must contain the source code and project configuration required to build and deploy your Worker.

Push your project to the repository before you connect it to Workers Builds. You can connect an empty repository, but the first build will fail because there is nothing to build. Push a commit to start a new build.

## Connect a new Worker

  1. In the Cloudflare dashboard, go to **Workers & Pages**.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select **Create application** > **Continue with Artifacts**.

  3. Select the namespace that contains your repository.

  4. Select the repository that contains your project.

  5. Review the project name, deploy command, and Preview command.

  6. (Optional) Enter a build command if your project requires one.

  7. (Optional) Under **Advanced settings** , set **Path** if your project is not in the repository root.

  8. Select **Deploy**.




## Connect an existing Worker

Before you begin, push the existing Worker's source code and configuration to Artifacts. Connecting an existing Worker does not copy its original source code from the deployed Worker.

  1. In the Cloudflare dashboard, go to **Workers & Pages**.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select the Worker you want to connect.

  3. Go to **Settings** > **Builds**.

  4. Select **Connect**.

  5. From the **Git connection** dropdown, select the Artifacts namespace that contains your repository.

  6. Select the repository.

  7. Review the build command, deploy command, and Preview command. Confirm that the Wrangler configuration targets the existing Worker.

  8. (Optional) Under **Advanced settings** , set **Path** if your project is not in the repository root.

  9. Save the connection.

  10. Push a commit to the repository to start a build.




## Build production and Preview branches

Pushes to the production branch run the configured build and deploy commands. The Artifacts integration only supports `main` as the production branch. The default deploy command, `npx wrangler deploy`, deploys the change to production.

To test changes before production, open your Worker in the Cloudflare dashboard. Go to **Settings** > **Builds** , select **Previews Base** , and turn on **Builds for Preview branches**. For more information, refer to [Preview builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/#configure-preview-builds). Pushes to non-production branches run the Preview command, which defaults to `npx wrangler preview`. A successful build creates or updates a branch Preview URL in the Worker's **Previews** section.

## Manage the connection

To change the repository or source provider, disconnect Workers Builds and create another connection. Existing deployments continue serving traffic after you disconnect a repository.

For build settings and environment variables, refer to [Workers Builds configuration](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/).

[PreviousOverview](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/)[NextGitHub integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/builds/git-integration/artifacts-integration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
