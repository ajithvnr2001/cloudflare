---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/
title: Enable Logpush IBM Cloud Logs \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:15.418840+00:00
---

# Enable Logpush IBM Cloud Logs · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup

  4. /[Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/)
  5. /Enable IBM Cloud Logs



# Enable IBM Cloud Logs

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewManage via the Cloudflare dashboardManage via API 1\. Create a job

Cloudflare Logpush supports pushing logs directly to IBM Cloud Logs via dashboard or API.

## Manage via the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to the **Logpush** page at the account or domain (also known as zone) level.

For account: [ Go to **Logpush** ↗ ](https://dash.cloudflare.com/?to=/:account/logs)

For domain (also known as zone): [ Go to **Logpush** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/analytics/logs)

  2. Depending on your choice, you have access to [account-scoped datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/) and [zone-scoped datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/), respectively.

  3. Select **Create a Logpush job**.



  4. In **Select a destination** , choose **IBM Cloud Logs**.

  5. Enter the following destination information:



  * **HTTP Source Address** \- For example, `ibmcl://<INSTANCE_ID>.ingress.<REGION>.logs.cloud.ibm.com/logs/v1/singles`.
  * **IBM API Key** \- For more information refer to the [IBM Cloud Logs documentation ↗︎](https://cloud.ibm.com/docs/cloud-logs).



When you are done entering the destination details, select **Continue**.

  6. Select the dataset to push to the storage service.

  7. In the next step, you need to configure your logpush job:

     * Enter the **Job name**.
     * Under **If logs match** , you can select the events to include and/or remove from your logs. Refer to [Filters](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/) for more information. Not all datasets have this option available.
     * In **Send the following fields** , you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.
  8. In **Advanced Options** , you can:

     * Choose the format of timestamp fields in your logs (`RFC3339` (default), `Unix`, or `UnixNano`).
     * Select a [sampling rate](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#sampling-rate) for your logs or push a randomly-sampled percentage of logs.
     * Enable redaction for `CVE-2021-44228`. This option will replace every occurrence of `${` with `x{`.
  9. Select **Submit** once you are done configuring your logpush job.




## Manage via API

To set up an IBM Cloud Logs job:

  1. Create a job with the appropriate endpoint URL and authentication parameters.
  2. Enable the job to begin pushing logs.



Note

Ensure Log Share permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the [Roles section](https://developers.cloudflare.com/logs/logpush/permissions/#roles).

### 1\. Create a job

To create a job, make a `POST` request to the Logpush jobs endpoint with the following fields:

  * **name** (optional) - Use your domain name as the job name.
  * **output_options** (optional) - This parameter is used to define the desired output format and structure. Below are the configurable fields: 
    * output_type
    * timestamp_format
    * batch_prefix and batch_suffix
    * record_prefix and record_suffix
    * record_delimiter
  * **destination_conf** \- A log destination consisting of Instance ID, Region and [IBM API Key ↗︎](https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey) in the string format below.



`ibmcl://<INSTANCE_ID>.ingress.<REGION>.logs.cloud.ibm.com/logs/v1/singles?ibm_api_key=<IBM_API_KEY>`

  * **max_upload_records** (optional) - The maximum number of log lines per batch. This must be at least 1,000 lines or more. Note that there is no way to specify a minimum number of log lines per batch. This means that log files may contain many fewer lines than specified.
  * **max_upload_bytes** (optional) - The maximum uncompressed file size for a batch of logs. We recommend a default value of 2 MB per upload based on IBM's limits, which our system will enforce for this destination. Since minimum file sizes cannot be set, log files may be smaller than the specified batch size.
  * **dataset** \- The category of logs you want to receive. Refer to [Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/) for the full list of supported datasets.



Example request using cURL:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Logs Write`

Create Logpush jobbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logpush/jobs" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "<DOMAIN_NAME>",
    		"output_options": {
    				"output_type": "ndjson",
    				"timestamp_format": "rfc3339",
    				"batch_prefix": "[",
    				"batch_suffix": "]",
    				"record_prefix": "{\"applicationName\":\"ibm-platform-log\",\"subsystemName\":\"internet-svcs:logpush\",\"text\":{",
    				"record_suffix": "}}",
    				"record_delimiter": ","
    		},
    		"destination_conf": "ibmcl://<INSTANCE_ID>.ingress.<REGION>.logs.cloud.ibm.com/logs/v1/singles?ibm_api_key=<IBM_API_KEY>",
    		"max_upload_bytes": 2000000,
    		"dataset": "http_requests",
    		"enabled": true
    	}'

Response:
    
    
    {
      "errors": [],
      "messages": [],
      "result": {
        "id": <JOB_ID>,
        "dataset": "http_requests",
        "kind": "",
        "max_upload_bytes": 2000000,
        "enabled": true,
        "name": "<DOMAIN_NAME>",
        "output_options": {
          "output_type": "ndjson",
          "timestamp_format": "rfc3339",
          "batch_prefix": "[",
          "batch_suffix": "]",
          "record_prefix": "{\"applicationName\":\"ibm-platform-log\",\"subsystemName\":\"internet-svcs:logpush\",\"text\":{",
          "record_suffix": "}}",
          "record_delimiter": ","
        },
        "destination_conf": "ibmcl://<INSTANCE_ID>.ingress.<REGION>.logs.cloud.ibm.com/logs/v1/singles?ibm_api_key=<IBM_API_KEY>",
        "last_complete": null,
        "last_error": null,
        "error_message": null
      },
      "success": true
    }

Refer to [Manage Logpush with cURL](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-curl/) to update a job (including enabling and disabling).

[PreviousEnable IBM QRadar](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/)[NextEnable other providers](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/other-providers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
