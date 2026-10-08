---
url: https://developers.cloudflare.com/rules/snippets/examples/rewrite-site-links/
title: Rewrite links on HTML pages \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:54.005765+00:00
---

# Rewrite links on HTML pages · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/rewrite-site-links/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Rewrite Site Links



# Rewrite links on HTML pages

Dynamically rewrite links in HTML responses.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/rewrite-site-links/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    export default {
    	async fetch(request) {
    		// Define the old hostname here.
    		const OLD_URL = "oldsite.com";
    		// Then add your new hostname that should replace the old one.
    		const NEW_URL = "newsite.com";
    
    		class AttributeRewriter {
    			constructor(attributeName) {
    				this.attributeName = attributeName;
    			}
    			element(element) {
    				const attribute = element.getAttribute(this.attributeName);
    				if (attribute) {
    					element.setAttribute(
    						this.attributeName,
    						attribute.replace(OLD_URL, NEW_URL),
    					);
    				}
    			}
    		}
    
    		const rewriter = new HTMLRewriter()
    			.on("a", new AttributeRewriter("href"))
    			.on("img", new AttributeRewriter("src"));
    
    		const res = await fetch(request);
    		if (!res.headers.has("Content-Type")) {
    			return res;
    		}
    		const contentType = res.headers.get("Content-Type");
    		if (typeof contentType !== "string") {
    			return res;
    		}
    
    		// If the response is HTML, it can be transformed with
    		// HTMLRewriter -- otherwise, it should pass through
    		if (contentType.startsWith("text/html")) {
    			return rewriter.transform(res);
    		} else {
    			return res;
    		}
    	},
    };

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/rewrite-site-links.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
