---
url: https://developers.cloudflare.com/changelog/post/2025-04-09-secrets-store-beta/
title: Cloudflare Secrets Store now available in Beta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:53.043269+00:00
---

# Cloudflare Secrets Store now available in Beta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-09-secrets-store-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 9, 2025

## Cloudflare Secrets Store now available in Beta

[Secrets Store](https://developers.cloudflare.com/secrets-store/)[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1914,height=1536,format=webp/_astro/secrets-store-landing-page.BQoEWsq8.png)

To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store) or use this Wrangler command:
    
    
    wrangler secrets-store store create <name> --remote

The following are supported in the Secrets Store beta:

  * Secrets Store UI & API: create your store & create, duplicate, update, scope, and delete a secret
  * Workers UI: bind a new or existing account level secret to a Worker and deploy in code
  * Wrangler: create your store & create, duplicate, update, scope, and delete a secret
  * Account Management UI & API: assign Secrets Store permissions roles & view audit logs for actions taken in Secrets Store core platform



For instructions on how to get started, visit our [developer documentation](https://developers.cloudflare.com/secrets-store/).
