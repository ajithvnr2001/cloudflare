---
url: https://developers.cloudflare.com/bots/botbase/
title: BotBase \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:27.895507+00:00
---

# BotBase · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/botbase/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /BotBase



# BotBase

Last updated Oct 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityAccessWhat you can doRequestsClassificationRadar's public-facing BotBase

BotBase is Cloudflare's directory of all known bots, including [verified bots and agents](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/). It provides a comprehensive, searchable view of the entire bot directory directly in the Cloudflare dashboard, where you can see how Cloudflare classifies each bot and target individual bots in your security configuration.

BotBase currently serves as a visibility plane for tracked bots. To mitigate these bots, you can use [Security rules](https://developers.cloudflare.com/security/rules/) or the [AI traffic options](https://developers.cloudflare.com/bots/concepts/bot/#ai-bots).

## Availability

BotBase is available to [Enterprise Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/) customers.

## Access

To view BotBase, go to **Security Analytics** > **Bot analysis** > **BotBase**. You can also access BotBase from **Security Settings** > **Bot Management** > **BotBase**.

## What you can do

  * Browse the full catalogue of all verified bots and agents, and see the behavior or behaviors each one is classified under.
  * Search and filter the directory to find a specific bot or group of bots.
  * Filter your own traffic to a specific bot to investigate its activity on your zone.
  * Copy a bot's detection ID to target it in [Security rules](https://developers.cloudflare.com/security/rules/).
  * If you operate a bot, submit it for verification from the **Submission form** tab and track its review status from the **Submission history** tab. For more information, refer to [Becoming a Verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/#becoming-a-verified-bot).



## Requests

The **Requests** column summarizes requests associated with each bot over the previous 24 hours and shows an hourly sparkline.

Metric | Definition  
---|---  
**Successful** | Requests with an edge HTTP response status in the `2xx` or `3xx` range.  
**Unsuccessful** | Requests with any other edge HTTP response status.  
  
These metrics describe HTTP response outcomes, not the mitigation that a website owner configured for a request. Unsuccessful requests can include errors returned by the origin, such as `404` and `5xx` responses.

To investigate a bot's traffic, select its row to open Security Analytics in a new tab filtered to that bot's detection ID. Expand a request in the request log to review the **Mitigation** , **Edge status code** , and **Origin status code** fields.

## Classification

BotBase classifies each tracked bot by its behavior — what the bot may do on your site. A single bot can have one or more behaviors. To read more, see [Verified bot classifications](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/).

## Radar's public-facing BotBase

Every bot tracked in BotBase, along with select metadata, is available publicly in [Cloudflare Radar's bots and agents directory ↗︎](https://radar.cloudflare.com/bots/directory).

[PreviousBot Analytics](https://developers.cloudflare.com/bots/bot-analytics/)[NextBusiness Insights](https://developers.cloudflare.com/bots/business-insights/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/botbase.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
