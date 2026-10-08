---
url: https://developers.cloudflare.com/ai-search/api/instances/rest-api/
title: REST API \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:36.854862+00:00
---

# REST API · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/api/instances/rest-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

API

  4. /Instances
  5. /REST API



# REST API

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/api/instances/rest-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthenticationAPI pathsInstances Example: Create an instanceJobs Example: Trigger a sync job

Use the AI Search REST API to manage instances and sync jobs over HTTP.

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

AI Search scopes Instance APIs to a [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/):

Path | Description  
---|---  
`/accounts/{account_id}/ai-search/namespaces/{namespace}/instances/{id}` | Operates on instances within a namespace  
  
Every account has a `default` namespace. Use `default` unless you created a custom namespace. For the full specification, refer to the [Namespace API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/).

## Instances

Create, list, get, update, and delete AI Search instances. For the full specification, refer to the [Instances API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/).

Operation | Method | Description  
---|---|---  
[Create](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/) | `POST` | Create a new instance  
[List](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/list/) | `GET` | List all instances  
[Get](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/read/) | `GET` | Get an instance by ID  
[Update](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/update/) | `PUT` | Update instance configuration  
[Delete](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/delete/) | `DELETE` | Delete an instance  
[Stats](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/stats/) | `GET` | Get indexing statistics  
  
### Example: Create an instance

Create an instance in the default namespace:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "id": "my-instance"
      }'

## Jobs

Trigger and monitor [sync jobs](https://developers.cloudflare.com/ai-search/configuration/indexing/syncing/) that scan your data source and index new or updated content. For the full specification, refer to the [Jobs API reference](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/).

Operation | Method | Description  
---|---|---  
[Create](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create/) | `POST` | Trigger a new sync job  
[List](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/list/) | `GET` | List all jobs for an instance  
[Get](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/get/) | `GET` | Get job details  
[Logs](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/logs/) | `GET` | View job logs  
  
### Example: Trigger a sync job

Start a new sync job for an instance:
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/<INSTANCE_NAME>/jobs" \
      -H "Authorization: Bearer <API_TOKEN>"

[PreviousWorkers binding](https://developers.cloudflare.com/ai-search/api/instances/workers-binding/)[NextWorkers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/api/instances/rest-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
