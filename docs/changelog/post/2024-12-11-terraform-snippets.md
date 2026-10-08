---
url: https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/
title: Terraform Support for Snippets \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:59.924411+00:00
---

# Terraform Support for Snippets · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)December 11, 2024

## Terraform Support for Snippets

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2024-12-11-terraform-snippets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, you can manage [Cloudflare Snippets](https://developers.cloudflare.com/rules/snippets/) with [Terraform](https://developers.cloudflare.com/terraform/). Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.

Example Terraform configuration:
    
    
    resource "cloudflare_snippet" "my_snippet" {
    	zone_id  = "<ZONE_ID>"
    	name = "my_test_snippet_1"
    	main_module = "file1.js"
    	files {
    		name = "file1.js"
    		content = file("file1.js")
    	}
    }
    
    resource "cloudflare_snippet_rules" "cookie_snippet_rule" {
    	zone_id  = "<ZONE_ID>"
    	rules {
    		enabled = true
    		expression = "http.cookie eq \"a=b\""
    		description = "Trigger snippet on specific cookie"
    		snippet_name = "my_test_snippet_1"
    	}
    	depends_on = [cloudflare_snippet.my_snippet]
    }

Learn more in the [Configure Snippets using Terraform](https://developers.cloudflare.com/rules/snippets/create-terraform/) documentation.
