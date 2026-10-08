---
url: https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/
title: What are artificial intelligence (AI) hallucinations?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:43.110796+00:00
---

# What are artificial intelligence (AI) hallucinations?

> Source: https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  What are artificial intelligence (AI) hallucinations? 

AI hallucinations are incorrect or false responses given by generative AI models. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define, and provide examples of, AI hallucinations 
  * Describe some of the causes of AI hallucinations 
  * Outline steps for preventing AI hallucinations 



Related content  [ What is artificial intelligence (AI)? ](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[ What is generative AI? ](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[ What is a large language model (LLM)? ](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[ What is a vector database? ](https://www.cloudflare.com/learning/ai/what-is-vector-database/)[ What is low-rank adaptation (LoRA)? ](https://www.cloudflare.com/learning/ai/what-is-lora/)

On this page

  * What are artificial intelligence hallucinations?

  * How does generative AI work?

  * What causes AI to hallucinate?

  * How can AI developers prevent AI hallucinations?

  * FAQs

    * What are AI hallucinations?

    * What causes an AI to hallucinate?

    * How can developers prevent AI hallucinations?

    * What is an example of an AI hallucination?

    * What is overfitting?




## What are artificial intelligence (AI) hallucinations?

[Artificial intelligence (AI)](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) hallucinations are falsehoods or inaccuracies in the output of a [generative AI](https://www.cloudflare.com/learning/ai/what-is-generative-ai/) model. Often these errors are hidden within content that appears logical or is otherwise correct. As usage of generative AI and [large language models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/) has become more widespread, many cases of AI hallucinations have been observed.

The term "hallucination" is metaphorical — AI models do not actually suffer from delusions as a mentally unwell human might. Instead they produce unexpected outputs that do not correspond to reality in response to prompts. They may misidentify patterns, misunderstand context, or draw from limited or biased data to get those unexpected outputs.

Some documented examples of AI hallucinations include:

  * An AI model was prompted to write about Tesla's quarterly results and produced a coherent article but with [false financial information](https://www.fastcompany.com/90819887/how-to-trick-openai-chat-gpt)

  * A lawyer used an LLM to produce supporting material in a legal case, but the LLM generated references to other legal cases [that did not exist](https://www.forbes.com/sites/mollybohannon/2023/06/08/lawyer-used-chatgpt-in-court-and-cited-fake-cases-a-judge-is-considering-sanctions/)

  * Google's Gemini image generation tool regularly produced [historically inaccurate images](https://www.cnet.com/tech/computing/ai-and-you-googles-gemini-embarrassing-images-vcs-and-ais-magical-abundance/) for a period of time in 2024




While AI has a number of use cases and real-world applications, in many cases, AI models' tendency to hallucinate means they cannot be entirely relied upon without human oversight.

## How does generative AI work?

All AI models are made up of a combination of training data and an algorithm. An algorithm, in the context of AI, is a set of rules that lay out how a computer program should weight or value certain attributes. AI algorithms contain billions of parameters — the rules on how attributes should be valued.

Generative AI needs training data because it learns by being fed millions (or billions, or trillions) of examples. From these examples, generative AI models learn to identify relationships between items in a data set — typically by using [vector databases](https://www.cloudflare.com/learning/ai/what-is-vector-database/) that store data as vectors, enabling the models to quantify and measure the relationships between data items. (A "vector" is a numerical representation of different data types, including non-mathematical types like words or images.)

Once the model has been trained, it keeps refining its outputs based on the prompts it receives. Its developers will also fine-tune the model for more specific uses, continuing to change the parameters of the algorithm, or using methods like [low-rank adaptation (LoRA)](https://www.cloudflare.com/learning/ai/what-is-lora/) to quickly adjust the model to a new use.

Put together, the result is a model that can respond to prompts from humans by generating text or images based on the samples it has seen.

However, human prompts can vary greatly in complexity and cause unexpected behavior by the model, since it is impossible to prepare it for every possible prompt. And, the model may misunderstand or misinterpret the relationships between concepts and items even after extensive training and fine-tuning. Unexpected prompts and misperceptions of patterns can lead to AI hallucinations.

## What causes AI to hallucinate?

**Sources of training data:** It is hard to vet training data because AI models need so much that a human cannot review all of it. Unreviewed training data may be incorrect or weighted too heavily in a certain direction. Imagine an AI model that is trained to write greeting cards, but its training data set ends up containing mostly birthday cards, unbeknownst to its developers. As a result, it might generate happy or funny messages in inappropriate contexts, such as when prompted to write a "Get well soon" card.

**Inherent limits of generative AI design:** AI models use probability to "predict" which words or visual elements are likely to appear together. Statistical analysis can help a computer create plausible-seeming content — content that has a high probability of being understood by humans. But statistical analysis is a mathematical process that may miss some of the nuances of language and meaning, resulting in hallucinations.

**Lack of direct experience of the physical world:** Today's AI programs are not able to detect whether something is "true" or "false" in an external reality. While a human could, for example, conduct experiments to determine if a scientific principle is true or false, AI currently can only train itself on preexisting content, not directly on the physical universe. It therefore struggles to tell the difference between accurate and inaccurate data, especially in its own responses.

**Struggle to understand context:** AI only looks at literal data and may not understand cultural or emotional context, leading to irrelevant responses and AI hallucinations. Satire, for example, may confuse AI (even humans often confuse satire with fact).

**Bias:** The training data used may lead to built-in bias if the data set is not broad enough. Bias can simply skew AI models towards giving certain kinds of answers, or it can even lead to promoting racial or gender stereotypes.

**Attacks on the model:** Malicious persons can use prompt injection attacks to alter the way generative AI models perceive prompts and produce results. A highly public example occurred in [2016](https://www.bbc.com/news/technology-35890188), when Microsoft launched a chatbot, Tay, that within a day started generating racist and sexist content due to Twitter (now X) users feeding it information that distorted its responses. AI models have become more sophisticated since then but are still [vulnerable](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/) to such attacks.

**Overfitting:** If an AI model is trained too much on its initial training data set, it can lose the ability to generalize, detect trends, or draw accurate conclusions from new data. It may also detect patterns in its training data that are not actually significant, leading to errors that are not apparent until it is fed new data. These scenarios are called "overfitting": the models fit too closely with their training data. As an example of overfitting, during the COVID-19 pandemic, AI models [trained on scans of COVID patients](https://www.technologyreview.com/2021/07/30/1030329/machine-learning-ai-failed-covid-hospital-diagnosis-pandemic/) in hospitals started picking up on the text font that the different hospitals used, and treating the font as a predictor of COVID diagnosis. For generative AI models, overfitting can lead to hallucinations.

## How can AI developers prevent AI hallucinations?

While developers may not be able to eliminate AI hallucinations completely, there are concrete steps they can take to make hallucinations and other inaccuracies less likely.

  * **More data and better data:** Large data sets from a range of sources can help eliminate bias and help models learn to detect trends and patterns in a wider variety of data.

  * **Avoid overfitting:** Developers should try not to train an AI model too much on one data set.

  * **Extensive testing:** AI models should be tested in a range of contexts and with unexpected prompts.

  * **Using models designed for the use case:** An LLM chatbot, for instance, may not be well-suited for answering factual queries about medical research.

  * **Continued refinement:** Even the most fine-tuned model is likely to have blind spots. AI models should continue to learn from the prompts they receive (with validation in place to help prevent prompt injection attacks).

  * **Putting up guardrails for generative AI chatbots:** A [retrieval augmented generation (RAG)](https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-rag/) chatbot that has access to company-specific data to enhance responses could still hallucinate. Developers can implement guardrails, such as instructing the chatbot to return "I do not have enough information to answer that" when it cannot find the answer, instead of making one up.




Learn how [Cloudflare for AI](https://ai.cloudflare.com/) helps developers build and run AI models from anywhere in the world. And discover how [Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/) enables developers to generate and store embeddings in a globally distributed vector database.

## FAQs

#### What are AI hallucinations?

AI hallucinations are incorrect or false responses given by generative AI (GenAI) models. These errors are sometimes hidden within content that otherwise seems correct. The term is a metaphor; the AI is not experiencing delusions but is producing unexpected outputs that do not align with reality.

#### What causes an AI to hallucinate?

Several factors can cause AI hallucinations, including issues with inaccurate or biased training data, a model's inability to understand real-world context, the inherent limitations of the statistical analysis GenAI uses, and being trained too heavily on a single data set — this last condition is known as "overfitting."

#### How can developers prevent AI hallucinations?

While eliminating hallucinations completely may not be possible, developers can take several steps to reduce their likelihood. These include using larger and more diverse datasets, avoiding overfitting the model to a single dataset, and conducting extensive testing with a wide range of prompts. It is also important to use models that are specifically designed for the intended use case and to implement guardrails, such as instructing a chatbot to state when it does not have enough information to answer a question.

#### What is an example of an AI hallucination?

Many people have asked GenAI models to write papers or legal briefs for them, only to find that the model has included references to sources or cases that do not exist. AI image generator users have found that models sometimes do not produce accurate images in response to their first few prompts — including too many fingers on a person's hand, for example.

#### What is overfitting?

Overfitting is a case in which an AI model has been trained too heavily on a single data set, causing misinterpretations or inaccuracies when the model is presented with new data. Developers can avoid overfitting by training their models on a broad base of sample data from a range of sources.
