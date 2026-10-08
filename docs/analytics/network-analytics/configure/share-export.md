---
url: https://developers.cloudflare.com/analytics/network-analytics/configure/share-export/
title: Share and export Network Analytics data \u00b7 Cloudflare Analytics docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:15.852997+00:00
---

# Share and export Network Analytics data · Cloudflare Analytics docs

> Source: https://developers.cloudflare.com/analytics/network-analytics/configure/share-export/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Analytics](https://developers.cloudflare.com/analytics/)
  3. /…

[Network analytics](https://developers.cloudflare.com/analytics/network-analytics/)

  4. /Configure
  5. /Share and export data



# Share and export data

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/analytics/network-analytics/configure/share-export/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewShare Network Analytics filtersExport sample log dataExport a Network Analytics report

## Share Network Analytics filters

When you add filters and specify a time range in Network Analytics, the URL changes to reflect those parameters.

To share your view of the data, copy the URL and send it to other users so that they can work with the same view.

## Export sample log data

You can export up to 100 raw events from the **Packet sample log** at a time. This option is useful when you need to combine and analyze Cloudflare data with data stored in a separate system or database, such as a SIEM system.

To export log data:

  1. Select **Export**.
  2. Choose either CSV or JSON format for rendering exported data. The downloaded file name will reflect the selected time range, using this pattern:


    
    
    network-analytics-attacks-<START_TIME>-<END_TIME>.json

## Export a Network Analytics report

To print or download a snapshot report from Network Analytics, select **Print report**. Your web browser's print interface displays options for printing or saving as a PDF.

[PreviousAdjust the displayed data](https://developers.cloudflare.com/analytics/network-analytics/configure/displayed-data/)[NextData collection](https://developers.cloudflare.com/analytics/network-analytics/reference/data-collection/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/analytics/network-analytics/configure/share-export.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
