---
url: https://developers.cloudflare.com/bots/business-insights/
title: Business Insights \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:33.528065+00:00
---

# Business Insights · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/business-insights/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Business Insights



# Business Insights

Last updated Sep 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/business-insights/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityAccessDefinitions Outcome

**Business Insights** helps business decision-makers and content owners analyze bot traffic to their website over the last 24 hours, 7 days, or 30 days.

## Availability

Business Insights is available to all [Enterprise Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/) customers.

Business Insights is an observability surface and does not provide controls. To mitigate bots, use [Security rules](https://developers.cloudflare.com/security/rules/) or the [AI bot management options](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/).

## Access

[ Go to **Business Insights** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/analytics/business-insights)

You can also reach the dashboard from your zone-level **Analytics** > **Business Insights** in the Cloudflare dashboard.

## Definitions

The dashboard uses the following definitions:

  * **Content pages** : Content is initially defined as HTML pages on your website.
  * **Crawl-to-referral ratio, per bot operator** : The average crawl-to-referral ratio (number of crawls sent by this company, vs. the number of visitors who visit you through a referral link from that company, tracked through UTM parameters) for a given company, in the selected time period.
  * **Crawl-to-referral ratio, site-wide** : The average crawl-to-referral ratio (number of crawls sent by this company, vs. the number of visitors who visit you through a referral link from that company, tracked through UTM parameters) across all activity on your zone, in the selected time period.
  * **Classification** : Each crawler is classified with Cloudflare's updated taxonomy. See [Verified bot classifications](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) for more information. If the company has at least 1 bot with an AI use case, we label the operator with the "AI" label, plus provide this as a filter.
  * **Operator** : An operator row aggregates requests from all bots associated with that operator.



### Outcome

**Outcome** summarizes the HTTP responses for requests attributed to an operator.

Outcome | Definition  
---|---  
**Allowed** | All requests received successful HTTP responses (`2xx` or `3xx`).  
**Blocked** | All requests received unsuccessful HTTP responses (status codes other than `2xx` or `3xx`).  
**Partially blocked** | The requests include both successful and unsuccessful HTTP responses.  
  
For a **Partially blocked** row, the Outcome cell shows the successful and unsuccessful request counts.

Outcome is based on HTTP response status and does not identify the mitigation that a website owner configured for a request. Unsuccessful responses can include errors returned by the origin, such as `404` and `5xx` responses. To investigate a request, review its mitigation, edge status code, and origin status code in [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/).

[PreviousBotBase](https://developers.cloudflare.com/bots/botbase/)[NextDelay action](https://developers.cloudflare.com/bots/workers-templates/delay-action/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/business-insights.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
