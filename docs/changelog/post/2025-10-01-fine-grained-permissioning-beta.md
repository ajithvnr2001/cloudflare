---
url: https://developers.cloudflare.com/changelog/post/2025-10-01-fine-grained-permissioning-beta/
title: Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:24.942318+00:00
---

# Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-10-01-fine-grained-permissioning-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2025

## Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-01-fine-grained-permissioning-beta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Fine-grained permissions for **Access Applications, Identity Providers (IdPs), and Targets** is now available in Public Beta. This expands our RBAC model beyond account & zone-scoped roles, enabling administrators to grant permissions scoped to individual resources.

#### What's New

  * **[Access Applications ↗︎](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)**: Grant admin permissions to specific Access Applications.
  * **[Identity Providers ↗︎](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)**: Grant admin permissions to individual Identity Providers.
  * **[Targets ↗︎](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target)**: Grant admin rights to specific Targets

![Updated Permissions Policy UX](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3004,height=1410,format=webp/_astro/2025-10-01-fine-grained-permissioning-ux.BWVmQsVF.png)

Note

During the public beta, members must also be assigned an account-scoped, read only role to view resources in the dashboard. This restriction will be lifted in a future release.

  * **Account Read Only** plus a fine-grained permission for a specific App, IdP, or Target
  * **Cloudflare Zero Trust Read Only** plus fine-grained permission for a specific App, IdP, or Target



For more info:

  * [Get started with Cloudflare Permissioning](https://developers.cloudflare.com/fundamentals/manage-members/roles/)
  * [Manage Member Permissioning via the UI & API](https://developers.cloudflare.com/fundamentals/manage-members/manage)


