---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/
title: Enable Logpush to Google Cloud Storage \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:15.237178+00:00
---

# Enable Logpush to Google Cloud Storage · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup

  4. /[Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/)
  5. /Enable Google Cloud Storage



# Enable Google Cloud Storage

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManage via the Cloudflare dashboardCreate and get access to a GCS bucketCompression and decompressive transcoding

Cloudflare Logpush supports pushing logs directly to Google Cloud Storage (GCS) via the Cloudflare dashboard or via API.

## Manage via the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to the **Logpush** page at the account or domain (also known as zone) level.

For account: [ Go to **Logpush** ↗ ](https://dash.cloudflare.com/?to=/:account/logs)

For domain (also known as zone): [ Go to **Logpush** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/analytics/logs)

  2. Depending on your choice, you have access to [account-scoped datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) and [zone-scoped datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/), respectively.

  3. Select **Create a Logpush job**.



  4. In **Select a destination** , choose **Google Cloud Storage**.

  5. Enter or select the following destination details:

     * **Bucket** \- GCS bucket name
     * **Path** \- bucket location within the storage container
     * **Organize logs into daily subfolders** (recommended)
     * For **Grant Cloudflare access to upload files to your bucket** , make sure your bucket has added Cloudflare’s IAM as a user with a [Storage Object Admin role ↗︎](https://cloud.google.com/storage/docs/access-control/iam-roles).



When you are done entering the destination details, select **Continue**.

  6. To prove ownership, Cloudflare will send a file to your designated destination. To find the token, select the **Open** button in the **Overview** tab of the ownership challenge file, then paste it into the Cloudflare dashboard to verify your access to the bucket. Enter the **Ownership Token** and select **Continue**.

  7. Select the dataset to push to the storage service.

  8. In the next step, you need to configure your logpush job:

     * Enter the **Job name**.
     * Under **If logs match** , you can select the events to include and/or remove from your logs. Refer to [Filters](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/) for more information. Not all datasets have this option available.
     * In **Send the following fields** , you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.
  9. In **Advanced Options** , you can:

     * Choose the format of timestamp fields in your logs (`RFC3339` (default), `Unix`, or `UnixNano`).
     * Select a [sampling rate](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#sampling-rate) for your logs or push a randomly-sampled percentage of logs.
     * Enable redaction for `CVE-2021-44228`. This option will replace every occurrence of `${` with `x{`.
  10. Select **Submit** once you are done configuring your logpush job.




## Create and get access to a GCS bucket

Cloudflare uses Google Cloud Identity and Access Management (IAM) to gain access to your bucket. The Cloudflare IAM service account needs admin permission for the bucket.

Ensure **Log Share** permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the [Roles section](https://developers.cloudflare.com/logs/logpush/permissions/#roles).

  


To enable Logpush to GCS:

  1. Create a GCS bucket. Refer to [instructions from GCS ↗︎](https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-console).

  2. In **Storage** > **Browser** > **Bucket** > **Permissions** , add the member `logpush@cloudflare-data.iam.gserviceaccount.com` with `Storage Object Admin` permission.




## Compression and decompressive transcoding

Logpush always delivers log files in gzip-compressed format. When uploading to GCS, Logpush sets `Content-Encoding: gzip` on the object metadata.

GCS performs [decompressive transcoding ↗︎](https://cloud.google.com/storage/docs/transcoding) by default. This means that when a client downloads an object stored with `Content-Encoding: gzip`, GCS may automatically decompress the file in transit if the client does not include `Accept-Encoding: gzip` in the request headers. When this happens, the downloaded file contains uncompressed data even though the filename retains the `.gz` extension.

To download log files in their original compressed format, use one of the following approaches:

  * **Include`Accept-Encoding: gzip` in your download request headers.** For example, when using gsutil:
        
        gsutil -h "Accept-Encoding: gzip" cp gs://your-bucket/path/file.log.gz .




[PreviousEnable Elastic](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/elastic/)[NextEnable Google BigQuery](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/enable-destinations/google-cloud-storage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
