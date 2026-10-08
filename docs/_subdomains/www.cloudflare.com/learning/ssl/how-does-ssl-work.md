---
url: https://www.cloudflare.com/learning/ssl/how-does-ssl-work/
title: How Does SSL Work? | SSL Certificates and TLS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:22.921046+00:00
---

# How Does SSL Work? | SSL Certificates and TLS

> Source: https://www.cloudflare.com/learning/ssl/how-does-ssl-work/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  How does SSL work? | SSL certificates and TLS 

SSL, also known as TLS, uses encryption to keep user data secure, authenticate the identity of websites, and stop attackers from tampering with Internet communications. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what SSL/TLS means 
  * Explain how SSL/TLS keeps Internet communications secure 
  * Learn how to obtain an SSL certificate, and how SSL certificates keep user data safe 



Related content  [ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ Why use HTTPS? ](https://www.cloudflare.com/learning/ssl/why-use-https/)

On this page

  * What is SSL?

  * How does SSL/TLS work?

    * The TLS handshake

    * Symmetric encryption with session keys

  * Authenticating the origin server

  * What is an SSL certificate?

  * How does a website get an SSL certificate?

  * Is it possible to get a free SSL certificate?

  * What is the difference between HTTP and HTTPS?




## What is SSL?

[SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/) stands for Secure Sockets Layer, and it refers to a protocol for encrypting, securing, and authenticating communications that take place on the Internet. Although SSL was replaced by an updated protocol called [TLS (Transport Layer Security)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) some time ago, "SSL" is still a commonly used term for this technology.

The main use case for SSL/TLS is securing communications between a client and a server, but it can also secure email, VoIP, and other communications over unsecured networks.

Sign up

Boost performance using Cloudflare CDN

[Start for free →](https://www.cloudflare.com/plans/)

## How does SSL/TLS work?

These are the essential principles to grasp for understanding how SSL/TLS works:

  * Secure communication begins with a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/), in which the two communicating parties open a secure connection and exchange the public key

  * During the TLS handshake, the two parties generate session keys, and the session keys encrypt and decrypt all communications after the TLS handshake

  * Different session keys are used to encrypt communications in each new session

  * TLS ensures that the party on the server side, or the website the user is interacting with, is actually who they claim to be

  * TLS also ensures that data has not been altered, since a message authentication code (MAC) is included with transmissions




With TLS, both [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) data that users send to a website (by clicking, filling out forms, etc.) and the HTTP data that websites send to users is encrypted. Encrypted data has to be decrypted by the recipient using a key.

Whitepaper

Maximize the power of TLS

[Read the whitepaper →](https://www.cloudflare.com/lp/maximize-tls/)

#### The TLS handshake

TLS communication sessions begin with a TLS handshake. A TLS handshake uses something called [asymmetric encryption](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/), meaning that two different keys are used on the two ends of the conversation. This is possible because of a technique called public key cryptography.

In [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/), two keys are used: a public key, which the server makes available publicly, and a private key, which is kept secret and only used on the server side. Data encrypted with the public key can only be decrypted with the private key.

During the TLS handshake, the client and server use the public and private keys to exchange randomly generated data, and this random data is used to create new keys for encryption, called the session keys.

#### Symmetric encryption with session keys

Unlike asymmetric encryption, in symmetric encryption the two parties in a conversation use the same key. After the TLS handshake, both sides use the same session keys for encryption. Once session keys are in use, the public and private keys are not used anymore. Session keys are temporary keys that are not used again once the session is terminated. A new, random set of session keys will be created for the next session.

![Symmetric Encryption](https://images.ctfassets.net/slt3lc6tev37/1PYEAgdkoII5tQ5yzweHEX/a025977d2cb6a74df020ceb6273ae6d5/symmetric-encryption.svg)Symmetric Encryption

## Authenticating the origin server

TLS communications from the server include a message authentication code, or MAC, which is a digital signature confirming that the communication originated from the actual website. This authenticates the server, preventing [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/) and domain spoofing. It also ensures that the data has not been altered in transit.

## What is an SSL certificate?

An [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) is a file installed on a website's [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). It's simply a data file containing the public key and the identity of the website owner, along with other information. Without an SSL certificate, a website's traffic can't be encrypted with TLS.

Technically, any website owner can create their own SSL certificate, and such certificates are called self-signed certificates. However, browsers do not consider self-signed certificates to be as trustworthy as SSL certificates issued by a certificate authority.

## How does a website get an SSL certificate?

Website owners need to obtain an SSL certificate from a certificate authority, and then install it on their web server (often a web host can handle this process). A certificate authority is an outside party who can confirm that the website owner is who they say they are. They keep a copy of the certificates they issue.

## Is it possible to get a free SSL certificate?

Many certificate authorities charge for SSL certificates. To help make the Internet more secure, Cloudflare offers [free SSL certificates](https://www.cloudflare.com/application-services/products/ssl/). Cloudflare was the first Internet security and performance company to do so. Cloudflare also has worked to optimize SSL/TLS performance so that websites moving from HTTP to HTTPS do not have their [performance](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) impacted. For more information about SSL options with Cloudflare, see our [Developer documentation](https://developers.cloudflare.com/ssl/).

## What is the difference between HTTP and HTTPS?

The S in "HTTPS" stands for "secure." HTTPS is just HTTP with SSL/TLS. A website with an HTTPS address has a legitimate SSL certificate issued by a certificate authority, and traffic to and from that website is authenticated and encrypted with the SSL/TLS protocol.

To encourage the Internet as a whole to move to the more secure HTTPS, many web browsers have started to mark HTTP websites as "not secure" or "unsafe." Thus, not only is HTTPS essential for keeping users safe and user data secure, it has also become essential for building trust with users.
