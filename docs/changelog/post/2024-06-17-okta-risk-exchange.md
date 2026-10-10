---
url: https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/
title: Exchange user risk scores with Okta \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:56.064005+00:00
---

# Exchange user risk scores with Okta · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 17, 2024

## Exchange user risk scores with Okta

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Beyond the controls in [Zero Trust](https://developers.cloudflare.com/cloudflare-one/), you can now [exchange user risk scores](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta) with Okta to inform SSO-level policies.

First, configure Cloudflare One to send user risk scores to Okta.

  1. Set up the [Okta SSO integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/).
  2. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.
  3. In **Your identity providers** , locate your Okta integration and select **Edit**.
  4. Turn on **Send risk score to Okta**.
  5. Select **Save**.
  6. Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.



Next, configure Okta to receive your risk scores.

  1. On your Okta admin dashboard, go to **Security** > **Device Integrations**.
  2. Go to **Receive shared signals** , then select **Create stream**.
  3. Name your integration. In **Set up integration with** , choose _Well-known URL_.
  4. In **Well-known URL** , enter the well-known URL value provided by Cloudflare One.
  5. Select **Create**.


