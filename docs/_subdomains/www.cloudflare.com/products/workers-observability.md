---
url: https://www.cloudflare.com/products/workers-observability/
title: Cloudflare Workers Observability - Telemetry for Your Workers
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:07.221289+00:00
---

# Cloudflare Workers Observability - Telemetry for Your Workers

> Source: https://www.cloudflare.com/products/workers-observability/

Workers Observability 

## See how your Workers projects perform

### Workers Observability provides telemetry for your Workers projects, giving you the ability to see how they are performing for your end users. With instant access to search, query, and filter your logs, you can resolve problems quickly and collaborate with your team. This enables proactive issue detection and faster resolution.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/workers/observability/)

**Proactive Problem Detection**

Investigate, query, and correlate data for early problem resolution with insight into the types of events happening. Workers Observability provides instant access to search, query, and filter your logs, allowing you to resolve problems quickly and efficiently.

**Collaborative Troubleshooting**

Save and share queries with the team for increased knowledge sharing and facilitate collaborative workflows. This helps teams work together more effectively to resolve issues.

**Easy Onboarding and Management**

Begin collecting telemetry with a few lines of code or a single click for quick debugging when problems arise. Workers Observability can be implemented with minimal setup and requires little maintenance.

### Workers Observability Telemetry

Capture high cardinality, high dimensionality telemetry data directly from Workers to understand application performance across your entire stack.

Faster

Slower

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Workers Observability`

####  You can use Workers Observability to: 

Discover how Workers Observability can help you improve your Workers projects 

[ Enable observability for your Workers projects  ](https://developers.cloudflare.com/workers/observability/)

Deploy Stable Releases 

Compare metrics across Workers to identify whether an issue is global or isolated, helping you deploy more stable releases and reduce downtime.

Rapid Incident Resolution 

Workers Observability provides instant access to search, query, and filter your logs, allowing you to resolve problems quickly and efficiently, reducing the impact on your users.

Team Collaboration 

Save and share queries with your team to increase knowledge sharing and facilitate collaborative workflows, ensuring that everyone is on the same page.

Proactive Problem Prevention 

Investigate, query, and correlate data for early problem resolution with insight into the types of events happening in your Workers projects, enabling proactive issue detection.

### Code Examples for Workers Observability

See how to leverage Workers Observability for improved performance and incident resolution

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

observability.js  searchLogs.js  sharedQuery.js  analyticsIntegration.sh 

1  2  3  4  5  6  7  8 
    
    
    export default {  async fetch(request, env) {    // Add observability    const observability = await env.OBSERVABILITY;    await observability.log('Request received');    // ...  },};

1  2  3  4  5 
    
    
    const logs = await env.OBSERVABILITY.searchLogs({  query: 'error',  filter: ' Workers:my-worker',});console.log(logs);

1  2  3  4  5 
    
    
    const sharedQuery = await env.OBSERVABILITY.saveQuery({  query: ' Workers:my-worker',  name: 'My Shared Query',});console.log(sharedQuery);

1  2  3  4  5 
    
    
    curl -X POST \  https://api.cloudflare.com/client/v4/workers/observability/analytics \  -H 'Authorization: Bearer YOUR_API_TOKEN' \  -H 'Content-Type: application/json' \  -d '{"provider": "my-analytics-provider"}'

Enable Workers Observability 

Learn how to capture high cardinality, high dimensionality telemetry data directly from Workers to understand application performance.

Search and Filter Logs 

Discover how to instantly search, query, and filter logs for fast problem resolution.

Collaborative Query Sharing 

Learn how to save and share queries with your team for increased knowledge sharing and collaborative workflows.

Analytics Provider Integration 

Integrate Workers Observability with your preferred analytics provider for a unified view of your data.

npm 

#### "

####  Over 10 million developers around the world rely on the npm Registry to download packages over 1 billion times a day. We invested in Cloudflare Workers to improve our global performance, and now with the Cloudflare Workers globally available key-value store (Cloudflare Workers KV), we can make performance improvements that used to be impossible. " 

![Laurie Voss](https://www.cloudflare.com/people/laurie-voss.png)

Laurie Voss  Co-founder and Chief Data Officer 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Workers Observability runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
