---
url: https://developers.cloudflare.com/resource-tagging/get-started/
title: Get started \u00b7 Cloudflare Resource Tagging docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:44.689564+00:00
---

# Get started · Cloudflare Resource Tagging docs

> Source: https://developers.cloudflare.com/resource-tagging/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Resource Tagging](https://developers.cloudflare.com/resource-tagging/)
  3. /Get started



# Get started

Last updated Apr 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/resource-tagging/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Verify tagging is enabled Interpreting the response2\. Create your first tags3\. List tagged resourcesNext steps

This guide walks you through verifying that tagging works on your account and making your first API calls.

## Prerequisites

  * At least one user with the Super Administrator, Workers Admin, or Tag Admin role. These roles can create, update, and delete tags.
  * The API is the preferred interface for managing tags. You can also use the dashboard under **Manage Account** > **Resource Tagging** , but you should be comfortable making authenticated HTTP requests for automation workflows.
  * An API token with the required permissions. [Account Owned Tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) are recommended for automation.



## 1\. Verify tagging is enabled

Test the API to confirm tagging is active on your account:
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/keys" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "Content-Type: application/json"

### Interpreting the response

Response | Meaning | Action  
---|---|---  
**200 OK** with `{"success": true, "result": [...]}` | Tagging is enabled. An empty array is normal if no tags exist yet. | Proceed to the next step.  
**403** mentioning "permission" or "role" | The caller lacks required permissions. | Verify the caller has a Super Admin, Workers Admin, or Tag Admin role, or that the token has `#com.cloudflare.api.account.tag.list` scope.  
**403** mentioning "feature" or "gate" | Tagging is not enabled for this account. | Contact [Cloudflare support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) for assistance.  
**401 Unauthorized** | Authentication failed. | Verify the token is valid, not expired, and formatted correctly in the `Authorization: Bearer` header.  
Any other response | Unexpected error. | Capture the full response body and contact [Cloudflare support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) with the Account ID, request details, and timestamp.  
  
## 2\. Create your first tags

Set tags on a resource using `PUT`:
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "resource_type": "worker",
        "resource_id": "'"$RESOURCE_ID"'",
        "tags": {
          "environment": "production",
          "team": "platform"
        }
      }'

Then retrieve the tags:
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&resource_id=$RESOURCE_ID" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "Content-Type: application/json"

## 3\. List tagged resources

Query all tagged resources in the account, optionally filtering by tag:
    
    
    # All tagged resources
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources" \
      -H "Authorization: Bearer $API_TOKEN"
    
    # Filter: only resources with environment=production
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags/resources?tag=environment=production" \
      -H "Authorization: Bearer $API_TOKEN"

## Next steps

  * Learn the full [tag filtering syntax](https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/) for complex queries.
  * Understand the [GET, merge, PUT workflow](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/#add-a-single-tag) for modifying individual tags.
  * Review [supported resource types](https://developers.cloudflare.com/resource-tagging/reference/resource-types/) and their required fields.
  * Review [API limits and validation rules](https://developers.cloudflare.com/resource-tagging/reference/limits/).



[PreviousOverview](https://developers.cloudflare.com/resource-tagging/)[NextOverview](https://developers.cloudflare.com/resource-tagging/how-to/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/resource-tagging/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
