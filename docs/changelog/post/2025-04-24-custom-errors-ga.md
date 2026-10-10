---
url: https://developers.cloudflare.com/changelog/post/2025-04-24-custom-errors-ga/
title: Custom Errors are now Generally Available \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:52.710572+00:00
---

# Custom Errors are now Generally Available · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-24-custom-errors-ga/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 24, 2025

## Custom Errors are now Generally Available

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Custom Errors](https://developers.cloudflare.com/rules/custom-errors/) are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.

You can now manage **Custom Error Rules** , **Custom Error Assets** , and redesigned **Error Pages** directly from the Cloudflare dashboard. These features let you deliver tailored messaging when errors occur, helping you maintain brand consistency and improve user experience — whether it’s a 404 from your origin or a security challenge from Cloudflare.

What's new:

  * **Custom Errors are now GA** – Available on all paid plans and ready for production traffic.
  * **UI for Custom Error Rules and Assets** – Manage your zone-level rules from the Rules > Overview and your zone-level assets from the Rules > Settings tabs.
  * **Define inline content or upload assets** – Create custom responses directly in the rule builder, upload new or reuse previously stored assets.
  * **Refreshed UI and new name for Error Pages** – Formerly known as “Custom Pages,” Error Pages now offer a cleaner, more intuitive experience for both zone and account-level configurations.
  * **Powered by Ruleset Engine** – Custom Error Rules support [conditional logic](https://developers.cloudflare.com/ruleset-engine/rules-language/) and override Error Pages for 500 and 1000 class errors, as well as errors originating from your origin or [other Cloudflare products](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/). You can also configure [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) to add, change, or remove HTTP headers from responses returned by Custom Error Rules.



Learn more in the [Custom Errors documentation](https://developers.cloudflare.com/rules/custom-errors/).
