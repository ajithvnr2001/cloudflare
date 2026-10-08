---
url: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/how-do-i-enable-http2-server-push-in-wordpress/
title: How do I enable HTTP2 Server Push in WordPress \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:51.674152+00:00
---

# How do I enable HTTP2 Server Push in WordPress · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/how-do-i-enable-http2-server-push-in-wordpress/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Third-Party Software](https://developers.cloudflare.com/support/third-party-software/)

  4. /[Content Management System (CMS)](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/)
  5. /How do I enable HTTP2 Server Push in WordPress



# How do I enable HTTP2 Server Push in WordPress

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/how-do-i-enable-http2-server-push-in-wordpress/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

HTTP/2 Server Push allows a website to push content to a browser, without having to wait for the HTML of one page to render first. In conjunction with the concurrency support built into HTTP/2, Server Push is able to dramatically reduce the amount of requests needed to load your website.

![Old URL: https://support.cloudflare.com/hc/en-us/article_attachments/115005733367/http2-server-push-2.png
Article IDs: 115002816808 | How do I enable HTTP/2 Server Push in WordPress
](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=600,height=320,format=webp/_astro/hc-import-http2_server_push_2.CwfrU1Mt.png)

Cloudflare supports HTTP/2 Server Push and it can be enabled for stylesheets and scripts using Cloudflare’s WordPress plugin. In order to utilise this feature, you must first ensure you have the Cloudflare WordPress plugin [installed and set up on your site](https://developers.cloudflare.com/automatic-platform-optimization/).

Once the plugin is installed, you can enable HTTP/2 Server Push by adding the following line to your `wp-config.php` file:
    
    
    define('CLOUDFLARE_HTTP2_SERVER_PUSH_ACTIVE', true);

You should insert this line above where it says  _"/* That's all, stop editing! Happy blogging. */_ ", like follows:|

![Old URL: https://support.cloudflare.com/hc/en-us/article_attachments/115005733547/Screen_Shot_2017-02-09_at_16.09.31.png
Article IDs: 115002816808 | How do I enable HTTP/2 Server Push in WordPress
](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2044,height=814,format=webp/_astro/hc-import-screen_shot_2017_02_09_at_16_09_31.CgPyEpOq.png)

You should then start to see requests coming in which are initiated through Server Push, for example, in the Network tab of Chrome Development Tools you should see some assets have "Push" as the initiator:

![Old URL: https://support.cloudflare.com/hc/en-us/article_attachments/115005787688/Screen-Shot-2016-04-26-at-15-08-59.png
Article IDs: 115002816808 | How do I enable HTTP/2 Server Push in WordPress
](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1856,height=314,format=webp/_astro/hc-import-screen_shot_2016_04_26_at_15_08_59.CUaoZjsJ.png)

[PreviousCloudflare WordPress Plugin Automatic Cache Management](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/)[NextImproving web security for content management systems like WordPress](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/improving-web-security-for-content-management-systems-like-wordpress/)

Was this helpful?

YesNo
