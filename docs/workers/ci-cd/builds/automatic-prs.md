---
url: https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/
title: Automatic pull requests \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:11.698816+00:00
---

# Automatic pull requests · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[CI/CD](https://developers.cloudflare.com/workers/ci-cd/)

  4. /[Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  5. /Automatic pull requests



# Automatic pull requests

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfiguration PR Why you should merge the PR What the PR includes PR descriptionName conflict PRReviewing PRs

Workers Builds can automatically create pull requests in your repository to configure your project or resolve deployment issues. Automatic pull requests are not supported for Artifacts repositories.

## Configuration PR

When you connect a repository that does not have a Wrangler configuration file, Workers Builds runs `wrangler deploy` which triggers [automatic project configuration](https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/). Instead of failing, it creates a pull request with the necessary configuration for your detected framework.

Note

A configuration PR is only created when your deploy command is `npx wrangler deploy`. If you have a custom deploy command, autoconfig will still run and configure your project, but no PR will be created.

### Why you should merge the PR

Without the configuration in your repository, every build has to run autoconfig first, which means your project gets built twice - once during autoconfig to generate the configuration, and again for the actual deployment. Merging the PR commits the configuration to your repository, so future builds skip autoconfig and go straight to building and deploying. This results in faster deployments and version-controlled settings.

### What the PR includes

![Example of an automatic configuration pull request created by Workers Builds](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1918,height=1348,format=webp/_astro/automatic-pr.CwJG6Bec.png)

The configuration PR may contain changes to the following files, depending on your framework:

  * **`wrangler.jsonc`** \- Wrangler configuration file with your Worker settings
  * **Framework adapter** \- Any required Cloudflare adapter for your framework (for example, `@astrojs/cloudflare` for Astro)
  * **Framework configuration** \- Updates to framework config files (for example, `astro.config.mjs` for Astro or `svelte.config.js` for SvelteKit)
  * **`package.json`** \- New scripts like `deploy`, `preview`, and `cf-typegen`, plus required dependencies
  * **`package-lock.json`** / **`yarn.lock`** / **`pnpm-lock.yaml`** \- Updated lock file with new dependencies
  * **`.gitignore`** \- Entries for `.wrangler` and `.dev.vars*` files
  * **`.assetsignore`** \- For frameworks that generate worker files in the output directory



### PR description

The PR description includes:

  * **Detected settings** \- Framework, build command, deploy command, and version command
  * **Preview link** \- A working preview generated using the detected settings
  * **Next steps** \- Links to documentation for adding bindings, custom domains, and more



Note

When you merge the PR, Workers Builds will update your build and deploy commands if they do not match the detected settings, ensuring successful deployments.

## Name conflict PR

If Workers Builds detects a mismatch between your Worker name in the Cloudflare dashboard and the `name` field in your Wrangler configuration file, it will create a pull request to fix the conflict.

This can happen when:

  * You rename your Worker in the dashboard but not in your config file
  * You connect a repository that was previously used with a different Worker
  * The `name` field in your config does not match the connected Worker



The PR will update the `name` field in your Wrangler configuration to match the Worker name in the dashboard.

For more details, refer to the [name conflict changelog](https://developers.cloudflare.com/changelog/2025-02-20-builds-name-conflict/).

## Reviewing PRs

When you receive a PR from Workers Builds:

  1. **Review the changes** \- Check that the configuration matches your project requirements
  2. **Test the preview** \- Use the preview link in the PR description to verify everything works
  3. **Merge when ready** \- Once satisfied, merge the PR to enable faster deployments



[PreviousConfiguration](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/)[NextOverview](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/builds/automatic-prs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
