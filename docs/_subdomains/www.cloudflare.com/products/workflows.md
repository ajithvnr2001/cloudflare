---
url: https://www.cloudflare.com/products/workflows/
title: Cloudflare Workflows - Durable Execution Engine
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:07.350979+00:00
---

# Cloudflare Workflows - Durable Execution Engine

> Source: https://www.cloudflare.com/products/workflows/

Workflows 

## Build durable workflows & multi-step applications

### Workflows is an execution engine built on Cloudflare Workers — to build applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. No need to worry about scaling, managing infrastructure, or handling durability: Workflows takes care of it for you.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/workflows/)

**Step-based**

Any logic wrapped in a step can be automatically retried and memoized for durability, without extra boilerplate or checkpoints.

**State included**

Every instance persists to its own local state: no need to set up or manage a database or control plane.

**Human-in-the-loop**

Wait on external events: webhooks, approvals, queue messages — and use them to determine the next steps in your Workflow.

### How do Workflows work?

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### State included

Every Workflow instance has its own built-in local database. State is automatically persisted and replayed: no need to run (or scale) complex database infrastructure.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Pay only for actual compute time

You are only billed while code executes. Waiting for third-party APIs or approvals costs $0, so bills are dramatically lower than duration-based platforms or self-hosted alternatives.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Just write code

Write code, test it, and use your favorite packages and API libraries — no custom DSL needed.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Human-in-the-loop

Build Workflows that can wait for events — approvals from a human, webhooks from a payment processor, or messages from a queue — with just a single line of code.

Shopify 

#### "

####  For Shopify, the real challenge is not about how many different pieces of complex technology we can use but the opposite. Cloudflare helps us find a simple way to achieve something very complex that we can scale and maintain. " 

![Duncan Davidson](https://www.cloudflare.com/people/duncan-davidson.png)

Duncan Davidson  VP of Developer Productivity 

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Workflows`

####  Ideal for resilient, multi-step systems 

You can use Workflows to: 

[ View docs  ](https://developers.cloudflare.com/workflows/)

Building AI agents 

Code review tasks, compact context, or processing data

Asynchronous tasks 

Lifecycle emails, billing jobs, and critical data processing tasks

Post-processing user-generated content 

Run inference, clean up or validate uploaded content

Improve agent performance 

Workflows can run across Cloudflare's global network, putting agent operations closer to users. 

### A durable execution engine to build multi-step applications

Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services. Workflows automatically retry, persist state, and run for minutes, hours, days, or weeks.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

steps.ts  workflow.ts  agents.ts 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18 
    
    
    export class CheckoutWorkflow extends WorkflowEntrypoint {  async run(event, step) {    const processorResponse = await step.do('submit payment', async () => {      let resp = await submitToPaymentProcessor(event.params.payment);      return await resp.json<any>();    });
        const textResponse = await step.do(      'send confirmation text',      sendConfirmation,    );
        await step.sleep('wait for feedback', '2 days');
        await step.do('send feedback email', sendFeedbackEmail);
        await step.sleep('delay before marketing', '30 days');
        await step.do('send marketing follow up', sendFollowUp);  }}

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32 
    
    
    import { listR2Files } from './listR2Files';
    interface Env {  CHUNKS_BUCKET: R2Bucket;  CHUNK_PROCESSOR: DurableObjectNamespace;}type Params = { instanceId: string };
    export class MyWorkflow extends WorkflowEntrypoint<Env, Params> {  async run(event: WorkflowEvent<Params>, step: WorkflowStep) {    const listResult = await listR2Files(this.env, event.instanceId, step);
        // Process each file from R2    for (const key of listResult.keys) {      await step.do('process file: ' + key, async () => {        return await doSomething(key, this.env.CHUNKS_BUCKET, event.instanceId);      });    }
        await step.do('restart workflow', async () => {      if (listResult.truncated) {        // There are still chunks to process        const instance = await this.env.CHUNK_PROCESSOR.get(event.instanceId);        await instance.restart();      } else {        // Reset the cursor for determinism on re-runs        await this.env.CHUNKS_BUCKET.delete('cursor/' + event.instanceId);        return 'was not truncated, done';      }    });  }}

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 
    
    
    interface Env {  MY_WORKFLOW: Workflow;  MyAgent: AgentNamespace<MyAgent>;}
    export class MyAgent extends Agent<Env> {  async onRequest(request: Request) {    let userId = request.headers.get('user-id');    // Trigger a schedule that runs a Workflow    // Pass it a payload    let { id: taskId } = await this.schedule(300, 'runWorkflow', {      id: userId,      flight: 'DL264',      date: '2025-02-23',    });  }
      async runWorkflow(data) {    let instance = await this.env.MY_WORKFLOW.create({      id: data.id,      params: data,    });
        // Schedule another task that checks the Workflow status every 5 minutes...    await this.schedule('*/5 * * * *', 'checkWorkflowStatus', {      id: instance.id,    });  }}
    export class MyWorkflow extends WorkflowEntrypoint<Env> {  async run(event: WorkflowEvent<Params>, step: WorkflowStep) {    // Your Workflow code here  }}

Step-by-step: Break your application down into discrete steps 

Break your application down into discrete steps that can be retried, persist returned state, and replayed automatically.

It's just code 

Workflows, like Workers, are just code. Import the libraries you want and get to shipping.

Call Workflows from the Agents SDK 

Use Workflows to enable agents to run background tasks as part of the Agents SDK:

###  Workflows Pricing 

Orchestrate complex multi-step processes. [View Compute pricing details](https://www.cloudflare.com/plans/#developer-platform/compute)

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

10 ms / invocation 

Paid

$0.02 / million CPU ms 

Storage 

Free

1 GB 

Paid

$0.20 / GB-month 

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
