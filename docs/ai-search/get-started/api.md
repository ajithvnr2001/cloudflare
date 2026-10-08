---
url: https://developers.cloudflare.com/ai-search/get-started/api/
title: REST API \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:41.459946+00:00
---

# REST API · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/get-started/api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /Get started
  4. /REST API



# REST API

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-search/get-started/api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Create an API token2\. Create an AI Search instance Connect a data source (optional)3\. Add content4\. Check indexing statusTry it outAdd to your application

This guide walks you through creating an AI Search instance using the REST API.

## 1\. Create an API token

You need an API token with **AI Search:Edit** and **AI Search:Run** permissions.

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




## 2\. Create an AI Search instance

Use the [Create instance API](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/) to create an instance. Replace `<ACCOUNT_ID>` with your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      --data '{
        "id": "my-instance"
      }'

### Connect a data source (optional)

You can create an instance that is connected to a website or R2 bucket as a data source. AI Search indexes the content automatically.

**Website:**

Automatically crawl and index a [website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/) that you own.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      --data '{
        "id": "my-instance",
        "type": "web-crawler",
        "source": "example.com"
      }'

**R2 bucket:**

Index documents stored in an [R2 bucket](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/). Connecting an R2 bucket requires a [service API token](https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/). If you have never created an R2-backed instance before, you need to pass the `token_id` field in the create request. Refer to the [service API token configuration](https://developers.cloudflare.com/ai-search/configuration/indexing/service-api-token/) for setup instructions.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      --data '{
        "id": "my-instance",
        "type": "r2",
        "source": "<R2_BUCKET_NAME>",
        "token_id": "<SERVICE_TOKEN_ID>"
      }'

## 3\. Add content

If you did not create an instance that is connected to a data source, upload files using the [Items API](https://developers.cloudflare.com/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/). You can skip this step if you connected a website or R2 bucket.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/my-instance/items" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -F "file=@/path/to/your/file.pdf"

AI Search indexes uploaded files automatically.

## 4\. Check indexing status

Check if your content has finished indexing.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/my-instance/stats" \
      -H "Authorization: Bearer <API_TOKEN>"

## Try it out

Once indexing is complete, run your first query.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/default/instances/my-instance/search" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "messages": [
          {
            "content": "How do I get started?",
            "role": "user"
          }
        ]
      }'

You can also test queries in the dashboard by going to your instance and selecting the **Playground** tab.

## Add to your application

### [Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)

Query AI Search directly from your Workers code.

### [REST API](https://developers.cloudflare.com/ai-search/api/search/rest-api/)

Query AI Search using HTTP requests.

[PreviousPython SDK](https://developers.cloudflare.com/ai-search/get-started/python/)[NextHow AI Search works](https://developers.cloudflare.com/ai-search/concepts/how-ai-search-works/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/get-started/api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
