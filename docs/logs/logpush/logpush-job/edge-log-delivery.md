---
url: https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/
title: Edge Log Delivery \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:14.833092+00:00
---

# Edge Log Delivery · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)

  4. /Logpush job setup
  5. /Edge Log Delivery



# Edge Log Delivery

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Edge Log Delivery allows customers to send logs directly from Cloudflare’s edge to their destination of choice. You can configure the maximum interval for your log batches between 30 seconds and five minutes. However, you cannot specify a minimum interval for log batches, meaning that log files may be sent in shorter intervals than the maximum specified. Compared to Logpush, Edge Log Delivery sends logs with lower latency, more frequently, and in smaller batches.

Edge Log Delivery is only available for HTTP request logs. Refer to the [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#kind) page for steps on how to configure a job to use Edge Log Delivery.

[PreviousLog Output Options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/)[NextCustom fields](https://developers.cloudflare.com/logs/logpush/logpush-job/custom-fields/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/logpush-job/edge-log-delivery.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
