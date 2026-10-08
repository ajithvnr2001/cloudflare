---
url: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/concepts/ddos-prevention/
title: How to prevent DDoS attacks \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:52.118458+00:00
---

# How to prevent DDoS attacks · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/concepts/ddos-prevention/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Prevent Ddos Attacks

  4. /[Concepts](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/concepts/)
  5. /How to prevent DDoS attacks



# How to prevent DDoS attacks

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/concepts/ddos-prevention/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReduce application requests to the origin Caching Web Application Firewall (WAF)Prevent external connections

Since DDoS attacks target your web servers, the way to prevent them is to reduce requests reaching those servers.
    
    
    flowchart TD;
        A[Malicious device]-->|Request to application|CDN;
        CDN -->|Sends remaining requests|Origin;
        subgraph CDN
            WAF
            Cache
        end
        A --Prevent external connections---x Origin
    

  


Requests can come to your origin server in two ways, from your web application and from direct connections to the server itself.

* * *

## Reduce application requests to the origin

### Caching

A cache stores copies of frequently accessed resources (images, CSS files).

When a resource is cached - either on a user's browser or Content Delivery Network (CDN) server - requests for that resource do not have to go to your origin server. Instead, these resources are served directly by the cache.
    
    
    flowchart TD;
        User-->|Sends Request|Cloudflare;
        Cloudflare-->B>Has cached content?];
        B-->|Yes - Requested content|User;
        B-->|No|Origin;
        Origin-->|Requested content|User;
    

  


In the context of DDoS attacks, caching reduces the number of requests going to your origin server, which makes it harder for your server to get overwhelmed by traffic.

### Web Application Firewall (WAF)

A Web Application Firewall (WAF) creates a shield between a web app and the Internet. This shield checks incoming web requests and filters undesired traffic to help mitigate many common attacks.
    
    
    flowchart TD;
        User-->|Sends Request|WAF;
        WAF-->|Filters Request|Application;
        Application-->|Sends Request|OriginServer;
        OriginServer-->|Serves Content|Application;
        Application-->|Serves Content|User;
    

## Prevent external connections

Generally, your origin server should only accept requests coming from your web application.

This is a general best practice for security, but especially important in the context of DDoS attacks. Any traffic that bypasses your web application will also bypass any WAF or caching and has a stronger chance of overwhelming your origin.
    
    
    sequenceDiagram
      participant Client
      participant DDoS_Protection_Service
      participant Origin_Server
    
      Client->>+DDoS_Protection_Service: Request
      Note right of DDoS_Protection_Service: Filtered traffic
      DDoS_Protection_Service->>+Origin_Server: Request
      Origin_Server-->>-DDoS_Protection_Service: Response
      DDoS_Protection_Service-->>Client: Response
    
      Client->>+Origin_Server: Direct connection
      Note over Origin_Server: Potential DDoS Attack
      Origin_Server-->>-Client: Error response
    

[PreviousWhat is a DDoS attack?](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/concepts/ddos-attacks/)[NextOverview](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/baseline/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/prevent-ddos-attacks/concepts/ddos-prevention.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
