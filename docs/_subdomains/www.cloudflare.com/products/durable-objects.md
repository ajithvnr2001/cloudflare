---
url: https://www.cloudflare.com/products/durable-objects/
title: Cloudflare Durable Objects - Stateful Serverless Functions
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:07.051979+00:00
---

# Cloudflare Durable Objects - Stateful Serverless Functions

> Source: https://www.cloudflare.com/products/durable-objects/

[React Flow](https://reactflow.dev)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

#  Build real-time & multiplayer apps without a degree in distributed systems. 

###  Ship multiplayer systems, chat services, session stores and other coordination-heavy apps using Durable Objects. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up) [ View docs  ](https://developers.cloudflare.com/durable-objects/)

**Stateful serverless**

Durable Objects are stateful serverless functions: they run for as long as you need them, can compute in the background, and handle multiple requests concurrently.

**WebSockets included**

Every Durable Object is also a WebSocket server and client. Broadcast and coordinate state in real-time with just a few lines of code.

**Like a micro-VM**

Think of every Durable Object as a micro-VM: create thousands (or millions) of them to do work, and throw them away when you're done.

**Embedded SQL database**

Every Durable Object has a built-in, embedded SQLite database. Serverless doesn't have to be stateless.

**Schedule Work**

Every Durable Object can do work in the background, periodically poll an API, and programmatically execute code in the future with the Alarms API (it's built-in).

**@cloudflare/actors**

The @cloudflare/actors library provides a set of powerful abstractions over Durable Objects: the container to Durable Object's micro-VM.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Durable Objects`

####  The building block for real-time apps 

Power chat rooms, multiplayer sessions, collaborative docs, and live dashboards. Durable Objects run close to users, maintain consistent state, and broadcast updates instantly – no Redis clusters or orchestration required. 

[ See more  ](https://developers.cloudflare.com/durable-objects/)

Build chat systems and messaging apps 

One object per chat room handles all messages, user presence, and room state with global consistency. No Redis clusters or message queues required. [Try it!](https://github.com/cloudflare/templates/tree/main/durable-chat-template)

Create collaborative editing experiences 

One object per document coordinates real-time edits from multiple users without distributed systems expertise. Think Figma or Google Docs architecture, simplified.

Power multiplayer games and interactive experiences 

One object per game session manages player state, game logic, and real-time updates close to users. Each game room scales independently without infrastructure overhead. [Try it!](https://github.com/cloudflare/templates/tree/main/multiplayer-globe-template)

Coordinate live dashboards and real-time analytics 

Objects aggregate and push real-time data updates to connected clients for monitoring and live events. Real-time data without the coordination nightmare.

### The simplest way to build real-time systems at global scale

Durable Objects give every developer the building blocks for coordination, state, and real-time communication—without managing Redis, clusters, or distributed locks. Used by teams shipping multiplayer apps, live dashboards, and collaborative editors that just work.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

counter.ts  websocket.ts  chat.ts 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43 
    
    
    import { DurableObject } from 'cloudflare:workers';
    export default {  async fetch(request, env) {    const url = new URL(request.url);    const counterName = url.searchParams.get('name');    if (!counterName) return new Response('missing ?name', { status: 400 });
        const counterStub = env.COUNTERS.getByName(counterName);
        let count;    switch (url.pathname) {      case '/increment':        count = await counterStub.increment();        break;      case '/decrement':        count = await counterStub.decrement();        break;      case '/':        count = await counterStub.get();        break;      default:        return new Response('not found', { status: 404 });    }    return new Response(`${count}`);  },};
    export class Counter extends DurableObject {  async get() {    return (await this.ctx.storage.get('value')) ?? 0;  }  async increment(amount = 1) {    const newValue = (await this.get()) + amount;    await this.ctx.storage.put('value', newValue);    return newValue;  }  async decrement(amount = 1) {    const newValue = (await this.get()) - amount;    await this.ctx.storage.put('value', newValue);    return newValue;  }}

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20 
    
    
    import { DurableObject } from 'cloudflare:workers';
    export class WebSocketServer extends DurableObject {  async fetch() {    const webSocketPair = new WebSocketPair();    const [client, server] = Object.values(webSocketPair);    this.ctx.acceptWebSocket(server);
        return new Response(null, {      status: 101,      webSocket: client,    });  }
      async webSocketMessage(ws, message) {    ws.send(      `[Durable Object] message: ${message}, connections: ${this.ctx.getWebSockets().length}`,    );  }}

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20 
    
    
    import { DurableObject } from 'cloudflare:workers';
    export class UserChatHistory extends DurableObject {  sql: SqlStorage;  constructor(ctx: DurableObjectState, env: Env) {    super(ctx, env);    this.sql = ctx.storage.sql;
        this.sql.exec(`CREATE TABLE IF NOT EXISTS history(      roomId    INTEGER PRIMARY KEY,      roomName  TEXT,      message   TEXT,      timestamp TIMESTAMP)`);  }
      async getHistory(roomId: string) {    return this.sql      .exec('SELECT * FROM history WHERE roomId = ?;', roomId)      .one();  }}

Global co-ordination without the infrastructure hassle 

Coordinate compute and state across thousands (or millions) of clients: route users to the same Durable Object, no matter where they are in the world.

Fan-out, fan-in 

Durable Objects can speak WebSockets: connect thousands of clients per object and create millions of objects to broadcast real time events.

An embedded SQL database in every Durable Object 

Every Durable Object has a built-in, [zero-latency SQLite database](https://blog.cloudflare.com/sqlite-in-durable-objects/): store per-user state, buffer events, and/or persist message histories without having to scale out another database.

Liveblocks 

####  Cloudflare released Durable Objects at just the right time for us. Without Cloudflare, hosting WebSocket servers might have required at least four additional people just for management. Using Durable Objects, we can provide serverless capabilities without a dedicated team. 

###  Durable Objects Pricing 

Stateful compute for real-time coordination. [View Compute pricing details](https://www.cloudflare.com/plans/#developer-platform/compute)

Component

Free

Paid

Requests 

Free

100,000 requests / day 

Paid

$0.15 / million requests 

Duration 

Free

13,000 GB-s / day 

Paid

$12.50 / million GB-s 

SQL Rows Read 

Free

50M / day 

Paid

$0.001 / million rows 

SQL Rows Written 

Free

100K / day 

Paid

$1.00 / million rows 

SQL Stored Data 

Free

5 GB 

Paid

$0.20 / GB-month 

Read Request Units (KV Storage Backend) 

Free

—

Paid

$0.20 / million rows 

Write Request Units (KV Storage Backend) 

Free

—

Paid

$1.00 / million rows 

Delete Request Units (KV Storage Backend) 

Free

—

Paid

$1.00 / million rows 

Stored Data (KV Storage Backend) 

Free

1 GB 

Paid

$0.20 / GB-month 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Durable Objects run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
