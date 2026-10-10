---
url: https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/
title: Self-serve provisioning of Cloudflare One Virtual Appliance via API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.712659+00:00
---

# Self-serve provisioning of Cloudflare One Virtual Appliance via API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-07-virtual-appliance-self-serve-api/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 7, 2026

## Self-serve provisioning of Cloudflare One Virtual Appliance via API

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.

  * Create a virtual appliance and receive a license key: `POST /accounts/{account_id}/magic/connectors` with `device.provision_license: true`.
  * Rotate the license key for an existing virtual appliance: `PATCH /accounts/{account_id}/magic/connectors/{connector_id}` with `provision_license: true`. The previous key is immediately and irrevocably revoked.
  * Delete a virtual appliance to release the associated licensed device.



The license key is returned in the response only once, at create or rotate time. Copy and store it securely.

For details, refer to [Configure a Cloudflare One Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/).
