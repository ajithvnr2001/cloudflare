---
url: https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/
title: New detection entry type: Document Matching for DLP \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:50.911278+00:00
---

# New detection entry type: Document Matching for DLP · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-07-17-document-matching/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 17, 2025

## New detection entry type: Document Matching for DLP

[Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create [document-based](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#document-entries) detection entries in DLP by uploading example documents. Cloudflare will encrypt your documents and create a unique fingerprint of the file. This fingerprint is then used to identify similar documents or snippets within your organization's traffic and stored files.

![DLP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1356,height=839,format=webp/_astro/document-match.CcN8pGgR.png)

**Key features and benefits:**

  * **Upload documents, forms, or templates:** Easily upload .docx and .txt files (up to 10 MB) that contain sensitive information you want to protect.

  * **Granular control with similarity percentage:** Define a minimum similarity percentage (0-100%) that a document must meet to trigger a detection, reducing false positives.

  * **Comprehensive coverage:** Apply these document-based detection entries in:

    * **Gateway policies:** To inspect network traffic for sensitive documents as they are uploaded or shared.

    * **CASB (Cloud Access Security Broker):** To scan files stored in cloud applications for sensitive documents at rest.

  * **Identify sensitive data:** This new detection entry type is ideal for identifying sensitive data within completed forms, templates, or even small snippets of a larger document, helping you prevent data exfiltration and ensure compliance.




Once uploaded and processed, you can add this new document entry into a DLP profile and policies to enhance your data protection strategy.
