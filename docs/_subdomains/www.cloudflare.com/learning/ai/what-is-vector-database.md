---
url: https://www.cloudflare.com/learning/ai/what-is-vector-database/
title: What is a vector database? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:16.182468+00:00
---

# What is a vector database? | Learning Center

> Source: https://www.cloudflare.com/learning/ai/what-is-vector-database/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  What is a vector database? 

A vector database is a specialized database designed to store, index, and query high-dimensional vector embeddings efficiently. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a vector database 
  * Understand how vector search works 
  * Know when to use a vector database 



Related content  [ What are embeddings? ](https://www.cloudflare.com/learning/ai/what-are-embeddings/)

On this page

  * What is a vector database?

  * What is a vector?

  * How do vector databases work?

  * How are vector databases used?

  * What are embeddings?

  * What are the advantages of using a vector database?

  * Does Cloudflare offer the ability to use vector databases?

  * FAQs

    * What is a vector database?

    * How do vector databases work?

    * What is a "vector" in the context of AI?

    * What are the main uses for vector databases?

    * What are the advantages of using a vector database with a machine learning model?




## What is a vector database?

A vector database is a collection of data stored as mathematical representations. Vector databases make it easier for machine learning models to remember previous inputs, allowing [machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) to be used to power search, recommendations, and text generation use-cases. Data can be identified based on similarity metrics instead of exact matches, making it possible for a computer model to understand data contextually.

When one visits a shoe store, a salesperson may suggest shoes that are similar to the pair one prefers. Likewise, when shopping in an ecommerce store, the store may suggest similar items under a header like "Customers also bought..." Vector databases enable machine learning models to identify similar objects, just as the salesperson can find comparable shoes and the ecommerce store can suggest related products. (In fact, the ecommerce store may use such a machine learning model for doing so.)

To summarize, vector databases make it possible for computer programs to draw comparisons, identify relationships, and understand context. This enables the creation of advanced [artificial intelligence (AI)](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) programs like [large language models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/).

![Embeddings - Documents in vector space clustered together](https://images.ctfassets.net/slt3lc6tev37/6GPsu7uHy0hGNfHXbfQvis/bf3c0b03654368a2783168ea76858326/vector_database_clusters.png)

_In this simple vector database, the documents in the upper right are likely similar to each other._

Resource

Regain control with the Connectivity Cloud

[Learn more](https://www.cloudflare.com/connectivity-cloud/)

## What is a vector?

A vector is an array of numerical values that expresses the location of a floating point along several dimensions.

In more everyday language, a vector is a list of numbers, like: {12, 13, 19, 8, 9}. These numbers indicate a location within a space, just as a row and column number indicates a certain cell in a spreadsheet (e.g. "B7").

## How do vector databases work?

Each vector in a vector database corresponds to an object or item, whether that is a word, an image, a video, a movie, a document, or any other piece of data. These vectors are likely to be lengthy and complex, expressing the location of each object along dozens or even hundreds of dimensions.

For example, a vector database of movies may locate movies along dimensions like running time, genre, year released, parental guidance rating, number of actors in common, number of viewers in common, and so on. If these vectors are created accurately, then similar movies are likely to end up clustered together in the vector database.

## How are vector databases used?

  * **Similarity and semantic searches:** Vector databases allow applications to connect pertinent items together. Vectors that are clustered together are similar and likely relevant to each other. This can help users search for relevant information (e.g. an image search), but it also helps applications: 
    * Recommend similar products
    * Suggest songs, movies, or shows
    * Suggest images or video
  * **Machine learning and deep learning:** The ability to connect relevant items of information makes it possible to construct machine learning (and [deep learning](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)) models that can do complex cognitive tasks.
  * **Large language models (LLMs) and generative AI:** LLMs, like that on which ChatGPT and Bard are built, rely on the contextual analysis of text made possible by vector databases. By associating words, sentences, and ideas with each other, LLMs can understand natural human language and even generate text.



Sign Up

Build, deploy, and deliver trusted applications

[Get started](https://www.cloudflare.com/lp/pg-developer-platform-multi-sku/)

## What are embeddings?

[Embeddings](https://www.cloudflare.com/learning/ai/what-are-embeddings/) are vectors generated by [neural networks](https://www.cloudflare.com/learning/ai/what-is-neural-network/). A typical vector database for a deep learning model is composed of embeddings. Once a neural network is properly fine-tuned, it can generate embeddings on its own so that they do not have to be created manually. These embeddings can then be used for similarity searches, contextual analysis, generative AI, and so on, as described above.

## What are the advantages of using a vector database?

Querying a machine learning model on its own, without a vector database, is neither fast nor cost-effective. Machine learning models cannot remember anything beyond what they were trained on. They have to be the context every single time (which is how many simple [chatbots](https://www.cloudflare.com/learning/bots/what-is-a-chatbot/) work).

Passing the context of a query to the model every time is very slow, as it is likely to be a lot of data; and expensive, as data has to move around, and computing power has to be expended repeatedly having the model parse the same data. And in practice, most machine learning [APIs](https://www.cloudflare.com/learning/security/api/what-is-an-api/) are likely constrained in how much data they can accept at once anyway.

This is where a vector database comes in handy: a dataset goes through the model only once (or periodically as it changes), and the model's embeddings of that data are stored in a vector database.

This saves a tremendous amount of processing time. It makes building user-facing applications around semantic search, classification, and anomaly detection possible, because results come back within tens of milliseconds, without waiting for the model to crunch through the whole data set.

For queries, developers ask the machine learning model for a representation (embedding) of just that query. Then the embedding can be passed to the vector database, and it can return similar embeddings — which have already been run through the model. Those embeddings can then be mapped back to their original content: whether that is a URL for a page, a link to an image, or product SKUs.

To summarize: Vector databases work at scale, work quickly, and are more cost-effective than querying machine learning models without them.

## Does Cloudflare offer the ability to use vector databases?

[Vectorize](https://developers.cloudflare.com/vectorize/) is a globally distributed vector database offered by Cloudflare. Applications built on Cloudflare Workers can use Vectorize to query documents stored in [Workers KV](https://www.cloudflare.com/developer-platform/workers-kv/), images stored in [R2](https://www.cloudflare.com/developer-platform/products/r2/), or user profiles stored in [D1](https://www.cloudflare.com/developer-platform/d1/). Just as Workers allows developers to build applications without spinning up any backend infrastructure, Vectorize allows developers to build AI capabilities into their applications without constructing their own vector database infrastructure. And for creating embeddings, Cloudflare offers Workers AI.

Learn about [building AI-driven applications on Cloudflare](http://ai.cloudflare.com).

## FAQs

#### What is a vector database?

A vector database stores data as mathematical representations called vectors. It is designed to cluster related items, which enables powerful capabilities like similarity searches. Vector databases are foundational for building advanced AI applications.

#### How do vector databases work?

Each object — whether it's a word, an image, or a document — is represented by a vector, which is a list of numbers. These numbers define the object's location across many different dimensions or characteristics. The database then groups or clusters vectors that are close to each other, allowing a machine learning model to quickly find similar items.

#### What is a "vector" in the context of AI?

A vector is an array of numerical values that represents an object. Think of it as a list of coordinates, like {12, 13, 19, 8, 9}, that pinpoints the object's location within a multi-dimensional space based on its various attributes.

#### What are the main uses for vector databases?

Vector databases are primarily used for similarity and semantic searches, machine learning and deep learning, and large language models (LLMs), which power AI agents and other advanced AI applications.

#### What are the advantages of using a vector database with a machine learning model?

Using a vector database is much faster and more cost-effective than querying a machine learning model directly for every task. The model only needs to process a dataset once to create embeddings, which are then stored in the vector database. This saves a huge amount of processing time and makes it possible to build user-facing applications that return results in milliseconds.
