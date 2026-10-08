---
url: https://www.cloudflare.com/learning/privacy/what-is-data-localization/
title: What is data localization?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:57.682067+00:00
---

# What is data localization?

> Source: https://www.cloudflare.com/learning/privacy/what-is-data-localization/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  What is data localization? 

To localize data means to keep data within the same region it came from. Cloud computing makes data localization more complicated, but not impossible. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define data localization 
  * Compare data localization with data residency 
  * Explore the relationship between data localization and privacy 



Related content  [ What is the GDPR? ](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[ What is pseudonymization? ](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[ What is the right to be forgotten? ](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[ What are cookies? ](https://www.cloudflare.com/learning/privacy/what-are-cookies/)

On this page

  * What is data localization?

    * Data localization vs. data residency

  * When is data localization required?

  * How does data localization work?

  * Does data localization enhance privacy?




## What is data localization?

Data localization is the practice of keeping data within the region it originated from. For example, if an organization collects data in the UK, they store it in the UK rather than transferring it to another country for processing.

The Internet makes it possible for data to cross the globe in milliseconds, so where that data goes and what is done with it is of increasing interest to regulators, [privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) advocates, and consumers.

#### Data localization vs. data residency

Data localization and data residency are two terms that are sometimes used interchangeably, although they have slightly different meanings. On its own, "data residency" refers to the place where data is stored. Data residency requirements may compel organizations to change where their data resides. Data localization is the action of [complying](https://www.cloudflare.com/the-net/pursuing-privacy-first-security/data-localization/) with data residency requirements.

## When is data localization required?

Some legal standards have data residency requirements that compel organizations to localize their data. However, most data privacy frameworks do not require data localization. But even if jurisdictions do not require data localization by law, highly regulated industries like banking and healthcare may adopt best practice guidance asserting more requirements for data if it is to be processed outside its country of origin. In these cases, organizations may prefer to localize data rather than meet those additional requirements.

For many companies that operate in regions with strict data processing regulations, they may want to avoid possible violations altogether by keeping data in those regions, even if doing so does not protect the data any better.

## How does data localization work?

Data localization is fairly simple for organizations that are based in a single country or region and use on-premise infrastructure to store data. As long as their data remains secure within their data centers, it should be properly localized.

Cloud computing makes data localization more complicated. Cloud servers are accessed over the Internet and can therefore be located anywhere in the world. Organizations that rely on cloud computing have much less visibility into where their data is actually processed and stored, since the cloud computing vendor handles those decisions.

However, data localization is possible with cloud computing if the cloud vendor commits to only processing and storing data within data centers in the specified region. Not all cloud vendors have enough of a global presence to set this up, but many do.

If a cloud vendor has a data center within the required region, then there are any number of ways they can ensure a given customer's data remains in that data center.

For example, the approach that Cloudflare takes for its [Regional Services](https://blog.cloudflare.com/introducing-regional-services/) offering is to proxy [Transmission Control Protocol (TCP)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) connections to a data center in the designated region. TCP is a transport [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) used for moving data back and forth across the Internet. TCP establishes a connection between two devices — say, a user's computer and a web server — and ensures that all [packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) of data arrive successfully between those two devices.

When a person visits a website that uses Cloudflare, they are actually connecting to a Cloudflare data center, rather than the website itself. The TCP connection is established between their device and a server in a Cloudflare data center.

If the website in question wants to localize their data via Regional Services, then this TCP connection is proxied — or forwarded — to another Cloudflare server that is within the localized region. Requests from the user's device to the website can then travel to the correct region before they are processed.

Imagine a user request traveling over TCP as being like a large truck with a trailer, and each Cloudflare data center as being like a security checkpoint. Ordinarily, when a "truck" arrives at a Cloudflare checkpoint, Cloudflare opens up the trailer and takes a look inside in order to ensure nothing dangerous is contained within.

However, with data localization, Cloudflare instead checks with the driver to see if the truck is headed to certain destinations. If the destination is the address of a data localization customer, Cloudflare tells the driver to continue on to a different checkpoint. Cloudflare does not look inside the trailer until it reaches that specific checkpoint.

## Does data localization enhance privacy?

Many organizations have increasing desire for or face [compliance obligations](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/) requiring data localization. Many categories of data that Cloudflare customers process (including healthcare, legal, or financial data) may be subject to obligations that specify the data be stored or processed in a specific location. The [Cloudflare Data Localization Suite](https://www.cloudflare.com/data-localization/) helps organizations that need to follow data localization requirements.

However, protecting user privacy is a complex issue, and multiple factors impact how private data is. For example, data localization does not ensure the use of [encryption, which is crucial for privacy](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/). If a user visits a website that localizes data and keeps that user's data within the same region, the data localization does not matter if the website does not use encrypted [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/). Data localization also would not stop a company from selling data to third parties within the same region, which could be seen as a privacy-violating act. Nor would it prevent unauthorized users within a company from accessing private data.

Therefore, data localization alone does not ensure that data remains private. Learn more about [data privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/).

Learn more about the built-in security, privacy, and compliance functions of a [connectivity cloud](https://www.cloudflare.com/connectivity-cloud/).
