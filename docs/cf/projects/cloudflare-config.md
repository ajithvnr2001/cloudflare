---
url: https://developers.cloudflare.com/cf/projects/cloudflare-config/
title: Programmatic configuration \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:47.499668+00:00
---

# Programmatic configuration · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/projects/cloudflare-config/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare CLI](https://developers.cloudflare.com/cf/)
  3. /[Workers projects](https://developers.cloudflare.com/cf/projects/)
  4. /cloudflare.config.ts



# Programmatic configuration

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cf/projects/cloudflare-config/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate the minimum configurationUnderstand the default exportEvaluate configurationReuse definitionsConfigure the WorkerUse typed builder valuesDeclare bindings Type cross-Worker bindingsDeclare triggersDeclare exports Manage Durable Object lifecycle Attach a ContainerSet account defaultsSelect a mode

`cloudflare.config.ts` is the typed configuration file for a Workers project. Its default export can define a Worker, Container applications, and account settings. Because the file is a TypeScript module, it can use imports, functions, environment variables, and asynchronous values.

Open beta

Programmatic configuration with `cloudflare.config.ts` is in open beta. The configuration format can change before the stable release.

Loading `cloudflare.config.ts` requires Node.js 22.18 or later. Bun is not supported: when `cf` runs on Bun, loading the file fails with `cloudflare.config.ts loading is not supported on Bun`. Most `cf` commands load the nearest `cloudflare.config.ts`, including commands that only call the Cloudflare API, so this is the practical minimum for any `cf` command you run inside the project.

Set `"type": "module"` in the project's `package.json`. Without it, Node.js prints a warning each time it loads the file. With `"type": "commonjs"`, loading fails with `Cannot use import statement outside a module`.

## Create the minimum configuration

Import the configuration helpers from `cf/config`. Add `cf` as a development dependency so the project can resolve that import. Projects created with [`cf init`](https://developers.cloudflare.com/cf/get-started/first-worker/) already include it.

npmyarnpnpmbun
    
    
    npm i -D cf
    
    
    yarn add -D cf
    
    
    pnpm add -D cf
    
    
    bun add -d cf

A Worker requires `name` and `compatibilityDate`. A Worker that runs code also requires `entrypoint`.

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { defineConfig } from "cf/config";

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

name: "example-worker", (name reference)

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

},

});

import { defineConfig } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "example-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", }, });

The `cf-worker` import attribute lets TypeScript infer the Worker module, binding types, and exported classes.

An assets-only Worker can omit `entrypoint`. Its build implementation must provide the asset source. A deployable build must contain a Worker bundle, static assets, or both.

`cloudflare.config.ts` does not have an `assets.directory` field. In Vite projects, the static assets are the output of Vite's client build, which includes Vite's `publicDir` directory (`public` by default). Projects that build with Wrangler set the directory in a generated `wrangler.config.ts` file. For details, refer to [How cf runs your project](https://developers.cloudflare.com/cf/projects/#how-cf-runs-your-project).

## Understand the default export

Use `defineConfig()` for the default export. The helper returns the value you pass to it and preserves literal values for TypeScript inference.

Field | Required | Purpose  
---|---|---  
`accountId` | No | Sets the default account for `cf` commands  
`complianceRegion` | No | Selects `public` or `fedramp-high`  
`worker` | Development and builds | Defines the Worker  
`containers` | No | Defines Container applications  
  
`cf` API commands can read an account-only default export. The Cloudflare Vite plugin and Wrangler require `worker` for development and builds.

Use the [configuration explorer](https://developers.cloudflare.com/cf/projects/config-explorer/) to inspect the generated fields, builder methods, and nested options.

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { bindings, defineConfig, triggers } from "cf/config";

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

accountId: "<ACCOUNT_ID>", (accountId reference)

`accountId`OptionalLink to accountId

`accountId?: string`

This is the ID of the account associated with your zone. It can also be specified through the `CLOUDFLARE_ACCOUNT_ID` environment variable.

complianceRegion: "public", (complianceRegion reference)

`complianceRegion`OptionalLink to complianceRegion

`complianceRegion?: "public" | "fedramp-high"`

The compliance boundary in which commands should operate. When omitted, this can be supplied through `CLOUDFLARE_COMPLIANCE_REGION`.

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: isStaging ? "example-staging" : "example-worker", (name reference)

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

MESSAGE: bindings.text(isStaging ? "staging" : "production"), (text reference)

`text`BuilderLink to text

`text<T$1 extends string>(value: T$1): TextBinding<T$1>;`

Inline string value made available to the Worker on `env` under the binding name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables](https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables)

},

triggers: [triggers.scheduled({ schedule: "0 * * * *" })], (triggers, scheduled, schedule reference)

`triggers`OptionalLink to triggers

`triggers?: Trigger[]`

Event triggers — fetch routes, queue consumers, cron schedules, Email Routing addresses, and raw sockets — that invoke this Worker. Construct entries with `triggers.fetch(...)`, `triggers.queue(...)`, `triggers.scheduled(...)`, `triggers.email(...)`, or `triggers.connect(...)`. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#triggers](https://developers.cloudflare.com/workers/wrangler/configuration/#triggers)

`scheduled`BuilderLink to scheduled

`scheduled(options: ScheduledTriggerOptions): ScheduledTrigger;`

Scheduled (cron) trigger — invokes this Worker on the given schedules. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

Options (1)

`schedule: string`
    A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

`schedule`RequiredLink to schedule

`schedule: string`

A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

},

};

});

import { bindings, defineConfig, triggers } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig(({ mode }) => { const isStaging = mode === "staging"; return { accountId: "<ACCOUNT_ID>", complianceRegion: "public", worker: { name: isStaging ? "example-staging" : "example-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", env: { MESSAGE: bindings.text(isStaging ? "staging" : "production"), }, triggers: [triggers.scheduled({ schedule: "0 * * * *" })], }, }; });

## Evaluate configuration

`defineConfig()`, `defineWorker()`, and `defineContainer()` each accept an object, a promise, or a function. A function can return an object or a promise.

Functions receive this context:

Property | Purpose  
---|---  
`mode` | Identifies the selected mode, which depends on the command when you omit `--mode`  
`isPreview` | Is `true` when the configuration is evaluated for a [Worker Preview](https://developers.cloudflare.com/cf/projects/#deploy-a-preview)  
  
Return one complete configuration for each mode. Programmatic configuration does not merge environment blocks.

## Reuse definitions

Use `defineWorker()` when another configuration file needs to import a Worker definition. Use `defineContainer()` when a Durable Object export and the `containers` array need to reference the same Container.

These helpers do not replace the default export. The default export must still use `defineConfig()`.

## Configure the Worker

The `worker` object supports these fields:

Field | Required | Purpose  
---|---|---  
`name` | Yes | Sets the Worker name  
`compatibilityDate` | Yes | Selects a Workers runtime compatibility date  
`entrypoint` | Conditional | Selects the Worker module  
`assets` | No | Sets runtime request behavior for built assets  
`cache` | No | Configures Worker cache behavior  
`compatibilityFlags` | No | Turns on runtime compatibility flags  
`domains` | No | Publishes the Worker to custom domains  
`env` | No | Declares bindings and inline values  
`exports` | No | Configures named Worker, Durable Object, and Workflow exports  
`limits` | No | Sets CPU and subrequest limits  
`logpush` | No | Sends trace events to Workers Logpush  
`observability` | No | Configures logs, traces, and sampling  
`placement` | No | Configures smart or targeted placement  
`previewUrls` | No | Controls [version preview URLs](https://developers.cloudflare.com/workers/versions-and-deployments/preview-urls/)  
`tailConsumers` | No | Sends events to Tail Workers  
`triggers` | No | Declares routes, queues, schedules, and sockets  
`unsafe` | No | Passes unsupported metadata through to deployment  
`workersDev` | No | Controls the `workers.dev` route  
  
The `assets` object controls runtime behavior only. It configures HTML handling, not-found handling, and whether matching requests run the Worker first. It does not select the asset source.

Use `domains` for custom domains. Use `triggers.fetch()` for routes.

## Use typed builder values

The `bindings`, `triggers`, and `exports` builders return ordinary configuration objects. Each object has a literal `type` field that identifies its kind.

The `type` field lets TypeScript select the valid options for each kind. For example, a queue trigger accepts batching options, while a scheduled trigger requires a cron expression. The configuration loader uses the same fields for runtime validation.

Use builders instead of writing `type` fields directly. Builders preserve literal values and generic type arguments for Worker type inference.

## Declare bindings

Each key under `worker.env` becomes a binding name in Worker code. The builder method selects the binding's runtime type.

This configuration declares inline values, a D1 database, a Queue, and a secret:

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { bindings, defineConfig } from "cf/config";

import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };

type Job = {

id: string;

operation: "index" | "delete";

};

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

name: "example-worker", (name reference)

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

API_ORIGIN: bindings.text("https://api.example.com"), (text reference)

`text`BuilderLink to text

`text<T$1 extends string>(value: T$1): TextBinding<T$1>;`

Inline string value made available to the Worker on `env` under the binding name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables](https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables)

FEATURES: bindings.json({ search: true }), (json reference)

`json`BuilderLink to json

`json<T$1 extends Json>(value: T$1): JsonBinding<T$1>;`

Inline JSON value made available to the Worker on `env` under the binding name.

DATABASE: bindings.d1({ name: "application-db" }), (d1, name reference)

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

`name`OptionalLink to name

`name?: string`

The name of this D1 database.

JOBS: bindings.queue<Job>({ name: "application-jobs" }), (queue, name reference)

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

API_KEY: bindings.secret(), (secret reference)

`secret`BuilderLink to secret

`secret(): SecretBinding;`

Declares a secret that is required by your Worker, exposed on `env` under the binding name. When defined, this binding: - Replaces .dev.vars/.env/process.env inference for type generation - Enables local dev validation with warnings for missing secrets For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#secrets-configuration-property](https://developers.cloudflare.com/workers/wrangler/configuration/#secrets-configuration-property)

},

},

});

import { bindings, defineConfig } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; type Job = { id: string; operation: "index" | "delete"; }; export default defineConfig({ worker: { name: "example-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", env: { API_ORIGIN: bindings.text("https://api.example.com"), FEATURES: bindings.json({ search: true }), DATABASE: bindings.d1({ name: "application-db" }), JOBS: bindings.queue<Job>({ name: "application-jobs" }), API_KEY: bindings.secret(), }, }, });

The generated `Env` type contains these runtime types:

Binding | Inferred runtime type  
---|---  
`API_ORIGIN` | `"https://api.example.com"`  
`FEATURES` | `{ search: true }`  
`DATABASE` | `D1Database`  
`JOBS` | `Queue<Job>`  
`API_KEY` | `string`  
  
Your Worker receives the inferred type through `env`:

src/index.jsjs
    
    
    export default {
    	async fetch(_request, env) {
    		await env.JOBS.send({
    			id: "example-job",
    			operation: "index",
    		});
    
    		const result = await env.DATABASE.prepare("SELECT 1").first();
    		return Response.json({
    			origin: env.API_ORIGIN,
    			search: env.FEATURES.search,
    			result,
    		});
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(_request, env) {
    		await env.JOBS.send({
    			id: "example-job",
    			operation: "index",
    		});
    
    		const result = await env.DATABASE.prepare("SELECT 1").first();
    		return Response.json({
    			origin: env.API_ORIGIN,
    			search: env.FEATURES.search,
    			result,
    		});
    	},
    } satisfies ExportedHandler<Env>;

The Cloudflare Vite plugin writes `.cloudflare/types/index.d.ts` during development and builds. Outside the Vite workflow, `cf workers types` writes the same file.

TypeScript wildcard patterns skip dot-prefixed directories, so include the generated directory explicitly. The `.ts` extensions in the examples on this page also need `allowImportingTsExtensions`:

tsconfig.jsonjson
    
    
    {
    	"compilerOptions": {
    		"allowImportingTsExtensions": true,
    		"noEmit": true
    	},
    	"include": ["src", "cloudflare.config.ts", ".cloudflare/types"]
    }

The builder API includes these methods:

Area | Builder methods  
---|---  
Inline values | `text`, `json`, `secret`  
Storage and data | `d1`, `kv`, `r2`, `hyperdrive`, `analyticsEngineDataset`, `artifacts`, `pipeline`  
AI and media | `ai`, `aiSearch`, `aiSearchNamespace`, `agentMemory`, `browser`, `images`, `media`, `stream`, `vectorize`  
Messaging | `queue`, `sendEmail`  
Worker composition | `assets`, `dispatchNamespace`, `durableObject`, `worker`, `workerLoader`, `workflow`  
Network and security | `mtlsCertificate`, `rateLimit`, `secretsStoreSecret`, `vpcNetwork`, `vpcService`  
Platform metadata | `flagship`, `logfwdr`, `versionMetadata`  
  
Required options differ by binding. TypeScript completion shows the options for each builder.

### Type cross-Worker bindings

`bindings.worker()`, `bindings.durableObject()`, and `bindings.workflow()` accept a Worker name or a Worker definition. Import a Worker definition to validate its export names at compile time.

For example, an API Worker can export its definition:

Select a highlighted line to show its type and description below it.

api/cloudflare.config.ts

Expand allCopy

import { defineConfig, defineWorker, exports } from "cf/config";

import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };

export const apiWorker = defineWorker({ (defineWorker reference)

`defineWorker`FunctionLink to defineWorker

`defineWorker<T extends ConfigInput<WorkerConfig>>(config: T): T;`

Defines a Worker configuration that you can pass to `worker` in `defineConfig()`. Pass a Worker configuration object, a promise that resolves to one, or a function that receives the config context (`isPreview` and `mode`) and returns either.

Options (18)

`name: string`
    The name of your Worker.

`compatibilityDate: string`
    A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

`compatibilityFlags?: string[]`
    A list of flags that enable features from upcoming features of the Workers runtime, usually used together with `compatibilityDate`. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-flags/](https://developers.cloudflare.com/workers/configuration/compatibility-flags/)

`entrypoint?: string | WorkerModule`
    The entrypoint module that will be executed. May be either a path string (e.g. `"./src/index.ts"`) or a module namespace imported with the `cf-worker` import attribute.

`assets?: { /** How to handle HTML requests. */ htmlHandling?: "auto-trailing-slash" | "drop-trailing-slash" | "force-trailing-slash" | "none"; /** How to handle requests that do not match an asset. */ notFoundHandling?: "single-page-application" | "404-page" | "none"; /** * Matches will be routed to the User Worker, and matches to negative rules will go to the Asset Worker. * * Can also be `true`, indicating that every request should be routed to the User Worker. */ runWorkerFirst?: string[] | boolean; }`
    Specify the directory of static assets to deploy/serve. More details at [https://developers.cloudflare.com/workers/frameworks/](https://developers.cloudflare.com/workers/frameworks/) For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#assets](https://developers.cloudflare.com/workers/wrangler/configuration/#assets)

`domains?: string[]`
    Custom domains that your Worker should be published to. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes](https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes)

`triggers?: Trigger[]`
    Event triggers — fetch routes, queue consumers, cron schedules, Email Routing addresses, and raw sockets — that invoke this Worker. Construct entries with `triggers.fetch(...)`, `triggers.queue(...)`, `triggers.scheduled(...)`, `triggers.email(...)`, or `triggers.connect(...)`. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#triggers](https://developers.cloudflare.com/workers/wrangler/configuration/#triggers)

`tailConsumers?: Array<{ /** The name of the service tail events will be forwarded to. */ worker: string; /** Whether to stream tail events in real time. */ streaming?: boolean; }>`
    A list of Tail Workers that are bound to this Worker. `@cloudflare/config` unifies regular and streaming tail consumers under a single field; pass `streaming: true` to forward streaming tail events.

`cache?: { /** If cache is enabled for this Worker. */ enabled: boolean; /** Whether cached assets may be reused across Worker versions. */ crossVersionCache?: boolean; }`
    Specify the cache behavior of the Worker.

`placement?: { mode: "off" | "smart"; hint?: string; } | { mode?: "targeted"; region: string; } | { mode?: "targeted"; host: string; } | { mode?: "targeted"; hostname: string; }`
    Specify how the Worker should be located to minimize round-trip time. More details: [https://developers.cloudflare.com/workers/platform/smart-placement/](https://developers.cloudflare.com/workers/platform/smart-placement/)

`limits?: { /** Maximum allowed CPU time for a Worker's invocation in milliseconds. */ cpuMs?: number; /** Maximum allowed number of fetch requests that a Worker's invocation can execute. */ subrequests?: number; }`
    Specify limits for runtime behavior. Only supported for the "standard" Usage Model. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#limits](https://developers.cloudflare.com/workers/wrangler/configuration/#limits)

`logpush?: boolean`
    Send Trace Events from this Worker to Workers Logpush. This will not configure a corresponding Logpush job automatically. For more information about Workers Logpush, see: <https://blog.cloudflare.com/logpush-for-workers/>

`observability?: { /** If observability is enabled for this Worker. */ enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** * Whether query strings are removed from request URLs in logs and traces. * * @default false */ redactQueryString?: boolean; /** Real-time Issues settings for this Worker. */ issues?: { /** Whether real-time Issues are enabled. */ enabled?: boolean; }; logs?: { enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** Set to false to disable invocation logs. */ invocationLogs?: boolean; /** * If logs should be persisted to the Cloudflare observability platform where they can be queried in the dashboard. * * @default true */ persist?: boolean; /** * What destinations logs emitted from the Worker should be sent to. * * @default [] */ destinations?: string[]; }; traces?: { enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** * If traces should be persisted to the Cloudflare observability platform where they can be queried in the dashboard. * * @default true */ persist?: boolean; /** * What destinations traces emitted from the Worker should be sent to. * * @default [] */ destinations?: string[]; }; }`
    Specify the observability behavior of the Worker. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#observability](https://developers.cloudflare.com/workers/wrangler/configuration/#observability)

`workersDev?: boolean`
    Whether we use `<name>.<subdomain>.workers.dev` to test and deploy your Worker. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#workersdev](https://developers.cloudflare.com/workers/wrangler/configuration/#workersdev)

`previewUrls?: boolean`
    Whether we use `<version>-<name>.<subdomain>.workers.dev` to serve Preview URLs for your Worker.

`unsafe?: { /** * Arbitrary key/value pairs that will be included in the uploaded metadata. Values specified * here will always be applied to metadata last, so can add new or override existing fields. */ metadata?: Record<string, unknown>; /** * Used for internal capnp uploads for the Workers runtime. */ capnp?: { basePath: string; sourceSchemas: string[]; compiledSchema?: never; } | { basePath?: never; sourceSchemas?: never; compiledSchema: string; }; }`
    "Unsafe" tables for runtime features that aren't directly supported by this configuration. Values are forwarded verbatim in the Worker's upload metadata.

`env?: Record<string, Binding>`
    Bindings exposed on the Worker's `env` object. Construct entries with `bindings.kv(...)`, `bindings.r2(...)`, etc.

`exports?: Record<string, Export>`
    Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

name: "api-worker", (name reference)

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

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

Admin: exports.worker(), (worker reference)

`worker`BuilderLink to worker

`worker(options?: WorkerEntrypointExportOptions): WorkerEntrypointExport;`

Declares a WorkerEntrypoint export defined by this Worker.

Options (1)

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`
    

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

});

export default defineConfig({ worker: apiWorker }); (defineConfig, worker reference)

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

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

import { defineConfig, defineWorker, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export const apiWorker = defineWorker({ name: "api-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", exports: { Admin: exports.worker(), Counter: exports.durableObject({ storage: "sqlite" }), }, }); export default defineConfig({ worker: apiWorker });

A second Worker can import that definition:

Select a highlighted line to show its type and description below it.

web/cloudflare.config.ts

Expand allCopy

import { bindings, defineConfig } from "cf/config";

import { apiWorker } from "../api/cloudflare.config.ts";

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

name: "web-worker", (name reference)

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

API: bindings.worker({ (worker reference)

`worker`BuilderLink to worker

`worker<TWorker$1 extends WorkerReference, TExportName$1 extends WorkerEntrypointExportName<TWorker$1> | undefined = undefined>(options: WorkerBindingOptions<TWorker$1, TExportName$1>): WorkerBinding<TWorker$1, NoInfer<TExportName$1>>;`

Service binding (Worker-to-Worker). `worker` is the name or config of the bound Worker; `exportName` selects a named `WorkerEntrypoint` export (defaults to the default export). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#service-bindings](https://developers.cloudflare.com/workers/wrangler/configuration/#service-bindings)

Options (4)

`worker: TWorker$1`
    The name or config of the bound Worker.

`exportName?: TExportName$1`
    The named export to bind to (defaults to the default export).

`props?: Record<string, unknown>`
    Optional properties that will be made available to the service via `ctx.props`.

`dev?: BindingDevOptions`
    Options that only apply during local development.

worker: apiWorker, (worker reference)

`worker`RequiredLink to worker

`worker: TWorker$1`

The name or config of the bound Worker.

exportName: "Admin", (exportName reference)

`exportName`OptionalLink to exportName

`exportName?: TExportName$1`

The named export to bind to (defaults to the default export).

}),

COUNTERS: bindings.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject<TWorker$1 extends WorkerReference, TExportName$1 extends DurableObjectExportName<TWorker$1>>(options: DurableObjectBindingOptions<TWorker$1, TExportName$1>): DurableObjectBinding<TWorker$1, TExportName$1>;`

Binding to a Durable Object class. `worker` is the name or config of the Worker that defines the class; `exportName` is the exported class name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects)

Options (2)

`worker: TWorker$1`
    The name or config of the Worker that defines the Durable Object class.

`exportName: TExportName$1`
    The exported class name of the Durable Object.

worker: apiWorker, (worker reference)

`worker`RequiredLink to worker

`worker: TWorker$1`

The name or config of the Worker that defines the Durable Object class.

exportName: "Counter", (exportName reference)

`exportName`RequiredLink to exportName

`exportName: TExportName$1`

The exported class name of the Durable Object.

}),

},

},

});

import { bindings, defineConfig } from "cf/config"; import { apiWorker } from "../api/cloudflare.config.ts"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "web-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", env: { API: bindings.worker({ worker: apiWorker, exportName: "Admin", }), COUNTERS: bindings.durableObject({ worker: apiWorker, exportName: "Counter", }), }, }, });

Import the other configuration file with its `.ts` extension. Node.js loads `cloudflare.config.ts` with its own module resolution, which does not add extensions. An import without the extension fails with a `Cannot find module` error (`ERR_MODULE_NOT_FOUND`). Because API commands also load the nearest configuration file, the error breaks ordinary API commands in that directory too.

TypeScript rejects unknown export names. It also infers the `API` Remote Procedure Call (RPC) methods and the Durable Object stub type from the imported entrypoint.

Use a Worker name when the target definition cannot be imported. TypeScript can validate the binding shape, but it cannot validate the remote export name.

## Declare triggers

Each `triggers` method returns a typed event declaration. Add these values to the `worker.triggers` array.

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { defineConfig, triggers } from "cf/config";

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

name: "example-worker", (name reference)

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

triggers.queue({ (queue reference)

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

name: "application-jobs", (name reference)

`name`RequiredLink to name

`name: string`

The name of the queue from which this consumer should consume.

maxBatchSize: 10, (maxBatchSize reference)

`maxBatchSize`OptionalLink to maxBatchSize

`maxBatchSize?: number`

The maximum number of messages per batch.

maxRetries: 3, (maxRetries reference)

`maxRetries`OptionalLink to maxRetries

`maxRetries?: number`

The maximum number of retries for each message.

}),

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

triggers.email({ addresses: ["support@example.com"] }), (email, addresses reference)

`email`BuilderLink to email

`email(options: EmailTriggerOptions): EmailTrigger;`

Email trigger — invokes this Worker for the configured Email Routing addresses.

Options (1)

`addresses: string[]`
    Inbound Email Routing addresses handled by this Worker. Each entry is a literal recipient address (e.g. `"support@example.com"`) or a `*@domain` catch-all (e.g. `"*@example.com"`).

`addresses`RequiredLink to addresses

`addresses: string[]`

Inbound Email Routing addresses handled by this Worker. Each entry is a literal recipient address (e.g. `"support@example.com"`) or a `*@domain` catch-all (e.g. `"*@example.com"`).

triggers.connect({ protocol: "tcp", port: 5432 }), (connect, protocol, port reference)

`connect`BuilderLink to connect

`connect(options: ConnectTriggerOptions): ConnectTrigger;`

Connect trigger — invokes this Worker's `connect(socket, env, ctx)` handler for raw socket connections received on the configured protocol/port.

Options (6)

`port: number`
    The port to listen on.

`address?: string`
    The address to bind to. Defaults to `127.0.0.1`.

`protocol: "tcp"`
    

`protocol: "udp"`
    

`idleTimeoutMs?: number`
    The idle timeout in milliseconds after which a peer flow is closed.

`maxPendingBytes?: number`
    The maximum number of pending datagram bytes per peer flow.

`protocol`RequiredLink to protocol

`protocol: "tcp" | "udp"`

The type definition does not include a description.

`port`RequiredLink to port

`port: number`

The port to listen on.

],

},

});

import { defineConfig, triggers } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "example-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", triggers: [ triggers.fetch({ pattern: "api.example.com/*", zone: "example.com", }), triggers.queue({ name: "application-jobs", maxBatchSize: 10, maxRetries: 3, }), triggers.scheduled({ schedule: "0 * * * *" }), triggers.email({ addresses: ["support@example.com"] }), triggers.connect({ protocol: "tcp", port: 5432 }), ], }, });

The builder provides these trigger methods:

Method | Event  
---|---  
`fetch` | A route receives HTTP traffic  
`queue` | A queue delivers messages  
`scheduled` | A cron schedule runs  
`email` | Email Routing receives matching email  
`connect` | TCP or UDP traffic reaches the configured port  
  
Set `protocol` to `"tcp"` or `"udp"` in `triggers.connect()`. UDP triggers also accept `idleTimeoutMs` and `maxPendingBytes`.

Triggers control which events invoke a Worker. They do not create `env` bindings. TypeScript checks the options for each trigger, while Workers runtime types provide the handler signatures.

## Declare exports

The `worker.exports` map describes how the platform manages module exports. Each key must match the `default` export or a named class exported by the entrypoint.

Use `exports.worker()` to configure a `WorkerEntrypoint`. It accepts an optional per-entrypoint cache setting. Use `exports.durableObject()` to declare a Durable Object class and its lifecycle state. Use `exports.workflow()` to declare a class that extends `WorkflowEntrypoint`.

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

name: "example-worker", (name reference)

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

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

default: exports.worker({ cache: { enabled: false } }), (worker, cache, enabled reference)

`worker`BuilderLink to worker

`worker(options?: WorkerEntrypointExportOptions): WorkerEntrypointExport;`

Declares a WorkerEntrypoint export defined by this Worker.

Options (1)

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`
    

`cache`OptionalLink to cache

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`

The type definition does not include a description.

`enabled`RequiredLink to enabled

`enabled: boolean`

Whether cache is enabled for this entrypoint.

Admin: exports.worker({ cache: { enabled: true } }), (worker, cache, enabled reference)

`worker`BuilderLink to worker

`worker(options?: WorkerEntrypointExportOptions): WorkerEntrypointExport;`

Declares a WorkerEntrypoint export defined by this Worker.

Options (1)

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`
    

`cache`OptionalLink to cache

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`

The type definition does not include a description.

`enabled`RequiredLink to enabled

`enabled: boolean`

Whether cache is enabled for this entrypoint.

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

OrderWorkflow: exports.workflow({ (workflow reference)

`workflow`BuilderLink to workflow

`workflow(options: WorkflowExportOptions): WorkflowExport;`

Declares a Workflow defined by this Worker. The export's key must name a class that extends `WorkflowEntrypoint`. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/)

Options (5)

`name: string`
    The name of the Workflow. It identifies the Workflow's instances and must be unique within the account.

`limits?: { /** Maximum number of steps a single Workflow instance may run. */ steps?: number; }`
    

`concurrency?: { /** Maximum number of Workflow instances that can run concurrently. */ limit?: number; }`
    

`schedules?: string | string[]`
    Cron schedule(s) that automatically trigger Workflow instances.

`defaultRetention?: { /** How long to retain instances that completed successfully or were terminated. */ successRetention?: number | string; /** How long to retain errored instances. */ errorRetention?: number | string; }`
    Default retention for instances of this Workflow, applied when an instance does not set its own retention. Accepts milliseconds or a duration string such as `"3 days"`.

name: "order-workflow", (name reference)

`name`RequiredLink to name

`name: string`

The name of the Workflow. It identifies the Workflow's instances and must be unique within the account.

limits: { steps: 100 }, (limits, steps reference)

`limits`OptionalLink to limits

`limits?: { /** Maximum number of steps a single Workflow instance may run. */ steps?: number; }`

The type definition does not include a description.

`steps`OptionalLink to steps

`steps?: number`

Maximum number of steps a single Workflow instance may run.

defaultRetention: { (defaultRetention reference)

`defaultRetention`OptionalLink to defaultRetention

`defaultRetention?: { /** How long to retain instances that completed successfully or were terminated. */ successRetention?: number | string; /** How long to retain errored instances. */ errorRetention?: number | string; }`

Default retention for instances of this Workflow, applied when an instance does not set its own retention. Accepts milliseconds or a duration string such as `"3 days"`.

successRetention: "3 days", (successRetention reference)

`successRetention`OptionalLink to successRetention

`successRetention?: number | string`

How long to retain instances that completed successfully or were terminated.

errorRetention: "7 days", (errorRetention reference)

`errorRetention`OptionalLink to errorRetention

`errorRetention?: number | string`

How long to retain errored instances.

},

}),

},

},

});

import { defineConfig, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "example-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", exports: { default: exports.worker({ cache: { enabled: false } }), Admin: exports.worker({ cache: { enabled: true } }), Counter: exports.durableObject({ storage: "sqlite" }), OrderWorkflow: exports.workflow({ name: "order-workflow", limits: { steps: 100 }, defaultRetention: { successRetention: "3 days", errorRetention: "7 days", }, }), }, }, });

The builders describe exported code. They do not create JavaScript exports. The entrypoint must still export `Admin`, `Counter`, and `OrderWorkflow`.

`exports.workflow()` requires a `name`, which must be unique within the account. It also accepts `limits.steps`, `concurrency.limit`, `schedules` for cron schedules that start instances, and `defaultRetention`. Retention values accept milliseconds or a duration string, such as `"3 days"`.

To bind to a Workflow, from the same Worker or another one, use `bindings.workflow()`. It requires the Workflow's `name`, the `worker` that defines it (a Worker name or a Worker definition), and the `exportName` of its class, such as `bindings.workflow({ name: "order-workflow", worker: "example-worker", exportName: "OrderWorkflow" })`.

### Manage Durable Object lifecycle

The `exports` map replaces an ordered Durable Object migration history. Keep live classes in the map. Add temporary tombstones when a class is deleted, renamed, or transferred.

The key of each entry is the Durable Object class name. The `state` field selects the valid lifecycle options:

State | Purpose  
---|---  
`created` or omitted | Declares a live class with `sqlite` or `legacy-kv` storage  
`deleted` | Retires a namespace after its class is removed  
`renamed` | Renames the key to the live class named by `renamedTo`  
`expecting-transfer` | Prepares the destination Worker to receive a namespace from `transferFrom`  
`transferred` | Transfers ownership to the same-account Worker named by `transferredTo`  
  
Use `sqlite` for new classes. A live or incoming class that uses `sqlite` can attach a Container definition. You cannot attach a Container to a `legacy-kv` class or a tombstone.

#### Distinguish exports from bindings

Exports and bindings serve different purposes:

Configuration | Purpose  
---|---  
`exports.Counter` | Declares the class and manages its namespace lifecycle  
`env.COUNTERS` | Injects a namespace binding under `env.COUNTERS`  
`ctx.exports.Counter` | Accesses a class exported by the same Worker without an `env` binding  
  
Live Durable Object exports become typed properties on `ctx.exports`. A Worker does not need an `env` binding to call its own class.

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

name: "counter-worker", (name reference)

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

compatibilityFlags: ["enable_ctx_exports"], (compatibilityFlags reference)

`compatibilityFlags`OptionalLink to compatibilityFlags

`compatibilityFlags?: string[]`

A list of flags that enable features from upcoming features of the Workers runtime, usually used together with `compatibilityDate`. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-flags/](https://developers.cloudflare.com/workers/configuration/compatibility-flags/)

Default: `[]`

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

},

});

import { defineConfig, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "counter-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", compatibilityFlags: ["enable_ctx_exports"], exports: { Counter: exports.durableObject({ storage: "sqlite" }), }, }, });

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class Counter extends DurableObject {
    	getValue() {
    		return this.ctx.storage.get("value");
    	}
    }
    
    export default {
    	async fetch(_request, _env, ctx) {
    		const id = ctx.exports.Counter.idFromName("global");
    		const stub = ctx.exports.Counter.get(id);
    		return Response.json({ value: await stub.getValue() });
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class Counter extends DurableObject {
    	getValue() {
    		return this.ctx.storage.get<number>("value");
    	}
    }
    
    export default {
    	async fetch(_request, _env, ctx) {
    		const id = ctx.exports.Counter.idFromName("global");
    		const stub = ctx.exports.Counter.get(id);
    		return Response.json({ value: await stub.getValue() });
    	},
    } satisfies ExportedHandler<Env>;

The generated types include live and incoming Durable Object exports. Tombstones do not appear on `ctx.exports`.

#### Rename or delete a class

A rename keeps the old name as a tombstone. The destination name must appear as a live entry in the same map. Remove the old class from the Worker code.

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

name: "counter-worker", (name reference)

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

import { defineConfig, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "counter-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", exports: { Counter: exports.durableObject({ storage: "sqlite" }), OldCounter: exports.durableObject({ state: "renamed", renamedTo: "Counter", }), UnusedCounter: exports.durableObject({ state: "deleted" }), }, }, });

Before you delete a namespace, remove every binding to that class. The uploaded Worker must not export a class marked as `deleted`.

Deployment responses identify stale tombstones that are safe to remove. Keep each tombstone until it appears in that response, then remove it from the map. You do not need to retain the complete migration history.

#### Transfer a class between Workers

A namespace transfer uses two deployments. Both Workers must use the same Cloudflare account.

First, deploy the destination Worker with an incoming live entry:

Select a highlighted line to show its type and description below it.

destination/cloudflare.config.ts

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

name: "destination-worker", (name reference)

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

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

Counter: exports.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject<TContainer extends ContainerDefinition | undefined = undefined>(options: DurableObjectExpectingTransferExportOptions<TContainer>): DurableObjectExpectingTransferExport<TContainer>;`

Prepare to receive cross-Worker Durable Object transfer. The source Worker must follow up with a deployment containing a `transferred` export to commit the transfer.

Options (5)

`state: "expecting-transfer"`
    

`transferFrom: string`
    The source Worker for the two-phase cross-Worker transfer.

`storage: "sqlite"`
    Selects the SQLite-backed storage engine (recommended for new classes).

`container?: TContainer`
    Attach a Container application to this Durable Object by config reference.

`storage: "legacy-kv"`
    Selects the legacy key-value storage engine.

state: "expecting-transfer", (state reference)

`state`RequiredLink to state

`state: "expecting-transfer"`

The type definition does not include a description.

storage: "sqlite", (storage reference)

`storage`RequiredLink to storage

`storage: "sqlite" | "legacy-kv"`

Selects the SQLite-backed storage engine (recommended for new classes). Selects the legacy key-value storage engine.

transferFrom: "source-worker", (transferFrom reference)

`transferFrom`RequiredLink to transferFrom

`transferFrom: string`

The source Worker for the two-phase cross-Worker transfer.

}),

},

},

});

import { defineConfig, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "destination-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", exports: { Counter: exports.durableObject({ state: "expecting-transfer", storage: "sqlite", transferFrom: "source-worker", }), }, }, });

Then deploy the source Worker with a transfer tombstone:

Select a highlighted line to show its type and description below it.

source/cloudflare.config.ts

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

name: "source-worker", (name reference)

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

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

Counter: exports.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject(options: DurableObjectTransferredExportOptions): DurableObjectTransferredExport;`

Transfer ownership of a Durable Object namespace to another Worker in the same account.

Options (2)

`state: "transferred"`
    

`transferredTo: string`
    The destination Worker. Must reference a Worker in the same account.

state: "transferred", (state reference)

`state`RequiredLink to state

`state: "transferred"`

The type definition does not include a description.

transferredTo: "destination-worker", (transferredTo reference)

`transferredTo`RequiredLink to transferredTo

`transferredTo: string`

The destination Worker. Must reference a Worker in the same account.

}),

},

},

});

import { defineConfig, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "source-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", exports: { Counter: exports.durableObject({ state: "transferred", transferredTo: "destination-worker", }), }, }, });

Lifecycle changes take effect when a version is deployed, not when it is uploaded. Deploy an export-changing version to 100% of traffic before you split traffic with other versions. The platform rejects split deployments whose versions disagree about `exports`.

### Attach a Container

Define a Container once. Reference it from a Durable Object export and add it to the top-level `containers` array.

Select a highlighted line to show its type and description below it.

cloudflare.config.ts

Expand allCopy

import { bindings, defineConfig, defineContainer, exports } from "cf/config";

import * as entrypoint from "./src/index.ts" with { type: "cf-worker" };

const imageProcessor = defineContainer({ (defineContainer reference)

`defineContainer`FunctionLink to defineContainer

`defineContainer<T extends ConfigInput<ContainerConfig>>(config: T): T;`

Defines a Container application that you can list in `containers` in `defineConfig()` or attach to a Durable Object export with its `container` option.

name: "image-processor",

image: { dockerfile: "./Dockerfile" },

instanceType: "lite",

maxInstances: 1,

});

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

name: "image-worker", (name reference)

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

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

ImageProcessor: exports.durableObject({ (durableObject reference)

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

storage: "sqlite", (storage reference)

`storage`RequiredLink to storage

`storage: "sqlite" | "legacy-kv"`

Selects the SQLite-backed storage engine (recommended for new classes). Selects the legacy key-value storage engine.

container: imageProcessor, (container reference)

`container`OptionalLink to container

`container?: TContainer`

Attach a Container application to this Durable Object by config reference.

}),

},

env: { (env reference)

`env`OptionalLink to env

`env?: Record<string, Binding>`

Bindings exposed on the Worker's `env` object. Construct entries with `bindings.kv(...)`, `bindings.r2(...)`, etc.

IMAGE_PROCESSOR: bindings.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject<TWorker$1 extends WorkerReference, TExportName$1 extends DurableObjectExportName<TWorker$1>>(options: DurableObjectBindingOptions<TWorker$1, TExportName$1>): DurableObjectBinding<TWorker$1, TExportName$1>;`

Binding to a Durable Object class. `worker` is the name or config of the Worker that defines the class; `exportName` is the exported class name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects)

Options (2)

`worker: TWorker$1`
    The name or config of the Worker that defines the Durable Object class.

`exportName: TExportName$1`
    The exported class name of the Durable Object.

worker: "image-worker", (worker reference)

`worker`RequiredLink to worker

`worker: TWorker$1`

The name or config of the Worker that defines the Durable Object class.

exportName: "ImageProcessor", (exportName reference)

`exportName`RequiredLink to exportName

`exportName: TExportName$1`

The exported class name of the Durable Object.

}),

},

},

containers: [imageProcessor], (containers reference)

`containers`OptionalLink to containers

`containers?: ConfigInput<ContainerConfig>[]`

Container applications defined by this configuration.

});

import { bindings, defineConfig, defineContainer, exports } from "cf/config"; import * as entrypoint from "./src/index.ts" with { type: "cf-worker" }; const imageProcessor = defineContainer({ name: "image-processor", image: { dockerfile: "./Dockerfile" }, instanceType: "lite", maxInstances: 1, }); export default defineConfig({ worker: { name: "image-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", exports: { ImageProcessor: exports.durableObject({ storage: "sqlite", container: imageProcessor, }), }, env: { IMAGE_PROCESSOR: bindings.durableObject({ worker: "image-worker", exportName: "ImageProcessor", }), }, }, containers: [imageProcessor], });

Container names must be unique. Each Container can be linked to only one Durable Object export.

`cf deploy` applies supported Container application changes. `cf workers versions create` prepares images for Durable Object-managed Containers, but it does not apply Container applications.

## Set account defaults

Set `accountId` and `complianceRegion` at the top level of the default export. Supported compliance regions are `public` and `fedramp-high`.

`CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_COMPLIANCE_REGION` take priority over these values. When neither the environment nor the configuration sets an account, `cf` uses the account it saved on an earlier command, or resolves one from your credentials. For the full order, refer to [Select an account](https://developers.cloudflare.com/cf/get-started/#select-an-account).

`cf` searches from the current directory toward the filesystem root and uses the nearest `cloudflare.config.ts` file.

When an API command reads account defaults, `cf` executes the module and resolves the default export. If the default export is a function, `cf` calls it with `isPreview: false` and the mode passed with `--mode`. Without `--mode`, the mode is `undefined`, while a Vite build of the same project uses `production`. `cf deploy`, `cf workers versions create`, and `cf workers triggers deploy` resolve the account the same way. Without `--mode`, they evaluate the configuration with an `undefined` mode, even when the Vite build used `production`. If `accountId` depends on the mode, pass `--mode` explicitly to every command.

API commands do not evaluate nested `worker` or `containers` factories, and they do not validate Worker fields. Syntax errors, import errors, and top-level runtime errors in the module still break them.

## Select a mode

Pass `--mode <NAME>`, or `-m <NAME>`, to evaluate function-form configuration for a named mode. Project commands also pass the mode to the build:
    
    
    cf build --mode staging
    cf deploy --mode staging

When you omit `--mode`, the default depends on the tool that evaluates the configuration:

Command | Default mode  
---|---  
`cf dev` with the Cloudflare Vite plugin | `development`  
`cf build`, `cf deploy`, and other commands that build with Vite | `production`  
Commands that build with Wrangler | `undefined`  
API commands, such as `cf d1 list` | `undefined`  
  
When `cf` runs a framework's own command, only Vite and Astro accept `--mode`. For other frameworks, the command stops with an error that says the detected command does not currently support `--mode`.

Build Output records the mode in its root `config.json`. To deploy an existing build with `--prebuilt`, pass the recorded mode. For the rule and examples, refer to [Deploy a prebuilt build](https://developers.cloudflare.com/cf/projects/#deploy-a-prebuilt-build).

[PreviousDevelop and deploy](https://developers.cloudflare.com/cf/projects/)[NextConfiguration explorer](https://developers.cloudflare.com/cf/projects/config-explorer/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/projects/cloudflare-config.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
