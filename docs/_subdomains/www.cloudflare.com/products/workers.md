---
url: https://www.cloudflare.com/products/workers/
title: Cloudflare Workers - Global Serverless Functions Platform
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:06.895295+00:00
---

# Cloudflare Workers - Global Serverless Functions Platform

> Source: https://www.cloudflare.com/products/workers/

[React Flow](https://reactflow.dev)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

#  Deploy serverless functions globally in seconds 

###  Cloudflare Workers are fast, elastic, and serverless functions that scale automatically from zero to millions of requests. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up) [ View docs  ](https://developers.cloudflare.com/workers/)

**Only pay for what you use**

Pay only for execution time ([CPU time](https://developers.cloudflare.com/workers/platform/limits/#cpu-time)), not idle time spent waiting on I/O.

**Near your users, or your data**

Deploy once, run in Cloudflare's 335+ cities by default, or use [Smart Placement](https://developers.cloudflare.com/pages/functions/smart-placement/) to run near your data, to minimize end-to-end latency.

**No cold starts**

Don't keep users waiting, or spend your time on prewarming rube-goldberg machines.

**Infinite concurrency without the markup**

No need to pay for pre-provisioned concurrency. Just scale up based on demand on your big launch days, no matter how many concurrent users you get.

**First-class local development**

Workers allows you to fully test your changes locally and allow you to get in the flow, ahead of pushing your changes with [workerd](https://github.com/cloudflare/workerd), our open-source runtime.

**Write in JS, TS, Python or Rust**

Choose from a template in your language to kickstart building an app.

### Serverless architecture, from the ground up: Isolates vs. Containers

Workers are built on unique architecture called isolates. Isolates are an order of magnitude more lightweight, which means they can easily and quickly scale up and down to meet your needs.

Traditional  
architecture

Workers v8  
isolates

User code

Process overhead

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Workers`

####  You can use Workers to: 

See real-world examples of Cloudflare Workers 

[ See more  ](https://developers.cloudflare.com/workers/)

Build scalable APIs 

Handle billions of requests with automatic scaling and global deployment. No load balancers, no capacity planning, no regional configuration.

Deploy complete web applications 

Ship React, Vue, or Next.js apps integrated backend logic, databases, and storage. Full-stack development without infrastructure management.

Run serverless functions at the edge 

Handle authentication, rate limiting, routing, caching logic near your users. Reduce latency and reduce load on your server by offloading processing to Workers.

Run business logic and background jobs 

Handle webhooks, process data, and run scheduled tasks with built-in Queues, Workflows, and Cron Triggers. Reliable automation without server babysitting.

### Hello World to full-stack on a single integrated platform

Go beyond hello world by connecting to any resources you need — database, storage, browser rendering, images and more with a simple binding.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

index.ts  todos.ts  ai.ts 

01  02  03  04  05  06  07  08  09  10  11  12 
    
    
    export default {  async fetch(request, env) {    const stmt = env.DB.prepare('SELECT * FROM comments LIMIT 3');    const { results } = await stmt.all();
        return new Response(renderHtml(JSON.stringify(results, null, 2)), {      headers: {        'content-type': 'text/html',      },    });  },} satisfies ExportedHandler<Env>;

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22 
    
    
    async list(): Promise<Todo[]> {    const todos = await this.kv.get(this.todosKey, "json");    if (Array.isArray(todos)) {      todos.sort((a: Todo, b: Todo) => b.createdAt - a.createdAt);    }    return (todos || []) as Todo[];  }
    async create(text: string): Promise<Todo> {  const newTodo: Todo = {    id: crypto.randomUUID(),    text,    completed: false,    createdAt: Date.now(),  };  const todos = await this.list();  todos.push(newTodo);  await this.kv.put(this.todosKey, JSON.stringify(todos), {    expirationTtl: 300,  });  return newTodo;}

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18 
    
    
    export default {  async fetch(request, env) {    const inputs = {      prompt: 'cats vibe coding an application',    };
        const response = await env.AI.run(      '@cf/black-forest-labs/flux-1-schnell',      inputs,    );
        return new Response(response, {      headers: {        'content-type': 'image/png',      },    });  },} satisfies ExportedHandler<Env>;

Access data from D1 

Efficiently interact with your database using Cloudflare's D1 service, allowing for streamlined data retrieval and manipulation within your applications, enhancing overall performance.

Persist your to-do list with Workers KV 

Utilize Cloudflare's KV storage to manage your to-do list, ensuring data persistence and easy retrieval, while enabling you to create and manage tasks seamlessly within your application.

Generate images on the fly with AI models 

Leverage AI capabilities to dynamically generate images based on user input, integrating advanced image processing features directly into your Cloudflare Workers applications.

######  Deploy with confidence, even on Fridays 

Go from localhost to global in seconds

npxpnpxyarn-exec

$ █

######  ...or by clicking merge 

Cloudflare Workers connects directly to your Git repository, allowing you to deploy however, whenever you want

###  Go fast, or slow 

Workers enables you to instantly deploy to all 330+ cities, or gradually roll out changes to a percentage of your users. If errors spike up, roll back when you need. 

Intercom 

#### "

####  Cloudflare's toolkit is accelerating that movement even faster. Their clear documentation, purpose-built tools, and developer-first platform helped Intercom go from concept to production in under a day. " 

![Jordan Neill](https://www.cloudflare.com/people/jordan-neill.png)

Jordan Neill  SVP Engineering 

###  Workers Pricing 

Serverless functions that run everywhere, instantly. [View Compute pricing details](https://www.cloudflare.com/plans/#developer-platform/compute)

Component

Free

Paid

Requests 

Free

100k / day 

Paid

$0.30 / million requests 

CPU Time 

Free

10 ms / request 

Paid

$0.02 / million CPU ms 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Workers run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
