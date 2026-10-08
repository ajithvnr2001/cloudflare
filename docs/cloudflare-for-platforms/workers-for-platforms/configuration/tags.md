---
url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/
title: Tags \u00b7 Cloudflare for Platforms docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:05.443400+00:00
---

# Tags · Cloudflare for Platforms docs

> Source: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/)
  3. /…

[Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

  4. /Configuration
  5. /Tags



# Tags

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd tags via dashboardTags API reference Get script tags Set script tags Add a single tag Delete a single tag Filter Workers by tag Delete Workers by tag

Use tags to organize, search, and filter user Workers at scale. Tag Workers based on customer ID, plan type, project ID, or environment. After you tag user Workers, you can perform bulk operations like deleting all Workers for a specific customer.

Note

You can set a maximum of eight tags per script. Avoid special characters like `,` and `&` when naming your tag.

## Add tags via dashboard

  1. Go to **Workers for Platforms** in the Cloudflare dashboard and select your namespace.
  2. Select a user Worker from the list.
  3. Go to **Settings** > **Tags**.
  4. Add your tags (for example, `customer-123`, `pro-plan`, `production`).
  5. Select **Save**.



You can also search and filter Workers by tags in the namespace view.

## Tags API reference

For complete API documentation, refer to [Workers for Platforms API](https://developers.cloudflare.com/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/).

### Get script tags

Fetch all tags for a Worker script.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Workers Tail Read`
  * `Workers Scripts Write`
  * `Workers Scripts Read`

List Workers for Platforms Script Tagsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$DISPATCH_NAMESPACE/scripts/$SCRIPT_NAME/tags" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

### Set script tags

Replace all tags on a Worker script. Existing tags not in the request are removed.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Workers Scripts Write`

Replace Workers for Platforms Script Tagsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$DISPATCH_NAMESPACE/scripts/$SCRIPT_NAME/tags" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

### Add a single tag

Add one tag to a Worker script without affecting existing tags.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Workers Scripts Write`

Create Workers for Platforms Script Tagbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$DISPATCH_NAMESPACE/scripts/$SCRIPT_NAME/tags/$TAG" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

### Delete a single tag

Remove one tag from a Worker script.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Workers Scripts Write`

Delete Workers for Platforms Script Tagbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$DISPATCH_NAMESPACE/scripts/$SCRIPT_NAME/tags/$TAG" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

### Filter Workers by tag

List all Workers that match a tag filter. Use `tag:yes` to include or `tag:no` to exclude.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Workers Tail Read`
  * `Workers Scripts Write`
  * `Workers Scripts Read`

List Workers for Platforms Scriptsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$DISPATCH_NAMESPACE/scripts?tags=production%3Ayes" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

### Delete Workers by tag

Delete all Workers matching a tag filter. Use this to bulk delete Workers when a customer leaves your platform.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Workers Scripts Write`

Delete Workers for Platforms Scriptsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$DISPATCH_NAMESPACE/scripts?tags=customer-123%3Ayes" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

[PreviousStatic assets](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/)[NextWorker Isolation](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-for-platforms/workers-for-platforms/configuration/tags.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
