---
url: https://developers.cloudflare.com/cf/get-started/first-worker/
title: Deploy your first Worker \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:46.801805+00:00
---

# Deploy your first Worker · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/get-started/first-worker/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare CLI](https://developers.cloudflare.com/cf/)
  3. /[Get started](https://developers.cloudflare.com/cf/get-started/)
  4. /Deploy a Worker



# Deploy your first Worker

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cf/get-started/first-worker/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin1\. Create a project3\. DeployCreate a project without promptsStart from an existing projectNext steps

This guide creates a [Worker](https://developers.cloudflare.com/workers/) with `cf init`, runs it on your machine, and deploys it to your Cloudflare account.

## Before you begin

[Install `cf`](https://developers.cloudflare.com/cf/get-started/) and check the [requirements](https://developers.cloudflare.com/cf/get-started/#requirements). You do not need to sign in until you deploy.

## 1\. Create a project

Create a project in a new directory:
    
    
    cf init my-worker

`cf init` asks which package manager to use, creates the project in `my-worker`, installs its dependencies, and generates types for its bindings. If you leave out the directory, `cf init` asks for one.

Apart from `node_modules` and the lockfile from the install, `cf init` creates these files:

  * my-worker/ 
    * .cloudflare/ 
      * types/ 
        * index.d.ts
    * src/ 
      * index.ts
    * .gitignore
    * cloudflare.config.ts
    * package.json
    * tsconfig.json
    * vite.config.ts



  * `src/index.ts` is the Worker.
  * `cloudflare.config.ts` describes the Worker in TypeScript.
  * `vite.config.ts` adds the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), which runs your code in the Workers runtime during development and builds it for deployment.
  * `package.json` has `dev`, `build`, and `deploy` scripts that run the matching `cf` commands. It lists `cf` and the Vite plugin 2.0 beta (`@cloudflare/vite-plugin@beta`), which `cf` uses, but not Wrangler.
  * `.cloudflare/types/index.d.ts` holds generated binding and runtime types. The Vite plugin updates it when you run `cf dev` or `cf build`. The generated `.gitignore` excludes `.cloudflare/`.



The Worker reads a `WORLD` binding and returns a greeting:

src/index.jsjs
    
    
    import { env } from "cloudflare:workers";
    
    export default {
    	fetch() {
    		return new Response(`Hello ${env.WORLD}!`);
    	},
    };

src/index.tsts
    
    
    import { env } from "cloudflare:workers";
    
    export default {
    	fetch() {
    		return new Response(`Hello ${env.WORLD}!`);
    	},
    } satisfies ExportedHandler;

`cloudflare.config.ts` names the Worker, points to its entrypoint, and declares the `WORLD` text binding. The annotations explain each field and builder:

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { bindings, defineConfig } from "cf/config";

import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };

export default defineConfig({ (defineConfig reference)

`defineConfig`FunctionLink to defineConfig

`defineConfig<T extends ConfigInput<CloudflareConfig>>(config: T): T;`

Defines the default export of `cloudflare.config.ts`. Pass a configuration object, a promise that resolves to one, or a function that receives the config context (`isPreview` and `mode`) and returns either.

Options (4)

`accountId?: string`
    This is the ID of the account associated with your zone. It can also be specified through the `CLOUDFLARE_ACCOUNT_ID` environment variable.

`complianceRegion?: "public" | "fedramp-high"`
    The compliance boundary in which commands should operate. When omitted, this can be supplied through `CLOUDFLARE_COMPLIANCE_REGION`.

`worker?: ConfigInput<WorkerConfig>`
    The Worker defined by this configuration.

`containers?: ConfigInput<ContainerConfig>[]`
    Container applications defined by this configuration.

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: "my-worker", (name reference)

`name`RequiredLink to name

`name: string`

The name of your Worker.

compatibilityDate: "<COMPATIBILITY_DATE>", (compatibilityDate reference)

`compatibilityDate`RequiredLink to compatibilityDate

`compatibilityDate: string`

A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

entrypoint, (entrypoint reference)

`entrypoint`OptionalLink to entrypoint

`entrypoint?: string | WorkerModule`

The entrypoint module that will be executed. May be either a path string (e.g. `"./src/index.ts"`) or a module namespace imported with the `cf-worker` import attribute.

env: { (env reference)

`env`OptionalLink to env

`env?: Record<string, Binding>`

Bindings exposed on the Worker's `env` object. Construct entries with `bindings.kv(...)`, `bindings.r2(...)`, etc.

WORLD: bindings.text("World"), (text reference)

`text`BuilderLink to text

`text<T$1 extends string>(value: T$1): TextBinding<T$1>;`

Inline string value made available to the Worker on `env` under the binding name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables](https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables)

},

},

});

import { bindings, defineConfig } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "my-worker", compatibilityDate: "<COMPATIBILITY_DATE>", entrypoint, env: { WORLD: bindings.text("World"), }, }, });

`cf init` sets `compatibilityDate` to a fixed, recent date that ships with your version of `cf`. The `cf-worker` import attribute points the configuration at your Worker module. `cf` reads the module path from it and does not load or run your Worker code.

## 2\. Develop locally

Start the development server:
    
    
    cd my-worker
    cf dev

Open the local URL that `cf dev` prints, by default `http://localhost:5173/`. The Worker responds with `Hello World!`.

Change the response in `src/index.ts`, save the file, and refresh the page. The development server picks up the change without a restart.

In this project, `cf dev` does not accept options such as `--port`. To change the port, set `server.port` in `vite.config.ts`.

## 3\. Deploy

  1. If you have not signed in yet, sign in:
         
         cf auth login

  2. Deploy the Worker:
         
         cf deploy

`cf deploy` builds the project, uploads the Worker, deploys it to your account, and prints the result. If you can access more than one account, `cf` asks which one to use. To learn how to set a default, refer to [Select an account](https://developers.cloudflare.com/cf/get-started/#select-an-account).




To check the build without deploying, run `cf deploy --dry-run`. A dry run makes no API requests, so it works before you sign in.

## Create a project without prompts

In a script or CI job, `cf init` cannot ask questions, so pass the directory. Choose the package manager with `--package-manager`, which accepts `npm`, `pnpm`, `yarn`, or `bun`. Without it, `cf init` uses npm, unless you ran `cf` through another package manager:
    
    
    cf init my-worker --package-manager npm

To skip the installation, add `--no-install`. Then run your package manager's install command in the project before you run `cf dev`.

## Start from an existing project

`cf` can also set up an existing app. In the project directory, install its dependencies, then run `cf init .`:
    
    
    cf init .

`cf` detects the framework and shows the settings it found, including the Worker name, framework, build command, and output directory. After you confirm, `cf` changes the project. For a Vite app, it:

  * Installs `cf` and `@cloudflare/vite-plugin` as development dependencies.
  * Adds the Cloudflare plugin to `vite.config.ts`, or creates the file.
  * Creates `cloudflare.config.ts`, with observability turned on.
  * Adds a `deploy` script that runs `cf deploy`.
  * Adds `.wrangler`, `.dev.vars*`, and `.env*` entries to `.gitignore`. In a Git repository without a `.gitignore` file, it creates one.



`cf` does not add `.cloudflare/`, where it writes builds and generated types, to `.gitignore`. Add it yourself:
    
    
    echo ".cloudflare/" >> .gitignore

`cf build` and `cf deploy` run the framework's build command, such as `vite build`, not the `build` script in `package.json`. To keep extra build steps, refer to [How cf runs your project](https://developers.cloudflare.com/cf/projects/#how-cf-runs-your-project).

If you skip `cf init .`, then `cf dev`, `cf build`, and `cf deploy` run the same setup the first time you use them. In CI, they apply the changes without asking, so run `cf init .` locally and commit the result first. For details, refer to [Automatic configuration](https://developers.cloudflare.com/cf/projects/#automatic-configuration).

Plain Vite apps work with this flow. `cf` also detects other frameworks, such as Astro, React Router, and SvelteKit, but detection does not mean the project builds. For example, Astro 6 and later does not build with `cf` during the beta.

Wrangler projects

Do not run `cf init .`, `cf dev`, `cf build`, or `cf deploy` in a project that has a `wrangler.jsonc`, `wrangler.json`, or `wrangler.toml` file. The automatic setup ignores the Wrangler configuration and can produce a Worker that does not match it. To convert a Wrangler project, use `cf migrate` instead. Refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

## Next steps

  * Add storage, queues, or other resources with [bindings](https://developers.cloudflare.com/cf/projects/cloudflare-config/#declare-bindings).
  * Route traffic to your Worker with [triggers](https://developers.cloudflare.com/cf/projects/cloudflare-config/#declare-triggers).
  * Learn how `cf` develops, builds, and deploys projects in [Develop, build, and deploy](https://developers.cloudflare.com/cf/projects/).
  * Explore every configuration option in the [configuration explorer](https://developers.cloudflare.com/cf/projects/config-explorer/).



[PreviousInstall and sign in](https://developers.cloudflare.com/cf/get-started/)[NextManage resources](https://developers.cloudflare.com/cf/get-started/resources/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/get-started/first-worker.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
