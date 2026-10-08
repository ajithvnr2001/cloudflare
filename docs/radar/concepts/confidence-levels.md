---
url: https://developers.cloudflare.com/radar/concepts/confidence-levels/
title: Confidence levels \u00b7 Cloudflare Radar docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:49.584278+00:00
---

# Confidence levels · Cloudflare Radar docs

> Source: https://developers.cloudflare.com/radar/concepts/confidence-levels/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Radar](https://developers.cloudflare.com/radar/)
  3. /[Concepts](https://developers.cloudflare.com/radar/concepts/)
  4. /Confidence levels



# Confidence levels

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/radar/concepts/confidence-levels/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The `result.meta.confidenceInfo.level` in the response provides an indication of how much confidence Cloudflare has in the data. Confidence levels can be affected either by internal issues affecting data quality or by not having a lot of data for a given location (like Antarctica) or Autonomous System (AS).

Level | Description  
---|---  
**1** | There is not enough data in this time range and/or for this location or Autonomous System. Data also exhibits an erratic pattern, possibly due to the reasons previously mentioned.  
**2** | There is not enough data in this timerange and/or in this location or Autonomous System.  
**3** | Data exhibits an erratic pattern but is not affected by known data issues (like pipeline issues).  
**4** | Unassigned.  
**5** | No known data quality issues.  
  
[PreviousBot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/)[NextNormalization methods](https://developers.cloudflare.com/radar/concepts/normalization/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/radar/concepts/confidence-levels.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
