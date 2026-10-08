---
url: https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/
title: Workers native integrations were removed from the Cloudflare dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:14.049460+00:00
---

# Workers native integrations were removed from the Cloudflare dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 9, 2025

## Workers native integrations were removed from the Cloudflare dashboard

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-09-workers-integrations-changes/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers native integrations were [originally launched in May 2023 ↗︎](https://blog.cloudflare.com/announcing-database-integrations/) to connect to popular database and observability providers with your Worker in just a few clicks. We are changing how developers connect Workers to these external services. The **Integrations** tab in the dashboard has been removed in favor of a more direct, command-line-based approach using [Wrangler secrets](https://developers.cloudflare.com/workers/wrangler/commands/general/#secret).

#### What's changed

  * **Integrations tab removed** : The integrations setup flow is no longer available in the Workers dashboard.
  * **Manual secret configuration** : New connections should be configured by adding credentials as secrets to your Workers using `npx wrangler secret put` commands.



#### Impact on existing integrations

**Existing integrations will continue to work without any changes required.** If you have integrations that were previously created through the dashboard, they will remain functional.

#### Updating existing integrations

If you'd like to modify your existing integration, you can update the secrets, environment variables, or [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) that were created from the original integration setup.

  * **Update secrets** : Use `npx wrangler secret put <SECRET_NAME>` to update credential values.
  * **Modify environment variables** : Update variables through the dashboard or Wrangler configuration.
  * **Dashboard management** : Access your Worker's settings in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) to modify connections created by our removed native integrations feature.



If you have previously set up an observability integration with [Sentry ↗︎](https://sentry.io), the following environment variables were set and are still modifiable:

  * `BLOCKED_HEADERS`: headers to exclude sending to Sentry
  * `EXCEPTION_SAMPLING_RATE`: number from 0 - 100, where 0 = no events go through to Sentry, and 100 = all events go through to Sentry
  * `STATUS_CODES_TO_SAMPLING_RATES`: a map of status codes -- like 400 or with wildcards like 4xx -- to sampling rates described above



#### Setting up new database and observability connections

For new connections, refer to our step-by-step guides on connecting to popular database and observability providers including: [Sentry](https://developers.cloudflare.com/workers/observability/third-party-integrations/sentry), [Turso](https://developers.cloudflare.com/workers/databases/third-party-integrations/turso/), [Neon](https://developers.cloudflare.com/workers/databases/third-party-integrations/neon/), [Supabase](https://developers.cloudflare.com/workers/databases/third-party-integrations/supabase/), [PlanetScale](https://developers.cloudflare.com/workers/databases/third-party-integrations/planetscale/), [Upstash](https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/), [Xata](https://developers.cloudflare.com/workers/databases/third-party-integrations/xata/).
