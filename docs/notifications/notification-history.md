---
url: https://developers.cloudflare.com/notifications/notification-history/
title: Alert history \u00b7 Cloudflare Notifications docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:25.754277+00:00
---

# Alert history · Cloudflare Notifications docs

> Source: https://developers.cloudflare.com/notifications/notification-history/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Notifications](https://developers.cloudflare.com/notifications/)
  3. /Alert history



# Alert history

Last updated Oct 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/notifications/notification-history/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAccess alert historyAvailability

Alert history is a log of alerts that have been sent to your account. Each record includes the alert itself, when it was sent, and who it was delivered to.

## Access alert history

You can access alert history [via the Cloudflare API](https://developers.cloudflare.com/api/resources/alerting/subresources/history/methods/list/). Use `GET` to retrieve history records for alerts sent to an account. Records are available for the last 30 or 90 days depending on your plan.

Syntaxtxt
    
    
    GET accounts/{account_id}/alerting/v3/history

Examplebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/alerting/v3/history?page=1&per_page=25" \
    --header "Authorization: Bearer <API_TOKEN>"

## Availability

Alert history is available on all plans. Retention depends on your plan:

  * **Free, Pro, and Business** : 30 days.
  * **Enterprise** : 90 days.



Note

Alert history is not available for events before 2021-10-11.

[PreviousAvailable alerts](https://developers.cloudflare.com/notifications/notification-available/)[NextHTTP Traffic Alerts](https://developers.cloudflare.com/notifications/reference/traffic-alerts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/notifications/notification-history.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
