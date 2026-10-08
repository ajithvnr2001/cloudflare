---
url: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-12-19-emergency/
title: 2023-12-19 - Emergency \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:51.134088+00:00
---

# 2023-12-19 - Emergency · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-12-19-emergency/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Changelog](https://developers.cloudflare.com/ddos-protection/change-log/)

  4. /[HTTP DDoS managed ruleset](https://developers.cloudflare.com/ddos-protection/change-log/http/)
  5. /2023-12-19 - Emergency



# 2023-12-19 - Emergency

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-12-19-emergency/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Rule ID| Description| Previous Action| New Action| Notes  
---|---|---|---|---  
...1fc1e601| HTTP requests with unusual HTTP headers or URI path (signature #31).| block| block| Add more characteristics to the unusual HTTP headers or URI path.  
...22807318| HTTP requests from known botnets.| log| ddos_dynamic| Extend the rule to catch more attacks.  
...d2f294d7| HTTP requests trying to impersonate browsers.| ddos_dynamic| ddos_dynamic| Change the rule to catch more attacks.  
  
[Previous2024-01-05](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-01-05/)[Next2023-12-14 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-12-14-emergency/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/change-log/http/2023-12-19-emergency.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
