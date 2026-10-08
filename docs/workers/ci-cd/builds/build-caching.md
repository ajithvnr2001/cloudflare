---
url: https://developers.cloudflare.com/workers/ci-cd/builds/build-caching/
title: Build caching \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:11.819191+00:00
---

# Build caching · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/ci-cd/builds/build-caching/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[CI/CD](https://developers.cloudflare.com/workers/ci-cd/)

  4. /[Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  5. /Build caching



# Build caching

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/ci-cd/builds/build-caching/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAbout build cache Package managers Frameworks LimitsEnable build cacheClear build cache

Improve Workers build times by caching dependencies and build output between builds with a project-wide shared cache.

The first build to occur after enabling build caching on your Workers project will save relevant artifacts to cache. Every subsequent build will restore from cache unless configured otherwise.

## About build cache

When enabled, build caching will automatically detect which package manager and framework the project is using from its `package.json` and cache data accordingly for the build.

The following shows which package managers and frameworks are supported for dependency and build output caching respectively.

### Package managers

Workers build cache will cache the global cache directories of the following package managers:

Package Manager | Directories cached  
---|---  
[npm ↗︎](https://www.npmjs.com/) | `.npm`  
[yarn ↗︎](https://yarnpkg.com/) | `.cache/yarn`  
[pnpm ↗︎](https://pnpm.io/) | `.pnpm-store`, `.local/share/pnpm/store`  
[bun ↗︎](https://bun.sh/) | `.bun/install/cache`  
  
If you configure pnpm to use a different store directory, Workers Builds does not cache it.

### Frameworks

Some frameworks provide a cache directory that is typically populated by the framework with intermediate build outputs or dependencies during build time. Workers Builds will automatically detect the framework you are using and cache this directory for reuse in subsequent builds.

The following frameworks support build output caching:

Framework | Directories cached  
---|---  
Astro | `node_modules/.astro`  
Docusaurus | `node_modules/.cache`, `.docusaurus`, `build`  
Eleventy | `.cache`  
Gatsby | `.cache`, `public`  
Next.js | `.next/cache`  
Nuxt | `node_modules/.cache/nuxt`  
SvelteKit | `node_modules/.cache/imagetools`  
  
Note

[Static assets](https://developers.cloudflare.com/workers/static-assets/) and [frameworks](https://developers.cloudflare.com/workers/framework-guides/) are now supported in Cloudflare Workers.

### Limits

The following limits are imposed for build caching:

  * **Retention** : Cache is purged 7 days after its last read date. Unread cache artifacts are purged 7 days after creation.
  * **Storage** : Every project is allocated 10 GB. If the project cache exceeds this limit, the project will automatically start deleting artifacts that were read least recently.



## Enable build cache

To enable build caching:

  1. Navigate to [Workers & Pages Overview ↗︎](https://dash.cloudflare.com) on the Dashboard.
  2. Find your Workers project.
  3. Go to **Settings** > **Build** > **Build cache**.
  4. Select **Enable** to turn on build caching.



## Clear build cache

The build cache can be cleared for a project when needed, such as when debugging build issues. To clear the build cache:

  1. Navigate to [Workers & Pages Overview ↗︎](https://dash.cloudflare.com) on the Dashboard.
  2. Find your Workers project.
  3. Go to **Settings** > **Build** > **Build cache**.
  4. Select **Clear Cache** to clear the build cache.



[PreviousBuild image](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/)[NextBuild branches](https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/ci-cd/builds/build-caching.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
