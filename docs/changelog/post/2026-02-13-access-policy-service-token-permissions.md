---
url: https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/
title: Fine-grained permissions for Access policies and service tokens \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:36.886206+00:00
---

# Fine-grained permissions for Access policies and service tokens · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 13, 2026

## Fine-grained permissions for Access policies and service tokens

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Fine-grained permissions for **Access policies** and **Access service tokens** are available. These new resource-scoped roles expand the existing RBAC model, enabling administrators to grant permissions scoped to individual resources.

#### New roles

  * **Cloudflare Access policy admin** : Can edit a specific [Access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) in an account.
  * **Cloudflare Access service token admin** : Can edit a specific [Access service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/) in an account.



These roles complement the existing resource-scoped roles for Access applications, identity providers, and infrastructure targets.

For more information:

  * [Resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles)
  * [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/)



Note

Resource-scoped roles is currently in beta.
