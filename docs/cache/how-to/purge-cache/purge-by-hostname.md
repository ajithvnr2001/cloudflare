---
url: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/
title: \u200bPurge cache by hostname \u00b7 Cloudflare Cache (CDN) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:44.902482+00:00
---

# ​Purge cache by hostname · Cloudflare Cache (CDN) docs

> Source: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cache / CDN](https://developers.cloudflare.com/cache/)
  3. /…

Cache configuration

  4. /[Purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache/)
  5. /​Purge cache by hostname



# ​Purge cache by hostname

Last updated Aug 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewResulting cache status

Purging by hostname means that all assets at URLs with a host that matches one of the provided values will be instantly purged from the cache.

  1. In the Cloudflare dashboard, go to the **Configuration** page.

[ Go to **Configuration** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/caching/configuration)
  2. Under **Purge Cache** , select **Custom Purge**. The **Custom Purge** window appears.

  3. Under **Purge by** , select **Hostname**.

  4. Follow the syntax instructions:

     * One hostname per line.
     * Separated by commas.
     * You can purge up to 100 hostnames at a time.
  5. Enter the appropriate value(s) in the text field using the format shown in the example.

  6. Select **Purge**.




For information on rate limits, refer to the [Availability and limits](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits) section.

## Resulting cache status

Purging by hostname deletes the resource, resulting in the `CF-Cache-Status` header being set to [`MISS`](https://developers.cloudflare.com/cache/concepts/cache-responses/#miss) for subsequent requests.

If [tiered cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) is used, purging by hostname may return `EXPIRED`, as the lower tier tries to revalidate with the upper tier to reduce load on the latter. Depending on whether the upper tier has the resource or not, and whether the end user is reaching the lower tier or the upper tier, `EXPIRED` or `MISS` are returned.

[PreviousPurge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/)[Next​Purge cache by prefix (URL)](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cache/how-to/purge-cache/purge-by-hostname.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
