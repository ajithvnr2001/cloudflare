---
url: https://developers.cloudflare.com/agents/runtime/operations/configuration/
title: Configuration \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:22.230833+00:00
---

# Configuration · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/operations/configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

Runtime

  4. /Operations
  5. /Configuration



# Configuration

Last updated Aug 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/runtime/operations/configuration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewProject structureWrangler configuration file Key fieldsTypeScript configurationVite configurationGenerating types Automatic generation Custom output path Without runtime types Example generated output Manual type definition Adding to package.jsonEnvironment variables and secrets Local development (.env) Production secrets Non-secret variables Environment-specific variablesLocal development Starting the dev server Local state persistence Clearing local state Inspecting local SQLiteDashboard setup Automatic resources Viewing Durable Objects Real-time logsProduction deployment Basic deploy Custom domain Preview deployments RollbacksMulti-environment setup Environment configuration Deploying to environments Separate Durable ObjectsAgent class lifecycle Adding a new agent Renaming an agent class Deleting an agent class Class lifecycle best practicesTroubleshooting No such Durable Object class Cannot find module in types Secrets not loading locally Migration tag conflict (legacy migrations only)Next steps

This guide covers everything you need to configure agents for local development and production deployment, including Wrangler configuration file setup, type generation, environment variables, and the Cloudflare dashboard.

## Project structure

The typical file structure for an Agent project created from `npm create cloudflare@latest agents-starter -- --template cloudflare/agents-starter` follows:

  * src/ 
    * index.ts your Agent definition
  * public/ 
    * index.html
  * test/ 
    * index.spec.ts your tests
  * package.json
  * tsconfig.json
  * vitest.config.mts
  * worker-configuration.d.ts
  * wrangler.jsonc your Workers and Agent configuration



## Wrangler configuration file

The `wrangler.jsonc` file configures your Cloudflare Worker and its bindings. Here is a complete example for an agents project:
    
    
    {
    	"$schema": "node_modules/wrangler/config-schema.json",
    	"name": "my-agent-app",
    	"main": "src/server.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": ["nodejs_compat"],
    
    	// Static assets (optional)
    	"assets": {
    		"directory": "public",
    		"binding": "ASSETS",
    	},
    
    	// Durable Object bindings for agents
    	"durable_objects": {
    		"bindings": [
    			{
    				"name": "MyAgent",
    				"class_name": "MyAgent",
    			},
    			{
    				"name": "ChatAgent",
    				"class_name": "ChatAgent",
    			},
    		],
    	},
    
      // Provision storage for each agent class
    	"exports": {
    		"MyAgent": {
    			"type": "durable-object",
    			"storage": "sqlite",
    		},
    		"ChatAgent": {
    			"type": "durable-object",
    			"storage": "sqlite",
    		},
    	},
    
    	// AI binding (optional, for Workers AI)
    	"ai": {
    		"binding": "AI",
    	},
    
    	// Observability (recommended)
    	"observability": {
    		"enabled": true,
    	},
    }
    
    
    "$schema" = "node_modules/wrangler/config-schema.json"
    name = "my-agent-app"
    main = "src/server.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "nodejs_compat" ]
    
    [assets]
    directory = "public"
    binding = "ASSETS"
    
    [[durable_objects.bindings]]
    name = "MyAgent"
    class_name = "MyAgent"
    
    [[durable_objects.bindings]]
    name = "ChatAgent"
    class_name = "ChatAgent"
    
    [exports.MyAgent]
    type = "durable-object"
    storage = "sqlite"
    
    [exports.ChatAgent]
    type = "durable-object"
    storage = "sqlite"
    
    [ai]
    binding = "AI"
    
    [observability]
    enabled = true

### Key fields

#### `compatibility_flags`

The `nodejs_compat` flag is required for agents:
    
    
    {
    	"compatibility_flags": ["nodejs_compat"],
    }
    
    
    compatibility_flags = [ "nodejs_compat" ]

This enables Node.js compatibility mode, which agents depend on for crypto, streams, and other Node.js APIs.

#### `durable_objects.bindings`

Each agent class needs a binding:
    
    
    {
    	"durable_objects": {
    		"bindings": [
    			{
    				"name": "Counter",
    				"class_name": "Counter",
    			},
    		],
    	},
    }
    
    
    [[durable_objects.bindings]]
    name = "Counter"
    class_name = "Counter"

Field | Description  
---|---  
`name` | The property name on `env`. Use this in code: `env.Counter`  
`class_name` | Must match the exported class name exactly  
  
When `name` and `class_name` differ

When `name` and `class_name` differ, follow the pattern shown below:
    
    
    {
    	"durable_objects": {
    		"bindings": [
    			{
    				"name": "COUNTER_DO",
    				"class_name": "CounterAgent",
    			},
    		],
    	},
    }
    
    
    [[durable_objects.bindings]]
    name = "COUNTER_DO"
    class_name = "CounterAgent"

This is useful when you want environment variable-style naming (`COUNTER_DO`) but more descriptive class names (`CounterAgent`).

#### `exports`

The `exports` field declares each Agent class your Worker exports and the storage backend Cloudflare should use for it:
    
    
    {
    	"exports": {
    		"MyAgent": {
    			"type": "durable-object",
    			"storage": "sqlite",
    		},
    	},
    }
    
    
    [exports.MyAgent]
    type = "durable-object"
    storage = "sqlite"

Field | Description  
---|---  
`type` | The kind of export. Always `"durable-object"` for an Agent.  
`storage` | The storage backend. Use `"sqlite"` for new Agents (recommended).  
  
For details on renaming, deleting, or transferring Agent classes, refer to [Durable Object class exports](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/). Existing Workers using the legacy `migrations` array continue to work — refer to [Durable Object class migrations (legacy)](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/).

#### `assets`

For serving static files (HTML, CSS, JS):
    
    
    {
    	"assets": {
    		"directory": "public",
    		"binding": "ASSETS",
    	},
    }
    
    
    [assets]
    directory = "public"
    binding = "ASSETS"

With a binding, you can serve assets programmatically:
    
    
    export default {
    	async fetch(request, env) {
    		// Static assets are served by the worker automatically by default
    
    		// Route the request to the appropriate agent
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		// Add your own routing logic here
    		return new Response("Not found", { status: 404 });
    	},
    };
    
    
    export default {
    	async fetch(request: Request, env: Env) {
    		// Static assets are served by the worker automatically by default
    
    		// Route the request to the appropriate agent
    		const agentResponse = await routeAgentRequest(request, env);
    		if (agentResponse) return agentResponse;
    
    		// Add your own routing logic here
    		return new Response("Not found", { status: 404 });
    	},
    } satisfies ExportedHandler<Env>;

#### `ai`

For Workers AI integration:
    
    
    {
    	"ai": {
    		"binding": "AI",
    	},
    }
    
    
    [ai]
    binding = "AI"

Access in your agent:
    
    
    const response = await this.env.AI.run("@cf/meta/llama-3-8b-instruct", {
    	prompt: "Hello!",
    });
    
    
    const response = await this.env.AI.run("@cf/meta/llama-3-8b-instruct", {
    	prompt: "Hello!",
    });

## TypeScript configuration

The Agents SDK ships a shared `tsconfig.json` that sets all the compiler options needed for agents projects — including the `ES2021` target required for `@callable()` decorators, strict mode, bundler module resolution, and Workers types.

Extend it in your `tsconfig.json`:
    
    
    {
    	"extends": "agents/tsconfig"
    }

This is equivalent to:
    
    
    {
    	"compilerOptions": {
    		"target": "ES2021",
    		"lib": ["ES2022", "DOM", "DOM.Iterable"],
    		"jsx": "react-jsx",
    		"module": "ES2022",
    		"moduleResolution": "bundler",
    		"types": ["node", "@cloudflare/workers-types", "vite/client"],
    		"allowImportingTsExtensions": true,
    		"noEmit": true,
    		"isolatedModules": true,
    		"verbatimModuleSyntax": true,
    		"esModuleInterop": true,
    		"forceConsistentCasingInFileNames": true,
    		"strict": true,
    		"skipLibCheck": true
    	}
    }

You can override individual options as needed:
    
    
    {
    	"extends": "agents/tsconfig",
    	"compilerOptions": {
    		"jsx": "preserve"
    	}
    }

Caution

Do not set `"experimentalDecorators": true`. The Agents SDK uses [TC39 standard decorators ↗︎](https://github.com/tc39/proposal-decorators), not TypeScript legacy decorators. Enabling `experimentalDecorators` applies an incompatible transform that silently breaks `@callable()` at runtime.

## Vite configuration

The Agents SDK provides a Vite plugin that handles TC39 decorator transforms. Vite 8 uses Oxc for transpilation, which does not yet support TC39 decorators — without this plugin, `@callable()` and other decorators will fail at runtime.

Add the plugin to your `vite.config.ts`:
    
    
    import { cloudflare } from "@cloudflare/vite-plugin";
    import react from "@vitejs/plugin-react";
    import agents from "agents/vite";
    import { defineConfig } from "vite";
    
    export default defineConfig({
    	plugins: [agents(), react(), cloudflare()],
    });

vite.config.tsts
    
    
    import { cloudflare } from "@cloudflare/vite-plugin";
    import react from "@vitejs/plugin-react";
    import agents from "agents/vite";
    import { defineConfig } from "vite";
    
    export default defineConfig({
    	plugins: [agents(), react(), cloudflare()],
    });

The `agents()` plugin is safe to include even if your project does not use decorators. It only runs the transform on files that contain `@` syntax.

The starter template and all examples include this plugin by default. If you encounter `SyntaxError: Invalid or unexpected token` with decorators, refer to [Callable methods — Troubleshooting](https://developers.cloudflare.com/agents/runtime/lifecycle/callable-methods/#troubleshooting).

## Generating types

Wrangler can generate TypeScript types for your bindings.

### Automatic generation

Run the types command:
    
    
    npx wrangler types

This creates or updates `worker-configuration.d.ts` with your `Env` type.

### Custom output path

Specify a custom path:
    
    
    npx wrangler types env.d.ts

### Without runtime types

For cleaner output (recommended for agents):
    
    
    npx wrangler types env.d.ts --include-runtime false

This generates just your bindings without Cloudflare runtime types.

### Example generated output
    
    
    // env.d.ts (generated)
    declare namespace Cloudflare {
    	interface Env {
    		OPENAI_API_KEY: string;
    		Counter: DurableObjectNamespace;
    		ChatAgent: DurableObjectNamespace;
    	}
    }
    interface Env extends Cloudflare.Env {}

### Manual type definition

You can also define types manually:
    
    
    // env.d.ts
    
    
    // env.d.ts
    import type { Counter } from "./src/agents/counter";
    import type { ChatAgent } from "./src/agents/chat";
    
    interface Env {
    	// Secrets
    	OPENAI_API_KEY: string;
    	WEBHOOK_SECRET: string;
    
    	// Agent bindings
    	Counter: DurableObjectNamespace<Counter>;
    	ChatAgent: DurableObjectNamespace<ChatAgent>;
    
    	// Other bindings
    	AI: Ai;
    	ASSETS: Fetcher;
    	MY_KV: KVNamespace;
    }

### Adding to package.json

Add a script for easy regeneration:
    
    
    {
    	"scripts": {
    		"types": "wrangler types env.d.ts --include-runtime false"
    	}
    }

## Environment variables and secrets

### Local development (`.env`)

Create a `.env` file for local secrets (add to `.gitignore`):
    
    
    # .env
    OPENAI_API_KEY=sk-...
    GITHUB_WEBHOOK_SECRET=whsec_...
    DATABASE_URL=postgres://...

Access in your agent:
    
    
    class MyAgent extends Agent {
    	async onStart() {
    		const apiKey = this.env.OPENAI_API_KEY;
    	}
    }
    
    
    class MyAgent extends Agent {
    	async onStart() {
    		const apiKey = this.env.OPENAI_API_KEY;
    	}
    }

### Production secrets

Use `wrangler secret` for production:
    
    
    # Add a secret
    npx wrangler secret put OPENAI_API_KEY
    # Enter value when prompted
    
    # List secrets
    npx wrangler secret list
    
    # Delete a secret
    npx wrangler secret delete OPENAI_API_KEY

### Non-secret variables

For non-sensitive configuration, use `vars` in the Wrangler configuration file:
    
    
    {
    	"vars": {
    		"API_BASE_URL": "https://api.example.com",
    		"MAX_RETRIES": "3",
    		"DEBUG_MODE": "false",
    	},
    }
    
    
    [vars]
    API_BASE_URL = "https://api.example.com"
    MAX_RETRIES = "3"
    DEBUG_MODE = "false"

All values must be strings. Parse numbers and booleans in code:
    
    
    const maxRetries = parseInt(this.env.MAX_RETRIES, 10);
    const debugMode = this.env.DEBUG_MODE === "true";
    
    
    const maxRetries = parseInt(this.env.MAX_RETRIES, 10);
    const debugMode = this.env.DEBUG_MODE === "true";

### Environment-specific variables

Use `env` sections for different environments (for example, staging, production):
    
    
    {
    	"name": "my-agent",
    	"vars": {
    		"API_URL": "https://api.example.com",
    	},
    
    	"env": {
    		"staging": {
    			"vars": {
    				"API_URL": "https://staging-api.example.com",
    			},
    		},
    		"production": {
    			"vars": {
    				"API_URL": "https://api.example.com",
    			},
    		},
    	},
    }
    
    
    name = "my-agent"
    
    [vars]
    API_URL = "https://api.example.com"
    
    [env.staging.vars]
    API_URL = "https://staging-api.example.com"
    
    [env.production.vars]
    API_URL = "https://api.example.com"

Deploy to specific environment:
    
    
    npx wrangler deploy --env staging
    npx wrangler deploy --env production

## Local development

### Starting the dev server

With Vite (recommended for full stack apps):
    
    
    npx vite dev

Without Vite:
    
    
    npx wrangler dev

### Local state persistence

Durable Object state is persisted locally in `.wrangler/state/`:

  * .wrangler/ 
    * state/ 
      * v3/ 
        * d1/ 
          * miniflare-D1DatabaseObject/ 
            * ... (SQLite files)



### Clearing local state

To reset all local Durable Object state:
    
    
    rm -rf .wrangler/state

Or restart with fresh state:
    
    
    npx wrangler dev --persist-to=""

### Inspecting local SQLite

You can inspect agent state directly:
    
    
    # Find the SQLite file
    ls .wrangler/state/v3/d1/
    
    # Open with sqlite3
    sqlite3 .wrangler/state/v3/d1/miniflare-D1DatabaseObject/*.sqlite

## Dashboard setup

### Automatic resources

When you deploy, Cloudflare automatically creates:

  * **Worker** \- Your deployed code
  * **Durable Object namespaces** \- One per agent class
  * **SQLite storage** \- Attached to each namespace



### Viewing Durable Objects

Log in to the Cloudflare dashboard, then go to Durable Objects.

[ Go to **Durable Objects** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)

Here you can:

  * See all Durable Object namespaces
  * View individual object instances
  * Inspect storage (keys and values)
  * Delete objects



### Real-time logs

View live logs from your agents:
    
    
    npx wrangler tail

Or in the dashboard:

  1. Go to your Worker.
  2. Select the **Observability** tab.
  3. Enable real-time logs.



Filter by:

  * Status (success, error)
  * Search text
  * Sampling rate



## Production deployment

### Basic deploy
    
    
    npx wrangler deploy

This:

  1. Bundles your code
  2. Uploads to Cloudflare
  3. Provisions the Agent's Durable Object namespace storage
  4. Makes it live on `*.workers.dev`



### Custom domain

Add a route in the Wrangler configuration file:
    
    
    {
    	"routes": [
    		{
    			"pattern": "agents.example.com/*",
    			"zone_name": "example.com",
    		},
    	],
    }
    
    
    [[routes]]
    pattern = "agents.example.com/*"
    zone_name = "example.com"

Or use a custom domain (simpler):
    
    
    {
    	"routes": [
    		{
    			"pattern": "agents.example.com",
    			"custom_domain": true,
    		},
    	],
    }
    
    
    [[routes]]
    pattern = "agents.example.com"
    custom_domain = true

### Preview deployments

Deploy without affecting production:
    
    
    npx wrangler deploy --dry-run    # See what would be uploaded
    npx wrangler versions upload     # Upload new version
    npx wrangler versions deploy     # Gradually roll out

### Rollbacks

Roll back to a previous version:
    
    
    npx wrangler rollback

## Multi-environment setup

### Environment configuration

Define environments in the Wrangler configuration file:
    
    
    {
    	"name": "my-agent",
    	"main": "src/server.ts",
    
    	// Base configuration (shared)
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"compatibility_flags": ["nodejs_compat"],
    	"durable_objects": {
    		"bindings": [{ "name": "MyAgent", "class_name": "MyAgent" }],
    	},
    	"exports": {
    		"MyAgent": { "type": "durable-object", "storage": "sqlite" },
    	},
    
    	// Environment overrides
    	"env": {
    		"staging": {
    			"name": "my-agent-staging",
    			"durable_objects": {
    				"bindings": [{ "name": "MyAgent", "class_name": "MyAgent" }],
    			},
    			"vars": {
    				"ENVIRONMENT": "staging",
    			},
    		},
    		"production": {
    			"name": "my-agent-production",
    			"durable_objects": {
    				"bindings": [{ "name": "MyAgent", "class_name": "MyAgent" }],
    			},
    			"vars": {
    				"ENVIRONMENT": "production",
    			},
    		},
    	},
    }
    
    
    name = "my-agent"
    main = "src/server.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    compatibility_flags = [ "nodejs_compat" ]
    
    [[durable_objects.bindings]]
    name = "MyAgent"
    class_name = "MyAgent"
    
    [exports.MyAgent]
    type = "durable-object"
    storage = "sqlite"
    
    [env.staging]
    name = "my-agent-staging"
    
    [[env.staging.durable_objects.bindings]]
    name = "MyAgent"
    class_name = "MyAgent"
    
      [env.staging.vars]
      ENVIRONMENT = "staging"
    
    [env.production]
    name = "my-agent-production"
    
    [[env.production.durable_objects.bindings]]
    name = "MyAgent"
    class_name = "MyAgent"
    
      [env.production.vars]
      ENVIRONMENT = "production"

### Deploying to environments
    
    
    # Deploy to staging
    npx wrangler deploy --env staging
    
    # Deploy to production
    npx wrangler deploy --env production
    
    # Set secrets per environment
    npx wrangler secret put OPENAI_API_KEY --env staging
    npx wrangler secret put OPENAI_API_KEY --env production

### Separate Durable Objects

Named environments do not inherit Durable Object bindings. Repeat the bindings for each environment, as in the multi-environment setup. Each environment gets its own Durable Objects. Staging agents do not share state with production agents.

To explicitly separate:
    
    
    {
    	"env": {
    		"staging": {
    			"durable_objects": {
    				"bindings": [
    					{
    						"name": "MyAgent",
    						"class_name": "MyAgent",
    						"script_name": "my-agent-staging",
    					},
    				],
    			},
    		},
    	},
    }
    
    
    [[env.staging.durable_objects.bindings]]
    name = "MyAgent"
    class_name = "MyAgent"
    script_name = "my-agent-staging"

## Agent class lifecycle

Each Agent maps to a Durable Object class. You manage the lifecycle of those classes (create, rename, delete, transfer) through the [`exports`](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/) field of your Wrangler configuration file.

### Adding a new agent

Declare the new class in the `exports`:
    
    
    {
    	"exports": {
    		"NewAgent": { "type": "durable-object", "storage": "sqlite" },
    	},
    }
    
    
    [exports.NewAgent]
    type = "durable-object"
    storage = "sqlite"

### Renaming an agent class

Replace the entry for the old name with a `renamed` tombstone and add a live entry for the new name:
    
    
    {
    	"exports": {
    		"OldName": {
    			"type": "durable-object",
    			"state": "renamed",
    			"renamed_to": "NewName",
    		},
    		"NewName": { "type": "durable-object", "storage": "sqlite" },
    	},
    }
    
    
    [exports.OldName]
    type = "durable-object"
    state = "renamed"
    renamed_to = "NewName"
    
    [exports.NewName]
    type = "durable-object"
    storage = "sqlite"

Also update:

  1. The class name in code.
  2. The `class_name` in bindings.
  3. Export statements.



### Deleting an agent class

Replace the entry with a `deleted` tombstone:
    
    
    {
    	"exports": {
    		"AgentToKeep": { "type": "durable-object", "storage": "sqlite" },
    		"AgentToDelete": { "type": "durable-object", "state": "deleted" },
    	},
    }
    
    
    [exports.AgentToKeep]
    type = "durable-object"
    storage = "sqlite"
    
    [exports.AgentToDelete]
    type = "durable-object"
    state = "deleted"

Caution

This permanently deletes all data for that class.

### Class lifecycle best practices

  1. **Keep`exports` in sync with your code.** Every Agent class your Worker exports needs an entry.
  2. **Use tombstones, not silent removal.** When retiring a class, leave a `deleted` / `renamed` / `transferred` tombstone in `exports` so Cloudflare reconciles the change explicitly.
  3. **Test locally first.** Lifecycle changes apply on `wrangler deploy`.
  4. **Back up production data** before renaming or deleting.



Existing Workers using the legacy `migrations` array continue to work — refer to [Durable Object class migrations (legacy)](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/) for the legacy reference, or [Migrate from the legacy `migrations` flow](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow) to move to `exports`.

## Troubleshooting

### No such Durable Object class

The class is missing from `exports`. Declare the class and its storage:
    
    
    {
    	"exports": {
    		"MissingClassName": { "type": "durable-object", "storage": "sqlite" },
    	},
    }
    
    
    [exports.MissingClassName]
    type = "durable-object"
    storage = "sqlite"

### Cannot find module in types

Regenerate types:
    
    
    npx wrangler types env.d.ts --include-runtime false

### Secrets not loading locally

Check that `.env` exists and contains the variable:
    
    
    cat .env
    # Should show: MY_SECRET=value

### Migration tag conflict (legacy `migrations` only)

If your Worker uses the legacy [`migrations`](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/) array, each entry must have a unique `tag`:
    
    
    {
    	// Wrong - duplicate tags
    	"migrations": [
    		{ "tag": "v1", "new_sqlite_classes": ["A"] },
    		{ "tag": "v1", "new_sqlite_classes": ["B"] },
    	],
    }
    
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "A" ]
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "B" ]
    
    
    {
    	// Correct - sequential tags
    	"migrations": [
    		{ "tag": "v1", "new_sqlite_classes": ["A"] },
    		{ "tag": "v2", "new_sqlite_classes": ["B"] },
    	],
    }
    
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "A" ]
    
    [[migrations]]
    tag = "v2"
    new_sqlite_classes = [ "B" ]

Consider converting to the declarative [`exports`](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/) field.

## Next steps

### [Agents API](https://developers.cloudflare.com/agents/runtime/agents-api/)

Complete API reference for the Agents SDK.

### [Routing](https://developers.cloudflare.com/agents/runtime/communication/routing/)

Route requests to your agent instances.

### [Schedule tasks](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/)

Background processing with delayed and cron-based tasks.

[PreviousAgent Skills](https://developers.cloudflare.com/agents/runtime/execution/agent-skills/)[NextCross-domain authentication](https://developers.cloudflare.com/agents/runtime/operations/cross-domain-authentication/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/operations/configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
