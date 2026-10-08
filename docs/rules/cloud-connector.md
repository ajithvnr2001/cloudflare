---
url: https://developers.cloudflare.com/rules/cloud-connector/
title: Cloud Connector \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:45.503780+00:00
---

# Cloud Connector · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/cloud-connector/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /Cloud Connector



# Cloud Connector

Last updated Aug 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/cloud-connector/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksApplied configurationsAvailability

Cloud Connector (Beta) allows you to route matching incoming traffic from your website to a public cloud provider that you define: [Cloudflare R2](https://developers.cloudflare.com/r2/) object storage or an external provider such as AWS, Google Cloud, Microsoft Azure, and Oracle Cloud. With Cloud Connector, you can manage traffic to cloud-hosted content through the same Cloudflare dashboard you use for the rest of your website, without having to configure additional rules.

Note

Cloud Connector requires that you [proxy the DNS records](https://developers.cloudflare.com/dns/proxy-status/) of your domain (or subdomain) through Cloudflare.

## How it works

First, you configure a Cloud Connector rule that specifies:

  * The cloud provider and a supported cloud service that will accept traffic.
  * The traffic that will be routed to that cloud service.



Then, Cloudflare will create the necessary configurations so that the content is accessible for requests matching your Cloud Connector rule. Your object storage bucket must be publicly accessible for Cloud Connector to work.

Cloud Connector rules are evaluated last in the [request evaluation workflow](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/). When a Cloud Connector rule matches and other rules have modified the same settings (such as the `Host` header), the Cloud Connector rule takes precedence.

## Applied configurations

Cloud Connector will perform the following configurations automatically, depending on the cloud provider:

  * Modify the `Host` header.
  * Adjust SSL/TLS for bucket-related traffic ([AWS S3 website endpoints](https://developers.cloudflare.com/rules/cloud-connector/providers/#ssl-connections-to-aws-s3-endpoints) only).



Additional configurations you may need

Cloud Connector will not apply any of the following configurations:

  * **Cache content served from storage bucket** : To define custom cache behavior — like when to cache returned objects and for [how long](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#edge-ttl) — you will need to create a [cache rule](https://developers.cloudflare.com/cache/how-to/cache-rules/). For an example rule configuration, refer to [Cache Level (Cache Everything)](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything/).
  * **Create URL rewrites** : To adjust the URL structure from what your website visitors use to obtain a resource and the folder structure being used in the storage bucket, you will need to create a [URL rewrite](https://developers.cloudflare.com/rules/transform/url-rewrite/). For example, you could create a URL rewrite to remove the `/files` prefix from URI paths before routing the request to your object storage bucket. For an example configuration, refer to [Rewrite path for object storage bucket](https://developers.cloudflare.com/rules/transform/examples/rewrite-path-object-storage/).



## Availability

Cloud Connector is available in beta to all customers. The maximum number of rules depends on your Cloudflare plan:

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Number of rules | 10 | 25 | 50 | 300  
  
[PreviousCache Rules ↗︎](https://developers.cloudflare.com/cache/how-to/cache-rules/)[NextConfigure a rule in the dashboard](https://developers.cloudflare.com/rules/cloud-connector/create-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/cloud-connector/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
