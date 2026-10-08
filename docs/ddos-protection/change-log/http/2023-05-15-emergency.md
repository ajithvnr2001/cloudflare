---
url: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-05-15-emergency/
title: 2023-05-15 - Emergency \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:49.040984+00:00
---

# 2023-05-15 - Emergency · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-05-15-emergency/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Changelog](https://developers.cloudflare.com/ddos-protection/change-log/)

  4. /[HTTP DDoS managed ruleset](https://developers.cloudflare.com/ddos-protection/change-log/http/)
  5. /2023-05-15 - Emergency



# 2023-05-15 - Emergency

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-05-15-emergency/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Rule ID| Description| Previous Action| New Action| Notes  
---|---|---|---|---  
...1fc1e601| HTTP requests with unusual HTTP headers or URI path (signature #31).| N/A| block|   
...863134d5| HTTP requests from known bad user agents.| block| block| Widen detection scope.  
...bb3cefd0| HTTP requests with unusual HTTP headers or URI path (signature #53).| N/A| block|   
...d2f294d7| HTTP requests trying to impersonate browsers.| ddos_dynamic| ddos_dynamic| Extend the rule to catch attacks across multiple subdomains.  
...d2f294d7| HTTP requests trying to impersonate browsers.| ddos_dynamic| ddos_dynamic| Expand the filter to catch more attacks.  
...f2494447| HTTP requests attempting to bypass the cache.| ddos_dynamic| ddos_dynamic| Make rule more accurate when blocking attacks.  
  
[Previous2023-05-16 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-05-16-emergency/)[Next2023-05-02 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-05-02-emergency/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/change-log/http/2023-05-15-emergency.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
