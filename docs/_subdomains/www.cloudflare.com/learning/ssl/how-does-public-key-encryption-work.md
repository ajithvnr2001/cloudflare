---
url: https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/
title: How Does Public Key Encryption Work? | Public Key Cryptography and SSL
method: crawl4ai+scrapegraph (scrapling: scrapling status 403)
fetched_at: 2026-10-08T08:04:27.003919+00:00
---

# How Does Public Key Encryption Work? | Public Key Cryptography and SSL

> Source: https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  How does public key cryptography work? 

Public key cryptography, also known as asymmetric cryptography, uses two separate keys instead of one shared one: a public key and a private key. Public key cryptography is an important technology for Internet security. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define public key cryptography 
  * Understand how public key cryptography works 
  * Learn why public key cryptography is essential for the TLS/SSL protocol 



Related content  [ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What is mixed content? ](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)

On this page

  * What is public key cryptography?

  * What is a cryptographic key?

  * How does TLS/SSL use public key cryptography?




## What is public key cryptography?

Public key cryptography is a method of encrypting or signing data with two different keys and making one of the keys, the public key, available for anyone to use. The other key is known as the private key. Data encrypted with the public key can only be decrypted with the private key. Because of this use of two keys instead of one, public key cryptography is also known as [asymmetric cryptography](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/). It is widely used, especially for [TLS/SSL](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), which makes [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) possible.

Sign up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is a cryptographic key?

In cryptography, a [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) is a piece of information used for scrambling data so that it appears random; often it's a large number, or string of numbers and letters. When unencrypted data, also called plaintext, is put into a cryptographic algorithm using the key, the plaintext comes out the other side as random-looking data. However, anyone with the right key for decrypting the data can put it back into plaintext form.

For example, suppose we take a plaintext message, "hello," and encrypt it with a key; let's say the key is "2jd8932kd8." Encrypted with this key, our simple "hello" now reads "X5xJCSycg14=", which seems like random garbage data. However, by decrypting it with that same key, we get "hello" back.

Plaintext + key = ciphertext:
    
    
    hello + 2jd8932kd8 = X5xJCSycg14=
    

Ciphertext + key = plaintext:
    
    
    X5xJCSycg14= + 2jd8932kd8 = hello
    

This is an example of symmetric cryptography, in which only one key is used. In public key cryptography, there would instead be two keys. The public key would encrypt the data, and the private key would decrypt it.

Whitepaper

Maximize the power of TLS

[Read the whitepaper →](https://www.cloudflare.com/lp/maximize-tls/)

## How does TLS/SSL use public key cryptography?

Public key cryptography is extremely useful for establishing secure communications over the Internet (via HTTPS). A website's [SSL/TLS certificate](https://www.cloudflare.com/application-services/products/ssl/), which is shared publicly, contains the public key, and the private key is installed on the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) — it's "owned" by the website.

[TLS handshakes](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) use public key cryptography to authenticate the identity of the origin server, and to exchange data that is used for generating the session keys. A key exchange algorithm, such as RSA or Diffie-Hellman, uses the public-private key pair to agree upon session keys, which are used for symmetric encryption once the handshake is complete. Clients and servers are able to agree upon new session keys for each communication session, so that bad actors are unable to decrypt communications even if they identify or steal one of the session keys from a previous session.
