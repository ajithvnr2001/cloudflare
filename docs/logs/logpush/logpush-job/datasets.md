---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/
title: Datasets \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.113269+00:00
---

# Datasets · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)

  4. /Logpush job setup
  5. /Datasets



# Datasets

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDatasetsAPIAvailabilityDeprecationRecommendationAdditional resources

## Datasets

The datasets below describe the fields available by log category:

  * [Zone-scoped datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/)
  * [Account-scoped datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/)



## API

The list of fields can also be accessed directly from the API using the following endpoints:

  * For zone-scoped datasets: `https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/datasets/<DATASET>/fields`

  * For account-scoped datasets: `https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/datasets/<DATASET>/fields`




The `<DATASET>` argument indicates the log category. For example, `http_requests`, `spectrum_events`, `firewall_events`, `nel_reports`, or `dns_logs`.

## Availability

  * The availability of Logpush dataset fields depends on your subscription plan.
  * Zone-scoped HTTP requests are available in both Logpush and Logpull.
  * [Custom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/) for HTTP requests are only available in Logpush.
  * All other datasets are only available through Logpush.



## Deprecation

Deprecated fields remain available to prevent breaking existing jobs. They may eventually become empty values if completely removed. Customers are encouraged to migrate away from deprecated fields if they are using them.

## Recommendation

For log field **ClientIPClass** , Cloudflare recommends using [bot tags](https://developers.cloudflare.com/bots/concepts/bot-tags/) to classify IPs.

## Additional resources

For more information on logs available in Cloudflare Zero Trust, refer to [Zero Trust logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/).

[PreviousDedicated Egress IP for Logpush](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/)[NextAccount Abuse Protection Events](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/account_abuse_protection_events/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/datasets/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
