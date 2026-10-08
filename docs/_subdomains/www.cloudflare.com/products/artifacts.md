---
url: https://www.cloudflare.com/products/artifacts/
title: Cloudflare Artifacts - Versioned Git-compatible storage for agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:06.133749+00:00
---

# Cloudflare Artifacts - Versioned Git-compatible storage for agents

> Source: https://www.cloudflare.com/products/artifacts/

Artifacts 

## Versioned storage that speaks Git

### Give your agents, developers, and automations a home for code and data. Artifacts is Git-compatible storage built for scale: create tens of millions of repos, fork from any remote, and hand off a URL to any Git client.

[ Start building ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/artifacts/)

**Git compatible**

Agents know git. Every repository can act as a git repo, allowing agents to interact with Artifacts the way they know best: using the git CLI.

**Programmable**

Create repos, new branches, commit, diff and search. All programmatically, without waiting.

**Tens of millions of repos**

Create a thousand, a million or ten million repos: one for every agent, for every upstream branch, or every user. No need to plan ahead.

### A few lines of code. Millions of repos.

Create, import, fork, and manage access: the full repo lifecycle from a Workers binding.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

index.ts  fork.ts  api.sh 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17 
    
    
    import type { Artifacts } from 'cloudflare:workers';
    interface Env {  ARTIFACTS: Artifacts;}
    export default {  async fetch(request: Request, env: Env) {    // Create a repo — returns the remote URL and an initial write token    const { remote, token, repo } = await env.ARTIFACTS.create('my-project');
        // Issue a scoped read token, valid for 1 hour    const readToken = await repo.createToken('read', 3600);
        return Response.json({ remote, token: readToken.plaintext });  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22 
    
    
    import type { Artifacts } from 'cloudflare:workers';
    interface Env {  ARTIFACTS: Artifacts;}
    export default {  async fetch(request: Request, env: Env) {    // Import from GitHub    const { repo } = await env.ARTIFACTS.import('workers-sdk', {      url: 'https://github.com/cloudflare/workers-sdk',      branch: 'main',    });
        // Fork to an isolated, read-only copy    const { remote, token } = await repo.fork('workers-sdk-review', {      readOnly: true,    });
        return Response.json({ remote, token });  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17 
    
    
    # Create a repocurl -X POST "https://artifacts.cloudflare.dev/v1/api/namespaces/default/repos" \  -H "Authorization: Bearer $JWT" \  -H "Content-Type: application/json" \  -d '{ "name": "my-project" }'
    # Issue a scoped read token, valid for 1 hourcurl -X POST "https://artifacts.cloudflare.dev/v1/api/namespaces/default/tokens" \  -H "Authorization: Bearer $JWT" \  -H "Content-Type: application/json" \  -d '{ "repo": "my-project", "scope": "read", "ttl": 3600 }'
    # Fork to an isolated copycurl -X POST "https://artifacts.cloudflare.dev/v1/api/namespaces/default/repos/my-project/fork" \  -H "Authorization: Bearer $JWT" \  -H "Content-Type: application/json" \  -d '{ "name": "my-project-fork" }'

Create a repo and issue tokens 

Declare an `artifacts` binding in `wrangler.jsonc`. Call `create()` to return the remote URL and auth token, and issue scoped tokens for any repo.

Import from GitHub and fork 

Import any GitHub repo by owner/name. Fork to an isolated copy for safe agent workspaces or review environments.

Manage repos over HTTP 

Every binding operation has a REST equivalent. Use the REST API from any language or environment that can make HTTP requests.

### How Artifacts work

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Create a repo in one line of code

Create one. Create one million. One API that scales.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Fork from anywhere

Fork from another repo: in Artifacts, from GitHub, or any other git-compatible upstream.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Hand off to any Git client

`create()` and `import()` return a `remote` URL directly. Pass it to your agent, a CLI, an IDE, or another Worker. Standard `git clone` just works.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

### Manage access with scoped tokens

Create short-lived tokens for any repo: `read` for safe inspection, `write` for agents that need to commit. Tokens expire automatically.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Artifacts`

####  One repo per agent. One per user. One per everything. 

See real-world examples of Cloudflare Artifacts 

[ View docs  ](https://developers.cloudflare.com/artifacts/)

Agent workspaces 

Give coding agents isolated, versioned environments. Fork from a shared baseline, let the agent commit its work, then diff against the original.

Config versioning 

Track configuration changes across deploys with full Git history, branching, and rollback. Every change is attributed and reversible.

Platform-managed repos 

Build Git-backed features for your users: notebooks, IaC, generated content. No Git infrastructure to run.

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Artifacts run on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
