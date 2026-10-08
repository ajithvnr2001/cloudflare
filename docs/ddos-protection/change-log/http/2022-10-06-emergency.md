---
url: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-10-06-emergency/
title: 2022-10-06 - Emergency \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:47.742421+00:00
---

# 2022-10-06 - Emergency · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/change-log/http/2022-10-06-emergency/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Changelog](https://developers.cloudflare.com/ddos-protection/change-log/)

  4. /[HTTP DDoS managed ruleset](https://developers.cloudflare.com/ddos-protection/change-log/http/)
  5. /2022-10-06 - Emergency



# 2022-10-06 - Emergency

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-10-06-emergency/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Rule ID| Description| Previous Action| New Action| Notes  
---|---|---|---|---  
...6fa59d23| HTTP requests that are very likely coming from bots.| managed_challenge| ddos_dynamic| Block very large attacks instead of challenging them.  
...91b2849e| HTTP requests with unusual HTTP headers (signature #13).| block| block| Some attacks were only partially mitigated. Now the rule should stop attacks completely.  
  
[Previous2022-10-14](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-10-14/)[Next2022-09-19 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2022-09-19-emergency/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/change-log/http/2022-10-06-emergency.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
