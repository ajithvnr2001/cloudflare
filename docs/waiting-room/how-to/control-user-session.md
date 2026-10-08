---
url: https://developers.cloudflare.com/waiting-room/how-to/control-user-session/
title: Control user session settings \u00b7 Cloudflare Waiting Room docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:50.560071+00:00
---

# Control user session settings · Cloudflare Waiting Room docs

> Source: https://developers.cloudflare.com/waiting-room/how-to/control-user-session/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Waiting Room](https://developers.cloudflare.com/waiting-room/)
  3. /How to
  4. /Control user session settings



# Control user session settings

Last updated Jun 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waiting-room/how-to/control-user-session/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSession durationDisable session renewal to limit browsing timeRevoke a user’s session using origin commands

Adjust these settings to control how long a user can hold their place on your site after leaving the waiting room.

## Session duration

Once on your site, a user is considered active as long as they make an HTTP request to any URL covered by your waiting room once every **session duration** minutes. Each new request restarts a user’s time to stay active equal to **session duration**.

## Disable session renewal to limit browsing time

You can limit each user’s time on your site to only one session duration by checking the box next to Disable Session Renewal from the dashboard. Once a user has been active on your site for **session duration** minutes, if there is active queueing, that user will be sent to the back of the queue. If there is not an active queue when **session duration** minutes is over, this user will be given a new waiting room cookie and counted as a new user again.

## Revoke a user’s session using origin commands

To terminate a user's session when they perform a specific action, you can send a command to the waiting room using an HTTP header on the response from your origin. This command tells the waiting room to revoke the session of the user associated with the current response. This allows spots to open up more dynamically and may increase throughput from your queue.

To enable this feature in the Cloudflare Dashboard, check the box next to Allow session termination via origin commands from the dashboard. To enable this feature through the [Cloudflare API](https://developers.cloudflare.com/api/resources/waiting_rooms/methods/update/), update the `enabled_origin_commands` property to include the value `”revoke”` in the list of enabled origin commands.

Then, to return a revocation origin command and revoke the user's session associated with the current request, add the `Cf-Waiting-Room-Command: revoke` HTTP header to the response from your origin.

To get the number of sessions revoked, you can query `sessionsRevoked` metrics from your [Waiting Room analytics](https://developers.cloudflare.com/waiting-room/waiting-room-analytics/#graphql-analytics) data via GraphQL API.

[PreviousMonitor waiting room status](https://developers.cloudflare.com/waiting-room/how-to/monitor-waiting-room/)[NextControl waiting room traffic](https://developers.cloudflare.com/waiting-room/how-to/control-waiting-room/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waiting-room/how-to/control-user-session.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
