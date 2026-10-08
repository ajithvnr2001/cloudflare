---
url: https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/
title: What is a warrant canary? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:17.346600+00:00
---

# What is a warrant canary? | Learning Center

> Source: https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  What is a warrant canary? 

A warrant canary is a method by which a communications service provider informs users that it has NOT been served with a secret government subpoena. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a warrant canary 
  * Understand how warrant canaries work 
  * Know the legal context of warrant canaries 



Related content  [ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)

On this page

  * What is a warrant canary?

    * Warrant canary examples

  * What is a transparency report?

  * What is a government request?

  * What is a national security letter?

  * What are encryption backdoors?

  * What are Cloudflare's warrant canaries?




## What is a warrant canary?

![Warrant canary - yellow bird on blue background](https://images.ctfassets.net/slt3lc6tev37/4PSnj6JHyfPZxYhddEU3ik/b0c847134dbf1576d3b36ad33588eed8/what-is-a-warrant-canary-illustration.png)

A warrant canary is a statement that declares that an organization has not taken certain actions or received certain requests for information from government or law enforcement authorities. Many services use warrant canaries to let users know how [private](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) their data is.

Some types of law enforcement and intelligence requests come with orders prohibiting organizations from disclosing that they have been received. However, by removing the corresponding warrant canary statement from their website (or wherever it is posted), organizations can indicate that they have received such a request.

Why is it called a "canary"? The term stems from the common "canary in the coal mine" analogy, which refers to the practice of bringing canaries down into mines to help indicate the presence of deadly gas. The gas was invisible and could not be smelled, but if the canary died, the miners would know the gas was present. Similarly, some government requests are "invisible" — they cannot be announced publicly. However, a missing warrant canary indicates that such a request exists, just as a canary's death indicated the presence of deadly gas.

#### Warrant canary examples

One of the earliest examples of a warrant canary was a sign posted inside a library in the US state of Vermont in 2005. The sign simply read, "The FBI has not been here"; if the sign was taken down, the implication would be that the US Federal Bureau of Investigations (FBI) had accessed patrons' records within that library.

Here is an example of a more sophisticated warrant canary for an online service: "Our company has never installed any law enforcement software or equipment anywhere on our network." (See the Cloudflare warrant canaries section below for more examples.)

## What is a transparency report?

Warrant canaries typically appear in transparency reports. A transparency report is a report published at regular intervals by an organization, to report on law enforcement requests for information. Some transparency reports also describe how often content was removed or blocked as a result of government intervention.

When a warrant canary disappears from the latest version of a transparency report, this indicates that the statement no longer applies — in other words, a government agency has made a request as described in the canary.

You can read the [Cloudflare Transparency Report here](https://www.cloudflare.com/transparency/).

## What is a government request?

A government request is any request for information from a government agency. Government requests include requests from law enforcement agencies, which generally investigate crime, as well as requests from intelligence agencies or other government agencies with investigatory authorities. Government agencies generally must go to a court to order organizations to produce information, making it compulsory for organizations to comply. But they can also simply request information. Requests from intelligence agencies are particularly relevant for warrant canary usage because they typically cannot be announced publicly.

## What is a national security letter?

A national security letter (NSL) is a type of intelligence request specific to US intelligence agencies. NSL recipients are required to keep the fact that they have received an NSL secret so the agencies can conduct their investigations without interference and without tipping off the subject of the investigation. Federal agencies can only use NSLs to request certain types of records — they cannot request the content of communications, such as email body text or phone conversations.

## What are encryption backdoors?

[Encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) is a method of concealing information by scrambling it so that it appears to be random data. Only parties with the [encryption key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) can decrypt and view the real information.

There have been many instances when governments have asked technology service providers to introduce backdoors into their encryption. A backdoor is a built-in way to circumvent encryption, much like giving someone a master key that can open any lock within a building.

Backdoors make encryption weaker and less secure. For this reason, technology providers may include an encryption warrant canary to indicate whether or not their encryption has been weakened at the request of a government agency.

## What are Cloudflare's warrant canaries?

As of December 2020, Cloudflare has the following warrant canaries posted:

  1. Cloudflare has never turned over our encryption or authentication keys or our customers' encryption or authentication keys to anyone.
  2. Cloudflare has never installed any law enforcement software or equipment anywhere on our network.
  3. Cloudflare has never provided any law enforcement organization a feed of our customers' content transiting our network.
  4. Cloudflare has never modified customer content at the request of law enforcement or another third party.
  5. Cloudflare has never modified the intended destination of DNS responses at the request of law enforcement or another third party.
  6. Cloudflare has never weakened, compromised, or subverted any of its encryption at the request of law enforcement or another third party.



See the [Cloudflare Transparency Report](https://www.cloudflare.com/transparency/) to learn more.
