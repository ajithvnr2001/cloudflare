---
url: https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/
title: What is encrypted SNI? | How ESNI works
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:00.982082+00:00
---

# What is encrypted SNI? | How ESNI works

> Source: https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is encrypted SNI? | How ESNI works 

Encrypted server name indication (ESNI) helps keep user browsing private. It does this by encrypting a previously unencrypted part of the TLS handshake that can reveal which website a user is visiting. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn why ESNI is necessary for privacy and security 
  * Understand how ESNI works using public key cryptography and DNS records 
  * Explore additional privacy-focused protocols for secure web browsing 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ Types of SSL certificates: SSL certificate types explained ](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)

On this page

  * What is encrypted SNI?

  * What is TLS?

  * How does server name indication work?

  * How does encrypted SNI work?

  * Does ESNI alone keep web browsing private?

  * What is Encrypted Client Hello?

  * Does Cloudflare support ESNI?




## What is encrypted SNI (ESNI)?

Encrypted server name indication (ESNI) is an essential feature for keeping user browsing data private. It ensures that snooping third parties cannot spy on the [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) process to determine which websites users are visiting. ESNI, as the name implies, accomplishes this by encrypting the [server name indication (SNI)](https://www.cloudflare.com/learning/ssl/what-is-sni/) part of the TLS handshake.

SNI tells a web server which [TLS certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) to show at the start of a connection between the client and server. SNI is an addition to the TLS protocol that enables a server to host multiple TLS certificates at the same [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/).

Think of SNI as being like the apartment number on a mailing address: multiple apartments are in one building, so each apartment needs a different number to distinguish it. Similarly, while the server is indicated by the IP address, a client device needs to include SNI in its first message to the server to indicate which website (which apartment) it is trying to reach.

## What is TLS?

Transport Layer Security, or [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) for short, is an [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) protocol that keeps communications private and secure on the Internet. TLS is used mostly to encrypt the communication between applications and web servers, like when web browsers load a website. All websites that use TLS must have a TLS certificate. TLS is sometimes called SSL, although [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/) is an outdated name for the protocol.

All TLS connections start with something called a "handshake." Just as a handshake is used in real life when two people meet and exchange introductions, the TLS handshake is a series of introductory communications between a client device (like a user's smartphone) and a web application or website. During a TLS handshake, the two communicating devices agree on what [encryption keys](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) to use, among other steps. Despite the number of steps involved, a TLS handshake takes only a few milliseconds.

## How does server name indication (SNI) work?

SNI is a small but crucial part of the first step of the TLS handshake. The first message in a TLS handshake is called the "client hello." As part of this message, the client asks to see the web server's TLS certificate. The server is supposed to send the certificate as part of its reply.

The problem is, many web servers host more than one website, and each website may have its own TLS certificate. If the server shows the wrong one to the client, then the client will be unable to connect securely to the desired website, resulting in a "[Your connection is not private" error](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/).

SNI solves this problem by indicating which website the client is trying to reach. Paradoxically, no encryption can take place until after the TLS handshake is successfully completed using SNI. As a result, regular SNI is not encrypted because the client hello message is sent at the start of the TLS handshake. Any attacker monitoring the connection between the client and the server could determine which website the client was connecting with by reading the SNI part of the handshake, even though all further communications are indecipherable to the attacker. (Attackers could use this information in a number of ways — setting up a [phishing website](https://www.cloudflare.com/learning/access-management/phishing-attack/) to trick the user, for instance.)

## How does encrypted SNI work?

ESNI keeps SNI secret by encrypting the SNI part of the client hello message (and only this part). Encryption only works if both sides of a communication — in this case, the client and the server — have the key for encrypting and decrypting the information, just as two people can use the same locker only if both have a key to the locker. Because the client hello message is sent before the client and server have negotiated TLS encryption keys, the ESNI encryption key has to be communicated some other way.

The solution: [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/). The web server adds a public key to its [DNS record](https://www.cloudflare.com/learning/dns/dns-records/), so that when the client looks up where to find the right server, it finds the server's public key as well. This is somewhat like leaving a house key in a lockbox outside one's home so that a visitor can safely enter the home. The client can then use the public key to encrypt its SNI record in such a way that only that specific server can decrypt it. (This is a somewhat simplified explanation; for a lengthier technical explanation, see [this blog post](https://blog.cloudflare.com/encrypted-sni/).)

Imagine that Alice wants to visit Bob's website, [www.bobisawesome.example.com](http://www.bobisawesome.example.com). Like every responsible website owner should, Bob uses TLS for his website so that all traffic to and from his website is encrypted. Bob has also implemented ESNI to further protect site visitors like Alice.

When Alice types <https://www.bobisawesome.example.com> into her laptop's browser, her laptop goes through the following process for loading the website:

  * Her laptop sends a query to a DNS server to find out the website's IP address.

  * The DNS response tells Alice's laptop which IP address to use in order to find Bob's website, and the DNS response also includes Bob's ESNI public key.

  * Alice's laptop sends a client hello message to the indicated IP address, encrypting the SNI part of the message by using Bob's public key.

  * Bob's web server shows Bob's TLS certificate.

  * The TLS handshake proceeds, and Alice's laptop loads [www.bobisawesome.example.com](http://www.bobisawesome.example.com). Any attackers who may be monitoring the network cannot see which website Alice is visiting.*




*_This last statement is only true if the DNS part of the process used DNSSEC and either DNS over HTTPS or DNS over TLS — more below._

## Does ESNI alone keep web browsing private?

ESNI is a major step towards privacy and security on the web, but other new protocols and features are important as well. The Internet was not designed with security and privacy in mind, and as a result there are a number of steps in the process of visiting a website that are not private. However, various new protocols are helping to encrypt and secure each step from malicious attackers.

The Domain Name System, or [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/), matches human-readable website addresses like [www.bobisawesome.example.com](http://www.bobisawesome.example.com) to alphanumerical IP addresses. It is like looking up someone's address in a large address book that everyone uses. However, normal DNS is not encrypted, meaning anyone could see which address someone is looking up, and anyone could pretend to be the address book. Even with ESNI in place, an attacker could see what DNS records users are querying and figure out which websites they are visiting.

Three additional protocols aim to close these gaps: [DNS over TLS](https://www.cloudflare.com/learning/dns/dns-over-tls/), DNS over HTTPS, and [DNSSEC](https://www.cloudflare.com/learning/dns/dns-security/).

DNS over TLS and DNS over HTTPS both do the same thing: encrypt DNS queries with TLS encryption. The main differences between them are what layer of the network they use and which network port they use. DNSSEC verifies that DNS records are real and come from a legitimate DNS server, not from an attacker impersonating a DNS server (as in a [DNS cache poisoning attack](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)).

## What is Encrypted Client Hello (ECH)?

Encrypted Client Hello (ECH) is another extension to the TLS protocol that protects the SNI part of the Client Hello through encryption. However, unlike ESNI, ECH encrypts the entire Client Hello. Learn more about ECH in [this blog post](https://blog.cloudflare.com/encrypted-client-hello/).

## Does Cloudflare support ESNI?

The Cloudflare network has supported ESNI [since September 2018](https://blog.cloudflare.com/esni/). Not only was Cloudflare the first major network to support ESNI, but Cloudflare was also instrumental in developing ESNI. ESNI has not yet been published as an official RFC, or Internet standard, but a [draft RFC](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/?include_text=1) is in the works.

Check your browser for security, privacy, and ESNI usage with this [free ESNI checker tool](https://www.cloudflare.com/ssl/encrypted-sni/). Learn more about [why SNI was created](https://www.cloudflare.com/learning/ssl/what-is-sni/), or [how a TLS handshake works](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/).
