---
url: https://www.cloudflare.com/products/workers-ai/
title: Cloudflare Workers AI - Edge AI Inference Platform
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:09.569274+00:00
---

# Cloudflare Workers AI - Edge AI Inference Platform

> Source: https://www.cloudflare.com/products/workers-ai/

[React Flow](https://reactflow.dev)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

#  The AI Inference platform 

###  Workers AI lets you run AI inference globally with one API call. No GPUs to manage, no capacity planning. Just intelligent machine learning models running where they're needed, on Cloudflare's global network. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up) [ View docs  ](https://developers.cloudflare.com/workers-ai/)

**Serverless pricing**

Pay-per-inference pricing with no idle costs. No guessing what.

**Rich model catalog**

50+ models running close to users in 200+ cities

**Widely compatible**

One API call, works with any OpenAI SDK or task type

### Scale up, and down

Inference is hard to predict and spiky in nature, unlike training. GPU utilization is, on average, only 20-40% — with one-third of organizations utilizing less than 15%. Workers AI allows customers to save by only paying for usage. No guessing or committing to hardware that goes unused.

What you pay for  
on a hyperscaler

What you pay for  
on Cloudflare

###  AI models easily accessible via code, OpenAI SDK or API 

Test, prototype, and evaluate the latest LLMs with the speed and reliability of a production environment, accessible in seconds. 

######  Kimi K2.6 

Powerful vision and agentic tool calling model 

######  GLM 4.7 Flash 

Rapid multilingual agent with expert tool calling 

######  GPT-OSS-120B 

Specialized for coding and debugging 

######  Llama 4 Scout 

Balanced generalist for everyday tasks 

[ Try in Cloudflare AI Playground ](https://playground.ai.cloudflare.com/) [ See all models ](https://developers.cloudflare.com/workers-ai/models/)

### Run any AI model with one API call

Call any model directly from your code using a single endpoint. Workers AI handles provisioning, scaling, and latency optimization automatically.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

llm.ts  curl  image.ts  curl 

1  2  3  4  5 
    
    
    const response = await env.AI.run('@cf/moonshotai/kimi-k2.6', {  messages: [    { role: 'system', content: 'You are a friendly assistant' },    { role: 'user', content: 'What is the origin of the phrase Hello, World' },  ],});

1  2  3  4 
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/moonshotai/kimi-k2.6 \  -X POST \  -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \  -d '{ "messages": [{ "role": "system", "content": "You are a friendly assistant" }, { "role": "user", "content": "Why is pizza so good" }]}'

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21 
    
    
    export interface Env {  AI: Ai;}
    export default {  async fetch(request, env): Promise<Response> {    const response = await env.AI.run('@cf/black-forest-labs/flux-1-schnell', {      prompt: 'a bengal cat vibe coding to music',      seed: Math.floor(Math.random() * 10),    });    // Convert from base64 string    const binaryString = atob(response.image);    // Create byte representation    const img = Uint8Array.from(binaryString, (m) => m.codePointAt(0));    return new Response(img, {      headers: {        'Content-Type': 'image/jpeg',      },    });  },} satisfies ExportedHandler<Env>;

1  2  3  4 
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/black-forest-labs/flux-1-schnell  \  -X POST  \  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"  \  -d '{ "prompt": "cyberpunk cat", "seed": "Random positive integer" }'

Build AI applications by calling any LLM 

Call any LLM directly from your Worker with a simple API.

Call LLMs via REST API 

Use the REST API to call any LLM from any platform or language.

Generate images instantaneously 

Generate images from your Worker using AI models.

Generate images via REST API 

Use the REST API to generate images from any platform.

### Practical AI at the Edge

Run real-world AI workloads directly on Cloudflare's global network — from LLMs to image generation and embeddings. No GPU clusters, no orchestration layers — just fast, scalable inference wherever your users are.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Workers AI`

####  Explore a Rich Catalog of 50+ Ready-to-Use Models 

Real-world examples in action 

[ See more  ](https://developers.cloudflare.com/workers-ai/)

Image generation 

Execute image generation, manipulation, and creative workflows without managing GPU infrastructure. Perfect for content platforms, social apps, and creative tools.

Speech-to-text, in real-time 

Transcribe, analyze, and generate audio content without specialized infrastructure. Built for voice agents, note-taking apps, and media processing.

Embeddings 

Create intelligent search, recommendations, and context-aware features using vector embeddings. Seamlessly integrates with Vectorize AI Search for complete AI workflows.

LLMs 

Perform a wide range of natural language tasks. Use large language models for text generation, classification, question answering, and other complex language-based operations through a simple API.

Shopify 

#### "

####  For Shopify, the real challenge is not about how many different pieces of complex technology we can use but the opposite. Cloudflare helps us find a simple way to achieve something very complex that we can scale and maintain. " 

![Duncan Davidson](https://www.cloudflare.com/people/duncan-davidson.png)

Duncan Davidson  VP of Developer Productivity 

###  Workers AI Pricing 

50+ models running at the edge. [View AI pricing details](https://www.cloudflare.com/plans/#developer-platform/ai)

Component

Free

Paid

Neurons 

Free

10,000 neurons / day 

Paid

$0.011 / thousand neurons 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Workers AI runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
