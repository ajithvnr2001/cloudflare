---
url: https://developers.cloudflare.com/rules/compression-rules/examples/disable-compression-avif/
title: Disable compression for AVIF images \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:47.346264+00:00
---

# Disable compression for AVIF images · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/compression-rules/examples/disable-compression-avif/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Compression Rules](https://developers.cloudflare.com/rules/compression-rules/)

  4. /[Examples](https://developers.cloudflare.com/rules/compression-rules/examples/)
  5. /Disable compression for AVIF images



# Disable compression for AVIF images

Create a compression rule to turn off compression for AVIF images, based on either the content type or the file extension specified in the request.

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/compression-rules/examples/disable-compression-avif/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following example rule will disable compression for AVIF images, based on either the content type or the file extension specified in the request.

**When incoming requests match**

  * Custom filter expression: 
    * _Media Type_ _equals_ `image/avif` **OR**
    * _File extension_ _equals_ `avif`



**Then**

  * **Compression options** > _Disable compression_



The following example sets the rules of an existing [entry point ruleset](https://developers.cloudflare.com/ruleset-engine/about/rulesets/#entry-point-ruleset) (with ID `{ruleset_id}`) for the `http_response_compression` phase to a single compression rule, using the [Update a zone ruleset](https://developers.cloudflare.com/api/resources/rulesets/methods/update/) operation:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Response Compression Write`
  * `Config Settings Write`
  * `Dynamic URL Redirects Write`
  * `Cache Settings Write`
  * `Custom Errors Write`
  * `Origin Write`
  * `Managed headers Write`
  * `Zone Transform Rules Write`
  * `Mass URL Redirects Write`
  * `Magic Firewall Write`
  * `L4 DDoS Managed Ruleset Write`
  * `HTTP DDoS Managed Ruleset Write`
  * `Sanitize Write`
  * `Transform Rules Write`
  * `Select Configuration Write`
  * `Bot Management Write`
  * `Zone WAF Write`
  * `Account WAF Write`
  * `Account Rulesets Write`
  * `Logs Write`
  * `Logs Write`

Update a zone rulesetbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/rulesets/$RULESET_ID" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"rules": [
    				{
    						"ref": "disable_compression_for_avif",
    						"expression": "http.response.content_type.media_type eq \"image/avif\" or http.request.uri.path.extension eq \"avif\"",
    						"action": "compress_response",
    						"action_parameters": {
    								"algorithms": [
    										{
    												"name": "none"
    										}
    								]
    						}
    				}
    		]
    	}'

Use the `ref` field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to [Troubleshooting](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications) in the Terraform documentation.

[PreviousDisable Brotli compression](https://developers.cloudflare.com/rules/compression-rules/examples/disable-all-brotli/)[NextEnable Zstandard compression for default content types](https://developers.cloudflare.com/rules/compression-rules/examples/enable-zstandard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/compression-rules/examples/disable-compression-avif.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
