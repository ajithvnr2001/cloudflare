---
url: https://www.cloudflare.com/learning/ssl/what-is-a-session-key/
title: What Is a Session Key? | Session Keys and TLS Handshakes
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:49.002511+00:00
---

# What Is a Session Key? | Session Keys and TLS Handshakes

> Source: https://www.cloudflare.com/learning/ssl/what-is-a-session-key/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is a session key? Session keys and TLS handshakes 

The TLS (historically known as "SSL") protocol uses both asymmetric/public key and symmetric cryptography, and new keys for symmetric encryption have to be generated for each communication session. Such keys are called "session keys." 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what a session is, what a key is, and when new session keys have to be created 
  * Understand the differences between asymmetric and symmetric cryptography 
  * Learn how the SSL/TLS encryption protocol uses both kinds of cryptography 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ Types of SSL certificates: SSL certificate types explained ](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)

On this page

  * What is a session key?

  * What is a session?

  * What is a cryptographic key?

  * Does HTTPS use symmetric or asymmetric cryptography?

  * What is the &#39




## What is a session key?

A session key is any [symmetric](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/) [cryptographic key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) used to encrypt one communication session only. In other words, it's a temporary key that is only used once, during one stretch of time, for [encrypting](https://www.cloudflare.com/learning/ssl/what-is-encryption/) and decrypting datasent between two parties; future conversations between the two would be encrypted with different session keys. A session key is like a password that someone resets every time they log in.

In [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (historically known as "[SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)"), the two communicating parties (the client and the server) generate session keys at the start of any communication session, during the [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/). The official [RFC for TLS](https://www.rfc-editor.org/rfc/rfc8446) does not actually call these keys "session keys", but functionally that's exactly what they are.

## What is a session?

A session is essentially a single conversation between two parties. A session takes place over a network, and it begins when two devices acknowledge each other and open a virtual connection. It ends when the two devices have obtained the information they need from each other and send "close_notify" messages, terminating the connection, much like if two people are texting each other, and they close the conversation by saying, "Talk to you later." The connection can also time out due to inactivity, like if two people are texting and simply stop responding to each other.

![Session keys - three sessions each with a new key](https://images.ctfassets.net/slt3lc6tev37/V9RAG8z5jvFu1c0FUyE5A/5a686114c92664bccef84c32a37a09f3/what_is_a_session_key.png)Session keys - three sessions each with a new key

A session can either be a set period of time, or it can last for as long as the two parties are communicating. If the former, the session will expire after a certain amount of time; in the context of [TLS encryption](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), the two devices would then have to exchange information and generate new session keys to reopen the connection.

## What is a cryptographic key?

In cryptography, it is common to talk about [keys](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) (usually a short piece of data) to refer to special inputs of a cryptographic algorithm. The most common keys are those used for data encryption; however, other types of keys exist for different purposes.

A data encryption algorithm uses a (secret) key to convert a message into a ciphertext — that is, a scrambled, unreadable version of the message. One can recover the original message from the ciphertext by using a decryption key.

In a symmetric encryption algorithm, both the encryption and decryption keys are the same. Thus, anyone holding the secret key can encrypt and decrypt data, and this is why the term symmetric keys is often used.

Contrarily, in an [asymmetric encryption](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/) algorithm, also known as [public-key encryption](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/), there exist two keys: one is public and can only be used for encrypting data, whereas the other one remains private and is used only for decrypting ciphertexts.

## Does HTTPS use symmetric or asymmetric cryptography?

[HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/), which is [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) in combination with the TLS protocol, uses both types of cryptography. All communications over TLS start with a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/). Asymmetric cryptography is crucial for making the TLS handshake work.

During the course of a TLS handshake, the two communicating devices will establish the session keys, and these will be used for symmetric encryption for the rest of the session (unless the devices choose to update their keys during the session). Usually, the two communicating devices are a client, or a user device like a laptop or a smartphone, and a server, which is any web server that hosts a website. (For more, see [What is the client-server model?](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/))

In the TLS handshake, the client and server also:

  * Negotiate which cryptographic algorithms to use (doing so securely via asymmetric cryptography)

  * Authenticate the server's identity against its TLS certificate (using asymmetric cryptography)




## What is the 'master secret' in a TLS handshake? How does it relate to session keys?

The master secret is the result from combining a string of random data sent by the client, random data sent by the server, and another string of data called the "premaster secret" via an algorithm. The client and the server each have those three messages, so they should arrive at the same result for the master secret.

The client and server then use the master secret to calculate several session keys for use in that session only. They should end up with the same session keys.

Learn more about how TLS works: [What happens in a TLS handshake?](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)
