---
url: https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/
title: How to enhance AI models with RAG (retrieval-augmented generation)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:23.849456+00:00
---

# How to enhance AI models with RAG (retrieval-augmented generation)

> Source: https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  How to enhance AI models with RAG (retrieval-augmented generation) 

Well-built retrieval augmented generation (RAG) pipelines can help organizations turn dormant data into decisive business drivers. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define retrieval augmented generation (RAG) 
  * Build successful RAG pipelines 
  * Identify the best ways to measure the success of a RAG pipeline 



Related content  [ What is retrieval-augmented generation (RAG) in AI? ](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[ What is a large language model (LLM)? ](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[ What is a vector database? ](https://www.cloudflare.com/learning/ai/what-is-vector-database/)[ What are embeddings? ](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[ What is low-rank adaptation (LoRA)? ](https://www.cloudflare.com/learning/ai/what-is-lora/)

On this page

  * What is retrieval augmented generation and why is it valuable?

  * What steps are needed to build successful RAG pipelines?

    * Step 1: Conceive potential RAG use cases

    * Step 2: Identify RAG-worthy data sources internally

    * Step 3: Build a RAG pipeline

  * Should you partner with IT on RAG execution and deployment?

  * What’s the best way to measure the success of your RAG pipeline?

  * How can you simplify RAG workflow creation?

  * Why should you use RAG?

  * FAQs

    * What is retrieval-augmented generation?

    * What are the main benefits of using RAG?

    * What are the steps for building a RAG pipeline?

    * What are some examples of high-impact use cases for RAG?

    * What kind of data sources are suitable for a RAG system?

    * What are the five parts of a typical RAG workflow?

    * How can you measure the success of a RAG pipeline?

    * What is the benefit of using an embedding model in a RAG pipeline?

    * What does Cloudflare AI Search do to simplify RAG workflow creation?




## What is retrieval augmented generation (RAG) and why is it valuable?

[Retrieval augmented generation (RAG)](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/) is a technique used in the development of [artificial intelligence (AI)](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) that enhances [large language models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/) by giving them access to internal and external data sources that weren’t included in their original training — for example, third-party research, product documentation, or a business’s internal knowledge base.

Using RAG, teams can query authoritative organizational knowledge and third-party resources in [natural language](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/) to avoid interrupting colleagues or performing time-consuming searches across fragmented systems.

Because the LLM uses supplemented data at runtime, [hallucinations](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/) are less likely and everyone works from the same source of truth. The result is greater LLM accuracy courtesy of grounded, reliable information.

## What steps are needed to build successful RAG pipelines?

RAG helps businesses enhance the [AI models](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) they use, from vendors such as OpenAI or Anthropic, without the extra time, expense, and technical resources that would be required to retrain them on specific knowledge for the intended use case. Therefore, RAG democratizes LLM enhancement.

Fortunately, building RAG pipelines doesn’t require massive infrastructure or deep [machine-learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) expertise. So, getting started is easy. The simple three-part process starts with identifying use cases, selecting appropriate data sources, and creating the actual RAG pipeline.

### Step 1: Conceive potential RAG use cases

First, determine what data sources would be most helpful for teams to access using natural language prompting. Focus on high-impact friction points, including resources that teams frequently reference for answers, systems where they often encounter bottlenecks, or processes where the same questions surface repeatedly.

To find the most promising RAG use cases, ask internal teams the following questions:

\- **What common requests for institutional knowledge live in people's heads or in hard-to-access written documents?** Examples include standard operating procedures and resolutions to common problems. With the help of RAG, a self-service billing assistant could answer common user questions like, “Where can I download past invoices?”

\- **What questions are frequently escalated across teams?** Queries about evolving technical policies, for instance, probably come up often. Using RAG, a customer-facing policy assistant can explain a company’s refund policy.

\- **What files or tasks require manual and repetitive queries in multiple places, such as Confluence, SharePoint, and internal wikis?** A RAG-enabled compliance assistant could pull from HR guidelines to answer, “What training modules are required for new hires in Europe?”

\- **What formal needs or requirements must be met?** Responses to audits, request for proposals (RFPs), and compliance are common use cases. Thanks to RAG, a sales RFP assistant can pull from compliance-approved templates to generate RFP responses.

\- **What information applies to everyone?** Company training and onboarding documents are universally helpful, for instance. An interactive customer onboarding guide could leverage RAG to walk new users through training steps by retrieving the most current how-to materials.

Prioritize RAG use cases where combining generative reasoning with internal and external knowledge can solve tangible problems, reduce context-switching, eliminate repetitive tasks, and improve consistency across teams.

### Step 2: Identify RAG-worthy data sources internally

RAG systems are only as strong as the data they retrieve. Therefore, the quality, completeness, [governance](https://www.cloudflare.com/learning/privacy/what-is-data-governance/), and structure of available data sources directly impacts response quality.

RAG-worthy data checks the following boxes:

\- **It answers common questions:** Ideal sources include product FAQs, policy documentation, internal process guides, and compliance mappings.

\- **It’s accurate and maintained:** Look for documentation with clear ownership and a regular updating cadence.

\- **It’s structured enough for chunking:** Markdown files, PDFs, HTML documents, JSON files, and wikis can all be broken into logical sections. If datasets include screenshots or image-based PDFs, tools like Cloudflare [Workers AI](https://www.cloudflare.com/developer-platform/products/workers-ai/) can convert images into [vectors](https://www.cloudflare.com/learning/ai/what-is-vector-database/) that are then readable by LLMs.

Avoid data sources that introduce noise or inconsistency, including:

\- **Data in unstructured and messy formats** — for example, Slack threads or raw email chains — unless it’s cleaned, vetted, and formatted

\- **Datasets that are fluid and always changing** , like dashboards with live metrics

\- **Duplicate, conflicting, or outdated files** , which can confuse retrieval and introduce error

Work with internal stakeholders and IT to inventory, deduplicate, and assign ongoing ownership to each data source.

### Step 3: Build a RAG pipeline

Next, process and organize datasets into a structure that’s suitable for semantic retrieval. A typical RAG workflow includes five parts: ingestion, embedding, vector database storage, query retrieval, and response generation.

**1\. Ingestion**

Start by collecting relevant files and documents from shared repositories, storage buckets, or content systems. Then focus on:

  * **Chunking:** To enable precise retrieval, programmatically divide content into logical sections that create semantically coherent units (e.g., paragraphs, headings, FAQ items, and code blocks).

  * **Normalization:** Clean and standardize data across formats (e.g., PDFs to text, HTML to markdown).




\- **Metadata tagging:** Append useful metadata (e.g., owner, creation date, system) to support filtered retrieval.

**2\. Embedding**

Use an [embedding model](https://www.cloudflare.com/learning/ai/what-are-embeddings/), such as [BGE embedding models](https://developers.cloudflare.com/workers-ai/models/?tasks=Text+Embeddings), to convert each text chunk into a numerical vector that captures its semantic meaning.

**3\. Vector database storage**

Store embeddings and all associated metadata in a scalable [vector database](https://www.cloudflare.com/learning/ai/what-is-vector-database/), such as [Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/). Doing so enables efficient querying and filtering for large-scale knowledge bases.

**4\. Query retrieval**

When a user submits a prompt, the system: converts the query into a vector; searches the vector database for appropriate, semantically similar chunks; and applies filters based on metadata to fine-tune retrieval — for example, limiting access to specific information based on role or department

**5\. Response generation**

Finally, retrieved chunks are injected into the prompt as additional context before being passed to the LLM. The LLM uses this context to generate a meaningful and accurate response that’s grounded in internal and external data.

## Should you partner with IT on RAG execution and deployment?

Standing up a valuable RAG pipeline is an all-hands-on-deck effort. However, it relies on IT to: lead execution; manage infrastructure like data pipelines, vector database scaling, and access control; and integrate systems.

And yet, IT can’t own the process alone. Start by aligning cross-functional teams, including IT, subject matter experts, and business stakeholders. Together, these teams should identify use cases and trusted data sources, define content authority standards, and assign ownership to ensure datasets remain accurate and updated.

Apply [access controls](https://www.cloudflare.com/learning/access-management/what-is-access-control/) to restrict sensitive data by user role or business unit, and ensure [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) and [compliance](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/) guardrails are in place across the system.

Start with a pilot, iterate based on results, then scale across teams.

## What’s the best way to measure the success of your RAG pipeline?

Build success metrics into the process from the start to evaluate RAG system effectiveness and business value.

In particular, evaluate the system against KPIs like:

  * **Retrieval accuracy:** Are the right documents and answers surfaced?



\- **Response relevance and factuality:** Are users receiving current and trustworthy answers?

\- **Latency:** Are responses delivered in an acceptable timeframe?

\- **User adoption and satisfaction:** Are employees _actually_ using the system and gaining efficiency?

\- **Data governance:** Are [security and compliance guardrails](https://www.cloudflare.com/learning/ai/what-is-ai-security/) maintained as new sources are added?

RAG evaluation often involves human-in-the-loop validation to check accuracy. To improve RAG pipeline implementation over time, continuously solicit user feedback, analyze performance metrics on query and retrieval logs, review content hygiene, and evaluate progress against business goals.

## How can you simplify RAG workflow creation?

Manually building a RAG pipeline requires stitching together storage, vector databases, embedding models, LLMs, and custom indexing / retrieval logic, as well as maintaining the system as data changes. It takes time and collaboration, and the complexity of these tasks can pull teams away from other high-impact projects. For some organizations, this makes RAG adoption impractical despite its potential benefits.

Cloudflare [AI Search (formerly AutoRAG)](https://developers.cloudflare.com/ai-search/) can help.

AI Search is a fully managed RAG pipeline built on Cloudflare’s developer platform. In just four steps, users can connect data sources like corporate websites, ecommerce product catalogs, and developer documentation. AI Search handles ingestion, markdown conversion, chunking, embedding, and storage in Vectorize. It then performs semantic retrieval and generates responses with Workers AI.

AI Search removes the heavy infrastructure burden of building RAG pipelines by automating scale, storage, and AI inference while ensuring internal data sources are accessed securely and appropriately within RAG systems. Plus, AI Search continuously reindexes data in the background, keeping answers fresh as internal sources are updated.

## Why should you use RAG?

Your organization’s data is a massive strategic asset. Building a secure RAG pipeline makes this data accessible to team members and clients by augmenting corporate LLMs with the unique guidelines, processes, and knowledge base that differentiate your enterprise and market.

Simply put: RAG enhances popular models with internal company knowledge and approved third-party resources for real-time AI advantage.

Whether building manually or with AI Search, begin with the right use cases, curate high-quality data, and collaborate to deliver fast, accurate, grounded answers.

Ready to get started? Build your own internal RAG in [four easy steps](https://developers.cloudflare.com/ai-search/).

## FAQs

#### What is retrieval-augmented generation (RAG)?

Retrieval-augmented generation (RAG) is a method for improving large language models (LLMs) by providing them with access to internal and external data sources that were not part of their original training.

#### What are the main benefits of using RAG?

RAG allows teams to query organizational knowledge and third-party resources using natural language, which can help avoid interruptions to colleagues and reduce the time spent on manual searches. It also democratizes the enhancement of AI models from vendors like OpenAI or Anthropic, without the need for the time, expense, or technical resources required for full retraining.

#### What are the steps for building a RAG pipeline?

The steps for building a RAG pipeline are: conceiving potential use cases, identifying appropriate data sources, and building the actual RAG pipeline. Pipeline construction involves ingestion of content, using an embedding model to convert text into vectors, storing embeddings and metadata in a vector database, enabling query retrieval, and facilitating response generation.

#### What are some examples of high-impact use cases for RAG?

High-impact RAG use cases include creating: a self-service billing assistant, a customer-facing policy assistant, a compliance assistant for HR guidelines, a sales RFP assistant, and an interactive customer onboarding guide. These use cases can help solve tangible problems, reduce repetitive tasks, and improve consistency across teams.

#### What kind of data sources are suitable for a RAG system?

RAG-worthy data sources should be accurate, regularly maintained, and structured enough to be broken into logical sections, such as Markdown files, PDFs, HTML documents, or JSON files. They should also answer common questions, like product FAQs or internal process guides.

#### What are the five parts of a typical RAG workflow?

A typical RAG workflow consists of five parts: ingestion, embedding, vector database storage, query retrieval, and response generation.

#### How can you measure the success of a RAG pipeline?

The success of a RAG pipeline can be measured using key performance indicators (KPIs) such as retrieval accuracy, response relevance and factuality, latency, user adoption and satisfaction, and data governance. Continuous user feedback and performance metric analysis can help improve the implementation over time.

#### What is the benefit of using an embedding model in a RAG pipeline?

An embedding model, such as BGE embedding models, converts text chunks into numerical vectors that capture their semantic meaning. These vectors are then stored in a vector database for efficient querying and filtering.

#### What does Cloudflare AI Search do to simplify RAG workflow creation?

Cloudflare AI Search is a fully managed RAG pipeline that automates ingestion, chunking, embedding, and storage in Vectorize. It also handles semantic retrieval and response generation with Workers AI, which removes the need for manual infrastructure management.
