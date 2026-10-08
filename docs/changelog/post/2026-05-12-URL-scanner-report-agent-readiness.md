---
url: https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/
title: Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:52.734410+00:00
---

# Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 12, 2026

## Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve added a new **Agent Readiness** tab to URL Scanner reports accessible via the Cloudflare dashboard. This feature evaluates your site against emerging AI standards and provides six specialized scores to help you optimize for the next generation of AI agents and automated discovery.

The Internet is shifting from a human-read web to a machine-read web. AI agents now browse, interact with, and even perform transactions on websites. If a site isn't "agent-ready," these bots may consume excessive bandwidth, fail to find critical information, or be unable to navigate your services efficiently.

This update provides material value by breaking down readiness into six actionable categories:

  * **Basic Web Presence**
  * **Discoverability**
  * **Content Accessibility**
  * **Bot Access Control**
  * **Protocol Discovery**
  * **Commerce**



#### Accessing the report

You can view these scores for any scanned URL directly in the dashboard or via our API.

  * **Dashboard:** Go to **Protect & Connect > Application Security > Investigate**. After running a scan, select the **Agent Readiness** tab in the report.
  * **API:** Use the [URL Scanner API ↗︎](https://developers.cloudflare.com/radar/investigate/url-scanner/) to programmatically retrieve these scores for your infrastructure.



To learn more about the methodology behind these scores, refer to the [blogpost ↗︎](https://blog.cloudflare.com/agent-readiness/).
