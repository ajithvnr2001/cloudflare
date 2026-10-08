---
url: https://developers.cloudflare.com/turnstile/turnstile-analytics/
title: Turnstile Analytics \u00b7 Cloudflare Turnstile docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:08.546190+00:00
---

# Turnstile Analytics · Cloudflare Turnstile docs

> Source: https://developers.cloudflare.com/turnstile/turnstile-analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /Turnstile Analytics



# Turnstile Analytics

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/turnstile-analytics/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable statisticsView widget metrics

Turnstile Analytics shows widget statistics across traffic dimensions like hostname, country, browser, and IP address. Use these metrics to identify where challenge activity is highest and whether specific sources are failing or bypassing challenges.

## Available statistics

  * **Top Hostnames** : If the Turnstile widget is placed across multiple hostnames, this will display the highest traffic hostnames where challenges are being issued.
  * **Top Browsers** : A breakdown of browsers that are most commonly encountering Turnstile challenges, helping customers spot trends in visitor traffic.
  * **Top Countries** : View the top originating countries for visitors completing challenges, which can help identify regional traffic anomalies.
  * **Top User Agents** : Identify which user agents are generating the most Turnstile challenge requests.
  * [**Top ASNs** ↗︎](https://cloudflare.com/learning/network-layer/what-is-an-autonomous-system): Displays the highest volume of challenges issued from specific Autonomous System Numbers (ASNs), helping customers detect potential bot activity.
  * **Top Operating Systems** : Shows which operating systems are most common among visitors passing or failing challenges.
  * [**Top Source IPs** ↗︎](https://cloudflare.com/learning/ddos/glossary/ip-spoofing): Identify the highest-volume IP addresses issuing Turnstile challenges, which can be useful in identifying attack sources or repeated challenge failures.



## View widget metrics

To see an overview of your widget analytics:

[ Go to **Turnstile** ↗ ](https://dash.cloudflare.com/?to=/:account/turnstile) ![Turnstile Analytics overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2028,height=904,format=webp/_astro/top-actions.Bxq-7U4T.png)

The metrics show changes in the solve rate, widget traffic, and top actions for your widget.

Refer to the pages below for more information about Turnstile Analytics:

  * [Challenge outcome](https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/)
  * [Token validation](https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/)



[PreviousOfflabel](https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/)[NextChallenge outcome](https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/turnstile-analytics/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
