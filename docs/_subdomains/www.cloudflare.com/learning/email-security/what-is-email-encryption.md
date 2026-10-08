---
url: https://www.cloudflare.com/learning/email-security/what-is-email-encryption/
title: What is email encryption?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:00.311671+00:00
---

# What is email encryption?

> Source: https://www.cloudflare.com/learning/email-security/what-is-email-encryption/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is email encryption? 

Email encryption disguises the content of an email message so that it cannot be viewed or tampered with by unauthorized parties. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define ‘email encryption’ 
  * Explain how email encryption works 
  * Learn the primary types of email encryption 



Related content  [ What is email? | Email definition ](https://www.cloudflare.com/learning/email-security/what-is-email/)[ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ What is the Simple Mail Transfer Protocol (SMTP)? ](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[ What is IMAP? ](https://www.cloudflare.com/learning/email-security/what-is-imap/)

On this page

  * What is email encryption?

  * How does email encryption work?

  * Why is encryption important for email security?

  * What are some common email encryption tools?

    * STARTTLS

    * STLS

    * Pretty Good Privacy and OpenPGP

    * Secure/Multipurpose Internet Mail Extensions

    * Alternative email encryption protocols

  * Does email encryption keep email secure?




## What is email encryption?

Email encryption is a method of disguising content in an [email](https://www.cloudflare.com/learning/email-security/what-is-email/) message to prevent unauthorized parties from viewing or altering it. [Encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) disguises this content by encoding it — in other words, using a [cryptographic key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)* to change readable text into indecipherable combinations of randomized characters. Using a key, the recipient’s email provider is able to decode the text and reveal the content of the email message once it has been safely delivered to the intended inbox.

Many email providers use encryption to securely transmit messages between the sender and recipient’s email servers. This can help ensure that attackers do not intercept emails while they are in transit, allowing them to view, alter, or steal the sensitive information those messages contain. However, some email services do not offer encryption, which leaves users more vulnerable to data theft and other attacks.

*_A cryptographic key is a string of characters that a cryptographic algorithm uses to scramble data._

## How does email encryption work?

Email encryption is handled by email service providers, which are responsible for storing, transmitting, and receiving email messages between users. There are two primary methods of encrypting emails: transport-level encryption and end-to-end encryption.

**Transport-level encryption**

Transport-level encryption uses the [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) protocol to encrypt and decrypt email messages. It is also responsible for authenticating the identity of the servers involved in transmitting email messages, so that attackers cannot intercept the messages.

The process of encrypting messages and authenticating the identity of the client (i.e. user device) and web server is called a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/), which is carried out in four steps:

  * The client and server agree on the version of TLS that will be used to establish a connection.

  * The client and server agree on the cipher suite (or _algorithms_) that will be used to determine the encryption keys for that session.

  * A TLS certificate is used to verify the identity of the server.

  * Encryption keys* (also known as _[session keys](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)_) are generated and used to encrypt the message after the handshake is completed.




Transport-level encryption protects emails during the SMTP process. SMTP, or Simple Mail Transfer Protocol, is an email delivery protocol responsible for exchanging data between an email client and server. During this process, an email message is typically transferred to multiple email servers before it reaches its intended destination; TLS encryption ensures that the message is protected between relays from server to server. Each server-client or server-server connection uses a new TLS handshake process. This means that the message is briefly decrypted and then re-encrypted for each hop. (Learn more about [how SMTP works](https://www.cloudflare.com/learning/email-security/what-is-smtp/).)

To visualize this process, imagine that Alice is sending a gift from San Francisco to Tokyo. They place the gift inside a box, which keeps the contents private and secure (just as encryption keeps the content of an email message private). They give the package to a postal carrier, who delivers it to a local post office. The package is inspected to make sure that the content and the delivery information are both correct. Then, it is shipped to Tokyo, where it goes through customs and is inspected again. Finally, the package is transferred to a local post office for delivery, where it undergoes one last inspection before arriving at its intended destination.

This is similar to TLS encryption, in which an email is decrypted and re-encrypted by every server it travels to before it is delivered to its final destination.

*_A session key is a temporary cryptographic string that is used by both parties during the TLS handshake._

**End-to-end encryption**

Unlike transport-layer encryption, [end-to-end encryption](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/) (also called _E2EE_) does not decrypt and re-encrypt an email message while it is in transit. Instead, the message can only be decrypted by two parties: the sender and the final recipient of the email. This prevents third parties from intercepting an email message and snooping, altering, or copying its contents.

Like TLS encryption, E2EE uses public key encryption (or [asymmetric encryption](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)) to encrypt and secure messages between the sender and recipient. However, while TLS encrypts messages between a client and server, E2EE encrypts communication between the sender and recipient of the email — ensuring that no one, even service providers, can decrypt the message. (Learn more about how E2EE differs from TLS encryption.)

Returning to the previous example, now imagine that Alice is sending a package from one neighborhood in San Francisco to another. The package is picked up by a mail carrier and delivered directly to its final destination, without any intermediary inspections. This is similar to end-to-end encryption, in which the sender’s email message is not decrypted before it reaches its intended recipient.

## Why is encryption important for email security?

When email was first developed in the 1970s, messages between users were not encrypted. All of the content an email message contained — including any sensitive data in the body of the message — was in plaintext, meaning that anyone could easily read them. This left users vulnerable to attacks, since attackers could intercept messages and steal data without having to first decrypt them.

With the development of encryption protocols, users and email providers were able to convert plaintext messages into ciphertext, preventing unauthorized parties from snooping or stealing data via a packet sniffer (a program designed to collect and analyze data transmitted over a network).

However, while these encryption protocols play an important role in securing email from attacks, they are still vulnerable to risk.

By necessity, email messages encrypted using TLS are decrypted between server relays, making it difficult to completely shield data from [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/) (sometimes called _attacker-in-the-middle attacks_) while an email is in transit. During an on-path attack, attackers intercept sensitive data before it reaches its intended recipient.

Service providers that offer E2EE, meanwhile, may incorporate encryption backdoors into their services. A backdoor is a secret way to circumvent encryption methods and access sensitive user data. Providers may use these backdoors to spy on user activity or illegally use their data.

## What are some common email encryption tools?

Email encryption is typically handled by the service provider (e.g. Gmail) or configured by a user. Organizations that need strong encryption to protect their messages may use [gateway](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/) software or web-based services, both of which allow them to set policies to determine which emails need to be encrypted and specify the protocol that should be used to encrypt the messages.

Some of the most common encryption tools include the following:

#### STARTTLS

STARTTLS is a command that tells an email server to initiate a TLS connection. It uses **transport layer** encryption.

**STARTTLS advantages:**

  * Used to secure SMTP and [IMAP](https://www.cloudflare.com/learning/email-security/what-is-imap/) connections

  * Can be used by any email server that supports encryption, even if servers use different protocols

  * Widely supported by email providers




**STARTTLS disadvantages:**

  * Must be configured by the recipient’s email provider

  * Messages may be intercepted between SMTP relays

  * Adds latency to SMTP connections




#### STLS

STLS, like STARTTLS, is a command that initiates a TLS connection for POP3. It uses **transport layer** encryption.

**STLS advantages:**

  * Used to secure POP3 connections

  * Can be used by any email server that supports encryption, even if servers use different protocols

  * Wide support by email providers




**STLS disadvantages** are roughly the same as that of STARTTLS:

  * Must be configured by the recipient’s email provider

  * Messages may be intercepted between SMTP relays

  * Adds latency to SMTP connections




#### Pretty Good Privacy (PGP) and OpenPGP

Pretty Good Privacy (PGP) and OpenPGP are programs that use public and private key cryptography. They offer **end-to-end** encryption.

**PGP advantages:**

  * Offers digital signatures to prove the authenticity of messages

  * Compatible with most email services




**PGP disadvantages:**

  * More difficult to configure; requires users to set up a public/private key pair

  * Does not encrypt metadata (e.g. email headers)

  * Makes it possible for third parties to identify the sender and recipient of an email

  * Not compatible with other protocols

  * Does not easily integrate with email clients




#### Secure/Multipurpose Internet Mail Extensions (S/MIME)

Secure/Multipurpose Internet Mail Extensions (S/MIME) is a public key encryption standard that tells servers how to encrypt MIME data. It uses **end-to-end** encryption.

**S/MIME advantages:**

  * Uses Certificate Authorities (CAs) to authenticate messages

  * Offers digital signatures to prove the authenticity of messages

  * Widely supported by email providers




**S/MIME disadvantages:**

  * Certificates need to be renewed on an annual basis

  * Does not encrypt metadata (e.g. email headers)

  * Makes it possible for third parties to identify the sender and recipient of an email

  * Not compatible with other protocols




#### Alternative email encryption protocols

Other email encryption protocols include GNU Privacy Guard (GPG), a free alternative to PGP, and Bitmessage, an encryption protocol patterned after the cryptocurrency Bitcoin.

## Does email encryption keep email secure?

Email encryption protects the content of emails. But the content of the email messages themselves could still be insecure, or dangerous. For example, an attacker could send a fully encrypted [phishing email](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/) to an intended victim, and the encryption methods they use would do nothing to stop the victim from falling for the attack.

Email security is a broad field with multiple attack vectors to address. To learn more about keeping email inboxes secure, see [What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)
