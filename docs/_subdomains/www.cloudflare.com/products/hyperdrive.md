---
url: https://www.cloudflare.com/products/hyperdrive/
title: Cloudflare Hyperdrive - Global Database Acceleration
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:08.336733+00:00
---

# Cloudflare Hyperdrive - Global Database Acceleration

> Source: https://www.cloudflare.com/products/hyperdrive/

[React Flow](https://reactflow.dev)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

#  Make your database feel instant, everywhere. 

###  Hyperdrive makes regional databases feel global. Connection pooling provides 3x faster queries from globally-distributed Workers, with optional caching for 100x speed and scale on repeated queries. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up) [ View docs  ](https://developers.cloudflare.com/hyperdrive/)

**Zero Migration**

Change the connection string, keep everything else

**Compatible**

Works with PostgreSQL, MySQL, and popular ORMs

**Fast**

Sub-5ms cached query results and global pooling

### Hyperdrive lets you benefit from Workers' global scale with your existing regional databases

Database connections require multiple network roundtrips to the regional database to be set up - and occupy some of the limited amount of available connections to your database. With Hyperdrive, your database connections are pooled globally to allow your Workers reuse connections across invocations. And Hyperdrive eliminates network roundtrips between Workers and regional databases by securely routing your connection over Cloudflare's network in a single request. The cherry on top? Built-in query caching with sub-5ms latency.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Hyperdrive`

####  You can use Hyperdrive to: 

See real-world examples of Cloudflare Hyperdrive 

[ See more  ](https://developers.cloudflare.com/hyperdrive/)

Build fast, global, full-stack 

Build full-stack Workers applications that feel fast everywhere by eliminating the distance penalty between global compute and regional data. No complex multi-region database setups required.

Scale read-heavy applications globally 

Handle millions of database queries without overwhelming your database. Connection pooling and query caching distribute load.

Cache database queries at the edge 

Store frequently-accessed data like user profiles, configuration settings, and routing tables at 330+ locations worldwide. Perfect for authentication, authorization, and edge decision-making.

Compatible with your existing stack 

Swap your connection string - and that's it. Build with your existing databases, drivers, ORMs and libraries. Scale your app globally, no major re-architecture required.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

index.ts  postgres.ts  mysql.ts 

01  02  03  04  05  06  07  08  09  10 
    
    
    // Use your existing drivers, ORMs and librariesimport postgres from 'postgres';
    export default {  async fetch(request, env, ctx): Promise<Response> {    // Just swap your direct connection string with Hyperdrive's connection string    const sql = postgres(env.HYPERDRIVE.connectionString);    const results = await sql`SELECT * FROM pg_tables`;  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16 
    
    
    import postgres from 'postgres';
    export default {  async fetch(request, env, ctx): Promise<Response> {    const sql = postgres(env.HYPERDRIVE.connectionString);
        try {      const results = await sql`SELECT * FROM pg_tables`;      ctx.waitUntil(sql.end());
          return Response.json(results);    } catch (e) {      return Response.json(        { error: e instanceof Error ? e.message : e },        { status: 500 },      );    }  },} satisfies ExportedHandler<Env>;

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22 
    
    
    import { createConnection } from 'mysql2/promise';
    export default {  async fetch(request, env, ctx): Promise<Response> {    const connection = await createConnection({      host: env.DB_HOST,      user: env.DB_USER,      password: env.DB_PASSWORD,      database: env.DB_NAME,      port: env.DB_PORT,      disableEval: true,    });
        const [results, fields] = await connection.query('SHOW tables;');
        return new Response(JSON.stringify({ results, fields }), {      headers: {        'Content-Type': 'application/json',        'Access-Control-Allow-Origin': '*',      },    });  },} satisfies ExportedHandler<Env>;

Connect to PostgreSQL, MySQL, or compatible databases 

Use your existing drivers, ORMs and libraries with Hyperdrive. Just swap your direct connection string with Hyperdrive's connection string.

Connect to PostgreSQL from Workers 

Connect directly to your regional PostgreSQL database using Hyperdrive's connection string. Connections are pooled globally and routed over Cloudflare's network for lower latency and higher concurrency.

Connect to MySQL from Workers 

Use familiar MySQL drivers to query your existing databases through Hyperdrive. Benefit from global pooling and edge routing without changing your query logic or schema.

Discord 

#### "

####  Knowing that we don’t have to worry about DDoS attacks against our API and gateway servers gives us the peace of mind to focus on improving our product. " 

![Stanislav Vishnevskiy](https://www.cloudflare.com/people/stanislav-vishnevskiy.png)

Stanislav Vishnevskiy  CTO 

###  Hyperdrive Pricing 

Make any database global instantly. [View Storage & Data pricing details](https://www.cloudflare.com/plans/#developer-platform/storage)

Component

Free

Paid

Queries 

Free

100,000 / day 

Paid

Free 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Hyperdrive runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
