---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/
title: Enable IBM QRadar \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:15.355103+00:00
---

# Enable IBM QRadar · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)Logpush job setup

  4. /[Enable destinations](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/)
  5. /Enable IBM QRadar



# Enable IBM QRadar

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHTTP Receiver Protocol Cloudflare Firewall events Cloudflare HTTP eventsAmazon AWS S3 Rest API

To configure a QRadar/Cloudflare integration you have the option to use one of the following methods:

  * [HTTP Receiver protocol](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/#http-receiver-protocol)
  * [Amazon AWS S3 Rest API](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-qradar/#amazon-aws-s3-rest-api)



## HTTP Receiver Protocol

To send Cloudflare logs to QRadar you need to create a [Logpush job to HTTP endpoints](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/http/) via API. Below you can find two curl examples of how to send Cloudflare Firewall events and Cloudflare HTTP events to QRadar.

### Cloudflare Firewall events

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Logs Write`

Create Logpush jobbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logpush/jobs" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "<NAME>",
    		"output_options": {
    				"field_names": [
    						"Action",
    						"ClientIP",
    						"ClientASN",
    						"ClientASNDescription",
    						"ClientCountry",
    						"ClientIPClass",
    						"ClientRefererHost",
    						"ClientRefererPath",
    						"ClientRefererQuery",
    						"ClientRefererScheme",
    						"ClientRequestHost",
    						"ClientRequestMethod",
    						"ClientRequestPath",
    						"ClientRequestProtocol",
    						"ClientRequestQuery",
    						"ClientRequestScheme",
    						"ClientRequestUserAgent",
    						"EdgeColoCode",
    						"EdgeResponseStatus",
    						"Kind",
    						"MatchIndex",
    						"Metadata",
    						"OriginResponseStatus",
    						"OriginatorRayID",
    						"RayID",
    						"RuleID",
    						"Source",
    						"Datetime"
    				],
    				"timestamp_format": "rfc3339"
    		},
    		"destination_conf": "<QRADAR_URL>:<LOG_SOURCE_PORT>",
    		"max_upload_bytes": 5000000,
    		"max_upload_records": 1000,
    		"dataset": "firewall_events",
    		"enabled": true
    	}'

### Cloudflare HTTP events

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Logs Write`

Create Logpush jobbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logpush/jobs" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "<NAME>",
    		"output_options": {
    				"field_names": [
    						"ClientRequestMethod",
    						"EdgeResponseStatus",
    						"ClientIP",
    						"ClientSrcPort",
    						"CacheCacheStatus",
    						"ClientCountry",
    						"ClientDeviceType",
    						"ClientIPClass",
    						"ClientMTLSAuthCertFingerprint",
    						"ClientMTLSAuthStatus",
    						"ClientRegionCode",
    						"ClientRequestBytes",
    						"ClientRequestHost",
    						"ClientRequestPath",
    						"ClientRequestProtocol",
    						"ClientRequestReferer",
    						"ClientRequestScheme",
    						"ClientRequestSource",
    						"ClientRequestURI",
    						"ClientRequestUserAgent",
    						"ClientSSLCipher",
    						"ClientSSLProtocol",
    						"ClientXRequestedWith",
    						"EdgeEndTimestamp",
    						"EdgeRequestHost",
    						"EdgeResponseBodyBytes",
    						"EdgeResponseBytes",
    						"EdgeServerIP",
    						"EdgeStartTimestamp",
    						"SecurityActions",
    						"SecurityRuleIDs",
    						"SecuritySources",
    						"OriginIP",
    						"OriginResponseStatus",
    						"OriginSSLProtocol",
    						"ParentRayID",
    						"RayID",
    						"SecurityAction",
    						"WAFAttackScore",
    						"SecurityRuleID",
    						"SecurityRuleDescription",
    						"WAFSQLiAttackScore",
    						"WAFXSSAttackScore",
    						"EdgeStartTimestamp"
    				],
    				"timestamp_format": "rfc3339"
    		},
    		"destination_conf": "<QRADAR_URL>:<LOG_SOURCE_PORT>",
    		"max_upload_bytes": 5000000,
    		"max_upload_records": 1000,
    		"dataset": "http_requests",
    		"enabled": true
    	}'

Cloudflare checks the accessibility of the IP address, port, and validates the certificate of the HTTP Receive log source. If all parameters are valid, a Logpush is created, and starts to send events to HTTP Receiver log source.

## Amazon AWS S3 Rest API

When you use the Amazon S3 REST API protocol, IBM QRadar collects Cloudflare Log events from an Amazon S3 bucket. To use this option, you need to:

  1. Create an [Amazon S3 bucket ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) to store your Cloudflare Logs. Make a note of the bucket name and the AWS access key ID and secret access key with sufficient permissions to write to the bucket.
  2. [Enable a Logpush to Amazon S3](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/aws-s3/).
  3. In the AWS Management Console, go to the Amazon S3 service. Create a bucket endpoint to allow Cloudflare to send logs directly to the S3 bucket.
  4. Follow the steps in [Integrate Cloudflare Logs with QRadar by using the Amazon AWS S3 REST API protocol ↗︎](https://www.ibm.com/docs/en/dsm?topic=configuration-cloudflare-logs).
  5. Test the configuration by generating some logs in Cloudflare and ensuring that they are delivered to the S3 bucket and subsequently forwarded to QRadar.



[PreviousEnable Amazon Kinesis](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/kinesis/)[NextEnable IBM Cloud Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/enable-destinations/ibm-qradar.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
