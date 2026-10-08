---
url: https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/
title: Deprecate legacy Workers KV namespace API routes \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:03.321594+00:00
---

# Deprecate legacy Workers KV namespace API routes · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)July 15, 2026

## Deprecate legacy Workers KV namespace API routes

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The legacy Workers KV API routes under `/accounts/{account_id}/workers/namespaces/*` are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented [Workers KV API](https://developers.cloudflare.com/api/resources/kv/) routes under `/accounts/{account_id}/storage/kv/namespaces/*` before that date.

The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from `/workers/namespaces/` to `/storage/kv/namespaces/`.

#### What you need to do

Update any integration that calls a route under `/accounts/{account_id}/workers/namespaces/` to use the equivalent route under `/accounts/{account_id}/storage/kv/namespaces/`. The migration is a direct URL path substitution — request parameters and response payloads are identical:

  * `GET` and `POST /accounts/{account_id}/workers/namespaces` → `GET` and `POST /accounts/{account_id}/storage/kv/namespaces`
  * `GET`, `PUT`, and `DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}` → `GET`, `PUT`, and `DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}`
  * `GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys` → `GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys`
  * `GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}` → `GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}`
  * `GET`, `PUT`, and `DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}` → `GET`, `PUT`, and `DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}`



For more information about the deprecation timeline, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).
