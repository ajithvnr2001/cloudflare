---
url: https://www.cloudflare.com/products/kv/
title: Cloudflare KV - Global Key-Value Database
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:16.835922+00:00
---

# Cloudflare KV - Global Key-Value Database

> Source: https://www.cloudflare.com/products/kv/

KV 

## Fast, globally distributed key-value database with infinite scale

### Workers KV is an eventually consistent, high-performance key-value data database built for Workers. KV is ideal for read-heavy, low-latency edge decision making and configuration.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/kv/)

**Global Low-Latency Reads**

Serve configuration or content to users worldwide with <5ms hot read latencies — thanks to Cloudflare's edge network.

**Infinite Scale, Simple API**

One API to store and retrieve key-value pairs — unlimited storage, high scalability, no infrastructure to manage.

**More Than a Cache**

Unlike a volatile cache, KV stores data persistently in central regions with exceptional availability and durability.

### Fast, global, simple - here's how:

Workers KV persists data in Cloudflare edge colocations and distributed central regions. Reads from new edge locations pull requested key-value pairs, making them available for sub-5ms reads on subsequent requests ("hot reads"). This architecture is optimized for read-heavy workloads, letting you scale to 1 million RPS and beyond, with no infrastructure to manage.

Faster

Slower

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`KV`

####  Perfect for Edge-First Applications 

You can use KV to: 

[ View docs  ](https://developers.cloudflare.com/kv/)

Build Distributed Configuration 

Manage feature flags, A/B test variants, and redirect rules globally without managing deployments.

Serve Static Assets 

Serve small but critical files like scripts, icons, images, or JSON payloads directly from the edge.

Personalize your app 

Store user preferences or routing maps to customize experiences with near-zero latency.

Authorization 

Quickly look up API keys or authentication tokens to validate requests before they reach your origin.

Manage Dynamic Data 

Store and retrieve complex information as JSON documents, allowing your data structure to evolve easily without complex migrations.

### Cloudflare Workers are fast, elastic, and serverless functions that scale automatically from zero to millions of requests

Instant access to the data your functions need. Workers KV stores and serves key-value pairs worldwide in milliseconds – ideal for personalization, configuration, and read-heavy workloads at global scale.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

basic.ts  ab-tests.ts  api-keys.ts  proxy.ts 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16 
    
    
    export default {  async fetch(request, env, ctx): Promise<Response> {    await env.KV.put('KEY', 'VALUE');    const value = await env.KV.get('KEY');    const allKeys = await env.KV.list();    await env.KV.delete('KEY');
        return new Response(      JSON.stringify({        value: value,        allKeys: allKeys,      }),    );  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15 
    
    
    export default {  async fetch(request, env) {    // Get the entire A/B test configuration object from KV    const config = await env.CONFIG_STORE.get('homepage-test', 'json');
        // Assign user to a group (e.g., based on a cookie or URL)    const group = request.headers.get('X-User-Group') || 'control';
        // Return the specific configuration for the user's group    const variantData = config[group] || config.control;    return new Response(JSON.stringify(variantData), {      headers: { 'content-type': 'application/json' },    });  },} satisfies ExportedHandler<Env>;

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22 
    
    
    export default {  async fetch(request, env) {    // Get Authorization key from request headers    const apiKey = request.headers.get('Authorization')?.replace('Bearer ', '');
        if (!apiKey) {      return new Response('Authorization header missing', { status: 401 });    }
        // Check if the API key is valid and get associated metadata    const keyData = await env.API_KEYS.get(apiKey, 'json');
        if (keyData && keyData.enabled) {      // Key is valid, add user info to the request and fetch the origin      const newHeaders = new Headers(request.headers);      newHeaders.set('X-User-ID', keyData.userId);      return fetch(request, { headers: newHeaders });    }
        return new Response('Invalid API Key', { status: 403 });  },} satisfies ExportedHandler<Env>;

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23 
    
    
    export default {  async fetch(request, env) {    const url = new URL(request.url);    const path = url.pathname; // e.g., "/api/users"
        // Look up the path prefix (e.g., "/api") to find the correct origin hostname    const pathPrefix = '/' + path.split('/')[1];    const originHostname = await env.ROUTING_RULES.get(pathPrefix);
        if (originHostname) {      // Construct the new URL for the backend service      const newUrl = new URL(url);      newUrl.hostname = originHostname;
          // Act as a reverse proxy: fetch the content from the backend      // and return it to the original client.      return fetch(newUrl.toString(), request);    }
        // If no route matches, return a 404 or forward to a default origin    return new Response('Service not found for this path', { status: 404 });  },} satisfies ExportedHandler<Env>;

Store and retrieve data globally 

Write, read, list, and delete key-value pairs from any Worker using a simple API. Ideal for configuration, personalization, and low-latency lookups.

Power A/B Tests from the Edge 

Use Workers KV to store and serve configuration data, like A/B test variants. Fetch a JSON object containing your test parameters and dynamically alter your application's response with minimal latency.

Verify API Keys Instantly 

Secure your endpoints by validating API keys or authentication tokens at the edge. Before a request hits your origin, a Worker can check the key against a KV store, blocking unauthorized traffic with zero latency.

Route Requests with a Dynamic Reverse Proxy 

Use Workers KV to maintain a dynamic routing table at the edge. Map incoming paths to different backend services or origins without redeploying your Worker. This allows you to seamlessly shift traffic, canary release new versions, or build a multi-service architecture behind a single domain.

Leagued 

#### "

####  Choosing Cloudflare as our serverless provider was a no-brainer. Workers KV took just 15 minutes to get up and running. The ability to quickly spin up a Worker, deploy it to production, and scale effortlessly has been invaluable. " 

Sammi Sinno  CEO 

###  Workers KV Pricing 

Lightning-fast key-value storage. [View Storage & Data pricing details](https://www.cloudflare.com/plans/#developer-platform/storage)

Component

Free

Paid

Stored Data 

Free

1 GB 

Paid

$0.50 / GB-month 

Read Requests 

Free

100,000 / day 

Paid

$0.50 / million requests 

Write, Delete, List requests 

Free

1,000 / day 

Paid

$5.00 / million requests 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, KV runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
