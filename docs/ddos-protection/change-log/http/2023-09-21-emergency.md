---
url: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-21-emergency/
title: 2023-09-21 - Emergency \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:50.289026+00:00
---

# 2023-09-21 - Emergency · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-21-emergency/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Changelog](https://developers.cloudflare.com/ddos-protection/change-log/)

  4. /[HTTP DDoS managed ruleset](https://developers.cloudflare.com/ddos-protection/change-log/http/)
  5. /2023-09-21 - Emergency



# 2023-09-21 - Emergency

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-21-emergency/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Rule ID| Description| Previous Action| New Action| Notes  
---|---|---|---|---  
...1d73128d| HTTP requests from known botnet (signature #56).| block| block| Make the rule customizable as it might cause false positive in rare cases.  
...4a95ba67| HTTP requests with unusual HTTP headers or URI path (signature #32).| ddos_dynamic| ddos_dynamic| Expand the scope of the rule to catch more attacks.  
...6fe7a312| HTTP requests from known botnet (signature #70).| block| block| Update the rule to remove some rare false positives.  
  
[Previous2023-09-24 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-24-emergency/)[Next2023-09-05 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2023-09-05-emergency/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/change-log/http/2023-09-21-emergency.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
