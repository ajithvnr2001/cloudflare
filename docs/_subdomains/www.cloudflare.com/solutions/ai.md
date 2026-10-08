---
url: https://www.cloudflare.com/solutions/ai/
title: Cloudflare AI Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:20:48.894802+00:00
---

# Cloudflare AI Cloud

> Source: https://www.cloudflare.com/solutions/ai/

Cloudflare AI 

###  Build and deploy AI agents and applications on the AI Cloud 

Cloudflare provides the infrastructure to scale your AI applications at every step — store training data, run inference — on the same network Cloudflare uses to power its own use of AI. 

**Run Serverless inference on GPUs**

Ship models that respond in <100 ms worldwide. No clusters to manage.

**Build Agents & MCP Servers**

Cloudflare Agents SDK + MCP let Workers coordinate tools, schedule tasks, and reason toward goals.

**Store your training data**

Store your training data in R2 for egress-free multi-cloud access to GPUs.

SiteGPT 

#### "

####  We use Cloudflare for everything – storage, cache, queues, and most importantly for training data and deploying the app on the edge, so I can ensure the product is reliable and fast. It's also been the most affordable option, with competitors costing more for a single day's worth of requests than Cloudflare costs in a month. " 

![Bhanu Teja Pachipulusu](https://www.cloudflare.com/people/bhanu-teja.png)

Bhanu Teja Pachipulusu  Founder 

### Proven AI infrastructure, powering products at scale

The same end-to-end AI stack behind Cloudflare's own products — battle-tested across billions of requests and millions of users daily. Build with the same primitives we use in production.

### The full-stack for building Agents

Everything you need to build, deploy, and scale AI Agents from inference to orchestration, all on one global network.

**Workers AI model catalog**

Access Llama 3, Gemma 3, Whisper, TTS, and LoRA-fine-tuned variants across 190+ locations. 

**Agents SDK**

Build goal-driven agents that call models, APIs, and schedules from a single TypeScript API. 

**Remote MCP servers**

Secure, OAuth-scoped endpoints that expose tools and data to agents without self-hosting. 

**AI Search**

Complete RAG workflows with automatic indexing and fresh data. Ship AI search and chat with one instance in minutes. 

**Vectorize**

Globally-replicated vector database that pairs with Workers AI for RAG in a few lines of code. 

**R2 object storage**

Store terabytes of training data, checkpoints, and user uploads. Move to any cloud for $0 egress. 

**AI Gateway**

Built-in caching, rate-limiting, model fallback, and observability for every inference call. 

[ Try in Cloudflare AI Playground  ](https://playground.ai.cloudflare.com/) [ Agents  ](https://agents.cloudflare.com)

### …And the tools to simplify it

Deploy MCP Servers between meetings with Agents SDK.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

/index.ts

01020304050607080910
    
    
    import GitHubHandler from "./github-handler";
    
    export default new OAuthProvider({
      apiRoute: "/sse",
      apiHandler: MyMCP.Router,
      defaultHandler: GitHubHandler,
      authorizeEndpoint: "/authorize",
      tokenEndpoint: "/token",
      clientRegistrationEndpoint: "/register",
    });

OAuth integration included 

Implements the provider side of the OAuth 2.1 protocol, allowing you to easily add authorization to your MCP server.

MCP playground for testing 

Our [MCP playground](https://playground.ai.cloudflare.com/) allows you to connect to remote MCP servers, with the authentication check included

MCPAgent 

Built on DurableObjects to provide an out of the box transport layer, with memory management included

### End-to-end, goal-driven agents with Agents SDK

Build intelligent, goal-driven agents that call models, APIs, and tasks from one unified SDK — designed to run fast, securely, and globally on Workers.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

npmpnpmyarn

$ █

Built-in state management 

Agents include built-in state management — sync state with clients, trigger events on changes, and read or write to each Agent's SQL database automatically.

Multi-modal interfaces 

Connect via [WebSockets](https://developers.cloudflare.com/agents/api-reference/websockets/) to stream updates in real time — from long-running reasoning tasks, [asynchronous workflows](https://developers.cloudflare.com/agents/api-reference/run-workflows/), or chat sessions built with the `useAgent` hook. Agents SDK also supports email, and voice modalities.

Multi-model with AI Gateway 

Agents are just code. Use any [AI model](https://developers.cloudflare.com/agents/api-reference/using-ai-models/), integrate browsers or APIs, fetch data from external sources, and add custom methods to extend functionality.

Secure Sandboxes 

Execute commands, manage files, run services, and expose them via public URLs - all within secure, sandboxed containers with our [Sandbox SDK](https://github.com/cloudflare/sandbox-sdk).

### Powerful primitives, seamlessly integrated

Build on the infrastructure powering 20% of the Internet.

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
