---
url: https://www.cloudflare.com/learning/privacy/encryption-and-privacy/
title: Why is encryption important for privacy?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:09.808317+00:00
---

# Why is encryption important for privacy?

> Source: https://www.cloudflare.com/learning/privacy/encryption-and-privacy/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  Why is encryption important for privacy? 

Encryption protects data that travels on the Internet from eavesdroppers or attackers. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how encryption protects privacy 
  * Understand how encryption works 
  * Identify some steps users should take to make sure their online activities are encrypted 



Related content  [ What is end-to-end encryption (E2EE)? ](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[ What are cookies? ](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[ What is the right to be forgotten? ](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[ What is a warrant canary? ](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

On this page

  * Why is encryption important for online privacy?

  * What is encryption?

  * How does Transport Layer Security protect user privacy?

  * How does DNS over HTTPS help protect user privacy?

  * What does Cloudflare do to support online privacy?




## Why is encryption important for online privacy?

[Data privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) is the ability to control who can see your personal information. On the Internet, [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) is what makes data privacy possible. Without encryption, Internet browsing information is potentially shared with third parties as information passes between networks. What's more, users do not have the chance to agree to this information sharing.

With encryption, Internet browsing information is only shared between those who have the [encryption key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/). The only two parties who should have access to the key are the user (or actually the user's device) and the website they are visiting. What the website does with the user's browsing information is a separate and important privacy question, but encryption still protects data "in transit" — as it crosses the Internet from users to websites and back.

As users browse the Internet, their devices send requests out to various web servers, and those web servers send responses in reply. Both requests and responses travel across several different networks, all of which can view the contents of the requests and responses unless the data within is encrypted. In the course of their normal activities, users regularly share personal and sensitive information on the Internet, often without realizing it, making encryption all the more important.

## What is encryption?

Encryption conceals data by scrambling it, so that anyone who tries to view it sees only random information. Encrypted data can only be unscrambled through the process of decryption.

Encryption is essential for protecting users' online activities. People are able to go online to shop, look up ailments, and search for a life partner because encryption prevents an eavesdropper from seeing what they are doing.

Encryption works by using a key: a string of characters used within an encryption algorithm for altering data so that it appears random. Like a physical key, an encryption key locks (encrypts) data so that only the right key can unlock (decrypt) it.

To understand how encryption enables privacy, consider this example. Suppose Alice and Bob are in class together and Alice wants to pass a note to Bob. However, Chuck sits in between Alice and Bob, and she wants to keep her message private from Chuck. Fortunately, she and Bob have worked out a system for sending secret messages by replacing letters in the following way:
    
    
    A=Z
    B=A
    C=B
    D=C
    

And so on. In this case, the key is "1" and the encryption algorithm is "letter - 1": each letter is moved back one position to the previous letter in the alphabet. By using this system, Alice's message of "HELLO BOB" is changed to "GDKKN ANA." All Chuck can see as he passes Alice's note from her to Bob is this nonsense combination of letters. Bob, however, knows the key Alice has used, knows to move each letter one position forward, and is able to change the message back to "HELLO BOB."

In this scenario, Alice encrypted her message to Bob, and Bob was able to decrypt and read it. This kept Alice's message private from Chuck.

Alice used a very simple encryption cipher, but modern-day encryption algorithms are much more complex. Today's encryption methods are able to stand up to intensive analysis by those who wish to decode messages. This prevents intermediary networks, Internet service providers, and any potential snoopers from being able to read requests and responses on the Internet.

In addition, many modern-day encryption methods rely on using two keys instead of one, a technique called "public key encryption." Learn more about [public key encryption](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/).

## How does Transport Layer Security (TLS) protect user privacy?

The Internet, as originally constructed, allowed anyone to see the traffic passing through networks in plaintext. Over the last several decades, encryption protocols have been introduced to help keep user activities private.

Transport Layer Security ([TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)) is the most widely used protocol for online encryption. TLS is sometimes called Secure Sockets Layer ([SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)), but this name refers to an older version of the protocol that is now out of date.

A website that uses TLS to encrypt data in transit, protecting user privacy, is said to use [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/): the secure version of the HTTP protocol. For this reason, websites with encryption have http**s** :// at the front of their URL, not http://. However, many modern browsers instead show a lock in the URL bar to indicate that the website is secure, rather than showing the full URL. Users should look for either this lock or for "https" to make sure the website they are visiting protects their privacy.

![website with HTTPS](https://images.ctfassets.net/slt3lc6tev37/2mkpUOPzl2jEPEERn2e57B/3b180ecab3ff7e0a5da1706434722573/ssl-certificate-secure-browsing.png)website with HTTPS

## How does DNS over HTTPS help protect user privacy?

Users who are concerned about privacy can use [DNS over HTTPS](https://www.cloudflare.com/learning/dns/dns-over-tls/) for their [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) queries. DNS over HTTPS encrypts DNS queries so that no one can spy on which websites users are visiting. Support for DNS over HTTPS in browsers is growing.

## What does Cloudflare do to support online privacy?

As part of Cloudflare's commitment to data privacy, Cloudflare continues to research encryption methods and privacy-enhancing technologies. Learn about Cloudflare's latest efforts [on our blog](https://blog.cloudflare.com/tag/encryption/).

In addition, Cloudflare was the first vendor to offer free TLS encryption to websites. Cloudflare has the ability to enforce encrypted connections for users visiting web properties protected by Cloudflare. And Cloudflare has long supported both DNS over HTTPS and DNS over TLS for DNS resolution.
