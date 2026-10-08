---
url: https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/
title: Logpush subrequest merging for HTTP requests \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:48.294303+00:00
---

# Logpush subrequest merging for HTTP requests · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 21, 2026

## Logpush subrequest merging for HTTP requests

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-21-logpush-subrequests-merging/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines per visitor request. With subrequest merging enabled, subrequest data is embedded as a nested array field on the parent log record instead.

#### What's new

  * New subrequest_merging field on Logpush jobs — Set "merge_subrequests": true when creating or updating an http_requests Logpush job to enable the feature.
  * New Subrequests log field — When subrequest merging is enabled, a Subrequests field (`array\<object\>`) is added to each parent request log record. Each element in the array contains the standard http_requests fields for that subrequest.



#### Limitations

  * Applies to the http_requests (zone-scoped) dataset only.
  * A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
  * Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
  * Subrequests that do not qualify appear as separate log entries — no data is lost.
  * Subrequest merging is being gradually rolled out and is not yet available on all zones. Contact your account team for concerns or to ensure it is enabled for your zone.
  * For more information, refer to [Subrequests](https://developers.cloudflare.com/logs/logpush/logpush-job/subrequests/).


