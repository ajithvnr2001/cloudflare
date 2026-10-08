---
url: https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/
title: Threat actor identification with \"also known as\" aliases \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:35.715760+00:00
---

# Threat actor identification with "also known as" aliases · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 3, 2026

## Threat actor identification with "also known as" aliases

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-03-threat-actor-name-mapping/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Identifying threat actors can be challenging, because naming conventions often vary across the security industry. To simplify your research, **Cloudflare Threat Events** now include an **Also known as** field, providing a list of common aliases and industry-standard names for the groups we track.

This new field is available in both the Cloudflare dashboard and via the API. In the dashboard, you can view these aliases by expanding the event details side panel (under the **Attacker** field) or by adding it as a column in your configurable table view.

#### Key benefits

  * Easily map Cloudflare-tracked actors to the naming conventions used by other vendors without manual cross-referencing.
  * Quickly identify if a detected threat actor matches a group your team is already monitoring via other intelligence feeds.



For more information on how to access this data, refer to the [Threat Events API documentation ↗︎](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/).
