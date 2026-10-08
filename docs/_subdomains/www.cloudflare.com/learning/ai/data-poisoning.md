---
url: https://www.cloudflare.com/learning/ai/data-poisoning/
title: What is AI data poisoning?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:04.800694+00:00
---

# What is AI data poisoning?

> Source: https://www.cloudflare.com/learning/ai/data-poisoning/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  What is AI data poisoning? 

AI data poisoning is a deliberate attempt to introduce bias into an AI model's training data so that its outputs are skewed. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how an AI data poisoning attack works 
  * Describe the types of AI and LLM data poisoning attacks 
  * List data poisoning prevention methods 



Related content  [ What is artificial intelligence (AI)? ](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[ What is machine learning? ](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[ What is a large language model (LLM)? ](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[ AI inference vs. training: What is AI inference? ](https://www.cloudflare.com/learning/ai/inference-vs-training/)[ What are the OWASP Top 10 risks for LLMs? ](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)

On this page

  * Article Summary:

  * What is AI data poisoning?

  * How does a data poisoning attack work?

  * How do AI data poisoning attacks happen?

  * What are the two main categories of data poisoning attack?

  * What are the types of AI data poisoning attacks?

  * How to prevent data poisoning

  * FAQs

    * What is AI data poisoning?

    * How does data poisoning affect AI models?

    * What are the main types of AI data poisoning attacks?

    * What are common attack vectors for AI data poisoning?

    * What are the potential consequences of data poisoning?

    * What are some ways to prevent AI data poisoning?




## Article Summary:

  * Data poisoning involves injecting malicious information into training datasets to manipulate an AI model's behavior, compromising its accuracy, reliability, and the overall integrity of machine learning results.

  * Attackers utilize AI data poisoning to create backdoors or bias outputs, allowing them to bypass security filters or cause the system to make specific, incorrect predictions.

  * Protecting against data poisoning requires rigorous data sanitization, verifying training sources, and implementing continuous monitoring to detect and neutralize adversarial inputs before they corrupt the model.




## What is AI data poisoning?

[Artificial intelligence](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) (AI) data poisoning is when an attacker manipulates the outputs of an AI or [machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) model by changing its training data. The attacker's goal in an AI data poisoning attack is to get the model to produce biased or dangerous results during [inference](https://www.cloudflare.com/learning/ai/inference-vs-training/).

AI and machine learning* models have two primary ingredients: training data and algorithms. Think of an algorithm as being like the engine of a car, and training data as the gasoline that gives the engine something to burn: data makes an AI model go. A data poisoning attack is like if someone were to add an extra ingredient to the gasoline that makes the car drive poorly.

The potential consequences of AI data poisoning have become more severe as more companies and people begin to rely on AI in their everyday activities. A successful AI data poisoning attack can permanently alter a model's output in a way that favors the person behind the attack.

AI data poisoning is of particular concern for [large language models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/). Data poisoning is listed in the [OWASP Top 10 for LLMs](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/), and in recent years researchers have warned of data poisoning vulnerabilities affecting [healthcare](https://www.hackster.io/news/don-t-trust-doctor-llm-researchers-warn-of-medical-misinformation-data-poisoning-vulnerability-f21c25504391), [code generation](https://www.infosecurity-magazine.com/news/confusedpilot-attack-targets-ai/), and [text generation](https://www.crn.com/news/ai/2024/the-ai-danger-zone-data-poisoning-targets-llms) models.

**"Machine learning" and "artificial intelligence" are sometimes used interchangeably, although the two terms refer to slightly different sets of computational capabilities. Machine learning, however, is a type of AI.*

## How does a data poisoning attack work?

AI developers use vast amounts of data to train their models. Essentially, the training data set provides the models with examples, and the models then learn to generalize from those examples. The more examples there are in the data set, the more refined and accurate the model becomes — so long as the data is correct and relatively unbiased.

Data poisoning introduces bias on purpose to the training data set, changing the starting point for the model's algorithms so that its results come out differently than its developers originally intended.

Imagine a teacher writes a math problem on a chalkboard for her students to solve: for example, "47 * (18 + 5) = ?". The answer is 1,081. But if a student sneaks behind her back and changes "47" to "46," then the answer is no longer 1,081, but 1,058. Data poisoning attacks are like that sneaky student: if the starting data changes slightly, the answer is also changed.

## How do AI data poisoning attacks happen?

Unauthorized alterations to training data can come from a number of sources.

**Insider attack:** Someone with legitimate access to the training data can introduce bias, false data, or other alterations that corrupt outputs. These attacks are more difficult to detect and stop than attacks by an external third party without authorized access to the data.

**[Supply chain](https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/) attack:** Most AI and machine learning models rely on data sets from a variety of sources to train their models. One or more of those sources could contain "poisoned" data that affects any model using that data for training and fine-tuning models.

**Unauthorized access:** There are any number of ways that an attacker could gain access to a training data set, from using [lateral movement](https://www.cloudflare.com/learning/security/glossary/what-is-lateral-movement/) via a previous compromise, to obtaining a developer's credentials using [phishing](https://www.cloudflare.com/learning/access-management/phishing-attack/), to multiple potential attacks in between.

## What are the two main categories of data poisoning attack?

  * **Direct (or targeted) attacks:** These attacks aim to skew or alter a model's output only in response to particular queries or actions. Such an attack would leave a model otherwise unaltered, giving expected responses to almost all queries. For example, an attacker might want to trick an AI-based email security filter into allowing certain malicious URLs through, while otherwise performing as expected.

  * **Indirect (or nontargeted) attacks:** These attacks aim to affect a model's performance in general. An indirect attack may aim to simply slow down the performance of the model as a whole, or to bias it towards giving particular kinds of answers. A foreign adversary, for instance, might want to bias general-use LLMs towards giving out misinformation within a particular country for propaganda purposes.




## What are the types of AI data poisoning attacks?

There are several ways an attacker can poison an AI model's data for their own purposes. Some of the most important techniques to know include:

  * **Backdoor poisoning:** This attack introduces a hidden vulnerability into the model so that, in response to certain specific triggers known to the attacker, it behaves in an unsafe way. Backdoor poisoning is particularly dangerous because an AI model with a hidden backdoor will otherwise behave normally.

  * **Mislabeling:** An attacker can change the way data is labeled within the training data set of a model, leading the model to misidentify items after it has been trained.

  * **Data injection and manipulation:** Such an attack alters, adds to, or removes data from a data set. These attacks aim to make the AI model biased in a certain direction.

  * **Availability attack:** This attack aims to slow down or crash the model by injecting data that degrades its overall performance.




## How to prevent data poisoning

**Data validation:** Before training, data sets should be analyzed to identify malicious, suspicious, or outlier data.

**Principle of least privilege:** In other words, only those persons and systems that absolutely need access to training data should have it. The [principle of least privilege](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/) is a core tenet of a [Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) approach to security, which can help prevent lateral movement and [credential compromise](https://www.cloudflare.com/the-net/credential-stuffing/).

**Diverse data sources:** Drawing from a wider range of sources for data can help reduce the impacts of bias in a given data set.

**Monitoring and auditing:** Tracking and recording who changed training data, what was changed, and when it was changed enables developers to identify suspicious patterns, or to trace an attacker's activity after the data set has been poisoned.

**Adversarial training:** This involves training an AI model to recognize intentionally misleading inputs.

Other application defense measures like [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/) can also be applied to AI models. To prevent data poisoning and other attacks, Cloudflare offers AI Security for Apps, which can be deployed in front of LLMs to identify and block abuse before it reaches them. [Learn more about AI Security for Apps](https://www.cloudflare.com/application-services/products/ai-security-for-apps/).

## FAQs

#### What is AI data poisoning?

AI data poisoning is a deliberate attempt to bias an AI model’s training data so that it produces dangerous or inaccurate results. Someone might, for example, alter an AI model's data so that it lies to or tricks its users. AI data poisoning is of particular concern for large language models (LLMs), so it is important for AI developers to carefully [safeguard](https://www.cloudflare.com/the-net/ai-secure/) and vet their training data.

#### How does data poisoning affect AI models?

By introducing slight changes to training data, an attacker can significantly alter an AI model’s outputs — just as a math problem will lead to a different answer if the initial values change (e.g. "3 + 3 = 6" vs. "3 + 4 = 7"). A data-poisoned model will therefore perform differently from how its developers and users expect, and possibly give responses that benefit the attacker or put users at risk.

#### What are the main types of AI data poisoning attacks?

The primary data poisoning attack methods include backdoor poisoning, mislabeling, data injection, data manipulation, and availability attacks. Each type of data poisoning attack aims to bias or degrade AI model performance.

#### What are common attack vectors for AI data poisoning?

Attackers may use insider access, supply chain attacks via tainted external data, or unauthorized access to manipulate or corrupt training datasets.

#### What are the potential consequences of data poisoning?

Data poisoning can permanently alter a model’s output to favor the attacker. It can cause a model to produce propaganda or hate speech, make inaccurate recommendations, provide false data, or promote malware downloads.

#### What are some ways to prevent AI data poisoning?

To prevent AI data poisoning, [protecting collections of training data](https://www.cloudflare.com/the-net/data-protection-ai/) from unauthorized alteration is crucial. [Prevention methods](https://www.cloudflare.com/learning/ai/what-is-ai-security/) include data validation, applying the principle of least privilege, using diverse data sources, monitoring and auditing data changes, and using adversarial training to get models to recognize misleading inputs.
