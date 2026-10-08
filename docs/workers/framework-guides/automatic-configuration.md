---
url: https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/
title: Deploy an existing project \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:27.129298+00:00
---

# Deploy an existing project · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Framework guides
  4. /Deploy an existing project



# Deploy an existing project

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksSupported frameworksFiles created and modified wrangler.jsonc package.json .gitignore .assetsignoreUsing automatic configuration Deploy with automatic configuration Configure without deploying Preview changes with dry runNon-interactive modeImporting a repository from the dashboardSkipping automatic configurationNext.js configurationTroubleshooting Multiple frameworks detected Framework not detected Configuration already exists Workspaces

Wrangler can automatically detect your framework and configure your project for Cloudflare Workers. This allows you to deploy existing projects with a single command, without manually setting up configuration files or installing adapters.

Note

Minimum required Wrangler version: **4.68.0**. Check your version by running `wrangler --version`. To update Wrangler, refer to [Install/Update Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/).

## How it works

When you run `wrangler deploy` or `wrangler setup` in a project directory without a Wrangler configuration file, Wrangler will:

  1. **Detect your framework** \- Analyzes your project to identify the framework you're using
  2. **Prompt for confirmation** \- Shows the detected settings and asks you to confirm before making changes
  3. **Install adapters** \- Installs any required Cloudflare adapters for your framework
  4. **Generate configuration** \- Creates a `wrangler.jsonc` file with appropriate settings
  5. **Update package.json** \- Adds helpful scripts like `deploy`, `preview`, and `cf-typegen`
  6. **Configure git** \- Adds Wrangler-specific entries to `.gitignore`



## Supported frameworks

Automatic configuration supports the following frameworks:

Framework | Adapter/Tool | Notes  
---|---|---  
[Next.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) | `vinext` | Configures vinext for Cloudflare Workers and adds the required Vite and Wrangler configuration.  
[Astro](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/) | `@astrojs/cloudflare` | Runs `astro add cloudflare` automatically  
[SvelteKit](https://developers.cloudflare.com/workers/framework-guides/web-apps/sveltekit/) | `@sveltejs/adapter-cloudflare` | Runs `sv add sveltekit-adapter` automatically  
[Nuxt](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/nuxt/) | Built-in Cloudflare preset |   
[React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/) | Cloudflare Vite plugin |   
[Solid Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/solid/) | Built-in Cloudflare preset |   
[TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/) | Cloudflare Vite plugin |   
[Angular](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/angular/) |  |   
[Analog](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/analog/) | Built-in Cloudflare preset |   
[Vite](https://developers.cloudflare.com/workers/vite-plugin/) | Cloudflare Vite plugin |   
[Vike](https://developers.cloudflare.com/workers/framework-guides/web-apps/vike/) |  |   
[Waku](https://developers.cloudflare.com/workers/framework-guides/web-apps/more-web-frameworks/waku/) |  |   
Static sites | None | Any directory with an `index.html`  
  
Automatic configuration may also work with other projects, such as React or Vue SPAs. Try running `wrangler deploy` or `wrangler setup` to see if your project is detected.

## Files created and modified

When automatic configuration runs, the following files may be created or modified:

### `wrangler.jsonc`

A new Wrangler configuration file is created with settings appropriate for your framework:
    
    
    {
    	"$schema": "node_modules/wrangler/config-schema.json",
    	"name": "my-project",
    	"main": "dist/_worker.js/index.js",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": ["nodejs_compat"],
    	"assets": {
    		"binding": "ASSETS",
    		"directory": "dist",
    	},
    	"observability": {
    		"enabled": true,
    	},
    }
    
    
    "$schema" = "node_modules/wrangler/config-schema.json"
    name = "my-project"
    main = "dist/_worker.js/index.js"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "nodejs_compat" ]
    
    [assets]
    binding = "ASSETS"
    directory = "dist"
    
    [observability]
    enabled = true

The exact configuration varies based on your framework.

### `package.json`

New scripts are added to your `package.json`:
    
    
    {
    	"scripts": {
    		"deploy": "npm run build && wrangler deploy",
    		"preview": "npm run build && wrangler dev",
    		"cf-typegen": "wrangler types"
    	}
    }

### `.gitignore`

Wrangler-specific entries are added:
    
    
    # wrangler files
    .wrangler
    .dev.vars*
    !.dev.vars.example

### `.assetsignore`

For frameworks that generate worker files in the output directory, an `.assetsignore` file is created to exclude them from static asset uploads:
    
    
    _worker.js
    _routes.json

## Using automatic configuration

### Deploy with automatic configuration

To deploy an existing project, run [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy) in your project directory:

npmyarnpnpm
    
    
    npx wrangler deploy
    
    
    yarn wrangler deploy
    
    
    pnpm wrangler deploy

Wrangler will detect your framework, show the configuration it will apply, and prompt you to confirm before making changes and deploying.

### Configure without deploying

To configure your project without deploying, use [`wrangler setup`](https://developers.cloudflare.com/workers/wrangler/commands/general/#setup):

npmyarnpnpm
    
    
    npx wrangler setup
    
    
    yarn wrangler setup
    
    
    pnpm wrangler setup

This is useful when you want to review the generated configuration before deploying.

### Preview changes with dry run

To see what changes would be made without actually modifying any files:

npmyarnpnpm
    
    
    npx wrangler setup --dry-run
    
    
    yarn wrangler setup --dry-run
    
    
    pnpm wrangler setup --dry-run

This outputs a summary of the configuration that would be generated.

## Non-interactive mode

To skip the confirmation prompts, use the [`--yes` flag](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy):

npmyarnpnpm
    
    
    npx wrangler deploy --yes
    
    
    yarn wrangler deploy --yes
    
    
    pnpm wrangler deploy --yes

This applies the configuration automatically using sensible defaults. This is useful in CI/CD environments or when you want to accept the detected settings without reviewing them.

## Importing a repository from the dashboard

When you import a GitHub or GitLab repository via the Cloudflare dashboard, autoconfig runs non-interactively. If your repository does not have a Wrangler configuration file, [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) will create a pull request with the necessary configuration.

The PR includes all the configuration changes described above. A preview deployment is generated so you can test the changes before merging. Once merged, your project is ready for deployment.

For more details, refer to [Automatic pull requests](https://developers.cloudflare.com/workers/ci-cd/builds/automatic-prs/).

## Skipping automatic configuration

If you do not want automatic configuration to run, ensure you have a valid Wrangler configuration file (`wrangler.toml`, `wrangler.json`, or `wrangler.jsonc`) in your project before running `wrangler deploy`.

You can also manually configure your project by following the framework-specific guides in the [Framework guides](https://developers.cloudflare.com/workers/framework-guides/).

## Next.js configuration

For Next.js projects, automatic configuration uses [vinext](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) as the default deployment path for Cloudflare Workers. The generated configuration adds the vinext and Vite dependencies, creates the Cloudflare Workers configuration, and adds package scripts for development, builds, and deployment.

vinext supports Next.js caching features such as Incremental Static Regeneration (ISR), `"use cache"`, and `unstable_cache`. For production applications, configure the generated Workers project with the cache backend your application requires. For more information, refer to [vinext caching ↗︎](https://github.com/cloudflare/vinext#caching).

If you need the OpenNext adapter instead of vinext, configure it manually by following the [OpenNext adapter guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/).

## Troubleshooting

### Multiple frameworks detected

When you import a repository via [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) in the Cloudflare dashboard, automatic configuration will fail if your project contains multiple frameworks. To resolve this, set the [root directory](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/#build-settings) to the path containing only one framework. For monorepos, refer to [monorepo setup](https://developers.cloudflare.com/workers/ci-cd/builds/advanced-setups/#monorepos).

When running `wrangler deploy` or `wrangler setup` locally, Wrangler will prompt you to select which framework to use if multiple frameworks are detected.

### Framework not detected

If your framework is not detected, ensure your `package.json` includes the framework as a dependency.

### Configuration already exists

If a Wrangler configuration file already exists, automatic configuration will not run. To reconfigure your project, delete the existing configuration file and run `wrangler deploy` or `wrangler setup` again.

### Workspaces

Support for monorepos and npm/yarn/pnpm workspaces is currently limited. Wrangler analyzes the project directory where you run the command, but does not detect dependencies installed at the workspace root. This can cause framework detection to fail if the framework is listed as a dependency in the workspace's root `package.json` rather than in the individual project's `package.json`.

If you encounter issues, report them in the [Wrangler GitHub repository ↗︎](https://github.com/cloudflare/workers-sdk/issues/new/choose).

[PreviousMigrate from Vercel to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/vercel-to-workers/)[NextReact + Vite](https://developers.cloudflare.com/workers/framework-guides/web-apps/react/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/framework-guides/automatic-configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
