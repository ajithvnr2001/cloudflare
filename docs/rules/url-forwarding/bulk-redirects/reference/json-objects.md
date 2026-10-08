---
url: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/
title: Bulk Redirects API JSON objects \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:59.696477+00:00
---

# Bulk Redirects API JSON objects · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)[Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)

  4. /Reference
  5. /API JSON objects



# Bulk Redirects API JSON objects

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/json-objects/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBulk Redirect RuleURL redirect list item

## Bulk Redirect Rule

A fully populated Bulk Redirect Rule object has the following JSON structure:
    
    
    {
    	"action": "redirect",
    	"expression": "http.request.full_uri in $<LIST_NAME>",
    	"action_parameters": {
    		"from_list": {
    			"name": "<LIST_NAME>",
    			"key": "http.request.full_uri"
    		}
    	}
    }

The JSON object properties must comply with the following:

  * `action` must be `redirect`

  * `action_parameters` must contain a `from_list` object with additional settings.

  * `from_list` must contain the following properties:

    * `name`: The name of an existing Bulk Redirect List to associate with the current Bulk Redirect Rule.
    * `key`: An expression that defines the value that will be matched against the configured URL redirect's source URL values, following the rules of the [URL matching algorithm](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/#url-matching-algorithm). Refer to [Bulk Redirects concepts](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-rules) for more information.
  * `expression` must reference the request field used in the `key` property. Refer to [Bulk Redirects concepts](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-rules) for more information.




## URL redirect list item

A fully populated URL redirect list item object has the following JSON structure:
    
    
    {
    	"id": "7c5dae5552338874e5053f2534d2767a",
    	"redirect": {
    		"source_url": "https://example.com/blog",
    		"target_url": "https://example.com/blog/latest",
    		"status_code": 301,
    		"include_subdomains": false,
    		"subpath_matching": false,
    		"preserve_query_string": false,
    		"preserve_path_suffix": true
    	},
    	"created_on": "2021-10-11T12:39:02Z",
    	"modified_on": "2021-10-11T12:39:02Z"
    }

For details on the `redirect` object properties, refer to [URL redirect parameters](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/).

[PreviousCSV file format](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/)[NextFAQ](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/bulk-redirects/reference/json-objects.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
