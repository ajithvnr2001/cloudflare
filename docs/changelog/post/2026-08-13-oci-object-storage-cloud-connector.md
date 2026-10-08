---
url: https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/
title: Oracle Cloud Infrastructure Object Storage support in Cloud Connector \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:08.307410+00:00
---

# Oracle Cloud Infrastructure Object Storage support in Cloud Connector · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 13, 2026

## Oracle Cloud Infrastructure Object Storage support in Cloud Connector

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-13-oci-object-storage-cloud-connector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.

OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional `oraclecloud.com` and dedicated `customer-oci.com` path-style endpoints.

Public buckets only

Cloud Connector does not sign requests or provide OCI credentials. Your bucket must allow anonymous object reads. Private buckets and pre-authenticated request URLs are not supported.

#### API example

Set `provider` to `oci_storage` and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:
    
    
    {
    	"expression": "http.request.uri.path wildcard \"/assets/*\"",
    	"provider": "oci_storage",
    	"description": "Route assets to OCI Object Storage",
    	"enabled": true,
    	"parameters": {
    		"host": "<BUCKET_NAME>.vhcompat.objectstorage.<REGION>.oci.customer-oci.com"
    	}
    }

For endpoint formats and bucket requirements, refer to [Supported cloud providers in Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage).
