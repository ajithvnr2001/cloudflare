---
url: https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/
title: Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:55.967475+00:00
---

# Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2024

## Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Organizations can now eliminate long-lived credentials from their SSH setup and enable strong multi-factor authentication for SSH access, similar to other Access applications, all while generating access and command logs.

SSH with [Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) uses short-lived SSH certificates from Cloudflare, eliminating SSH key management and reducing the security risks associated with lost or stolen keys. It also leverages a common deployment model for Cloudflare One customers: [WARP-to-Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/).

SSH with Access for Infrastructure enables you to:

  * **Author fine-grained policy** to control who may access your SSH servers, including specific ports, protocols, and SSH users.
  * **Monitor infrastructure access** with Access and SSH command logs, supporting regulatory compliance and providing visibility in case of security breach.
  * **Preserve your end users' workflows.** SSH with Access for Infrastructure supports native SSH clients and does not require any modifications to users’ SSH configs.

![Example of an infrastructure Access application](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1916,height=1714,format=webp/_astro/infrastructure-app.BhpJOgxs.png)

To get started, refer to [SSH with Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/).
