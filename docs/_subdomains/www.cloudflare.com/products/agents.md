---
url: https://www.cloudflare.com/products/agents/
title: Cloudflare Agents - Build Stateful AI Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:03:08.427608+00:00
---

# Cloudflare Agents - Build Stateful AI Agents

> Source: https://www.cloudflare.com/products/agents/

Editing headline…

Reading docs…

## The Agent Cloud

The Agents SDK gives you the primitives to build proactive, stateful AI agents on Cloudflare. Built-in memory, scheduling, email handling, and real-time communication: agents that don't just respond, but take initiative.

[Start building for free](https://dash.cloudflare.com/sign-up)[View docs](https://developers.cloudflare.com/agents/)

**Built-in memory**

Every agent instance has its own SQLite database. Persist conversation history, user preferences, and state without managing infrastructure.

**Proactive by design**

Agents can schedule tasks, respond to emails, handle webhooks, and send messages — not just wait for user input.

**Multiplayer by default**

Built-in WebSocket support and state synchronization. Multiple users can interact with the same agent instance in real-time.

## How Agents work

![](https://www.cloudflare.com/static/pattern.png)

##### Stateful by default

Each agent instance is a [Durable Object](https://www.cloudflare.com/product/durable-objects/) with its own SQLite database. State persists automatically across requests and hibernation cycles.

![](https://www.cloudflare.com/static/pattern.png)

##### Real-time communication

WebSockets with automatic hibernation, resumable streams, and state sync. Build chat, collaboration, or multiplayer experiences.

![](https://www.cloudflare.com/static/pattern.png)

##### Proactive scheduling

Schedule tasks with cron expressions, respond to incoming emails, or trigger actions from webhooks and queue messages.

![](https://www.cloudflare.com/static/pattern.png)

##### MCP integration

Connect to any MCP server to give agents access to external tools, APIs, and data sources.

## How Agents work

![](https://www.cloudflare.com/static/pattern.png)

##### Stateful by default

Each agent instance is a [Durable Object](https://www.cloudflare.com/product/durable-objects/) with its own SQLite database. State persists automatically across requests and hibernation cycles.

![](https://www.cloudflare.com/static/pattern.png)

##### Real-time communication

WebSockets with automatic hibernation, resumable streams, and state sync. Build chat, collaboration, or multiplayer experiences.

![](https://www.cloudflare.com/static/pattern.png)

##### Proactive scheduling

Schedule tasks with cron expressions, respond to incoming emails, or trigger actions from webhooks and queue messages.

![](https://www.cloudflare.com/static/pattern.png)

##### MCP integration

Connect to any MCP server to give agents access to external tools, APIs, and data sources.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

`Agents`

####  Agents for every use case 

Build with the Agents SDK: 

[ View docs  ](https://developers.cloudflare.com/agents/)

Proactive assistants 

Agents that send scheduled emails, monitor systems, and take action without waiting for user prompts.

Real-time collaboration 

Multiplayer chat, collaborative editing, or shared agent sessions where multiple users interact simultaneously.

Messaging and notifications 

Integrate with Slack, Discord, email, or any messaging platform. Agents can both receive and send messages proactively.

### From chat to code to orchestration

The Agents SDK handles state, streaming, and tool integration so you can focus on what your agent does.

![Background Pattern](https://www.cloudflare.com/static/pattern.png)

chat.ts  codemode.ts  workflow.ts 

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23 
    
    
    import { routeAgentRequest } from 'agents';import { AIChatAgent } from '@cloudflare/ai-chat';import { streamText, convertToModelMessages } from 'ai';import { openai } from '@ai-sdk/openai';
    export class ChatAgent extends AIChatAgent<Env> {  async onChatMessage(onFinish) {    const result = streamText({      model: openai('gpt-5'),      messages: await convertToModelMessages(this.messages),      onFinish,    });
        return result.toUIMessageStreamResponse();  }}
    export default {  async fetch(request: Request, env: Env) {    return (      (await routeAgentRequest(request, env)) ||      new Response('Not found', { status: 404 })    );  },};

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 
    
    
    import { Agent } from 'agents';import { experimental_codemode as codemode } from '@cloudflare/codemode/ai';import { streamText, convertToModelMessages } from 'ai';import { openai } from '@ai-sdk/openai';
    export class CodeModeAgent extends Agent<Env> {  async onChatMessage(onFinish) {    // Wrap tools with Code Mode - LLMs write code    // instead of making tool calls directly    const { prompt, tools } = await codemode({      prompt: 'You are a helpful assistant',      tools: this.mcp.getAITools(),      // ... additional config for proxy, loader, globalOutbound    });
        return streamText({      model: openai('gpt-5'),      system: prompt,      tools,      messages: await convertToModelMessages(this.messages),      onFinish,    });  }}

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26 
    
    
    import { AgentWorkflow } from 'agents/workflows';import type { AgentWorkflowEvent, AgentWorkflowStep } from 'agents/workflows';import type { MyAgent } from './agent';
    type TaskParams = { taskId: string; data: string };
    export class ProcessingWorkflow extends AgentWorkflow<MyAgent, TaskParams> {  async run(event: AgentWorkflowEvent<TaskParams>, step: AgentWorkflowStep) {    const { taskId, data } = event.payload;
        // Durable step with automatic retries    const result = await step.do('process-data', async () => {      return processData(data);    });
        // Report progress to Agent (broadcasts to clients)    await this.reportProgress({ step: 'process', percent: 0.5 });
        // Call Agent method via typed RPC    await this.agent.saveResult(taskId, result);
        // Report completion    await step.reportComplete(result);    return result;  }}

Resumable streaming chat 

Build chat agents with automatic stream resumption. If a client disconnects, the agent buffers and resumes seamlessly.

Let LLMs write code to call tools 

Code Mode converts MCP tools into a TypeScript API. LLMs write code instead of making tool calls — better accuracy, fewer tokens.

Durable multi-step orchestration 

Extend AgentWorkflow for tasks that need durability, retries, and progress reporting back to the Agent.

###  Powerful primitives, seamlessly integrated 

#####  Built on systems powering 20% of the Internet, the Agents SDK builds on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard. 

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
