---
url: https://developers.cloudflare.com/api/resources/kv/
title: KV | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:44.812899+00:00
---

# KV | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/kv/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# KV

#### KVNamespaces

##### [List namespaces](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/list)

GET/accounts/{account_id}/storage/kv/namespaces

##### [Get a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/get)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}

##### [Create a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/create)

POST/accounts/{account_id}/storage/kv/namespaces

##### [Rename a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/update)

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}

##### [Delete a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/delete)

DELETE/accounts/{account_id}/storage/kv/namespaces/{namespace_id}

##### [Write multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/bulk_update)

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk

##### [Delete multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/bulk_delete)

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete

##### [Get multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/methods/bulk_get)

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get

##### ModelsExpand Collapse 

Namespace object { id, title, jurisdiction, 2 more } 

id: string

ID of the Workers KV namespace.

maxLength32

title: string

Human-readable string name for a Workers KV namespace.

maxLength512

jurisdiction: optional "eu" or "fedramp" or "us"

Specify the jurisdiction to restrict the KV namespace to durably store data within. Can only be set at namespace creation time.

One of the following:

"eu"

"fedramp"

"us"

mode: optional "instant"

The mode of the Workers KV namespace. Specify `instant` when creating a namespace to create a KV Instant namespace. Omit this field when creating a namespace to create a classic namespace. Currently, `instant` is the only supported explicit value.

supports_url_encoding: optional boolean

True if keys written on the URL will be URL-decoded before storing. For example, if set to “true”, a key written on the URL as “%3F” will be stored as ”?”.

NamespaceDeleteResponse object { } 

NamespaceBulkUpdateResponse object { successful_key_count, unsuccessful_keys } 

successful_key_count: optional number

Number of keys successfully written or deleted by the bulk operation.

unsuccessful_keys: optional array of string

Names of keys that failed to be written or deleted. Retry the operation for these keys.

NamespaceBulkDeleteResponse object { successful_key_count, unsuccessful_keys } 

successful_key_count: optional number

Number of keys successfully written or deleted by the bulk operation.

unsuccessful_keys: optional array of string

Names of keys that failed to be written or deleted. Retry the operation for these keys.

NamespaceBulkGetResponse = object { values }  or object { values } 

One of the following:

WorkersKVBulkGetResult object { values } 

values: optional map[string or number or boolean or map[unknown]]

Requested keys are paired with their values in an object.

One of the following:

string

number

boolean

map[unknown]

WorkersKVBulkGetResultWithMetadata object { values } 

values: optional map[object { metadata, value, expiration } ]

Requested keys are paired with their values and metadata in an object.

metadata: unknown

The metadata associated with the key.

value: unknown

The value associated with the key.

expiration: optional number

Expires the key at a certain time, measured in number of seconds since the UNIX epoch.

#### KVNamespacesKeys

##### [List keys in a namespace](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/list)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys

##### [Write multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update)

Deprecated

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk

##### [Delete multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_delete)

Deprecated

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete

##### [Get multiple key-value pairs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_get)

Deprecated

POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get

##### ModelsExpand Collapse 

Key object { name, expiration, metadata } 

A name for a value. A value stored under a given key may be retrieved via the same key.

name: string

A key’s name. The name may be at most 512 bytes. All printable, non-whitespace characters are valid. Use percent-encoding to define key names as part of a URL.

maxLength512

expiration: optional number

The time, measured in number of seconds since the UNIX epoch, at which the key will expire. This property is omitted for keys that will not expire.

metadata: optional unknown

Arbitrary JSON that is associated with a key.

KeyBulkUpdateResponse object { successful_key_count, unsuccessful_keys } 

successful_key_count: optional number

Number of keys successfully written or deleted by the bulk operation.

unsuccessful_keys: optional array of string

Names of keys that failed to be written or deleted. Retry the operation for these keys.

KeyBulkDeleteResponse object { successful_key_count, unsuccessful_keys } 

successful_key_count: optional number

Number of keys successfully written or deleted by the bulk operation.

unsuccessful_keys: optional array of string

Names of keys that failed to be written or deleted. Retry the operation for these keys.

KeyBulkGetResponse = object { values }  or object { values } 

One of the following:

WorkersKVBulkGetResult object { values } 

values: optional map[string or number or boolean or map[unknown]]

Requested keys are paired with their values in an object.

One of the following:

string

number

boolean

map[unknown]

WorkersKVBulkGetResultWithMetadata object { values } 

values: optional map[object { metadata, value, expiration } ]

Requested keys are paired with their values and metadata in an object.

metadata: unknown

The metadata associated with the key.

value: unknown

The value associated with the key.

expiration: optional number

Expires the key at a certain time, measured in number of seconds since the UNIX epoch.

#### KVNamespacesMetadata

##### [Get a key's metadata](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/metadata/methods/get)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}

##### ModelsExpand Collapse 

MetadataGetResponse = unknown

Arbitrary JSON that is associated with a key.

#### KVNamespacesValues

##### [Get a key's value](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get)

GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}

##### [Write a key-value pair with optional metadata](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/update)

PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}

##### [Delete a key-value pair](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/delete)

DELETE/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}

##### ModelsExpand Collapse 

ValueUpdateResponse object { } 

ValueDeleteResponse object { } 

[ Previous

* * *

Subscriptions ](https://developers.cloudflare.com/api/resources/k2/subresources/streams/subresources/subscriptions)[ Next

* * *

Namespaces ](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces)
