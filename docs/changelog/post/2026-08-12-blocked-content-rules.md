---
url: https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/
title: Block emails by content with blocked content rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:33.185393+00:00
---

# Block emails by content with blocked content rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-12-blocked-content-rules/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 12, 2026

## Block emails by content with blocked content rules

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Email security now lets administrators write their own content-based blocking rules. A new **Blocked content** area under **Policies & rules** lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.

  * Create rules using either **plaintext** matches or **regular expressions** — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.
  * Choose the **search location** for each rule: **subject** , **body** , or **subject and body**.
  * Use the built-in **regular expression checker** to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.
  * Matching messages are marked with a malicious [disposition](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/) and prevented from reaching users' inboxes.



Blocked content rules currently only support the block action.

This feature is available for the following Email security packages:

  * **Enterprise**
  * **Enterprise + PhishGuard**



To get started, refer to [Blocked content](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/blocked-content/).
