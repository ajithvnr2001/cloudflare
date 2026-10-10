---
url: https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/
title: MRT Explorer on Cloudflare Radar \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:38.017113+00:00
---

# MRT Explorer on Cloudflare Radar · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-05-19-radar-mrt-explorer/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)May 19, 2026

## MRT Explorer on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes an [MRT Explorer ↗︎](https://radar.cloudflare.com/routing/mrt-explorer) tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.

#### Loading a file

Paste a URL to fetch an MRT file remotely, drag and drop one onto the page, or browse for a local file. Gzip and bzip2 compressed files are supported. A sample file is also available to get started right away.

![Screenshot of the MRT Explorer file input form](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2428,height=898,format=webp/_astro/mrt-explorer-form.DKnzUqMC.png)

#### Inspecting events

Once parsed, the tool lists every BGP event with its timestamp, prefix, AS path, OTC (Only to Customer), and community attributes.

![Screenshot of the MRT Explorer event list](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2410,height=1536,format=webp/_astro/mrt-explorer-list.8fq2u5Kc.png)

#### Event details

Clicking on the "View details" action opens a modal with additional properties and the full event JSON.

![Screenshot of the MRT Explorer event details modal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1694,height=1890,format=webp/_astro/mrt-explorer-details.EMcHevWw.png)

#### Shareable URLs

When loading a file by URL, the query string captures the source so the link can be shared directly — the recipient's browser immediately fetches and parses the same file.

Try the [MRT Explorer on Cloudflare Radar ↗︎](https://radar.cloudflare.com/routing/mrt-explorer).
