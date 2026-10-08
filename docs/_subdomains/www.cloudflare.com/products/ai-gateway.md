---
url: https://www.cloudflare.com/products/ai-gateway/
title: Cloudflare AI Gateway - AI Application Control Plane
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:08.531786+00:00
---

# Cloudflare AI Gateway - AI Application Control Plane

> Source: https://www.cloudflare.com/products/ai-gateway/

AI Gateway 

## An intelligent control plane for your AI applications

### Connect to any model, dynamically route requests, and manage usage, billing, and logs from one unified gateway.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/ai-gateway/)

**Reduce Costs & Latency**

Easily cache responses and reduces redundant API calls — leading to direct cost savings.

**Improve Reliability with Dynamic Controls**

Configure how and when model providers APIs are called based on specific attributes or fallbacks

**Add Observability**

Enables rich usage insights such as token counts, prompt performance, and pattern analysis.

### Dynamic Routing

Automatically route requests based on latency, cost, or availability. Adjust rules instantly from the dashboard or API — no redeploys, no downtime.

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

### Core Capabilities

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Global Network Performance

Built on Cloudflare's infrastructure. Ensures low-latency, globally distributed access with automatic scalability and built-in security.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Caching

Reduces redundant API calls. Saves money and improves response time by storing and reusing frequent requests automatically.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Built-in Observability

Logs, metrics, and usage analytics. Includes fallback routing, rate limiting, and safety guardrails to manage cost, behavior, and compliance across multiple providers.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Security controls and guardrails

Protect your AI applications from leaking or sending sensitive information. Protects your AI app from malicious traffic without needing to configure or maintain anything extra.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Unified Billing

Manage all your costs with one simple bill and access every provider through a single API. Spend less time managing and more time shipping.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`AI Gateway`

####  Built for AI Application Control 

You can use AI Gateway to: 

[ View docs  ](https://developers.cloudflare.com/ai-gateway/)

Reducing latency and cost of AI apps by caching API responses 

Optimize your AI application performance and reduce costs by intelligently caching responses from AI providers.

Usage analytics — monitoring prompt performance, token counts, and behavior 

Gain deep insights into your AI usage patterns, token consumption, and prompt performance across all providers.

Building custom dashboards and alerting systems directly from AI Gateway logs 

Create comprehensive monitoring and alerting systems using AI Gateway's rich logging and metrics data.

### Control your AI infrastructure

Examples showing how to configure caching, routing, and monitoring for AI workloads.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

index.js  index.js  logging  fallback 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 
    
    
    // wrangler.jsonc// Simple configuration{  "ai": {    "binding": "AI"  }}
    // Pass through the Gateway from your Worker with Workers AI// index.jsconst resp = await env.AI.run(  "@cf/meta/llama-3.1-8b-instruct",  {    prompt: "tell me a joke",  },  {    gateway: {      id: "my-gateway",    },  },);
    // Use with OpenAI SDKimport OpenAI from "openai";
    const openai = new OpenAI({  apiKey: "my api key", // defaults to process.env["OPENAI_API_KEY"]  baseURL: await env.AI.gateway("my-gateway").getUrl("openai"),});

01  02  03  04  05  06  07  08  09  10  11  12  13  14 
    
    
    // AI Gateway with caching setenv.AI.gateway('my-gateway').run({  provider: 'openai',  endpoint: 'gpt-3.5-turbo',  headers: {    authorization: 'Bearer my-api-token',    'cf-aig-cache-ttl': 3600,  },  query: {    messages: [{ role: 'user', content: 'What is the capital of France?' }],  },});

01  02  03  04  05  06  07  08  09  10  11 
    
    
    // The patchLog method allows you to send feedback, score, and metadata for a specific log ID. All object properties are optional, so you can include any combination of the parameters:gateway.patchLog('my-log-id', {  feedback: 1,  score: 100,  metadata: {    user: '123',  },});
    // Read log details in your Worker with getLogconst log = await gateway.getLog('my-log-id');

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44 
    
    
    // Add as many fallbacks as you need, just by adding another object in the array.
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id} \  --header 'Content-Type: application/json' \  --data '[  {    "provider": "workers-ai",    "endpoint": "@cf/meta/llama-3.1-8b-instruct",    "headers": {      "Authorization": "Bearer {cloudflare_token}",      "Content-Type": "application/json"    },    "query": {      "messages": [        {          "role": "system",          "content": "You are a friendly assistant"        },        {          "role": "user",          "content": "What is Cloudflare?"        }      ]    }  },  {    "provider": "openai",    "endpoint": "chat/completions",    "headers": {      "Authorization": "Bearer {open_ai_token}",      "Content-Type": "application/json"    },    "query": {      "model": "gpt-4o-mini",      "stream": true,      "messages": [        {          "role": "user",          "content": "What is Cloudflare?"        }      ]    }  }]'

One-line setup 

Set up AI Gateway to proxy requests to AI providers with caching and observability. Compatible with OpenAI SDK and AI SDK.

Caching AI Responses 

Configure intelligent caching to reduce costs and improve response times.

Send feedback & access logs 

Your AI Gateway dashboard shows logs of individual requests, including the user prompt, model response, provider, timestamp, request status, token usage, cost, and duration. 

Fallback Routing and Rate Limiting 

Configure intelligent fallbacks and rate limiting for reliable AI operations.

Rightblogger 

####  Without AI Gateway, it’s difficult to see which applications are driving the majority of the costs with the OpenAI API … We can choose to limit the number of requests used by certain tools to control costs. 

### Frequently asked questions

###### Your question here

Add your answer here.

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, AI Gateway runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
