---
url: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/additional-detections/
title: Additional detections \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:32.575178+00:00
---

# Additional detections · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/additional-configurations/detection-ids/additional-detections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /…

Additional configurations

  4. /[Detection IDs](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/)
  5. /Additional detections



# Additional detections

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/additional-detections/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare bot detection includes additional signals to catch different kinds of automated traffic.

Bot management customers automatically benefit from the residential proxy detection improvement below, which lowers the [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/) for matched requests. Using the detection ID in [custom rules](https://developers.cloudflare.com/waf/custom-rules/) provides even more visibility and control over mitigating residential proxy traffic.

Detection ID | Description  
---|---  
`50331651` | Observes traffic from residential proxy networks and similar commercial proxies.   
  
When the ID matches a request, Bot Management sets the bot score to 29 and uses [anomaly detection](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/#anomaly-detection-enterprise) as its score source.  
  
[PreviousScraping detections](https://developers.cloudflare.com/bots/additional-configurations/detection-ids/scraping-detections/)[NextJavaScript detections ↗︎](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/additional-configurations/detection-ids/additional-detections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
