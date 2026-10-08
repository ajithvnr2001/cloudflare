---
url: https://developers.cloudflare.com/waf/detections/malicious-uploads/get-started/
title: Get started with malicious uploads detection \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:42.374866+00:00
---

# Get started with malicious uploads detection · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/malicious-uploads/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Malicious uploads](https://developers.cloudflare.com/waf/detections/malicious-uploads/)
  5. /Get started



# Get started

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/malicious-uploads/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Turn on the detection2\. Validate the content scanning behavior3\. Create a custom rule4\. (Optional) Configure a custom scan expression

Note

WAF content scanning is available to customers on an Enterprise plan with a paid add-on.

## 1\. Turn on the detection

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. (Optional) Filter by **Detection tools**.

  3. Turn on **Malicious uploads detection**.




Use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Enable Content Scanning for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/enable" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Use the `cloudflare_content_scanning` resource to enable content scanning for a zone. For example:
    
    
    resource "cloudflare_content_scanning" "zone_content_scanning_example" {
    	zone_id = var.cloudflare_zone_id
    	enabled = true
    }

Note

Enabling malicious uploads detection can introduce latency since content objects will be scanned. Latency can vary depending on object size.

## 2\. Validate the content scanning behavior

Use [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) and HTTP logs to validate that malicious content objects are being detected correctly.

You can use the [EICAR anti-malware test file ↗︎](https://www.eicar.org/download-anti-malware-testfile/) to test content scanning (select the ZIP format).

Alternatively, create a custom rule like described in the next step using a _Log_ action instead of a mitigation action like _Block_. This rule will generate [security events](https://developers.cloudflare.com/waf/analytics/security-events/) that will allow you to validate your configuration.

## 3\. Create a custom rule

[Create a custom rule](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/) that blocks detected malicious content objects uploaded to your application.

For example, create a custom rule with the _Block_ action and the following expression:

Field | Operator | Value  
---|---|---  
Has malicious content object | equals | True  
  
If you use the Expression Editor, enter the following expression:
    
    
    (cf.waf.content_scan.has_malicious_obj)

Rule action: _Block_

This rule will match requests where Cloudflare detects a suspicious or malicious content object. For a list of fields provided by WAF content scanning, refer to [Content scanning fields](https://developers.cloudflare.com/waf/detections/malicious-uploads/#content-scanning-fields).

Optional: Combine with other Rules language fields

You can combine the previous expression with other [fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/) and [functions](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/) of the Rules language. This allows you to customize the rule scope or combine content scanning with other security features. For example:

  * The following expression will match requests with malicious content objects uploaded to a specific endpoint:

Field | Operator | Value | Logic  
---|---|---|---  
Has malicious content object | equals | True | And  
URI Path | contains | `upload.php` |   
  
Expression when using the editor:
        
        (cf.waf.content_scan.has_malicious_obj and http.request.uri.path contains "upload.php")

  * The following expression will match requests from bots uploading content objects:

Field | Operator | Value | Logic  
---|---|---|---  
Has content object | equals | True | And  
Bot Score | less than | `10` |   
  
Expression when using the editor:
        
        (cf.waf.content_scan.has_obj and cf.bot_management.score lt 10)




For additional examples, refer to [Example rules](https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/).

## 4\. (Optional) Configure a custom scan expression

To check uploaded content in a way that is not covered by the default configuration, add a [custom scan expression](https://developers.cloudflare.com/waf/detections/malicious-uploads/#custom-scan-expressions).

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. (Optional) Filter by **Detection tools**.

  3. Under **Malicious uploads detection** > **Configurations** , select the edit icon.

  4. Select **Add content location**.

  5. In **Content location** , enter your custom scan expression. For example:
         
         lookup_json_string(http.request.body.raw, "file")

  6. Select **Save**.




Use a `POST` request similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`
  * `Account WAF Write`

Create Content Scanning custom expressions for a zone.bash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/content-upload-scan/payloads" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '[
    		{
    				"payload": "lookup_json_string(http.request.body.raw, \"file\")"
    		}
    	]'

The above request will add the following expression to the current list of custom scan expressions:
    
    
    lookup_json_string(http.request.body.raw, "file")

Use the `cloudflare_content_scanning_expression` resource to add a custom scan expression. For example:
    
    
    resource "cloudflare_content_scanning_expression" "my_custom_scan_expression" {
      zone_id = var.cloudflare_zone_id
      payload = "lookup_json_string(http.request.body.raw, \"file\")"
    }

For more information, refer to [Custom scan expressions](https://developers.cloudflare.com/waf/detections/malicious-uploads/#custom-scan-expressions).

[PreviousOverview](https://developers.cloudflare.com/waf/detections/malicious-uploads/)[NextExample rules](https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/malicious-uploads/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
