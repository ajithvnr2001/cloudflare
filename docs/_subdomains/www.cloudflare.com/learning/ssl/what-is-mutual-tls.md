---
url: https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/
title: What is mutual TLS (mTLS)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:07.762903+00:00
---

# What is mutual TLS (mTLS)?

> Source: https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is mutual TLS (mTLS)? 

Mutual TLS (mTLS) is a type of authentication in which the two parties in a connection authenticate each other using the TLS protocol. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how mutual TLS (mTLS) works 
  * Understand the difference between mutual TLS and regular TLS 
  * Illustrate how mTLS stops attacks 



On this page

  * What is mutual TLS?

  * What is TLS?

    * 1\. Public key and private key

    * 2\. TLS certificate

    * 3\. TLS handshake

  * How does mTLS work?

    * Certificate authorities in mTLS

  * Why use mTLS?

  * Websites already use TLS, so why is mTLS not used on the entire Internet?

  * How does Cloudflare use mTLS?




## What is mutual TLS (mTLS)?

Mutual TLS, or mTLS for short, is a method for [mutual authentication](https://www.cloudflare.com/learning/access-management/what-is-mutual-authentication/). mTLS ensures that the parties at each end of a network connection are who they claim to be by verifying that they both have the correct private [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/). The information within their respective [TLS certificates](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) provides additional verification.

mTLS is often used in a [Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) security framework* to verify users, devices, and servers within an organization. It can also help [keep APIs secure](https://www.cloudflare.com/application-services/solutions/api-security/)Whitepaper

Maximize the power of TLS

[Get the whitepaper](https://www.cloudflare.com/lp/maximize-tls/)

Guide

The Zero Trust guide to securing aplication access

[Read the guide →](https://www.cloudflare.com/lp/guide-to-zero-trust-access/)

## What is TLS?

[Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) is an [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) protocol in wide use on the Internet. TLS, which was formerly called [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/), authenticates the server in a [client-server](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) connection and encrypts communications between client and server so that external parties cannot spy on the communications.

There are three important things to understand about how TLS works:

#### 1\. Public key and private key

TLS works using a technique called [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/), which relies on a pair of keys — a public key and a private key. Anything encrypted with the public key can be decrypted only with the _private_ key.

Therefore, a server that decrypts a message that was encrypted with the public key proves that it possesses the private key. Anyone can view the public key by looking at the domain's or server's TLS certificate.

#### 2\. TLS certificate

A [TLS certificate](https://www.cloudflare.com/application-services/products/ssl/) is a data file that contains important information for verifying a server's or device's identity, including the public key, a statement of who issued the certificate (TLS certificates are issued by a certificate authority), and the certificate's expiration date.

#### 3\. TLS handshake

The [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) is the process for verifying the TLS certificate and the server's possession of the private key. The TLS handshake also establishes how encryption will take place once the handshake is finished.

WAF Protection

Defend against “Top 10” attack techniques

[Learn more →](https://www.cloudflare.com/application-services/products/waf/)

## How does mTLS work?

Normally in TLS, the server has a TLS certificate and a public/private key pair, while the client does not. The typical TLS process works like this:

  * Client connects to server

  * Server presents its TLS certificate

  * Client verifies the server's certificate

  * Client and server exchange information over encrypted TLS connection


![The basic steps in a TLS handshake](https://images.ctfassets.net/slt3lc6tev37/37w1tzGsD4XvYUkQCHbWG8/6fbbb48d0f5077cc2c662a4cc6817b1c/how_tls_works-what_is_mutual_tls.png)The basic steps in a TLS handshake

In mTLS, however, both the client and server have a certificate, and both sides authenticate using their public/private key pair. Compared to regular TLS, there are additional steps in mTLS to verify both parties (additional steps in **bold**):

  * Client connects to server

  * Server presents its TLS certificate

  * Client verifies the server's certificate

  * **Client presents its TLS certificate**

  * **Server verifies the client's certificate**

  * **Server grants access**

  * Client and server exchange information over encrypted TLS connection


![The basic steps in a mutual TLS \(mTLS\) handshake](https://images.ctfassets.net/slt3lc6tev37/5SjaQfZzDLEGqyzFkA0AA4/d227a26bbd7bc6d24363e9b9aaabef55/how_mtls_works-what_is_mutual_tls.png)The basic steps in a mutual TLS (mTLS) handshake

#### Certificate authorities in mTLS

The organization implementing mTLS acts as its own certificate authority. This contrasts with standard TLS, in which the certificate authority is an external organization that checks if the certificate owner legitimately owns the associated [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) (learn about [TLS certificate validation](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)).

A "root" TLS certificate is necessary for mTLS; this enables an organization to be their own certificate authority. The certificates used by authorized clients and servers have to correspond to this root certificate. The root certificate is self-signed, meaning that the organization creates it themselves. (This approach does not work for one-way TLS on the public Internet because an external certificate authority has to issue those certificates.)

## Why use mTLS?

mTLS helps ensure that traffic is secure and trusted in both directions between a client and server. This provides an additional layer of security for users who log in to an organization's network or applications. It also verifies connections with client devices that do not follow a login process, such as Internet of Things ([IoT](https://www.cloudflare.com/learning/ddos/glossary/internet-of-things-iot/)) devices.

mTLS prevents various kinds of attacks, including:

  * **On-path attacks:** [On-path attackers](https://www.cloudflare.com/learning/security/threats/on-path-attack/) place themselves between a client and a server and intercept or modify communications between the two. When mTLS is used, on-path attackers cannot authenticate to either the client or the server, making this attack almost impossible to carry out.

  * **Spoofing attacks:** Attackers can attempt to "spoof" (imitate) a web server to a user, or vice versa. Spoofing attacks are far more difficult when both sides have to authenticate with TLS certificates.

  * **Credential stuffing:** Attackers use [leaked sets of credentials](https://www.cloudflare.com/the-net/credential-stuffing/) from a [data breach](https://www.cloudflare.com/learning/security/what-is-a-data-breach/) to try to log in as a legitimate user. Without a legitimately issued TLS certificate, [credential stuffing](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/) attacks cannot be successful against organizations that use mTLS.

  * **Brute force attacks:** Typically carried out with [bots](https://www.cloudflare.com/learning/bots/what-is-a-bot/), a [brute force attack](https://www.cloudflare.com/learning/bots/brute-force-attack/) is when an attacker uses rapid trial and error to guess a user's password. mTLS ensures that a password is not enough to gain access to an organization's network. ([Rate limiting](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/) is another way to deal with this type of bot attack.)

  * **Phishing attacks:** The goal of a [phishing attack](https://www.cloudflare.com/learning/access-management/phishing-attack/) is often to steal user credentials, then use those credentials to compromise a network or an application. Even if a user falls for such an attack, the attacker still needs a TLS certificate and a corresponding private key in order to use those credentials.

  * **Malicious API requests:** When used for [API security](https://www.cloudflare.com/learning/security/api/what-is-api-security/), mTLS ensures that API requests come from legitimate, authenticated users only. This stops attackers from sending malicious API requests that aim to exploit a vulnerability or subvert the way the API is supposed to function.




## Websites already use TLS, so why is mTLS not used on the entire Internet?

For everyday purposes, one-way authentication provides sufficient protection. The goals of TLS on the public Internet are 1) to ensure that people do not visit [spoofed websites](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/), 2) to keep [private data](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) secure and encrypted as it crosses the various networks that [comprise the Internet](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/), and 3) to make sure that data is not altered in transit. One-way TLS, in which the client verifies the server's identity only, accomplishes these goals.

Additionally, distributing TLS certificates to all end user devices would be extremely difficult. Generating, managing, and verifying the billions of certificates necessary for this is a near-impossible task.

But on a smaller scale, mTLS is highly useful and quite practical for individual organizations, especially when those organizations [employ a Zero Trust approach](https://www.cloudflare.com/the-net/roadmap-zerotrust/) to network security. Since a Zero Trust approach does not trust any user, device, or request by default, organizations must be able to authenticate every user, device, and request every time they try to access any point in the network. mTLS helps make this possible by authenticating users and verifying devices.

## How does Cloudflare use mTLS?

[Cloudflare Zero Trust](https://www.cloudflare.com/sase/) uses mTLS for Zero Trust security. [Cloudflare API Shield](https://blog.cloudflare.com/introducing-api-shield/) also uses mTLS to verify API endpoints, ensuring that no unauthorized parties can send potentially malicious API requests. Learn how to [implement mTLS with Cloudflare](https://blog.cloudflare.com/using-your-devices-as-the-key-to-your-apps/).
