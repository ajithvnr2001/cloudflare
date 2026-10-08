---
url: https://www.cloudflare.com/products/ai-search/
title: Cloudflare AI Search - Automatic RAG infrastructure and querying
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:08.648270+00:00
---

# Cloudflare AI Search - Automatic RAG infrastructure and querying

> Source: https://www.cloudflare.com/products/ai-search/

AI Search 

## Search primitive for your agents

### Connect your data and deliver natural language search in your applications without worrying about infrastructure.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/ai-search/)

**Atomic search unit for platforms**

Create isolated AI Search instances at runtime, and spin them up or down for multi-tenant use cases.

**Always up to date**

AI Search continuously re-indexes your data so responses always reflect the latest information.

**Any source, format, and language**

Index multimodal content from sources like R2 and websites, with Workers AI models enabling search across 100+ languages.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`AI Search`

####  Everything you need for RAG 

You can use AI Search to: 

[ Add search  ](https://search.ai.cloudflare.com/)

Agent file search 

Give agents retrieval over your files and knowledge. Use it in popular agent libraries like Cloudflare's Agents SDK and more.

Multimodal search 

Search across text, images, PDFs and more from a single query, so users find the right answer no matter how it's stored.

Per-tenant or per-agent file search 

Provision an isolated AI Search instance per tenant, project, or agent at runtime, each with its own content and retrieval.

Website and code search 

Index your websites and codebases so teams and agents get cited answers across your content and code.

### Call AI Search from anywhere

Query from a Worker binding, call it from your backend with an SDK, embed a ready-made UI, or connect an MCP client.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

index.ts  main.py  App.tsx  mcp.json 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22 
    
    
    export interface Env {  AI_SEARCH: AiSearchNamespace;}
    export default {  async fetch(request, env): Promise<Response> {    // Create a dedicated AI Search instance for the tenant at runtime.    const instance = await env.AI_SEARCH.create({      id: 'tenant-a',    });
        // Upload a file and wait for it to finish indexing.    await instance.items.uploadAndPoll('handbook.pdf', file);
        // Search only that tenant's AI Search instance.    const results = await instance.search({      query: 'What does the handbook say about travel approvals?',    });
        return Response.json(results);  },} satisfies ExportedHandler<Env>;

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19 
    
    
    from cloudflare import Cloudflare
    client = Cloudflare()
    # Upload and index content into an existing instance.item = client.aisearch.namespaces.instances.items.upload(    id="my-instance",    account_id=account_id,    name="default",    file=file,)
    # Search the instance with a natural language query.results = client.aisearch.namespaces.instances.search(    id="my-instance",    account_id=account_id,    name="default",    query="How does AI Search handle uploaded content?",)

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15 
    
    
    import '@cloudflare/ai-search-snippet';
    export default function App() {  // Prebuilt search bar web component, wired to your AI Search endpoint  return (    <search-bar-snippet      apiUrl="https://<PUBLIC_ID>.search.ai.cloudflare.com/"      placeholder="Search..."      maxResults={50}      maxRenderResults={10}      show-url="true"      show-date="true"    />  );}

1  2  3  4  5  6  7  8 
    
    
    // Add AI Search to your MCP client config{  "mcpServers": {    "ai-search": {      "url": "https://<PUBLIC_ID>.search.ai.cloudflare.com/mcp",    },  },}

Dynamic search creation for multi-tenancy 

Provision a dedicated AI Search instance per tenant at runtime through your Cloudflare Worker, then upload and query it directly.

Call AI Search from your own backend 

Use the Cloudflare SDKs, like Python, to upload content and search your instance from any backend.

Embed search on your site 

Add a working search UI to any page with one component, backed by the public endpoint on every AI Search.

Add AI Search to an MCP client 

Point any MCP client at your instance's endpoint so agents can search your content as a tool.

Sentry 

#### "

####  AI Search has been a cheat code for building AI at Sentry. It is so remarkably simple that even our non-technical teams are building and deploying production-ready features. " 

![David Cramer](https://www.cloudflare.com/people/david-cramer.webp)

David Cramer  Co-founder 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, AI Search runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
