---
url: https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/
title: What is data sovereignty?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:58.397787+00:00
---

# What is data sovereignty?

> Source: https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  What is data sovereignty? 

Data sovereignty is the idea that data is subject to the laws and regulations of the country or region where such data originates. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn the concept of data sovereignty 
  * Compare data sovereignty, data residency, and data localization 
  * Understand how data sovereignty and data residency can affect privacy compliance programs 



Related content  [ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[ What is data localization? ](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[ What is data localization? ](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[ What is the GDPR? ](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)

On this page

  * What is data sovereignty?

  * How do data sovereignty and data localization affect privacy compliance programs?

  * How Cloudflare helps organizations ensure data sovereignty and localization

  * FAQs

    * What is data sovereignty?

    * What is data localization?

    * What regulatory frameworks are related to data sovereignty?

    * What are cross-border data transfers?




## What is data sovereignty?

The term “data sovereignty” refers to the idea that data — such as intellectual property, financial data, or personal information — collected or stored in a particular geographic location, such as a specific country or the European Union (EU), should be subject to the laws of that location. Whether people are entering credit card information into an ecommerce website or posting comments on a social media platform, [data sovereignty](https://www.cloudflare.com/the-net/building-cyber-resilience/challenges-data-sovereignty/) rules aim to ensure that this user data is regulated by the legal framework in place where those users are citizens.

The broad concept of data sovereignty is often intertwined with questions of [data privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/#:~:text=Cloudflare%20products%20are%20built%20with,sell%20this%20information%20to%20advertisers)), government access to data, security, international business competition, and human rights. Some data sovereignty paradigms seek to make sure that data generated in one jurisdiction physically stays in that jurisdiction. Others seek to make sure that the legal protections guaranteed to data generated in a jurisdiction will follow the data even if it is processed or stored in another jurisdiction. Still others seek to make sure that data generated in a jurisdiction at a minimum remains available to law enforcement in that jurisdiction, regardless of whether it is also processed or stored elsewhere.

Almost every country has some kind of data protection law that provides certain protections to the personal information collected from its citizens. Relevant examples of data sovereignty rules include:

  * The [General Data Protection Regulation (GDPR)](https://www.cloudflare.com/trust-hub/gdpr/) and the [ePrivacy Directive](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/#:~:text=The%20ePrivacy%20Directive%20requires%20that,purpose%20before%20they%20provide%20consent.)

  * The California Consumer Privacy Laws ([CCPA](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/) and CPRA)

  * The Australian Privacy Principles (APP)

  * The Japan Act on the Protection of Personal Information (APPI)




For an example of a data sovereignty regulation in action, imagine an ecommerce store that sells to customers around the world, including the EU. In order to fulfill customer orders from the EU, the store collects and processes a variety of user data, including names, addresses, and billing information.

Regardless of where the ecommerce store may be based, the EU GDPR will apply to the data of EU customers. This means the store must do things like explicitly inform customers before collecting their data, and only collect personal information pertinent to the transaction (in this case, information related to order fulfillment). If the store wants to collect and use additional personal information for other reasons, such as sending marketing emails, the store will need to obtain the customer’s consent (which can be revoked at any time).

In addition, under the GDPR, customers can request access to their collected data and ask the company to rectify or delete their data (“data subject requests”), which means the ecommerce store must also build systems to accept and respond to such data subject requests.

## How do data sovereignty and data localization affect privacy compliance programs?

Data sovereignty and [data localization](https://www.cloudflare.com/learning/privacy/what-is-data-localization/) are closely related concepts. As noted above, data sovereignty is the idea that data is regulated by the laws of the country or region in which the data is processed. Data localization, meanwhile, is the practice of storing data within the physical boundaries of a country or region where it originated from. It is often used to ensure that highly sensitive information, such as banking details or medical information, remains [compliant](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/) with local regulations, as transferring or processing that data in another region may [put organizations at risk](https://www.cloudflare.com/the-net/pursuing-privacy-first-security/data-localization/) of compliance violations.

Referring back to the ecommerce business described above: From the moment it processes personal data, it needs to observe the different legal frameworks applicable to the consumer data that is being collected. Unless the business wants to take the most protective regulations and apply those to all customers’ data, the ecommerce business will need to map its data to ensure that the applicable data protection requirements follow that personal data.

In addition, data sovereignty rules can have a significant impact on decisions about where data is processed and stored. Some of these laws also have implications for cross-border data transfers, because the legal protections for the personal information follows the data regardless of where it is processed.

In the case of the ecommerce business, in order to transfer the data of EU citizens to a data center outside the EU, the business will need to consider what GDPR-approved legal mechanism it will use to transfer the data. Depending on where the business is located, it may need to put in place special contractual provisions in order to process EU personal data outside the EU or certify to an adequacy framework such as the EU-US Data Privacy Framework.

The kind of data sovereignty and localization requirements attached to the personal data that a business processes can also influence an organization’s decision about use of a cloud-based storage solution. [Cloud storage](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/) offers increased flexibility and scalability, and many can offer data localization solutions as well. But to satisfy very conservative jurisdictions with strict localization requirements, an organization may need to seek on-premise storage in addition to — or instead of — cloud-based solutions.

## How Cloudflare helps organizations ensure data sovereignty and localization

Cloudflare has a long history of providing data protection to its customers and end users before these protections were enshrined into law, and we believe it is important to not only say we comply with certain laws but to also demonstrate our compliance.

Cloudflare is certified to ISO/IEC 27701:2019 (which maps to the EU GDPR) and compliant with ISO 27001/27002, Payment Card Industry Data Security Standards [(PCI DSS)](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/#:~:text=It%20is%20intended%20to%20protect,debit%20cards%2C%20or%20prepaid%20cards.), and SSAE 18 SOC 2 Type II. Cloudflare is also certified under EU-US Data Privacy Framework, the Swiss-US Data Privacy Framework, and the UK extension to the EU Data Privacy Framework. In addition, Cloudflare is certified to the EU Cloud Code of Conduct. These [validations and others we hold](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) provide assurance to organizations who transfer their most sensitive data through Cloudflare, and help companies meet and maintain their own compliance obligations.

Cloudflare has long followed tenets that align to common data sovereignty regulations:

  * Cloudflare only collects the personal data we need to provide our services and to make our products better for customers

  * Cloudflare does not track our customers’ end users across Internet properties, and we do not profile our customers’ end users to sell advertisements

  * Cloudflare gives our customers the ability to access, correct, or delete their personal information

  * Cloudflare gives our customers control over the information that is processed by different services — for example, any data that is cached on the [content delivery network (CDN)](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/), stored in Workers Key Value Store, or captured by the [web application firewall (WAF)](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/)




In addition, Cloudflare can also support meeting any data localization requirements applicable. Our [Data Localization suite](https://www.cloudflare.com/data-localization/) makes it easy for businesses to set rules and controls at the Internet edge and to keep data locally stored and protected.

Learn more about the built-in security, privacy, and compliance functions of a [connectivity cloud](https://www.cloudflare.com/connectivity-cloud/).

## FAQs

#### What is data sovereignty?

Data sovereignty is the principle that data is subject to the laws and regulations of the country or region that it comes from, and that user data must be regulated by the legal frameworks that apply where the users are citizens.

#### What is data localization?

Data localization is the practice of storing data within the physical boundaries of the country or region where it was collected. This helps ensure compliance with local regulations.

#### What regulatory frameworks are related to data sovereignty?

Examples of regulatory frameworks relevant for data sovereignty include the EU's GDPR, California's CCPA, the Australian Privacy Principles, and the Japan Act on the Protection of Personal Information. These laws define requirements for how personal data is collected, processed, and stored.

#### What are cross-border data transfers?

Cross-border data transfers involve moving personal data between different countries or jurisdictions. Organizations must use legal mechanisms, like special contracts or adequacy frameworks, to comply with regulations when transferring data internationally.
