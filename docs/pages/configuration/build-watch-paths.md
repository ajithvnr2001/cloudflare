---
url: https://developers.cloudflare.com/pages/configuration/build-watch-paths/
title: Build watch paths \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:28.630365+00:00
---

# Build watch paths · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/configuration/build-watch-paths/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Configuration
  4. /Build watch paths



# Build watch paths

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/pages/configuration/build-watch-paths/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure pathsExamples Trigger builds for specific directories (monorepo) Exclude a directory from triggering builds Trigger builds for a specific filetype Trigger builds for a directory but exclude a subdirectory

When you connect a git repository to Pages, by default a change to any file in the repository will trigger a Pages build. You can configure Pages to include or exclude specific paths to specify if Pages should skip a build for a given path. This can be especially helpful if you are using a monorepo project structure and want to limit the amount of builds being kicked off.

## Configure paths

To configure which paths are included and excluded:

  1. Go to the **Workers & Pages** in the Cloudflare dashboard.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Find your Pages project.

  3. Go to **Settings** > **Build** > **Build watch paths**. Pages will default to setting your project's includes paths to everything ([*]) and excludes paths to nothing (`[]`).




The configuration fields can be filled in two ways:

  * **Static filepaths** : Enter the precise name of the file you are looking to include or exclude (for example, `docs/README.md`).
  * **Wildcard syntax:** Use wildcards to match multiple paths. You can specify wildcards at the start or end of your rule.



Wildcard syntax

A wildcard (`*`) matches zero or more characters, **including path separators (`/`)**. This means a single `*` at the end of a path pattern will match files in nested subdirectories as well. For example:

  * `docs/*` matches `docs/README.md`, `docs/guides/setup.md`, and `docs/guides/advanced/config.md`.
  * `*.md` matches `README.md`, `docs/README.md`, and `src/content/guide.md`.
  * `*` alone matches all files in the repository.



For each path in a push event, build watch paths will be evaluated as follows:

  * Paths satisfying excludes conditions are ignored first
  * Any remaining paths are checked against includes conditions
  * If any matching path is found, a build is triggered. Otherwise the build is skipped



Pages will bypass the path matching for a push event and default to building the project if:

  * A push event contains 0 file changes, in case a user pushes an empty push event to trigger a build
  * A push event contains 3000+ file changes or 20+ commits



## Examples

### Trigger builds for specific directories (monorepo)

If you want to trigger a build only when files change within specific directories, such as `project-a/` and `packages/`. Because `*` matches across path separators, this includes changes in nested subdirectories like `project-a/src/index.js` or `packages/utils/lib/helpers.ts`.

  * Include paths: `project-a/*, packages/*`
  * Exclude paths: ``



### Exclude a directory from triggering builds

If you want to trigger a build for any changes, but want to exclude changes to a certain directory, such as all changes in a `docs/` directory (including nested paths like `docs/guides/setup.md`).

  * Include paths: `*`
  * Exclude paths: `docs/*`



### Trigger builds for a specific filetype

If you want to trigger a build for a specific file or specific filetype, for example all `.md` files anywhere in the repository.

  * Include paths: `*.md`
  * Exclude paths: ``



### Trigger builds for a directory but exclude a subdirectory

If you want to trigger a build for changes in `src/` but want to ignore changes in `src/tests/`.

  * Include paths: `src/*`
  * Exclude paths: `src/tests/*`



[PreviousBuild image](https://developers.cloudflare.com/pages/configuration/build-image/)[NextCustom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/configuration/build-watch-paths.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
