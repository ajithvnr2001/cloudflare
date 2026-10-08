---
url: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/speed-up-wordpress-and-improve-performance/
title: Speed Up WordPress and Improve Performance \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:51.771572+00:00
---

# Speed Up WordPress and Improve Performance · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/speed-up-wordpress-and-improve-performance/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Third-Party Software](https://developers.cloudflare.com/support/third-party-software/)

  4. /[Content Management System (CMS)](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/)
  5. /Speed Up WordPress and Improve Performance



# Speed Up WordPress and Improve Performance

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/speed-up-wordpress-and-improve-performance/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Caching Anonymous Page Views Optimise Images Enable HTTP/2 Minify Assets Advanced Performance Tools

Cloudflare's CDN services can help cache your content across our giant global network, but performance isn't just about moving static files closer to your visitor. Cloudflare does more than offer a CDN, Cloudflare's optimisation features allow you to enhance the performance of your WordPress site beyond what a traditional CDN can do.

### Caching Anonymous Page Views

![Creating a cache rule for anonymous page views.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1674,height=1470,format=webp/_astro/hc-import-screen_shot_2017_03_09_at_16_54_36_1_.hRrVrFif.png)

Cloudflare's "[Bypass Cache on Cookie](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/)" functionality allows non-logged-in pages to be fully cached by Cloudflare. This means your server can save time and resources by not having to regenerate pages where the HTML is effectively static, whilst not interfering with dynamic behaviour - as soon as a user logs-in to the WordPress dashboard or adds something to their WooCommerce, the Edge cache is bypassed.

### Optimise Images

Images can be incredibly costly to page load times; fortunately, Cloudflare can dramatically help improve image load times. You can find these features in the Cloudflare dashboard by going to **Speed** > **Settings** > **Image Optimization**.

After enabling [**Polish**](https://developers.cloudflare.com/images/polish/), you can dramatically improve image and web page load times by compressing images and stripping metadata. Lossless will strip most metadata (`EXIF` data, for example) but doesn't change the image detail. Lossy will strip most metadata and compresses images by approximately 48 percent.

### Enable HTTP/2

**HTTP/2** allows for a multitude of performance features including multiplexing, header compression. In order to enable HTTP/2 on your WordPress site, ensure that your site is loaded over HTTPS.

After **enabling SSL** you must also ensure that users are redirected to the HTTPS version so that it can be loaded over HTTP/2. You can do this using an  _Always use HTTPS_ **Page Rule** :

![Create a page rule to ensure your Wordpress website is correctly loaded over HTTP/2](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1670,height=984,format=webp/_astro/hc-import-screen_shot_2016_09_30_at_15_34_14.DNIz1oVk.png)

Cloudflare's **WordPress plugin** allows you to push necessary assets to your users using HTTP/2 Server Push, dramatically reducing the amount of roundtrips required to load CSS and JavaScript. Refer to [How do I enable HTTP/2 Server Push in WordPress ↗︎](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/how-do-i-enable-http2-server-push-in-wordpress/) for a tutorial on setting it up.

### Minify Assets

If you are using Grunt or Gulp as part of a build process, you can implement minification in your builds.

Due to HTTP/2 multiplexing requests, we advise against concatenating CSS or JavaScript files together or installing anything on your server which may do this.

### Advanced Performance Tools

Enterprise users can utilise [Prefetching URLs From HTML Headers](https://developers.cloudflare.com/speed/optimization/content/prefetch-urls/) and [custom cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/) to enhance caching.

[PreviousImproving web security for content management systems like WordPress](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/improving-web-security-for-content-management-systems-like-wordpress/)[NextWhat settings are applied when I click Optimize Cloudflare for WordPress in Cloudflare's WordPress plugin](https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/what-settings-are-applied-when-i-click-optimize-cloudflare-for-wordpress-in-cloudflares-wordpress-plugin/)

Was this helpful?

YesNo
