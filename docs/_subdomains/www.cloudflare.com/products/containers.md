---
url: https://www.cloudflare.com/products/containers/
title: Cloudflare Containers - Global Container Platform
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:06.523598+00:00
---

# Cloudflare Containers - Global Container Platform

> Source: https://www.cloudflare.com/products/containers/

[React Flow](https://reactflow.dev)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

#  Containers without orchestration headaches 

###  Run containers globally with one command. No Kubernetes, no regions. Run code written in any programming language, everywhere it's needed across Cloudflare's global network. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up) [ View docs  ](https://developers.cloudflare.com/containers/)

**Programmable**

Manage the full container lifecycle from code in your Worker. No YAML or configuration language to learn.

**Global**

Cloudflare automatically places each instance in the optimal location across our global network.

**Simple**

Deploy with one command, no devops experience required.

### Serverless meets stateful: Orchestrate Containers with Workers

Use Workers to handle requests, route traffic, and manage sessions – Containers to run any code in full isolation. Scale workloads globally without clusters, control planes, or cold starts.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Containers`

####  You can use Containers to: 

See real-world examples of Cloudflare Containers 

[ See more  ](https://developers.cloudflare.com/containers/)

Run AI generated code securely 

Execute untrusted code in a fully isolated environment per session or per user. Give your AI agents the ability to generate and run code.

Run latency sensitive services close to end users 

Deploy compute-intensive workloads that need to run near users for optimal performance. Cloudflare automatically places each instance in the optimal location across our network.

Run compute intensive workflows and background jobs 

Process data, images, videos or any content that demands multiple CPU cores, extra memory, or a specialized runtime.

Provide sandboxed dev environments 

Spin up complete development environments on-demand for testing, CI/CD, or collaborative coding.

### Create and manage containers entirely from your code

Create a container in one line of JavaScript, and forward requests to it by calling fetch()

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

sandbox.ts  index.ts  builder.ts 

1  2  3  4 
    
    
    class CodeSandbox extends Container {  defaultPort = 1337; // pass requests to this port by default, including WebSockets  sleepAfter = '15m'; // automatically sleep containers after inactivity, save $$$}

1  2  3  4  5  6  7  8 
    
    
    async fetch(request, env) {  const { sessionId } = await request.json();
      // Get a new container instance for each session, and pass requests to it  const containerInstance = getContainer(env.CODE_SANDBOX, sessionId);
      return containerInstance.fetch(request);}

01  02  03  04  05  06  07  08  09  10  11 
    
    
    class BuilderContainer extends Container {  async onStop() {    await this.env.QUEUE.send({ status: 'success', message: 'Build Complete' });  }
      async onError(err) {    await this.env.QUEUE.send({ status: 'error', message: err });  }
      async isRunning() {    return this.ctx.container.running;  }}

Define Container 

Define and customize your container with N lines of code. Bring your own images to use any language with more compute power on Workers.

Integrate With Workers 

Handle incoming requests in your Worker, and forward them to a specific container instance, spun up on demand, close to the end user.

Manage the full container lifecycle from code 

Handle errors, exit statuses, health checks, trigger cron jobs, scale up additional instances — all from code in your Worker.

Zendesk 

#### "

####  Like Zendesk, innovation is in Cloudflare’s DNA — it mirrors our beautifully simple development ethos with the connectivity cloud, a powerful, yet simple-to-implement, end-to-end solution that does all the heavy lifting, so we don’t need to. " 

![Nan Guo](https://www.cloudflare.com/people/nan-guo.png)

Nan Guo  Senior Vice President of Engineering 

###  Containers Pricing 

Run any language in secure, global containers (also applies to Sandboxes). [View Compute pricing details](https://www.cloudflare.com/plans/#developer-platform/compute)

Component

Free

Paid

Memory 

Free

25 GiB-hrs included 

Paid

$0.0000025 / GiB-second 

CPU 

Free

375 vCPU-min included 

Paid

$0.000020 / vCPU-second 

Disk 

Free

200 GB-hrs included 

Paid

$0.00000007 / GB-second 

Network Egress (NA/EU) 

Free

1 TB included 

Paid

$0.025 / GB 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Containers run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
