---
url: https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/
title: Risk score Changelog \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:28.171444+00:00
---

# Risk score Changelog · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Changelog](https://developers.cloudflare.com/cloudflare-one/changelog/)
  4. /Risk score



# Risk score

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/changelog/risk-score/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview2024-06-14

[Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/risk-score.xml)

## 2026-04-08

  
**User risk scoring for high risk browsing activity**  


Cloudflare One's **User Risk Scoring** now incorporates direct signals from **Gateway DNS traffic patterns**. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.

#### Why this matters

Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:

  * **Security threats** : Domains associated with malware, phishing, or command-and-control (C2) centers.
  * **High-risk content** : Categories such as questionable content or violence that may violate corporate compliance.



Even if a Gateway policy is set to **Block** the traffic, the interaction is still captured as a "hit" to ensure the user's risk profile reflects the attempted activity.

#### New risk behaviors

Two new behaviors are now available in the dashboard:

  * **Suspicious Security Domain Visited** : Triggers when a user visits a domain in the security threats or security risk categories.
  * **High risk domain visited** : Triggers when a user visits domains categorized as questionable content, violence, or CIPA.



To learn more and get started, refer to the [User Risk Scoring documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/).

## 2026-01-15

  
**Support for CrowdStrike device scores in User Risk Scoring**  


Cloudflare One has expanded its [User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the [CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).

Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.

New risk behaviors The following risk scoring behaviors are now available:

  * CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a "Low" score from CrowdStrike.
  * CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a "Medium" score from CrowdStrike.



These scores are derived from [CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.

## 2024-06-17

  
**Exchange user risk scores with Okta**  


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



## 2024-06-14

**SentinelOne signal ingestion**

You can now configure a [predefined risk behavior](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#predefined-risk-behaviors) to evaluate user risk score using device posture attributes from the [SentinelOne integration](https://developers.cloudflare.com/cloudflare-one/integrations/service-providers/sentinelone/).

[PreviousGateway](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/)[NextReference architecture ↗︎](https://developers.cloudflare.com/reference-architecture/architectures/sase/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/changelog/risk-score.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
