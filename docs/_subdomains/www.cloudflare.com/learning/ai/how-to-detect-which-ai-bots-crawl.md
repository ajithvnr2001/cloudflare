---
url: https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/
title: How to detect AI crawlers
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:25.455504+00:00
---

# How to detect AI crawlers

> Source: https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  How to detect AI crawlers 

If a website sees unusual activity, it may be because of AI crawler bots. Reviewing a website's log files can help determine which AI bots are crawling a website. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe why AI bots crawl websites 
  * Understand how to detect bots and AI crawlers in log files via user-agent strings 
  * List the major AI crawler bots and what they do 



Related content  [ How to block AI crawlers ](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[ How to prevent web scraping ](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[ What is generative AI? ](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[ What is a large language model (LLM)? ](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[ What is an AI agent? ](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)

On this page

  * How to detect AI crawlers

  * What do AI crawler bots do?

  * How to track AI crawler activity via user-agent strings

  * Which AI bots are crawling your site?

    * List of common AI web crawlers

  * How to block bots and AI crawlers

  * What about unverified AI crawler bots?

  * FAQs

    * What is the primary purpose of AI crawler bots?

    * How do AI crawlers differ from traditional search engine crawlers?

    * Which AI crawlers currently send the most requests across the Internet?

    * What is the most common method for requesting that bots stay off a website?

    * How does Cloudflare AI Crawl Control assist with bot management?




## How to detect AI crawlers

[Bots](https://www.cloudflare.com/learning/bots/what-is-a-bot/) make up a large percentage of page visitors to websites. Bots that visit websites serve a range of purposes, but especially common today are AI crawler bots. Such bots focus on discovering web content for [training AI models](https://www.cloudflare.com/learning/ai/inference-vs-training/). AI bots also help AI assistants surface webpages to answer user queries. Since high amounts of bot traffic can strain a web properties' resources, website administrators need to make sure they can identify AI crawlers in logs, and take steps to reduce their impact if they crawl too often.

Verified AI crawler activity can be monitored using website logs along with a [logs analytics tool](https://www.cloudflare.com/application-services/products/log-explorer/) (since manual analysis of millions of logs is nearly impossible). Administrators can search in their logs for the user-agent strings of the entities requesting content, and get visibility into how many requests come from AI crawlers.

## What do AI crawler bots do?

[AI](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) crawlers are bots that "crawl" or request webpages, using hyperlinks to explore the entire public web. They are far from the only crawler bots: for decades, [search engine crawler bots](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/) have scanned and indexed web content in order to provide it to users in search results.

But one of the differences between AI crawlers and search crawlers is that AI crawlers are much less likely to refer human user traffic to the pages they crawl. Rather, they use the pages they crawl to train AI models that respond to user queries without the user leaving the AI app or visiting a website.

Web servers, therefore, might serve high amounts of AI requests but see traffic from human visitors drop, in contrast to what happens when search crawler bots discover web content and begin referring traffic to the pages that host it. Websites that experience this may want to limit or block AI crawler bots so that their resources are not spent in vain. Conversely, some website administrators may want to make sure AI crawlers can crawl their websites so that they show up in AI overviews. Either way, identifying and managing AI crawler bot traffic is crucial for most websites.

## How to track AI crawler activity via user-agent strings

All persons and things browsing the web have a user-agent string included in the HTTP requests they send (this is distinct from their IP address). For humans, user-agent strings are generated by the browser and usually indicate device type and browser type, something like:

  * `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36`



Bots are not necessarily using browsers or specific consumer devices, and most crawler bots have simple, clearly defined user agent strings, like:

  * `Googlebot`



Search in logs for the user-agent strings associated with known bots to see which crawlers are reaching a website, how many pages they are requesting, how often they crawl, and more.

The most common AI crawlers, and the ones that are most likely to crawl a site at any given time, include:

  * Meta-ExternalAgent

  * GPTBot (from OpenAI)

  * GoogleOther

  * Amazonbot

  * PetalBot (from Huawei)




A more complete list of these AI crawlers with their user-agent strings is available below, or in the continually updated, and freely available, [Cloudflare Radar report](https://radar.cloudflare.com/bots).

## Which AI bots are crawling your site?

AI bots can be from organizations that run AI models, or they can be from [AI agents](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/) or other AI products. Some are looking for training data for their models; others look for information they can source to answer live user queries.

The following bots are all verified and have public documentation.

#### List of common AI web crawlers

**Meta-ExternalAgent**

This bot is from Meta (best known for operating Facebook and Instagram). Meta-ExternalAgent crawls the web to find content for training AI models. As of 2026, this bot sends the second-most requests of all bots on the web (after the search crawler Googlebot).

User-agent string in log files:

  * `meta-externalagent/1.1 (+https://developers.facebook.com/docs/sharing/webmasters/crawler)`

  * `meta-externalagent/1.1`




**GPTBot**

From OpenAI, the GPTBot crawler finds content for use in training AI models, including the widely used ChatGPT model. GPTBot sends the third-most requests, ranking just after Meta-ExternalAgent. (Be sure to check out the [live rankings in Cloudflare Radar](https://radar.cloudflare.com/bots).)

User-agent string in log files:

  * `GPTBot`



**OAI-SearchBot**

Also from OpenAI, OAI-SearchBot is used to find websites to reference in search results within ChatGPT.

User-agent string in log files:

  * `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot`



**GoogleOther**

This crawler bot from Google is distinct from Google's crawler for search (GoogleBot). It serves many purposes, not just AI model training. Google has cautioned against blocking GoogleOther since it finds web content that is used in many parts of the Google ecosystem.

User-agent string in log files:

  * `GoogleOther`



**Amazonbot**

This crawler is from Amazon and helps Amazon train generative AI models, among other uses for the content it crawls.

User-agent string in log files:

  * `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1)`



**PetalBot**

PetalBot is from device manufacturer Huawei, and it finds web content both for Petal, Huawei's search engine, and for Huawei's other services, including AI search.

User-agent string in log files:

  * `Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://webmaster.petalsearch.com/site/petalbot)`

  * `Mozilla/5.0 (compatible;PetalBot;+https://webmaster.petalsearch.com/site/petalbot)`




**Applebot**

A crawler operated by Apple, Applebot powers many services within the Apple ecosystem, including search features in Spotlight, Siri, and Safari. Applebot also provides content for training generative AI models that power Apple Intelligence, Services, and Developer Tools, among other services.

User-agent string in log files:

  * `(Applebot/0.1; +http://www.apple.com/go/applebot)`



**DuckAssistbot**

[According to](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) search engine provider DuckDuckGo, DuckAssistbot is "a web crawler for DuckDuckGo Search that crawls pages in real-time for our AI-assisted answers... This data is not used in any way to train AI models."

User-agent string in log files:

  * `DuckAssistBot/1.1; (+http://duckduckgo.com/duckassistbot.html)`



Other crawlers and AI assistants include MistralAI-User, Manus Bot, Devin, and QualifiedBot.

Cloudflare Radar divides these and other AI-focused bots into AI crawlers, AI assistants, and AI search. To see all verified AI bots, sort the Cloudflare Radar list by category.

## How to block bots and AI crawlers

[Robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/) guidelines tell bots where they should and should not go on a website, or if they should crawl the website at all. Robots.txt is not binding — following it is more of a courtesy than anything else. But, most reputable bots will follow robots.txt guidelines. Setting robots.txt rules tells AI crawler bots that follow the rules to not crawl part or all of a website.

For instance, a robots.txt file could include this command:

`User-Agent: Example.com-Bot`

`Disallow: /`

This tells Example.com-Bot (not a real bot, just used for this example) that the site administrator does not desire it to crawl any part of the website.

It can be time-consuming to manually create these robots.txt rules. To make it easier to manage AI crawler bot traffic, Cloudflare offers [AI Crawl Control](https://www.cloudflare.com/ai-crawl-control/).

AI Crawl Control lets website administrators block or allow specific AI crawlers, block all AI crawlers, or even charge specific crawlers for the privilege of crawling.

## What about unverified AI crawler bots?

Not all bots follow robots.txt or respect website administrators' wishes. Some crawler bots even camouflage their activity so that they can [scrape](https://www.cloudflare.com/learning/bots/what-is-content-scraping/) content without being blocked. More sophisticated [bot management tools](https://www.cloudflare.com/application-services/products/bot-management/) are necessary in these cases, tools that can identify ill-intentioned bot activity even when it is disguised.

Cloudflare AI Crawl Control uses [machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/), behavioral analysis, and fingerprinting to identify all bot traffic, even when it is disguised. Cloudflare can detect and block unwanted bot activity on any website.

Get started with [AI Crawl Control](https://www.cloudflare.com/ai-crawl-control/).

## FAQs

#### What is the primary purpose of AI crawler bots?

These bots explore the public web to find and gather content used to train artificial intelligence models, especially generative AI models and large language models. Some AI crawlers also help virtual assistants find relevant webpages to provide answers for user questions.

#### How do AI crawlers differ from traditional search engine crawlers?

While both crawl the web via hyperlinks, search crawlers typically direct human visitors back to the original website through search results. In contrast, AI crawlers often use a site's data to generate responses within an AI application, which can result in a decrease in actual human traffic to the source website.

#### Which AI crawlers currently send the most requests across the Internet?

As of 2026, Meta-ExternalAgent is the second-most active bot on the web, following only the search crawler Googlebot. GPTBot, which is operated by OpenAI to train models like ChatGPT, ranks third in total request volume.

#### What is the most common method for requesting that bots stay off a website?

Website administrators often use a robots.txt file to provide instructions on which parts of a site should or should not be accessed by bots. Although these guidelines are not technically binding, most reputable AI bots will respect the rules set by the administrator.

#### How does Cloudflare AI Crawl Control assist with bot management?

This tool simplifies the AI crawler management process by allowing administrators to easily allow or block specific AI crawlers or restrict all of them at once. It can also identify unverified bots that try to hide their identity by using machine learning and behavioral analysis to spot disguised activity.
