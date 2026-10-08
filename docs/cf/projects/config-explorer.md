---
url: https://developers.cloudflare.com/cf/projects/config-explorer/
title: Configuration explorer \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:47.909075+00:00
---

# Configuration explorer · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/projects/config-explorer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare CLI](https://developers.cloudflare.com/cf/)
  3. /[Workers projects](https://developers.cloudflare.com/cf/projects/)
  4. /Configuration explorer



# Configuration explorer

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cf/projects/config-explorer/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`cloudflare.config.ts` is a TypeScript file, so every field has a type and a description. Use the configuration explorer to see how the file describes the main parts of an application: project settings, the Worker, bindings, triggers, and exports.

Select a category, then select a highlighted field to see its type, description, default value, and accepted options. Editors with TypeScript support show the same information in autocomplete and hover text as you write the file, and type checking flags values that do not match.

To learn how to structure a project's configuration, refer to [Programmatic configuration](https://developers.cloudflare.com/cf/projects/cloudflare-config/). To return different configuration for each environment, refer to [Modes](https://developers.cloudflare.com/cf/projects/#modes).

Select a highlighted line to show its type and description below it.

Generated from `@cloudflare/config`0.20.0

defineConfig6 optionsWorker18 optionsBindings35 optionsTriggers5 optionsExports7 options

Expand allCopy

### defineConfig

import { defineConfig } from "cf/config";

import * as entrypoint from "./src/index" with { type: "cf-worker" };

export default defineConfig(({ isPreview, mode }) => ({ (isPreview, mode reference)

`isPreview`Context valueLink to isPreview

`isPreview: boolean`

Whether the config is being evaluated for a Preview build.

`mode`Context valueLink to mode

`mode: string | undefined`

The mode the config is being evaluated in. Set via the `--mode` CLI flag. In Vite the mode defaults to `development` in `vite dev` and `production` in `vite build` ([more info](https://vite.dev/guide/env-and-mode.html#modes)). In Wrangler the mode defaults to `undefined`.

accountId: "<ACCOUNT_ID>", (accountId reference)

`accountId`OptionalLink to accountId

`accountId?: string`

This is the ID of the account associated with your zone. It can also be specified through the `CLOUDFLARE_ACCOUNT_ID` environment variable.

complianceRegion: mode === "fedramp" ? "fedramp-high" : "public", (complianceRegion reference)

`complianceRegion`OptionalLink to complianceRegion

`complianceRegion?: "public" | "fedramp-high"`

The compliance boundary in which commands should operate. When omitted, this can be supplied through `CLOUDFLARE_COMPLIANCE_REGION`.

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: isPreview ? "example-preview" : "example-worker", (name reference)

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

containers: [], (containers reference)

`containers`OptionalLink to containers

`containers?: ConfigInput<ContainerConfig>[]`

Container applications defined by this configuration.

}));

import { defineConfig } from "cf/config"; import * as entrypoint from "./src/index" with { type: "cf-worker" }; export default defineConfig(({ isPreview, mode }) => ({ accountId: "<ACCOUNT_ID>", complianceRegion: mode === "fedramp" ? "fedramp-high" : "public", worker: { name: isPreview ? "example-preview" : "example-worker", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", }, containers: [], }));

### Worker

import { bindings, defineConfig, exports, triggers } from "cf/config";

import * as entrypoint from "./src/index" with { type: "cf-worker" };

export default defineConfig(({ mode }) => ({ (mode reference)

`mode`Context valueLink to mode

`mode: string | undefined`

The mode the config is being evaluated in. Set via the `--mode` CLI flag. In Vite the mode defaults to `development` in `vite dev` and `production` in `vite build` ([more info](https://vite.dev/guide/env-and-mode.html#modes)). In Wrangler the mode defaults to `undefined`.

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: mode === "staging" ? "images-staging" : "images", (name reference)

`name`RequiredLink to name

`name: string`

The name of your Worker.

compatibilityDate: "<COMPATIBILITY_DATE>", (compatibilityDate reference)

`compatibilityDate`RequiredLink to compatibilityDate

`compatibilityDate: string`

A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-dates](https://developers.cloudflare.com/workers/configuration/compatibility-dates)

compatibilityFlags: ["nodejs_compat"], (compatibilityFlags reference)

`compatibilityFlags`OptionalLink to compatibilityFlags

`compatibilityFlags?: string[]`

A list of flags that enable features from upcoming features of the Workers runtime, usually used together with `compatibilityDate`. More details at [https://developers.cloudflare.com/workers/configuration/compatibility-flags/](https://developers.cloudflare.com/workers/configuration/compatibility-flags/)

Default: `[]`

entrypoint, (entrypoint reference)

`entrypoint`OptionalLink to entrypoint

`entrypoint?: string | WorkerModule`

The entrypoint module that will be executed. May be either a path string (e.g. `"./src/index.ts"`) or a module namespace imported with the `cf-worker` import attribute.

assets: { (assets reference)

`assets`OptionalLink to assets

`assets?: { /** How to handle HTML requests. */ htmlHandling?: "auto-trailing-slash" | "drop-trailing-slash" | "force-trailing-slash" | "none"; /** How to handle requests that do not match an asset. */ notFoundHandling?: "single-page-application" | "404-page" | "none"; /** * Matches will be routed to the User Worker, and matches to negative rules will go to the Asset Worker. * * Can also be `true`, indicating that every request should be routed to the User Worker. */ runWorkerFirst?: string[] | boolean; }`

Specify the directory of static assets to deploy/serve. More details at [https://developers.cloudflare.com/workers/frameworks/](https://developers.cloudflare.com/workers/frameworks/) For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#assets](https://developers.cloudflare.com/workers/wrangler/configuration/#assets)

htmlHandling: "auto-trailing-slash", (htmlHandling reference)

`htmlHandling`OptionalLink to htmlHandling

`htmlHandling?: "auto-trailing-slash" | "drop-trailing-slash" | "force-trailing-slash" | "none"`

How to handle HTML requests.

},

domains: ["images.example.com"], (domains reference)

`domains`OptionalLink to domains

`domains?: string[]`

Custom domains that your Worker should be published to. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes](https://developers.cloudflare.com/workers/wrangler/configuration/#types-of-routes)

triggers: [ (triggers reference)

`triggers`OptionalLink to triggers

`triggers?: Trigger[]`

Event triggers — fetch routes, queue consumers, cron schedules, Email Routing addresses, and raw sockets — that invoke this Worker. Construct entries with `triggers.fetch(...)`, `triggers.queue(...)`, `triggers.scheduled(...)`, `triggers.email(...)`, or `triggers.connect(...)`. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#triggers](https://developers.cloudflare.com/workers/wrangler/configuration/#triggers)

triggers.scheduled({ (scheduled reference)

`scheduled`BuilderLink to scheduled

`scheduled(options: ScheduledTriggerOptions): ScheduledTrigger;`

Scheduled (cron) trigger — invokes this Worker on the given schedules. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

Options (1)

`schedule: string`
    A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

schedule: "0 * * * *", (schedule reference)

`schedule`RequiredLink to schedule

`schedule: string`

A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

}),

],

tailConsumers: [ (tailConsumers reference)

`tailConsumers`OptionalLink to tailConsumers

`tailConsumers?: Array<{ /** The name of the service tail events will be forwarded to. */ worker: string; /** Whether to stream tail events in real time. */ streaming?: boolean; }>`

A list of Tail Workers that are bound to this Worker. `@cloudflare/config` unifies regular and streaming tail consumers under a single field; pass `streaming: true` to forward streaming tail events.

Default: `[]`

{

worker: "log-sink", (worker reference)

`worker`RequiredLink to worker

`worker: string`

The name of the service tail events will be forwarded to.

streaming: true, (streaming reference)

`streaming`OptionalLink to streaming

`streaming?: boolean`

Whether to stream tail events in real time.

},

],

cache: { (cache reference)

`cache`OptionalLink to cache

`cache?: { /** If cache is enabled for this Worker. */ enabled: boolean; /** Whether cached assets may be reused across Worker versions. */ crossVersionCache?: boolean; }`

Specify the cache behavior of the Worker.

enabled: true, (enabled reference)

`enabled`RequiredLink to enabled

`enabled: boolean`

If cache is enabled for this Worker.

crossVersionCache: true, (crossVersionCache reference)

`crossVersionCache`OptionalLink to crossVersionCache

`crossVersionCache?: boolean`

Whether cached assets may be reused across Worker versions.

},

placement: { (placement reference)

`placement`OptionalLink to placement

`placement?: { mode: "off" | "smart"; hint?: string; } | { mode?: "targeted"; region: string; } | { mode?: "targeted"; host: string; } | { mode?: "targeted"; hostname: string; }`

Specify how the Worker should be located to minimize round-trip time. More details: [https://developers.cloudflare.com/workers/platform/smart-placement/](https://developers.cloudflare.com/workers/platform/smart-placement/)

mode: "smart", (mode reference)

`mode`RequiredLink to mode

`mode: "off" | "smart"`

The type definition does not include a description.

},

limits: { (limits reference)

`limits`OptionalLink to limits

`limits?: { /** Maximum allowed CPU time for a Worker's invocation in milliseconds. */ cpuMs?: number; /** Maximum allowed number of fetch requests that a Worker's invocation can execute. */ subrequests?: number; }`

Specify limits for runtime behavior. Only supported for the "standard" Usage Model. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#limits](https://developers.cloudflare.com/workers/wrangler/configuration/#limits)

cpuMs: 50, (cpuMs reference)

`cpuMs`OptionalLink to cpuMs

`cpuMs?: number`

Maximum allowed CPU time for a Worker's invocation in milliseconds.

subrequests: 100, (subrequests reference)

`subrequests`OptionalLink to subrequests

`subrequests?: number`

Maximum allowed number of fetch requests that a Worker's invocation can execute.

},

logpush: true, (logpush reference)

`logpush`OptionalLink to logpush

`logpush?: boolean`

Send Trace Events from this Worker to Workers Logpush. This will not configure a corresponding Logpush job automatically. For more information about Workers Logpush, see: <https://blog.cloudflare.com/logpush-for-workers/>

observability: { (observability reference)

`observability`OptionalLink to observability

`observability?: { /** If observability is enabled for this Worker. */ enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** * Whether query strings are removed from request URLs in logs and traces. * * @default false */ redactQueryString?: boolean; /** Real-time Issues settings for this Worker. */ issues?: { /** Whether real-time Issues are enabled. */ enabled?: boolean; }; logs?: { enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** Set to false to disable invocation logs. */ invocationLogs?: boolean; /** * If logs should be persisted to the Cloudflare observability platform where they can be queried in the dashboard. * * @default true */ persist?: boolean; /** * What destinations logs emitted from the Worker should be sent to. * * @default [] */ destinations?: string[]; }; traces?: { enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** * If traces should be persisted to the Cloudflare observability platform where they can be queried in the dashboard. * * @default true */ persist?: boolean; /** * What destinations traces emitted from the Worker should be sent to. * * @default [] */ destinations?: string[]; }; }`

Specify the observability behavior of the Worker. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#observability](https://developers.cloudflare.com/workers/wrangler/configuration/#observability)

enabled: true, (enabled reference)

`enabled`OptionalLink to enabled

`enabled?: boolean`

If observability is enabled for this Worker.

logs: { (logs reference)

`logs`OptionalLink to logs

`logs?: { enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** Set to false to disable invocation logs. */ invocationLogs?: boolean; /** * If logs should be persisted to the Cloudflare observability platform where they can be queried in the dashboard. * * @default true */ persist?: boolean; /** * What destinations logs emitted from the Worker should be sent to. * * @default [] */ destinations?: string[]; }`

The type definition does not include a description.

persist: true, (persist reference)

`persist`OptionalLink to persist

`persist?: boolean`

If logs should be persisted to the Cloudflare observability platform where they can be queried in the dashboard.

Default: `true`

},

traces: { (traces reference)

`traces`OptionalLink to traces

`traces?: { enabled?: boolean; /** The sampling rate. */ headSamplingRate?: number; /** * If traces should be persisted to the Cloudflare observability platform where they can be queried in the dashboard. * * @default true */ persist?: boolean; /** * What destinations traces emitted from the Worker should be sent to. * * @default [] */ destinations?: string[]; }`

The type definition does not include a description.

persist: true, (persist reference)

`persist`OptionalLink to persist

`persist?: boolean`

If traces should be persisted to the Cloudflare observability platform where they can be queried in the dashboard.

Default: `true`

},

},

workersDev: false, (workersDev reference)

`workersDev`OptionalLink to workersDev

`workersDev?: boolean`

Whether we use `<name>.<subdomain>.workers.dev` to test and deploy your Worker. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#workersdev](https://developers.cloudflare.com/workers/wrangler/configuration/#workersdev)

Default: `true`

previewUrls: true, (previewUrls reference)

`previewUrls`OptionalLink to previewUrls

`previewUrls?: boolean`

Whether we use `<version>-<name>.<subdomain>.workers.dev` to serve Preview URLs for your Worker.

Default: `false`

unsafe: { (unsafe reference)

`unsafe`OptionalLink to unsafe

`unsafe?: { /** * Arbitrary key/value pairs that will be included in the uploaded metadata. Values specified * here will always be applied to metadata last, so can add new or override existing fields. */ metadata?: Record<string, unknown>; /** * Used for internal capnp uploads for the Workers runtime. */ capnp?: { basePath: string; sourceSchemas: string[]; compiledSchema?: never; } | { basePath?: never; sourceSchemas?: never; compiledSchema: string; }; }`

"Unsafe" tables for runtime features that aren't directly supported by this configuration. Values are forwarded verbatim in the Worker's upload metadata.

Default: `{}`

metadata: { build: "docs-example" }, (metadata reference)

`metadata`OptionalLink to metadata

`metadata?: Record<string, unknown>`

Arbitrary key/value pairs that will be included in the uploaded metadata. Values specified here will always be applied to metadata last, so can add new or override existing fields.

},

env: { (env reference)

`env`OptionalLink to env

`env?: Record<string, Binding>`

Bindings exposed on the Worker's `env` object. Construct entries with `bindings.kv(...)`, `bindings.r2(...)`, etc.

API_ORIGIN: bindings.text("https://api.example.com"), (text reference)

`text`BuilderLink to text

`text<T$1 extends string>(value: T$1): TextBinding<T$1>;`

Inline string value made available to the Worker on `env` under the binding name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables](https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables)

DATABASE: bindings.d1({ (d1 reference)

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

name: "images-db", (name reference)

`name`OptionalLink to name

`name?: string`

The name of this D1 database.

}),

IMAGES: bindings.r2({ (r2 reference)

`r2`BuilderLink to r2

`r2(options?: R2BindingOptions): R2Binding;`

Binding to an R2 bucket. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#r2-buckets](https://developers.cloudflare.com/workers/wrangler/configuration/#r2-buckets)

Options (3)

`name?: string`
    The name of this R2 bucket at the edge.

`jurisdiction?: string`
    The jurisdiction that the bucket exists in. Default if not present.

`dev?: BindingDevOptions & { /** EXPERIMENTAL: credentials for the local S3-compatible endpoint. */ experimentalS3Credentials?: { accessKeyId: string; secretAccessKey: string; }; }`
    Settings that only apply to local development.

name: "source-images", (name reference)

`name`OptionalLink to name

`name?: string`

The name of this R2 bucket at the edge.

}),

},

exports: { (exports reference)

`exports`OptionalLink to exports

`exports?: Record<string, Export>`

Configuration for named exports declared by the Worker. Each entry's key is the exported class name; the value configures the export. - Construct entries with `exports.durableObject(...)`. - Declares Durable Object classes exported from this Worker. For more information about Durable Objects, see the documentation at [https://developers.cloudflare.com/workers/learning/using-durable-objects](https://developers.cloudflare.com/workers/learning/using-durable-objects). For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects). - Construct entries with `exports.workflow(...)`. - Declares Workflows defined by this Worker. For more information about Workflows, see the documentation at [https://developers.cloudflare.com/workflows/](https://developers.cloudflare.com/workflows/).

Admin: exports.worker({ (worker reference)

`worker`BuilderLink to worker

`worker(options?: WorkerEntrypointExportOptions): WorkerEntrypointExport;`

Declares a WorkerEntrypoint export defined by this Worker.

Options (1)

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`
    

cache: { (cache reference)

`cache`OptionalLink to cache

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`

The type definition does not include a description.

enabled: true, (enabled reference)

`enabled`RequiredLink to enabled

`enabled: boolean`

Whether cache is enabled for this entrypoint.

},

}),

Counter: exports.durableObject({ (durableObject reference)

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

`storage: "sqlite"`

Selects the SQLite-backed storage engine (recommended for new classes).

}),

},

},

}));

import { bindings, defineConfig, exports, triggers } from "cf/config"; import * as entrypoint from "./src/index" with { type: "cf-worker" }; export default defineConfig(({ mode }) => ({ worker: { name: mode === "staging" ? "images-staging" : "images", compatibilityDate: "<COMPATIBILITY_DATE>", compatibilityFlags: ["nodejs_compat"], entrypoint, assets: { htmlHandling: "auto-trailing-slash", }, domains: ["images.example.com"], triggers: [ triggers.scheduled({ schedule: "0 * * * *", }), ], tailConsumers: [ { worker: "log-sink", streaming: true, }, ], cache: { enabled: true, crossVersionCache: true, }, placement: { mode: "smart", }, limits: { cpuMs: 50, subrequests: 100, }, logpush: true, observability: { enabled: true, logs: { persist: true, }, traces: { persist: true, }, }, workersDev: false, previewUrls: true, unsafe: { metadata: { build: "docs-example" }, }, env: { API_ORIGIN: bindings.text("https://api.example.com"), DATABASE: bindings.d1({ name: "images-db", }), IMAGES: bindings.r2({ name: "source-images", }), }, exports: { Admin: exports.worker({ cache: { enabled: true, }, }), Counter: exports.durableObject({ storage: "sqlite", }), }, }, }));

### Bindings

import { bindings, defineConfig } from "cf/config";

import * as entrypoint from "./src/index" with { type: "cf-worker" };

export default defineConfig({

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: "binding-showcase", (name reference)

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

MY_AGENT_MEMORY: bindings.agentMemory({ (agentMemory reference)

`agentMemory`BuilderLink to agentMemory

`agentMemory(options: AgentMemoryBindingOptions): AgentMemoryBinding;`

Agent Memory namespace binding. Each binding is scoped to a namespace and allows agents to persist and recall memory.

Options (2)

`namespace: string`
    The user-chosen namespace name. Must exist in Cloudflare at deploy time.

`dev?: BindingDevOptions`
    Options that only apply during local development.

namespace: "my-namespace", (namespace reference)

`namespace`RequiredLink to namespace

`namespace: string`

The user-chosen namespace name. Must exist in Cloudflare at deploy time.

}),

MY_AI: bindings.ai(), (ai reference)

`ai`BuilderLink to ai

`ai<TAiModelList extends AiModelListType = AiModels>(options?: AiBindingOptions): TypedAiBinding<TAiModelList>;`

Binding to the Workers AI project. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#workers-ai](https://developers.cloudflare.com/workers/wrangler/configuration/#workers-ai)

Options (1)

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_AI_SEARCH: bindings.aiSearch({ (aiSearch reference)

`aiSearch`BuilderLink to aiSearch

`aiSearch(options: AiSearchBindingOptions): AiSearchBinding;`

AI Search instance binding. Each binding is bound directly to a single pre-existing instance within the "default" namespace.

Options (2)

`name: string`
    The user-chosen instance name. Must exist in Cloudflare at deploy time.

`dev?: BindingDevOptions`
    Options that only apply during local development.

name: "my-resource", (name reference)

`name`RequiredLink to name

`name: string`

The user-chosen instance name. Must exist in Cloudflare at deploy time.

}),

MY_AI_SEARCH_NAMESPACE: bindings.aiSearchNamespace({ (aiSearchNamespace reference)

`aiSearchNamespace`BuilderLink to aiSearchNamespace

`aiSearchNamespace(options: AiSearchNamespaceBindingOptions): AiSearchNamespaceBinding;`

AI Search namespace binding. Each binding is scoped to a namespace and allows dynamic instance CRUD within it.

Options (2)

`namespace: string`
    The user-chosen namespace name. Must exist in Cloudflare at deploy time.

`dev?: BindingDevOptions`
    Options that only apply during local development.

namespace: "my-namespace", (namespace reference)

`namespace`RequiredLink to namespace

`namespace: string`

The user-chosen namespace name. Must exist in Cloudflare at deploy time.

}),

MY_ANALYTICS_ENGINE_DATASET: bindings.analyticsEngineDataset(), (analyticsEngineDataset reference)

`analyticsEngineDataset`BuilderLink to analyticsEngineDataset

`analyticsEngineDataset(options?: AnalyticsEngineDatasetBindingOptions): AnalyticsEngineDatasetBinding;`

Binding to an Analytics Engine dataset. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#analytics-engine-datasets](https://developers.cloudflare.com/workers/wrangler/configuration/#analytics-engine-datasets)

Options (1)

`name?: string`
    The name of this dataset to write to.

MY_ARTIFACTS: bindings.artifacts({ (artifacts reference)

`artifacts`BuilderLink to artifacts

`artifacts(options: ArtifactsBindingOptions): ArtifactsBinding;`

Binding to an Artifacts instance. Artifacts provides git-compatible file storage on Cloudflare Workers.

Options (2)

`namespace: string`
    The namespace to use.

`dev?: BindingDevOptions`
    Options that only apply during local development.

namespace: "my-namespace", (namespace reference)

`namespace`RequiredLink to namespace

`namespace: string`

The namespace to use.

}),

MY_ASSETS: bindings.assets(), (assets reference)

`assets`BuilderLink to assets

`assets(): AssetsBinding;`

Binding to the Worker's static assets. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#assets](https://developers.cloudflare.com/workers/wrangler/configuration/#assets)

MY_BROWSER: bindings.browser(), (browser reference)

`browser`BuilderLink to browser

`browser(options?: BrowserBindingOptions): BrowserBinding;`

Binding to a headless browser usable from the Worker. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#browser-rendering](https://developers.cloudflare.com/workers/wrangler/configuration/#browser-rendering)

Options (1)

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_D1: bindings.d1(), (d1 reference)

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

MY_DISPATCH_NAMESPACE: bindings.dispatchNamespace(), (dispatchNamespace reference)

`dispatchNamespace`BuilderLink to dispatchNamespace

`dispatchNamespace(options?: DispatchNamespaceBindingOptions): DispatchNamespaceBinding;`

Binding to a Workers for Platforms dispatch namespace. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#dispatch-namespace-bindings-workers-for-platforms](https://developers.cloudflare.com/workers/wrangler/configuration/#dispatch-namespace-bindings-workers-for-platforms)

Options (3)

`namespace?: string`
    The namespace to bind to.

`outbound?: { /** Name of the Worker handling the outbound requests. */ worker: string; /** (Optional) List of parameter names, for sending context from your dispatch Worker to the outbound handler. */ parameters?: string[]; }`
    Details about the outbound Worker which will handle outbound requests from your namespace.

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_DURABLE_OBJECT: bindings.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject<TWorker$1 extends WorkerReference, TExportName$1 extends DurableObjectExportName<TWorker$1>>(options: DurableObjectBindingOptions<TWorker$1, TExportName$1>): DurableObjectBinding<TWorker$1, TExportName$1>;`

Binding to a Durable Object class. `worker` is the name or config of the Worker that defines the class; `exportName` is the exported class name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects)

Options (2)

`worker: TWorker$1`
    The name or config of the Worker that defines the Durable Object class.

`exportName: TExportName$1`
    The exported class name of the Durable Object.

worker: "my-worker", (worker reference)

`worker`RequiredLink to worker

`worker: TWorker$1`

The name or config of the Worker that defines the Durable Object class.

exportName: "MyDurableObject", (exportName reference)

`exportName`RequiredLink to exportName

`exportName: TExportName$1`

The exported class name of the Durable Object.

}),

MY_FLAGSHIP: bindings.flagship(), (flagship reference)

`flagship`BuilderLink to flagship

`flagship(options?: FlagshipBindingOptions): FlagshipBinding;`

Binding to a Flagship feature-flag service.

Options (2)

`id?: string`
    The Flagship app ID to bind to.

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_HYPERDRIVE: bindings.hyperdrive({ (hyperdrive reference)

`hyperdrive`BuilderLink to hyperdrive

`hyperdrive(options: HyperdriveBindingOptions): HyperdriveBinding;`

Binding to a Hyperdrive configuration. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#hyperdrive](https://developers.cloudflare.com/workers/wrangler/configuration/#hyperdrive)

Options (2)

`id: string`
    The ID of the Hyperdrive configuration.

`dev?: { /** The database connection string used during local development. */ connectionString?: string; }`
    Options that only apply during local development.

id: "resource-id", (id reference)

`id`RequiredLink to id

`id: string`

The ID of the Hyperdrive configuration.

}),

MY_IMAGES: bindings.images(), (images reference)

`images`BuilderLink to images

`images(options?: ImagesBindingOptions): ImagesBinding$1;`

Binding to Cloudflare Images. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#images](https://developers.cloudflare.com/workers/wrangler/configuration/#images)

Options (1)

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_JSON: bindings.json({ feature: true }), (json reference)

`json`BuilderLink to json

`json<T$1 extends Json>(value: T$1): JsonBinding<T$1>;`

Inline JSON value made available to the Worker on `env` under the binding name.

MY_KV: bindings.kv(), (kv reference)

`kv`BuilderLink to kv

`kv<TKey extends string = string>(options?: KvBindingOptions): TypedKvBinding<TKey>;`

Binding to a Workers KV namespace. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#kv-namespaces](https://developers.cloudflare.com/workers/wrangler/configuration/#kv-namespaces)

Options (2)

`id?: string`
    The ID of the KV namespace.

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_LOGFWDR: bindings.logfwdr({ (logfwdr reference)

`logfwdr`BuilderLink to logfwdr

`logfwdr(options: LogfwdrBindingOptions): LogfwdrBinding;`

Binding for forwarding logs to logfwdr.

Options (1)

`destination: string`
    The destination for this logged message.

destination: "my-destination", (destination reference)

`destination`RequiredLink to destination

`destination: string`

The destination for this logged message.

}),

MY_MEDIA: bindings.media(), (media reference)

`media`BuilderLink to media

`media(options?: MediaBindingOptions): MediaBinding$1;`

Binding to Cloudflare Media Transformations.

Options (1)

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_MTLS_CERTIFICATE: bindings.mtlsCertificate({ (mtlsCertificate reference)

`mtlsCertificate`BuilderLink to mtlsCertificate

`mtlsCertificate(options: MtlsCertificateBindingOptions): MtlsCertificateBinding;`

Binding to an uploaded mTLS certificate. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#mtls-certificates](https://developers.cloudflare.com/workers/wrangler/configuration/#mtls-certificates)

Options (2)

`id: string`
    The UUID of the uploaded mTLS certificate.

`dev?: BindingDevOptions`
    Options that only apply during local development.

id: "resource-id", (id reference)

`id`RequiredLink to id

`id: string`

The UUID of the uploaded mTLS certificate.

}),

MY_PIPELINE: bindings.pipeline({ (pipeline reference)

`pipeline`BuilderLink to pipeline

`pipeline<TRecord extends PipelineRecord = PipelineRecord>(options: PipelineBindingOptions): TypedPipelineBinding<TRecord>;`

Binding to a Cloudflare Pipeline.

Options (2)

`name: string`
    Name of the Pipeline to bind.

`dev?: BindingDevOptions`
    Options that only apply during local development.

name: "my-resource", (name reference)

`name`RequiredLink to name

`name: string`

Name of the Pipeline to bind.

}),

MY_QUEUE: bindings.queue(), (queue reference)

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

MY_R2: bindings.r2(), (r2 reference)

`r2`BuilderLink to r2

`r2(options?: R2BindingOptions): R2Binding;`

Binding to an R2 bucket. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#r2-buckets](https://developers.cloudflare.com/workers/wrangler/configuration/#r2-buckets)

Options (3)

`name?: string`
    The name of this R2 bucket at the edge.

`jurisdiction?: string`
    The jurisdiction that the bucket exists in. Default if not present.

`dev?: BindingDevOptions & { /** EXPERIMENTAL: credentials for the local S3-compatible endpoint. */ experimentalS3Credentials?: { accessKeyId: string; secretAccessKey: string; }; }`
    Settings that only apply to local development.

MY_RATE_LIMIT: bindings.rateLimit({ (rateLimit reference)

`rateLimit`BuilderLink to rateLimit

`rateLimit(options: RateLimitBindingOptions): RateLimitBinding;`

Binding to a rate limiter.

Options (2)

`namespace: string`
    The namespace ID for this rate limiter.

`simple: { /** The maximum number of requests allowed in the time period. */ limit: number; /** The time period in seconds (10 for ten seconds, 60 for one minute). */ period: 10 | 60; }`
    Simple rate limiting configuration.

namespace: "my-namespace", (namespace reference)

`namespace`RequiredLink to namespace

`namespace: string`

The namespace ID for this rate limiter.

simple: { (simple reference)

`simple`RequiredLink to simple

`simple: { /** The maximum number of requests allowed in the time period. */ limit: number; /** The time period in seconds (10 for ten seconds, 60 for one minute). */ period: 10 | 60; }`

Simple rate limiting configuration.

limit: 1, (limit reference)

`limit`RequiredLink to limit

`limit: number`

The maximum number of requests allowed in the time period.

period: 10, (period reference)

`period`RequiredLink to period

`period: 10 | 60`

The time period in seconds (10 for ten seconds, 60 for one minute).

},

}),

MY_SECRET: bindings.secret(), (secret reference)

`secret`BuilderLink to secret

`secret(): SecretBinding;`

Declares a secret that is required by your Worker, exposed on `env` under the binding name. When defined, this binding: - Replaces .dev.vars/.env/process.env inference for type generation - Enables local dev validation with warnings for missing secrets For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#secrets-configuration-property](https://developers.cloudflare.com/workers/wrangler/configuration/#secrets-configuration-property)

MY_SECRETS_STORE_SECRET: bindings.secretsStoreSecret({ (secretsStoreSecret reference)

`secretsStoreSecret`BuilderLink to secretsStoreSecret

`secretsStoreSecret(options: SecretsStoreSecretBindingOptions): SecretsStoreSecretBinding;`

Binding to a Secrets Store secret.

Options (2)

`storeId: string`
    ID of the secret store.

`secretName: string`
    Name of the secret.

storeId: "store-id", (storeId reference)

`storeId`RequiredLink to storeId

`storeId: string`

ID of the secret store.

secretName: "my-secret", (secretName reference)

`secretName`RequiredLink to secretName

`secretName: string`

Name of the secret.

}),

MY_SEND_EMAIL: bindings.sendEmail({ (sendEmail reference)

`sendEmail`BuilderLink to sendEmail

`sendEmail(options?: SendEmailBindingOptions): SendEmailBinding;`

Binding for sending email from inside the Worker. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#email-bindings](https://developers.cloudflare.com/workers/wrangler/configuration/#email-bindings)

Options (6)

`destinationAddress: string`
    If this binding should be restricted to a specific verified address.

`allowedDestinationAddresses?: never`
    

`destinationAddress?: never`
    

`allowedDestinationAddresses: string[]`
    If this binding should be restricted to a set of verified addresses.

`allowedSenderAddresses?: string[]`
    If this binding should be restricted to a set of sender addresses.

`dev?: BindingDevOptions`
    Options that only apply during local development.

destinationAddress: "value", (destinationAddress reference)

`destinationAddress`RequiredLink to destinationAddress

`destinationAddress: string`

If this binding should be restricted to a specific verified address.

}),

MY_STREAM: bindings.stream(), (stream reference)

`stream`BuilderLink to stream

`stream(options?: StreamBindingOptions): StreamBinding$1;`

Binding to Cloudflare Stream.

Options (1)

`dev?: BindingDevOptions`
    Options that only apply during local development.

MY_TEXT: bindings.text("production"), (text reference)

`text`BuilderLink to text

`text<T$1 extends string>(value: T$1): TextBinding<T$1>;`

Inline string value made available to the Worker on `env` under the binding name. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables](https://developers.cloudflare.com/workers/wrangler/configuration/#environment-variables)

MY_VECTORIZE: bindings.vectorize({ (vectorize reference)

`vectorize`BuilderLink to vectorize

`vectorize(options: VectorizeBindingOptions): VectorizeBinding;`

Binding to a Vectorize index. For reference, see [https://developers.cloudflare.com/workers/wrangler/configuration/#vectorize-indexes](https://developers.cloudflare.com/workers/wrangler/configuration/#vectorize-indexes)

Options (2)

`name: string`
    The name of the Vectorize index.

`dev?: BindingDevOptions`
    Options that only apply during local development.

name: "my-resource", (name reference)

`name`RequiredLink to name

`name: string`

The name of the Vectorize index.

}),

MY_VERSION_METADATA: bindings.versionMetadata(), (versionMetadata reference)

`versionMetadata`BuilderLink to versionMetadata

`versionMetadata(): VersionMetadataBinding;`

Binding to the Worker version's metadata.

MY_VPC_NETWORK: bindings.vpcNetwork({ (vpcNetwork reference)

`vpcNetwork`BuilderLink to vpcNetwork

`vpcNetwork(options: VpcNetworkBindingOptions): VpcNetworkBinding;`

Binding to a VPC network.

Options (5)

`tunnelId: string`
    The tunnel ID of the Cloudflare Tunnel to route traffic through. Mutually exclusive with `networkId`.

`networkId?: never`
    

`dev?: BindingDevOptions`
    Options that only apply during local development.

`tunnelId?: never`
    

`networkId: string`
    The network ID to route traffic through. Mutually exclusive with `tunnelId`.

tunnelId: "tunnel-id", (tunnelId reference)

`tunnelId`RequiredLink to tunnelId

`tunnelId: string`

The tunnel ID of the Cloudflare Tunnel to route traffic through. Mutually exclusive with `networkId`.

}),

MY_VPC_SERVICE: bindings.vpcService({ (vpcService reference)

`vpcService`BuilderLink to vpcService

`vpcService(options: VpcServiceBindingOptions): VpcServiceBinding;`

Binding to a VPC service.

Options (2)

`id: string`
    The service ID of the VPC connectivity service.

`dev?: BindingDevOptions`
    Options that only apply during local development.

id: "resource-id", (id reference)

`id`RequiredLink to id

`id: string`

The service ID of the VPC connectivity service.

}),

MY_WORKER: bindings.worker({ (worker reference)

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

worker: "my-worker", (worker reference)

`worker`RequiredLink to worker

`worker: TWorker$1`

The name or config of the bound Worker.

}),

MY_WORKER_LOADER: bindings.workerLoader(), (workerLoader reference)

`workerLoader`BuilderLink to workerLoader

`workerLoader(): WorkerLoaderBinding;`

Binding to a Worker Loader.

MY_WORKFLOW: bindings.workflow({ (workflow reference)

`workflow`BuilderLink to workflow

`workflow<TWorker$1 extends WorkerReference, TExportName$1 extends WorkflowExportName<TWorker$1>>(options: WorkflowBindingOptions<TWorker$1, TExportName$1>): WorkflowBinding<TWorker$1, NoInfer<TExportName$1>>;`

Create a Workflow binding. `worker` may be a Worker config reference or a Worker name. `exportName` must be a valid `WorkflowEntrypoint` export for the given Worker.

Options (3)

`name: string`
    The name of the Workflow.

`worker: TWorker$1`
    The name or config of the Worker that defines the Workflow.

`exportName: TExportName$1`
    The exported class name of the Workflow.

name: "my-resource", (name reference)

`name`RequiredLink to name

`name: string`

The name of the Workflow.

worker: "my-worker", (worker reference)

`worker`RequiredLink to worker

`worker: TWorker$1`

The name or config of the Worker that defines the Workflow.

exportName: "MyWorkflow", (exportName reference)

`exportName`RequiredLink to exportName

`exportName: TExportName$1`

The exported class name of the Workflow.

}),

},

},

});

import { bindings, defineConfig } from "cf/config"; import * as entrypoint from "./src/index" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "binding-showcase", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", env: { MY_AGENT_MEMORY: bindings.agentMemory({ namespace: "my-namespace", }), MY_AI: bindings.ai(), MY_AI_SEARCH: bindings.aiSearch({ name: "my-resource", }), MY_AI_SEARCH_NAMESPACE: bindings.aiSearchNamespace({ namespace: "my-namespace", }), MY_ANALYTICS_ENGINE_DATASET: bindings.analyticsEngineDataset(), MY_ARTIFACTS: bindings.artifacts({ namespace: "my-namespace", }), MY_ASSETS: bindings.assets(), MY_BROWSER: bindings.browser(), MY_D1: bindings.d1(), MY_DISPATCH_NAMESPACE: bindings.dispatchNamespace(), MY_DURABLE_OBJECT: bindings.durableObject({ worker: "my-worker", exportName: "MyDurableObject", }), MY_FLAGSHIP: bindings.flagship(), MY_HYPERDRIVE: bindings.hyperdrive({ id: "resource-id", }), MY_IMAGES: bindings.images(), MY_JSON: bindings.json({ feature: true }), MY_KV: bindings.kv(), MY_LOGFWDR: bindings.logfwdr({ destination: "my-destination", }), MY_MEDIA: bindings.media(), MY_MTLS_CERTIFICATE: bindings.mtlsCertificate({ id: "resource-id", }), MY_PIPELINE: bindings.pipeline({ name: "my-resource", }), MY_QUEUE: bindings.queue(), MY_R2: bindings.r2(), MY_RATE_LIMIT: bindings.rateLimit({ namespace: "my-namespace", simple: { limit: 1, period: 10, }, }), MY_SECRET: bindings.secret(), MY_SECRETS_STORE_SECRET: bindings.secretsStoreSecret({ storeId: "store-id", secretName: "my-secret", }), MY_SEND_EMAIL: bindings.sendEmail({ destinationAddress: "value", }), MY_STREAM: bindings.stream(), MY_TEXT: bindings.text("production"), MY_VECTORIZE: bindings.vectorize({ name: "my-resource", }), MY_VERSION_METADATA: bindings.versionMetadata(), MY_VPC_NETWORK: bindings.vpcNetwork({ tunnelId: "tunnel-id", }), MY_VPC_SERVICE: bindings.vpcService({ id: "resource-id", }), MY_WORKER: bindings.worker({ worker: "my-worker", }), MY_WORKER_LOADER: bindings.workerLoader(), MY_WORKFLOW: bindings.workflow({ name: "my-resource", worker: "my-worker", exportName: "MyWorkflow", }), }, }, });

### Triggers

import { defineConfig, triggers } from "cf/config";

import * as entrypoint from "./src/index" with { type: "cf-worker" };

export default defineConfig({

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: "trigger-showcase", (name reference)

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

pattern: "example.com/*", (pattern reference)

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

name: "jobs", (name reference)

`name`RequiredLink to name

`name: string`

The name of the queue from which this consumer should consume.

maxBatchSize: 20, (maxBatchSize reference)

`maxBatchSize`OptionalLink to maxBatchSize

`maxBatchSize?: number`

The maximum number of messages per batch.

}),

triggers.scheduled({ (scheduled reference)

`scheduled`BuilderLink to scheduled

`scheduled(options: ScheduledTriggerOptions): ScheduledTrigger;`

Scheduled (cron) trigger — invokes this Worker on the given schedules. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

Options (1)

`schedule: string`
    A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

schedule: "0 * * * *", (schedule reference)

`schedule`RequiredLink to schedule

`schedule: string`

A "cron" definition to trigger a Worker's "scheduled" function. Lets you call Workers periodically, much like a cron job. More details here [https://developers.cloudflare.com/workers/platform/cron-triggers](https://developers.cloudflare.com/workers/platform/cron-triggers)

}),

triggers.email({ (email reference)

`email`BuilderLink to email

`email(options: EmailTriggerOptions): EmailTrigger;`

Email trigger — invokes this Worker for the configured Email Routing addresses.

Options (1)

`addresses: string[]`
    Inbound Email Routing addresses handled by this Worker. Each entry is a literal recipient address (e.g. `"support@example.com"`) or a `*@domain` catch-all (e.g. `"*@example.com"`).

addresses: ["support@example.com"], (addresses reference)

`addresses`RequiredLink to addresses

`addresses: string[]`

Inbound Email Routing addresses handled by this Worker. Each entry is a literal recipient address (e.g. `"support@example.com"`) or a `*@domain` catch-all (e.g. `"*@example.com"`).

}),

triggers.connect({ (connect reference)

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

protocol: "tcp", (protocol reference)

`protocol`RequiredLink to protocol

`protocol: "tcp"`

The type definition does not include a description.

port: 5432, (port reference)

`port`RequiredLink to port

`port: number`

The port to listen on.

}),

],

},

});

import { defineConfig, triggers } from "cf/config"; import * as entrypoint from "./src/index" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "trigger-showcase", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", triggers: [ triggers.fetch({ pattern: "example.com/*", zone: "example.com", }), triggers.queue({ name: "jobs", maxBatchSize: 20, }), triggers.scheduled({ schedule: "0 * * * *", }), triggers.email({ addresses: ["support@example.com"], }), triggers.connect({ protocol: "tcp", port: 5432, }), ], }, });

### Exports

import { defineConfig, exports } from "cf/config";

import * as entrypoint from "./src/index" with { type: "cf-worker" };

export default defineConfig({

worker: { (worker reference)

`worker`OptionalLink to worker

`worker?: ConfigInput<WorkerConfig>`

The Worker defined by this configuration.

name: "export-showcase", (name reference)

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

LiveClass: exports.durableObject({ (durableObject reference)

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

`storage: "sqlite"`

Selects the SQLite-backed storage engine (recommended for new classes).

}),

RemovedClass: exports.durableObject({ (durableObject reference)

`durableObject`BuilderLink to durableObject

`durableObject(options: DurableObjectDeletedExportOptions): DurableObjectDeletedExport;`

Retire a provisioned Durable Object namespace whose class has been removed from code.

Options (1)

`state: "deleted"`
    

state: "deleted", (state reference)

`state`RequiredLink to state

`state: "deleted"`

The type definition does not include a description.

}),

OldClass: exports.durableObject({ (durableObject reference)

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

renamedTo: "NewClass", (renamedTo reference)

`renamedTo`RequiredLink to renamedTo

`renamedTo: string`

The destination class name. Must be a valid JavaScript identifier and must appear as a live (`state: "created"`) `durableObject` entry in the same `exports` map.

}),

OutgoingClass: exports.durableObject({ (durableObject reference)

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

transferredTo: "target-worker", (transferredTo reference)

`transferredTo`RequiredLink to transferredTo

`transferredTo: string`

The destination Worker. Must reference a Worker in the same account.

}),

IncomingClass: exports.durableObject({ (durableObject reference)

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

`storage: "sqlite"`

Selects the SQLite-backed storage engine (recommended for new classes).

transferFrom: "source-worker", (transferFrom reference)

`transferFrom`RequiredLink to transferFrom

`transferFrom: string`

The source Worker for the two-phase cross-Worker transfer.

}),

ApiEntrypoint: exports.worker({ (worker reference)

`worker`BuilderLink to worker

`worker(options?: WorkerEntrypointExportOptions): WorkerEntrypointExport;`

Declares a WorkerEntrypoint export defined by this Worker.

Options (1)

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`
    

cache: { (cache reference)

`cache`OptionalLink to cache

`cache?: { /** Whether cache is enabled for this entrypoint. */ enabled: boolean; }`

The type definition does not include a description.

enabled: true, (enabled reference)

`enabled`RequiredLink to enabled

`enabled: boolean`

Whether cache is enabled for this entrypoint.

},

}),

CheckoutWorkflow: exports.workflow({ (workflow reference)

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

name: "checkout-workflow", (name reference)

`name`RequiredLink to name

`name: string`

The name of the Workflow. It identifies the Workflow's instances and must be unique within the account.

limits: { (limits reference)

`limits`OptionalLink to limits

`limits?: { /** Maximum number of steps a single Workflow instance may run. */ steps?: number; }`

The type definition does not include a description.

steps: 100, (steps reference)

`steps`OptionalLink to steps

`steps?: number`

Maximum number of steps a single Workflow instance may run.

},

}),

},

},

});

import { defineConfig, exports } from "cf/config"; import * as entrypoint from "./src/index" with { type: "cf-worker" }; export default defineConfig({ worker: { name: "export-showcase", entrypoint, compatibilityDate: "<COMPATIBILITY_DATE>", exports: { LiveClass: exports.durableObject({ storage: "sqlite", }), RemovedClass: exports.durableObject({ state: "deleted", }), OldClass: exports.durableObject({ state: "renamed", renamedTo: "NewClass", }), OutgoingClass: exports.durableObject({ state: "transferred", transferredTo: "target-worker", }), IncomingClass: exports.durableObject({ state: "expecting-transfer", storage: "sqlite", transferFrom: "source-worker", }), ApiEntrypoint: exports.worker({ cache: { enabled: true, }, }), CheckoutWorkflow: exports.workflow({ name: "checkout-workflow", limits: { steps: 100, }, }), }, }, });

[Previouscloudflare.config.ts](https://developers.cloudflare.com/cf/projects/cloudflare-config/)[NextCoding agents](https://developers.cloudflare.com/cf/agents/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/projects/config-explorer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
