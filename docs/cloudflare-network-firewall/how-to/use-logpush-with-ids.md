---
url: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/
title: Use Logpush with IDS \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:07.661263+00:00
---

# Use Logpush with IDS · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /How to
  4. /Use Logpush with IDS



# Use Logpush with IDS

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/use-logpush-with-ids/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewNotes on using Logpush with IDS

You can use Logpush with Cloudflare Network Firewall (formerly Magic Firewall) IDS to log detected risks:

  1. Consult the [Logpush Destination docs](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#destination) to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.

  2. Follow the [Manage Lopush with cURL](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-curl/) tutorial to validate your Logpush destination and define a Logpush job.




## Notes on using Logpush with IDS

  * Magic IDS is an account-scoped dataset. This means the string `/zone/<ZONE_ID>` in the Cloudflare API URLs in the tutorial should be replaced with `/account/<ACCOUNT_ID>`.

  * Consult the [Magic IDS Detection fields doc](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/) to know what fields you want configured for the job.

  * When creating the Logpush job, the dataset field should equal `magic_ids_detections`.

  * Timestamps by default are unixnano. Consult the [Logpush Options docs](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#options) to learn what format you can choose that will be compatible with your destination and/or expectations. Note that all options must be added _after_ all fields you want from the Logpush job, akin to URL parameters.




[PreviousFilter different views](https://developers.cloudflare.com/cloudflare-network-firewall/how-to/filter-views/)[NextOverview](https://developers.cloudflare.com/cloudflare-network-firewall/packet-captures/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/how-to/use-logpush-with-ids.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
