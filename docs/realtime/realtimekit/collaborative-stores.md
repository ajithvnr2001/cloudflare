---
url: https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/
title: Storage and Broadcast \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:56.166178+00:00
---

# Storage and Broadcast · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)
  4. /Collaborative Stores



# Storage and Broadcast

Last updated Aug 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Create a Store Update a Store Subscribe to a Store Fetch Store Data

The RealtimeKit Stores API allows you to create multiple key-value pair realtime stores. Users can subscribe to changes in a store and receive real-time updates. Data is stored until a [session](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#session) is active.

WebMobile

ReactWeb ComponentsAngular

### Create a Store

You can create a realtime store (changes are synced with other users):

Param | Type | Description | Required  
---|---|---|---  
`name` | string | Name of the store | true  
  
To create a store:
    
    
    const stores = useRealtimeKitSelector((m) => m.stores);
    const store = stores.create('myStore');
    
    
    const store = meeting.stores.create('myStore');
    
    
    const store = meeting.stores.create('myStore');
    
    
    val meeting = RealtimeKitMeetingBuilder.build(activity)
    val store = meeting.stores.create("myStore")
    
    
    let meeting = RealtimeKitiOSClientBuilder().build()
    let store = meeting.stores.create(name: "myStore")

Note

This method must be executed for every user.

### Update a Store

You can add, update or delete entries in a store:

Param | Type | Description | Required  
---|---|---|---  
`key` | string | Unique identifier used to store/update a value in the store | Yes  
`value` | StoreValue | Value that can be stored against a key | Yes  
      
    
    type StoreValue = string | number | object | array;
    
    
    const stores = useRealtimeKitSelector((m) => m.stores.stores);
    const store = stores.get("myStore");
    
    await store.set("user", { name: "John Doe" });
    
    await store.update("user", { age: 34 }); // { name: 'John Doe', age: 34 }
    
    await store.delete("user");
    
    
    type StoreValue = string | number | object | array;
    
    
    const { stores } = meeting.stores;
    const store = stores.get("myStore");
    
    await store.set("user", { name: "John Doe" });
    
    await store.update("user", { age: 34 }); // { name: 'John Doe', age: 34 }
    
    await store.delete("user");
    
    
    type StoreValue = string | number | object | array;
    
    
    const { stores } = meeting.stores;
    const store = stores.get("myStore");
    
    await store.set("user", { name: "John Doe" });
    
    await store.update("user", { age: 34 }); // { name: 'John Doe', age: 34 }
    
    await store.delete("user");
    
    
    val store = meeting.stores.get("myStore")
    
    store.set("user", mapOf("name" to "John Doe"))
    
    
    let store = meeting.stores.get(name: "myStore")
    store.set("user", ["name": "John Doe"])

Note

The `set` method overwrites the existing value, while the `update` method updates the existing value.

For example, if the stored value is `['a', 'b']` and you call `update` with `['c']`, the final value will be `['a', 'b', 'c']`.

### Subscribe to a Store

You can attach event listeners on a store's key, which fire when the value changes.
    
    
    const stores = useRealtimeKitSelector((m) => m.stores.stores);
    const store = stores.get('myStore');
    store.subscribe('key', (data) => {
        console.log(data);
    });
    
    // subscribe to all keys of a store
    store.subscribe('\*', (data) => {
    console.log(data);
    });
    
    store.unsubscribe('key');
    
    
    const { stores } = meeting.stores;
    const store = stores.get('myStore');
    store.subscribe('key', (data) => {
        console.log(data);
    });
    
    // subscribe to all keys of a store
    store.subscribe('\*', (data) => {
    console.log(data);
    });
    
    store.unsubscribe('key');
    
    
    const { stores } = meeting.stores;
    const store = stores.get('myStore');
    store.subscribe('key', (data) => {
        console.log(data);
    });
    
    // subscribe to all keys of a store
    store.subscribe('\*', (data) => {
    console.log(data);
    });
    
    store.unsubscribe('key');
    
    
    val store = meeting.stores.create("myStore")
    val keyChangeCallback = { key: String, value: Any? ->
      println(value)
    }
    store.subscribe("key", keyChangeCallback)
    
    // Subscribe to all keys
    store.subscribe(RtkStore.WILDCARD_KEY) { key, value ->
      println(value)
    }
    
    store.unsubscribe("key", keyChangeCallback)
    
    
    let store = meeting.stores.create(name: "myStore")
    let keyChangeCallback: ((String, (Any?)) -> Void) = { key, value in
        print(value ?? "null")
    }
    store.subscribe(key: "key", onChange: keyChangeCallback)
    
    // Subscribe to all keys
    store.subscribe(key: RtkStore.Companion().WILDCARD_KEY) { key, value in
        print(value ?? "null")
    }
    
    store.unsubscribe(key: "key", onChange: keyChangeCallback)

### Fetch Store Data

You can fetch the data stored in the store:
    
    
    const stores = useRealtimeKitSelector((m) => m.stores.stores);
    const store = stores.get('myStore');
    
    // fetch value for a specific key
    const data = store.get('key');
    
    // fetch all the data in the store
    const data = store.getAll();
    
    
    const { stores } = meeting.stores;
    const store = stores.get('myStore');
    
    // fetch value for a specific key
    const data = store.get('key');
    
    // fetch all the data in the store
    const data = store.getAll();
    
    
    const { stores } = meeting.stores;
    const store = stores.get('myStore');
    
    // fetch value for a specific key
    const data = store.get('key');
    
    // fetch all the data in the store
    const data = store.getAll();
    
    
    val store = meeting.stores.create("myStore")
    
    // fetch value for a specific key
    val data = store.get("key")
    
    // fetch all the data in the store
    val data = store.getAll()
    
    
    let store = meeting.stores.create(name: "myStore")
    
    // fetch value for a specific key
    store.get(key: "key")
    
    // fetch all the data in the store
    store.getAll()

[PreviousRTKThemePreset](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkthemepreset/)[NextMessage Broadcast APIs](https://developers.cloudflare.com/realtime/realtimekit/broadcast-apis/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/collaborative-stores/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
