---
url: https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/
title: What are the OWASP Top 10 risks for LLMs?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:32.828420+00:00
---

# What are the OWASP Top 10 risks for LLMs?

> Source: https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/

[ Learning Center ](https://www.cloudflare.com/learning/) / artificial intelligence (AI)

##  What are the OWASP Top 10 risks for LLMs? 

Large language model (LLM) applications are vulnerable to prompt injection, data poisoning, model denial of service, and more attacks. 

[Learning Center](https://www.cloudflare.com/learning)/artificial intelligence (AI)/[AI for cybersecurity](https://www.cloudflare.com/learning/ai/ai-for-cybersecurity/)[What is AI image generation?](https://www.cloudflare.com/learning/ai/ai-image-generation/)[How to prevent misuse of AI](https://www.cloudflare.com/learning/ai/ai-misuse/)[What is vibe coding?](https://www.cloudflare.com/learning/ai/ai-vibe-coding/)[What is big data?](https://www.cloudflare.com/learning/ai/big-data/)[What are ChatGPT plugins?](https://www.cloudflare.com/learning/ai/chatgpt-plugins/)[What is AI data poisoning?](https://www.cloudflare.com/learning/ai/data-poisoning/)[What is the third wave of AI?](https://www.cloudflare.com/learning/ai/evolution-of-ai/)[What is the history of AI?](https://www.cloudflare.com/learning/ai/history-of-ai/)[How to block AI crawlers](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/)[How to enhance AI models with RAG (retrieval-augmented generation)](https://www.cloudflare.com/learning/ai/how-to-build-rag-pipelines/)[How to detect AI crawlers](https://www.cloudflare.com/learning/ai/how-to-detect-which-ai-bots-crawl/)[How to get started with vibe coding](https://www.cloudflare.com/learning/ai/how-to-get-started-with-vibe-coding/)[How to manage AI agents for business use](https://www.cloudflare.com/learning/ai/how-to-manage-ai-agents-for-businesses/)[How to prevent web scraping](https://www.cloudflare.com/learning/ai/how-to-prevent-web-scraping/)[How to secure AI systems](https://www.cloudflare.com/learning/ai/how-to-secure-ai-systems/)[How to secure training data against AI data leaks](https://www.cloudflare.com/learning/ai/how-to-secure-training-data-against-ai-data-leaks/)[AI inference vs. training: What is AI inference?](https://www.cloudflare.com/learning/ai/inference-vs-training/)[What is an MCP client?](https://www.cloudflare.com/learning/ai/mcp-client-and-server/)[What is natural language processing (NLP)?](https://www.cloudflare.com/learning/ai/natural-language-processing-nlp/)[What are the OWASP Top 10 risks for LLMs?](https://www.cloudflare.com/learning/ai/owasp-top-10-risks-for-llms/)[How to prevent prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/)[What is retrieval-augmented generation (RAG) in AI?](https://www.cloudflare.com/learning/ai/retrieval-augmented-generation-rag/)[What are artificial intelligence (AI) hallucinations?](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/)[What is an AI agent?](https://www.cloudflare.com/learning/ai/what-is-agentic-ai/)[What is AI security?](https://www.cloudflare.com/learning/ai/what-is-ai-security/)[What is artificial intelligence (AI)?](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[What is deep learning?](https://www.cloudflare.com/learning/ai/what-is-deep-learning/)[What is generative AI?](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)[What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)[What is machine learning?](https://www.cloudflare.com/learning/ai/what-is-machine-learning/)[What is the Model Context Protocol (MCP)?](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/)[What is a neural network?](https://www.cloudflare.com/learning/ai/what-is-neural-network/)[What is predictive AI?](https://www.cloudflare.com/learning/ai/what-is-predictive-ai/)[What is quantization in machine learning?](https://www.cloudflare.com/learning/ai/what-is-quantization/)[What is shadow AI?](https://www.cloudflare.com/learning/ai/what-is-shadow-ai/)[What is a large language model (LLM)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[What are embeddings?](https://www.cloudflare.com/learning/ai/what-are-embeddings/)[What is a vector database?](https://www.cloudflare.com/learning/ai/what-is-vector-database/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what OWASP is 
  * Summarize each of the OWASP Top 10 threats for LLMs 
  * Uncover ways to address LLM vulnerabilities 



Related content  [ How to prevent prompt injection ](https://www.cloudflare.com/learning/ai/prompt-injection/)[ What is AI data poisoning? ](https://www.cloudflare.com/learning/ai/data-poisoning/)[ What is artificial intelligence (AI)? ](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)[ What is a large language model (LLM)? ](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)[ What is generative AI? ](https://www.cloudflare.com/learning/ai/what-is-generative-ai/)

On this page

  * What is OWASP?

    * 1\. Prompt injection

    * 2\. Insecure output handling

    * 3\. Training data poisoning

    * 4\. Model denial of service

    * 5\. Supply chain vulnerabilities

    * 6\. Sensitive information disclosure

    * 7\. Insecure plugin design

    * 8\. Excessive agency

    * 9\. Overreliance

    * 10\. Model theft

  * How can organizations secure LLMs?

  * How does Cloudflare help reduce LLM risks?

  * FAQs

    * What are the top 10 risks for large language models according to the Open Web Application Security Project?

    * How do LLM security vulnerabilities differ from traditional application vulnerabilities

    * What is prompt injection?

    * What are the key governance concerns for LLM applications?

    * Which strategies are most effective for securing LLMs in organizations?




## What is OWASP?

The Open Web Application Security Project (OWASP) is an international non-profit organization with [web application](https://www.cloudflare.com/learning/security/what-is-web-application-security/) security as its core mission. OWASP strives to help other organizations improve their web application security by providing a range of free information through documents, tools, videos, conferences, and forums.

The [OWASP Top 10 report](https://www.cloudflare.com/learning/security/threats/owasp-top-10/) highlights the 10 most critical risks for application security, according to security experts. OWASP recommends that all organizations incorporate insights from this report into their [web application security strategy](https://www.cloudflare.com/the-net/state-application-security/).

In 2023, an OWASP working group launched a new project to create a similar report focusing on threats to [large language model (LLM)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/) applications. The OWASP Top 10 for Large Language Model Applications identifies threats, provides examples of vulnerabilities and real-work attack scenarios, and offers mitigation strategies. OWASP hopes to raise awareness among developers, designers, architects, and managers while also helping them defend against threats.

Below are the vulnerabilities highlighted in the OWASP Top 10 for LLM Applications report from October 2023:

#### 1\. Prompt injection

[Prompt injection](https://www.cloudflare.com/learning/ai/prompt-injection/) is a tactic in which attackers manipulate the prompts used for an LLM. Attackers might intend to steal sensitive information, affect decision-making processes guided by the LLM, or use the LLM in a [social engineering](https://www.cloudflare.com/learning/security/threats/social-engineering-attack/) scheme.

Attackers might manipulate prompts in two ways:

  * **Direct prompt injection** (also called “jailbreaking”) is the process of overwriting the system prompt, which instructs the LLM on how to respond to user input. Through this tactic, the attacker might be able to access and exploit backend systems.

  * **Indirect prompt injection** is when an attacker controls external websites, files, or other external sources that are used as input for the LLM. The attacker could then exploit the systems that the LLM accesses or employ the model to manipulate the user.




There are multiple ways to prevent damage from prompt injections. For example, organizations can implement robust [access control](https://www.cloudflare.com/learning/access-management/what-is-access-control/) policies for backend systems, integrate humans into LLM-directed processes, and ensure humans have the final say over LLM-driven decisions.

#### 2\. Insecure output handling

When organizations fail to scrutinize LLM outputs, any outputs generated by malicious users could cause problems with downstream systems. The exploitation of insecure output handling could result in [cross-site scripting (XSS)](https://www.cloudflare.com/learning/security/threats/cross-site-scripting/), [cross-site request forgery (CSRF)](https://www.cloudflare.com/learning/security/threats/cross-site-request-forgery/), server-side request forgery (SSRF), [remote code execution (RCE)](https://www.cloudflare.com/learning/security/what-is-remote-code-execution/), and other types of attacks. For example, an attacker might cause an LLM to output a malicious script that is interpreted by a browser, resulting in an XSS attack.

Resource

Survey shows application modernization makes AI ROI 3x more likely

[Get the report →](https://www.cloudflare.com/resource/g/app-innovation-report/2026/)

Organizations can prevent insecure output handling by applying a [Zero Trust security](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) model and treating the LLM like any user or device. They would validate any output from the LLM before allowing them to drive other functions.

#### 3\. Training data poisoning

Attackers might attempt to manipulate — or “poison” — data used for training an LLM model. [Data poisoning](https://www.cloudflare.com/learning/ai/data-poisoning/) can hinder the model’s ability to deliver accurate results or support AI-driven decision making. This type of attack could be launched by malicious competitors who want to damage the reputation of the organization using the model.

To reduce the likelihood of data poisoning, organizations must [secure the data supply chain](https://www.cloudflare.com/the-net/data-protection-ai/). As part of that work, they should verify the legitimacy of data sources — including any components of [big data](https://www.cloudflare.com/learning/ai/big-data/) used for modeling. They should also prevent the model from scraping data from untrusted sources and sanitize data.

#### 4\. Model denial of service

Similar to a [distributed denial-of-service (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attack, attackers might run resource-heavy operations using an LLM in an attempt to degrade service quality, drive up costs, or otherwise disrupt operations. This type of attack might go undetected since LLMs often consume large amounts of resources, and resource demands can fluctuate depending on user inputs.

To avoid this type of [denial-of-service](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/) attack, organizations can enforce [API](https://www.cloudflare.com/learning/security/api/what-is-an-api/) [rate limits](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/) for individual users or [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). They can also validate and sanitize inputs. And they should continuously monitor resource usage to identify any suspicious spikes.

#### 5\. Supply chain vulnerabilities

Vulnerabilities in the supply chain for LLM applications can leave models exposed to security risks or yield inaccurate results. Several components used for LLM applications — including pre-trained models, the data used to train models, third-party data sets, and plugins — can set the groundwork for [an attack](https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/) or cause other problems with the LLM application’s operation.

[Addressing supply chain vulnerabilities](https://www.cloudflare.com/the-net/supply-chain-attacks/) starts with carefully vetting suppliers and ensuring they have adequate security in place. Organizations should also maintain an up-to-date inventory of components, and scrutinize supplied data and models.

#### 6\. Sensitive information disclosure

LLM applications might inadvertently reveal confidential data in responses, ranging from sensitive customer information to intellectual property. These types of disclosures could constitute compliance violations or lead to security breaches.

Mitigation efforts should focus on preventing [confidential information](https://www.cloudflare.com/learning/privacy/what-is-personal-information/) and malicious inputs from entering training models in the first place. Data sanitizing and scrubbing are essential for these efforts.

Since building LLMs might involve cross-border data transfers, organizations should also implement automated [data localization](https://www.cloudflare.com/learning/privacy/what-is-data-localization/) controls that keep certain sensitive data in specific regions. They can allow other data to be incorporated into LLMs.

#### 7\. Insecure plugin design

LLM plugins can enhance model functionality and facilitate integration with third-party services. But some plugins might lack sufficient access controls, creating opportunities for attackers to inject malicious inputs. Those inputs could enable RCE or another type of attack.

Preventing plugin exploitation requires more secure plugin design. Plugins should control inputs and perform input checks, making sure no malicious code gets through. In addition, plugins should implement authentication controls based on the [principle of least privilege](https://www.cloudflare.com/learning/access-management/principle-of-least-privilege/).

#### 8\. Excessive agency

Developers often give LLM applications some degree of agency — the ability to take actions automatically in response to a prompt. Giving applications too much agency, however, can cause problems. If an LLM produces unexpected outputs (because of an attack, an AI hallucination, or some other error), the application could take potentially damaging actions, such as disclosing sensitive information or deleting files.

The best way to prevent excessive agency is for developers to limit the functionality, permissions, and autonomy of plugins and other tools to the minimum levels necessary. Organizations running LLM applications with plugins can also require humans to authorize certain actions before they are taken.

#### 9\. Overreliance

LLMs are not perfect. They can occasionally produce factually incorrect results, [AI hallucinations](https://www.cloudflare.com/learning/ai/what-are-ai-hallucinations/), or biased results, even though they might deliver those results in an authoritative way. When organizations or individuals rely on LLMs excessively, they can disseminate incorrect information that leads to regulatory violations, legal exposure, and damaged reputations.

To avoid the problems of overreliance, organizations should implement LLM oversight policies. They also should regularly review outputs and compare them with information in other, trusted external sources to confirm their accuracy.

#### 10\. Model theft

Attackers might attempt to access, copy, or steal proprietary LLM models. These attacks could result in the erosion of a company’s competitive edge or the loss of sensitive information within the model.

Applying strong access controls, including [role-based access control (RBAC)](https://www.cloudflare.com/learning/access-management/role-based-access-control-rbac/) capabilities, can help prevent unauthorized access to LLM models. Organizations should also regularly monitor access logs and respond to any unauthorized behavior. [Data loss prevention (DLP)](https://www.cloudflare.com/learning/access-management/what-is-dlp/) capabilities can help spot attempts to [exfiltrate](https://www.cloudflare.com/learning/security/what-is-data-exfiltration/) information from the application.

## How can organizations secure LLMs?

As the OWASP document suggests, organizations need a multi-faceted strategy to protect LLM applications from threats. For example, they should:

  * Analyze network traffic for patterns that might indicate a breached LLM, which could compromise applications.

  * Establish real-time visibility into packets and data interacting with LLMs at the bit level.

  * Apply DLP to secure sensitive data in transit.

  * Verify, filter, and isolate traffic to protect applications from compromised LLMs.

  * Employ [remote browser isolation (RBI)](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/) to insulate users from models with injected malicious code.

  * Use [web application firewall (WAF)](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)–managed rulesets to block LLM attacks based on SQL injection, XSS, and other web attack vectors.

  * [Employ a Zero Trust security model](https://www.cloudflare.com/the-net/roadmap-zerotrust/) to shrink their attack surface by granting only context-based, least-privilege access per resource.




## How does Cloudflare help reduce LLM risks?

To help organizations address the risks threatening LLM applications, Cloudflare offers AI Security for Apps — an advanced security solution designed specifically for LLM applications. Organizations can deploy [AI Security for Apps](https://www.cloudflare.com/application-services/products/ai-security-for-apps/) in front of LLMs to detect vulnerabilities and identify abuses before they reach models. Taking advantage of Cloudflare’s large global network, it runs close to users to spot attacks early and protect both users and models.

In addition, [Cloudflare AI Gateway](https://blog.cloudflare.com/ai-gateway-is-generally-available) provides an AI ops platform for managing and scaling [generative AI](https://www.cloudflare.com/learning/ai/what-is-generative-ai/) workloads from a unified interface. It acts as a proxy between an organization’s service and their interface provider, helping the organization [observe and control AI applications](https://www.cloudflare.com/learning/ai/what-is-ai-security/).

For a more in-depth look at the OWASP Top 10 for LLMs, see the [official report](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf).

## FAQs

#### What are the top 10 risks for large language models (LLMs) according to the Open Web Application Security Project (OWASP)?

The vulnerabilities OWASP highlights in their Top 10 for LLM report include:

  * Prompt injection

  * Insecure output handling

  * Training data poisoning

  * Model denial of service

  * Supply chain vulnerabilities

  * Sensitive information disclosure

  * Insecure plugin design

  * Excessive agency

  * Overreliance

  * Model theft




#### How do LLM security vulnerabilities differ from traditional application vulnerabilities

[LLM security vulnerabilities](https://www.cloudflare.com/the-net/vulnerable-llm-ai/) involve unique attack vectors specifically targeting the language model's reasoning and processing capabilities. Traditional applications typically face threats like SQL injection or cross-site scripting (XSS), while LLMs face novel threats like prompt injection, model denial of service, and hallucination manipulation.

#### What is prompt injection?

Prompt injection occurs when an attacker manipulates an LLM by inserting malicious inputs that override the original instructions. These attacks can lead to data theft, system manipulation, and exposure of sensitive information.

#### What are the key governance concerns for LLM applications?

LLM governance concerns include ensuring proper model oversight, [managing data privacy](https://www.cloudflare.com/the-net/building-cyber-resilience/ai-data-governance/), and implementing responsible AI practices. Strong governance frameworks help organizations [maintain compliance](https://www.cloudflare.com/the-net/pursuing-privacy-first-security/data-localization/) while mitigating risks related to biased outputs, intellectual property violations, and downstream liability.

#### Which strategies are most effective for securing LLMs in organizations?

To protect LLM applications, organizations should use a [layered security approach](https://www.cloudflare.com/the-net/ai-secure/) that includes monitoring traffic for threats, ensuring data visibility, applying data loss prevention (DLP), filtering and isolating risky activity, using web application firewalls (WAFs) to block common attacks, and adopting a Zero Trust security model with least-privilege access.
