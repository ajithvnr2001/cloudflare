---
url: https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/
title: Manage tags \u00b7 Cloudflare Resource Tagging docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:44.866630+00:00
---

# Manage tags · Cloudflare Resource Tagging docs

> Source: https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Resource Tagging](https://developers.cloudflare.com/resource-tagging/)
  3. /[How-to guides](https://developers.cloudflare.com/resource-tagging/how-to/)
  4. /Manage tags



# Manage tags

Last updated Apr 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet tags on a resourceGet tags for a resourceAdd a single tagRemove a single tagDelete all tags

All tag operations use the Tagging API. Authentication requires an [account API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) or user API token with appropriate permissions.

## Set tags on a resource

Use `PUT` to set tags on an account-level resource. This operation replaces all existing tags on the resource.
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "resource_type": "worker",
        "resource_id": "'"$RESOURCE_ID"'",
        "tags": {
          "environment": "production",
          "team": "platform",
          "cost-center": "engineering"
        }
      }'

For zone-level resources, use the zone endpoint:
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/tags" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "resource_type": "zone",
        "resource_id": "'"$ZONE_ID"'",
        "tags": {
          "environment": "production",
          "customer": "acme-corp"
        }
      }'

Some resource types require additional fields. Refer to [supported resource types](https://developers.cloudflare.com/resource-tagging/reference/resource-types/) for details.

## Get tags for a resource

Retrieve tags for a specific resource:
    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&resource_id=$RESOURCE_ID" \
      -H "Authorization: Bearer $API_TOKEN"

Note

In the current beta, querying tags for a resource that does not exist or has never been tagged returns a `500` error instead of `404`. Verify the resource exists and has been tagged at least once.

## Add a single tag

The API does not support partial updates — `PUT` always replaces all tags. To add a tag without removing existing ones, use the `GET`, merge, `PUT` pattern:

  1. `GET` the current tags.


    
    
    curl -X GET "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&resource_id=$RESOURCE_ID" \
      -H "Authorization: Bearer $API_TOKEN"
    
    # Response: {"result": {"tags": {"environment": "production", "team": "platform"}}}

  2. Merge the new tag into the existing set locally.


    
    
    {
      "environment": "production",
      "team": "platform",
      "cost-center": "engineering"
    }

  3. `PUT` the complete merged tag set.


    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "resource_type": "worker",
        "resource_id": "'"$RESOURCE_ID"'",
        "tags": {
          "environment": "production",
          "team": "platform",
          "cost-center": "engineering"
        }
      }'

Caution

If you `PUT` only the new tag, all existing tags are deleted. Always `GET` first, merge locally, then `PUT` the complete set.

## Remove a single tag

Follow the same `GET`, merge, `PUT` pattern, but omit the tag you want to remove from the set before calling `PUT`.

## Delete all tags

To remove all tags from a resource:
    
    
    curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags" \
      -H "Authorization: Bearer $API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "resource_type": "worker",
        "resource_id": "'"$RESOURCE_ID"'"
      }'

This returns `204 No Content` on success. Only use `DELETE` when you want to remove all tags from a resource (for example, when decommissioning it).

[PreviousOverview](https://developers.cloudflare.com/resource-tagging/how-to/)[NextFilter resources by tag](https://developers.cloudflare.com/resource-tagging/how-to/filter-resources/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/resource-tagging/how-to/manage-tags.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
