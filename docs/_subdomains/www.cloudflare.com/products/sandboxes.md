---
url: https://www.cloudflare.com/products/sandboxes/
title: Cloudflare Sandboxes - Secure Code Execution
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:06.786941+00:00
---

# Cloudflare Sandboxes - Secure Code Execution

> Source: https://www.cloudflare.com/products/sandboxes/

Sandboxes 

## Secure code execution for AI agents and developer tools

### Run untrusted code in isolated environments. Give your AI agents, code interpreters, and developer tools a secure place to execute code, install packages, and interact with the filesystem.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/sandbox/)

**Fully isolated**

Each sandbox runs in its own secure container. Execute AI-generated or user-submitted code with zero risk to your infrastructure.

**Fast spin-up**

Sandboxes start in milliseconds, not minutes. Execute code immediately without waiting for cold starts.

**Bring your own images**

Use standard container images with your own dependencies, tools, and runtimes. Full flexibility without lock-in.

### How Sandboxes work

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### SDK-driven control

Import `@cloudflare/sandbox` and manage the entire sandbox lifecycle from your Worker. Clone repos, execute commands, read/write files — all via simple async methods.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Built on Containers

Sandboxes run on [Cloudflare Containers](https://www.cloudflare.com/product/containers/), so you get the same global placement, automatic scaling, and pay-per-use pricing.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Real-time streaming

Stream stdout and stderr live from long-running commands. Get immediate feedback without polling.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Code interpreter built-in

Run Python or JavaScript code directly with `runCode()`. Rich outputs like charts, tables, and images are parsed automatically.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Sandboxes`

####  Secure execution for any workload 

Use Sandboxes to: 

[ View docs  ](https://developers.cloudflare.com/sandbox/)

AI agent code execution 

Give your agents a secure environment to write and run code, install packages, and interact with the filesystem.

Interactive development environments 

Spin up complete dev environments on-demand for testing, CI/CD, or collaborative coding.

Code interpreters 

Run user-submitted Python or JavaScript with automatic output parsing for charts, tables, and rich content.

### Simple APIs for complex workloads

Clone repos, execute commands, manage files, and run code — all with a few lines of TypeScript.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

index.ts  files.ts  interpreter.ts 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16 
    
    
    import { getSandbox } from '@cloudflare/sandbox';export { Sandbox } from '@cloudflare/sandbox';
    export default {  async fetch(request: Request, env: Env) {    const sandbox = getSandbox(env.Sandbox, 'test-runner');
        await sandbox.gitCheckout('https://github.com/cloudflare/agents');    const result = await sandbox.exec('npm test');
        return Response.json({      passed: result.exitCode === 0,      output: result.stdout,    });  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17 
    
    
    import { getSandbox } from '@cloudflare/sandbox';export { Sandbox } from '@cloudflare/sandbox';
    export default {  async fetch(request: Request, env: Env) {    const sandbox = getSandbox(env.Sandbox, 'file-ops');
        await sandbox.mkdir('/workspace/src', { recursive: true });    await sandbox.writeFile(      '/workspace/package.json',      JSON.stringify({        name: 'my-app',        type: 'module',      }),    );
        const result = await sandbox.readFile('/workspace/package.json');    return Response.json({ content: result.content });  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17 
    
    
    import { getSandbox } from '@cloudflare/sandbox';export { Sandbox } from '@cloudflare/sandbox';
    export default {  async fetch(request: Request, env: Env) {    const sandbox = getSandbox(env.Sandbox, 'interpreter');    const ctx = await sandbox.createCodeContext({ language: 'python' });
        const result = await sandbox.runCode(      `import mathfor i in range(5):    print(f"Step {i}: {math.pi * i:.2f}")`,      { context: ctx },    );
        return Response.json({ output: result.logs?.stdout?.join('\n') });  },};

Clone and run tests 

Clone a repository and execute shell commands with a simple SDK. Get exit codes, stdout, and stderr.

Create and manage files 

Read, write, and organize files in the sandbox filesystem. Perfect for scaffolding projects or processing uploads.

Run Python or JavaScript 

Execute code with automatic output parsing. Charts, tables, and images are extracted for you.

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

#####  Built on systems powering 20% of the Internet, Sandboxes run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
