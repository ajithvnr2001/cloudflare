---
url: https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/
title: What is pseudonymization?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:09.797093+00:00
---

# What is pseudonymization?

> Source: https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  What is pseudonymization? 

Pseudonymization replaces personal information with aliases to make data sets more private. Pseudonymous data cannot be matched to an identifiable person unless it is combined with a separate set of information. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define pseudonymization 
  * Explain how pseudonymization works 
  * Describe why pseudonymization is not required by the GDPR 
  * Contrast pseudonymization vs. anonymization 



Related content  [ What is the right to be forgotten? ](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[ What is the GDPR? ](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[ Why is encryption important for privacy? ](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[ What are cookies? ](https://www.cloudflare.com/learning/privacy/what-are-cookies/)

On this page

  * What is pseudonymization?

  * How does pseudonymization work?

  * Is pseudonymization required by the GDPR?

  * What is the difference between pseudonymization and anonymization?




## What is pseudonymization?

Pseudonymization is the process of removing personal identifiers from data and replacing those identifiers with placeholder values. It is sometimes used for protecting personal [privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) or improving data security. In combination with other important privacy safeguards, such as [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/), pseudonymization can help maintain user privacy.

Generally, a "pseudonym" is a fake name used to conceal one's identity. For instance, many book authors use a pseudonym or "pen name." Data pseudonymization is somewhat like this concept, but the pseudonym values are not usually used publicly. It is also important to note that any personal information, not just a person's name, can be pseudonymized.

## How does pseudonymization work?

Imagine Alice creates an account on a [streaming](https://www.cloudflare.com/learning/video/what-is-streaming/) service. As part of the signup process, the streaming service stores her name in their database. However, the service does not record her in its personal records database (let's call this _Database 1_) as "Alice," instead using pseudonymization to change "Alice" to "Person 17332."

Database 1:

Name Account type

Person 17332 Full membership

Person 12348 Free trial

Person 74738 VIP membership

Person 78383 Full membership

A list of names and their corresponding pseudonym is kept in a separate database (let's call this _Database 2_). Someone who only had access to Database 1 would be able to view the pseudonymous data but would be unable to match that data to a specific individual, such as Alice. To do so, they would also need access to Database 2, the list of names and pseudonyms.

Database 2:

Name Pseudonym

Alice Person 17332

Bob Person 12348

Carlos Person 74738

David Person 78383

Now imagine Chuck, a rogue employee at the streaming service, steals Database 1. He analyzes the data, but cannot verify the identity of any user, because the list of pseudonyms is stored separately. He cannot do much with his stolen data unless he also steals Database 2.

In this way, pseudonymization helps protect privacy and enhance security. However, identifying someone is still possible in several ways. If the identifying data is not stored separately, individuals can be identified — for instance if Chuck steals Database 2 as well, he can easily identify Alice by name. In addition, it is often possible to identify individuals in pseudonymized data by combining the data with other external data sources (imagine if Alice had posted about having a full membership on the streaming service on social media).

Pseudonymization therefore needs to be combined with other processes and technologies in order to keep data private. For example: imagine that the streaming service uses encryption to protect Databases 1 and 2, not just pseudonymization. If Chuck steals both databases, now all he can see is:

Database 1:

Name Account type

P0kOFAw20PHbOnT7oXXvlm4 lfOkGbahX+1XCv1VECrE= nm+nauwi7eePi7ZKJH0sIeV LbxBJgixIdL1sOXvsUnw=

88X5ceFkvcYjG+WxROkAT6X Lh8wuqc3NctBP7mkIAYM= w+1iufZv3OrLPb7sESpeNIu 5kzX4IVaNYz7DhpSeFKo=

Zh3MZza5QM0Q+BtNGBx7eel MafyehzZBv5I2zdodp8E= CGDoLDA7X/poEyTI+UWa8mu C9bjmbMfAmwhrNZbjUbc=

WbAJpSq+GRuaVK5Qogdfa2t WYQq2Ge2GiS1zJsmUOG8= nm+nauwi7eePi7ZKJH0sIeV LbxBJgixIdL1sOXvsUnw=

Database 2:

Name Pseudonym

lenaV3sVToJ8FdDHNwLIMed 0AN5I+P7KSrN3nKj8WN8= P0kOFAw20PHbOnT7oXXvlm4 lfOkGbahX+1XCv1VECrE=

srS9OH6GK4qa33jgZx+24ZJ ghF1BZE9Agc825l1c0lA= 88X5ceFkvcYjG+WxROkAT6X Lh8wuqc3NctBP7mkIAYM=

ddbqSa7o561pBZzFHebo2LZ vKrgWCKj7XM1n10/waw8= Zh3MZza5QM0Q+BtNGBx7eel MafyehzZBv5I2zdodp8E=

TKtTr4dDNRd+yb6f4DzUlrg hC10OgUXlkR0X8wzkzJw= WbAJpSq+GRuaVK5Qogdfa2t WYQq2Ge2GiS1zJsmUOG8=

For this reason, encryption provides stronger protections against snoopers like Chuck. Learn more about [privacy and encryption](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/).

## Is pseudonymization required by the GDPR?

The General Data Protection Regulation ([GDPR](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)) mentions pseudonymization as one method that can be used to protect personal data, but it does not require its use. Pseudonymization is no guarantee that privacy will be preserved, nor does it guarantee that an organization will avoid violating the GDPR.

In fact, the GDPR still considers pseudonymous data to be personal data because it can be associated with a person by adding additional information. (In the example above, one could identify Alice's membership level in Database 1 by adding the information from Database 2.) The GDPR states that:

"Personal data which have undergone pseudonymisation, which could be attributed to a natural person by the use of additional information should be considered to be information on an identifiable natural person."

So while pseudonymization can be useful for protecting data, it is not sufficient on its own for maintaining privacy or for GDPR compliance.

## What is the difference between pseudonymization and anonymization?

Anonymization makes data completely anonymous. Identifying information is stripped away altogether, and unlike pseudonymization, the process ideally cannot be reversed. If the data in the example above was anonymized, all information that could identify Alice, like her name, would be removed from the database instead of it just being replaced with a pseudonym:

Name Account type

* * *

Full membership

* * *

Free trial

* * *

VIP membership

* * *

Full membership

Data anonymization helps with privacy but is not always practical or possible. If it was impossible for the example streaming service to associate accounts with specific people, they would not be able to provide their service at all.

However, there are cases when anonymization is preferable. For instance, medical researchers sometimes use aggregated healthcare data that has been anonymized in order to preserve privacy. Additionally, anonymous data can still provide valuable insights — some web analytics services anonymize their data, for instance.

But even anonymized data may not fully protect user privacy. By combining anonymized data with other data sets, by looking at the context for the data, or by using several other methods, it is sometimes possible to associate anonymous data with a specific person. Even anonymized personal data needs to be protected with encryption, [access control](https://www.cloudflare.com/learning/access-management/what-is-access-control/), and other safeguards against privacy violations.
