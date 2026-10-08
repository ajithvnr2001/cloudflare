---
url: https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/
title: Delete Workflow instances individually or in batches \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:14.633353+00:00
---

# Delete Workflow instances individually or in batches · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 17, 2026

## Delete Workflow instances individually or in batches

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-17-instance-delete/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now delete one or up to 100 Workflow instances and their stored state via the [Workflows API](https://developers.cloudflare.com/workflows/build/workers-api/) or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. [Storage billing](https://developers.cloudflare.com/workflows/reference/pricing/#storage-usage) is based on the average daily peak.

Delete one instance by calling [`delete()`](https://developers.cloudflare.com/workflows/build/workers-api/#delete) on its handle:
    
    
    const instance = await env.MY_WORKFLOW.get("instance-abc");
    await instance.delete();

If a Workflow deletes its own instance, execution stops during `await instance.delete()`. Code after the call does not run.

Delete multiple instances by calling [`deleteBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch) on the Workflow binding:
    
    
    const result = await env.MY_WORKFLOW.deleteBatch([
    	"instance-abc",
    	"instance-def",
    ]);
    
    console.log(result.deleted);
    console.log(result.errors);

The batch result contains `{ id }` entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.

Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use `latest` to delete the most recently created instance. Use `--local` against a local `wrangler dev` session:

instance-ids.jsonjson
    
    
    ["instance-abc", "instance-def"]
    
    
    npx wrangler workflows instances delete my-workflow <INSTANCE_ID>
    npx wrangler workflows instances delete my-workflow <INSTANCE_ID> <INSTANCE_ID>
    npx wrangler workflows instances delete my-workflow latest
    npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json
    npx wrangler workflows instances delete my-workflow <INSTANCE_ID> --local

For more information, refer to [Delete Workflow instances](https://developers.cloudflare.com/workflows/build/trigger-workflows/#delete-workflow-instances), [`delete`](https://developers.cloudflare.com/workflows/build/workers-api/#delete), and [`deleteBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#deletebatch).
