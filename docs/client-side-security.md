---
url: https://developers.cloudflare.com/client-side-security/
title: Overview \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:56.939757+00:00
---

# Overview · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/

  1. [Home](https://developers.cloudflare.com/)
  2. /Client-side security



# Client-side security

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFeaturesAvailability

Ensures the safety and privacy of your website visitors' browsing environment.

Available on all plans

Websites load third-party scripts for analytics, ads, chat widgets, and payment forms. If an attacker compromises one of these scripts, they can steal visitor data directly from the browser, an attack known as a [client-side supply chain attack ↗︎](https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/). Client-side security (formerly Page Shield) gives you visibility into these resources and alerts you when something changes or looks malicious.

Client-side security monitors scripts, connections, and cookies loaded by your website visitors. You can set up alert notifications and create content security rules to control which resources are allowed on your pages.

Learn how to [get started](https://developers.cloudflare.com/client-side-security/get-started/).

* * *

## Features

[Resource monitoring](https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/)

Displays information about client-side resources loaded in your domain's pages.

Monitor client-side resources

[Page attribution](https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/#view-details)

Find in which page a resource first appeared, and view a list of the latest occurrences of the resource in your pages.

Find resource occurrences

[Malicious script detection](https://developers.cloudflare.com/client-side-security/detection/review-malicious-scripts/)

Detects malicious scripts in your pages using threat intelligence and machine learning.

Review malicious scripts

[Code change detection](https://developers.cloudflare.com/client-side-security/detection/review-changed-scripts/)

Detects any changes in the scripts loaded in your pages.

Review changed scripts

[Alerts](https://developers.cloudflare.com/client-side-security/alerts/)

Receive notifications about newly detected scripts, scripts loaded from unknown domains, new scripts considered malicious, or code changes in your existing scripts.

Use Alerts

[Content security rules](https://developers.cloudflare.com/client-side-security/rules/)

Content security rules define allowed resources on your websites. Use content security rules to enforce an allowlist of resources, effectively blocking resources not included in your rules.

Use Content security rules

## Availability

| Free | Pro | Business | Enterprise | Advanced  
---|---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes | Yes  
Script monitoring | Yes | Yes | Yes | Yes | Yes  
Connection monitoring | No | No | Yes | Yes | Yes  
Cookie monitoring | No | No | Yes | Yes | Yes  
Page attribution | No | No | Yes | Yes | Yes  
New Resources Alerts and New Domain Alerts | No | No | Yes | Yes | Yes  
Malicious script detection and alerting | No | No | No | No | Yes  
Code change detection and alerting | No | No | No | No | Yes  
Malicious connection detection and alerting | No | No | No | No | Yes  
Cookie monitoring advanced fields | No | No | No | No | Yes  
Number of content security rules (positive blocking) | 0 | 0 | 0 | 0 | 5  
Number of Logpush jobs | 0 | 0 | 0 | 0 | 4  
  
The Page Shield add-on is now Client-Side Security Advanced. The features and entitlements are unchanged.

[NextGet started](https://developers.cloudflare.com/client-side-security/get-started/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
