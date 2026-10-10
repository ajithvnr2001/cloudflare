---
url: https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/
title: Run more headless browsers concurrently with Browser Run \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:32.589158+00:00
---

# Run more headless browsers concurrently with Browser Run · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-20-limits-increase/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 20, 2026

## Run more headless browsers concurrently with Browser Run

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) lets you automate headless browsers on Cloudflare's global network. Run full browser sessions for interactive workflows, or use [Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) for one-request tasks such as screenshots, PDFs, and capturing page content.

If you are on the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/), your default [limits](https://developers.cloudflare.com/browser-run/limits/#workers-paid) are now higher:

Limit | Previous | New  
---|---|---  
Concurrent browsers | 120 | **200**  
New browser instances / second | 1 | **3**  
Quick Actions requests / second | 10 | **30**  
  
You can now run hundreds of browser sessions in parallel, launch new browsers faster, and process three times as many [Quick Actions](https://developers.cloudflare.com/browser-run/quick-actions/) per second. These published limits are defaults, not maximums. If your workload needs more more concurrent browsers, [request higher limits ↗︎](https://forms.gle/CdueDKvb26mTaepa9).
