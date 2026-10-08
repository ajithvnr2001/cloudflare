---
url: https://developers.cloudflare.com/logs/faq/general-faq/
title: General FAQ \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:09.337078+00:00
---

# General FAQ · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/faq/general-faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /[Faq](https://developers.cloudflare.com/logs/faq/)
  4. /General Faq



# General FAQ

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/faq/general-faq/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Once a request has passed through the Cloudflare network, how soon are the logs available? Are logs available for customers who are not on an Enterprise plan? When pulling or pushing logs, I occasionally come across a time period with no data, even though I am sure my domain received requests at that time. Is this an expected behavior? Can I receive logs in a format other than JSON? Is it possible to track cache purge requests in the logs? At which stage are HTTP requests logged?

[❮ Back to FAQ](https://developers.cloudflare.com/logs/faq/)

### Once a request has passed through the Cloudflare network, how soon are the logs available?

When using **Logpush** , logs are pushed in batches as soon as possible. For example, if you receive a file at 10:10, the file consists of logs that were processed before 10:10.

When using **Logpull** , logs become available in approximately one to five minutes. Cloudflare requires that calls to the **Logpull API** to be for time periods of at least one minute in the past. For example, if it is 9:43 now, you can ask for logs processed between 9:41 and 9:42. The response will include logs for requests that passed through our network between 9:41 and 9:42 and potentially earlier. Usually Cloudflare's processing takes between three and four minutes, so when you ask for that same time period, you may also see logs of requests that passed through our network at 9:39 or earlier.

These timings are only a guideline, not a guarantee, and may depend on network conditions, the request volume for your domain, and other factors. Although we try to get the logs to you as fast as possible, we prioritize not losing log data over speed. On rare occasions, you may experience a longer delay. In this case, you do not need to take any action. The logs will be available as soon as they are processed.

### Are logs available for customers who are not on an Enterprise plan?

Yes. Logpush is available on Free, Pro, Business, and Enterprise plans. Available datasets depend on the products enabled on your account. For more information, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/). The legacy Logpull API remains available only on the Enterprise plan.

### When pulling or pushing logs, I occasionally come across a time period with no data, even though I am sure my domain received requests at that time. Is this an expected behavior?

Yes. The time period for which you pull or receive logs is based on our processing time, not the time the requests passed through our network. Empty responses do not mean there were no requests during that time period, just that we did not process any logs for your domain during that time.

### Can I receive logs in a format other than JSON?

Not at this time. Talk to your Cloudflare account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/) if you are interested in other formats and we will consider them for the future.

### Is it possible to track cache purge requests in the logs?

Yes, since Nov 25, 2025 [Audit Log v2](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

### At which stage are HTTP requests logged?

Requests are logged only after they successfully reach our proxy. It means that requests failing during the TCP or TLS handshake between the client and the Cloudflare proxy will not be available in the logs.

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/faq/general-faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
