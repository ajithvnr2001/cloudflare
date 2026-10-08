---
url: https://www.cloudflare.com/learning/ssl/what-is-https/
title: What is HTTPS? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:02.804517+00:00
---

# What is HTTPS? | Learning Center

> Source: https://www.cloudflare.com/learning/ssl/what-is-https/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is HTTPS? 

HTTPS is the secure version of HTTP, encrypted using TLS to protect data transmitted between a web browser and a website. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define HTTPS and how it differs from HTTP 
  * Explain why HTTPS is important for security 
  * Understand the role of encryption in HTTPS 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is TLS? ](https://www.cloudflare.com/learning/ssl/what-is-tls/)

On this page

  * What is HTTPS?

  * How does HTTPS work?

  * Why is HTTPS important? What happens if a website doesn’t have HTTPS?

    * Before encryption:

    * After encryption:

  * What port does HTTPS use?

  * How else is HTTPS different from HTTP?

  * How does a website start using HTTPS?




## What is HTTPS?

Hypertext transfer protocol secure (HTTPS) is the secure version of [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/), which is the primary protocol used to send data between a web browser and a website. HTTPS is encrypted in order to increase security of data transfer. This is particularly important when users transmit sensitive data, such as by logging into a bank account, email service, or health insurance provider.

Any website, especially those that require login credentials, should use HTTPS. In modern web browsers such as Chrome, websites that do not use HTTPS are marked differently than those that are. Look for a padlock in the URL bar to signify the webpage is secure. Web browsers take HTTPS seriously; [Google Chrome and other browsers flag all non-HTTPS websites as not secure.](https://www.cloudflare.com/learning/ssl/why-use-https/)

![Google Chrome Security Example](https://www.cloudflare.com/img/learning/security/glossary/what-is-https/not-secure.png)

## How does HTTPS work?

HTTPS uses an [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) protocol to encrypt communications. The protocol is called [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), although formerly it was known as [Secure Sockets Layer (SSL)](https://www.cloudflare.com/learning/ssl/what-is-ssl/). This protocol secures communications by using what’s known as an [asymmetric public key infrastructure](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/). This type of security system uses two different keys to encrypt communications between two parties:

  1. The private key - this key is controlled by the owner of a website and it’s kept, as the reader may have speculated, private. This key lives on a web server and is used to decrypt information encrypted by the public key.
  2. The public key - this key is available to everyone who wants to interact with the server in a way that’s secure. Information that’s encrypted by the public key can only be decrypted by the private key.



eBook

5 Ways to Maximize Security & Performance

[Get the eBook](https://www.cloudflare.com/lp/five-ways-maximize-performance/)

ebook

Everywhere security for every phase of the attack lifecycle

[Read the ebook](https://www.cloudflare.com/lp/everywhere-security-ebook/)

## Why is HTTPS important? What happens if a website doesn’t have HTTPS?

HTTPS prevents websites from having their information broadcast in a way that’s easily viewed by anyone snooping on the network. When information is sent over regular HTTP, the information is broken into packets of data that can be easily “sniffed” using free software. This makes communication over the an unsecure medium, such as public Wi-Fi, highly vulnerable to interception. In fact, all communications that occur over HTTP occur in plain text, making them highly accessible to anyone with the correct tools, and vulnerable to [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/).

With HTTPS, traffic is encrypted such that even if the packets are sniffed or otherwise intercepted, they will come across as nonsensical characters. Let’s look at an example:

#### Before encryption:
    
    
    This is a string of text that is completely readable

#### After encryption:
    
    
    ITM0IRyiEhVpa6VnKyExMiEgNveroyWBPlgGyfkflYjDaaFf/Kn3bo3OfghBPDWo6AfSHlNtL8N7ITEwIXc1gU5X73xMsJormzzXlwOyrCs+9XCPk63Y+z0=

In websites without HTTPS, it is possible for Internet service providers (ISPs) or other intermediaries to inject content into webpages without the approval of the website owner. This commonly takes the form of advertising, where an ISP looking to increase revenue injects paid advertising into the webpages of their customers. Unsurprisingly, when this occurs, the profits for the advertisements and the quality control of those advertisements are in no way shared with the website owner. HTTPS eliminates the ability of unmoderated third parties to inject advertising into web content.

![Third-party content injection](https://www.cloudflare.com/img/learning/security/glossary/what-is-https/third-party-content.png)

Image from [Ars Technica](https://arstechnica.com/information-technology/2015/08/atts-free-wi-fi-hotspot-injects-extra-ads-on-non-att-websites/)

For a full list of benefits HTTPS provides, see [Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)

Sign Up

Free SSL included with any Cloudflare plan

[Start for free](https://www.cloudflare.com/plans/)

## What port does HTTPS use?

HTTPS uses port 443. This differentiates HTTPS from HTTP, which uses port 80.

(In networking, a port is a virtual software-based point where network connections start and end. All network-connected computers expose a number of ports to enable them to receive traffic. Each port is associated with a specific process or service, and different protocols use different ports.)

## How else is HTTPS different from HTTP?

Technically speaking, HTTPS is not a separate protocol from HTTP. It is simply using TLS/SSL encryption over the HTTP protocol. HTTPS occurs based upon the transmission of [TLS/SSL certificates](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/), which verify that a particular provider is who they say they are.

When a user connects to a webpage, the webpage will send over its SSL certificate which contains the public key necessary to start the secure session. The two computers, the client and the server, then go through a process called an SSL/TLS handshake, which is a series of back-and-forth communications used to establish a secure connection. To take a deeper dive into encryption and the SSL/TLS handshake, [read about what happens in a TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/).

## How does a website start using HTTPS?

Many website hosting providers and other services will offer TLS/SSL certificates for a fee. These certificates will be often be shared amongst many customers. More expensive certificates are available which can be individually registered to particular web properties.

All websites using Cloudflare [receive HTTPS for free](https://www.cloudflare.com/application-services/products/ssl/) using a shared certificate (the technical term for this is a multi-domain SSL certificate). Setting up a free account will guarantee a web property receives continually updated HTTPS protection. You can also explore our paid plans for individual certificates and other features. In either case, a web property receives all the benefits of using HTTPS.
