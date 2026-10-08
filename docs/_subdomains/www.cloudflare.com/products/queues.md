---
url: https://www.cloudflare.com/products/queues/
title: Cloudflare Queues - Managed Message Queue Service
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:08.009946+00:00
---

# Cloudflare Queues - Managed Message Queue Service

> Source: https://www.cloudflare.com/products/queues/

Queues 

## Flexible, reliable messaging for modern applications

### Send and receive messages with asynchronous delivery from every location across Cloudflare's global network. 

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/queues/)

**Guaranteed delivery**

‘At least once’ delivery helps you balance message retention and end-to-end latency.

**Improved visibility**

See metrics on queue backlogs, consumer concurrency, and message operations.

**Cost efficiency**

Move messages and data around or outside your environment with no egress fees.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Queues`

####  Built for agents and high-performance apps 

Simplify message processing and data movement across a variety of use cases. 

[ View docs  ](https://developers.cloudflare.com/queues/)

Process customer messages 

Send, list, and acknowledge messages across multiple queues.

Simplify LLM calling 

Batch requests in order to reduce inference costs. 

Protect downstream APIs 

Queues can enforce rate limiting rules in order to preserve system availability. 

### How it all fits together

Agents on your laptop, Workers in the cloud, databases in your VPC. All addressed by private IP, all routed through one network. 

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

queue.ts  etl.ts  crawler.ts 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41 
    
    
    // Producer Worker - Send messages to queueexport default {  async fetch(request, env) {    const { searchParams } = new URL(request.url);    const message = searchParams.get('message');
        if (!message) {      return new Response('Missing message parameter', { status: 400 });    }
        // Send message to queue    await env.MY_QUEUE.send({      message: message,      timestamp: new Date().toISOString(),      userId: request.headers.get('X-User-ID'),    });
        return new Response('Message sent to queue', { status: 200 });  },};
    // Consumer Worker - Process messages from queueexport default {  async queue(batch, env, ctx) {    for (const message of batch.messages) {      try {        // Process the message        console.log('Processing message:', message.body);
            // Simulate some work        await new Promise((resolve) => setTimeout(resolve, 1000));
            // Acknowledge the message        message.ack();      } catch (error) {        console.error('Failed to process message:', error);        message.retry();      }    }  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51 
    
    
    // Data ingestion workerexport default {  async fetch(request, env) {    const data = await request.json();
        // Send data to ETL queue for processing    await env.ETL_QUEUE.send({      type: 'data_ingestion',      payload: data,      timestamp: new Date().toISOString(),      source: 'api',    });
        return new Response('Data queued for processing', { status: 200 });  },};
    // ETL processing workerexport default {  async queue(batch, env, ctx) {    for (const message of batch.messages) {      try {        const { type, payload } = message.body;
            if (type === 'data_ingestion') {          // Transform the data          const transformedData = await transformData(payload);
              // Store in data warehouse          await env.DATA_WAREHOUSE.prepare(            'INSERT INTO processed_data (data, processed_at) VALUES (?, ?)',          )            .bind(JSON.stringify(transformedData), new Date().toISOString())            .run();        }
            message.ack();      } catch (error) {        console.error('ETL processing failed:', error);        message.retry();      }    }  },};
    async function transformData(data) {  // Your data transformation logic here  return {    ...data,    processed: true,    transformedAt: new Date().toISOString(),  };}

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77 
    
    
    // URL discovery workerexport default {  async fetch(request, env) {    const { searchParams } = new URL(request.url);    const startUrl = searchParams.get('url');
        if (!startUrl) {      return new Response('Missing URL parameter', { status: 400 });    }
        // Add initial URL to crawl queue    await env.CRAWL_QUEUE.send({      url: startUrl,      depth: 0,      maxDepth: 3,    });
        return new Response('Crawling started', { status: 200 });  },};
    // Crawler workerexport default {  async queue(batch, env, ctx) {    for (const message of batch.messages) {      try {        const { url, depth, maxDepth } = message.body;
            // Fetch the page        const response = await fetch(url);        const html = await response.text();
            // Extract links        const links = extractLinks(html, url);
            // Process the page content        await processPage(url, html);
            // Add new links to queue if within depth limit        if (depth < maxDepth) {          for (const link of links) {            await env.CRAWL_QUEUE.send({              url: link,              depth: depth + 1,              maxDepth: maxDepth,            });          }        }
            message.ack();      } catch (error) {        console.error('Crawling failed:', error);        message.retry();      }    }  },};
    function extractLinks(html, baseUrl) {  // Simple link extraction logic  const linkRegex = /<a[^>]+href=["']([^"']+)["'][^>]*>/gi;  const links = [];  let match;
      while ((match = linkRegex.exec(html)) !== null) {    const href = match[1];    const absoluteUrl = new URL(href, baseUrl).toString();    links.push(absoluteUrl);  }
      return links;}
    async function processPage(url, html) {  // Your page processing logic here  console.log(`Processed page: ${url}`);}

Basic Queue Operations 

Send messages to a queue and process them asynchronously.

ETL Pipeline with Queues 

Build reliable ETL pipelines by buffering data through queues.

Web Crawler with Queues 

Build distributed web crawlers using queues to manage URL processing.

SiteGPT 

#### "

####  We use Cloudflare for everything – storage, cache, queues, and most importantly for training data and deploying the app on the edge, so I can ensure the product is reliable and fast. It's also been the most affordable option, with competitors costing more for a single day's worth of requests than Cloudflare costs in a month. " 

![Bhanu Teja Pachipulusu](https://www.cloudflare.com/people/bhanu-teja.png)

Bhanu Teja Pachipulusu  Founder 

###  Queues Pricing 

Reliable message processing. [View Storage & Data pricing details](https://www.cloudflare.com/plans/#developer-platform/storage)

Component

Free

Paid

Standard Operations 

Free

10,000 operations/day included 

Paid

$0.40 / million operations 

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Queues run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
