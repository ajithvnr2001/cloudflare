---
url: https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/
title: Grant teammates and agents access to specific Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:31.244655+00:00
---

# Grant teammates and agents access to specific Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 15, 2026

## Grant teammates and agents access to specific Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now grant access to specific Workers and choose from four roles to control the level of access you give teammates, agents, and CI/CD workflows.

Choose from four roles to control the level of access:

  * **Metadata Read-Only** : View settings, metrics, logs, and traces without access to Worker code or the ability to make changes.
  * **Content Read-Only** : Read Worker code, settings, and observability data without the ability to modify or deploy changes.
  * **Editor** : Update and deploy a Worker without the ability to delete it.
  * **Admin** : Everything in Editor, plus the ability to delete the Worker.

![Permission policy form showing four roles scoped to an individual Worker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1752,height=888,format=webp/_astro/individual-worker-permission-roles.Cn5i9cW0.png)

Worker-level access controls are available today for all customers. You can configure them in the Cloudflare dashboard, through the API, or with Terraform.

#### Roles designed for how teams build

Give **Metadata Read-Only** to a debugging agent so it can inspect settings and observability data without seeing Worker code. Give **Content Read-Only** to a code review agent so it can read code without changing it. Give **Editor** to a CI/CD workflow so it can deploy without deleting the Worker or accessing other Workers. **Admin** gives a teammate or agent full control over the Worker, including the ability to delete it.

Apply these roles across all Developer Platform products, across all Workers, or to an individual Worker.

#### Durable Objects

You can use granular permissions to control access to Durable Objects. Durable Objects do not have their own roles or scopes. Instead, they inherit the permissions assigned to the Worker that implements them.

Learn more about granular permissions in the [Durable Objects documentation](https://developers.cloudflare.com/workers/authorization/durable-objects/).

#### Grant access to members and User Groups

In the Cloudflare dashboard, go to **Manage Account** > **Members** and select a [member](https://developers.cloudflare.com/fundamentals/manage-members/manage/). Create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), set the scope to **Individual Workers** , select the Workers they need, and choose a role to grant the right level of access.

If several people on the same team or project need the same access, assign the permission policy to a [User Group](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/) instead of each member individually. Everyone added to the group automatically inherits the policy.

#### Create a scoped API token

For an agent or CI/CD workflow, go to **Manage Account** > **Account API Tokens** and create an [account-owned API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/). Set the scope to **Specified Workers** , select the Workers the token can access, and choose a role to grant the right level of access.

![Account API token policy with Metadata Read-Only access scoped to a specific Worker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1778,height=652,format=webp/_astro/scoped-worker-api-token-permissions.DR6OL7W0.png)

For more information, refer to the [Workers roles and permissions documentation](https://developers.cloudflare.com/workers/authorization/workers/).
