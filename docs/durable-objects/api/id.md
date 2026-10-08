---
url: https://developers.cloudflare.com/durable-objects/api/id/
title: Durable Object ID \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:05.629772+00:00
---

# Durable Object ID · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/api/id/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Workers Binding API
  4. /Durable Object ID



# Durable Object ID

Last updated May 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/api/id/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDescriptionMethods toString equalsProperties name jurisdictionRelated resources

## Description

A Durable Object ID is a 64-digit hexadecimal number used to identify a Durable Object. Not all 64-digit hex numbers are valid IDs. Durable Object IDs are constructed indirectly via the [`DurableObjectNamespace`](https://developers.cloudflare.com/durable-objects/api/namespace) interface.

The `DurableObjectId` interface refers to a new or existing Durable Object. This interface is most frequently used by [`DurableObjectNamespace::get`](https://developers.cloudflare.com/durable-objects/api/namespace/#get) to obtain a [`DurableObjectStub`](https://developers.cloudflare.com/durable-objects/api/stub) for submitting requests to a Durable Object. Note that creating an ID for a Durable Object does not create the Durable Object. The Durable Object is created lazily after creating a stub from a `DurableObjectId`. This ensures that objects are not constructed until they are actually accessed.

Logging

If you are experiencing an issue with a particular Durable Object, you may wish to log the `DurableObjectId` from your Worker and include it in your Cloudflare support request.

## Methods

### `toString`

`toString` converts a `DurableObjectId` to a 64 digit hex string. This string is useful for logging purposes or storing the `DurableObjectId` elsewhere, for example, in a session cookie. This string can be used to reconstruct a `DurableObjectId` via `DurableObjectNamespace::idFromString`.
    
    
    // Create a new unique ID
    const id = env.MY_DURABLE_OBJECT.newUniqueId();
    // Convert the ID to a string to be saved elsewhere, e.g. a session cookie
    const session_id = id.toString();
    
    ...
    // Recreate the ID from the string
    const id = env.MY_DURABLE_OBJECT.idFromString(session_id);

#### Parameters

  * None.



#### Return values

  * A 64 digit hex string.



### `equals`

`equals` is used to compare equality between two instances of `DurableObjectId`.
    
    
    const id1 = env.MY_DURABLE_OBJECT.newUniqueId();
    const id2 = env.MY_DURABLE_OBJECT.newUniqueId();
    console.assert(!id1.equals(id2), "Different unique ids should never be equal.");
    
    
    id1 = env.MY_DURABLE_OBJECT.newUniqueId()
    id2 = env.MY_DURABLE_OBJECT.newUniqueId()
    assert not id1.equals(id2), "Different unique ids should never be equal."

#### Parameters

  * A required `DurableObjectId` to compare against.



#### Return values

  * A boolean. True if equal and false otherwise.



## Properties

### `name`

`name` is an optional property of a `DurableObjectId`, which returns the name that was used to create the `DurableObjectId` via [`DurableObjectNamespace::idFromName`](https://developers.cloudflare.com/durable-objects/api/namespace/#idfromname). This value is undefined if the `DurableObjectId` was constructed using [`DurableObjectNamespace::newUniqueId`](https://developers.cloudflare.com/durable-objects/api/namespace/#newuniqueid).

The `name` property is also available on `ctx.id` inside the Durable Object when the caller uses `idFromName()` or `getByName()`. `ctx.id.name` will be `undefined` in the following cases:

  * The caller accesses the Durable Object using `idFromString()`, even if the ID was originally created with `idFromName()`.
  * Names longer than 1,024 bytes are not passed through to `ctx.id`.
  * The Durable Object was created with `newUniqueId()`.



Alarms

`ctx.id.name` is especially useful inside [alarm handlers](https://developers.cloudflare.com/durable-objects/api/alarms/), where there is no calling client to pass the name as an argument. When the alarm fires, `ctx.id.name` holds the same name the object was originally accessed with.

Alarms created before 2026-03-15 do not have `name` stored. When such an alarm fires, `ctx.id.name` will be `undefined`, and any new alarm scheduled from that handler will also lack a `name`. To fix this, reschedule the alarm from a `fetch()` or RPC handler where `name` is available.
    
    
    const uniqueId = env.MY_DURABLE_OBJECT.newUniqueId();
    const fromNameId = env.MY_DURABLE_OBJECT.idFromName("foo");
    console.assert(uniqueId.name === undefined, "unique ids have no name");
    console.assert(
    	fromNameId.name === "foo",
    	"name matches parameter to idFromName",
    );
    
    
    const uniqueId: DurableObjectId = env.MY_DURABLE_OBJECT.newUniqueId();
    const fromNameId: DurableObjectId = env.MY_DURABLE_OBJECT.idFromName("foo");
    console.assert(uniqueId.name === undefined, "unique ids have no name");
    console.assert(
    	fromNameId.name === "foo",
    	"name matches parameter to idFromName",
    );
    
    
    unique_id = env.MY_DURABLE_OBJECT.newUniqueId()
    from_name_id = env.MY_DURABLE_OBJECT.idFromName("foo")
    assert unique_id.name is None, "unique ids have no name"
    assert from_name_id.name == "foo", "name matches parameter to idFromName"

The same `name` is available inside the Durable Object via `ctx.id.name`:
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class ChatRoom extends DurableObject {
    	async getRoomName() {
    		return this.ctx.id.name; // "foo" when accessed via getByName("foo")
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class ChatRoom extends DurableObject<Env> {
    	async getRoomName(): Promise<string | undefined> {
    		return this.ctx.id.name; // "foo" when accessed via getByName("foo")
    	}
    }
    
    
    from workers import DurableObject
    
    class ChatRoom(DurableObject):
        async def get_room_name(self):
            return self.ctx.id.name  # "foo" when accessed via get_by_name("foo")

### `jurisdiction`

`jurisdiction` is an optional property of a `DurableObjectId`, which returns the [jurisdiction](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction) the ID is restricted to, such as `"eu"` or `"fedramp"`. The same value is available inside the Durable Object via `ctx.id.jurisdiction`, including in [alarm handlers](https://developers.cloudflare.com/durable-objects/api/alarms/) and objects accessed via `idFromString()`, so you can make region-aware decisions without passing the jurisdiction as an argument or persisting it in storage.

`jurisdiction` is preserved across every ID-construction path, including:

  * IDs created from a jurisdiction-restricted subnamespace, for example `env.MY_DURABLE_OBJECT.jurisdiction("eu").idFromName("foo")` or `.newUniqueId()`.
  * IDs created via `env.MY_DURABLE_OBJECT.newUniqueId({ jurisdiction: "eu" })`.
  * IDs restored from a string via `idFromString()` — the jurisdiction is encoded in the string itself, so it works on any namespace binding.



`ctx.id.jurisdiction` is `undefined` in two cases:

  * The Durable Object was not created in a jurisdiction-restricted namespace.
  * The Durable Object's alarm was scheduled before 2026-03-15. To backfill the value, reschedule the alarm from a `fetch()` or RPC handler.


    
    
    const plainId = env.MY_DURABLE_OBJECT.idFromName("foo");
    const euId = env.MY_DURABLE_OBJECT.jurisdiction("eu").idFromName("foo");
    console.assert(plainId.jurisdiction === undefined, "no jurisdiction set");
    console.assert(euId.jurisdiction === "eu", "jurisdiction matches namespace");
    
    
    plain_id = env.MY_DURABLE_OBJECT.idFromName("foo")
    eu_id = env.MY_DURABLE_OBJECT.jurisdiction("eu").idFromName("foo")
    assert plain_id.jurisdiction is None, "no jurisdiction set"
    assert eu_id.jurisdiction == "eu", "jurisdiction matches namespace"

## Related resources

  * [Durable Objects: Easy, Fast, Correct – Choose Three ↗︎](https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/).



[PreviousDurable Object Namespace](https://developers.cloudflare.com/durable-objects/api/namespace/)[NextDurable Object Stub](https://developers.cloudflare.com/durable-objects/api/stub/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/api/id.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
