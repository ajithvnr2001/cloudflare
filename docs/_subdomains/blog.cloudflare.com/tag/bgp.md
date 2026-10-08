---
url: https://blog.cloudflare.com/tag/bgp/
title: Posts tagged \"BGP\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:22.672423+00:00
---

# Posts tagged "BGP" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/bgp/

TAG

# BGP

[Subscribe to BGP RSS feed](https://blog.cloudflare.com/tag/bgp/rss)

August 18, 2026## [BGP Role model: tracking the adoption of RFC 9234](https://blog.cloudflare.com/rfc9234-bgp-role-model/)

RFC 9234 lets routers reject route leaks on their own, using BGP Roles and the Only to Customer attribute. We measured who has deployed it, and found two Tier 1 networks unexpectedly stripping OTC.

![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Iliana Xygkou](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAGC1W8ZPJBM3V4CJ2523N8.png&w=64&h=64&f=webp&fit=cover&position=center)![Mingwei Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ER28A8EPWVBKJWBWZ58R.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Bryton Herdes](https://blog.cloudflare.com/author/bryton/), [Iliana Xygkou](https://blog.cloudflare.com/author/iliana-xygkou/), and [Mingwei Zhang](https://blog.cloudflare.com/author/mingwei/)

July 24, 2026## [BGP ORIGIN attribute manipulation and its impact on the Internet](https://blog.cloudflare.com/bgp-origin-attribute/)

By doing in-depth testing, we found nearly 70% of BGP paths experience ORIGIN attribute rewrites by transit providers seeking traffic advantages. We examine the global impact of this practice and argue for deprecating ORIGIN in route selection.

![Iliana Xygkou](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAGC1W8ZPJBM3V4CJ2523N8.png&w=64&h=64&f=webp&fit=cover&position=center)![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Iliana Xygkou](https://blog.cloudflare.com/author/iliana-xygkou/) and [Bryton Herdes](https://blog.cloudflare.com/author/bryton/)

June 3, 2026## [Enforcing the First AS in BGP AS_PATHs](https://blog.cloudflare.com/enforce-first-as-bgp/)

BGP is vulnerable to routing hijacks and path leaks that negatively impact traffic on the Internet. RPKI helps solve some of these problems, but for some forged paths, we need to rely on a simpler mechanism: First AS enforcement in BGP.

![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bryce Walters](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48XA2YEPHMWWS0YSZNE4DT.webp&w=64&h=64&f=webp&fit=cover&position=center)![Mingwei Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ER28A8EPWVBKJWBWZ58R.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Bryton Herdes](https://blog.cloudflare.com/author/bryton/), [Bryce Walters](https://blog.cloudflare.com/author/bryce-walters/), and [Mingwei Zhang](https://blog.cloudflare.com/author/mingwei/)

April 28, 2026## [Shutdowns, power outages, and conflict: a review of Q1 2026 Internet disruptions](https://blog.cloudflare.com/q1-2026-internet-disruption-summary/)

The first quarter of 2026 saw a surge in Internet disruptions, from nationwide shutdowns in Uganda and Iran to unprecedented drone strikes on cloud infrastructure. We explore the data behind these events using Cloudflare Radar.

![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[David Belson](https://blog.cloudflare.com/author/david-belson/)

April 10, 2026## [500 Tbps of capacity: 16 years of scaling our global network](https://blog.cloudflare.com/500-tbps-of-capacity/)

Cloudflare’s global network has officially crossed 500 Tbps of external capacity, enough to route more than 20% of the web and absorb the largest DDoS attacks ever recorded.

![Tanner Ryan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW467CNB4WTT5E3940DPZKCA.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanner Ryan](https://blog.cloudflare.com/author/tanner/)

February 27, 2026## [ASPA: making Internet routing more secure](https://blog.cloudflare.com/aspa-secure-internet/)

ASPA is the cryptographic upgrade for BGP that helps prevent route leaks by verifying the path network traffic takes. New features in Cloudflare Radar make tracking its adoption easy.

![Mingwei Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ER28A8EPWVBKJWBWZ58R.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Mingwei Zhang](https://blog.cloudflare.com/author/mingwei/) and [Bryton Herdes](https://blog.cloudflare.com/author/bryton/)

January 23, 2026## [Route leak incident on January 22, 2026](https://blog.cloudflare.com/route-leak-incident-january-22-2026/)

An automated routing policy configuration error caused us to leak some Border Gateway Protocol prefixes unintentionally from a router at our Miami data center. We discuss the impact and the changes we are implementing as a result.

![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Tom Strickx](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SA24D9KSWM8WR9ZTW1BJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Bryton Herdes](https://blog.cloudflare.com/author/bryton/) and [Tom Strickx](https://blog.cloudflare.com/author/tom-strickx/)

January 6, 2026## [A closer look at a BGP anomaly in Venezuela](https://blog.cloudflare.com/bgp-route-leak-venezuela/)

There has been speculation about the cause of a BGP anomaly observed in Venezuela on January 2. We take a look at BGP route leaks, and dive into what the data suggests caused the anomaly in question.

![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Bryton Herdes](https://blog.cloudflare.com/author/bryton/)

October 31, 2025## [BGP zombies and excessive path hunting](https://blog.cloudflare.com/going-bgp-zombie-hunting/)

A BGP “zombie” is essentially a route that has become stuck in the Default-Free Zone (DFZ) of the Internet, potentially due to a missed or lost prefix withdrawal. We’ll walk through some situations where BGP zombies are more likely to rise from the dead and wreak havoc. 

![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)![June Slater](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SCBXA2XSNDDC08ZYCVCS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Mingwei Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ER28A8EPWVBKJWBWZ58R.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Bryton Herdes](https://blog.cloudflare.com/author/bryton/), [June Slater](https://blog.cloudflare.com/author/june-slater/), and [Mingwei Zhang](https://blog.cloudflare.com/author/mingwei/)

September 26, 2025## [Monitoring AS-SETs and why they matter](https://blog.cloudflare.com/monitoring-as-sets-and-why-they-matter/)

We will cover some of the reasons why operators need to monitor the AS-SET memberships for their ASN, and now Cloudflare Radar can help. 

![Mingwei Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ER28A8EPWVBKJWBWZ58R.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Mingwei Zhang](https://blog.cloudflare.com/author/mingwei/) and [Bryton Herdes](https://blog.cloudflare.com/author/bryton/)

May 21, 2025## [Bringing connections into view: real-time BGP route visibility on Cloudflare Radar](https://blog.cloudflare.com/bringing-connections-into-view-real-time-bgp-route-visibility-on-cloudflare/)

Real-time BGP route visualization is now available on Cloudflare Radar, providing immediate insights into global Internet routing.

![Mingwei Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ER28A8EPWVBKJWBWZ58R.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Mingwei Zhang](https://blog.cloudflare.com/author/mingwei/)

September 2, 2024## [Making progress on routing security: the new White House roadmap](https://blog.cloudflare.com/white-house-routing-security/)

On September 3, 2024, the White House published a report on Internet routing security. We’ll talk about what that means and how you can help.

![Mike Conlow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K1CW81W7PJYX48E0HBY1.png&w=64&h=64&f=webp&fit=cover&position=center)![Emily Music](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44ZQ5BAP576B77RTRPVBCB.png&w=64&h=64&f=webp&fit=cover&position=center)![Tom Strickx](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SA24D9KSWM8WR9ZTW1BJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Mike Conlow](https://blog.cloudflare.com/author/mike-conlow/), [Emily Music](https://blog.cloudflare.com/author/emily-music/), and [Tom Strickx](https://blog.cloudflare.com/author/tom-strickx/)

August 6, 2024## [The backbone behind Cloudflare’s Connectivity Cloud](https://blog.cloudflare.com/backbone2024/)

Read through the latest milestones and expansions of Cloudflare's global backbone and how it supports our Connectivity Cloud and our services

![Shozo Moritz Takaya](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PS0652VR1R4C309YE8YC.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Bryton Herdes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KYAJP648S3013NEXJ8RKZF1Y.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Shozo Moritz Takaya](https://blog.cloudflare.com/author/shozo/) and [Bryton Herdes](https://blog.cloudflare.com/author/bryton/)

June 21, 2024## [Exam-ining recent Internet shutdowns in Syria, Iraq, and Algeria](https://blog.cloudflare.com/syria-iraq-algeria-exam-internet-shutdown/)

Similar to actions taken over the last several years, governments in Syria, Iraq, and Algeria have again disrupted Internet connectivity nationwide in an attempt to prevent cheating on exams. We investigate how these disruptions were implemented, and their impact

![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[David Belson](https://blog.cloudflare.com/author/david-belson/)

September 26, 2023## [Traffic anomalies and notifications with Cloudflare Radar](https://blog.cloudflare.com/traffic-anomalies-notifications-radar/)

Cloudflare Radar now displays country and ASN traffic anomalies in the Outage Center as they are detected, as well as publishing anomaly information via API. We are also launching Radar notifications, enabling users to subscribe to notifications about traffic anomalies

![David Belson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EZZ65KR303FZYTSNR3WH.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[David Belson](https://blog.cloudflare.com/author/david-belson/)

July 28, 2023## [Cloudflare Radar's new BGP origin hijack detection system](https://blog.cloudflare.com/bgp-hijack-detection/)

BGP origin hijacks allow attackers to intercept, monitor, redirect, or drop traffic destined for the victim's networks. We explain how Cloudflare built its BGP hijack detection system, from its design and implementation to its integration on Cloudflare Radar

![Mingwei Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47ER28A8EPWVBKJWBWZ58R.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Celso Martinho](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K1GG0634XMEFX9CSSGM2.png&w=64&h=64&f=webp&fit=cover&position=center)

[Mingwei Zhang](https://blog.cloudflare.com/author/mingwei/) and [Celso Martinho](https://blog.cloudflare.com/author/celso/)

December 16, 2022## [Helping build a safer Internet by measuring BGP RPKI Route Origin Validation](https://blog.cloudflare.com/rpki-updates-data/)

Is BGP safe yet? If the question needs asking, then it isn't. But how far the Internet is from this goal is what we set out to answer.

![Carlos Rodrigues](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P9VMTDZ2R4BDYEPSPMX4.png&w=64&h=64&f=webp&fit=cover&position=center)![Vasilis Giotsas](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FSZC6EWB0YJ1G7V5AEGX.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Carlos Rodrigues](https://blog.cloudflare.com/author/carlos-rodrigues/) and [Vasilis Giotsas](https://blog.cloudflare.com/author/vasilis/)

November 24, 2022## [Why BGP communities are better than AS-path prepends](https://blog.cloudflare.com/prepends-considered-harmful/)

Routing on the Internet follows a few basic principles. Unfortunately not everything on the Internet is created equal, and prepending can do more harm than good. In this blog post we’ll talk about the problems that prepending aims to solve, and some alternative solutions

![Tom Strickx](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SA24D9KSWM8WR9ZTW1BJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tom Strickx](https://blog.cloudflare.com/author/tom-strickx/)

Load more
