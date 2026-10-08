---
url: https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/
title: What Is Asymmetric Encryption? | Asymmetric vs. Symmetric Encryption
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:53.087953+00:00
---

# What Is Asymmetric Encryption? | Asymmetric vs. Symmetric Encryption

> Source: https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is asymmetric encryption? 

Asymmetric encryption, also known as public key encryption, makes the HTTPS protocol possible. In asymmetric encryption, two keys are used instead of one. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what asymmetric encryption is 
  * Understand the difference between asymmetric and symmetric encryption 
  * Explain why asymmetric encryption is important for the TLS/SSL protocol 



Related content  [ How does public key cryptography work? ](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)

On this page

  * What is asymmetric encryption?

  * What is symmetric encryption?

  * How are asymmetric encryption and symmetric encryption used for TLS/SSL?

  * How does a cryptographic key work?

  * How does Cloudflare help web properties implement asymmetric encryption?




## What is asymmetric encryption?

There are two sides in an encrypted communication: the sender, who encrypts the data, and the recipient, who decrypts it. As the name implies, asymmetric encryption is different on each side; the sender and the recipient use two different keys. Asymmetric encryption, also known as [public key encryption](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/), uses a public key-private key pairing: data encrypted with the public key can only be decrypted with the private key.

[TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (or [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)), the protocol that makes [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) possible, relies partially on asymmetric encryption. A client will obtain a website's public key from that website's TLS certificate (or [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)) and use that to initiate secure communication. The website keeps the private key secret.

## What is symmetric encryption?

In symmetric encryption, the same key both encrypts and decrypts data. For symmetric encryption to work, the two or more communicating parties must know what the key is; for it to remain secure, no third party should be able to guess or steal the key.

## How are asymmetric encryption and symmetric encryption used for TLS/SSL?

TLS, historically known as SSL, is a protocol for encrypting communications over a network. TLS uses both asymmetric encryption and symmetric encryption. During a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/), the client and server agree upon new keys to use for symmetric encryption, called "session keys." Each new communication session will start with a new TLS handshake and use new session keys.

The TLS handshake itself makes use of asymmetric cryptography for security while the two sides generate the session keys, and in order to authenticate the identity of the website's origin server.

## How does a cryptographic key work?

A key is a string of data that, when used in conjunction with a [cryptographic algorithm](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/), encrypts or decrypts messages. Data encrypted with the key will look like a random series of characters, but anyone with the right key can put it back into plaintext form. (A key can also be used to digitally sign data, not just for encryption.)

## How does Cloudflare help web properties implement asymmetric encryption?

Cloudflare offers the use of [free SSL/TLS certificates](https://www.cloudflare.com/application-services/products/ssl/). Website owners who have signed up for Cloudflare can implement SSL/TLS with one click. This makes it easy for websites to move from [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) to HTTPS, keeping user data secure and increasing user trust.

To learn more about SSL/TLS handshakes and how they use both asymmetric and symmetric encryption, see [What happens in a TLS handshake?](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)
