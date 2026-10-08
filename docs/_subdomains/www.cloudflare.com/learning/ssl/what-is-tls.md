---
url: https://www.cloudflare.com/learning/ssl/what-is-tls/
title: What is Transport Layer Security? | TLS protocol
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:15.416923+00:00
---

# What is Transport Layer Security? | TLS protocol

> Source: https://www.cloudflare.com/learning/ssl/what-is-tls/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is TLS (Transport Layer Security)? 

TLS is a security protocol that provides privacy and data integrity for Internet communications. Implementing TLS is a standard practice for building secure web apps. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define Transport Layer Security (TLS) 
  * Explain how TLS works 
  * Differentiate between TLS and SSL 
  * Understand how TLS affects performance 
  * Outline how to implement TLS 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[ What is asymmetric encryption? ](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)

On this page

  * What is Transport Layer Security?

  * What is the difference between TLS and SSL?

  * What is the difference between TLS and HTTPS?

  * Why should businesses and web applications use the TLS protocol?

  * What does TLS do?

  * What is a TLS certificate?

  * How does TLS work?

  * How does TLS affect web application performance?

  * How to start implementing TLS on a website




## What is Transport Layer Security (TLS)?

Transport Layer Security, or TLS, is a widely adopted security [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) designed to facilitate privacy and data security for communications over the Internet. A primary use case of TLS is encrypting the communication between web applications and servers, such as web browsers loading a website. TLS can also be used to encrypt other communications such as email, messaging, and [voice over IP (VoIP)](https://www.cloudflare.com/learning/video/what-is-voip/). In this article we will focus on the role of TLS in [web application security](https://www.cloudflare.com/learning/security/what-is-web-application-security/).

TLS was proposed by the Internet Engineering Task Force (IETF), an international standards organization, and the first version of the protocol was published in 1999. The most recent version is [TLS 1.3](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3/), which was published in 2018.

Whitepaper

Maximize the power of TLS

[Get the report →](https://www.cloudflare.com/lp/maximize-tls/)

## What is the difference between TLS and SSL?

TLS evolved from a previous encryption protocol called Secure Sockets Layer ([SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)), which was developed by Netscape. TLS version 1.0 actually began development as SSL version 3.1, but the name of the protocol was changed before publication in order to indicate that it was no longer associated with Netscape. Because of this history, the terms TLS and SSL are sometimes used interchangeably.

Secure SSL

Free SSL included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is the difference between TLS and HTTPS?

[HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) is an implementation of TLS encryption on top of the [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) protocol, which is used by all websites as well as some other web services. Any website that uses HTTPS is therefore employing TLS encryption.

## Why should businesses and web applications use the TLS protocol?

TLS encryption can help protect web applications from [data breaches](https://www.cloudflare.com/learning/security/what-is-a-data-breach/) and other attacks. Today, TLS-protected HTTPS is a standard practice for websites. The Google Chrome browser gradually [cracked down on non-HTTPS sites](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/), and other browsers have followed suit. Everyday Internet users are more wary of websites that do not feature the HTTPS padlock icon.

![SSL Certificate Secure Browsing](https://images.ctfassets.net/slt3lc6tev37/2mkpUOPzl2jEPEERn2e57B/3b180ecab3ff7e0a5da1706434722573/ssl-certificate-secure-browsing.png)SSL Certificate Secure Browsing

## What does TLS do?

There are three main components to what the TLS protocol accomplishes: [Encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/), Authentication, and Integrity.

  * **Encryption:** hides the data being transferred from third parties.

  * **Authentication:** ensures that the parties exchanging information are who they claim to be.

  * **Integrity:** verifies that the data has not been forged or tampered with.




## What is a TLS certificate?

For a website or application to use TLS, it must have a TLS certificate installed on its [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) (the certificate is also known as an "[SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)" because of the naming confusion described above). A TLS certificate is issued by a certificate authority to the person or business that owns a domain. The certificate contains important information about who owns the domain, along with the server's public key, both of which are important for validating the server's identity.

## How does TLS work?

A TLS connection is initiated using a sequence known as the [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/). When a user navigates to a website that uses TLS, the TLS handshake begins between the user's device (also known as the _client_ device) and the web server.

During the TLS handshake, the user's device and the web server:

  * Specify which version of TLS (TLS 1.0, 1.2, 1.3, etc.) they will use

  * Decide on which cipher suites (see below) they will use

  * Authenticate the identity of the server using the server's TLS certificate

  * Generate session keys for encrypting messages between them after the handshake is complete




The TLS handshake establishes a cipher suite for each communication session. The cipher suite is a set of algorithms that specifies details such as which shared [encryption keys](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/), or [session keys](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/), will be used for that particular session. TLS is able to set the matching session keys over an unencrypted channel thanks to a technology known as [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/).

The handshake also handles authentication, which usually consists of the server proving its identity to the client. This is done using public keys. Public keys are encryption keys that use one-way encryption, meaning that anyone with the public key can unscramble the data encrypted with the server's private key to ensure its authenticity, but only the original sender can encrypt data with the private key. The server's public key is part of its TLS certificate.

Once data is encrypted and authenticated, it is then signed with a message authentication code (MAC). The recipient can then verify the MAC to ensure the integrity of the data. This is kind of like the tamper-proof foil found on a bottle of aspirin; the consumer knows no one has tampered with their medicine because the foil is intact when they purchase it.

![The TCP Handshake](https://images.ctfassets.net/slt3lc6tev37/3wZIhjRIjfVSmCbVqkBKzb/4a7aa34324108c725dc25fc9e7c4ea4a/tls-ssl-handshake.png)The TCP Handshake

## How does TLS affect web application performance?

The latest versions of TLS hardly impact web application performance at all.

Because of the complex process involved in setting up a TLS connection, some load time and computational power must be expended. The [client and server](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) must communicate back and forth several times before any data is transmitted, and that eats up precious milliseconds of load times for web applications, as well as some memory for both the client and the server.

However, there are technologies in place that help to mitigate potential [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) created by the TLS handshake. One is TLS False Start, which lets the server and client start transmitting data before the TLS handshake is complete. Another technology to speed up TLS is TLS Session Resumption, which allows clients and servers that have previously communicated to use an abbreviated handshake.

These improvements have helped to make TLS a very fast protocol that should not noticeably affect [load times](https://www.cloudflare.com/learning/performance/why-site-speed-matters/). As for the computational costs associated with TLS, they are mostly negligible by today’s standards.

TLS 1.3, released in 2018, has made TLS even faster. TLS handshakes in TLS 1.3 only require one round trip (or back-and-forth communication) instead of two, shortening the process by a few milliseconds. When the user has connected to a website before, the TLS handshake has zero round trips, speeding it up still further.

## How to start implementing TLS on a website

Cloudflare offers [free TLS/SSL certificates](https://www.cloudflare.com/application-services/products/ssl/) to all users. Anyone who does not use Cloudflare will have to acquire an SSL certificate from a certificate authority, often for a fee, and install the certificate on their [origin servers](https://www.cloudflare.com/learning/cdn/glossary/origin-server/).

For more on how TLS/SSL certificates work, see [What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)
