---
url: https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/
title: Applications to be remapped to the new categories \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:28.397585+00:00
---

# Applications to be remapped to the new categories · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 6, 2025

## Applications to be remapped to the new categories

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-06-Applications-recategorised-plan/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We have previously added new application categories to better reflect their content and improve HTTP traffic management: refer to [Changelog](https://developers.cloudflare.com/cloudflare-one/changelog/gateway/#2025-10-28). While the new categories are live now, we want to ensure you have ample time to review and adjust any existing rules you have configured against old categories. The remapping of existing applications into these new categories will be completed by January 30, 2026. This timeline allows you a dedicated period to:

  * Review the new category structure.
  * Identify any policies you have that target the older categories.
  * Adjust your rules to reference the new, more precise categories before the old mappings change. Once the applications have been fully remapped by January 30, 2026, you might observe some changes in the traffic being mitigated or allowed by your existing policies. We encourage you to use the intervening time to prepare for a smooth transition.



**Applications being remappedd**

Application Name | Existing Category | New Category  
---|---|---  
Google Photos | File Sharing | Photography & Graphic Design  
Flickr | File Sharing | Photography & Graphic Design  
ADP | Human Resources | Business  
Greenhouse | Human Resources | Business  
myCigna | Human Resources | Health & Fitness  
UnitedHealthcare | Human Resources | Health & Fitness  
ZipRecruiter | Human Resources | Business  
Amazon Business | Human Resources | Business  
Jobcenter | Human Resources | Business  
Jobsuche | Human Resources | Business  
Zenjob | Human Resources | Business  
DocuSign | Legal | Business  
Postident | Legal | Business  
Adobe Creative Cloud | Productivity | Photography & Graphic Design  
Airtable | Productivity | Development  
Autodesk Fusion360 | Productivity | IT Management  
Coursera | Productivity | Education  
Microsoft Power BI | Productivity | Business  
Tableau | Productivity | Business  
Duolingo | Productivity | Education  
Adobe Reader | Productivity | Business  
AnpiReport | Productivity | Travel  
ビズリーチ | Productivity | Business  
doda (デューダ) | Productivity | Business  
求人ボックス | Productivity | Business  
マイナビ2026 | Productivity | Business  
Power Apps | Productivity | Business  
RECRUIT AGENT | Productivity | Business  
シフトボード | Productivity | Business  
スタンバイ | Productivity | Business  
Doctolib | Productivity | Health & Fitness  
Miro | Productivity | Photography & Graphic Design  
MyFitnessPal | Productivity | Health & Fitness  
Sentry Mobile | Productivity | Travel  
Slido | Productivity | Photography & Graphic Design  
Arista Networks | Productivity | IT Management  
Atlassian | Productivity | Business  
CoderPad | Productivity | Business  
eAgreements | Productivity | Business  
Vmware | Productivity | IT Management  
Vmware Vcenter | Productivity | IT Management  
AWS Skill Builder | Productivity | Education  
Microsoft Office 365 (GCC) | Productivity | Business  
Microsoft Exchange Online (GCC) | Productivity | Business  
Canva | Sales & Marketing | Photography & Graphic Design  
Instacart | Shopping | Food & Drink  
Wawa | Shopping | Food & Drink  
McDonald's | Shopping | Food & Drink  
Vrbo | Shopping | Travel  
American Airlines | Shopping | Travel  
Booking.com | Shopping | Travel  
Ticketmaster | Shopping | Entertainment & Events  
Airbnb | Shopping | Travel  
DoorDash | Shopping | Food & Drink  
Expedia | Shopping | Travel  
EasyPark | Shopping | Travel  
UEFA Tickets | Shopping | Entertainment & Events  
DHL Express | Shopping | Business  
UPS | Shopping | Business  
  
For more information on creating HTTP policies, refer to [Applications and app types](https://developers.cloudflare.com/cloudflare-one/traffic-policies/application-app-types/).
