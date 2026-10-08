---
url: https://www.cloudflare.com/learning/ai/mcp-client-and-server/
title: What is an MCP client?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:30.492202+00:00
---

# What is an MCP client?

> Source: https://www.cloudflare.com/learning/ai/mcp-client-and-server/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  What is an MCP client? 

An MCP client is a subprogram of an AI agent application, and it communicates with an MCP server to get information and carry out tasks. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how MCP clients and servers interact 
  * Understand MCP hosts 
  * Get started with deploying MCP clients and servers on Cloudflare 



Related content  [ What is the Model Context Protocol (MCP)? ](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[ What is an AI agent? ](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[ How to manage AI agents for business use ](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[ AI inference vs. training: What is AI inference? ](https://www.cloudflare.com/learning/ai/inference-vs-training/)[ What is retrieval-augmented generation (RAG) in AI? ](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)

On this page

  * What is an MCP client?

  * How MCP hosts work

  * What is an MCP server?

  * What are the core features of MCP servers?

  * What are the core features of MCP clients?

  * How to build an MCP server or MCP client with Cloudflare




## What is an MCP client?

A [Model Context Protocol (MCP)](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) client is a computer program that, as part of or at the direction of an [AI agent](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/), makes requests of an MCP server. The information that the MCP client obtains from the MCP server helps the AI agent make decisions or carry out tasks. Think of an MCP client as being like an assistant that can book restaurant reservations or follow up with people on behalf of their employer (the AI agent).

Suppose Acme Corp. builds an [AI](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) agent that can autonomously order furniture sets for children's bedrooms in response to simple customer prompts like, "I would like to furnish my nine-year-old's room." In order to find the best options, the AI agent would need information about what children's furniture is available, its prices, and the dimensions of the items of furniture as compared to the typical bedroom. If furniture manufacturers expose this information using MCP, the AI agent can task an MCP client with requesting the desired information directly.

MCP clients operate within MCP hosts: an MCP host is an AI agent or application. MCP is not like the [client-server model](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) on which the Internet was built, in which the "clients" were originally assumed to be discrete devices with their own [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Rather, MCP clients, hosts, and servers may all be running on the same machine, although this is not always the case.

## How MCP hosts work

An MCP host is an agentic AI application. Along with its other functions, the application contains one or more clients, which are subsidiary programs of the host. The clients help the host obtain necessary information or carry out actions to respond to end user prompts. Each client communicates directly with one MCP server. Additional server connections require instantiating more clients.

![Diagram: An end user device runs an AI application that queries an MCP client which in turn queries an MCP server](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/7bI7rJtLh89jmZaibSgiLl/e426f93616a8210d80b979c47d89dc75/image4.png)Diagram: An end user device runs an AI application that queries an MCP client which in turn queries an MCP server

 _This diagram shows how MCP clients and servers interact under the hood of a user-facing app when MCP servers are hosted on Cloudflare._

From the end user perspective, this all takes place under the hood: what they see is that they enter a prompt into an AI application, and the application replies or carries out their requests. But behind the scenes, the application relies at least partially on MCP clients and servers to get the job done.

## What is an MCP server?

An MCP server is a software program that supports the usage of MCP and makes information available to MCP clients. MCP servers take an active role in helping MCP clients fulfill their prompts, requesting more context where necessary, for instance.

MCP servers and MCP clients can run on the same physical machine. Or, they can be separate devices that connect remotely to each other over the Internet. An MCP server can be hosted on a web server (or on Cloudflare, as in the diagram above) but it does not have to be.

## What are the core features of MCP servers?

MCP servers make several features available to MCP clients. These features help MCP clients carry out their tasks.

  * **Tools:** These are functions that can be executed to help carry out prompts. An MCP server tool could be a function that calls an [API](https://www.cloudflare.com/learning/security/api/what-is-an-api/), for example.

  * **Resources:** Resources are saved sources of read-only data, such as documents, API documentation, or knowledge base articles.

  * **Prompts:** Stored, structured templates for calling specific tools and resources.




## What are the core features of MCP clients?

MCP clients also make features available to MCP servers, which can request information or get clarity from clients using these features.

  * **Elicitation:** Once a connection is initiated, the server may need more context or information in order to fulfill the client's request. The server uses the Elicitation feature to get this information from the client, which may in turn ask the user.

  * **Roots:** Clients may ask servers to focus on certain subdirectories of files to ensure the server generates a relevant response. Imagine in the example above a client asks the server to focus on `file:///home-goods/furniture/childrens-furniture/`. This way the server is less likely to provide the client with irrelevant information that does not help satisfy the user prompt, such as information about home goods in general or adult-sized beds.

  * **Sampling:** The server can send a request to the client for the AI application to complete a task.




## How to build an MCP server or MCP client with Cloudflare

Cloudflare enables developers to build, test, and deploy their own MCP clients and servers as part of developing their own AI agents. Developers can build on their local devices and [deploy to Cloudflare](https://www.cloudflare.com/developer-platform/solutions/), or build via their GitHub accounts. Deploying an MCP server or client on Cloudflare means that they can expose tools and data to agents without self-hosting and in milliseconds, on a global network that is within approximately %{OperationMilliseconds} milliseconds of %{GlobalInternetConnectedPercent}% of the Internet-connected population globally.

Authentication via [OAuth](https://www.cloudflare.com/learning/access-management/what-is-oauth/) can be built into MCP servers as well. Without [authentication](https://www.cloudflare.com/learning/access-management/what-is-authentication/), anyone can connect and use the server. With authentication, only authorized parties can do so. Authentication therefore can help keep data on an MCP server confidential and secure.

For a full tutorial on how to build a remote MCP server with Cloudflare, [see Cloudflare's MCP developer docs](https://developers.cloudflare.com/agents/guides/remote-mcp-server/).
