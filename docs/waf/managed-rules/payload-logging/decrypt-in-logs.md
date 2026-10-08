---
url: https://developers.cloudflare.com/waf/managed-rules/payload-logging/decrypt-in-logs/
title: Store decrypted matched payloads in logs \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:44.832608+00:00
---

# Store decrypted matched payloads in logs · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/managed-rules/payload-logging/decrypt-in-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Managed rules](https://developers.cloudflare.com/waf/managed-rules/)

  4. /[Log the payload of matched rules](https://developers.cloudflare.com/waf/managed-rules/payload-logging/)
  5. /Store decrypted matched payloads in logs



# Store decrypted matched payloads in logs

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/managed-rules/payload-logging/decrypt-in-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewStructure of encrypted_matched_data property in Logpush

You can include the encrypted matched payload in your [Logpush](https://developers.cloudflare.com/logs/logpush/) jobs by adding the **General** > [**Metadata**](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/firewall_events/#metadata) field from the Firewall Events dataset to your job.

The payload, in its encrypted form, is available in the `encrypted_matched_data` property of the `Metadata` field.

However, you may want to decrypt the matched payload before storing the logs in your SIEM system of choice. Cloudflare provides a [sample Worker project ↗︎](https://github.com/cloudflare/matched-data-worker) on GitHub that does the following:

  1. Behaves as an S3-compatible storage to receive logs from Logpush. These logs will contain encrypted matched payload data.
  2. Decrypts matched payload data using your private key.
  3. Sends the logs to the final log storage system with decrypted payload data.



You will need to make some changes to the sample project to push the logs containing decrypted payload data to your log storage system.

Refer to the Worker project's [README ↗︎](https://github.com/cloudflare/matched-data-worker/blob/main/README.md) for more information on configuring and deploying this Worker project.

## Structure of `encrypted_matched_data` property in Logpush

Matched payload information includes the specific string that triggered a rule, along with some text that appears immediately before and after the matched string.

Once you decrypt its value, the `encrypted_matched_data` property of the `Metadata` field in Logpush has a structure similar to the following:
    
    
    {
    	// for fields with only one match (such as URI or user agent fields):
    	"<match_location>": {
    		"before": "<text_before_match>",
    		"content": "<matched_text>",
    		"after": "<text_after_match>"
    	},
    	// for fields with possible multiple matches (such as form, header, or body fields):
    	"<match_location>": [
    		{
    			"before": "<text_before_match_1>",
    			"content": "<matched_text_1>",
    			"after": "<text_after_match_1>"
    		},
    		{
    			"before": "<text_before_match_2>",
    			"content": "<matched_text_2>",
    			"after": "<text_after_match_2>"
    		}
    	]
    }

The `before` and `after` properties are optional (there may be no content before/after the matched text) and will contain at most 15 bytes of content appearing before and after the match.

Below are a few examples of payload matches:

URI matchjson
    
    
    {
    	"http.request.uri": {
    		"before": "/admin",
    		"content": "/.git/",
    		"after": "config"
    	}
    }

Header value matchjson
    
    
    {
    	"http.request.headers.values[3]": [
    		{ "content": "phar://", "after": "example" }
    	]
    }

Raw body content matchjson
    
    
    {
    	"http.request.body.raw": {
    		"before": "NY>",
    		"content": "<!ENTITY xxe SYSTEM \"file:///dev/random\">] > ",
    		"after": "<foo>&xxe;</foo>"
    	}
    }

[PreviousConfigure via API](https://developers.cloudflare.com/waf/managed-rules/payload-logging/configure-api/)[NextOverview](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/managed-rules/payload-logging/decrypt-in-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
