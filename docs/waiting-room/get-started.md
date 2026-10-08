---
url: https://developers.cloudflare.com/waiting-room/get-started/
title: Get started \u00b7 Cloudflare Waiting Room docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:49.963279+00:00
---

# Get started · Cloudflare Waiting Room docs

> Source: https://developers.cloudflare.com/waiting-room/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Waiting Room](https://developers.cloudflare.com/waiting-room/)
  3. /Get started



# Get started

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waiting-room/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginStep 1 — Plan out your waiting room Location Access method Queue activationStep 2 — Create your waiting room Appearance (optional) Prepare your waiting room for mobile application trafficStep 3 — Activate your waiting room Queue some visitors Queue all visitorsStep 4 — Next steps

* * *

## Before you begin

Before you start this tutorial, make sure you have:

  * Reviewed the [About](https://developers.cloudflare.com/waiting-room/about/) Waiting Room page.).
  * Reviewed your [rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/) to make sure they allow at least one request every 20 seconds (required for automatic page refreshes).



* * *

## Step 1 — Plan out your waiting room

Before you create your waiting room, think about how you want it to appear and operate.

### Location

Which page will you cover with a waiting room? You can only have one waiting room per page, so you need to identify the high-traffic areas of your website.

Specify the URL for your page by setting the `hostname` and `path` in your [configuration settings](https://developers.cloudflare.com/waiting-room/reference/configuration-settings/).

Advanced Waiting Room customers can also [specify multiple hostname and path combinations](https://developers.cloudflare.com/waiting-room/how-to/place-waiting-room/) for the same zone.

### Access method

You can direct visitors to your high-traffic page:

  * Directly (via URL)
  * Indirectly (via [a redirect](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/))



### Queue activation

When you activate your waiting room, choose whether:

  * **All visitors** to be queued, in preparation for a product release or other time-based event.
  * Only **some visitors** to be queued, as traffic reaches the thresholds defined in `Total active users` and `New users per minute`.



## Step 2 — Create your waiting room

Create your waiting room by:

  * Using the [dashboard](https://developers.cloudflare.com/waiting-room/how-to/create-waiting-room/).
  * Using the [API](https://developers.cloudflare.com/waiting-room/how-to/create-waiting-room/).



### Appearance (optional)

Some customers can [customize the design](https://developers.cloudflare.com/waiting-room/how-to/customize-waiting-room/) of their waiting room by editing the page's HTML and CSS.

If you have this ability, think about how you want the page to appear.

### Prepare your waiting room for mobile application traffic

If you need to manage traffic in a non-browser environment such as a mobile app or web app, use a [JSON-friendly waiting room](https://developers.cloudflare.com/waiting-room/how-to/json-response/) that can be consumed via your API endpoints. Note that if you have a mobile app or web app that depends on resources that would be protected by a waiting room, you will need to update those clients to handle Waiting Room appropriately.

## Step 3 — Activate your waiting room

Depending on your queue activation, you may deploy your waiting room differently.

### Queue some visitors

To queue visitors only when necessary:

  1. Go to **Traffic** > **Waiting Room**.
  2. On a waiting room, set **Enabled** to **On**.
  3. Your waiting room will begin queueing visitors once it approaches the target traffic thresholds defined in [**Total active users**](https://developers.cloudflare.com/waiting-room/reference/configuration-settings/) and in [**New users per minute**](https://developers.cloudflare.com/waiting-room/reference/configuration-settings/).



### Queue all visitors

To queue all visitors prior to a time-based offering, set up a pre-queue as part of a [waiting room event](https://developers.cloudflare.com/waiting-room/additional-options/create-events/#create-an-event-from-the-dashboard).

To start queueing all new visitors without a scheduled event:

  1. Go to **Traffic** > **Waiting Room**.
  2. On a waiting room: 
     1. Ensure **Enabled** is set to **On**.
     2. Set **Queue-all** to **On**.
  3. Your waiting room will begin queueing all new visitors and will not allow any new visitors to the path protected by your waiting room. Queue-all will override all other waiting room settings, including event settings.



Note

Only new visitors will be queued. Active users that are already on your website will continue there and will not return to the queue until their session expires.

  4. To begin allowing visitors to the path protected by your waiting room, set **Queue-all** to **Off**.



## Step 4 — Next steps

After you have created and deployed your first waiting room, you might also want to:

  * [Test your waiting room](https://developers.cloudflare.com/waiting-room/additional-options/test-waiting-room/) before it goes live.
  * [Monitor your traffic](https://developers.cloudflare.com/waiting-room/how-to/monitor-waiting-room/) in real time.
  * [Troubleshoot](https://developers.cloudflare.com/waiting-room/troubleshooting/) potential issues.



[PreviousAbout](https://developers.cloudflare.com/waiting-room/about/)[NextPlans](https://developers.cloudflare.com/waiting-room/plans/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waiting-room/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
