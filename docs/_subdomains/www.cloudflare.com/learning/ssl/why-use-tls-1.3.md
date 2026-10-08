---
url: https://www.cloudflare.com/learning/ssl/why-use-tls-1.3
title: Why Use TLS 1.3? | SSL and TLS Vulnerabilities
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:18.372663+00:00
---

# Why Use TLS 1.3? | SSL and TLS Vulnerabilities

> Source: https://www.cloudflare.com/learning/ssl/why-use-tls-1.3

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  Why use TLS 1.3? 

TLS 1.3 improves over previous versions of the TLS (SSL) protocol in several important ways. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand why TLS 1.3 is faster and more secure than TLS 1.2 
  * Learn about TLS vulnerabilities 



Related content  [ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ Types of SSL certificates: SSL certificate types explained ](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)

On this page

  * What is the difference between TLS 1.3 and TLS 1.2?

  * What are the advantages of using the latest TLS version?

  * Why are there different TLS versions?

  * How do new versions of TLS get developed?

  * What is a vulnerability?

  * What are some important SSL and TLS vulnerabilities?

  * Does Cloudflare support TLS 1.3?




## What is the difference between TLS 1.3 and TLS 1.2?

TLS 1.3 is the latest version of the [TLS protocol](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/). TLS, which is used by [HTTPS](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) and other network protocols for [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/), is the modern version of [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/). TLS 1.3 dropped support for older, less secure cryptographic features, and it sped up [TLS handshakes](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/), among other improvements.

For context, the Internet Engineering Task Force (IETF) published TLS 1.3 in August 2018. TLS 1.2, the version it replaced, was standardized a decade previous, in 2008.

Sign up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What are the advantages of using the latest TLS version?

In a nutshell, TLS 1.3 is faster and more secure than TLS 1.2. One of the changes that makes TLS 1.3 faster is an update to the way a TLS handshake works: TLS handshakes in TLS 1.3 only require one round trip (or back-and-forth communication) instead of two, shortening the process by a few milliseconds. And in cases when the client has connected to a website before, the TLS handshake will have zero round trips. This makes HTTPS connections faster, cutting down [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) and improving the overall user experience.

Many of the major vulnerabilities in TLS 1.2 had to do with older cryptographic algorithms that were still supported. TLS 1.3 drops support for these vulnerable cryptographic algorithms, and as a result it is less vulnerable to cyber attacks.

Whitepaper

Maximize the power of TLS

[Read the whitepaper →](https://www.cloudflare.com/lp/maximize-tls/)

## Why are there different TLS versions?

![TLS SSL development timeline - SSL 1996 TLS 1.2 2008 TLS 1.3 2018](https://images.ctfassets.net/slt3lc6tev37/6LJWu0HvkaTE5wM0bhULyI/b2415217ca87e38cc222b8ea288ad71d/tls_ssl_development_timeline.png)TLS SSL development timeline - SSL 1996 TLS 1.2 2008 TLS 1.3 2018

Updates are a natural part of software development. Computer systems are so complex that it is inevitable that they'll need repairs or improvements to be more efficient or more secure. Any software is going to have vulnerabilities – flaws that an attacker can exploit.

In the case of TLS, parts of the protocol carried over from its early days in the 1990s resulted in several high-profile vulnerabilities persisting in TLS 1.2. Additionally, those who work on developing the protocol are continually identifying inefficiencies that can be eliminated.

## How do new versions of TLS get developed?

The IETF is in charge of developing TLS, codifying feedback and ideas via a document known as a "Request For Comments," or an RFC. Most [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) on the Internet are defined via RFCs. All RFCs are numbered; TLS 1.3 is defined by [RFC 8446](https://blog.cloudflare.com/rfc-8446-aka-tls-1-3/).

Once a new version of a protocol is released, it's up to browsers and operating systems to build support for those protocols. All operating systems and browsers should want better performance and security, so they have incentive to do so. However, it can still take some time for support for updated protocols to be widespread, especially because private businesses and consumers may be slow to adopt the latest versions of browsers, applications, and operating systems.

## What is a vulnerability?

A software vulnerability is a flaw in the design of a computer program that an attacker can take advantage of to perform malicious activity or gain illicit access. Essentially, vulnerabilities are inevitable in computer systems, just as it is practically impossible to build a bank that is impregnable to highly determined bank robbers.

The security community documents and catalogues vulnerabilities as they are discovered and described. Known vulnerabilities are assigned a number, like CVE-2016-0701. (The first number is the year when it was discovered.)

## What are some important SSL and TLS vulnerabilities?

A number of outdated cryptography features resulted in vulnerabilities or enabled specific kinds of cyber attacks. Here is a non-exhaustive list of TLS 1.2 cryptography weaknesses, and the vulnerabilities or attacks associated with them.

  * RSA key transport: [Doesn’t provide forward secrecy](https://blog.cloudflare.com/staying-on-top-of-tls-attacks/)

  * CBC mode ciphers: [BEAST](https://blog.cloudflare.com/taming-beast-better-ssl-now-available-across/) and [Lucky 13](https://en.wikipedia.org/wiki/Lucky_Thirteen_attack) attacks

  * RC4 stream cipher: [Not secure for use in HTTPS](https://blog.cloudflare.com/killing-rc4-the-long-goodbye/)

  * Arbitrary Diffie-Hellman groups: [CVE-2016-0701](http://blog.intothesymmetry.com/2016/01/openssl-key-recovery-attack-on-dh-small.html)

  * Export ciphers: [FREAK](https://censys.io/blog/freak) and [LogJam](https://blog.cloudflare.com/logjam-the-latest-tls-vulnerability-explained/) attacks




A lot of TLS 1.2 features have been removed in addition to those listed above. The idea is to make it impossible for someone to enable the vulnerable aspects of TLS 1.2. This is somewhat like when the government made it illegal to manufacture new cars without seatbelts: The goal of the regulations was for seatbelt-less cars to be phased out so that everyone would be safer. For a while, drivers could still choose to use older car models and be less safe, but eventually those more dangerous cars disappeared from the roads.

## Does Cloudflare support TLS 1.3?

Cloudflare prioritizes supporting all the latest, most secure versions of networking protocols. Cloudflare immediately offered support for TLS 1.3; in fact, Cloudflare [supported TLS 1.3 back in 2016](https://blog.cloudflare.com/introducing-tls-1-3/), before the IETF finished fine-tuning it.

For more technical details on TLS 1.3 and how it differs from TLS 1.2, see this [detailed look at TLS 1.3](https://blog.cloudflare.com/rfc-8446-aka-tls-1-3/) by Cloudflare Head of Cryptography Nick Sullivan.
