---
url: https://developers.cloudflare.com/api/resources/secrets_store/
title: Secrets Store | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:19:10.536601+00:00
---

# Secrets Store | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/secrets_store/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Secrets Store

#### Secrets StoreStores

##### [List account stores](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/list)

GET/accounts/{account_id}/secrets_store/stores

##### [Get a store by ID](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/get)

GET/accounts/{account_id}/secrets_store/stores/{store_id}

##### [Create a store](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/create)

POST/accounts/{account_id}/secrets_store/stores

##### [Delete a store](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/methods/delete)

DELETE/accounts/{account_id}/secrets_store/stores/{store_id}

##### ModelsExpand Collapse 

StoreListResponse object { id, created, modified, 2 more } 

id: string

Store Identifier.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the store.

account_id: optional string

Account Identifier.

maxLength32

StoreGetResponse object { id, created, modified, 2 more } 

id: string

Store Identifier.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the store.

account_id: optional string

Account Identifier.

maxLength32

StoreCreateResponse object { id, created, modified, 2 more } 

id: string

Store Identifier.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the store.

account_id: optional string

Account Identifier.

maxLength32

StoreDeleteResponse = unknown

Result is null for delete operations.

#### Secrets StoreStoresSecrets

##### [List store secrets](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/list)

GET/accounts/{account_id}/secrets_store/stores/{store_id}/secrets

##### [Get a secret by ID](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/get)

GET/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

##### [Create a secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/create)

POST/accounts/{account_id}/secrets_store/stores/{store_id}/secrets

##### [Patch a secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/edit)

PATCH/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

##### [Delete a secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/delete)

DELETE/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}

##### [Delete secrets](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/bulk_delete)

DELETE/accounts/{account_id}/secrets_store/stores/{store_id}/secrets

##### [Duplicate Secret](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores/subresources/secrets/methods/duplicate)

POST/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate

##### ModelsExpand Collapse 

SecretListResponse object { id, created, modified, 5 more } 

id: string

Secret identifier tag.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the secret.

status: "pending" or "active" or "deleted"

One of the following:

"pending"

"active"

"deleted"

store_id: string

Store Identifier.

maxLength32

comment: optional string

Freeform text describing the secret.

scopes: optional array of "workers" or "ai_gateway" or "dex" or 3 more

The list of services that can use this secret.

One of the following:

"workers"

"ai_gateway"

"dex"

"access"

"containers"

"websearch"

SecretGetResponse object { id, created, modified, 5 more } 

id: string

Secret identifier tag.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the secret.

status: "pending" or "active" or "deleted"

One of the following:

"pending"

"active"

"deleted"

store_id: string

Store Identifier.

maxLength32

comment: optional string

Freeform text describing the secret.

scopes: optional array of "workers" or "ai_gateway" or "dex" or 3 more

The list of services that can use this secret.

One of the following:

"workers"

"ai_gateway"

"dex"

"access"

"containers"

"websearch"

SecretCreateResponse object { id, created, modified, 5 more } 

id: string

Secret identifier tag.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the secret.

status: "pending" or "active" or "deleted"

One of the following:

"pending"

"active"

"deleted"

store_id: string

Store Identifier.

maxLength32

comment: optional string

Freeform text describing the secret.

scopes: optional array of "workers" or "ai_gateway" or "dex" or 3 more

The list of services that can use this secret.

One of the following:

"workers"

"ai_gateway"

"dex"

"access"

"containers"

"websearch"

SecretEditResponse object { id, created, modified, 5 more } 

id: string

Secret identifier tag.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the secret.

status: "pending" or "active" or "deleted"

One of the following:

"pending"

"active"

"deleted"

store_id: string

Store Identifier.

maxLength32

comment: optional string

Freeform text describing the secret.

scopes: optional array of "workers" or "ai_gateway" or "dex" or 3 more

The list of services that can use this secret.

One of the following:

"workers"

"ai_gateway"

"dex"

"access"

"containers"

"websearch"

SecretDeleteResponse = unknown

Result is null for delete operations.

SecretBulkDeleteResponse = unknown

Result is null for delete operations.

SecretDuplicateResponse object { id, created, modified, 5 more } 

id: string

Secret identifier tag.

maxLength32

created: string

When the secret was created.

formatdate-time

modified: string

When the secret was modified.

formatdate-time

name: string

The name of the secret.

status: "pending" or "active" or "deleted"

One of the following:

"pending"

"active"

"deleted"

store_id: string

Store Identifier.

maxLength32

comment: optional string

Freeform text describing the secret.

scopes: optional array of "workers" or "ai_gateway" or "dex" or 3 more

The list of services that can use this secret.

One of the following:

"workers"

"ai_gateway"

"dex"

"access"

"containers"

"websearch"

#### Secrets StoreQuota

##### [View secret usage](https://developers.cloudflare.com/api/resources/secrets_store/subresources/quota/methods/get)

GET/accounts/{account_id}/secrets_store/quota

##### ModelsExpand Collapse 

QuotaGetResponse object { secrets } 

secrets: object { quota, usage } 

quota: number

The number of secrets the account is entitled to use.

usage: number

The number of secrets the account is currently using.

[ Previous

* * *

Maintenance Configs ](https://developers.cloudflare.com/api/resources/r2_data_catalog/subresources/namespaces/subresources/tables/subresources/maintenance_configs)[ Next

* * *

Stores ](https://developers.cloudflare.com/api/resources/secrets_store/subresources/stores)
