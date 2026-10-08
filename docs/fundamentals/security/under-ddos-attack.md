---
url: https://developers.cloudflare.com/fundamentals/security/under-ddos-attack/
title: Under a DDoS attack? \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:27.943786+00:00
---

# Under a DDoS attack? · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/security/under-ddos-attack/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /Security
  4. /Under a DDoS attack?



# Under a DDoS attack?

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/security/under-ddos-attack/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCommon signs of an attack

A distributed denial-of-service (DDoS) attack is where a large number of computers or devices, usually controlled by a single attacker, attempt to access a website or online service all at once. This flood of traffic can overwhelm the website's origin servers, causing the site to slow down or even crash.
    
    
    sequenceDiagram;
        participant User;
        participant Website;
        participant Server;
        participant Botnet;
        User->>Website: Requests to access site
        Website->>Origin Server: Processes user requests
        Botnet->>Origin Server: Sends a flood of traffic
        Origin Server-->>Website: Slows down due to traffic overload
        Origin Server-->>User: Unable to respond to user requests
    

  


## Common signs of an attack

Common signs that you are under DDoS attack include:

  * Your site is offline or slow to respond to requests.
  * Unexpected spikes appear in the graph of **Requests Through Cloudflare** or **Bandwidth** in your Cloudflare **Analytics** app.
  * Strange requests appear in your origin web server logs that do not match normal visitor behavior.



Note

If you are currently under DDoS attack, refer to [Proactive DDoS defense best practices](https://developers.cloudflare.com/ddos-protection/best-practices/proactive-defense/).

[PreviousSecure your website ↗︎](https://developers.cloudflare.com/learning-paths/application-security/account-security/)[NextCreate API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/security/under-ddos-attack.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
