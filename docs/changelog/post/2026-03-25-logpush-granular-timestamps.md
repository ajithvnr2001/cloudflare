---
url: https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/
title: Logpush \u2014 More granular timestamps \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:41.582279+00:00
---

# Logpush — More granular timestamps · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-25-logpush-granular-timestamps/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 25, 2026

## Logpush — More granular timestamps

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the [Logpush API](https://developers.cloudflare.com/api/resources/logpush/subresources/jobs/).

To use the new formats, set `timestamp_format` in your Logpush job's `output_options`:

  * `rfc3339ms` — `2024-02-17T23:52:01.123Z`
  * `rfc3339ns` — `2024-02-17T23:52:01.123456789Z`



Default timestamp formats apply unless explicitly set. The dashboard defaults to `rfc3339` and the API defaults to `unixnano`.

For more information, refer to the [Log output options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/) documentation.
