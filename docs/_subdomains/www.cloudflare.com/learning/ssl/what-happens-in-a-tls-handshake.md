---
url: https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/
title: What Happens in a TLS Handshake? | SSL Handshake
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:44.092024+00:00
---

# What Happens in a TLS Handshake? | SSL Handshake

> Source: https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What happens in a TLS handshake? | SSL handshake 

In a TLS/SSL handshake, clients and servers exchange SSL certificates, cipher suite requirements, and randomly generated data for creating session keys. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what a TLS handshake is 
  * Understand what a TLS handshake accomplishes 
  * Explain the steps in a TLS handshake 
  * Explore different types of TLS handshakes 



Related content  [ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is mixed content? ](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[ What is HTTPS? ](https://www.cloudflare.com/learning/ssl/what-is-https/)

On this page

  * What is a TLS handshake?

  * TLS vs. SSL handshakes

  * When does a TLS handshake occur?

  * What happens during a TLS handshake?

    * What are the steps of a TLS handshake?

  * What is different about a handshake in TLS 1.3?

    * 0-RTT mode for session resumption

  * What is a cipher suite?




## What is a TLS handshake?

![the TLS Handshake](https://images.ctfassets.net/slt3lc6tev37/5aYOr5erfyNBq20X5djTco/3c859532c91f25d961b2884bf521c1eb/tls-ssl-handshake.png)the TLS Handshake

[TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) is an encryption and authentication protocol designed to secure Internet communications. A TLS handshake is the process that kicks off a communication session that uses TLS. During a TLS handshake, the two communicating sides exchange messages to acknowledge each other, verify each other, establish the cryptographic algorithms they will use, and agree on session keys. TLS handshakes are a foundational part of [how HTTPS works](https://www.cloudflare.com/learning/ssl/what-is-https/).

## TLS vs. SSL handshakes

[SSL, or Secure Sockets Layer](https://www.cloudflare.com/learning/ssl/what-is-ssl/), was the original security protocol developed for [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/). SSL was replaced by TLS, or Transport Layer Security, some time ago. SSL handshakes are now called TLS handshakes, although the "SSL" name is still in wide use.

Whitepaper

Maximize the power of TLS

[Get the report →](https://www.cloudflare.com/lp/maximize-tls/)Guide

The Zero Trust guide to securing aplication access

[Read the guide →](https://www.cloudflare.com/lp/guide-to-zero-trust-access/)

## When does a TLS handshake occur?

A TLS handshake takes place whenever a user navigates to a website over HTTPS and the browser first begins to query the website's [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). A TLS handshake also happens whenever any other communications use HTTPS, including [API calls](https://www.cloudflare.com/learning/security/api/what-is-api-call/) and [DNS over HTTPS](https://www.cloudflare.com/learning/dns/dns-over-tls/) queries.

TLS handshakes occur after a [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) connection has been opened via a TCP handshake.

Secure SSL

Free SSL included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What happens during a TLS handshake?

During the course of a TLS handshake, the client and server together will do the following:

  * Specify which version of TLS (TLS 1.0, 1.2, 1.3, etc.) they will use

  * Decide on which cipher suites (see below) they will use

  * Authenticate the identity of the server via the server’s public key and the SSL certificate authority’s digital signature

  * Generate session keys in order to use symmetric encryption after the handshake is complete




#### What are the steps of a TLS handshake?

TLS handshakes are a series of datagrams, or messages, exchanged by a client and a server. A TLS handshake involves multiple steps, as the client and server exchange the information necessary for completing the handshake and making further conversation possible.

The exact steps within a TLS handshake will vary depending upon the kind of key exchange algorithm used and the cipher suites supported by both sides. The RSA key exchange algorithm, while now considered not secure, was used in versions of TLS before 1.3. It goes roughly as follows:

  * **The 'client hello' message:** The client initiates the handshake by sending a "hello" message to the server. The message will include which TLS version the client supports, the cipher suites supported, and a string of random bytes known as the "client random."

  * **The 'server hello' message:** In reply to the client hello message, the server sends a message containing the server's [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/), the server's chosen cipher suite, and the "server random," another random string of bytes that's generated by the server.

  * **Authentication:** The client verifies the server's SSL certificate with the certificate authority that issued it. This confirms that the server is who it says it is, and that the client is interacting with the actual owner of the domain.

  * **The premaster secret:** The client sends one more random string of bytes, the "premaster secret." The premaster secret is encrypted with the public key and can only be decrypted with the private key by the server. (The client gets the [public key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) from the server's SSL certificate.)

  * **Private key used:** The server decrypts the premaster secret.

  * **Session keys created:** Both client and server generate session keys from the client random, the server random, and the premaster secret. They should arrive at the same results.

  * **Client is ready:** The client sends a "finished" message that is encrypted with a session key.

  * **Server is ready:** The server sends a "finished" message encrypted with a session key.

  * **Secure symmetric encryption achieved:** The handshake is completed, and communication continues using the session keys.




All TLS handshakes make use of asymmetric cryptography (the public and private key), but not all will use the private key in the process of generating session keys. For instance, an ephemeral Diffie-Hellman handshake proceeds as follows:

  * **Client hello:** The client sends a client hello message with the protocol version, the client random, and a list of cipher suites.

  * **Server hello:** The server replies with its SSL certificate, its selected cipher suite, and the server random. In contrast to the RSA handshake described above, in this message the server also includes the following (step 3):

  * **Server's digital signature:** The server computes a digital signature of all the messages up to this point.

  * **Digital signature confirmed:** The client verifies the server's digital signature, confirming that the server is who it says it is.

  * **Client DH parameter:** The client sends its DH parameter to the server.

    * **Client and server calculate the premaster secret:** Instead of the client generating the premaster secret and sending it to the server, as in an RSA handshake, the client and server use the DH parameters they exchanged to calculate a matching premaster secret separately.

    * **Session keys created:** Now, the client and server calculate session keys from the premaster secret, client random, and server random, just like in an RSA handshake.

    * **Client is ready:** Same as an RSA handshake.

    * **Server is ready**

    * **Secure symmetric encryption achieved**




*DH parameter: DH stands for Diffie-Hellman. The Diffie-Hellman algorithm uses exponential calculations to arrive at the same premaster secret. The server and client each provide a parameter for the calculation, and when combined they result in a different calculation on each side, with results that are equal.

To read more about the contrast between ephemeral Diffie-Hellman handshakes and other kinds of handshakes, and how they achieve forward secrecy, see [What is Keyless SSL?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)

## What is different about a handshake in TLS 1.3?

TLS 1.3 does not support RSA, nor other cipher suites and parameters that are vulnerable to attack. It also shortens the TLS handshake, making a TLS 1.3 handshake both faster and more secure.

The basic steps of a TLS 1.3 handshake are:

  * **Client hello:** The client sends a client hello message with the protocol version, the client random, and a list of cipher suites. Because support for insecure cipher suites has been removed from TLS 1.3, the number of possible cipher suites is vastly reduced. The client hello also includes the parameters that will be used for calculating the premaster secret. Essentially, the client is assuming that it knows the server’s preferred key exchange method (which, due to the simplified list of cipher suites, it probably does). This cuts down the overall length of the handshake — one of the important differences between TLS 1.3 handshakes and TLS 1.0, 1.1, and 1.2 handshakes.

  * **Server generates master secret:** At this point, the server has received the client random and the client's parameters and cipher suites. It already has the server random, since it can generate that on its own. Therefore, the server can create the master secret.

  * **Server hello and "Finished":** The server hello includes the server’s certificate, digital signature, server random, and chosen cipher suite. Because it already has the master secret, it also sends a "Finished" message.

  * **Final steps and client "Finished":** Client verifies signature and certificate, generates master secret, and sends "Finished" message.

  * **Secure symmetric encryption achieved**




#### 0-RTT mode for session resumption

TLS 1.3 also supports an even faster version of the TLS handshake that does not require any [round trips](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/), or back-and-forth communication between client and server, at all. If the client and the server have connected to each other before (as in, if the user has visited the website before), they can each derive another shared secret from the first session, called the "resumption main secret." The server also sends the client something called a session ticket during this first session. The client can use this shared secret to send encrypted data to the server on its first message of the next session, along with that session ticket. And TLS resumes between client and server.

## What is a cipher suite?

A cipher suite is a set of algorithms for use in establishing a secure communications connection. There are a number of cipher suites in wide use, and an essential part of the TLS handshake is agreeing upon which cipher suite will be used for that handshake.

To learn more about TLS/SSL, see [How does SSL work?](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/).
