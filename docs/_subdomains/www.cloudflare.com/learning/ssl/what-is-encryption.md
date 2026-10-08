---
url: https://www.cloudflare.com/learning/ssl/what-is-encryption/
title: What is Encryption? | Types of Encryption
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:01.466945+00:00
---

# What is Encryption? | Types of Encryption

> Source: https://www.cloudflare.com/learning/ssl/what-is-encryption/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is encryption? 

Encryption is a way to conceal information by altering it so that it appears to be random data. Encryption is essential for security on the Internet. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what encryption means 
  * Learn about the different types of data encryption 
  * Learn why encryption is so important in modern computing 
  * Explain how encryption keeps Internet communications secure 



Related content  [ What is asymmetric encryption? ](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[ How does public key cryptography work? ](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)

On this page

  * What is encryption?

  * How does encryption work?

  * What is a key in cryptography?

  * What are the different types of encryption?

  * Why is encryption important?

  * What is an encryption algorithm?

  * What are some common encryption algorithms?

  * What is a brute force attack in encryption?

  * How is encryption used to keep Internet browsing secure?




## What is encryption?

Encryption is a way of scrambling data so that only authorized parties can understand the information. In technical terms, it is the process of converting human-readable plaintext to incomprehensible text, also known as ciphertext. In simpler terms, encryption takes readable data and alters it so that it appears random. Encryption requires the use of a [cryptographic key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/): a set of mathematical values that both the sender and the recipient of an encrypted message agree on.

## How does encryption work?

Encryption is a mathematical process that alters data using an encryption algorithm and a key. Imagine if Alice sends the message "Hello" to Bob, but she replaces each letter in her message with the letter that comes two places later in the alphabet. Instead of "Hello," her message now reads "Jgnnq." Fortunately, Bob knows that the key is "2" and can decrypt her message back to "Hello."

Alice used an extremely simple encryption algorithm to encode her message to Bob. More complicated encryption algorithms can further scramble the message:

![encryption example](https://images.ctfassets.net/slt3lc6tev37/4zLJngHjth92rb9VUrclZr/ec5b406b06e1fbee7dc0d5950789ce76/encryption-example.svg)encryption example

Although encrypted data appears random, encryption proceeds in a logical, predictable way, allowing a party that receives the encrypted data and possesses the right key to decrypt the data, turning it back into plaintext. Truly secure encryption will use keys complex enough that a third party is highly unlikely to decrypt or break the ciphertext by [brute force](https://www.cloudflare.com/learning/bots/brute-force-attack/) — in other words, by guessing the key. (Alice's first encryption method would be broken very quickly.)

Data can be encrypted "at rest," when it is stored, or "in transit," while it is being transmitted somewhere else.

## What is a key in cryptography?

A cryptographic key is a string of characters used within an encryption algorithm for altering data so that it appears random. Like a physical key, it locks (encrypts) data so that only someone with the right key can unlock (decrypt) it.

## What are the different types of encryption?

The two main kinds of encryption are symmetric encryption and [asymmetric encryption](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/). Asymmetric encryption is also known as [public key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) encryption.

In symmetric encryption, there is only one key, and all communicating parties use the same (secret) key for both encryption and decryption. In asymmetric, or public key, encryption, there are two keys: one key is used for encryption, and a different key is used for decryption. The decryption key is kept private (hence the "private key" name), while the encryption key is shared publicly, for anyone to use (hence the "public key" name). Asymmetric encryption is a foundational technology for [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (often called [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)).

## Why is encryption important?

**Privacy:** Encryption ensures that no one can read communications or data at rest except the intended recipient or the rightful data owner. This prevents attackers, ad networks, Internet service providers, and in some cases governments from intercepting and reading sensitive data, protecting user [privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/).

**Security:** Encryption helps prevent [data breaches](https://www.cloudflare.com/learning/security/what-is-a-data-breach/), whether the data is in transit or at rest. If a corporate device is lost or stolen and its hard drive is properly encrypted, the data on that device will still be secure. Similarly, encrypted communications enable the communicating parties to exchange sensitive data without leaking the data.

**Data integrity:** Encryption also helps prevent malicious behavior such as [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/). When data is transmitted across the Internet, encryption ensures that what the recipient receives has not been viewed or tampered with on the way.

**Regulations:** For all these reasons, many industry and government regulations require companies that handle user data to keep that data encrypted. Examples of regulatory and compliance standards that require encryption include HIPAA, PCI-DSS, and the [GDPR](https://www.cloudflare.com/learning/privacy/what-is-the-gdpr/).

## What is an encryption algorithm?

An encryption algorithm is the method used to transform data into ciphertext. An algorithm will use the encryption key in order to alter the data in a predictable way, so that even though the encrypted data will appear random, it can be turned back into plaintext by using the decryption key.

## What are some common encryption algorithms?

Commonly used symmetric encryption algorithms include:

  * AES

  * 3-DES

  * SNOW




Commonly used asymmetric encryption algorithms include:

  * RSA

  * Elliptic curve cryptography




## What is a brute force attack in encryption?

A [brute force attack](https://www.cloudflare.com/learning/bots/brute-force-attack/) is when an attacker who does not know the decryption key attempts to determine the key by making millions or billions of guesses. Brute force attacks are much faster with modern computers, which is why encryption has to be extremely strong and complex. Most modern encryption methods, coupled with high-quality passwords, are resistant to brute force attacks, although they may become vulnerable to such attacks in the future as [computers become more and more powerful](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/). Weak passwords are still susceptible to brute force attacks.

## How is encryption used to keep Internet browsing secure?

Encryption is foundational for a variety of technologies, but it is especially important for keeping [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) requests and responses secure. The protocol responsible for this is called [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) (Hypertext Transfer Protocol Secure). A website served over HTTPS instead of HTTP will have a URL that begins with https:// instead of http://, usually represented by a secured lock in the address bar.

HTTPS uses the encryption protocol called Transport Layer Security (TLS). In the past, an earlier encryption protocol called Secure Sockets Layer (SSL) was the standard, but TLS has replaced SSL. A website that implements HTTPS will have a [TLS certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) installed on its origin server. [Learn more about TLS and HTTPS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/).

To help keep the Internet more secure, Cloudflare offers free TLS/SSL encryption for any websites using Cloudflare services. Learn more about [free TLS/SSL encryption from Cloudflare](https://www.cloudflare.com/application-services/products/ssl/).
