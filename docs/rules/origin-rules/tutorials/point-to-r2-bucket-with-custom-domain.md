---
url: https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-r2-bucket-with-custom-domain/
title: Point to R2 bucket with a custom domain \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:50.198908+00:00
---

# Point to R2 bucket with a custom domain · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-r2-bucket-with-custom-domain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Origin Rules](https://developers.cloudflare.com/rules/origin-rules/)

  4. /[Tutorials](https://developers.cloudflare.com/rules/origin-rules/tutorials/)
  5. /Point to R2 bucket with a custom domain



# Point to R2 bucket with a custom domain

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-r2-bucket-with-custom-domain/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Configure custom domain in your Pages project2\. Create origin rule to rewrite host header and override DNS record3\. (Optional) Configure URL rewriteMore resources

This tutorial will instruct you how to configure an origin rule and a DNS record to point to an R2 bucket configured with a custom domain.

The procedure will use the following example values:

URL that website visitors will access | `mycustomerexample.com/images/*`  
---|---  
R2 bucket custom domain | `imagesbucket.example.com`  
  
When configuring your R2 bucket's custom domain, use a custom domain that you do not plan to use in production (`imagesbucket.example.com` in this example).

## 1\. Configure custom domain in your Pages project

  1. In the Cloudflare dashboard, go to the **R2 object storage** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/overview)
  2. Select your bucket.

  3. On the bucket page, select **Settings**.

  4. Under **Public access** > **Custom Domains** , select **Connect Domain**.

  5. Enter the domain name you want to connect to — `imagesbucket.example.com` in this example — and select **Continue**.

  6. Review the new record that will be added to the DNS table and select **Connect Domain**.




Your domain is now connected. The status takes a few minutes to change from **Initializing** to **Active** , and you may need to refresh to review the status update. If the status has not changed, select the **...** next to your bucket and select **Retry connection**.

To view the added DNS record, select **...** next to the connected domain and select **Manage DNS**.

Note

The domain used must belong to the same account as the R2 bucket.

## 2\. Create origin rule to rewrite host header and override DNS record

In your `mycustomerexample.com` zone, create an origin rule with the following configuration:

**If incoming requests match**

Field | Operator | Value  
---|---|---  
URI Path | wildcard | `/images/*`  
  
If using the Expression Editor, enter the following expression:
    
    
    (http.request.uri.path wildcard "/images/*")

**Set origin parameters**

  * Value after **Host header** > **Rewrite to** : `imagesbucket.example.com`
  * Value after **DNS record** > **Override to** : `imagesbucket.example.com`



## 3\. (Optional) Configure URL rewrite

In our example, the URL that website visitors will access starts with `/images`. However, images stored in the example R2 bucket do not have this initial URL segment.

Use a URL rewrite to remove the `/images` segment from the URL path. Cloudflare provides a rule template in the dashboard called **Rewrite Path for Object Storage Bucket** that you can use to configure the required rewrite.

  1. In the Cloudflare dashboard, go to the Rules **Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)
  2. Select **Create rule** > **URL Rewrite Rule**.

  3. Enter a descriptive name for the rule in **Rule name**.

  4. In **If incoming requests match** , select **Wildcard pattern**.

  5. Enter the following value in **Request URL** :
         
         https://<YOUR_HOSTNAME>/images/*

In the current example, the value would be `https://mycustomerexample.com/images/*`.

  6. In **Then rewrite the path and/or query** , enter the following values under **Path** :

Target path | Rewrite to  
---|---  
[`/`] `images/*` | [`/`] `${1}`  
  
  7. Select **Deploy**.




Note

Cloudflare provides a rule template in the dashboard called **Rewrite Path for Object Storage Bucket** that you can use and adapt to configure the URL rewrite rule.

## More resources

  * [Tutorial: Change URI Path and Host Header](https://developers.cloudflare.com/rules/origin-rules/tutorials/change-uri-path-and-host-header/)
  * [Cloudflare R2: Public buckets](https://developers.cloudflare.com/r2/buckets/public-buckets/)
  * [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)



[PreviousPoint to Pages with a custom domain](https://developers.cloudflare.com/rules/origin-rules/tutorials/point-to-pages-with-custom-domain/)[NextAvailable settings](https://developers.cloudflare.com/rules/origin-rules/features/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/origin-rules/tutorials/point-to-r2-bucket-with-custom-domain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
