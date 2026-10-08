---
url: https://developers.cloudflare.com/kv/api/delete-key-value-pairs/
title: Delete key-value pairs \u00b7 Cloudflare Workers KV docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:39.611755+00:00
---

# Delete key-value pairs · Cloudflare Workers KV docs

> Source: https://developers.cloudflare.com/kv/api/delete-key-value-pairs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[KV](https://developers.cloudflare.com/kv/)
  3. /Workers Binding API
  4. /Delete key-value pairs



# Delete key-value pairs

Last updated Jun 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/kv/api/delete-key-value-pairs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReference delete() methodGuidance Delete data in bulkOther methods to access KV

To delete a key-value pair, call the `delete()` method of the [KV binding](https://developers.cloudflare.com/kv/concepts/kv-bindings/) on any [KV namespace](https://developers.cloudflare.com/kv/concepts/kv-namespaces/) you have bound to your Worker code:
    
    
    env.NAMESPACE.delete(key);
    
    
    self.env.NAMESPACE.delete(key)

#### Example

An example of deleting a key-value pair from within a Worker:
    
    
    export default {
      async fetch(request, env, ctx) {
        try {
          await env.NAMESPACE.delete("first-key");
    
          return new Response("Successful delete", {
            status: 200
          });
        }
        catch (e)
        {
          return new Response(e.message, {status: 500});
        }
      },
    };
    
    
    from workers import WorkerEntrypoint, Response
    
    class Default(WorkerEntrypoint):
        async def fetch(self, request):
            try:
                await self.env.NAMESPACE.delete("first-key")
    
                return Response("Successful delete", status=200)
            except Exception as e:
                return Response(str(e), status=500)

## Reference

The following method is provided to delete from KV:

  * delete()



### `delete()` method

To delete a key-value pair, call the `delete()` method of the [KV binding](https://developers.cloudflare.com/kv/concepts/kv-bindings/) on any KV namespace you have bound to your Worker code:
    
    
    env.NAMESPACE.delete(key);
    
    
    await self.env.NAMESPACE.delete(key)

#### Parameters

  * `key`: `string`
    * The key to associate with the value.



#### Response

  * `response`: `Promise<void>`
    * A `Promise` that resolves if the delete is successful.



This method returns a promise that you should `await` on to verify successful deletion. Calling `delete()` on a non-existing key is returned as a successful delete.

Calling the `delete()` method will remove the key and value from your KV namespace. As with any operations, it may take some time for the key to be deleted from various points in the Cloudflare global network.

## Guidance

### Delete data in bulk

Delete more than one key-value pair at a time with Wrangler or [via the REST API](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_delete/).

The bulk REST API can accept up to 10,000 KV pairs at once. Bulk writes are not supported using the [KV binding](https://developers.cloudflare.com/kv/concepts/kv-bindings/).

## Other methods to access KV

You can also [delete key-value pairs from the command line with Wrangler](https://developers.cloudflare.com/kv/reference/kv-commands/#kv-namespace-delete) or [with the REST API](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/delete/).

[PreviousWrite key-value pairs](https://developers.cloudflare.com/kv/api/write-key-value-pairs/)[NextList keys](https://developers.cloudflare.com/kv/api/list-keys/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/kv/api/delete-key-value-pairs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
