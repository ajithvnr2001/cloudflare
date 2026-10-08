---
url: https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/
title: Pause Cloudflare \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:22.818245+00:00
---

# Pause Cloudflare · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /[Domains](https://developers.cloudflare.com/fundamentals/manage-domains/)
  4. /Pause Cloudflare



# Pause Cloudflare

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAlternatives to global pause Disable proxy on DNS records Enable Development Mode

To troubleshoot your site, you can pause Cloudflare globally. This will send traffic directly to your origin web server instead of Cloudflare's reverse proxy. Paused domains also cannot use Cloudflare services like [Rules](https://developers.cloudflare.com/rules/), [WAF](https://developers.cloudflare.com/waf/), and [SSL/TLS certificates](https://developers.cloudflare.com/ssl/edge-certificates/). Consider turning on [Development Mode](https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/#enable-development-mode) to bypass caching while preserving protection.

  1. In the Cloudflare dashboard, go to the **Account home** page and select your account and domain.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Within **Overview** , choose **Advanced Actions** > **Pause Cloudflare on Site**.




The process of pausing Cloudflare takes five minutes or less. This approach is preferable to [changing nameservers](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/), which can cause propagation delays of several hours.

Note

Disabling a zone does not impact Spectrum applications.

* * *

## Alternatives to global pause

### Disable proxy on DNS records

Instead of pausing Cloudflare globally, you can disable the proxy on individual records:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and select your account and domain.

  2. Go to **DNS** > **Records**. Choose the record and select **Edit**.

  3. Toggle **Proxy Status** to **Off**.




Adjusting the proxy status will prevent that record from using Cloudflare services like [Rules](https://developers.cloudflare.com/rules/), [WAF](https://developers.cloudflare.com/waf/), and [SSL/TLS certificates](https://developers.cloudflare.com/ssl/edge-certificates/).

### Enable Development Mode

To troubleshoot caching issues, you could [enable Development Mode](https://developers.cloudflare.com/cache/reference/development-mode/). This will bypass Cloudflare's cache while still preserving Cloudflare services like [Rules](https://developers.cloudflare.com/rules/), [WAF](https://developers.cloudflare.com/waf/), and [SSL/TLS certificates](https://developers.cloudflare.com/ssl/edge-certificates/).

[PreviousOnboard a domain](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/)[NextRedirect one domain to another](https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/manage-domains/pause-cloudflare.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
