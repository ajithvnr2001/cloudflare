---
url: https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/
title: Support for CrowdStrike device scores in User Risk Scoring \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.836808+00:00
---

# Support for CrowdStrike device scores in User Risk Scoring · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-1-15-crowdstrike-score/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 15, 2026

## Support for CrowdStrike device scores in User Risk Scoring

[Risk Score](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One has expanded its [User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the [CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).

Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.

New risk behaviors The following risk scoring behaviors are now available:

  * CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a "Low" score from CrowdStrike.
  * CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a "Medium" score from CrowdStrike.



These scores are derived from [CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.
