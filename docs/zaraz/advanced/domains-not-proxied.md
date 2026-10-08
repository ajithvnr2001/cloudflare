---
url: https://developers.cloudflare.com/zaraz/advanced/domains-not-proxied/
title: Use Zaraz on domains not proxied by Cloudflare \u00b7 Cloudflare Zaraz docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:16.984855+00:00
---

# Use Zaraz on domains not proxied by Cloudflare · Cloudflare Zaraz docs

> Source: https://developers.cloudflare.com/zaraz/advanced/domains-not-proxied/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Zaraz](https://developers.cloudflare.com/zaraz/)
  3. /[Advanced options](https://developers.cloudflare.com/zaraz/advanced/)
  4. /Domains not proxied by Cloudflare



# Domains not proxied by Cloudflare

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/zaraz/advanced/domains-not-proxied/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can load Zaraz on domains that are not proxied through Cloudflare. However, you will need to create a separate domain, or subdomain, proxied by Cloudflare (also [known as orange-clouded ↗︎](https://community.cloudflare.com/t/step-3-enabling-the-orange-cloud/52715) domains), and load the script from it:

  1. Create a new subdomain like `my-subdomain.example.com` and proxy it through Cloudflare. Refer to [Enabling the Orange Cloud ↗︎](https://community.cloudflare.com/t/step-3-enabling-the-orange-cloud/52715) for more information.
  2. Add the following script to your main website’s HTML, immediately before the `</head>` tag closes:


    
    
    <script src="https://my-subdomain.example.com/cdn-cgi/zaraz/i.js"></script>

[PreviousData layer compatibility mode](https://developers.cloudflare.com/zaraz/advanced/datalayer-compatibility/)[NextGoogle Consent Mode](https://developers.cloudflare.com/zaraz/advanced/google-consent-mode/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/zaraz/advanced/domains-not-proxied.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
