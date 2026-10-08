---
url: https://developers.cloudflare.com/version-management/reference/traffic-filters/
title: Traffic filters \u00b7 Cloudflare Version Management docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:15.115472+00:00
---

# Traffic filters · Cloudflare Version Management docs

> Source: https://developers.cloudflare.com/version-management/reference/traffic-filters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Version Management](https://developers.cloudflare.com/version-management/)
  3. /Reference
  4. /Traffic filters



# Traffic filters

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/version-management/reference/traffic-filters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you [create an environment](https://developers.cloudflare.com/version-management/how-to/environments/#create-environment), you specify a traffic filter for that environment. This filter ensures that all traffic reaching the environment and, by extension, the configuration changes associated with the environment's version is intentional.

To send traffic to a specific environment, send requests to your zone that match the pattern specified in your filter. These could be characteristics such as **Edge Server IP** , **Cookie** , **Hostname** , or **User Agent**.

To make sure requests are reaching an environment, review the [Metrics](https://developers.cloudflare.com/version-management/how-to/versions/#view-metrics) associated with your environment. These metrics will also help you evaluate whether your configuration changes are affecting traffic in the way you expect.

[PreviousAvailable configurations](https://developers.cloudflare.com/version-management/reference/available-configurations/)[NextRead-only environments](https://developers.cloudflare.com/version-management/reference/read-only-environments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/version-management/reference/traffic-filters.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
