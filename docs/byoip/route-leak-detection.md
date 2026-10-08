---
url: https://developers.cloudflare.com/byoip/route-leak-detection/
title: Route Leak Detection \u00b7 Cloudflare BYOIP docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:40.234158+00:00
---

# Route Leak Detection · Cloudflare BYOIP docs

> Source: https://developers.cloudflare.com/byoip/route-leak-detection/

  1. [Home](https://developers.cloudflare.com/)
  2. /[BYOIP](https://developers.cloudflare.com/byoip/)
  3. /Route Leak Detection



# Route Leak Detection

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/byoip/route-leak-detection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable Route Leak Detection

Route Leak Detection protects your routes on the Internet by notifying you when your traffic is routed somewhere it should not go, which could indicate a possible attack. Route Leak Detection also reduces the amount of time needed to mitigate leaks by providing you with timely notifications.

Cloudflare detects route leaks by using several sources of routing data to create a synthesis of how the Internet sees routes to BYOIP users. Cloudflare then watches these views to track any sudden changes that occur on the Internet. If the changes can be correlated to actions Cloudflare has taken, no further action is required. However, if changes have not been made, Cloudflare notifies you to inform you that your routes and users may be at risk.

## Enable Route Leak Detection

Route Leak Detection Alert

**Who is it for?**

[BYOIP customers](https://developers.cloudflare.com/byoip/) who want to receive a notification when their prefixes are advertised in places they should not be.

**Other options / filters**

None.

**Included with**

Purchase of BYOIP.

**What should you do if you receive one?**

Confirm your traffic is healthy. Reach out to your transit providers to ensure you are behaving as expected and ask them to follow up with any providers accepting the unauthorized routes.

You must be a user who has brought your own IP address to Cloudflare, which includes Magic Transit, Spectrum, and WAF users. Only prefixes advertised by Cloudflare qualify for Route Leak Detection.

  1. In the Cloudflare dashboard, go to the **Notifications** page.

[ Go to **Notifications** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)
  2. Select **Add**.

  3. Locate **Route Leak Detection** from the list > **Select**.

  4. Enter a name and description for the notification.

  5. Enter one or more email addresses to receive the notifications.

  6. Select **Save**.




[PreviousCDN and Spectrum](https://developers.cloudflare.com/byoip/service-bindings/cdn-and-spectrum/)[NextGeneral](https://developers.cloudflare.com/byoip/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/byoip/route-leak-detection.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
