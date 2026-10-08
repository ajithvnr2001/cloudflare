---
url: https://www.cloudflare.com/products/browser-rendering/
title: Cloudflare Browser Rendering - Headless Browsers for AI Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:06.673262+00:00
---

# Cloudflare Browser Rendering - Headless Browsers for AI Agents

> Source: https://www.cloudflare.com/products/browser-rendering/

Browser Run 

## Headless, programmable web browsers built for AI Agents

### Give your application web browsing capabilities. Spin up a web browser in the cloud on-demand, and control it with your own code or AI-generated code. Take screenshots, extract text, run tests and automate any workflow — even ones with no API to rely on.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/browser-rendering/)

**Scale to thousands of browsers**

Instant access to a global pool of browsers with low cold-start time — ideal for screenshotting, extracting structured data, or automation at scale.

**Global by Default**

Runs on Cloudflare's global network, opening browser sessions close to users for better speed and availability.

**Easy to Integrate**

REST APIs for common actions, and works with Playwright and Puppeteer, the best-in-class browser automation libraries

### Made for Programmable Browsing

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Global Pool of Browsers

Deployed on Cloudflare's network. Enables faster cold starts and lower latency across use cases.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### REST API Support

Browser Rendering offers easy, fast setup for tasks like screenshotting, extracting content, generating PDFs, snapshotting and capturing structured data with JSON or markdown for AI.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Supports common browser libraries

Playwright & Puppeteer support. Gives developers full control when needed with standard automation tools.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### "Well-behaved" Bot Mode

Identifies itself as a bot using cryptographic signatures. Ensures compliant, ethical scraping — distinguishes Cloudflare from competitors that bypass bot protections.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

####  Ideal for Agentic Workflows 

You can use Browser Rendering to: 

[ View docs  ](https://developers.cloudflare.com/)

Create website thumbnails and social previews using the /screenshot REST API 

Generate visual previews for websites and social media sharing

Power AI agents that need browser-based automation where APIs don't exist 

Enable AI agents to interact with web pages and extract data

Generate PDFs from webpages and HTML content using the /pdf REST API 

Convert web content to PDF format for documents and reports

### Headless browsers on standby that you can use at scale without any complicated setup

Eliminate the need to manage complex browser infrastructure by running browser-based tasks like screenshots and PDF generation on Cloudflare's global network.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

curl  playwright.ts  curl 

01  02  03  04  05  06  07  08  09  10 
    
    
    curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/screenshot' \  -H 'Authorization: Bearer <apiToken>' \  -H 'Content-Type: application/json' \  -d '{    "html": "Hello World!",    "screenshotOptions": {      "omitBackground": true    }  }' \  --output "screenshot.png"

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35 
    
    
    import { launch, type BrowserWorker } from "@cloudflare/playwright";
    interface Env {  MYBROWSER: BrowserWorker;}
    export default {  async fetch(request: Request, env: Env) {    const browser = await launch(env.MYBROWSER);    const page = await browser.newPage();
        await page.goto("https://demo.playwright.dev/todomvc");
        const TODO_ITEMS = [      "buy some cheese",      "feed the cat",      "book a doctors appointment",    ];
        const newTodo = page.getByPlaceholder("What needs to be done?");    for (const item of TODO_ITEMS) {      await newTodo.fill(item);      await newTodo.press("Enter");    }
        const img = await page.screenshot();    await browser.close();
        return new Response(img, {      headers: {        "Content-Type": "image/png",      },    });  },};

1  2  3  4  5  6 
    
    
    curl -X 'POST' 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/markdown' \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer <apiToken>' \  -d '{    "url": "https://example.com"}'

Generate screenshots 

Take screenshots of web pages using the REST API or Workers bindings. [See docs](https://developers.cloudflare.com/browser-rendering/rest-api/screenshot-endpoint/).

Run Playwright for powering agentic workflows 

Use Playwright to automate complex browser interactions for AI agents. [See docs](https://developers.cloudflare.com/browser-rendering/platform/playwright/).

Retrieve webpage and generate markdown for AI consumption 

Extract content from web pages and convert to markdown format for AI processing. [See docs](https://developers.cloudflare.com/browser-rendering/rest-api/markdown-endpoint/).

Lovable 

#### "

####  We needed a reliable way to capture screenshots at scale, and Cloudflare Browser Rendering solved it with a single API call. It was remarkably easy to implement and handles all our traffic without a hiccup. " 

![Emil Ahlbäck](https://www.cloudflare.com/people/emil-ahlback.png)

Emil Ahlbäck  Founding Engineer 

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
