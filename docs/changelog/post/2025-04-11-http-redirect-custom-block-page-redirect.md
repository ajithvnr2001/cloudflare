---
url: https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/
title: HTTP redirect and custom block page redirect \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:09.751466+00:00
---

# HTTP redirect and custom block page redirect · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 11, 2025

## HTTP redirect and custom block page redirect

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use more flexible redirect capabilities in Cloudflare One with Gateway.

  * A new **Redirect** action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.
  * For **Block** actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.



Learn more in our documentation for [HTTP Redirect](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#redirect) and [Block page redirect](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page).
