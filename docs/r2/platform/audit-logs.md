---
url: https://developers.cloudflare.com/r2/platform/audit-logs/
title: Audit Logs \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:47.853405+00:00
---

# Audit Logs · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/platform/audit-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /Platform
  4. /Audit Logs



# Audit Logs

Last updated Sep 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/platform/audit-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewViewing audit logsLogged operationsExample log entry

[Audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/) provide a comprehensive summary of changes made within your Cloudflare account, including those made to R2 buckets. This functionality is available on all plan types, free of charge, and is always enabled.

## Viewing audit logs

To view audit logs for your R2 buckets, go to the **Audit logs** page.

[ Go to **Audit logs** ↗ ](https://dash.cloudflare.com/?to=/:account/audit-log)

For more information on how to access and use audit logs, refer to [Review audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).

## Logged operations

The following configuration actions are logged:

Operation | Description  
---|---  
CreateBucket | Creation of a new bucket.  
DeleteBucket | Deletion of an existing bucket.  
AddCustomDomain | Addition of a custom domain to a bucket.  
RemoveCustomDomain | Removal of a custom domain from a bucket.  
ChangeBucketVisibility | Change to the managed public access (`r2.dev`) settings of a bucket.  
PutBucketStorageClass | Change to the default storage class of a bucket.  
PutBucketLifecycleConfiguration | Change to the object lifecycle configuration of a bucket.  
DeleteBucketLifecycleConfiguration | Deletion of the object lifecycle configuration for a bucket.  
PutBucketCors | Change to the CORS configuration for a bucket.  
DeleteBucketCors | Deletion of the CORS configuration for a bucket.  
  
Note

Audit Logs do not include data access operations, such as `GetObject` and `PutObject`. To record supported object operations with response status codes below `400`, use [R2 Data Access Logs](https://developers.cloudflare.com/r2/buckets/data-access-logs/).

Data Access Logs also include supported requests to public R2 buckets through `r2.dev` or custom domains.

## Example log entry

Below is an example of an audit log entry showing the creation of a new bucket:
    
    
    {
    	"action": { "info": "CreateBucket", "result": true, "type": "create" },
    	"actor": {
    		"email": "<ACTOR_EMAIL>",
    		"id": "3f7b730e625b975bc1231234cfbec091",
    		"ip": "fe32:43ed:12b5:526::1d2:13",
    		"type": "user"
    	},
    	"id": "5eaeb6be-1234-406a-87ab-1971adc1234c",
    	"interface": "API",
    	"metadata": { "zone_name": "r2.cloudflarestorage.com" },
    	"newValue": "",
    	"newValueJson": {},
    	"oldValue": "",
    	"oldValueJson": {},
    	"owner": { "id": "1234d848c0b9e484dfc37ec392b5fa8a" },
    	"resource": { "id": "my-bucket", "type": "r2.bucket" },
    	"when": "2024-07-15T16:32:52.412Z"
    }

[PreviousEvent subscriptions](https://developers.cloudflare.com/r2/platform/event-subscriptions/)[NextLimits](https://developers.cloudflare.com/r2/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/platform/audit-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
