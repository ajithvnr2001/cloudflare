---
url: https://developers.cloudflare.com/ai-crawl-control/reference/glossary/
title: Glossary \u00b7 Cloudflare AI Crawl Control docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:26.981636+00:00
---

# Glossary · Cloudflare AI Crawl Control docs

> Source: https://developers.cloudflare.com/ai-crawl-control/reference/glossary/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
  3. /Reference
  4. /Glossary



# Glossary

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-crawl-control/reference/glossary/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Review the definitions for terms used across Cloudflare's AI Crawl Control documentation.

Term| Definition  
---|---  
AI crawler| A bot which scrapes content from websites in support of an AI model, including by scraping content for indexing, retrieval augmented generation, or training.  
canonical URL| The preferred version of a web page, specified by a `<link rel="canonical">` HTML tag in the page's `<head>` section. When multiple URLs serve the same or similar content, the canonical URL tells search engines and crawlers which version is authoritative.  
category| A classification describing a crawler's stated purpose: "AI Crawler", "AI Search", "AI Assistant", or "Search Engine". One category per crawler.  
Content Signals| An emerging IETF standard for expressing AI content preferences via HTTP headers or metadata. Aims to replace non-standard vendor signals. Refer to contentsignals.org.  
crawl| A single HTTP request from a bot to access a page on your site.  
crawler| A specific bot operated by a company to access web content. One operator (like OpenAI) may run multiple crawlers (GPTBot, ChatGPT-User).  
In-band pricing| Pricing transmitted in HTTP response headers alongside content. In Pay Per Crawl, the origin sets prices via the `crawler-price` header.  
Merchant of Record| The entity who facilitates "buying and selling". For pay per crawl, Cloudflare is the merchant of record.  
operator| The company or organization that owns and operates an AI crawler. Examples include OpenAI, Microsoft, Google, ByteDance, Anthropic, and Meta. In AI Crawl Control, crawlers are grouped by their operators.  
Referrer| The site a user was on before visiting your domain, tracked via the HTTP Referer header. In AI Crawl Control, referrer data shows traffic arriving from AI platforms like ChatGPT or Perplexity.  
robots.txt| A text file at the root of a website that instructs crawlers which pages they should or should not access. Compliance is voluntary. AI Crawl Control helps monitor which crawlers violate your robots.txt rules.  
  
[PreviousWorker templates](https://developers.cloudflare.com/ai-crawl-control/reference/worker-templates/)[NextRedirects for AI Training](https://developers.cloudflare.com/ai-crawl-control/reference/redirects-for-ai-training/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-crawl-control/reference/glossary.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
