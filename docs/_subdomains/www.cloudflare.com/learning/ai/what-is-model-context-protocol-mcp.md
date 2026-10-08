---
url: https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/
title: What is the Model Context Protocol (MCP)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:06.070468+00:00
---

# What is the Model Context Protocol (MCP)?

> Source: https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  What is the Model Context Protocol (MCP)? 

The Model Context Protocol (MCP) enables AI agents to access external tools and data sources so that they can more effectively take action. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the role of the Model Context Protocol (MCP) in agentic AI 
  * Explain how MCP works 
  * Identify security challenges in MCP 



Related content  [ What is an MCP client? ](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[ What is an AI agent? ](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[ What is a large language model (LLM)? ](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[ What is generative AI? ](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[ What is artificial intelligence (AI)? ](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)

On this page

  * What is the Model Context Protocol?

  * What are AI agents?

  * How does MCP work?

    * MCP messages

    * Remote and local MCP connections

    * Steps in an MCP connection

  * What is an MCP server?

  * Is MCP secure?

  * FAQs

    * What is the Model Context Protocol?

    * How does MCP work?

    * What are AI agents and how does MCP help them?

    * What are the different types of messages used in MCP?

    * Is the Model Context Protocol secure?

    * How does MCP relate to API security?




## What is the Model Context Protocol (MCP)?

The Model Context Protocol is a standard way to make information available to [large language models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/). Somewhat similar to the way an application programming interface (API) works, MCP offers a documented, standardized way for a computer program to integrate services from an external source. It supports [agentic AI](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/): intelligent programs that can autonomously pursue goals and take action.

MCP, essentially, allows [AI](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) programs to exceed their training. It enables them to incorporate new sources of information into their decision-making and content generation, and helps them connect to external tools.

Imagine an assistant who needs to make reservations for his boss at a restaurant. The assistant will call the restaurant's phone number, ask what times they have available, and request a table. MCP is a way to provide a "phone number" to AI agents so that they can get the information they need in order to carry out tasks.

Resource

Survey shows application modernization makes AI ROI 3x more likely

[Get the report →](https://www.cloudflare.com/resource/g/app-innovation-report/2026/)

MCP was developed by AI company Anthropic and later open-sourced. Since becoming open source in late 2024, MCP has rapidly become an industry standard, enabling more widespread use of AI agents.

## What are AI agents?

AI agents are AI programs built on top of LLMs. They use LLM information-processing capabilities to obtain data, make decisions, and take actions on behalf of human users.

MCP is one way for AI agents to find the information they need and to take actions. It helps connect AI agents to the "outside world," so to speak — the world beyond the LLM's training data. (Other methods include [API](https://www.cloudflare.com/learning/security/api/what-is-an-api/) integrations and headless browsing.)

## How does MCP work?

MCP is a [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) — an agreed-upon set of steps and instructions for use between diverse, network-connected computing devices. MCP presumes a client-server architecture, in which one entity, the client (the AI agent or a subsidiary program) sends requests to servers, which respond.

[MCP clients](https://www.cloudflare.com/learning/ai/mcp-client-and-server/) operate within MCP hosts. Clients maintain a one-to-one connection with MCP servers, but multiple clients can run from the same MCP host. Therefore MCP hosts can draw data from multiple MCP servers simultaneously. MCP servers, in turn, can use API integrations to obtain data from additional sources.

What this means is that an AI agent can use MCP to connect to multiple servers at once — however, each connection takes place independently of every other connection. Think of a team of reporters at a newspaper, all contacting sources individually but then putting their information together to produce a news item.

#### MCP messages

There are four types of messages used in MCP:

  * **Requests:** The client (contained within the host) asks for information from an MCP server.

  * **Results:** The MCP server replies with the desired information.

  * **Errors:** These are sent when the server cannot give a reply.

  * **Notifications:** One-way messages that need no response (like a public service announcement). These can be sent by either client or server.




#### Remote and local MCP connections

MCP connections can be either remote or local. Remote connections take place between AI agents and MCP servers over the Internet. Local connections take place within the same machine (MCP clients and MCP servers are software programs running separately from each other).

#### Steps in an MCP connection

There are three phases in MCP network communications:

  * **Initialization:** The client sends the first message, and in the short series of messages that follows, client and server agree on protocol versions

  * **Message exchange:** Requests, results, and notifications are exchanged

  * **Termination:** Either the client or the server ends the connection with a "close()" message




To [make MCP more secure](https://www.cloudflare.com/learning/ai/what-is-ai-security/), additional steps for [authentication](https://www.cloudflare.com/learning/access-management/what-is-authentication/) and [authorization](https://www.cloudflare.com/learning/access-management/authn-vs-authz/) may take place prior to these three phases.

## What is an MCP server?

An MCP server is a program hosted on a server or in the cloud that exposes capabilities for AI agents to use via MCP. MCP servers can provide AI agents with access to new data sets or other tools that they need. For instance, an MCP server might allow an AI agent to use an email service, so that the agent can send emails on behalf of the human user it is assisting.

## Is MCP secure?

MCP does not have authentication, authorization, or [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) natively built in, so developers have to [implement](https://www.cloudflare.com/the-net/ai-secure/) that themselves or use a service that assists with implementation.

MCP does not require the use of [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) — instead running over [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) in many implementations. It therefore can lack encryption and authentication unless developers proactively implement [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) usage. MCP, like any networking protocol, can be vulnerable to impersonation or to [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/) if TLS is not used.

Because MCP offers similar functionality to an API (external parties requesting data and services), many of the [major API security considerations](https://www.cloudflare.com/learning/security/api/owasp-api-security-top-10/) also apply to MCP implementations. Organizations making MCP servers available must ensure that confidential data is not exposed, that [resources are protected](https://www.cloudflare.com/the-net/data-protection-ai/), that excessive requests are stopped by [rate limiting](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/), that AI agents do not have too many permissions, and that inputs are validated and sanitized.

Some MCP servers offer libraries to make OAuth implementation easier. Cloudflare provides an OAuth Provider Library that implements the provider side of the OAuth 2.1 protocol, allowing you to easily add authorization to your MCP server.

Developers can use this OAuth Provider Library in three ways:

  * Integrating directly with a third-party OAuth provider

  * Integrate with their own OAuth provider, including authorization-as-a-service providers

  * A [Cloudflare Worker](https://workers.cloudflare.com/) ([serverless function](https://www.cloudflare.com/learning/serverless/what-is-serverless/) deployed on the Cloudflare network) handles authorization, while an MCP server running on Cloudflare handles the complete OAuth flow




Cloudflare makes several MCP servers available for use by developers building agentic AI. Cloudflare also enables developers to build and deploy their own MCP servers to support AI agents. [Learn how to get started with MCP on Cloudflare](https://developers.cloudflare.com/agents/model-context-protocol/authorization/).

## FAQs

#### What is the Model Context Protocol (MCP)?

The Model Context Protocol (MCP) is a standard that allows AI agents and large language models (LLMs) to connect to external tools and access new information beyond their original training data. This enables them to more effectively make decisions and take action on behalf of users.

#### How does MCP work?

MCP operates on a client-server model. An AI agent (the client) sends requests to one or more MCP servers. These servers then respond with the requested information or provide access to external tools via additional API connections.

#### What are AI agents and how does MCP help them?

AI agents are advanced AI programs, built on top of LLMs, that can autonomously pursue goals for a user. MCP is one of the primary ways these agents connect to the "outside world," allowing them to find the real-time information and tools they need to carry out tasks.

#### What are the different types of messages used in MCP?

MCP uses four message types: Requests from the client for information, Results from the server with the information, Errors when the server cannot reply, and Notifications, which are one-way messages that do not require a response.

#### Is the Model Context Protocol (MCP) secure?

MCP does not have security features like authentication, authorization, or encryption built in natively. Developers must implement these protections themselves: for instance, by using Transport Layer Security (TLS) to prevent on-path attacks.

#### How does MCP relate to API security?

Because MCP provides similar functionality to an API by allowing external parties to request data and services, many of the same security considerations apply. Organizations that make MCP servers available to external parties must protect their confidential data, implement rate limiting to stop excessive requests, and ensure AI agents do not have too many permissions.
