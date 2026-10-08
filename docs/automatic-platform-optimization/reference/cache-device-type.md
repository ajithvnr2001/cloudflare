---
url: https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/
title: Cache by device type \u00b7 Cloudflare Automatic Platform Optimization docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:22.329540+00:00
---

# Cache by device type · Cloudflare Automatic Platform Optimization docs

> Source: https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/)
  3. /[Reference](https://developers.cloudflare.com/automatic-platform-optimization/reference/)
  4. /Cache by device type



# Cache by device type

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

APO cache by device type provides all of the same benefits of Cloudflare's cache while targeting visitors with content appropriate to their device. Cloudflare evaluates the `User-Agent` header in the HTTP request to identify the device type. Cloudflare then identifies each device type with a case insensitive match to the regex below:

  * **Mobile** : `(?:phone|windows\s+phone|ipod|blackberry|(?:android|bb\d+|meego|silk|googlebot) .+? mobile|palm|windows\s+ce|opera mini|avantgo|mobilesafari|docomo|kaios)`
  * **Tablet** : `(?:ipad|playbook|(?:android|bb\d+|meego|silk)(?! .+? mobile))`
  * **Desktop** : Everything else not matched above.



To enable caching by device type, enable the setting from the Cloudflare dashboard's APO card or from the WordPress plugin version 4.4.0 or later.

Once enabled, Cloudflare sends a `CF-Device-Type` HTTP header to your origin with a value of either `mobile`, `tablet`, `desktop` for every request to specify the visitor’s device type. If your origin responds with the appropriate content for that device type, Cloudflare only caches the resource for that specific device type.

Note

Changing Cache By Device Type setting will invalidate Cache.

The Cloudflare for WordPress plugin automatically purges all cache variations for updated pages.

Cloudflare recommends that you use plugins that support cache by device type, which you may have to enable on the plugin. You will still need to test your plugins to make sure they behave as expected.

[PreviousPage Rule integration with APO](https://developers.cloudflare.com/automatic-platform-optimization/reference/page-rule-integration/)[NextSubdomains and subdirectories](https://developers.cloudflare.com/automatic-platform-optimization/reference/subdomain-subdirectories/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/automatic-platform-optimization/reference/cache-device-type.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
