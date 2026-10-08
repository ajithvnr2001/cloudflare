---
url: https://developers.cloudflare.com/cf/wrangler/reference/
title: Wrangler to cf reference \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:48.251724+00:00
---

# Wrangler to cf reference · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/wrangler/reference/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare CLI](https://developers.cloudflare.com/cf/)
  3. /[Coming from Wrangler](https://developers.cloudflare.com/cf/wrangler/)
  4. /Command and config mapping



# Wrangler to cf reference

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cf/wrangler/reference/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCommands Commands not yet supportedConfiguration fieldsBuild settingsConvert environments to modesConvert Durable Object migrationsComplete example

`cf migrate` converts a Wrangler project to `cf` for you. It writes `cloudflare.config.ts` from the Wrangler configuration file, adds `cf` to the project, and lists the items that you finish by hand. Start with [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/), then use this page to understand what `cf migrate` changed or to finish a conversion by hand.

## Commands

Most Wrangler commands have a `cf` equivalent, although the command name and arguments can differ. For example, Worker versions and deployments are under `cf workers versions` and `cf workers deployments`.

To find the `cf` command for a task, use any of the following:

  * **Search** : describe the task to `cf cli search`, then inspect the match with `cf schema`:
        
        cf cli search "create a D1 database"
        cf schema d1 create

  * **Help** : add `--help` to a command group, such as `cf d1 --help`, to list its commands and options.

  * **Coding agent** : ask your agent for the `cf` equivalent of a Wrangler command. To set up your agent, refer to [Use cf with coding agents](https://developers.cloudflare.com/cf/agents/).




Resource commands in `cf` take the identifiers that the Cloudflare API expects, such as a D1 database ID rather than its name. They act on remote resources. `--local` works only for a few resources that local development provides, such as KV keys, D1 through `cf d1 raw`, `cf d1 migrations list`, and `cf d1 migrations apply`, and R2 objects. For the full list, refer to [Local resource data](https://developers.cloudflare.com/cf/projects/#local-resource-data). Commands without a local equivalent, such as `cf d1 query`, return an error.

### Commands not yet supported

`cf` is in beta, and some Wrangler commands are not supported yet. Run these with `npx wrangler` instead of installing Wrangler. Wrangler does not read `cloudflare.config.ts`, so pass the Worker name.

  * **`wrangler tail`** : `cf` cannot stream live logs yet. Run:
        
        npx wrangler tail <WORKER_NAME>

  * **`wrangler secret put`** : `cf` cannot set a single secret yet. Run `npx wrangler secret put <SECRET_NAME> --name <WORKER_NAME>`, or upload secrets with a new Worker version by passing `--secrets-file <PATH>` to `cf deploy` or `cf workers versions create`.




## Configuration fields

`cf migrate` converts Wrangler fields as the following table shows. Worker settings go under `worker` in `cloudflare.config.ts`, and bindings go under `worker.env`. A required item is a follow-up that you resolve by hand, as described in [Resolve follow-up items](https://developers.cloudflare.com/cf/wrangler/migrate/#resolve-follow-up-items).

Wrangler field | `cloudflare.config.ts` | Notes  
---|---|---  
`name` | `worker.name` | —  
`main` | `worker.entrypoint` | Written as a string path. You can replace it with a `cf-worker` import.  
`compatibility_date` | `worker.compatibilityDate` | —  
`compatibility_flags` | `worker.compatibilityFlags` | —  
`account_id` | `accountId` | Top level  
`compliance_region` | `complianceRegion` | Top level. `fedramp_high` becomes `fedramp-high`.  
`vars` | `bindings.text()` or `bindings.json()` | Strings use `text()`. Other values use `json()`.  
`secrets.required` | `bindings.secret()` | —  
KV, D1, R2, Hyperdrive, and other bindings | The matching `bindings` builder | Preview resource fields are a required item.  
`services` | `bindings.worker({ worker })` | A legacy service environment is a required item.  
`queues.producers` | `bindings.queue({ name })` | —  
`queues.consumers` | `triggers.queue({ name })` | Consumer settings become camelCase options, such as `maxBatchSize`.  
Hyperdrive `localConnectionString` | `dev: { connectionString }` on `bindings.hyperdrive()` | —  
`remote: true` on a binding | `dev: { remote: true }` | —  
`routes` with `zone_name` | `triggers.fetch({ pattern, zone })` | —  
`routes` with `zone_id` | `triggers.fetch({ pattern, zone })` | Required item. `zone` accepts a zone name or a zone ID.  
`routes` with `custom_domain: true` | `worker.domains` | —  
`triggers.crons` | `triggers.scheduled({ schedule })` | —  
`durable_objects.bindings` | `bindings.durableObject({ worker, exportName })` | Required item. Review each binding.  
`migrations` | `worker.exports` | Not converted. Refer to Convert Durable Object migrations.  
`workflows` | `bindings.workflow()` and `exports.workflow()` | Required item. Refer to [Workflows](https://developers.cloudflare.com/cf/projects/cloudflare-config/#declare-exports).  
`containers` | `defineContainer()` in top-level `containers` | Required item. Refer to [Containers](https://developers.cloudflare.com/cf/projects/cloudflare-config/#attach-a-container).  
`assets.binding` | `bindings.assets()` | —  
`assets.html_handling`, `not_found_handling`, `run_worker_first` | `worker.assets` | Keys become camelCase, such as `notFoundHandling`.  
`assets.directory` | Build settings | Refer to Build settings.  
`observability` | `worker.observability` | Keys become camelCase, such as `headSamplingRate`.  
`limits` | `worker.limits` | Keys become camelCase, such as `cpuMs`.  
`placement` | `worker.placement` | —  
`tail_consumers` | `worker.tailConsumers` | —  
`streaming_tail_consumers` | `worker.tailConsumers` | Each entry gets `streaming: true`.  
`workers_dev` | `worker.workersDev` | —  
`preview_urls` | `worker.previewUrls` | —  
`env.<NAME>` | A `case` in `switch (ctx.mode)` | Refer to Convert environments to modes.  
`previews` | A branch on `ctx.isPreview` | Required item. Review the branch.  
`site` | — | Not supported. Move the site to [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/).  
D1 `migrations_dir`, `migrations_pattern`, `migrations_table` | — | Pass `--dir`, `--pattern`, and `--table` to `cf d1 migrations apply`.  
`build`, `minify`, `alias`, and other build fields | Build settings | Refer to Build settings.  
  
For every field and builder, refer to [Programmatic configuration](https://developers.cloudflare.com/cf/projects/cloudflare-config/) and the [Configuration explorer](https://developers.cloudflare.com/cf/projects/config-explorer/).

## Build settings

Build settings do not go in `cloudflare.config.ts`. Where they go depends on the bundler:

Wrangler field | Vite bundler: `vite.config.ts` | Wrangler bundler: `wrangler.config.ts`  
---|---|---  
`alias` | `resolve.alias` | `alias`  
`define` | `define` | `define`  
`minify` | `build.minify` | `minify`  
`upload_source_maps` | `build.sourcemap` in the Worker's Vite environment | `uploadSourceMaps`  
`assets.directory` | `publicDir` | `assetsDirectory`  
`build` | Run the command yourself before `cf build` | `build`, with camelCase keys  
`dev` | `server` options | `dev`, with camelCase keys  
`rules`, `tsconfig`, `no_bundle`, `find_additional_modules`, `base_dir`, `preserve_file_names` | Not used. Vite handles module resolution and bundling. | camelCase keys, such as `noBundle` and `baseDir`  
  
With the Wrangler bundler, `cf migrate` writes these settings to `wrangler.config.ts` for you and adds `types: { generate: false }`. With the Vite bundler, it lists the fields in a required item for you to move. `wrangler.config.ts` is experimental and can change during the beta.

## Convert environments to modes

Wrangler environments inherit some top-level fields. `cloudflare.config.ts` does not merge environments. It returns one complete configuration for each mode instead. `cf migrate` writes a `switch (ctx.mode)` statement with one `case` for each environment. For the generated shape, refer to [Environments](https://developers.cloudflare.com/cf/wrangler/migrate/#environments).

Replace `--env <NAME>` with `--mode <NAME>` on project commands, such as `cf dev`, `cf build`, `cf deploy`, `cf workers versions create`, and `cf workers triggers deploy`.

Without `--mode`, the mode depends on the command and the bundler:

Command | Vite bundler | Wrangler bundler  
---|---|---  
`cf dev` | `development` | `undefined`  
`cf build` and `cf deploy` | `production` | `undefined`  
API commands, such as `cf d1 list` | `undefined` | `undefined`  
  
API commands evaluate `cloudflare.config.ts` only to read `accountId` and `complianceRegion`. If `accountId` depends on the mode, a Vite build and an API command can resolve different accounts. Keep `accountId` independent of the mode, or pass the same `--mode` to every command.

For more information, refer to [Modes](https://developers.cloudflare.com/cf/projects/#modes).

## Convert Durable Object migrations

`worker.exports` replaces the ordered `migrations` history. `cf migrate` does not convert it.

On the first deployment that switches from `migrations` to `worker.exports`, declare every class whose namespace is live today. Use `storage: "sqlite"` or `storage: "legacy-kv"` to match its existing storage.

Do not copy the full migration history. Omit rename and delete operations that have already been applied. If you add them, they become stale tombstones that the deployment reports as safe to remove.

Add a tombstone only for a lifecycle change that has not been applied yet:

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { defineConfig, exports } from "cf/config";

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

name: "orders-api", (name reference)

`name`RequiredLink to name

`name: string`

The name of your Worker.

entrypoint, (entrypoint reference)

`entrypoint`OptionalLink to entrypoint

`entrypoint?: string | WorkerModule`

The entrypoint module that will be executed. May be either a path string (e.g. `"./src/index.ts"`) or a module namespace imported with the `cf-worker` import attribute.

compatibilityDate: "2026-08-24", (compatibilityDate reference)

`compatibilityDate`RequiredLink to compatibilityDate

`compatibilityDate: string`

A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

Counter: exports.durableObject({ storage: "sqlite" }), (durableObject, storage reference)

`durableObject`BuilderLink to durableObject

`durableObject<TContainer extends ContainerDefinition | undefined = undefined>(options: DurableObjectCreatedExportOptions<TContainer>): DurableObjectCreatedExport<TContainer>;`

Declares a Durable Object class defined by this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects) For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects)

Options (4)

`state?: "created"`
    

`storage: "sqlite"`
    Selects the SQLite-backed storage engine (recommended for new classes).

`container?: TContainer`
    Attach a Container application to this Durable Object by config reference.

`storage: "legacy-kv"`
    Selects the legacy key-value storage engine.

`storage`RequiredLink to storage

`storage: "sqlite" | "legacy-kv"`

Selects the SQLite-backed storage engine (recommended for new classes). Selects the legacy key-value storage engine.

OldCounter: exports.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject(options: DurableObjectRenamedExportOptions): DurableObjectRenamedExport;`

Rename a provisioned Durable Object namespace's class.

Options (2)

`state: "renamed"`
    

`renamedTo: string`
    The destination class name. Must be a valid JavaScript identifier and must appear as a live (`state: "created"`) `durableObject` entry in the same `exports` map.

state: "renamed", (state reference)

`state`RequiredLink to state

`state: "renamed"`

The type definition does not include a description.

renamedTo: "Counter", (renamedTo reference)

`renamedTo`RequiredLink to renamedTo

`renamedTo: string`

The destination class name. Must be a valid JavaScript identifier and must appear as a live (`state: "created"`) `durableObject` entry in the same `exports` map.

}),

UnusedCounter: exports.durableObject({ state: "deleted" }), (durableObject, state reference)

`durableObject`BuilderLink to durableObject

`durableObject(options: DurableObjectDeletedExportOptions): DurableObjectDeletedExport;`

Retire a provisioned Durable Object namespace whose class has been removed from code.

Options (1)

`state: "deleted"`
    

`state`RequiredLink to state

`state: "deleted"`

The type definition does not include a description.

},

},

});

import { defineConfig, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "orders-api", entrypoint, compatibilityDate: "2026-08-24", exports: { Counter: exports.durableObject({ storage: "sqlite" }), OldCounter: exports.durableObject({ state: "renamed", renamedTo: "Counter", }), UnusedCounter: exports.durableObject({ state: "deleted" }), }, }, });

Keep a tombstone until a deployment response reports that it is stale, then remove it. Use `cf deploy`, rather than a version upload, for a version that creates, deletes, renames, or transfers a Durable Object class. You cannot roll back a Durable Object lifecycle change to a version from before the change.

For transfers between Workers and the full list of states, refer to [Manage Durable Object lifecycle](https://developers.cloudflare.com/cf/projects/cloudflare-config/#manage-durable-object-lifecycle).

## Complete example

This example finishes the migration of `orders-api`, the Worker used in [Migrate a Wrangler project](https://developers.cloudflare.com/cf/wrangler/migrate/). It has a D1 database, a queue, a cron trigger, a route, and a Durable Object. After `cf migrate` and the follow-up steps, `cloudflare.config.ts` is:

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { bindings, defineConfig, exports, triggers } from "cf/config";

import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };

type Job = { orderId: string };

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

accountId: "<ACCOUNT_ID>", (accountId reference)

`accountId`OptionalLink to accountId

`accountId?: string`

This is the ID of the account associated with your zone. It can also be specified through the `CLOUDFLARE_ACCOUNT_ID` environment variable.

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: "orders-api", (name reference)

`name`RequiredLink to name

`name: string`

The name of your Worker.

entrypoint, (entrypoint reference)

`entrypoint`OptionalLink to entrypoint

`entrypoint?: string | WorkerModule`

The entrypoint module that will be executed. May be either a path string (e.g. `"./src/index.ts"`) or a module namespace imported with the `cf-worker` import attribute.

compatibilityDate: "2026-08-24", (compatibilityDate reference)

`compatibilityDate`RequiredLink to compatibilityDate

`compatibilityDate: string`

A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

compatibilityFlags: ["nodejs_compat"], (compatibilityFlags reference)

`compatibilityFlags`OptionalLink to compatibilityFlags

`compatibilityFlags?: string[]`

A list of flags that enable features from upcoming features of the Workers runtime, usually used together with `compatibilityDate`. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-flags/](https://developers.cloudflare.com/workers/configuration/compatibility-flags/)

Default: `[]`

env: { (env reference)

`env`OptionalLink to env

`env?: Record<string, Binding>`

Bindings exposed on the Worker's `env` object. Construct entries with `bindings.kv(...)`, `bindings.r2(...)`, etc.

ENVIRONMENT: bindings.text("production"), (text reference)

`text`BuilderLink to text

`text<T$1 extends string>(value: T$1): TextBinding<T$1>;`

Inline string value made available to the Worker on `env` under the binding name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables](https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables)

DB: bindings.d1({ (d1 reference)

`d1`BuilderLink to d1

`d1(options?: D1BindingOptions): D1Binding;`

Binding to a D1 database. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#d1-databases](https://developers.cloudflare.com/workers/wrangler/configuration/#d1-databases)

Options (3)

`id?: string`
    The UUID of this D1 database (not required).

`name?: string`
    The name of this D1 database.

`dev?: BindingDevOptions`
    Options that only apply during local development.

name: "orders-db", (name reference)

`name`OptionalLink to name

`name?: string`

The name of this D1 database.

id: "<DATABASE_ID>", (id reference)

`id`OptionalLink to id

`id?: string`

The UUID of this D1 database (not required).

}),

JOBS: bindings.queue<Job>({ name: "orders-jobs" }), (queue, name reference)

`queue`BuilderLink to queue

`queue<TBody = unknown>(options?: QueueBindingOptions): TypedQueueBinding<TBody>;`

Producer binding to a Cloudflare Queue. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#queues](https://developers.cloudflare.com/workers/wrangler/configuration/#queues)

Options (3)

`name?: string`
    The name of this Queue.

`deliveryDelay?: number`
    The number of seconds to wait before delivering a message.

`dev?: BindingDevOptions`
    Options that only apply during local development.

`name`OptionalLink to name

`name?: string`

The name of this Queue.

COUNTERS: bindings.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject<TWorker$1 extends WorkerReference, TExportName$1 extends DurableObjectExportName<TWorker$1>>(options: DurableObjectBindingOptions<TWorker$1, TExportName$1>): DurableObjectBinding<TWorker$1, TExportName$1>;`

Binding to a Durable Object class. `worker` is the name or config of the Worker that defines the class; `exportName` is the exported class name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects)

Options (2)

`worker: TWorker$1`
    The name or config of the Worker that defines the Durable Object class.

`exportName: TExportName$1`
    The exported class name of the Durable Object.

worker: "orders-api", (worker reference)

`worker`RequiredLink to worker

`worker: TWorker$1`

The name or config of the Worker that defines the Durable Object class.

exportName: "Counter", (exportName reference)

`exportName`RequiredLink to exportName

`exportName: TExportName$1`

The exported class name of the Durable Object.

}),

},

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

Counter: exports.durableObject({ storage: "sqlite" }), (durableObject, storage reference)

`durableObject`BuilderLink to durableObject

`durableObject<TContainer extends ContainerDefinition | undefined = undefined>(options: DurableObjectCreatedExportOptions<TContainer>): DurableObjectCreatedExport<TContainer>;`

Declares a Durable Object class defined by this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects) For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects)

Options (4)

`state?: "created"`
    

`storage: "sqlite"`
    Selects the SQLite-backed storage engine (recommended for new classes).

`container?: TContainer`
    Attach a Container application to this Durable Object by config reference.

`storage: "legacy-kv"`
    Selects the legacy key-value storage engine.

`storage`RequiredLink to storage

`storage: "sqlite" | "legacy-kv"`

Selects the SQLite-backed storage engine (recommended for new classes). Selects the legacy key-value storage engine.

},

triggers: [ (triggers reference)

`triggers`OptionalLink to triggers

`triggers?: Trigger[]`

Event triggers — fetch routes, queue consumers, cron schedules, Email Routing addresses, and raw sockets — that invoke this Worker. Construct entries with `triggers.fetch(...)`, `triggers.queue(...)`, `triggers.scheduled(...)`, `triggers.email(...)`, or `triggers.connect(...)`. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#triggers](https://developers.cloudflare.com/workers/wrangler/configuration/#triggers)

triggers.fetch({ (fetch reference)

`fetch`BuilderLink to fetch

`fetch(options: FetchTriggerOptions): FetchTrigger;`

Fetch trigger — a route that your Worker should be published to. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes](https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes)

Options (2)

`pattern: string`
    A route that your Worker should be published to. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes](https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes)

`zone?: string`
    The DNS zone the pattern is attached to. Required when the pattern is ambiguous.

pattern: "api.example.com/*", (pattern reference)

`pattern`RequiredLink to pattern

`pattern: string`

A route that your Worker should be published to. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes](https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes)

zone: "example.com", (zone reference)

`zone`OptionalLink to zone

`zone?: string`

The DNS zone the pattern is attached to. Required when the pattern is ambiguous.

}),

triggers.queue({ name: "orders-jobs", maxBatchSize: 10 }), (queue, name, maxBatchSize reference)

`queue`BuilderLink to queue

`queue(options: QueueConsumerTriggerOptions): QueueConsumerTrigger;`

Queue consumer trigger — invokes this Worker when messages arrive on the named queue. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#queues](https://developers.cloudflare.com/workers/wrangler/configuration/#queues)

Options (8)

`name: string`
    The name of the queue from which this consumer should consume.

`deadLetterQueue?: string`
    The queue to send messages that failed to be consumed.

`maxBatchSize?: number`
    The maximum number of messages per batch.

`maxBatchTimeout?: number`
    The maximum number of seconds to wait to fill a batch with messages.

`maxConcurrency?: number | null`
    The maximum number of concurrent consumer Worker invocations. Leaving this unset will allow your consumer to scale to the maximum concurrency needed to keep up with the message backlog.

`maxRetries?: number`
    The maximum number of retries for each message.

`retryDelay?: number`
    The number of seconds to wait before retrying a message.

`visibilityTimeoutMs?: number`
    The number of milliseconds to wait for pulled messages to become visible again.

`name`RequiredLink to name

`name: string`

The name of the queue from which this consumer should consume.

`maxBatchSize`OptionalLink to maxBatchSize

`maxBatchSize?: number`

The maximum number of messages per batch.

triggers.scheduled({ schedule: "0 * * * *" }), (scheduled, schedule reference)

`scheduled`BuilderLink to scheduled

`scheduled(options: ScheduledTriggerOptions): ScheduledTrigger;`

Scheduled (cron) trigger — invokes this Worker on the given schedules. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

Options (1)

`schedule: string`
    A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

`schedule`RequiredLink to schedule

`schedule: string`

A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

],

},

});

import { bindings, defineConfig, exports, triggers } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; type Job = { orderId: string }; export default defineConfig({ accountId: "<ACCOUNT_ID>", worker: { name: "orders-api", entrypoint, compatibilityDate: "2026-08-24", compatibilityFlags: ["nodejs_compat"], env: { ENVIRONMENT: bindings.text("production"), DB: bindings.d1({ name: "orders-db", id: "<DATABASE_ID>", }), JOBS: bindings.queue<Job>({ name: "orders-jobs" }), COUNTERS: bindings.durableObject({ worker: "orders-api", exportName: "Counter", }), }, exports: { Counter: exports.durableObject({ storage: "sqlite" }), }, triggers: [ triggers.fetch({ pattern: "api.example.com/*", zone: "example.com", }), triggers.queue({ name: "orders-jobs", maxBatchSize: 10 }), triggers.scheduled({ schedule: "0 * * * *" }), ], }, });

Compared with the file that `cf migrate` generates, the finished file:

  * Imports the entrypoint with the `cf-worker` attribute instead of a string path, so the Worker module exports are typed.
  * Declares the `Counter` class under `exports`, replacing the `migrations` history.
  * Types the queue messages with `bindings.queue<Job>()`.
  * Has no `TODO(@cloudflare)` comments or `throw` statement.



To see the generated file, refer to [Read the output](https://developers.cloudflare.com/cf/wrangler/migrate/#read-the-output).

[PreviousMigrate a project](https://developers.cloudflare.com/cf/wrangler/migrate/)[NextDevelop and deploy](https://developers.cloudflare.com/cf/projects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/wrangler/reference.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
