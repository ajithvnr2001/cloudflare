---
url: https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/
title: Example rules checking uploaded content objects \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:41.994819+00:00
---

# Example rules checking uploaded content objects · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[Malicious uploads](https://developers.cloudflare.com/waf/detections/malicious-uploads/)
  5. /Example rules



# Example rules

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLog requests with an uploaded content objectBlock requests to URI path with a malicious content objectBlock requests with non-PDF file uploadsBlock requests with uploaded files over 500 KBBlock requests with uploaded files over the content scanning limit (50 MB)

## Log requests with an uploaded content object

This [custom rule](https://developers.cloudflare.com/waf/custom-rules/) example logs all requests with at least one uploaded content object:

  * **When incoming requests match:**

Field | Operator | Value  
---|---|---  
Has content object | equals | True  
  
If you are using the Expression Editor:  
`(cf.waf.content_scan.has_obj)`

  * **Action:** _Log_




## Block requests to URI path with a malicious content object

This custom rule example blocks requests addressed at `/upload.php` that contain at least one uploaded content object considered malicious:

  * **When incoming requests match:**

Field | Operator | Value |   
---|---|---|---  
Has malicious content object | equals | True | And  
URI Path | equals | `/upload.php` |   
  
If you are using the Expression Editor:  
`(cf.waf.content_scan.has_malicious_obj and http.request.uri.path eq "/upload.php")`

  * **Action:** _Block_




## Block requests with non-PDF file uploads

This custom rule example blocks requests addressed at `/upload` with uploaded content objects that are not PDF files:

  * **When incoming requests match:**  
`any(cf.waf.content_scan.obj_types[*] != "application/pdf") and http.request.uri.path eq "/upload"`
  * **Action:** _Block_



## Block requests with uploaded files over 500 KB

This custom rule example blocks requests addressed at `/upload` with uploaded content objects over 500 KB (512,000 bytes) in size:

  * **When incoming requests match:**  
`any(cf.waf.content_scan.obj_sizes[*] > 512000) and http.request.uri.path eq "/upload"`
  * **Action:** _Block_



## Block requests with uploaded files over the content scanning limit (50 MB)

This custom rule example blocks requests with uploaded content objects over 50 MB in size (the current content scanning limit):

  * **When incoming requests match:**  
`any(cf.waf.content_scan.obj_sizes[*] >= 52428800)`
  * **Action:** _Block_



In this example, you must also test for equality because currently any file over 50 MB will be handled internally as if it had a size of 50 MB (52,428,800 bytes). This means that using the `>` (greater than) [comparison operator](https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#comparison-operators) would not work for this particular rule — you should use `>=` (greater than or equal) instead.

[PreviousGet started](https://developers.cloudflare.com/waf/detections/malicious-uploads/get-started/)[NextCommon API calls](https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/malicious-uploads/example-rules.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
