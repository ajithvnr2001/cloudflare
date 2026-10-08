---
url: https://developers.cloudflare.com/cache/reference/development-mode/
title: Development Mode \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:45.907620+00:00
---

# Development Mode · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/reference/development-mode/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /Reference
  4. /Development Mode



# Development Mode

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/reference/development-mode/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable Development Mode

Development Mode temporarily suspends Cloudflare's edge caching and [Polish](https://developers.cloudflare.com/images/polish/) features for three hours unless disabled beforehand. Development Mode allows customers to immediately observe changes to their [cacheable content](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#default-cached-file-extensions) like images, CSS, or JavaScript.

Note

To bypass cache for longer than three hours, use bypass cache in [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#bypass-cache).

## Enable Development Mode

Development Mode temporarily bypasses Cloudflare's cache and does not purge cached files. To instantly purge your Cloudflare cache, refer to [purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache/).

  1. In the Cloudflare dashboard, go to the **Configuration** page.

[ Go to **Configuration** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/caching/configuration)
  2. Toggle **Development Mode** to **On**.




[PreviousCSAM Scanning Tool](https://developers.cloudflare.com/cache/reference/csam-scanning/)[NextRange request behavior](https://developers.cloudflare.com/cache/reference/range-requests/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/reference/development-mode.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
