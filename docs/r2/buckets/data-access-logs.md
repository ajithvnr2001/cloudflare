---
url: https://developers.cloudflare.com/r2/buckets/data-access-logs/
title: Data Access Logs \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:44.243129+00:00
---

# Data Access Logs · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/buckets/data-access-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /[Buckets](https://developers.cloudflare.com/r2/buckets/)
  4. /Data Access Logs



# Data Access Logs

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/buckets/data-access-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported interfacesLogged operationsTurn on Data Access LogsView Data Access LogsTurn off Data Access LogsLog fields

R2 Data Access Logs provide per-request records for object operations in a bucket. The logs are generally available for R2 buckets without a [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions).

Data Access Logs differ from [Audit Logs](https://developers.cloudflare.com/r2/platform/audit-logs/), which record bucket configuration changes. They also differ from [R2 metrics](https://developers.cloudflare.com/r2/platform/metrics-analytics/), which provide aggregated request and storage data.

Note

Data Access Logs include requests with HTTP status codes below `400`, including `304 Not Modified`. Log delivery is asynchronous and best effort, and events may be delayed or omitted. Requests with status codes of `400` or greater are excluded. Do not rely on Data Access Logs as a complete record of bucket activity.

## Supported interfaces

Data Access Logs record requests from these interfaces:

Interface | Source  
---|---  
`S3` | Requests through the S3-compatible API.  
`API` | Object operations from the Cloudflare dashboard or API.  
`Workers` | Object operations through an R2 binding. These events include the Worker script name.  
`Public` | Requests to public buckets through `r2.dev` or custom domains. These requests are unauthenticated.  
  
## Logged operations

Data Access Logs record the following operations:

Category | Operations  
---|---  
Read | `GetObject`, `HeadObject`  
Write and copy | `PutObject`, `CopyObject`  
List | `ListObjectsV1`, `ListObjectsV2`  
Multipart upload | `CreateMultipartUpload`, `UploadPart`, `UploadPartCopy`, `CompleteMultipartUpload`, `AbortMultipartUpload`, `ListMultipartUploads`, `ListParts`  
Delete | `DeleteObject`, `DeleteObjects`, `DeleteObjectsByPrefix`  
  
Bucket and configuration operations are not included. Failed requests with an HTTP status code of `400` or greater are also not included.

## Turn on Data Access Logs

  1. In the Cloudflare dashboard, go to the bucket you wish to enable.

[ Go to **Bucket settings** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/:bucket/settings)
  2. Under **Data Access Logs** , select _Enabled_.




R2 records new supported operations after you turn on Data Access Logs. Earlier operations are not added retroactively.

Data Access Logs have seven-day retention. Beginning December 1, 2026, they use [Cloudflare Observability pricing](https://developers.cloudflare.com/observability/pricing/).

## View Data Access Logs

In the **Data Access Logs** section of the bucket settings, select **View logs in Workers Observability**. The **Events** view opens with the `r2` dataset and current bucket selected for the previous hour.

Use the [Query Builder](https://developers.cloudflare.com/workers/observability/query-builder/) to change the time range, add filters, or aggregate events.

## Turn off Data Access Logs

  1. In the Cloudflare dashboard, go to the bucket you wish to disable.

[ Go to **Bucket settings** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/:bucket/settings)
  2. In **Data Access Logs** , select _Disabled_.




## Log fields

Every event can include these fields:

Field | Description  
---|---  
`$metadata.timestamp` | Event timestamp in Unix milliseconds.  
`$metadata.service` | Bucket name used as the service name.  
`$metadata.namespace` | Event namespace. The value is `r2`.  
`action` | R2 operation name.  
`actor.type` | Actor type: `user` or `service`. Public bucket requests use `service`.  
`actor.id` | Identifier for the authenticated actor. Public bucket requests use `public`.  
`actor.email` | Email address for a user actor.  
`actor.accessKeyId` | Access key ID for a request authenticated with AWS Signature Version 4.  
`bucket` | Target bucket name.  
`interface` | Request interface: `S3`, `API`, `Workers`, or `Public`.  
`request.bytes` | Request `Content-Length` value in bytes.  
`response.bytes` | Response `Content-Length` value in bytes.  
`response.errorCode` | Response error code. This value is `NotModified` for a `304` response and `null` for a `2xx` response.  
`response.errorMessage` | Response error message. This value describes a `304` response and is `null` for a `2xx` response.  
`requestMetadata.colo` | Cloudflare data center code, or `XXX` when the data center is unavailable.  
  
S3-compatible API, Cloudflare API, and public bucket events can also include these fields:

Field | Description  
---|---  
`request.method` | HTTP request method.  
`request.uri` | Request path.  
`response.status` | HTTP response status code.  
`requestMetadata.ip` | Client IP address.  
`requestMetadata.userAgent` | Client user agent.  
  
Workers binding events include this additional field:

Field | Description  
---|---  
`scriptName` | Name of the Worker script that triggered the operation.  
  
Workers binding events do not include the HTTP method, URI, response status, client IP address, or user agent.

An event can include these operation-specific fields:

Field | Description  
---|---  
`resource.key` | Object key.  
`resource.type` | Resource type: `object` or `multipart_upload`.  
`resource.size` | Object size in bytes when available.  
`resource.uploadId` | Upload ID for a multipart upload.  
`sourceResource` | Source bucket, key, and resource type for a copy operation.  
`prefix` | Prefix used by a list or prefix-delete operation.  
`delimiter` | Delimiter used by a list operation.  
`maxKeys` | Maximum keys requested by an object list operation.  
`maxUploads` | Maximum uploads requested by a multipart upload list operation.  
`objects` | Object keys included in a bulk delete operation.  
  
The `request.bytes` and `response.bytes` fields reflect `Content-Length` values, not exact transferred-byte measurements. A byte count or resource size of `0` can mean either zero bytes or that the value was unavailable when R2 created the event.

[PreviousConfigure CORS](https://developers.cloudflare.com/r2/buckets/cors/)[NextLocal uploads](https://developers.cloudflare.com/r2/buckets/local-uploads/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/buckets/data-access-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
