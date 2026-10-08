---
url: https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/
title: What is end-to-end encryption (E2EE)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:01.197636+00:00
---

# What is end-to-end encryption (E2EE)?

> Source: https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/

[ Learning Center ](https://www.cloudflare.com/learning/) / privacy

##  What is end-to-end encryption (E2EE)? 

End-to-end encryption prevents messaging services from spying on private correspondence between users. 

[Learning Center](https://www.cloudflare.com/learning)/privacy/[Why is encryption important for privacy?](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[What is the right to be forgotten?](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[What are the Fair Information Practices? | FIPPs](https://www.cloudflare.com/learning/privacy/what-are-fair-information-practices-fipps/)[What is data compliance?](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/)[What is data governance?](https://www.cloudflare.com/learning/privacy/what-is-data-governance/)[What is data localization?](https://www.cloudflare.com/learning/privacy/what-is-data-localization/)[What is data privacy?](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)[What is data sovereignty?](https://www.cloudflare.com/learning/privacy/what-is-data-sovereignty/)[What is end-to-end encryption (E2EE)?](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/)[What is the ePrivacy Directive?](https://www.cloudflare.com/learning/privacy/what-is-eprivacy-directive/)[What is FedRAMP?](https://www.cloudflare.com/learning/privacy/what-is-fedramp/)[What is HIPAA compliance?](https://www.cloudflare.com/learning/privacy/what-is-hipaa-compliance/)[What is PCI DSS compliance? | PCI DSS definition](https://www.cloudflare.com/learning/privacy/what-is-pci-dss-compliance/)[What is personal information? | Personal data](https://www.cloudflare.com/learning/privacy/what-is-personal-information/)[What is PII (personally identifiable information)?](https://www.cloudflare.com/learning/privacy/what-is-pii/)[What is pseudonymization?](https://www.cloudflare.com/learning/privacy/what-is-pseudonymization/)[What is SOX compliance?](https://www.cloudflare.com/learning/privacy/what-is-sox-compliance/)[What is the CAN-SPAM Act?](https://www.cloudflare.com/learning/privacy/what-is-the-can-spam-act/)[What is the CCPA (California Consumer Privacy Act)?](https://www.cloudflare.com/learning/privacy/what-is-the-ccpa/)[What is the GDPR?](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/)[What are cookies?](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[What is a warrant canary?](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how end-to-end encryption works 
  * Compare end-to-end encryption with other types of encryption 
  * Understand the privacy implications of end-to-end encryption 



Related content  [ Why is encryption important for privacy? ](https://www.cloudflare.com/learning/privacy/encryption-and-privacy/)[ What are cookies? ](https://www.cloudflare.com/learning/privacy/what-are-cookies/)[ What is a warrant canary? ](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/)[ What is the right to be forgotten? ](https://www.cloudflare.com/learning/privacy/right-to-be-forgotten/)[ What is data privacy? ](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)

On this page

  * What is end-to-end encryption?

  * What is unique about end-to-end encryption vs. other types of encryption?

  * How does encryption work?

  * What kind of encryption does E2EE use?

  * What is the difference between E2EE and TLS?

  * How does end-to-end encryption support privacy?

  * What are the limitations of end-to-end encryption?

  * What are end-to-end encryption backdoors?




## What is end-to-end encryption?

End-to-end encryption (E2EE) is a type of messaging that keeps messages private from everyone, including the messaging service. When E2EE is used, a message only appears in decrypted form for the person sending the message and the person receiving the message. The sender is one "end" of the conversation and the recipient is the other "end"; hence the name "end-to-end."

Think of end-to-end encryption as being like a letter that goes through the mail in a sealed envelope. The person sending the letter is able to read it, and the person who receives it can open it and read it. Postal service employees cannot read the letter because it remains sealed in the envelope.

## What is unique about end-to-end encryption vs. other types of encryption?

Many messaging services offer encrypted communications without true end-to-end encryption. A message is encrypted as it travels from the sender to the service's server, and from the server to the recipient, but when it reaches the server, it is decrypted briefly before being re-encrypted. (This is the case with the common encryption protocol [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) — learn more below.)

Imagine if there was a postal service that, after accepting someone's letter for delivery, opened the envelope and transferred the letter to a new envelope before delivering it to the recipient. The letter's contents could be exposed to the postal service's employees.

The service can promise that it will not read the message in its decrypted form — just as the postal service in the example above might promise that its employees will never read letters while they are transferred to their new envelope. But someone sending a message still has to trust that the messaging service will keep its promise.

E2EE is "end-to-end" because it is impossible for anyone in the middle to decrypt the message. Users do not have to trust that the service they are using will not read their messages: it is not possible for the service to do so. Imagine if, instead of sending a letter in an envelope, someone sent it in a locked box to which only they had the key. Now it would be physically impossible for anyone to read the letter aside from its intended recipient. This is how E2EE works.

## How does encryption work?

[Encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) works by altering data so that only someone who possesses a specific piece of knowledge — known as the [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) — can interpret the data. Suppose Alice sends Bob a message, but Chuck steals the message on its way to Bob. If Alice encrypted the message using a key that she and Bob both have, Chuck cannot read it, and Alice's message remains secure. If instead the message reaches Bob, Bob is able to decrypt the message using the key that he possesses, and he can read it.

Keys can take different forms in different contexts. In the example above, a key may be as simple as a set of instructions for decrypting Alice's message. With communications over the Internet, a key is a string of bits that plays a role in the complex mathematical equations used to scramble and unscramble data.

With E2EE, the key that can encrypt and decrypt messages remains saved on a user's device. If Alice and Bob use an E2EE messaging app, the app saves a key on Alice's phone and a key on Bob's phone. Alice's phone encrypts her message with the key, then transmits the encrypted message to Bob's phone. Bob's phone automatically applies the key and decrypts the message, allowing Bob to read it.

## What kind of encryption does E2EE use?

End-to-end encryption uses a specialized form of encryption called [public key encryption](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) (also sometimes called [asymmetric encryption](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)). Public key encryption enables two parties to communicate without having to send the secret key over an insecure channel.

Public key encryption relies on using two keys instead of one: a public key and a private key. While anyone, including the messaging service, can view the public key, only one person knows the private key. Data encrypted with the public key can only be decrypted with the private key (not the public key). This contrasts with symmetric encryption, where only one key is used to both encrypt and decrypt.

Suppose Alice and Bob need to change the key they are using to encrypt their communications. Should Alice simply send Bob a new key? No, because Chuck might steal and duplicate the new key on its way to Bob, and then he could decrypt all their future communications. Instead, Alice and Bob decide to use public key encryption. Alice keeps a private key for herself and sends a public key to Bob — this way, it does not matter if Chuck steals the key in transit, because only Alice has the private key.

## What is the difference between E2EE and TLS?

Transport Layer Security (TLS) is an encryption protocol that, like E2EE, uses public key encryption and ensures that no intermediary parties can read messages.

However, TLS is implemented between a user and a server, not between two users. This keeps data secure in transit to and from a server, but the data on the server itself is in decrypted form. This is often necessary — for example, if a user is using a web application, the server needs access to their data in order for the application to function. However, from a privacy standpoint, this is not appropriate in all situations. For instance, if users want to message each other, they may not want the service provider to be able to see their messages.

## How does end-to-end encryption support privacy?

E2EE ensures that no one can see messages except for the two people who are communicating with each other (provided that the devices they are using are not compromised or stolen). When implemented properly, it does not require users to trust that a service will handle their data properly. Thus, E2EE gives people total control over who can read their messages, enabling them to keep their messages private.

## What are the limitations of end-to-end encryption?

E2EE keeps messages secure in transit (as they pass from one person to another). But it does not protect messages once they reach their destination.

Suppose Alice and Bob are using an E2EE app, but Chuck steals Bob's phone. Now Chuck can see Alice's messages to Bob. If Chuck does not want to bother stealing Bob's phone, he could also sneak up behind Bob and look over his shoulder to read Alice's messages. Or, he could try to infect Bob's phone with [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/) in order to steal Alice's messages. Either way, E2EE alone does not protect Bob from these kinds of attacks.

Finally, E2EE is not guaranteed to be future-proof. When implemented correctly, modern encryption methods are strong enough to resist encryption-breaking efforts from even the most powerful computers in the world. But computers may become more powerful in the future. [Quantum computers](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/), if developed, would be able to crack modern encryption algorithms. Using E2EE keeps messages secure in the present, but it may not keep them secure permanently.

## What are end-to-end encryption backdoors?

In cybersecurity, a backdoor is a way around a system's normal security measures. Imagine a completely secured building with multiple locks on all the doors — except for a hidden door in the back that is left unlocked, and that only a few people know about. An encryption backdoor is sort of like that; it is a secret way to access data that has been "locked" by encryption. Some encryption backdoors are in fact intentionally built into a service to allow the service provider to see the encrypted data.

There have been a few cases where a service claimed to offer secure E2EE messaging, but actually had built a backdoor into their service. They may do this for a variety of reasons: to access user messages and scan them for fraud or other illegal activities, or to outright spy on their users. Users should make sure to carefully review a service's Terms of Service and [warrant canaries](https://www.cloudflare.com/learning/privacy/what-is-warrant-canary/) if they want to keep their messages private.

Some have argued that E2EE service providers should build backdoors into their encryption so that law enforcement agencies can view user messages when necessary. [Data privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) advocates tend to disagree, since backdoors weaken encryption and decrease user privacy.

One of Cloudflare's warrant canaries states: "Cloudflare has never weakened, compromised, or subverted any of its encryption at the request of law enforcement or another third party." See the [Cloudflare Transparency Report](https://www.cloudflare.com/transparency/) to learn more.
