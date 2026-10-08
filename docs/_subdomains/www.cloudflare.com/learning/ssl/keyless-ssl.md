---
url: https://www.cloudflare.com/learning/ssl/keyless-ssl/
title: How Does Keyless SSL Work? | Forward Secrecy
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:29.511645+00:00
---

# How Does Keyless SSL Work? | Forward Secrecy

> Source: https://www.cloudflare.com/learning/ssl/keyless-ssl/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  How does keyless SSL work? 

Keyless SSL makes it possible for organizations that cannot share their private keys to move to the cloud while maintaining SSL/TLS encryption. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain the steps in a TLS handshake and the difference between a session key and a private key 
  * Understand how keyless SSL separates the part of the TLS handshake using the private key from the rest of the handshake 
  * Learn the difference between Diffie-Hellman and RSA handshakes 
  * Understand what forward secrecy is 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is mixed content? ](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[ What is TLS (Transport Layer Security)? ](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[ What is HTTPS? ](https://www.cloudflare.com/learning/ssl/what-is-https/)[ Why use HTTPS? ](https://www.cloudflare.com/learning/ssl/why-use-https/)

On this page

  * What is keyless SSL?

  * How does keyless SSL work?

  * How does keyless SSL work with an RSA key exchange TLS handshake?

  * How does keyless SSL work with the Ephemeral Diffie-Hellman Key Exchange?

  * What is a session key?

  * What is forward secrecy? What is perfect forward secrecy?

  * How does Cloudflare implement keyless SSL?




## What is keyless SSL?

![Keyless SSL](https://blog.cloudflare.com/content/images/2014/Sep/illustration-keyless-ssl.png)Keyless SSL

Keyless [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/) is a service for companies that use a cloud vendor for SSL encryption. Usually this would mean that the cloud vendor has to know the company's private key, but keyless SSL is a way to circumvent that. For regulatory reasons many organizations cannot share their private keys. With keyless SSL, these organizations are still able to use TLS and leverage the cloud while keeping the key secure.

SSL, more accurately known as [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), is a protocol for authenticating and encrypting communications over a network. SSL/TLS requires the use of what's called a public key and a private key, and in the case of a company using the protocol to secure traffic to and from their website (see [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/)), the private key typically remains in the company's possession. But when a company moves to the cloud and a vendor provides TLS encryption, the vendor has the private key instead.

By moving the part of the handshake involving the private key off of the vendor's server, the private key can remain securely in the company's possession. Instead of using the private key directly to authenticate the vendor's server, the cloud vendor forwards data to and receives data from the company's server to accomplish this. This communication occurs over a secure, encrypted channel. Thus, a private key is still used, but it is not shared with anyone outside the company.

For instance, suppose that Acme Co. implements TLS. Acme Co. will securely store their private key on a server that they own and control. If Acme Co. moves to the cloud and uses a cloud service provider for web hosting, that vendor will then have the private key. However, if Acme Co. moves to the cloud with a vendor that implements keyless SSL/TLS instead, the private key can stay on the server that Acme Co. owns and controls, as in the non-cloud TLS implementation.

## How does keyless SSL work?

Keyless SSL is based on the fact that there is only one time when the private key is used during the TLS handshake, which occurs at the beginning of a TLS communication session. Keyless SSL works by splitting the steps of the [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) up geographically. A cloud vendor offering keyless SSL moves the private key part of the process to another server, usually a server that the customer keeps on premises.

When the private key becomes necessary during the handshake for decrypting or signing data, the vendor's server forwards the necessary data to the customer's private key server. The private key decrypts or signs the data on the customer's server, the customer's server sends the data back to the vendor's server, and the TLS handshake continues like usual.

Keyless SSL is only "keyless" from the cloud vendor's point of view: they never see their customer's private key, but the customer still has and uses it. Meanwhile, the public key is still used on the client side like normal.

## How does keyless SSL work with an RSA key exchange TLS handshake?

In an RSA handshake, the steps in a TLS handshake are as follows:

  * The client sends the server a plaintext "hello" message that includes the protocol version they want to use, a list of supported cipher suites, and a short string of random data called the "client random."

  * The server responds (in plaintext) with its SSL certificate, its preferred cipher suite, and a different short string of random data, called the "server random."

  * The client creates another random set of data, called the "premaster secret." Taking the public key from the server's SSL certificate, the client encrypts the premaster secret and sends it to the server; only someone with the private key can decrypt the premaster secret.

  * The server decrypts the premaster secret. **Note that this is the only time the private key is used!**

  * Now both client and server have the client random, the server random, and the premaster secret. Independently of each other, they combine these three inputs to come up with [session keys](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/). They should both arrive at the same result, and all subsequent communications during the session are encrypted with these new session keys.


![SSL Handshake \(RSA\) Without Keyless SSL](https://images.ctfassets.net/slt3lc6tev37/HMtyedlloYodaGnzxFcON/176dea4dbf1c8b4f3d58e6afd43ee9ea/ssl-handshake-rsa.jpg)SSL Handshake (RSA) Without Keyless SSL

Keyless SSL comes into play in step 4. With keyless SSL, instead of decrypting the premaster secret themselves, the cloud vendor sends it in encrypted form over a secure channel to a server that the customer hosts or controls. The customer's private key decrypts the premaster secret, and then the decrypted premaster secret is sent back to the cloud vendor. The cloud vendor's server uses this to derive the session keys, and TLS communications continue as normal.

![Cloudflare Keyless SSL Handshake \(RSA\)](https://images.ctfassets.net/slt3lc6tev37/5eQlkE5a3vIM6deiHTY7dA/1c34bfefb3d8abe5d5ad3ec91e69e355/cloudflare-keyless-ssl-handshake-rsa.jpg)Cloudflare Keyless SSL Handshake (RSA)

## How does keyless SSL work with the Ephemeral Diffie-Hellman Key Exchange?

An ephemeral Diffie-Hellman (DHE) handshake ("ephemeral" because the same key is never used twice) generates session keys using the Diffie-Hellman algorithm, a way of exchanging keys over an unsecure channel. With this kind of TLS handshake, private key authentication is a separate process from session key generation.

The main difference between the DHE handshake and an RSA handshake, aside from the algorithms used, is how the premaster secret is generated. In an RSA handshake, the premaster secret is made up of randomized data generated by the client; in a DHE handshake, the client and the server use agreed-upon parameters to calculate the same premaster secret separately.

  * Just like in an RSA handshake, the client sends the protocol version they want to use, a list of supported cipher suites, and the client random.

  * The server responds with its chosen cipher suite, a server random, and its SSL certificate. Here the DHE handshake starts to differ from an RSA handshake: The server also sends its Diffie-Hellman (DH) parameter, which will be used for calculating the premaster secret. It also includes a digital signature for authentication. This is the only time the private key is used, and it authenticates that the server is who it says it is.

  * The client verifies the server's digital signature and authenticates the SSL certificate. The client then replies with its DH parameter.

  * Using the client's DH parameter and the server's DH parameter, both parties calculate the premaster secret separately from each other.

  * They then combine this premaster secret with the client random and server random to get the session keys.


![SSL Handshake \(Diffie-Hellman\) Without Keyless SSL](https://images.ctfassets.net/slt3lc6tev37/1mzPVvjnKpVD0LUSsUlq2r/23c6dee053aaab22b122b53783dc098f/ssl-handshake-diffie-hellman.jpg)SSL Handshake (Diffie-Hellman) Without Keyless SSL

The private key is only used in step 2, and this is where keyless SSL becomes relevant. At this point, the SSL/TLS vendor sends the client random, server random, and server's DH parameter to the customer-controlled server that has the private key. This information is used to generate the server's digital signature and is sent back to the cloud vendor, who passes it on to the client. The client is able to verify this signature with the public key, and the handshake proceeds. This way, the cloud vendor does not need to touch the private key.

![Cloudflare Keyless SSL \(Diffie Hellman\)](https://images.ctfassets.net/slt3lc6tev37/2lGPm4AKMjmMOBzPoTZEQM/1b6699cd71193897ce80353938366057/cloudflare-keyless-ssl-diffie-hellman.jpg)Cloudflare Keyless SSL (Diffie Hellman)

Ephemeral Diffie-Hellman handshakes, although they take slightly longer than RSA handshakes, have the advantage of something called forward secrecy. Because the private key is only used for authentication, an attacker cannot use it to discover any given session key.

## What is a session key?

A session key is a symmetric key used by both sides of a secure communication over TLS, after the TLS handshake is completed. Once the two sides agree upon a set of session keys, there is no need to use the public and private keys anymore. TLS generates different session keys for each unique session.

## What is forward secrecy? What is perfect forward secrecy?

Forward secrecy ensures that encrypted data stays encrypted even if the private key is exposed. This is also known as "perfect forward secrecy." Forward secrecy is possible if a unique session key is used for each communication session, and if the session key is generated separately from the private key. If a single session key is compromised, only that session can be decrypted by an attacker; all other sessions will remain encrypted.

In a protocol set up for forward secrecy, the private key is used for authentication during an initial handshake process, and otherwise it is not used. The ephemeral Diffie-Hellman handshake generates session keys separately from the private key and therefore has forward secrecy.

In contrast, RSA does not have forward secrecy; with the private key compromised, an attacker could determine session keys for past conversations, because they can decrypt the premaster secret and the client randoms and server randoms are in plaintext. By combining these three, the attacker can derive any given session key.

## How does Cloudflare implement keyless SSL?

Cloudflare was the first cloud vendor to release [keyless SSL](https://www.cloudflare.com/ssl/keyless-ssl/), allowing enterprises facing tight security restrictions, such as banks, to move to the cloud. Cloudflare supports both RSA and Diffie-Hellman handshakes, so that companies can incorporate forward secrecy and protect against the possibility of an attacker decrypting their data after stealing their private key.

All communications between Cloudflare servers and the private key servers take place over a secure, encrypted channel. Additionally, Cloudflare has found that keyless SSL has a negligible impact on [performance](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) despite the extra trips to the private key server.

For more technical details on [how keyless SSL works, take a look at this blog post](https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details/). For more on keyless SSL from Cloudflare, explore the details of our [keyless SSL service](https://www.cloudflare.com/ssl/keyless-ssl/).
