---
url: https://developers.cloudflare.com/workers/authorization/
title: Roles and permissions \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:09.161370+00:00
---

# Roles and permissions · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/authorization/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /Roles and permissions



# Roles and permissions

Last updated Sep 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/authorization/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRolesMembers, User Groups, and API tokens Members and User Groups Manage team access with User Groups API tokens Use granular permissions with WranglerBindingsCommon access patterns

You can control who can access your Developer Platform resources and what they can do with them by assigning [roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/) and [scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/) through [permission policies](https://developers.cloudflare.com/fundamentals/manage-members/policies/). Each policy combines a role, which defines the actions allowed, with a scope, which defines where those actions apply.

For Developer Platform products, scopes can be set at three levels:

Level | Scope | Use when  
---|---|---  
Platform | All products on an account | You want to grant access across Workers, R2, D1, KV, Durable Objects, Queues, Workers AI, Vectorize, Hyperdrive, and other Developer Platform resources.  
Product | All resources in one product | You want to grant access to all Workers, all R2 buckets, or all D1 databases, without granting access to other products.  
Resource | One resource inside a product | You want to grant access to a specific resource, such as an individual Worker or R2 bucket.  
  
## Roles

Assign one of these roles to define the level of permission you want to grant:

Role | What it allows  
---|---  
Metadata Read-Only | View resource lists, settings, metrics, logs, and traces. Cannot view product content such as code, data, or stored objects.  
Content Read-Only | Everything in Metadata Read-Only, plus read product content such as Worker code, D1 database rows, or R2 objects. Cannot make changes.  
Editor | Everything in Content Read-Only, plus update product content and settings. Cannot create or delete resources.  
Admin | Full control, including creating and deleting resources.  
  
## Members, User Groups, and API tokens

Developer Platform permissions can be granted in two ways:

Grant type | Best for | How it works  
---|---|---  
[Members](https://developers.cloudflare.com/fundamentals/manage-members/manage/) and [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) | People using the dashboard or API | Permissions are inherited when the member signs in to the dashboard or authenticates to the API.  
[API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) | CI/CD systems, automation, and service accounts | The token receives only the product and resource permissions selected when the token is created.  
  
### Members and User Groups

When you assign a [role](https://developers.cloudflare.com/fundamentals/manage-members/roles/) to a [member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or [User Group](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/), that permission applies whenever the user uses the Cloudflare dashboard or API.

For example, if you assign a member **Metadata Read-Only** at the platform level, they can view settings, metrics, logs, and traces for all Developer Platform products on the account — Workers, R2, D1, and everything else — but cannot view product content like code, data, or stored objects.

If you assign **Metadata Read-Only** at the Workers product level, they can view settings and observability data for all Workers on the account, but have no visibility into R2, D1, or other products.

If you assign **Metadata Read-Only** for a single Worker, they can only see settings and observability data for that one Worker. They will not see any other Workers or any other products.

### Manage team access with User Groups

If several people on the same team or project need the same access, create a [User Group](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) instead of assigning permissions to each member.

Assign the permission policy to the group, then add the relevant members. Each member automatically inherits the group's policy.

### API tokens

Use [API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) for CI/CD pipelines, agents, scripts, and other automated systems that need to access Developer Platform resources programmatically.

For example, create an API token with **Workers Editor** for a deployment pipeline that needs to update and deploy Worker code.

API tokens support product-level and, where available, resource-level permissions. They do not support platform-level permissions. To grant an API token broad Developer Platform access, select the product-level permissions for each product the token needs.

### Use granular permissions with Wrangler

Note

The [`wrangler login`](https://developers.cloudflare.com/workers/wrangler/commands/general/#login) OAuth flow does not currently support granular authorization.

To use granular permissions with [Wrangler](https://developers.cloudflare.com/workers/wrangler/), authenticate with an account-owned API token.

To authenticate Wrangler with an account-owned API token, create a token with only the permissions you need, then set these environment variables:
    
    
    export CLOUDFLARE_API_TOKEN="<YOUR_API_TOKEN>"
    export CLOUDFLARE_ACCOUNT_ID="<YOUR_ACCOUNT_ID>"

Wrangler uses the token's permissions. If the token is scoped to a specific Worker, Wrangler can only perform actions allowed for that Worker.

Wrangler commands can require different permissions depending on what they manage:

What you want to do | Example Wrangler command | Required access  
---|---|---  
Deploy an existing Worker | `wrangler deploy` | `Editor` scoped to that Worker, or `Editor` at the Workers product scope.  
Create a new Worker | `wrangler deploy` for a Worker that does not exist yet | `Admin` at the Workers product scope.  
Tail logs for one Worker | `wrangler tail` | `Metadata Read-Only` scoped to that Worker, or `Metadata Read-Only` at the Workers product scope.  
List KV namespaces | `wrangler kv namespace list` | Developer Platform `Metadata Read-Only` at a scope that includes KV.  
Create a KV namespace | `wrangler kv namespace create` | Developer Platform `Admin` at a scope that includes KV.  
Change Routes or Custom Domains during deployment | `wrangler deploy` | `Editor` for the Worker, plus [`Workers Routes Write`](https://developers.cloudflare.com/workers/authorization/workers/#routes-and-custom-domains) for every affected zone.  
  
## Bindings

To deploy a Worker that has [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) to resources like [Workers KV](https://developers.cloudflare.com/kv/), [R2](https://developers.cloudflare.com/r2/), or [D1](https://developers.cloudflare.com/d1/), you need **Editor** access to the Worker. You do not need separate permissions on the bound resources to deploy the Worker.

Permissions on bound resources are only required if you need to access those resources directly, for example, reading KV keys, querying a D1 database, or listing R2 objects.

## Common access patterns

Use case | Scope | Role  
---|---|---  
View settings, logs, and metrics across all products | Platform | Metadata Read-Only  
Read Worker code without modifying it | Workers product | Content Read-Only  
Deploy any existing Worker, no access to other products | Workers product | Editor  
Change Routes or Custom Domains during deployment | Workers product and each affected zone | Editor and [`Workers Routes Write`](https://developers.cloudflare.com/workers/authorization/workers/#routes-and-custom-domains)  
Rename an existing Worker | Individual Worker or Workers product | Editor  
Create or delete Workers | Workers product | Admin  
Automated deployments from CI/CD or agents | API token with Workers product | Editor  
Automated deployments to one specific Worker | API token with individual Worker | Editor  
  
[PreviousExamples](https://developers.cloudflare.com/workers/previews/examples/)[NextWorkers](https://developers.cloudflare.com/workers/authorization/workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/authorization/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
