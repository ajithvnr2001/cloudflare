---
url: https://developers.cloudflare.com/stream/transform-videos/sources/
title: Define source origin \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:49.941245+00:00
---

# Define source origin · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/transform-videos/sources/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Transform videos](https://developers.cloudflare.com/stream/transform-videos/)
  4. /Define source origin



# Define source origin

Last updated Sep 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/stream/transform-videos/sources/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure originsAllow source videos only from allowed originsAllow source videos from any origin

When optimizing remote videos, you can specify which origins can be used as the source for transformed videos. By default, Cloudflare accepts only source videos from the zone where your transformations are served.

On this page, you will learn how to define and manage the origins for the source videos that you want to optimize.

Note

The allowed origins setting applies to requests from Cloudflare Workers.

If you use a Worker to optimize remote videos via a `fetch()` subrequest, then this setting may conflict with existing logic that handles source videos.

## Configure origins

To get started, you must have [transformations enabled on your zone](https://developers.cloudflare.com/stream/transform-videos/#getting-started).

In the Cloudflare dashboard, go to **Stream** > **Transformations** and select the zone where you want to serve transformations.

In **Sources** , you can configure the origins for transformations on your zone.

![Enable allowed origins from the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1664,height=872,format=webp/_astro/allowed-origins.4hu5lHws.png)

## Allow source videos only from allowed origins

You can restrict source videos to **allowed origins** , which applies transformations only to source videos from a defined list.

By default, your accepted sources are set to **allowed origins**. Cloudflare will always allow source videos from the same zone where your transformations are served.

If you request a transformation with a source video from outside your **allowed origins** , then the video will be rejected. For example, if you serve transformations on your zone `a.com` and do not define any additional origins, then `a.com/video.mp4` can be used as a source video, but `b.com/video.mp4` will return an error.

To define a new origin:

  1. From **Sources** , select **Add origin**.
  2. Under **Domain** , specify the domain for the source video. Only valid web URLs will be accepted.

![Add the origin for source videos in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2142,height=1104,format=webp/_astro/add-origin.BtfOyoOS.png)

When you add a root domain, subdomains are not accepted. In other words, if you add `b.com`, then source videos from `media.b.com` will be rejected.

To support individual subdomains, define an additional origin such as `media.b.com`. If you add only `media.b.com` and not the root domain, then source videos from the root domain (`b.com`) and other subdomains (`cdn.b.com`) will be rejected.

To support all subdomains, use the `*` wildcard at the beginning of the root domain. For example, `*.b.com` will accept source videos from the root domain (like `b.com/video.mp4`) as well as from subdomains (like `media.b.com/video.mp4` or `cdn.b.com/video.mp4`).

  3. Optionally, you can specify the **Path** for the source video. If no path is specified, then source videos from all paths on this domain are accepted.



Cloudflare checks whether the defined path is at the beginning of the source path. If the defined path is not present at the beginning of the path, then the source video will be rejected.

For example, if you define an origin with domain `b.com` and path `/themes`, then `b.com/themes/video.mp4` will be accepted but `b.com/media/themes/video.mp4` will be rejected.

  4. Select **Add**. Your origin will now appear in your list of allowed origins.
  5. Select **Save**. These changes will take effect immediately.



When you configure **allowed origins** , only the initial URL of the source video is checked. Any redirects, including URLs that leave your zone, will be followed, and the resulting video will be transformed.

If you change your accepted sources to **any origin** , then your list of sources will be cleared and reset to default.

## Allow source videos from any origin

When your accepted sources are set to **any origin** , any publicly available video can be used as the source video for transformations on this zone.

**Any origin** is less secure and may allow third parties to serve transformations on your zone.

[PreviousBind to Workers API](https://developers.cloudflare.com/stream/transform-videos/bindings/)[NextTroubleshooting](https://developers.cloudflare.com/stream/transform-videos/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/transform-videos/sources.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
