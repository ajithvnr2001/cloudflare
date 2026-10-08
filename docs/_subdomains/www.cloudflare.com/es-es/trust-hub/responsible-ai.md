---
url: https://www.cloudflare.com/es-es/trust-hub/responsible-ai/
title: Cloudflare\u2019s approach to responsible AI | Cloudflare
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (127 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T08:16:18.377059+00:00
---

# Cloudflare’s approach to responsible AI | Cloudflare

> Source: https://www.cloudflare.com/es-es/trust-hub/responsible-ai/

Preview Mode
[Documentation](https://staging.mrk.cfdata.org/mrk/redwood-blade-repository/)
# Cloudflare’s approach to responsible AI
![Native function calling in Workers AI easier, smarter, faster - illustration](https://cf-assets.www.cloudflare.com/slt3lc6tev37/6vQhSNIXEocuvZNP6R9b7g/16254efe93f9846bd68be4c45e652395/Native-function-calling-in-Workers-AI-easier-smarter-faster.svg)
Cloudflare has a long history of protecting our customers' Internet applications, corporate assets and networks against cyber threats – using innovative products powered by machine learning models we build in-house. We use the power of Cloudflare’s global network to detect and mitigate more than 227 billion cybersecurity threats a day on average without compromising the privacy of our customers’ data.
Our platform is also the best place to deploy artificial intelligence (AI) agents at scale, enabled by our globally distributed, serverless infrastructure. What sets us apart is we do not train large language models (LLMs) ourselves, so customers never need to worry that their data is used to train LLMs. Customers can instead choose from leading large language models in our [Workers AI Catalog](https://developers.cloudflare.com/workers-ai/models/) or bring their own–delivering high performance, cost-efficient AI experiences on Cloudflare’s trusted platform.
[Read FAQ](https://www.cloudflare.com/es-es/trust-hub/responsible-ai/#responsible-ai-faq)[Responsible AI Principles](https://www.cloudflare.com/es-es/responsible-ai-principles/)
![Native function calling in Workers AI easier, smarter, faster - illustration](https://cf-assets.www.cloudflare.com/slt3lc6tev37/6vQhSNIXEocuvZNP6R9b7g/16254efe93f9846bd68be4c45e652395/Native-function-calling-in-Workers-AI-easier-smarter-faster.svg)
### Frequently asked questions
Do Cloudflare products incorporate AI?
_Machine learning_ _: Intelligent Threat Mitigation_
Cloudflare leverages _predictive_ _AI_ to safeguard the security and integrity of our network by continuously analyzing network traffic to detect and address threats – both known and new vulnerabilities – before they can cause harm. Our AI technologies learn from each encounter, improving their ability to recognize and counteract new and emerging threats and ensuring that our defenses remain robust and up-to-date. Examples of Cloudflare products that use machine learning include Bot Management, WAF, Page Shield, API Shield, and Cloudflare Email Security (formerly Area 1). 
[Predictive AI systems](https://www.cloudflare.com/es-es/learning/ai/what-is-predictive-ai/) use machine learning (ML) models and statistical analysis to identify patterns, anticipate behaviors, and forecast future events.
For example, if we detect malicious, fraudulent or illegal activity on our network, such as, but not limited to, botnet activity, we may use this threat signal as a data point that is used to train our ML models. We may also use samples of data transiting through our systems to train the ML models powering our web application firewall (WAF). Some of our features (e.g. Cloudflare Email Security) also rely on customized models that are trained on a particular customer’s historical traffic patterns in order to detect and mitigate anomalous activity and are used solely for that customer. This approach allows us to provide our industry-leading security services that our customers require to protect their websites, networks, and employees from bots, DDoS attacks, phishing, and other cybersecurity threats.
_Workers AI_
Workers AI offers AI inference-as-a-service on Cloudflare's global edge network. Customers can leverage pre-trained models from our [Workers AI catalog](https://developers.cloudflare.com/workers-ai/models/) (subject to third-party licenses) or deploy their own custom models for inference tasks. Importantly, Cloudflare does not train AI models or provide GPU access for training.
_AI assistants_
Cloudflare uses large language models (LLMs) available in [Workers AI](https://developers.cloudflare.com/workers-ai/models/), Cloudflare’s inference-as-a-service offering, to power AI assistants, such as Cloudflare [Cursor](https://developers.cloudflare.com/workers/ai/) and Cloudy. 
Does Cloudflare provide any Generative AI systems?
[Generative AI systems](https://www.cloudflare.com/es-es/learning/ai/what-is-generative-ai/) use large language models (LLMs) to generate new content, whether it is text, images or code. Our limited use of Generative AI is in the areas of analyzing customer configurations and suggesting configuration improvements, and in allowing customers to write technical or operational code and rules to use with our products, via our AI assistants Cursor and Cloudy.
[Cursor](https://blog.cloudflare.com/introducing-cursor-the-ai-assistant-for-docs/) is an AI assistant trained to answer questions about Cloudflare’s Developer Platform. [Cloudy](https://blog.cloudflare.com/introducing-ai-agent/) helps users quickly understand and improve their WAF and Gateway configurations in Cloudflare One and get summaries of Email Security detections.
Does Cloudflare train AI on customer data?
We recognize that the privacy and security of our customers’ content is paramount, and we do not use our customers’ content to train any LLMs.
Cloudflare’s strength proposition lies in the ability of our machine learning systems to analyze network traffic from the billions of requests that flow through our infrastructure. By observing cyber attacks targeting any single customer, we gain insights that enhance the security, performance, and reliability for our entire network. This allows us to proactively protect all Cloudflare customers, as our defenses evolve based on the latest threat landscape. Importantly, our systems do not train on customer content, focusing instead on the patterns within network traffic to continuously improve our services.
In addition, customers can use Workers AI, Cloudflare's AI inference-as-a-service platform, to leverage pre-trained models from our [Workers AI catalog](https://developers.cloudflare.com/workers-ai/models/) (subject to third-party licenses) or deploy their own custom models for inference tasks. These models can be used to run on GPUs on Cloudflare’s global network. Please note that Cloudflare neither trains its own large language models (LLMs) nor provides its customers with access to GPUs for training their own models.
Cloudy uses publicly available LLM models via Workers AI, and it does not train any models using customer content. Rather, when customers enter their WAF rules and/or Gateway configurations as prompts, Cloudy will use this information to generate an appropriate answer. The custom rules are used as context only to generate a specific response to a specific question. We do not store this data nor do we train models using it.
How does Cloudflare protect our customers’ privacy during AI development?
We are deeply committed to protecting the privacy of personal data, and this commitment extends to AI. As such, Cloudflare does not use any Customer Content, as defined in our Enterprise and Self-Serve Subscription Agreements, to train Cloudflare products that use machine learning (ML) models without customer consent.
In addition, we do not train large language models (LLMs).
  

How does Cloudflare support other developers in using AI?
Beyond our network and application security offerings, Cloudflare provides a scalable, future-ready platform for our customers to train, develop, deploy, and optimize AI. Specifically, Cloudflare provides the following capabilities:
  * TRAIN: Store and protect training data with R2 Storage while securely hosting AI models. Our platform also supports data residency requirements across jurisdictions without incurring egress fees, thus reducing transfer costs while ensuring compliance;
  * DEVELOP: Use Vectorize to generate, store, and search embeddings, and leverage Workers AI to access a curated list of open-source third-party AI models, including General-Purpose AI (GPAI) models. Cloudflare’s platform ensures high availability and real-time inference powered by cloud GPUs, supporting robust AI applications; 
  * SECURE: Protect public AI endpoints with AI Gateway, implementing safeguards against vulnerabilities like prompt injections, data leaks, and unauthorized code execution. This ensures system resilience;
  * OPTIMIZE: Monitor AI performance, track usage, and achieve granular control and transparency with Cloudflare’s observability tools, such as AI Gateway. Gain actionable insights to optimize costs, traffic, and resource allocation while improving accountability. Use AI Audit to log and track website scanning, reclaim control, and even monetize content-sharing, including copyright-protected material. 


Does Cloudflare comply with the EU AI Act?
The European Union's Artificial Intelligence Act (AI Act) creates a legal framework for the development and use of artificial intelligence in the EU. Its main objectives are to promote the adoption of and trust in AI systems and support innovation while ensuring AI systems are safe and respect fundamental rights. The AI Act categorizes AI systems based on risk levels (unacceptable, high, limited and minimal) and establishes requirements and obligations for AI operators to enhance accountability and transparency. 
Satisfying the AI Act’s requirements necessarily requires a level of cooperation between customers and their vendors. Our EU customers expect Cloudflare to design our AI-powered products in ways that support their compliance with the AI Act, and we recognize our responsibility in this regard. We have always been, and will remain, fully committed to developing industry-leading, AI-powered security products that align with the requirements of law, including the new AI Act. 
_Application of the EU AI Act_
The AI Act applies to an AI System (defined below) whenever a provider makes it available in the EU. As defined in the AI Act, a provider is the developer of the system. Typically, the AI system will bear the provider’s name or trademark. The AI Act also applies to organizations based in the EU that use AI systems. Such organizations are defined by the AI Act as deployers. 
In addition, the AI system-related provisions of the AI Act also apply if the output produced by an AI system outside the EU is used in the EU. In this way, the AI Act may apply to AI system providers and deployers that are not based in the EU. 
Finally, the AI Act also regulates the providers of General-Purpose AI (GPAI) models (defined below) made available in the EU.
An AI system is a machine-based system, designed to function with some level of autonomy, which can infer from the input it receives how to generate outputs like predictions, content, recommendations, or decisions. An AI system incorporates one or more AI models.
An AI model is an algorithm that has been trained on a dataset, in order to make predictions or perform new tasks on unseen data. However, like software needing installation on a computer to run, an AI model first needs to be integrated with other components, such as a user interface, data pipelines, and computer hardware, to be capable of use. Collectively, once integrated, the AI model and the components into which it has been integrated make up the AI system.
A GPAI model is a particular type of AI model, generally trained on a very large dataset, that displays significant generality and is capable of performing a wide range of distinct tasks. GPAI models are often fine-tuned or modified to create new AI models. Large language models (LLMs) and other types of generative AI models are the most common examples of GPAI models.
_High-risk AI systems_
Cloudflare does not provide any high-risk AI systems. The AI Act lists the types of AI systems that are considered to be high risk, due to their potential to present a significant risk of harm to the health, safety, or fundamental rights of individuals. Cloudflare’s AI-driven products do not fall within this list, and are designed to protect our customers against cyber attacks and threats. 
_GPAI models_
Cloudflare does not provide General-Purpose AI (GPAI) models trained by Cloudflare as part of its product offerings. The AI models, including GPAI models, made available on Workers AI, are provided by third-party providers who have the responsibility to assess their compliance with the AI Act.
This is important because GPAI models, such as LLMs, require extensive training data. This process can raise concerns regarding data sourcing and potential privacy implications, as highlighted by recent media attention on data scraping practices. In contrast, predictive ML models, like those used in Cloudflare's security services, are trained on specific datasets with structured outputs (e.g., threat scores), minimizing the risk of inadvertent data disclosure. This distinction underscores Cloudflare's commitment to responsible AI deployment and data security. 
_Deploying AI systems_
We deploy and use AI systems within our own operations, leveraging AI to enhance our internal processes and services. To the extent we rely on vendors who use AI technologies, we perform a cross-functional review of those vendors, applying a dedicated vendor AI risk assessment.
Should we deploy any high-risk AI systems, we are committed to implementing compliance obligations determined by the AI Act, in line with the principles of transparency and fairness.
  

Has Cloudflare developed an AI Literacy program? 
We recognize the transformative nature of AI in the workplace and have therefore invested in developing a workforce skilled in the use and development of AI technologies. This includes providing mandatory training on safe and trustworthy AI for all employees and tailored AI learning pathways to equip teams with the tools and training specific to their circumstances and the AI systems we develop and use. 
CÓMO EMPEZAR
  * [Planes gratuitos](https://www.cloudflare.com/plans/free/)
  * [Planes para pequeñas empresas](https://www.cloudflare.com/small-business/)
  * [Para empresas](https://www.cloudflare.com/enterprise/)
  * [Sugerencias](https://www.cloudflare.com/about-your-website/)
  * [Solicita una demostración](https://www.cloudflare.com/plans/enterprise/demo/)
  * [Contactar con ventas](https://www.cloudflare.com/plans/enterprise/contact/)


SOLUCIONES
  * [Conectividad cloud](https://www.cloudflare.com/connectivity-cloud/)
  * [Servicios para aplicaciones](https://www.cloudflare.com/application-services/)
  * [SASE y seguridad en el espacio de trabajo](https://www.cloudflare.com/sase/)
  * [Servicios de red](https://www.cloudflare.com/network-services/)
  * [Plataforma para desarrolladores](https://www.cloudflare.com/developer-platform/)


SOPORTE
  * [Centro de ayuda](https://support.cloudflare.com)
  * [Atención al cliente](https://dash.cloudflare.com/?to=/:account/support)
  * [Foro de la comunidad](https://community.cloudflare.com)
  * [Discord para desarrolladores ](https://discord.com/invite/cloudflaredev)
  * [¿Has perdido el acceso a tu cuenta?](https://developers.cloudflare.com/support/account-management-billing/common-account-questions/login-and-account-issues/)
  * [Estado de Cloudflare](https://www.cloudflarestatus.com/)


CONFORMIDAD
  * [Recursos de conformidad](https://www.cloudflare.com/trust-hub/compliance-resources/)
  * [Confianza](https://www.cloudflare.com/trust-hub/)
  * [RGPD](https://www.cloudflare.com/trust-hub/gdpr/)
  * [IA responsable](https://www.cloudflare.com/trust-hub/responsible-ai/)
  * [Informe de transparencia](https://www.cloudflare.com/transparency/)
  * [Notificar abuso](https://www.cloudflare.com/trust-hub/abuse-approach/)


INTERÉS PÚBLICO
  * [Proyecto Galileo](https://www.cloudflare.com/galileo/)
  * [Proyecto Athenian](https://www.cloudflare.com/athenian/)
  * [Cloudflare for Campaigns](https://www.cloudflare.com/campaigns/)
  * [Project Fair Shot](https://www.cloudflare.com/fair-shot/)


EMPRESA
  * [Acerca de Cloudflare](https://www.cloudflare.com/about-overview/)
  * [Mapa de red](https://www.cloudflare.com/network/)
  * [Nuestro equipo](https://www.cloudflare.com/people/)
  * [Logotipos y dossier de prensa](https://www.cloudflare.com/press/press-kit/)
  * [Diversidad, equidad e inclusión](https://www.cloudflare.com/diversity-equity-and-inclusion/)
  * [Impact/ESG](https://www.cloudflare.com/impact/)


[](https://www.facebook.com/cloudflare "Facebook")[](https://x.com/cloudflare "X")[](https://www.linkedin.com/company/cloudflare "LinkedIn")[](https://www.youtube.com/cloudflare "Youtube")[](https://instagram.com/cloudflare "Instagram")
© 2026 Cloudflare, Inc.[Política de privacidad](https://www.cloudflare.com/privacypolicy/)[Condiciones de uso](https://www.cloudflare.com/website-terms/)[Informar sobre problemas de seguridad](https://www.cloudflare.com/disclosure/)[Confianza y seguridad](https://www.cloudflare.com/trust-hub/abuse-approach/)![privacy options](https://www.cloudflare.com/img/privacyoptions.svg)Preferencias de cookies[Marca](https://www.cloudflare.com/trademark/)
![](https://testingcf.jsdelivr.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=36264091)![](https://fastly.jsdelivr.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=81019903)![](https://jsdelivr.b-cdn.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=72753444)![](https://9y49n2-m.ns1pcdn.net/a/t128.jpg?r=97382669)![](https://1a4s4dv-m.ns1pcdn.net/a/t128.jpg?r=16424558)![](https://kgnvry-ns1p.b-cdn.net/a/t128.jpg?r=55062150)![](https://benchmarks.cdn-b.compute-pipe.com/r20-100KB.png?r=13572686)![](https://benchmark.1e100cdn.net/r20-100KB.png?r=45980067)![](https://cedexis-test.akamaized.net/img/r20-100KB.png?r=42856801)![](https://benchmarks.cdn-c.compute-pipe.com/r20-100KB.png?r=14256147)![](https://benchmarks.cdn.compute-pipe.com/r20-100KB.png?r=2010344)![](https://5bav82-m.ns1pcdn.net/a/t128.jpg?r=70903781)![](https://ns1p-aws-backed.global.ssl.fastly.net/a/t128.jpg?r=56579301)![](https://1xtvhvx-m.ns1pcdn.net/a/t128.jpg?r=62879981)![](https://1xtsor1-m.ns1pcdn.net/a/t128.jpg?r=5416825)![](https://1lmnv6z-m.ns1pcdn.net/a/t128.jpg?r=26936881)
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=bc36be7e-48e4-431f-952e-cd2d15ed4134&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=09d91a4a-e84b-4ee9-83d1-b8dd621bc63d&restricted_data_use=restrict_optimization&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fes-es%2Ftrust-hub%2Fresponsible-ai%2F&tw_engaged_ms=256&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791446666898-650016583&twpid=tw.1791446666898.801927725504384826&txn_id=nvldc&type=javascript&version=2.4.11)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=bc36be7e-48e4-431f-952e-cd2d15ed4134&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=09d91a4a-e84b-4ee9-83d1-b8dd621bc63d&restricted_data_use=restrict_optimization&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fes-es%2Ftrust-hub%2Fresponsible-ai%2F&tw_engaged_ms=256&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791446666898-650016583&twpid=tw.1791446666898.801927725504384826&txn_id=nvldc&type=javascript&version=2.4.11)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0526d1a7-faed-483f-9413-65b48ea08661&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=09d91a4a-e84b-4ee9-83d1-b8dd621bc63d&restricted_data_use=restrict_optimization&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fes-es%2Ftrust-hub%2Fresponsible-ai%2F&tw_engaged_ms=30&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791446666898-650016583&twpid=tw.1791446666898.801927725504384826&txn_id=pomsv&type=javascript&version=2.4.11)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=0526d1a7-faed-483f-9413-65b48ea08661&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=09d91a4a-e84b-4ee9-83d1-b8dd621bc63d&restricted_data_use=restrict_optimization&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fes-es%2Ftrust-hub%2Fresponsible-ai%2F&tw_engaged_ms=30&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791446666898-650016583&twpid=tw.1791446666898.801927725504384826&txn_id=pomsv&type=javascript&version=2.4.11)
