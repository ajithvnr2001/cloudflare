---
url: https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/
title: How to block AI crawlers
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:23.894580+00:00
---

# How to block AI crawlers

> Source: https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  How to block AI crawlers 

Some AI web crawlers scrape content from websites, train large language models (LLMs), and generate AI summaries without consent of the original content owners. Learn how to block them. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what AI crawlers do 
  * Understand the problems that AI crawlers create 
  * Identity the steps to identify and limit AI crawlers 



Related content  [ What is artificial intelligence (AI)? ](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[ What is a large language model (LLM)? ](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[ What is generative AI? ](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[ What is AI image generation? ](https://www.cloudflare.com/learning/ai/ai-image-generation/)[ What are artificial intelligence (AI) hallucinations? ](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)

On this page

  * How to block AI crawlers

  * What problems can AI crawlers cause?

  * What steps can content providers take to identify and limit AI crawlers?

  * How does Cloudflare help protect against AI crawlers?

  * FAQs

    * What are AI crawlers and how do they work?

    * What are the main problems AI crawlers can cause for website owners?

    * What steps can content providers take to limit AI crawlers&#39

    * How can content providers differentiate between good and bad web crawlers?

    * How does Cloudflare AI Crawl Control help website owners manage AI crawler activity?




## How to block AI crawlers

[Web crawlers](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/) (also known as web scrapers) are bots that access, download, or index content from all over the web. Some of these bots are sent out by search engines to index and categorize content on the web. Other bots might be malicious, sent to scrape and download content without permission from the website’s owner.

Artificial intelligence (AI) crawlers are a type of web crawler that use the content they scrape to train [large language models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/) or contribute to the responses those models generate.

AI crawlers operate similarly to traditional search engine crawlers in that they index information and use it to answer user queries. However, aspects of their functionality can cause problems for website owners. Understanding these problems is the first step in regaining control over original content.

## What problems can AI crawlers cause?

AI crawlers can create several problems for content publishers. They might:

\- **Ignore site policies that protect content:** As AI crawlers send [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) requests to download the site’s content, they are expected to announce themselves to the site, then parse content, text, links, metadata, and tags. They are supposed to adhere to the site’s policies, its [robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/) file’s protocols, and general site guidelines. However, many AI crawlers simply ignore a specific site’s set of rules and regulations and take whatever they can find, with or without permission.

\- **Steal intellectual property (IP):** AI crawlers and their LLMs might republish original content as AI-summarized content, without giving proper credit. Crawlers and LLMs might also indiscriminately combine content from multiple sites, over- or underemphasizing some content without properly evaluating accuracy or importance of certain ideas.

\- **Reduce visitors for original content:** Though AI-generated summaries might contain links to original websites, searchers are less likely to visit those sites when they can access summarized information. As a result, website owners experience reduced traffic and diminished ad-based revenue.

\- **Introduce biases and generate inaccurate information:** AI crawling can amplify existing biases and purposeful misinformation included within scraped data, without sufficiently evaluating that information before presenting AI-generated summaries. AI models are also prone to “[hallucinations](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/),” where the AI model basically makes up information it’s missing.

\- [Degrade site performance](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)**:** When bots repeatedly scrape a website, they can slow down its servers, increase page load times, and raise bandwidth costs.

## What steps can content providers take to identify and limit AI crawlers?

The first step in managing AI crawling activity is to get a better understanding — and better visibility — into that activity. Understanding which crawlers are accessing your site, how often they’re doing it, and how many referrals they are sending will help you define the rest of your strategy.

Next, website owners can implement a multi-tiered strategy to allow the crawlers they want and block the rest. These tactics include:

\- **Updating their robots.txt file** to restrict AI crawlers’ access to certain content. Keep in mind, though, that some crawlers might continue to ignore the file and its instructions.

\- **Using meta tags** to block AI crawlers from using all or specific parts of their site for training LLMs.

\- **Distinguishing humans from bots** to limit bots without slowing humans. Though websites have used [CAPTCHA](https://www.cloudflare.com/learning/bots/how-captchas-work/) tests in the past to prove that users are human, more advanced technologies, such as [Cloudflare Turnstile](https://www.cloudflare.com/application-services/products/turnstile/), can verify human users while reducing user frustration. This is an excellent way to limit AI crawlers that are ignoring a robots.txt file’s instructions.

\- **Separating good bots from bad bots** so you can continue to benefit from good ones. Modern [bot management solutions](https://www.cloudflare.com/application-services/products/bot-management/) can help you block malicious bots while allowing others to access your site.

\- **Employing rate limiting** through a [web application firewall (WAF)](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/) solution to block or slow AI crawlers from excessive attempts to access certain content.

\- **Deploying a WAF** to exclude certain known AI crawler IP addresses from accessing your site.

\- **Trapping misbehaving crawlers** using a tool such as [Cloudflare’s AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/), which feeds a jumble of nonsensical content and a maze of links only to AI bots that have been identified as ignoring the site’s robots.txt file.

\- **Blocking crawlers by default** to start with a clean slate. When launching a new website, you might choose to block all crawlers at first. You can then implement capabilities for identifying crawlers, monitoring their behavior, and selecting which are allowed to crawl your site, with certain restrictions.

## How does Cloudflare help protect against AI crawlers?

[Cloudflare AI Crawl Control](https://www.cloudflare.com/ai-crawl-control/) helps web content owners regain control over AI crawlers. Cloudflare sits in front of around 20% of all web properties, giving it deep insight into all kinds of crawler activity. This visibility enables content owners to use AI Crawl Control to:

\- **Understand AI crawling patterns on their web properties** , on a per-crawler, per-domain, or per-page basis

\- **Manage crawler activity** via block or allow rules

\- **Request payment from AI crawlers on a per-crawl basis** , either via [customizable HTTP 402 responses](https://blog.cloudflare.com/introducing-ai-crawl-control/#using-http-402-to-help-publishers-license-content-to-ai-crawlers) or a Cloudflare-built [pay per crawl system](https://blog.cloudflare.com/introducing-pay-per-crawl/)

Click here to [start for free](https://dash.cloudflare.com/sign-up).

## FAQs

#### What are AI crawlers and how do they work?

AI crawlers are a type of web crawler (or web scraper) that access, download, and index content from the Internet. They use scraped content to train large language models (LLMs) or contribute to the responses those models generate.

#### What are the main problems AI crawlers can cause for website owners?

AI crawlers might ignore site policies (like those found in the robots.txt file), steal intellectual property (IP), reduce visitors for original content, degrade site performance, introduce biases, and generate inaccurate information.

#### What steps can content providers take to limit AI crawlers' access to their sites?

Content providers can implement a multi-tiered strategy, which includes updating their robots.txt file, using meta tags to block crawlers from some parts of a site, distinguishing humans from bots, employing rate limiting, and trapping misbehaving crawlers.

#### How can content providers differentiate between good and bad web crawlers?

Content providers can use modern bot management solutions to help block malicious bots while allowing beneficial crawlers to access their site. Additionally, they can start by blocking all crawlers by default on a new website.

#### How does Cloudflare AI Crawl Control help website owners manage AI crawler activity?

Cloudflare AI Crawl Control helps content owners understand crawling patterns, manage crawler activity, and request payment from AI crawler owners.
