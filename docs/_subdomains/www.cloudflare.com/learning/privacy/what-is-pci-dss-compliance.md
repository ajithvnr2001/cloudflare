---
url: https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/
title: What is PCI DSS compliance? | PCI DSS definition
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:09.322599+00:00
---

# What is PCI DSS compliance? | PCI DSS definition

> Source: https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  What is PCI DSS compliance? | PCI DSS definition 

To protect cardholder data, PCI-compliant companies follow a set of credit card data security standards, known as PCI DSS. Explore why PCI compliance matters to all organizations that handle or process card payments. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define the Payment Card Industry Data Security Standard (PCI DSS) 
  * Describe the origins and evolution of PCI DSS 
  * Understand the importance of PCI DSS compliance 



Related content  [ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[ What is the GDPR? ](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[ What is the CAN-SPAM Act? ](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[ What is personal information? | Personal data ](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[ What is PII (personally identifiable information)? ](https://www.cloudflare.com/learning/privacy/what-is-pii/)

On this page

  * What is PCI DSS compliance?

  * What is PCI DSS?

  * The PCI DSS framework

  * Where did the PCI standards originate?

  * How is PCI compliance enforced?

  * Can Cloudflare help customers meet PCI requirements?




## What is PCI DSS compliance?

Payment Card Industry (PCI) compliance means obeying a set of security policies for cardholder data. All organizations that process transactions with credit, debit, and/or prepaid cards are subject to PCI compliance requirements.

Credit card data needs to remain secret to be secure, and becoming PCI compliant establishes that a company can be trusted to keep that data secret. Just as a homeowner would not lend their house keys to someone they couldn’t trust with their belongings, credit card brands won't trust a merchant with payment card data if that merchant fails to keep it secure.

If a business stores, processes, or transmits credit cardholder data — whether over the Internet, by phone, in an app, on paper, or in person — they must follow a set of rules for protecting information about those payments.

Although PCI compliance is not required by US federal law, the credit card companies can impose non-compliance fees to businesses that fail to properly secure cardholder data. More critically, failing to protect cardholder data makes it easier for criminals to steal that data. Such theft is a significant risk — over the next 10 years, the global payment card industry is forecast to lose an accumulated $397 billion worldwide from fraud, according to [projections](https://www.globenewswire.com/news-release/2022/12/22/2578877/0/en/Payment-Card-Fraud-Losses-Reach-32-34-Billion.html) from the Nilson Report.

## What is PCI DSS?

PCI DSS stands for "Payment Card Industry Data Security Standard” (PCI DSS). The PCI DSS framework guides businesses with robust processes for securing cardholder transaction data and card [authentication](https://www.cloudflare.com/learning/access-management/what-is-authentication/) information. It is intended to protect both cardholder data and authentication data with requirements that help prevent, detect, and react to security incidents.

PCI compliance applies globally to every merchant who accepts credit cards, debit cards, or prepaid cards. This means businesses of all sizes, from a corner coffee shop to a multinational designer clothing brand, are subject to PCI compliance — even if they use a third party for processing transactions.

Cardholder transaction data addressed by the PCI DSS includes:

  * **Primary account number:** The account number on the card, typically 16 digits long

  * **Full name:** The name of the cardholder

  * **Expiration date:** The month and year when the card expires

  * **Service code:** The value automatically retrieved from the card’s magnetic stripe or chip for in-person transactions




Sensitive authentication data covered by the PCI DSS includes:

  * **Full track data:** The card’s magnetic stripe data or equivalent on a credit card chip

  * **Card verification code:** The three- or four-digit security code on a card, which is almost always requested for online purchases

  * **Expiration date:** The month and year when the card expires

  * **Personal Identification Number (PIN):** The unique number — typically four digits — that permits ATM withdrawals and other transactions




## The PCI DSS framework

The PCI DSS framework comprises 12 fundamental requirements (with more than 300 sub-requirements):

  * Install and maintain network security controls.

  * Do not use default vendor-supplied passwords on network-connected devices.

  * Protect stored account data via [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) or other data protection methods.

  * Strongly encrypt cardholder data across open, public networks.

  * Protect all systems and [networks](https://www.cloudflare.com/network-security/) against [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/).

  * Maintain secure systems and software.

  * Restrict system and cardholder data access on a "need to know" basis.

  * Identify users and [authenticate](https://www.cloudflare.com/learning/access-management/what-is-authentication/) system components access.

  * Control and restrict physical access to cardholder data.

  * Log and monitor access to cardholder data.

  * Test security and network systems regularly.

  * Maintain organizational an information security policy.




_Note: These are summarized versions of the standards only, not the actual standards. See the official[PCI Security Standards Council](https://www.pcisecuritystandards.org/pci_security/) website for more details._

## Where did the PCI standards originate?

PCI DSS and related security standards are administered by the PCI Security Standards Council (PCI SSC), an industry organization founded by American Express, Discover Financial Services, JCB International, MasterCard Worldwide, and Visa Inc. Participating organizations also include merchants, payment card issuing banks, processors, developers and other vendors.

The first version, PCI DSS 1.0, was introduced in 2004. In 2006, the PCI SSC released version 1.1, which asked merchants to review all online applications and establish [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/) for added security.

PCI DSS has continued to evolve over the years in response to [data breaches](https://www.cloudflare.com/learning/security/what-is-a-data-breach/) and vulnerabilities appearing across the card-processing ecosystem. The current [version 4.0](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/PCI_DSS-QRG-v4_0.pdf) became the sole active version as of March 31, 2024, when version 3.2.1 was archived.

PCI DSS v4.0 was published in 2022 to “address emerging threats and technologies and enable innovative methods to combat new threats.” Organizations have until March 31, 2025 to comply with all PCI DSS v4.0 requirements.

Although the core PCI DSS requirements have not fundamentally changed, the new v4.0 provides greater focus on how security controls should be implemented. Examples of changes include:

  * Updated firewall terminology to [network security](https://www.cloudflare.com/learning/network-layer/network-security/) controls to support a broader range of technologies

  * Expansion of requirements to implement [multifactor authentication (MFA)](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/) for all access into the cardholder data environment

  * Increased flexibility for organizations to demonstrate how they are using different methods to achieve security objectives




[Here](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v3-2-1-to-v4-0-Summary-of-Changes-r2.pdf) is a summary of the key changes from v.3.2.1 to v4.0.

## How is PCI compliance enforced?

PCI compliance is enforced by the credit card brands responsible for payment processing. When a merchant (e.g., someone who accepts payment cards as a payment method for goods and services) makes a certain number of payment card transactions per year, they are required to complete a full PCI DSS Report on Compliance. If they fail to do so, they are subject to fines.

PCI DSS penalties are based on a number of factors, such as the severity of the violation, how long it took to fix or remediate the issue, and whether there was a breach. If a company remains PCI non-compliant, there is also a chance that they won’t be able to use credit cards for any payments within their system.

PCI DSS divides companies (or "merchants," as the standards call them) into four levels based on the number of card transactions they process during a 12-month period.

The four levels* are:

  * **Level 1:** More than six million transactions per year, across all channels

  * **Level 2:** Between one million and six million transactions per year, across all channels

  * **Level 3:** Between 20,000 and one million e-commerce transactions per year

  * **Level 4:** Fewer than 20,000 ecommerce transactions per year




The way a merchant can get certified as PCI compliant changes based on their level. Generally speaking, the more transactions they handle, the more rigorous the compliance auditing requirements.

For example, Level 2-4 merchants fill out and submit an annual Self-Assessment Questionnaire (SAQ). There are different SAQ types, depending on the way the merchant processes payment card information. Organizations should refer to the [SAQ Instructions and Guidelines](https://docs-prv.pcisecuritystandards.org/SAQ%20\(Assessment\)/Instructions%20%26%20Guidance/SAQ-Instructions-Guidelines-PCI-DSS-v4-0.pdf) to help determine which (if any) SAQ applies to their organization. A summary of the differences in SAQ requirements in v4.0 can be found [here](https://blog.pcisecuritystandards.org/pci-dss-v4-whats-new-with-self-assessment-questionnaires).

Level 1 merchants (like Cloudflare), which handle more than six million transactions a year, are audited annually. Level 1 merchants must receive a Report on Compliance from a PCI SSC Qualified Security Assessor (QSA) or PCI SSC Internal Security Assessor (ISA. This process for Level 1 merchants takes place either once a year or once a quarter, depending on the card company. Level 1 merchants may also have onsite data security assessments.

Finally, all merchants need to fill out and submit an [Attestation of Compliance (AOC) form](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Reporting%20Template%20or%20Form/PCI-DSS-v4-0-ROC-AOC-Merchants-r1.pdf), which is basically a statement to the credit card company that the merchant is PCI compliant.

*_These definitions are mostly accurate, but each credit card brand defines and assesses compliance slightly differently. It is important to check with each credit card company for their specific program criteria._

## Can Cloudflare help customers meet PCI requirements?

Cloudflare maintains PCI DSS Level 1 compliance, and has been [PCI compliant](https://www.cloudflare.com/trust-hub/compliance-resources/) since 2014. Many of our customers also require that we provide a copy of our AOC, which basically tells the credit card company we are PCI compliant. If we did not have this certification, we could not work with certain customers, nor would our acquiring bank allow us to use payment cards as a payment method for our services.

We also help our customers maintain security through their own [websites](https://www.cloudflare.com/ecommerce/) and applications. Here are some examples of how Cloudflare can help businesses meet certain PCI DSS requirements:

  * Customers that use [Cloudflare Web Application Firewall](https://www.cloudflare.com/application-services/products/waf/), enable the OWASP ruleset, and tune rules for their environment will meet the need to protect web-facing applications and satisfy PCI requirement 6.4.1.

  * Cloudflare enables merchants to use the latest versions of [TLS encryption](https://www.cloudflare.com/application-services/products/ssl/), another important part of PCI compliance.

  * Many organizations rely on corporate VPNs and other segmentation tools to reduce the scope of their cardholder data environment. [Cloudflare Access](https://www.cloudflare.com/products/zero-trust/access/) provides another means of segmentation by using Cloudflare’s global network as a VPN service to access internal resources. Additionally, these sessions can be configured to time out after 15 minutes of inactivity to help customers meet requirement 8.2.8.

  * The new requirements on client-side security, 6.4.3 and 11.6.1 in PCI DSS v4.0, specify the need to know and authorize JavaScript running on all payment pages, and the need to be alerted when any of this JavaScript is changed. [Cloudflare Page Shield](https://www.cloudflare.com/page-shield/) continuously monitors entire websites beyond just payment pages, and sends an alert when any script is changed and if it is deemed [malicious](https://blog.cloudflare.com/detecting-magecart-style-attacks-for-pageshield/).




Learn more about Cloudflare’s [website and application security services](https://www.cloudflare.com/application-services/products/) and about the built-in security, privacy, and compliance functions of a [connectivity cloud](https://www.cloudflare.com/connectivity-cloud/).
