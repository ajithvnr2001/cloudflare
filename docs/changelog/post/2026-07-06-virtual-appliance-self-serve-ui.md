---
url: https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/
title: Self-serve registration of Cloudflare One Virtual Appliance in the dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:01.296752+00:00
---

# Self-serve registration of Cloudflare One Virtual Appliance in the dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 6, 2026

## Self-serve registration of Cloudflare One Virtual Appliance in the dashboard

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now register a [Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) and generate its license key directly from the dashboard, without contacting your account team.

![Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=988,format=webp/_astro/2026-07-06-virtual-appliance-self-serve-ui.Dn2NC_ql.gif)

  * On the **Connectors** page, select **Add an appliance** and choose **Virtual appliance** to register a virtual appliance and generate its authentication key.
  * Use **Regenerate authentication key** from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.
  * The authentication key is shown only once — copy and store it securely.



This complements the existing [API and Terraform self-serve workflow](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key) for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).
