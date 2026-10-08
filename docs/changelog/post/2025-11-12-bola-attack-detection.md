---
url: https://developers.cloudflare.com/changelog/post/2025-11-12-bola-attack-detection/
title: New BOLA Vulnerability Detection for API Shield \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:29.144025+00:00
---

# New BOLA Vulnerability Detection for API Shield · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-11-12-bola-attack-detection/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2025

## New BOLA Vulnerability Detection for API Shield

[API Shield](https://developers.cloudflare.com/api-shield/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-12-bola-attack-detection/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Now, API Shield automatically searches for and highlights **Broken Object Level Authorization (BOLA) attacks** on managed API endpoints. API Shield will highlight both BOLA enumeration attacks and BOLA pollution attacks, telling you what was attacked, by who, and for how long.

You can find these attacks three different ways: Security Overview, Endpoint details, or Security Analytics. If these attacks are not found on your managed API endpoints, there will not be an overview card or security analytics suspicious activity card.

On the Security Overview card, select the suggestion > **View details** to review the top attacked API endpoints, endpoint details, and the attack summary: ![BOLA attack Overview card](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1546,height=816,format=webp/_astro/bola-overview-card.hwcSeAkb.png)![BOLA attack Overview drawer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1246,height=1078,format=webp/_astro/bola-overview-drawer.DD2c0bxS.png)

From the endpoint details, you can select **View attack** to find details about the BOLA attacker’s sessions.

![BOLA attack endpoint details](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2050,height=630,format=webp/_astro/bola-endpoint-attack.UQP3MDkp.png)

From here, select **View in Analytics** to observe attacker traffic over time for the last seven days.

![BOLA attack analytics drawer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1156,height=1176,format=webp/_astro/bola-analytics-drawer.DXzC6EJU.png)

Your search will filter to traffic on that endpoint in the last seven days, along with the malicious session IDs found in the attack. Session IDs are hashed for privacy and will not be found in your origin logs. Refer to IP and JA4 fingerprint to cross-reference behavior at the origin.

At any time, you can also start your investigation into attack traffic from Security Analytics by selecting the suspicious activity card.

![Suspicious Activity card](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1252,height=722,format=webp/_astro/bola-suspicious-card._B3GB3s4.png)

We urge you to take all of this client information to your developer team to research the attacker behavior and ensure any broken authorization policies in your API are fixed at the source in your application, preventing further abuse.

In addition, this release marks the end of the beta period for these scans. All Enterprise customers with API Shield subscriptions will see these new attacks if found on their zone.
