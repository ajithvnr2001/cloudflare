---
url: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/
title: Enable Rocket Loader \u00b7 Cloudflare Speed docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:34.706683+00:00
---

# Enable Rocket Loader · Cloudflare Speed docs

> Source: https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Speed](https://developers.cloudflare.com/speed/)
  3. /…

SettingsContent optimizations

  4. /[Rocket Loader](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/)
  5. /Enable



# Enable

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/enable/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To enable or disable Rocket Loader, use the following instructions.

To enable or disable **Rocket Loader** in the dashboard:

  1. In the Cloudflare dashboard, go to the **Speed** > **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization)
  2. Go to **Content Optimization**.

  3. For **Rocket Loader** , switch the toggle to **On**.




If you have a Content Security Policy (CSP) in place for your domain, you will need to [update your headers](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/#product-requirements) to support Rocket Loader.

To enable or disable **Rocket Loader** with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `rocket_loader` as the setting name in the URI path, and the `value` parameter set to `"on"` or `"off"`.

If you have a Content Security Policy (CSP) in place for your domain, you will need to [update your headers](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/#product-requirements) to support Rocket Loader.

Note

To use this feature on specific hostnames - instead of across your entire zone - use a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/).

[PreviousOverview](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/)[NextIgnore JavaScripts](https://developers.cloudflare.com/speed/optimization/content/rocket-loader/ignore-javascripts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/speed/optimization/content/rocket-loader/enable.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
