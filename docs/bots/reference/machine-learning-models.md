---
url: https://developers.cloudflare.com/bots/reference/machine-learning-models/
title: Machine Learning models \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:34.516478+00:00
---

# Machine Learning models · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/reference/machine-learning-models/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Reference
  4. /Machine Learning models



# Machine Learning models

Last updated May 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/bots/reference/machine-learning-models/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable auto-updates to the Machine Learning models What will change Risks of not updating Model versions and release notes

## Enable auto-updates to the Machine Learning models

Cloudflare encourages Enterprise customers to enable auto-updates to its Machine Learning models to get the newest bot detection models as they are released.

To enable auto-updates:

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **Bot traffic**.

  3. Go to **Bot Management**.

  4. Under **Configurations** , select the edit icon for **Auto-updates to the Machine Learning Model** and turn it on.




### What will change

If you are on an older Machine Learning model, you will see a score change to requests scored by the **Machine Learning** source instantly. If you are already on the latest model, you will see changes only after a new Machine Learning model becomes the global default.

Customers will be notified via email and dashboard prior to a new Machine Learning model becoming the global default.

### Risks of not updating

By not updating to the latest version, you will be using a Machine Learning model no longer maintained or monitored by our engineering team. As Internet traffic changes and new trends evolve, scoring accuracy by older versions may degrade.

### Model versions and release notes

Version | Release Notes | Launch Date  
---|---|---  
v1 | First Machine Learning Model released. | Q1 2019  
v2 | Introduced dynamic inter-request features to leverage the Cloudflare network to detect new bots more accurately.   
  
Feedback other Bot Management detection mechanisms to the machine learning model to more accurately detect bots. | Q1 2020  
v3 | Fixed accuracy issues under some conditions in the previous version. | Q2 2020  
v4 | Improved scoring for iOS devices.   
  
Fixed scoring inaccuracy in Firefox builds. | Q1 2021  
v5 | Recalibrated model for the [removal of `_cfduid` cookie ↗︎](https://blog.cloudflare.com/deprecating-cfduid-cookie/).   
  
Introduced new signals to reduce false negatives. | Q2 2021  
v6 | Significantly improved scoring for native Android application traffic.   
  
Improved scoring on the newest versions of Chromium browsers. | Q1 2022  
v7 | Increased recognition of distributed botnets.   
  
Improved HTTP/3 scoring. | Q1 2024  
v8 | Improved detection of residential proxies.   
  
Increased weight on network level traffic characteristics. | Q2 2024  
v9 | Improved model consistency and model efficacy against randomization attack techniques | Q2 2025  
  
[PreviousBot Management variables](https://developers.cloudflare.com/bots/reference/bot-management-variables/)[NextBot Detection Alerts](https://developers.cloudflare.com/bots/reference/alerts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/reference/machine-learning-models.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
