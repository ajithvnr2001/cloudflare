---
url: https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/
title: User risk scoring for high risk browsing activity \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:40.858079+00:00
---

# User risk scoring for high risk browsing activity · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-04-08-high-risk-browsing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 8, 2026

## User risk scoring for high risk browsing activity

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

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
