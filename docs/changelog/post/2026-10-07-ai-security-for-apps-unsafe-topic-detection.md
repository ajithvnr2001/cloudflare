---
url: https://developers.cloudflare.com/changelog/post/2026-10-07-ai-security-for-apps-unsafe-topic-detection/
title: Updated unsafe topic detection for AI Security for Apps \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-09T10:55:29.820143+00:00
---

# Updated unsafe topic detection for AI Security for Apps · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-07-ai-security-for-apps-unsafe-topic-detection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 7, 2026

## Updated unsafe topic detection for AI Security for Apps

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Security for Apps now supports an updated set of categories for detecting unsafe topics in incoming prompts.

The values available in [`cf.llm.prompt.unsafe_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/) have changed. Existing WAF custom rules remain valid, but rules that reference a removed or renamed category will no longer match that category. Review any rules that use this field and update their expressions to use the currently supported values.

For category descriptions and configuration guidance, refer to [Unsafe topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/).
