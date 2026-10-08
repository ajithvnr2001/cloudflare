---
url: https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/
title: Preview sent emails in the Activity log \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.850347+00:00
---

# Preview sent emails in the Activity log · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 17, 2026

## Preview sent emails in the Activity log

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-17-email-message-preview/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now preview the content of sent emails directly from the Email Service Activity log. Expand a sent email and open the new **Preview** section to inspect the message as it was sent, across tabs for the rendered **HTML** body, the **Text** body, the **Headers** , the **Attachments** , and the full **Raw** [RFC 5322 ↗︎](https://datatracker.ietf.org/doc/html/rfc5322) source.

![The rendered HTML preview of a sent email in the Email Service Activity log](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2864,height=1172,format=webp/_astro/email-message-preview.Bj6Lk8Y6.png)

Previously, the Activity log surfaced delivery and authentication metadata but not the message content, making rendering and content issues harder to debug. Message preview closes that gap.

To make messages previewable, turn on **Email preview** in your sending domain's settings. Previews cover messages sent while the setting is turned on and are retained for about seven days. Sending domains onboarded on or after 2026-07-02 have **Email preview** turned on automatically.

![The Email preview setting in a sending domain's settings](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2256,height=264,format=webp/_astro/email-preview-setting.XEd1WIiO.png)

Refer to [Email logs](https://developers.cloudflare.com/email-service/observability/logs/#message-preview) for more information.
