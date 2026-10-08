---
url: https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-06-emergency/
title: 2024-02-06 - Emergency \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:51.585060+00:00
---

# 2024-02-06 - Emergency · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-06-emergency/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

[Changelog](https://developers.cloudflare.com/ddos-protection/change-log/)

  4. /[HTTP DDoS managed ruleset](https://developers.cloudflare.com/ddos-protection/change-log/http/)
  5. /2024-02-06 - Emergency



# 2024-02-06 - Emergency

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-06-emergency/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Rule ID| Description| Previous Action| New Action| Notes  
---|---|---|---|---  
...1fc1e601| HTTP requests with unusual HTTP headers or URI path (signature #31).| block| block| Modify characteristics of the unusual HTTP headers or URI path.  
...3a679c52| Requests coming from known bad sources.| N/A| ddos_dynamic|   
...3ad719cd| HTTP requests from known botnet (signature #79).| ddos_dynamic| ddos_dynamic| Expand the scope of the rule to match more attacks.  
  
[Previous2024-02-08 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-08-emergency/)[Next2024-02-05 - Emergency](https://developers.cloudflare.com/ddos-protection/change-log/http/2024-02-05-emergency/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/change-log/http/2024-02-06-emergency.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
