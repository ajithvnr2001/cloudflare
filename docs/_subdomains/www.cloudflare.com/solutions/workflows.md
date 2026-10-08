---
url: https://www.cloudflare.com/solutions/workflows/
title: Durable Workflows - Multi-Step Application Engine
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:17.795766+00:00
---

# Durable Workflows - Multi-Step Application Engine

> Source: https://www.cloudflare.com/solutions/workflows/

Workflows 

###  Build durable multi-step applications. 

Workflows is an execution engine built on Cloudflare Workers — to build applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe progression, and programmatically trigger events-based instances based across your services. 

**Step-based**

Any logic wrapped in a step can be automatically retried and memoized for durability.

**State included**

Every instance persists to its own local state: no need to set up or manage a database or control plane.

**Human-in-the-loop**

Wait on external events: webhooks, approvals, queue messages — you name it.

### Proven workflow infrastructure, powering products at scale

The same end-to-end workflow stack behind Cloudflare's own products — battle-tested across billions of requests and millions of users daily. Build with the same primitives we use in production.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Workflows`

####  Use Workflows to Power 

Build applications that need to be reliable and long-running everywhere. 

Building AI agents 

Code review tasks, compact context, or processing data

Asynchronous tasks 

Lifecycle emails, billing jobs, and critical data processing tasks

Post-processing user-generated content 

Run inference, clean up or validate uploaded content

### Durable building blocks

Everything you need to build, deploy, and scale durable multi-step applications on Cloudflare's global infrastructure.

**Step-based execution**

Any logic wrapped in a step can be automatically retried and memoized for durability. 

**Built-in state management**

Every instance persists to its own local state: no need to set up or manage a database or control plane. 

**Human-in-the-loop**

Wait on external events: webhooks, approvals, queue messages — you name it. 

**Automatic retries**

Built-in retry logic with exponential backoff and configurable retry policies for resilient execution. 

**Observability included**

Built-in logging, metrics, and tracing to monitor workflow execution and debug issues. 

**Event-driven triggers**

Programmatically trigger workflow instances based on events across your services. 

**Scale-to-zero pricing**

Pay only for the CPU cycles your workflows actually use — idle workflows cost nothing. 

[ Workflows documentation  ](https://developers.cloudflare.com/workflows/) [ Get started guide  ](https://developers.cloudflare.com/workflows/get-started/)

### Everything you need to automate

Deploy durable multi-step applications between meetings.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

/index.ts

01020304050607080910111213141516
    
    
    import { WorkflowEntrypoint } from "cloudflare:workers";
    
    export class DataProcessingWorkflow extends WorkflowEntrypoint {
      async run(event, step) {
        // This step will be automatically retried on failure
        const result = await step.do("processData", async () => {
          const input = event.payload.data;
          return input;
        });
    
        // Another step that can be retried independently
        await step.do("transform", async () => {
          return result.map((item) => ({ ...item, processed: true }));
        });
      }
    }

Step-based execution included 

Any logic wrapped in a step can be automatically retried and memoized for durability with zero configuration.

State management for zero config 

Automatically persist workflow state without setting up databases or control planes

Event-driven architecture 

Built on Workers to provide an out of the box event-driven layer, with global distribution included

### Build with durable workflows

Deploy long-running applications with zero infrastructure overhead — designed to scale globally and handle complex multi-step processes automatically.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

npmpnpmyarn

$ █

Durable by design 

Your workflows run at the edge in 330+ cities worldwide — with [D1 databases](https://developers.cloudflare.com/d1/), [KV storage](https://developers.cloudflare.com/kv/), and [R2 object storage](https://developers.cloudflare.com/r2/) available for state management.

Event-driven ready 

Deploy both workflows and triggers together — from [webhooks](https://developers.cloudflare.com/workers/tutorials/build-a-slackbot/#configure-your-github-webhooks) to [queue messages](https://developers.cloudflare.com/queues/), all with automatic retry and state management.

Observable by default 

Built-in [logging](https://developers.cloudflare.com/workers/observability/logs/), [metrics](https://developers.cloudflare.com/workflows/observability/metrics-analytics/#metrics), and tracing help you monitor and debug workflow execution.

Clonable 

####  Cloneable is in the field of very heavy data collection, and we need a reliable provider who can sync data while users are working out in more isolated places. Not having to worry about latency from a bucket across the country and the egress costs, allows us/our customers to focus on what really matters: getting the data. 

##  Cloudflare powers  
1 in 5 sites on the Internet

Trusted by the teams you trust. 

ShopifyCharacter.AIIntercomDoorDashDiscordZendeskLovablenpmSiteGPTLiveblocksLeaguedSeatedPeopleShopifyCharacter.AIIntercom

Pause

![Duncan Davidson](https://www.cloudflare.com/people/duncan-davidson.png)

> ### “For Shopify, the real challenge is not about how many different pieces of complex technology we can use but the opposite. Cloudflare helps us find a simple way to achieve something very complex that we can scale and maintain.”

**Duncan Davidson** , VP of Developer Productivity, Shopify

And thousands more... 

![Fossil](https://www.cloudflare.com/companies/e4ea9663-706f-4411-b25c-539fca52c862.svg)

![Visa Print](https://www.cloudflare.com/companies/3ccce0b1-a008-42d0-a6e3-7c228a78d0c8.svg)

![Canva](https://www.cloudflare.com/companies/0c59832d-e3d3-458e-bb88-8894a4f9d18e.svg)

![Uber](https://www.cloudflare.com/companies/74c5e83e-abc8-49a4-a55b-0ecf972bb849.svg)

![Broadcom](https://www.cloudflare.com/companies/ecbc9f10-50da-4a73-9a27-54a18d00aa9e.svg)

![Department of Commerce](https://www.cloudflare.com/companies/21708102-7a68-4230-8ca6-b088879ce262.png)

![Hubspot](https://www.cloudflare.com/companies/47e69d4e-6b6d-46e4-868a-3f22950572f8.svg)

![Loreal](https://www.cloudflare.com/companies/4b6fd6e4-96c4-4c26-a4e4-d52c75d93cdf.svg)

![Roche](https://www.cloudflare.com/companies/02430f10-e1fe-4e48-8400-43adfa3328e2.svg)

![Homeland Security](https://www.cloudflare.com/companies/1e9d9fd3-c1e8-47df-a4dc-7c97d9f8b6c8.svg)

![Braze](https://www.cloudflare.com/companies/673e6f52-edfd-4d95-81b6-6a523da89374.svg)

![Carrefour](https://www.cloudflare.com/companies/6d07e6ca-12a0-4244-b1dd-327cde491e2f.svg)

![Delivery Hero](https://www.cloudflare.com/companies/6ad20752-7949-4dc6-9de8-c93d5e33888a.svg)

![SoFi](https://www.cloudflare.com/companies/ad2cf871-580c-41ba-ac0c-8d2f7be3c8ff.svg)

![Telus](https://www.cloudflare.com/companies/1f3ec03d-833c-4b28-b61d-317e3fa0c886.svg)

![Workday](https://www.cloudflare.com/companies/c9ead275-76e3-424e-b181-4f410ecb68ce.svg)

![Colgate Palmolive](https://www.cloudflare.com/companies/75ef1c21-b669-4199-b229-d6551a7e951d.svg)

![Indeed](https://www.cloudflare.com/companies/7f0c2889-d3c1-4b33-b205-e1917c22bb53.svg)

![Labcorp](https://www.cloudflare.com/companies/6d985b86-996a-45d4-b004-f8becedf5676.svg)

![NCR Voyix](https://www.cloudflare.com/companies/7b4629c1-433d-4069-a068-1a227076122c.svg)

![Garmin](https://www.cloudflare.com/companies/d3e85b73-865f-4017-b29c-5acaf120c0c4.svg)

![Genuine Parts Company](https://www.cloudflare.com/companies/d89fbfe9-ff19-4095-9f9d-94e39bc90ecc.svg)

![Mars](https://www.cloudflare.com/companies/ef9e904a-27f8-44e1-870f-935dc2bfdb90.svg)

![Telefonica](https://www.cloudflare.com/companies/54d619f3-887b-4eb2-8c4a-1fd75959f303.svg)

![Anthropic](https://www.cloudflare.com/companies/2427de55-f683-4bf7-a30a-d748222436ce.svg)

![Asana](https://www.cloudflare.com/companies/2aee0afe-176a-449e-a926-a4444adf1fe0.svg)

![Atlassian](https://www.cloudflare.com/companies/bd5897bc-21b1-4ec0-bc08-6697da26ac59.svg)

![Block](https://www.cloudflare.com/companies/05745480-bcb4-4699-8344-aa2e854fe6a6.svg)

![CoreWeave](https://www.cloudflare.com/companies/7d670892-b1c3-4d75-854e-f3cf43b5dd1a.svg)

![Leonardo.ai](https://www.cloudflare.com/companies/39a8c473-3e3e-448b-ac0b-109ec525621e.svg)

![Stripe](https://www.cloudflare.com/companies/23f76a0c-6da4-4fcd-a101-7fcddcb3cc29.svg)

![Block](https://www.cloudflare.com/companies/e6a62228-5ebe-410e-bb84-d06227d882a2.svg)

![Fossil](https://www.cloudflare.com/companies/e4ea9663-706f-4411-b25c-539fca52c862.svg)

![Visa Print](https://www.cloudflare.com/companies/3ccce0b1-a008-42d0-a6e3-7c228a78d0c8.svg)

![Canva](https://www.cloudflare.com/companies/0c59832d-e3d3-458e-bb88-8894a4f9d18e.svg)

![Uber](https://www.cloudflare.com/companies/74c5e83e-abc8-49a4-a55b-0ecf972bb849.svg)

![Broadcom](https://www.cloudflare.com/companies/ecbc9f10-50da-4a73-9a27-54a18d00aa9e.svg)

![Department of Commerce](https://www.cloudflare.com/companies/21708102-7a68-4230-8ca6-b088879ce262.png)

![Hubspot](https://www.cloudflare.com/companies/47e69d4e-6b6d-46e4-868a-3f22950572f8.svg)

![Loreal](https://www.cloudflare.com/companies/4b6fd6e4-96c4-4c26-a4e4-d52c75d93cdf.svg)

![Roche](https://www.cloudflare.com/companies/02430f10-e1fe-4e48-8400-43adfa3328e2.svg)

![Homeland Security](https://www.cloudflare.com/companies/1e9d9fd3-c1e8-47df-a4dc-7c97d9f8b6c8.svg)

![Braze](https://www.cloudflare.com/companies/673e6f52-edfd-4d95-81b6-6a523da89374.svg)

![Carrefour](https://www.cloudflare.com/companies/6d07e6ca-12a0-4244-b1dd-327cde491e2f.svg)

![Delivery Hero](https://www.cloudflare.com/companies/6ad20752-7949-4dc6-9de8-c93d5e33888a.svg)

![SoFi](https://www.cloudflare.com/companies/ad2cf871-580c-41ba-ac0c-8d2f7be3c8ff.svg)

![Telus](https://www.cloudflare.com/companies/1f3ec03d-833c-4b28-b61d-317e3fa0c886.svg)

![Workday](https://www.cloudflare.com/companies/c9ead275-76e3-424e-b181-4f410ecb68ce.svg)

![Colgate Palmolive](https://www.cloudflare.com/companies/75ef1c21-b669-4199-b229-d6551a7e951d.svg)

![Indeed](https://www.cloudflare.com/companies/7f0c2889-d3c1-4b33-b205-e1917c22bb53.svg)

![Labcorp](https://www.cloudflare.com/companies/6d985b86-996a-45d4-b004-f8becedf5676.svg)

![NCR Voyix](https://www.cloudflare.com/companies/7b4629c1-433d-4069-a068-1a227076122c.svg)

![Garmin](https://www.cloudflare.com/companies/d3e85b73-865f-4017-b29c-5acaf120c0c4.svg)

![Genuine Parts Company](https://www.cloudflare.com/companies/d89fbfe9-ff19-4095-9f9d-94e39bc90ecc.svg)

![Mars](https://www.cloudflare.com/companies/ef9e904a-27f8-44e1-870f-935dc2bfdb90.svg)

![Telefonica](https://www.cloudflare.com/companies/54d619f3-887b-4eb2-8c4a-1fd75959f303.svg)

![Anthropic](https://www.cloudflare.com/companies/2427de55-f683-4bf7-a30a-d748222436ce.svg)

![Asana](https://www.cloudflare.com/companies/2aee0afe-176a-449e-a926-a4444adf1fe0.svg)

![Atlassian](https://www.cloudflare.com/companies/bd5897bc-21b1-4ec0-bc08-6697da26ac59.svg)

![Block](https://www.cloudflare.com/companies/05745480-bcb4-4699-8344-aa2e854fe6a6.svg)

![CoreWeave](https://www.cloudflare.com/companies/7d670892-b1c3-4d75-854e-f3cf43b5dd1a.svg)

![Leonardo.ai](https://www.cloudflare.com/companies/39a8c473-3e3e-448b-ac0b-109ec525621e.svg)

![Stripe](https://www.cloudflare.com/companies/23f76a0c-6da4-4fcd-a101-7fcddcb3cc29.svg)

![Block](https://www.cloudflare.com/companies/e6a62228-5ebe-410e-bb84-d06227d882a2.svg)

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Workflows run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

[ Compute ](https://www.cloudflare.com/products/#compute)

[ Browser Run  Automated browsers  ](https://www.cloudflare.com/products/browser-run/)

[ Containers  Any language, anywhere  ](https://www.cloudflare.com/products/containers/)

[ Durable Objects  Stateful compute  ](https://www.cloudflare.com/products/durable-objects/)

[ Sandboxes  Secure code execution  ](https://www.cloudflare.com/products/sandboxes/)

[ Workers  Global serverless functions  ](https://www.cloudflare.com/products/workers/)

[ Workers for Platforms  Programmable Platform Solutions  ](https://www.cloudflare.com/products/workers-for-platforms/)

[ Workflows  Process orchestration  ](https://www.cloudflare.com/products/workflows/)

[ Storage ](https://www.cloudflare.com/products/#storage)

[ Artifacts  Git-native versioned storage  ](https://www.cloudflare.com/products/artifacts/)

[ D1  Serverless SQL  ](https://www.cloudflare.com/products/d1/)

[ Basin  Ingest, catalog & query data  ](https://www.cloudflare.com/products/data-platform/)

[ Hyperdrive  Global databases  ](https://www.cloudflare.com/products/hyperdrive/)

[ K2  Publish and subscribe to durable, ordered event streams  ](https://www.cloudflare.com/products/k2/)

[ Queues  Message processing  ](https://www.cloudflare.com/products/queues/)

[ R2  Egress-free storage  ](https://www.cloudflare.com/products/r2/)

[ KV  Ultra-fast key-value storage  ](https://www.cloudflare.com/products/kv/)

[ AI ](https://www.cloudflare.com/products/#ai)

[ Agents  Build stateful AI agents  ](https://www.cloudflare.com/products/agents/)

[ AI Gateway  AI observability  ](https://www.cloudflare.com/products/ai-gateway/)

[ AI Search  Instant retrieval  ](https://www.cloudflare.com/products/ai-search/)

[ Vectorize  Vector database  ](https://www.cloudflare.com/products/vectorize/)

[ Workers AI  Edge AI models  ](https://www.cloudflare.com/products/workers-ai/)

[ SASE / Zero Trust ](https://www.cloudflare.com/products/#sase)

[ SASE  Cloudflare SASE platform  ](https://www.cloudflare.com/sase/)

[ Access  Zero trust access to private resources  ](https://www.cloudflare.com/products/access/)

[ CASB  SaaS and cloud posture  ](https://www.cloudflare.com/products/casb/)

[ Data Loss Prevention  Protect sensitive data  ](https://www.cloudflare.com/products/dlp/)

[ Gateway  Web filtering  ](https://www.cloudflare.com/products/gateway/)

[ Browser Isolation  Secure web browsing  ](https://www.cloudflare.com/products/browser-isolation/)

[ WAN  Cloud-delivered networking  ](https://www.cloudflare.com/products/wan/)

[ Email Security  Phishing protection  ](https://www.cloudflare.com/products/email-security/)

[ Security ](https://www.cloudflare.com/products/#security)

[ DDoS Protection  Mitigation Solutions  ](https://www.cloudflare.com/products/ddos/)

[ Rate Limiting  Abuse prevention  ](https://www.cloudflare.com/products/rate-limiting/)

[ SSL  Secure Your Site with SSL  ](https://www.cloudflare.com/products/ssl/)

[ Turnstile  A CAPTCHA Replacement Solution  ](https://www.cloudflare.com/products/turnstile/)

[ WAF  Web Application Firewall  ](https://www.cloudflare.com/products/waf/)

[ Magic Transit  DDoS Protection for Networks  ](https://www.cloudflare.com/products/magic-transit/)

[ Client-Side Security  Prevent browser supply chain attacks  ](https://www.cloudflare.com/products/client-side-security/)

[ Bot Management  Block bad bots  ](https://www.cloudflare.com/products/bot-management/)

[ Network & Content Delivery ](https://www.cloudflare.com/products/#network)

[ CDN  Faster delivery & caching  ](https://www.cloudflare.com/products/cdn/)

[ DNS  Fast DNS  ](https://www.cloudflare.com/products/dns/)

[ Load Balancing  Zero downtime  ](https://www.cloudflare.com/products/load-balancing/)

[ TURN / SFU  Real-time infra  ](https://www.cloudflare.com/products/turn-sfu/)

[ Analytics  Web Performance & Security  ](https://www.cloudflare.com/products/analytics/)

# Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up)[ View docs  ](https://developers.cloudflare.com/)

No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet  No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet 
