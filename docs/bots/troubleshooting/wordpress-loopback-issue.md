---
url: https://developers.cloudflare.com/bots/troubleshooting/wordpress-loopback-issue/
title: Super Bot Fight Mode for WordPress \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:34.860863+00:00
---

# Super Bot Fight Mode for WordPress · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/troubleshooting/wordpress-loopback-issue/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Troubleshooting
  4. /Super Bot Fight Mode for WordPress



# Super Bot Fight Mode for WordPress

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/troubleshooting/wordpress-loopback-issue/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable Optimize for WordPressAvailability

When users attempt to run diagnostics in the Site Status page for WordPress installations, loopback issues arise when our bot detection services block them.

WordPress relies on making loopback requests to monitor and occasionally administer its websites. Customers can opt-in to optimize Super Bot Fight Mode for WordPress. If this feature is enabled, automated loopback requests made by your WordPress site will be authorized even when Super Bot Fight Mode blocks other bots.

Note

Loopback requests may also be blocked by [I’m Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/) or certain [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/).

## Enable Optimize for WordPress

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **Bot traffic**.

  3. Go to **Super Bot Fight Mode**.

  4. Under **Configurations** , select the edit icon for **Optimize for WordPress** and turn it on.




## Availability

This feature is available for all Super Bot Fight Mode customers.

[PreviousBot Management skips](https://developers.cloudflare.com/bots/troubleshooting/bot-management-skips/)[NextFalse positives](https://developers.cloudflare.com/bots/troubleshooting/false-positives/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/troubleshooting/wordpress-loopback-issue.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
