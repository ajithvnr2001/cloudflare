---
url: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/
title: Scraping detections \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:32.297841+00:00
---

# Scraping detections · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /…

Additional configurations

  4. /[Detection IDs](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/)
  5. /Scraping detections



# Scraping detections

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChallenges for scraping detections

Scraping behavioral detection IDs allow you to better protect your website from volumetric scraping attacks by identifying anomalous behavior. The detection IDs below are specifically designed to catch suspicious scraping activity at the zone level.

Detection ID | Description  
---|---  
`50331648` | Observes patterns of requests sent to your zone, dynamically analyzing behavior by ASN.  
`50331649` | Observes patterns of requests sent to your zone, dynamically analyzing behavior by JA4 fingerprint.  
  
## Challenges for scraping detections

Cloudflare's [Managed Challenge](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge) can limit scraping attacks on your website.

To access scraping detections:

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. Select **Create rule** and choose **Custom rule**.

  3. Fill out the form using **Bot Detection IDs** along with other necessary information.

  4. Select **Save as draft** to return to the rule later, or **Deploy** to deploy the rule.




Rule examplejs
    
    
    (any(cf.bot_management.detection_ids[*] in {50331648 50331649}) and not cf.bot_management.verified_bot)

Best practice

If you are choosing to challenge as your rule action, ensure that you exclude any API calls on which you do not want to issue a challenge. To exclude requests to such paths, edit the [WAF custom rule](https://developers.cloudflare.com/waf/custom-rules/) to exclude the relevant paths.

Note

The matched traffic for detection IDs `50331648` and `50331649` is dynamically re-calculated, meaning a single fingerprint would not be permanently flagged unless it continues to behave suspiciously at all times.

[PreviousAccount takeover detections](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/account-takeover-detections/)[NextAdditional detections](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/additional-detections/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/additional-configurations/detection-ids/scraping-detections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
