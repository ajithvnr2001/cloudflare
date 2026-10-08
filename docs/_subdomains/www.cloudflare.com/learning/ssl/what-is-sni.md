---
url: https://www.cloudflare.com/learning/ssl/what-is-sni/
title: What Is SNI? How TLS Server Name Indication Works
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:13.033925+00:00
---

# What Is SNI? How TLS Server Name Indication Works

> Source: https://www.cloudflare.com/learning/ssl/what-is-sni/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is SNI? How TLS server name indication works 

SNI, or Server Name Indication, is an addition to the TLS encryption protocol that enables a client device to specify the domain name it is trying to reach in the first step of the TLS handshake, preventing common name mismatch errors. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain what a virtual hostname is 
  * Understand why a server might provide the wrong SSL certificate 
  * Learn how SNI fixes this problem 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ Types of SSL certificates: SSL certificate types explained ](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[ How does public key cryptography work? ](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[ What is a session key? Session keys and TLS handshakes ](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)

On this page

  * What is SNI?

  * What is a server name?

  * What does the TLS SNI extension do?

  * What is a hostname? What is a virtual hostname?

  * What is encrypted SNI?

  * What happens if a user&#39




## What is SNI (Server Name Indication)?

SNI is somewhat like mailing a package to an apartment building instead of to a house. When mailing something to someone's house, the street address alone is enough to get the package to the right person. But when a package goes to an apartment building, it needs the apartment number in addition to the street address; otherwise, the package might not go to the right person or might not be delivered at all.

Many web servers are more like apartment buildings than houses: They host several domain names, and so the IP address alone is not enough to indicate which domain a user is trying to reach. This can result in the server showing the wrong [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/), which prevents or terminates an HTTPS connection – just like a package can't be delivered to an address if the correct person doesn't sign for it.

When multiple websites are hosted on one server and share a single IP address, and each website has its own SSL certificate, the server may not know which SSL certificate to show when a client device tries to securely connect to one of the websites. This is because the SSL/TLS handshake occurs before the client device indicates over HTTP which website it's connecting to.

Server Name Indication (SNI) is designed to solve this problem. SNI is an extension for the [TLS protocol](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (formerly known as the [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/) protocol), which is used in HTTPS. It's included in the [TLS/SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) process in order to ensure that client devices are able to see the correct SSL certificate for the website they are trying to reach. The extension makes it possible to specify the hostname, or [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/), of the website during the TLS handshake, instead of when the [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) connection opens after the handshake.

More simply put, SNI makes it possible for a user device to open a secure connection with <https://www.example.com> even if that website is hosted in the same place (same IP address) as <https://www.something.com>, <https://www.another-website.com>, and <https://www.example.io>.

SNI prevents what's known as a "common name mismatch error": when a [client (user) device](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) reaches the right [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) for a website, but the name on the SSL certificate doesn't match the name of the website. Often this kind of error results in a "[Your connection is not private](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)" error message in the user's browser.

SNI was added as an extension to TLS/SSL in 2003; it was not originally a part of the protocol. Almost all browsers, operating systems, and web servers support it, with the exception of some of the very oldest browsers and operating systems that are still in use.

Sign up

Increase security and trust using Cloudflare's free SSL / TLS

[Start for free →](https://www.cloudflare.com/plans/)

## What is a server name?

Although SNI stands for Server Name Indication, what SNI actually "indicates" is a website's hostname, or domain name, which can be separate from the name of the web server that is actually hosting the domain. In fact, it is common for multiple domains to be hosted on one server – in which case they are called virtual hostnames.

A server name is simply the name of a computer. For web servers this name is typically not visible to end users unless the server hosts only one domain and the server name is equivalent to the domain name.

## What does the TLS SNI extension do?

Often a web server is responsible for multiple hostnames – or domain names (which are the human-readable names of websites). Each hostname will have its own SSL certificate if the websites use [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/).

The problem is, all these hostnames on one server are at the same IP address. This isn't a problem over HTTP, because as soon as a [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) connection is opened the client will indicate which website they're trying to reach in an HTTP request.

But in HTTPS, a TLS handshake takes place first, before the HTTP conversation can begin (HTTPS still uses HTTP – it just encrypts the HTTP messages). Without SNI, then, there is no way for the client to indicate to the server which hostname they're talking to. As a result, the server may produce the SSL certificate for the wrong hostname. If the name on the SSL certificate does not match the name the client is trying to reach, the client browser returns an error and usually terminates the connection.

SNI adds the domain name to the TLS handshake process, so that the TLS process reaches the right domain name and receives the correct SSL certificate, enabling the rest of the TLS handshake to proceed as normal.

Specifically, SNI includes the hostname in the Client Hello message, or the very first step of a TLS handshake.

Whitepaper

Maximize the power of TLS

[Read the whitepaper →](https://www.cloudflare.com/lp/maximize-tls/)

## What is a hostname? What is a virtual hostname?

A hostname is the name of a device that connects to a network. In the context of the Internet, a domain name, or the name of a website, is a type of hostname. Both are separate from the IP address associated with the domain name.

A virtual hostname is a hostname that doesn't have its own IP address and is hosted on a server along with other hostnames. It is "virtual" in that it doesn't have a dedicated physical server, just as virtual reality exists only digitally, not in the physical world.

## What is encrypted SNI (ESNI)?

[Encrypted SNI (ESNI)](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/) adds on to the SNI extension by encrypting the SNI part of the Client Hello. This prevents anyone snooping between the client and server from being able to see which certificate the client is requesting, further protecting and securing the client. Cloudflare and Mozilla Firefox launched support for ESNI in 2018.

## What happens if a user's browser does not support SNI?

In this rare case, the user will likely be unable to reach certain websites, and the user's browser will return an error message like "Your connection is not private."

The vast majority of browsers and operating systems support SNI. Only very old versions of Internet Explorer, old versions of the BlackBerry operating system, and other outdated software versions do not support SNI.

To learn more about the TLS/SSL protocol, SSL certificates, and how HTTPS works, see [What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) or get a [free SSL certificate](https://www.cloudflare.com/application-services/products/ssl/) from Cloudflare.
