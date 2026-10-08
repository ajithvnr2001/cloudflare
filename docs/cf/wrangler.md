---
url: https://developers.cloudflare.com/cf/wrangler/
title: cf for Wrangler users \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:47.544150+00:00
---

# cf for Wrangler users · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/wrangler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare CLI](https://developers.cloudflare.com/cf/)
  3. /Coming from Wrangler



# cf for Wrangler users

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cf/wrangler/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat stays the sameWhat changesUse cf alongside a Wrangler projectRun project commands only after you migrateWhen to migrateHow migration worksWhat still needs Wrangler

If you build with [Wrangler](https://developers.cloudflare.com/workers/wrangler/), most of what you know carries over to `cf`. This page explains what changes, how to use `cf` next to an existing Wrangler project, and when to migrate the project itself.

## What stays the same

Workers, bindings, compatibility dates, versions, and deployments work the same way. When you migrate, `cf migrate` keeps your Worker name, bindings, resource IDs, routes, and triggers. Local secrets in `.dev.vars` keep working under `cf dev`.

## What changes

The main differences between the two tools are:

Area | Wrangler | `cf`  
---|---|---  
Coverage | Workers and a subset of Cloudflare products | The public Cloudflare API, with more than 2,900 commands  
Sign-in | `wrangler login` | `cf auth login`, with its own credentials  
Project configuration | `wrangler.jsonc` or `wrangler.toml` | `cloudflare.config.ts`, written in TypeScript  
Environments | `env` blocks selected with `--env` | Modes selected with `--mode`  
Build | Wrangler's bundler | Wrangler's bundler or the Cloudflare Vite plugin  
Deployable artifact | Internal to Wrangler | Build Output in `.cloudflare/output/v0/`  
Output | Tables for many commands, with `--json` on some | JSON for most API commands  
Resource identifiers | Names for many resources | The IDs that the Cloudflare API expects  
Local and remote data | Some commands default to local data | Remote. `--local` works only for supported KV, D1, and R2 commands  
  
For example, Wrangler accepts a D1 database name, while `cf` expects the database ID:
    
    
    wrangler d1 execute my-database --remote --command "SELECT 1"
    cf d1 query <DATABASE_ID> --sql "SELECT 1"

For the full list of equivalents, refer to [Wrangler to cf reference](https://developers.cloudflare.com/cf/wrangler/reference/).

## Use `cf` alongside a Wrangler project

You do not need to migrate a project to start using `cf`. Resource and account commands, such as `cf d1 list` or `cf r2 buckets list`, work in any directory, including an unmigrated Wrangler project. They do not read the Wrangler configuration file, so they do not use its `account_id`. Set `CLOUDFLARE_ACCOUNT_ID` or choose an account when `cf` asks. For details, refer to [Select an account](https://developers.cloudflare.com/cf/get-started/#select-an-account).

Until you migrate the project, keep using Wrangler for development and deployment, such as `wrangler dev` and `wrangler deploy`. Use `cf` for account and resource tasks, including products that Wrangler does not cover.

`cf` does not reuse your Wrangler login. Before you run `cf` for the first time, [install it and sign in](https://developers.cloudflare.com/cf/get-started/). In automation, both tools read `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.

## Run project commands only after you migrate

`cf dev`, `cf build`, and `cf deploy` read `cloudflare.config.ts`. They do not read `wrangler.jsonc` or `wrangler.toml`. In a Wrangler project that you have not migrated, the result depends on the project:

Project | Result  
---|---  
A Worker without a framework or static assets | The command fails with `cloudflare.config.ts is required when --experimental-new-config is enabled.` and a stack trace.  
A Worker that uses the Cloudflare Vite plugin | Automatic configuration writes a new `cloudflare.config.ts` for a single-page application, without your entrypoint or bindings. In a project without `index.html`, `cf build` fails with `Cannot resolve entry module index.html`, and `cf dev` returns `404` responses.  
A Worker with a static assets directory that contains `index.html` | Automatic configuration treats the project as a static site and writes `cloudflare.config.ts` and `wrangler.config.ts`. `cf build` succeeds, but the result is a static assets Worker named after `package.json`, without your Worker code or bindings.  
  
When automatic configuration runs, it also changes `package.json`, including the `deploy` script. It can also change the lockfile, `.gitignore`, and `vite.config.ts`. Without a terminal, such as in CI, it makes these changes without asking for confirmation.

Caution

Do not run `cf dev`, `cf build`, or `cf deploy` in a Wrangler project, including from CI, until you have run `cf migrate`.

If one of these commands already ran in the project, undo its changes before you migrate:

  1. Run `git status` to list the changed and new files.
  2. Restore each changed file, for example with `git restore package.json`.
  3. Delete each new file that `git status` lists, such as `cloudflare.config.ts`, `wrangler.config.ts`, and the `.cloudflare/` directory.
  4. Run `cf migrate`. It does not run while `cloudflare.config.ts` exists.



## When to migrate

Migrate a project when you want to:

  * Write configuration in TypeScript, with binding types inferred from it.
  * Use one CLI for project, account, and resource tasks.
  * Build once and deploy the same Build Output later, for example from CI.



Keep a project on Wrangler for now if it relies on a task listed in What still needs Wrangler.

## How migration works

`cf migrate` reads the Wrangler configuration file and writes `cloudflare.config.ts` beside it. It converts bindings, routes, triggers, and environments, and adds `cf` to the project as a development dependency. It keeps Wrangler's bundler unless the project already uses the Cloudflare Vite plugin, so you do not need to adopt Vite to migrate.

Preview the changes, then run the migration:
    
    
    cf migrate --dry-run
    cf migrate

Some settings need manual work afterwards, such as Durable Object migrations, Workflows, Containers, and package scripts. `cf migrate` lists each item and marks it in the generated file. For Workflows and Containers, refer to [Workflows and Containers](https://developers.cloudflare.com/cf/wrangler/migrate/#workflows-and-containers). For the complete procedure, refer to [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/).

## What still needs Wrangler

`cf` is in beta and does not yet cover every Wrangler task:

  * **Live logs** : `cf` cannot stream live logs yet. Run `npx wrangler tail <WORKER_NAME>` instead of installing Wrangler.
  * **Single secrets** : `cf` cannot set a single secret yet. For options, refer to [Commands not yet supported](https://developers.cloudflare.com/cf/wrangler/reference/#commands-not-yet-supported).



Wrangler does not read `cloudflare.config.ts`. If you still run Wrangler commands in a migrated project, keep the Wrangler configuration file until you no longer need them.

[PreviousManage resources](https://developers.cloudflare.com/cf/get-started/resources/)[NextMigrate a project](https://developers.cloudflare.com/cf/wrangler/migrate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/wrangler/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
