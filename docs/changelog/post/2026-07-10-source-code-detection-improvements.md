---
url: https://developers.cloudflare.com/changelog/post/2026-07-10-source-code-detection-improvements/
title: Source code detection improvements \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:35.050980+00:00
---

# Source code detection improvements · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-10-source-code-detection-improvements/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 10, 2026

## Source code detection improvements

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Data Loss Prevention (DLP) source code detection now focuses on identifying whole source code file uploads and downloads. Previously, source code detection performed partial scans resulting in a higher rate of false positives. Since only whole source code files are evaluated, code embedded in other content — such as chat messages, documentation, or code samples — is no longer flagged as source code, removing a common source of false positives.

Source code detection requires a minimum of 500 characters to evaluate a file. Files below this threshold are not flagged to reduce noise. This threshold filters out small fragments that lack enough context for reliable classification.

Enable and set [confidence levels](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds) to tune match sensitivity. A higher confidence level reduces false positives by requiring stronger signals that the content is truly source code. A lower confidence level catches more files at the cost of additional noise.

Source code detection applies to standalone source code files in [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/). It does not detect source code embedded within other file types or payloads, such as `.docx` files or chat messages.

For more information, refer to [Source Code predefined profiles](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code).
