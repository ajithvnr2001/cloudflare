---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/
title: Logpush is now available on all plans with usage-based pricing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.110254+00:00
---

# Logpush is now available on all plans with usage-based pricing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-logpush-usage-based-pricing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## Logpush is now available on all plans with usage-based pricing

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush is now available on Free, Pro, Business, and Enterprise plans with usage-based pricing. Free, Pro, and Business customers can enable Logpush through self-service. Enterprise customers continue to work with their account team. Logpush Transformers are also now generally available.

Each account receives included monthly usage before charges apply:

  * **Internal exports** : 25 GB per month, then $0.03 per additional GB.
  * **External exports** : 25 GB per month, then $0.10 per additional GB.
  * **Transformations** : 1 GB per month, then $0.04 per additional GB.



R2 and Pipelines use the internal destination rate. All other destinations use the external destination rate.

Existing Enterprise contracts retain their current Logpush pricing through renewal. Workers Logpush for Workers Trace Events retains request-based pricing, and OpenTelemetry destinations retain event-based Workers Observability pricing.

For complete rates, measurement details, and billing examples, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).
