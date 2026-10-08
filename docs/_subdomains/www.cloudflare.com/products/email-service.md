---
url: https://www.cloudflare.com/products/email-service/
title: Email Service
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:07.137890+00:00
---

# Email Service

> Source: https://www.cloudflare.com/products/email-service/

Email Service 

## Email for applications, workflows, and agents

### Cloudflare Email Service gives your applications and agents a native way to send transactional email, receive inbound messages, and automate workflows on a global network.

[ Start building for free ](https://dash.cloudflare.com/sign-up) [ View docs ](https://developers.cloudflare.com/email-routing/email-workers/)

**Built for Agents**

Give agents a real inbox and the ability to send, receive and reply without stitching together third-party tools.

**Programmable by default**

Route inbound email to Workers, process with AI, store attachments, and trigger workflows with code

**One platform, bidirectional email**

Combine email routing and email sending to handle the full email lifecycle on one platform. 

# Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required. 

[ Start building for free  ](https://dash.cloudflare.com/sign-up)[ View docs  ](https://developers.cloudflare.com/)

No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet  No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet 

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

send.ts  receive.ts  built.ts 

01  02  03  04  05  06  07  08  09  10  11  12 
    
    
    export default {  async fetch(request, env) {    await env.SEND_EMAIL.send({      to: [{ email: 'user@example.com' }],      from: { email: 'notifications@your-domain.com', name: 'Your App' },      subject: 'Your order has shipped',      text: 'Your order #1234 has shipped and is on its way.',    });
        return new Response('Email sent');  },};

01  02  03  04  05  06  07  08  09  10  11 
    
    
    export default {  async email(message, env, ctx) {    const raw = await new Response(message.raw).text();
        await env.EMAIL_QUEUE.send({      from: message.from,      to: message.to,      raw,    });  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 
    
    
    import { Agent, routeAgentEmail } from 'agents';import { createAddressBasedEmailResolver, type AgentEmail } from 'agents/email';import PostalMime from 'postal-mime';
    export class SupportAgent extends Agent {  async onEmail(email: AgentEmail) {    const raw = await email.getRaw();    const parsed = await PostalMime.parse(raw);
        const emails = this.state.emails || [];    emails.push({      from: email.from,      subject: parsed.subject,      body: parsed.text,      receivedAt: new Date().toISOString(),    });
        this.setState({ ...this.state, emails });
        await this.replyToEmail(email, {      fromName: 'Support Agent',      body: `We received your message about "${parsed.subject}".`,    });  }}
    export default {  async email(message, env) {    await routeAgentEmail(message, env, {      resolver: createAddressBasedEmailResolver('SupportAgent'),    });  },};

Send transactional emails 

Send from your appDeliver transactional and workflow email directly from Workers with a native binding.

Receive inbound email 

Route inbound email into Workers for parsing, automation, and downstream processing.

Build an email-native agent 

Use the Agents SDK to maintain state across conversations and reply from the same platform.

### A few lines of code. Global email delivery.

Use Email Sending for outbound delivery and Email Routing for inbound handling, all from the same Workers application.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Email Service`

####  Email for agents 

You can use Email Service to: 

[ View docs  ](https://developers.cloudflare.com/email-routing/email-workers/)

Send from Workers 

Trigger transactional and workflow email directly from application logic.

Route inbound email 

Receive mail on your domain and hand it to Workers for processing.

Enrich and orchestrate 

Classify content with AI, store attachments, and fan out async work with Queues.

Reply or escalate 

Respond automatically, update state, or hand off to downstream systems and humans.

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, Email Service runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
