---
url: https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/
title: IDS logs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:53.697829+00:00
---

# IDS logs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)

  4. /[Logpush integration](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/)
  5. /IDS logs



# IDS logs

Last updated Apr 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ids-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up Logpush for IDSNotes on using Logpush with IDS

You can use Logpush with [Cloudflare Network Firewall IDS](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/) (Intrusion Detection System) to export logs of detected threats. IDS monitors your network traffic for a wide range of known threat signatures, including attacks such as ransomware, data exfiltration, and network scanning.

## Set up Logpush for IDS

  1. Consult the [Logpush Destination docs](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#destination) to learn about what destinations Logpush supports. The documentation will also instruct you on how to correctly format the destination URL for Logpush.

  2. Follow the [Manage Logpush with cURL](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-curl/) tutorial to validate your Logpush destination and define a Logpush job.




## Notes on using Logpush with IDS

  * Magic IDS is an account-scoped dataset. Unlike zone-specific datasets that apply to a single domain, account-scoped datasets use a different API endpoint. Replace the string `/zone/<ZONE_ID>` in the Cloudflare API URLs in the tutorial with `/account/<ACCOUNT_ID>`.

  * Consult the [Magic IDS Detection fields doc](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/magic_ids_detections/) to know what fields you want configured for the job.

  * When creating the Logpush job, the dataset field should equal `magic_ids_detections`.

  * Timestamps default to `unixnano` format (nanoseconds since the Unix epoch, January 1, 1970). If your destination expects a different format (such as RFC 3339), refer to [Logpush Options](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#options) for available timestamp formats. In the Logpush API configuration string, options are appended after the field list.




[PreviousEmail security logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/email-security-logs/)[NextNetwork Firewall log filters](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/network-firewall-log-filters/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/logs/logpush/ids-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
