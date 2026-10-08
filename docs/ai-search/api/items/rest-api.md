---
url: https://developers.cloudflare.com/ai-search/api/items/rest-api/
title: REST API \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:37.323830+00:00
---

# REST API · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/api/items/rest-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

API

  4. /Items
  5. /REST API



# REST API

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/api/items/rest-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthenticationAPI pathsItems Example: Upload a document Example: List items

Use the AI Search REST API to upload, list, and manage individual documents within an instance.

Note

The Items API uploads files to an instance's built-in storage. For more details, refer to [Built-in storage](https://developers.cloudflare.com/ai-search/configuration/data-source/built-in-storage/).

## Authentication

All requests require an API token with **AI Search:Edit** and **AI Search:Run** permissions.

  1. In the Cloudflare dashboard, go to **My Profile** > **API Tokens**.

[ Go to **API Tokens** ↗ ](https://dash.cloudflare.com/profile/api-tokens)
  2. Select **Create Token**.

  3. Select **Create Custom Token**.

  4. Enter a **Token name** , for example `AI Search Manager`.

  5. Under **Permissions** , add two permissions:

     * **Account** > **AI Search:Edit**
     * **Account** > **AI Search:Run**
  6. Select **Continue to summary** , then select **Create Token**.

  7. Copy and save the token value. This is your `API_TOKEN`.




Include the token in the `Authorization` header for all requests:
    
    
    Authorization: Bearer <API_TOKEN>

## API paths

Item APIs are scoped to a [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/):

Path | Description  
---|---  
`/accounts/{account_id}/ai-search/namespaces/{namespace}/instances/{id}/` | Operates on instances within a namespace  
  
Every account has a `default` namespace. Use `default` unless you created a custom namespace. For the full specification, refer to the [Namespace API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/).

## Items

Upload, list, get, delete, and download items within an instance. For the full specification, refer to the [Items API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/).

Operation | Method | Description  
---|---|---  
[Upload](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/) | `POST` | Upload a document for indexing  
[List](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list/) | `GET` | List all items in an instance  
[Get](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get/) | `GET` | Get item info by ID  
[Delete](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/delete/) | `DELETE` | Delete an item  
[Download](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/download/) | `GET` | Download the original file  
  
### Example: Upload a document

Upload a file to an instance:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/<INSTANCE_NAME>/items" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -F "file=@/path/to/your/file.pdf"

### Example: List items

List all items in an instance:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/<INSTANCE_NAME>/items" \
      -H "Authorization: Bearer <API_TOKEN>"

To find a single item by its exact object key, pass the `key` query parameter:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/<INSTANCE_NAME>/items?key=docs/readme.md" \
      -H "Authorization: Bearer <API_TOKEN>"

Keys are unique per data source, so combine `key` with `source` (for example, `source=builtin`) to disambiguate when the same key exists across multiple sources.

[PreviousWorkers binding](https://developers.cloudflare.com/ai-search/api/items/workers-binding/)[NextWorkers binding migration](https://developers.cloudflare.com/ai-search/api/migration/workers-binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/api/items/rest-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
