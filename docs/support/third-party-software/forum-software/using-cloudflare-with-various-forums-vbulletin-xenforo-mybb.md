---
url: https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/
title: Using Cloudflare with various forums \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:52.100355+00:00
---

# Using Cloudflare with various forums · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Third-Party Software](https://developers.cloudflare.com/support/third-party-software/)

  4. /[Forum Software](https://developers.cloudflare.com/support/third-party-software/forum-software/)
  5. /Using Cloudflare with various forums



# Using Cloudflare with various forums

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/third-party-software/forum-software/using-cloudflare-with-various-forums-vbulletin-xenforo-mybb/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOverviewSteps

## Overview

Many widely used forum platforms are compatible with Cloudflare.

These include:

  * [Discourse ↗︎](https://community.cloudflare.com/t/using-discourse-with-cloudflare-best-practices/602890)
  * vBulletin
  * Xenforo
  * MyBB



If you have a forum using these platforms, you can increase its speed and safety by adding Cloudflare.

* * *

## Steps

**1**. Cloudflare acts as a reverse proxy, meaning that all visitor IP addresses will become Cloudflare-affiliated IP addresses. If you are using services like **Stopforumspan** or blocking registration by IP address, you need to [restore original visitor IPs](https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/).

**2**. To prevent admin functions from being affected by caching or performance features, create a [Cache Rule](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#bypass-cache) to bypass cache on the admin section of your site.

**3**. If you want certain services to access your website (APIs or certain IPs), [configure the WAF](https://developers.cloudflare.com/waf/).

**4**. Review your DNS records to make sure all your subdomain records are present. If you cannot find a subdomain, [add the DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/).

[PreviousOverview](https://developers.cloudflare.com/support/third-party-software/forum-software/)[NextOverview](https://developers.cloudflare.com/support/third-party-software/others/)

Was this helpful?

YesNo
