---
url: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstore/
title: RTKStore \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:57.167829+00:00
---

# RTKStore · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstore/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/core/)

  4. /API Reference
  5. /RTKStore



# RTKStore

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstore/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview store.set(key, value, [sync], [emit]) ⇒ Promise.<void> store.bulkSet(data) ⇒ Promise.<void> store.update(key, value, [sync]) ⇒ Promise.<void> store.delete(key, [sync], [emit]) ⇒ Promise.<void> store.bulkDelete(data) ⇒ Promise.<void> store.get(key) ⇒ any store.getAll() ⇒ RTKStoreData store.clear() store.updateRateLimits(num, period) store.updateBulkRateLimits(num, period) store.subscribe(key, cb) ⇒ void store.unsubscribe(key, [cb]) ⇒ void store.populate(data)

This module represents a single global store. The store can be accessed from the `meeting.stores` module.

**Returns** : An instance of RTKStore.  
**Example**
    
    
    const handRaiseStore = meeting.stores.stores.get('handRaise');

  * RTKStore ⇒ 
    * .set(key, value, [sync], [emit]) ⇒ `Promise.<void>`
    * .bulkSet(data) ⇒ `Promise.<void>`
    * .update(key, value, [sync]) ⇒ `Promise.<void>`
    * .delete(key, [sync], [emit]) ⇒ `Promise.<void>`
    * .bulkDelete(data) ⇒ `Promise.<void>`
    * .get(key) ⇒ `any`
    * .getAll() ⇒ `RTKStoreData`
    * .clear()
    * .updateRateLimits(num, period)
    * .updateBulkRateLimits(num, period)
    * .subscribe(key, cb) ⇒ `void`
    * .unsubscribe(key, [cb]) ⇒ `void`
    * .populate(data)



### store.set(key, value, [sync], [emit]) ⇒ `Promise.<void>`

Sets a value in the store.

**Kind** : instance method of `RTKStore`  
**Returns** : `Promise.<void>` \- A promise.

Param | Type | Default | Description  
---|---|---|---  
key | `string` |  | Unique identifier used to store value.  
value | `any` |  | Data to be set.  
[sync] | `boolean` | `true` | Whether to sync change to remote store.  
[emit] | `boolean` | `false` | Whether to emit to local subscribers.  
  
### store.bulkSet(data) ⇒ `Promise.<void>`

Sets multiple values in the store.

**Kind** : instance method of `RTKStore`  
**Returns** : `Promise.<void>` \- A promise.

Param | Type  
---|---  
data | `Array.<{key: string, payload: any}>`  
  
### store.update(key, value, [sync]) ⇒ `Promise.<void>`

Updates an already existing value in the store. If the value stored is `['a', 'b']`, the operation `store.update(key, ['c'])` will modify the value to `['a','b','c']`.

**Kind** : instance method of `RTKStore`  
**Returns** : `Promise.<void>` \- A promise.

Param | Type | Default | Description  
---|---|---|---  
key | `string` |  | Unique identifier used to store value.  
value | `any` |  | Data to be updated.  
[sync] | `boolean` | `true` | Whether to sync change to remote store.  
  
### store.delete(key, [sync], [emit]) ⇒ `Promise.<void>`

Deletes a key value pair form the store.

**Kind** : instance method of `RTKStore`  
**Returns** : `Promise.<void>` \- A promise.

Param | Type | Default | Description  
---|---|---|---  
key | `string` |  | Unique identifier used to store value.  
[sync] | `boolean` | `true` | Whether to sync change to remote store.  
[emit] | `boolean` | `false` | Whether to emit to local subscribers.  
  
### store.bulkDelete(data) ⇒ `Promise.<void>`

Deletes multiple values from the store.

**Kind** : instance method of `RTKStore`  
**Returns** : `Promise.<void>` \- A promise.

Param | Type  
---|---  
data | `Array.<{key: string}>`  
  
### store.get(key) ⇒ `any`

Returns value for the given key.

**Kind** : instance method of `RTKStore`  
**Returns** : `any` \- Value for the given key.

Param | Type | Description  
---|---|---  
key | `string` | Unique identifier used to store value.  
  
### store.getAll() ⇒ `RTKStoreData`

Returns the entire store.

**Kind** : instance method of `RTKStore`  
**Returns** : `RTKStoreData` \- An instance of RTKStoreData.  


### store.clear()

Clears all data in the store.

**Kind** : instance method of `RTKStore`  


### store.updateRateLimits(num, period)

**Kind** : instance method of `RTKStore`

Param | Type  
---|---  
num | `number`  
period | `number`  
  
### store.updateBulkRateLimits(num, period)

**Kind** : instance method of `RTKStore`

Param | Type  
---|---  
num | `number`  
period | `number`  
  
### store.subscribe(key, cb) ⇒ `void`

Listens for data change on a store key.

**Kind** : instance method of `RTKStore`  
**Returns** : `void` \- void

Param | Type | Description  
---|---|---  
key | `string` | Unique identifier used to store value.  
cb | `function` | The callback function that gets executed when data is modified.  
  
### store.unsubscribe(key, [cb]) ⇒ `void`

Removes all listeners for a key on the store.

**Kind** : instance method of `RTKStore`  
**Returns** : `void` \- void

Param | Type | Description  
---|---|---  
key | `string` | Unique identifier used to store value.  
[cb] | `function` | Callback to be removed.  
  
### store.populate(data)

**Kind** : instance method of `RTKStore`

Param | Type  
---|---  
data | `RTKStoreData`  
  
[PreviousRTKStage](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/)[NextRTKThemePreset](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkthemepreset/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/core/api-reference/RTKStore.md)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
