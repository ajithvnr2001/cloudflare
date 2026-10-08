---
url: https://developers.cloudflare.com/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/
title: Automate Worker deployments with a simplified SDK and more reliable Terraform provider \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:14.487199+00:00
---

# Automate Worker deployments with a simplified SDK and more reliable Terraform provider · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 19, 2025

## Automate Worker deployments with a simplified SDK and more reliable Terraform provider

[D1](https://developers.cloudflare.com/d1/)[Workers](https://developers.cloudflare.com/workers/)[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

#### Simplified Worker Deployments with our SDKs

We've simplified the programmatic deployment of Workers via our [Cloudflare SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/). This update abstracts away the low-level complexities of the `multipart/form-data` upload process, allowing you to focus on your code while we handle the deployment mechanics.

This new interface is available in:

  * [cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript) (4.4.1)
  * [cloudflare-python ↗︎](https://github.com/cloudflare/cloudflare-python) (4.3.1)



For complete examples, see our guide on [programmatic Worker deployments](https://developers.cloudflare.com/workers/platform/infrastructure-as-code).

#### The Old way: Manual API calls

Previously, deploying a Worker programmatically required manually constructing a `multipart/form-data` HTTP request, packaging your code and a separate `metadata.json` file. This was more complicated and verbose, and prone to formatting errors.

For example, here's how you would upload a Worker script previously with cURL:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/<account_id>/workers/scripts/my-hello-world-script \
      -X PUT \
      -H 'Authorization: Bearer <api_token>' \
      -F 'metadata={
            "main_module": "my-hello-world-script.mjs",
            "bindings": [
              {
                "type": "plain_text",
                "name": "MESSAGE",
                "text": "Hello World!"
              }
            ],
            "compatibility_date": "$today"
          };type=application/json' \
      -F 'my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module' <<EOF
    export default {
      async fetch(request, env, ctx) {
        return new Response(env.MESSAGE, { status: 200 });
      }
    };
    EOF

#### After: SDK interface

With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.

This approach allows you to specify metadata like `main_module`, `bindings`, and `compatibility_date` as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.

Here's how you can now programmatically deploy a Worker via the [`cloudflare-typescript` SDK ↗︎](https://github.com/cloudflare/cloudflare-typescript)
    
    
    import Cloudflare from "cloudflare";
    import { toFile } from "cloudflare/index";
    
    // ... client setup, script content, etc.
    
    const script = await client.workers.scripts.update(scriptName, {
    	account_id: accountID,
    	metadata: {
    		main_module: scriptFileName,
    		bindings: [],
    	},
    	files: {
    		[scriptFileName]: await toFile(Buffer.from(scriptContent), scriptFileName, {
    			type: "application/javascript+module",
    		}),
    	},
    });
    
    
    import Cloudflare from 'cloudflare';
    import { toFile } from 'cloudflare/index';
    
    // ... client setup, script content, etc.
    
    const script = await client.workers.scripts.update(scriptName, {
      account_id: accountID,
      metadata: {
        main_module: scriptFileName,
        bindings: [],
      },
      files: {
        [scriptFileName]: await toFile(Buffer.from(scriptContent), scriptFileName, {
          type: 'application/javascript+module',
        }),
      },
    });

View the complete example here: <https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts>[ ↗︎](https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts)

#### Terraform provider improvements

We've also made several fixes and enhancements to the [Cloudflare Terraform provider ↗︎](https://github.com/cloudflare/terraform-provider-cloudflare):

  * Fixed the [`cloudflare_workers_script` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) resource in Terraform, which previously was producing a diff even when there were no changes. Now, your `terraform plan` outputs will be cleaner and more reliable.
  * Fixed the [`cloudflare_workers_for_platforms_dispatch_namespace` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace), where the provider would attempt to recreate the namespace on a `terraform apply`. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.
  * The [`cloudflare_workers_route` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route) resource now allows for the `script` property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes [docs](https://developers.cloudflare.com/workers/configuration/routing/routes)). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.
  * Using `primary_location_hint` in the [`cloudflare_d1_database` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database) resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.



#### API improvements

We've also properly documented the [Workers Script And Version Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/script_and_version_settings) in our public OpenAPI spec and SDKs.
