---
url: https://developers.cloudflare.com/cf/projects/
title: Develop, build, and deploy \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:47.632727+00:00
---

# Develop, build, and deploy · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/projects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare CLI](https://developers.cloudflare.com/cf/)
  3. /Workers projects



# Develop, build, and deploy

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cf/projects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow cf runs your projectAutomatic configurationStart developmentBuildDeployModesDeploy a prebuilt buildUpload a versionDeploy triggersDeploy a previewProfile Worker startupGenerate typesLocal resource dataWhich configuration each command readsTroubleshooting No dev server is installed Dependencies are not installed Arguments are rejected A framework rejects --mode A prebuilt deploy rejects the mode Build Output is missing Preview output reaches a production deploy The preview name cannot be determined A local command has no local equivalent

`cf` develops, builds, and deploys Workers projects with the same CLI that manages the rest of your Cloudflare account. To create a project, follow [Deploy your first Worker](https://developers.cloudflare.com/cf/get-started/first-worker/).

Configure the project with [`cloudflare.config.ts`](https://developers.cloudflare.com/cf/projects/cloudflare-config/). Builds write Build Output to `.cloudflare/output/v0/`.

## How `cf` runs your project

`cf` does not run a dev server or bundler itself. For `cf dev`, `cf build`, and every other command that builds first, `cf` hands the work to one of these tools:

  1. **The framework's own command.** When `cf` detects a supported framework, it runs that framework's dev or build command through your package manager. In a Vite project, including a project created with `cf init`, that is `vite` or `vite build`, for example `npx vite build` with npm.
  2. **An installed Cloudflare build tool.** Otherwise, `cf` uses the Cloudflare build tool declared in the project's `package.json`. That is the Cloudflare Vite plugin, or Wrangler 4.136.0 or later when the Vite plugin is not declared.



`cf` uses the Cloudflare Vite plugin 2.0 beta (`@cloudflare/vite-plugin@beta`), which does not depend on Wrangler. Wrangler builds projects that declare it without the Vite plugin, such as projects that `cf migrate` converts with the Wrangler bundler and static sites that automatic configuration sets up. These projects keep build settings, such as the static assets directory, in a generated `wrangler.config.ts` file. That file can change during the beta.

`cf` does not run your `package.json` scripts. If your `build` script runs extra steps, such as `tsc -b && vite build`, then `cf build` and `cf deploy` skip them. Chain those steps with `cf build` in your own script instead:

package.jsonjson
    
    
    {
    	"scripts": {
    		"build": "tsc -b && cf build"
    	}
    }

When `cf` runs a framework command, it forwards `--mode` and rejects other arguments. For example, `cf dev --port 8788` fails in a Vite project. Set the option in the framework's configuration, such as `server.port` in `vite.config.ts`, or run the framework command directly. When `cf` uses an installed build tool instead, `cf dev` forwards extra arguments to it, and the tool rejects arguments it does not support. `cf build` accepts only `--mode`.

## Automatic configuration

When a project has no `cloudflare.config.ts`, `cf` tries to detect its framework and set the project up for Cloudflare before it continues. This automatic configuration runs from these commands:

  * `cf dev` and `cf build`
  * `cf deploy`, including `cf deploy --dry-run`
  * `cf previews deploy`
  * `cf workers versions create`, `cf workers triggers deploy`, and `cf workers check`
  * `cf init`



A project counts as configured only when `cloudflare.config.ts` exists in the directory where you run the command. Passing `--prebuilt` skips automatic configuration.

In a terminal, `cf` shows the planned changes and asks before it applies them. Without a terminal, or in CI, it applies the changes and installs packages without asking. Run `cf init .` locally before you set up CI. It configures an existing project without building it. Review the changes and commit them. For the list of changes, refer to [Start from an existing project](https://developers.cloudflare.com/cf/get-started/first-worker/#start-from-an-existing-project).

Wrangler projects

Automatic configuration does not read Wrangler configuration files. In a project that has `wrangler.jsonc`, `wrangler.json`, or `wrangler.toml` but no `cloudflare.config.ts`, do not run `cf init .`, `cf dev`, `cf build`, `cf deploy`, or another command that builds.

In a framework or static-assets project, `cf` writes a new `cloudflare.config.ts` that ignores the Wrangler configuration, including its entrypoint and bindings. In a Worker project without a detected framework, the command fails with an error such as `cloudflare.config.ts is required when --experimental-new-config is enabled.` Convert the project with `cf migrate` first. Refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

## Start development

Start the project's development server:
    
    
    cf dev

The dev server prints its local URL.

## Build

Build the project:
    
    
    cf build

After the build finishes, `cf` reads and validates `.cloudflare/output/v0/`. `cf build` does not upload anything and does not need credentials.

## Deploy

`cf deploy` builds the project, validates Build Output, resolves your credentials and account, uploads a new Worker Version, and deploys it:
    
    
    cf deploy

Sign in with `cf auth login`, or set `CLOUDFLARE_API_TOKEN`, before you deploy. For details, refer to [Sign in](https://developers.cloudflare.com/cf/get-started/#sign-in).

`cf deploy` can provision missing resources for bindings that omit resource identifiers. It does not write provisioned identifiers back to `cloudflare.config.ts`.

`cf deploy` accepts these options:

Option | Purpose  
---|---  
`--dry-run` | Builds and validates the Worker without uploading it  
`--message <TEXT>` | Records a message on the Worker Version  
`--tag <TAG>` | Records a tag on the Worker Version  
`--secrets-file <PATH>` | Uploads secrets from a JSON or `.env` format file with the version  
`--dispatch-namespace <NAMESPACE>` | Deploys a Workers for Platforms user Worker to that dispatch namespace  
`--containers-rollout <STRATEGY>` | Sets the Container rollout strategy: `immediate`, `gradual`, or `none`  
`--worker <NAME>` | Selects a Worker from Build Output instead of the default Worker  
`--prebuilt` | Deploys existing Build Output without building  
  
`--dry-run` sends no API requests and needs no credentials, so you can validate a project before you sign in. In a project without `cloudflare.config.ts`, it still runs automatic configuration first, which can install packages and change files.
    
    
    cf deploy --dry-run
    cf deploy --message "Fix header parsing" --tag v1.2.0

## Modes

A mode selects which configuration a function-form `cloudflare.config.ts` returns. Pass it with `--mode` or `-m`:
    
    
    cf dev --mode staging
    cf build -m staging
    cf deploy --mode staging

When you omit `--mode`, the Cloudflare Vite plugin uses `development` for `cf dev` and `production` for builds. Builds through Wrangler and API commands leave the mode `undefined`. For the full list, refer to [Select a mode](https://developers.cloudflare.com/cf/projects/cloudflare-config/#select-a-mode).

When `cf` runs a framework's own command, only Vite and Astro accept `--mode`. Other framework commands fail with an error. Refer to A framework rejects `--mode`.

This configuration deploys a separate staging Worker with its own API origin:

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { bindings, defineConfig } from "cf/config";

import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };

export default defineConfig(({ mode }) => { (defineConfig, mode reference)

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

`mode`Context valueLink to mode

`mode: string | undefined`

The mode the config is being evaluated in. Set via the `--mode` CLI flag. In Vite the mode defaults to `development` in `vite dev` and `production` in `vite build` ([more info](https://vite.dev/guide/env-and-mode.html#modes)). In Wrangler the mode defaults to `undefined`.

const isStaging = mode === "staging";

return {

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: isStaging ? "example-worker-staging" : "example-worker", (name reference)

`name`RequiredLink to name

`name: string`

The name of your Worker.

entrypoint, (entrypoint reference)

`entrypoint`OptionalLink to entrypoint

`entrypoint?: string | WorkerModule`

The entrypoint module that will be executed. May be either a path string (e.g. `"./src/index.ts"`) or a module namespace imported with the `cf-worker` import attribute.

compatibilityDate: "<COMPATIBILITY_DATE>", (compatibilityDate reference)

`compatibilityDate`RequiredLink to compatibilityDate

`compatibilityDate: string`

A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

env: { (env reference)

`env`OptionalLink to env

`env?: Record<string, Binding>`

Bindings exposed on the Worker's `env` object. Construct entries with `bindings.kv(...)`, `bindings.r2(...)`, etc.

API_ORIGIN: bindings.text( (text reference)

`text`BuilderLink to text

`text<T$1 extends string>(value: T$1): TextBinding<T$1>;`

Inline string value made available to the Worker on `env` under the binding name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables](https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables)

isStaging

? "https://staging-api.example.com"

: "https://api.example.com",

),

},

},

};

});

import { bindings, defineConfig } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig(({ mode }) => { const isStaging = mode === "staging"; return { worker: { name: isStaging ? "example-worker-staging" : "example-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", env: { API_ORIGIN: bindings.text( isStaging ? "https://staging-api.example.com" : "https://api.example.com", ), }, }, }; });

Return one complete configuration for each mode. Programmatic configuration does not merge environment blocks the way Wrangler environments do. A mode deploys a separate Worker only when it returns a different `name`.

Build Output records the mode it was built with. When you deploy an existing build, pass the same mode.

## Deploy a prebuilt build

Pass `--prebuilt` to deploy an existing `.cloudflare/output/v0/` directory without building. One CI job can build, and another can deploy the restored directory. `--prebuilt` also skips automatic configuration.

The deploy command must request the mode that Build Output records:

  * When Build Output records a mode, pass exactly that mode with `--mode`.
  * When Build Output records no mode, do not pass `--mode`.



Vite builds always record a mode. `cf build` without `--mode` records `production`, so deploy that build with `--mode production`:
    
    
    cf build
    cf deploy --prebuilt --mode production

Deploy a staging build with the staging mode:
    
    
    cf build --mode staging
    cf deploy --prebuilt --mode staging

Builds through Wrangler record a mode only when you pass `--mode` to `cf build`. To check the recorded mode, read `buildContext.mode` in `.cloudflare/output/v0/config.json`.

The same rule applies to `--prebuilt` with `cf previews deploy`, `cf workers versions create`, `cf workers triggers deploy`, and `cf workers check`. When the modes do not match, the command stops before it uploads anything and prints the `--mode` value to use.

For a complete pipeline, refer to [Use cf in CI](https://developers.cloudflare.com/cf/ci/).

## Upload a version

Upload a Worker Version without deploying it:
    
    
    cf workers versions create

This command builds and validates the project the same way as `cf deploy`. It accepts `--prebuilt`, `--mode`, `--message`, `--tag`, `--secrets-file`, `--dry-run`, and `--worker`. Use `--preview-alias <ALIAS>` to give the version a [preview URL](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/) alias.

To send traffic to an uploaded version, create a deployment:
    
    
    cf workers deployments create --worker example-worker --strategy percentage --versions '[{"version_id":"<VERSION_ID>","percentage":100}]'

## Deploy triggers

Apply trigger configuration from Build Output without uploading a new version:
    
    
    cf workers triggers deploy

This command applies routes, custom domains, the `workers.dev` setting, cron schedules, Queue consumers, and Workflows. It builds the project unless you pass `--prebuilt`. It also accepts `--mode`, `--worker`, and `--dry-run`. A dry run sends no API requests.

## Deploy a preview

Deploy the project as a Worker Preview:
    
    
    cf previews deploy

The command builds the project with `isPreview` set to `true`, so a function-form `cloudflare.config.ts` can return preview-specific settings. It then uploads the preview and prints the result as JSON. Previews in `cf` can change during the beta.

The preview name defaults to the current branch. `cf` reads the branch from Workers Builds, GitHub Actions, or GitLab CI/CD, and then from Git. On a detached `HEAD` with no CI branch, pass a name:
    
    
    cf previews deploy my-feature

The command accepts `--mode`, `--worker`, and `--prebuilt`. With `--prebuilt`, Build Output must come from a preview build, and the mode rule applies. There is no `--dry-run`, and the command needs credentials.

The JSON result contains `type`, `version`, `preview_id`, `preview_name`, `preview_slug`, `preview_urls`, `deployment_id`, and `deployment_urls`.

Previews do not support Durable Object-managed Containers. `cf deploy`, `cf workers versions create`, and `cf workers triggers deploy` refuse preview Build Output and print the `cf previews deploy` command to use instead.

## Profile Worker startup

Profile the Worker's startup performance locally:
    
    
    cf workers check

The command builds the project unless you pass `--prebuilt`. It prints the bundle size and startup timings as JSON, and writes a CPU profile to `worker-startup.cpuprofile`. Use `--outfile <PATH>` to choose a different file. The command also accepts `--mode` and `--worker`.

The measurement runs on your machine. Use it to find where startup time goes, not to predict startup time on Cloudflare.

## Generate types

Generate TypeScript types from `cloudflare.config.ts`:
    
    
    cf workers types

The command writes `.cloudflare/types/index.d.ts`, which contains the `Env` binding types and the Workers runtime types. Pass `--no-include-runtime` to leave out the runtime types, or `--mode` to evaluate the configuration for a named mode.

The Cloudflare Vite plugin writes the same file during development and builds. Run `cf workers types` in projects that build through Wrangler, or before `tsc` in a type-check script. Projects created with `cf init` include a `typecheck` script that runs `cf workers types && tsc`.

## Local resource data

Add `--local` to a supported command to run it against a local simulation instead of the Cloudflare API:
    
    
    cf d1 raw <DATABASE_ID> --sql "SELECT 1" --local
    cf r2 objects list --bucket-name <BUCKET_NAME> --local

`--local` works only for a few resources that local development provides. `cf` starts a short-lived local runtime for each command, so no dev server needs to be running. Local support covers these commands:

  * `cf kv keys get`, `cf kv keys list`, `cf kv keys put`, and `cf kv keys delete`
  * `cf kv bulk get`, `cf kv bulk put`, and `cf kv bulk delete`
  * `cf d1 raw`
  * `cf d1 migrations list` and `cf d1 migrations apply`
  * `cf r2 objects get`, `cf r2 objects put`, `cf r2 objects list`, and `cf r2 objects bulk-delete`
  * `cf d1 list`, `cf kv namespaces list`, and `cf r2 buckets list`



`cf d1 query` has no local equivalent. Use `cf d1 raw` instead. A command without a local equivalent fails with `This command has no local equivalent.` instead of calling the Cloudflare API.

By default, `--local` keeps its data in a `state/v3` directory inside the `cf` configuration directory. That is `~/.config/cloudflare/state/v3` on Linux and `~/Library/Preferences/cloudflare/state/v3` on macOS. Every project on your machine shares this directory. Pass `--persist-to <DIRECTORY>` to use `<DIRECTORY>/v3` instead. `--persist-to` works only with `--local`.

This is not the data your dev server uses. The Cloudflare Vite plugin 2.0 beta keeps development data in the project, under `.cloudflare/state/`.

## Which configuration each command reads

Project commands, such as `cf dev`, `cf build`, and `cf deploy`, run a build tool that loads the whole `cloudflare.config.ts`, including the Worker and Containers.

Ordinary API commands, such as `cf d1 list`, read only `accountId` and `complianceRegion` from the nearest `cloudflare.config.ts` in the current directory or a parent directory. A syntax error, import error, or top-level runtime error in that file still stops them. For details, refer to [Set account defaults](https://developers.cloudflare.com/cf/projects/cloudflare-config/#set-account-defaults).

API credentials, such as `CLOUDFLARE_API_TOKEN`, can also come from a `.env` file in the current directory. Commands that build first, such as `cf deploy`, load those values after the build finishes. For details, refer to [Load credentials from a .env file](https://developers.cloudflare.com/cf/get-started/#load-credentials-from-a-env-file).

## Troubleshooting

### No dev server is installed
    
    
    No Cloudflare dev-server is installed in this project.

`cf` found no framework that it recognizes and no Cloudflare build tool declared in `package.json`, for example in an empty directory. To create a project, run `cf init`.

### Dependencies are not installed

In a configured project whose dependencies are not installed, Vite reports that it cannot resolve `@cloudflare/vite-plugin`, or `cf` reports that a build tool is declared but not installed. Install dependencies with your package manager, then run the command again.

### Arguments are rejected
    
    
    Arguments cannot currently be forwarded to the detected dev command `npx vite`. Run that command directly with the required arguments.

`cf` runs the framework's command and forwards only `--mode`. Set the option in the framework's configuration, or run the framework command directly.

### A framework rejects `--mode`
    
    
    The detected command `<COMMAND>` does not currently support `--mode`.

Only Vite and Astro accept `--mode` when `cf` runs a framework command. Run the command without `--mode`.

### A prebuilt deploy rejects the mode
    
    
    The Build Output was created with mode "production", but this command did not specify a mode. Rerun with "--mode production".
    
    
    The Build Output does not record which mode it was created with, but this command requested mode "staging". Rebuild with "--mode staging" before deploying.

Pass exactly the mode that Build Output records, or omit `--mode` when it records none. Refer to Deploy a prebuilt build.

### Build Output is missing
    
    
    Build Output Specification: no root config found at <PATH>/.cloudflare/output/v0/config.json.

A `--prebuilt` command found no build. Run `cf build` first, or restore the complete `.cloudflare/output/v0/` directory from your build job.

### Preview output reaches a production deploy
    
    
    This build output is for a Preview. Run cf previews deploy --prebuilt --mode production instead.

The existing Build Output came from `cf previews deploy`. Run the suggested command to deploy the preview, or run `cf build` to create production output.

### The preview name cannot be determined
    
    
    We couldn't determine a Preview name from CI or Git.

`cf previews deploy` found no branch name, for example on a detached `HEAD`. Pass a name: `cf previews deploy <PREVIEW_NAME>`.

### A local command has no local equivalent
    
    
    This command has no local equivalent. Re-run without --local to use the Cloudflare API.

The command does not support `--local`. For D1 queries, use `cf d1 raw` instead of `cf d1 query`. Otherwise, run the command without `--local`.

[PreviousCommand and config mapping](https://developers.cloudflare.com/cf/wrangler/reference/)[Nextcloudflare.config.ts](https://developers.cloudflare.com/cf/projects/cloudflare-config/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/projects/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
