---
url: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/
title: Ignore JavaScripts in Rocket Loader \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:34.830465+00:00
---

# Ignore JavaScripts in Rocket Loader · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

SettingsContent optimizations

  4. /[Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/)
  5. /Ignore JavaScripts



# Ignore JavaScripts

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLimitations

You can have Rocket Loader ignore individual scripts by adding the `data-cfasync="false"` attribute to the relevant script tag:
    
    
    <script data-cfasync="false" src="/javascript.js"></script>

Rocket Loader will still optimize the loading of all other scripts on the page.

Note

If Rocket Loader is only impacting a specific page, use a [Configuration Rule](https://developers.cloudflare.com/rules/configuration-rules/) to exclude that page by URL.

## Limitations

  * Adding this attribute within JavaScript will not work if you wish to exclude the script from Rocket Loader.
  * If the script you want Rocket Loader to ignore has dependency on other JavaScript(s) on the page, those dependencies must also have the `data-cfasync="false"` attribute.
  * The `data-cfasync` attribute must be added before the `src` attribute.
  * Rocket Loader will recognize the tag when either single or double quotes are placed around the attribute value.



[PreviousEnable](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/)[NextSpeed Brain](https://developers.cloudflare.com/speed/optimization/content/speed-brain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/content/rocket-loader/ignore-javascripts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
