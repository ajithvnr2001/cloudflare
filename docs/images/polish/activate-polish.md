---
url: https://developers.cloudflare.com/images/polish/activate-polish/
title: Activate Polish \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:36.254919+00:00
---

# Activate Polish · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/polish/activate-polish/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /[Cloudflare Polish](https://developers.cloudflare.com/images/polish/)
  4. /Activate Polish



# Activate Polish

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/polish/activate-polish/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Images in the [cache must be purged](https://developers.cloudflare.com/cache/how-to/purge-cache/) or expired before seeing any changes in Polish settings.

Caution

Do not activate Polish and [image transformations](https://developers.cloudflare.com/images/optimization/transformations/overview) simultaneously. Image transformations already apply lossy compression, which makes Polish redundant.

  1. In the Cloudflare dashboard, go to the **Account home** page.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Select the domain where you want to activate Polish.

  3. Select **Speed** > **Settings** > **Image Optimization**.

  4. Under **Polish** , select _Lossy_ or _Lossless_ from the drop-down menu. [_Lossy_](https://developers.cloudflare.com/images/polish/compression/#lossy) gives greater file size savings.

  5. (Optional) Select **WebP**. Enable this option if you want to further optimize PNG and JPEG images stored in the origin server, and serve them as WebP files to browsers that support this format.




To ensure WebP is not served from cache to a browser without WebP support, disable any WebP conversion utilities at your origin web server when using Polish.

Note

To use this feature on specific hostnames - instead of across your entire zone - use a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/).

[PreviousOverview](https://developers.cloudflare.com/images/polish/)[NextPolish compression](https://developers.cloudflare.com/images/polish/compression/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/polish/activate-polish.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
