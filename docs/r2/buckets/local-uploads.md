---
url: https://developers.cloudflare.com/r2/buckets/local-uploads/
title: Local uploads \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:44.295849+00:00
---

# Local uploads · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/buckets/local-uploads/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /[Buckets](https://developers.cloudflare.com/r2/buckets/)
  4. /Local uploads



# Local uploads

Last updated Sep 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/buckets/local-uploads/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it works Without Local Uploads With Local UploadsWhen to use local uploads Read latency considerations Jurisdiction restrictionEnable local uploadsDisable local uploadsPricing

You can enable Local Uploads on your bucket to improve the performance of upload requests when clients upload data from a different region than your bucket. Local Uploads writes object data to a nearby location, then asynchronously copies it to your bucket. Data is available immediately and remains strongly consistent.

## How it works

The following sections describe how R2 handles upload requests with and without Local Uploads enabled.

### Without Local Uploads

When a client uploads an object to your R2 bucket, the object data must travel from the client to the storage infrastructure of your bucket. This behavior can result in higher latency and lower reliability when your client is in a different region than the bucket. Refer to [How R2 works](https://developers.cloudflare.com/r2/how-r2-works/) for details.

### With Local Uploads

When you make an upload request (i.e. `PutObject` and `UploadPart`) to a bucket with Local Uploads enabled, there are two cases that are handled:

  * **Client and bucket in same region:** R2 follows the normal upload flow where object data is uploaded from the client to the storage infrastructure of your bucket.
  * **Client and bucket in different regions:** Object data is written to storage near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains durable during the process.



Local uploads

ClientEastern North America

EdgeEastern North America

R2 Gateway Worker

EdgeEastern North America

R2 Gateway Worker

Object Data Infra

Object metadata

Object data

Your bucketEastern Europe

Metadata Service

Object Data Infra

Data is uploaded and accessible

## When to use local uploads

Local uploads are built for workloads that receive a lot of uploads originating from different geographic regions than where your bucket is located. This feature is ideal when:

  * Your users are globally distributed
  * Upload performance and reliability is critical to your application
  * You want to optimize write performance without changing your bucket's primary location



To understand the geographic distribution of where your read and write requests are initiated:

  1. Log in to the Cloudflare dashboard, and go to R2 Overview.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/overview)
  2. Select your bucket.

  3. Select **Metrics** and view the **Request Distribution** chart.




### Read latency considerations

When local uploads is enabled, uploaded data may temporarily reside near the client before replication completes.

If your workload requires immediate read after write, consider where your read requests originate. Reads from the uploader's region will be fast, while reads from near the bucket's region may experience cross-region latency until replication completes.

### Jurisdiction restriction

Local uploads are not supported for buckets with [jurisdictional restrictions](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions), because it requires temporarily routing data through locations outside the bucket’s region.

## Enable local uploads

When you enable Local Uploads, existing uploads will complete as expected with no interruption to traffic.

  1. Log in to the Cloudflare dashboard, and go to R2 Overview.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/overview)
  2. Select your bucket.

  3. Select **Settings**.

  4. Under **Local Uploads** , select **Enable**.




Run the following command:
    
    
    npx wrangler r2 bucket local-uploads enable <BUCKET_NAME>

## Disable local uploads

You can disable local uploads at any time. Existing requests made with local uploads will complete replication with no interruption to your traffic.

  1. Log in to the Cloudflare dashboard, and go to R2 Overview.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/overview)
  2. Select your bucket.

  3. Select **Settings**.

  4. Under **Local Uploads** , select **Disable**.




Run the following command:
    
    
    npx wrangler r2 bucket local-uploads disable <BUCKET_NAME>

## Pricing

There is **no additional cost** to enable local uploads. Upload requests made with this feature enabled incur the standard [Class A operation costs](https://developers.cloudflare.com/r2/pricing/), same as upload requests made without local uploads.

[PreviousData Access Logs](https://developers.cloudflare.com/r2/buckets/data-access-logs/)[NextDelete buckets](https://developers.cloudflare.com/r2/buckets/delete-buckets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/buckets/local-uploads.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
