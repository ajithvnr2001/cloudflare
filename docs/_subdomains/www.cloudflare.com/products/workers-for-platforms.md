---
url: https://www.cloudflare.com/products/workers-for-platforms/
title: Workers for Platforms - Programmable Solutions
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:07.522722+00:00
---

# Workers for Platforms - Programmable Solutions

> Source: https://www.cloudflare.com/products/workers-for-platforms/

Workers for Platforms 

## Make your platform programmable

### Workers for Platforms provides a managed execution environment where customers deploy and run code on Cloudflare’s global network. This enables customization at scale, empowering customers to build logic, automation, and applications.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

**Effortless Scalability**

No dedicated infrastructure or teams are needed for customer code execution. Workers for Platforms scales automatically on demand.

**Customer Empowerment**

Customers can customize experiences, trigger event-based actions, or extend your platform without needing your engineers to write code.

**Secure Code Execution**

Customer code runs in an isolated environment with built-in controls, eliminating security and compliance risks.

### Workers for Platforms Architecture

A managed environment for custom code on Cloudflare's global network

Faster

Slower

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Workers for Platforms`

####  You can use Workers for Platforms to: 

See real-world examples of Cloudflare Workers for Platforms 

[ Start with Workers for Platforms  ](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/)

Full-Stack Applications 

Extend static sites into full-stack applications with databases, KV-namespaces, and object storage, all within a managed execution environment.

Personalized Experiences 

Enable customers to tailor sites with custom logic, leveraging Cloudflare’s global network for deployment and execution.

Custom Integrations 

Extend platform capabilities with custom integrations that scale on demand, without the need for extensive infrastructure.

Event-Driven Automation 

Empower customers to automate tasks based on events, within a secure, isolated environment for code execution.

### Workers for Platforms Code Examples

Discover how to customize, empower customers, and build applications with Workers for Platforms.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

dispatch.ts  curl  curl 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27 
    
    
    export default {export default {  async fetch(request, env) {    // Get the user Worker name from the URL path    const url = new URL(request.url);    const workerName = url.pathname.split("/")[1];
        // Fetch the user Worker from the dispatch namespace    const userWorker = env.DISPATCHER.get(workerName);
        // Forward the request to the user Worker    return userWorker.fetch(request);  },};    await env.KV.put('KEY', 'VALUE');    const value = await env.KV.get('KEY');    const allKeys = await env.KV.list();    await env.KV.delete('KEY');
        return new Response(      JSON.stringify({        value: value,        allKeys: allKeys,      }),    );  },};

01  02  03  04  05  06  07  08  09  10  11 
    
    
    cat > worker.mjs << 'EOF'export default {  async fetch(request, env, ctx) {    return new Response("Hello from user Worker!");  },};EOFcurl -X PUT "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$NAMESPACE_NAME/scripts/$SCRIPT_NAME" \  -H "Authorization: Bearer $API_TOKEN" \  -F 'metadata={"main_module": "worker.mjs"};type=application/json' \  -F 'worker.mjs=@worker.mjs;type=application/javascript+module'

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15 
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$NAMESPACE_NAME/scripts/$SCRIPT_NAME/assets-upload-session" \  -H "Authorization: Bearer $API_TOKEN" \  -H "Content-Type: application/json" \  -d '{    "manifest": {      "/index.html": {        "hash": "<sha256-hash-first-16-bytes-hex>",        "size": 1234      },      "/styles.css": {        "hash": "<sha256-hash-first-16-bytes-hex>",        "size": 567      }    }  }'

Use dispatch Worker to Route Requests 

Receive incoming requests and route them to the correct user Worker. 

Deploy User Worker 

Upload user Workers with an API call

Deploy Static Assets 

Deploy a user Worker with Static Assets to serve multi-tenant frontend applications

npm 

#### "

####  Over 10 million developers around the world rely on the npm Registry to download packages over 1 billion times a day. We invested in Cloudflare Workers to improve our global performance, and now with the Cloudflare Workers globally available key-value store (Cloudflare Workers KV), we can make performance improvements that used to be impossible. " 

![Laurie Voss](https://www.cloudflare.com/people/laurie-voss.png)

Laurie Voss  Co-founder and Chief Data Officer 

###  Workers for Platforms Pricing 

Deploy Workers on behalf of your customers. [View Compute pricing details](https://www.cloudflare.com/plans/#developer-platform/compute)

Component

Free

Paid

Requests 

Free

—

Paid

$0.30 / million requests 

CPU Time 

Free

—

Paid

$0.02 / million CPU ms 

Scripts Deployed 

Free

—

Paid

$0.02 / script 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Workers for Platforms run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
