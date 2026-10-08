---
url: https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/
title: What Is a Cryptographic Key? | Keys and SSL Encryption
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:45.547884+00:00
---

# What Is a Cryptographic Key? | Keys and SSL Encryption

> Source: https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is a cryptographic key? 

A key is a group of random characters in a particular order. Encryption protocols use a key to alter data so that it's scrambled, and so that anyone without the key can't decode the information. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what a "key" is in cryptography 
  * Understand how a key is used to scramble data in encryption 
  * Explain how exchanging public keys makes HTTPS possible 



Related content  [ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)

On this page

  * What is a cryptographic key?

  * Keys in early forms of encryption

  * Keys in modern encryption

  * How are keys used in SSL encryption?




![Cryptographic Key](https://images.ctfassets.net/slt3lc6tev37/5UFGteYwYTmakGi1m4hh10/68451375d91f71ce26ebbe4bb8051f04/cryptographic-key.png)Cryptographic Key

## What is a cryptographic key?

In cryptography, a key is a string of characters used within an [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) algorithm for altering data so that it appears random. Like a physical key, it locks (encrypts) data so that only someone with the right key can unlock (decrypt) it.

![Cryptographic Key Hello](https://images.ctfassets.net/slt3lc6tev37/4jlj78kiMZiyMBrEhb1nIW/ed73490bf4aa7daa8aea28878c8dd2b8/cryptographic-key-hello.png)Cryptographic Key Hello

The original data is known as the _plaintext_ , and the data after the key encrypts it is known as the _ciphertext_.

The formula:

plaintext

  * key



= ciphertext

## Keys in early forms of encryption

Before the advent of computers, ciphertext was often created by simply replacing one letter with another letter in the plaintext, a method known as a "substitution cipher." For instance, suppose that someone sends a message reading "Hello" to another person, and each letter is replaced with the one after it in the alphabet: "Hello" becomes "Ifmmp."

H E L L O

+1 +1 +1 +1 +1

I F M M P

"Ifmmp" looks like a nonsensical string of letters, but if someone knows the key, they can substitute the proper letters and decrypt the message as "Hello." For this example, the key is (_letter_) - 1, moving each letter down one spot in the alphabet to arrive at the real letter.

I F M M P

-1 -1 -1 -1 -1

H E L L O

Such ciphers are relatively easy to break with simple statistical analysis, since certain letters will appear more often than others in any given text (for instance E is the most common letter in the English language). To combat this, cryptographers developed a system called the one-time pad.

A one-time pad is a single-use-only key that has at least as many values as the plaintext has characters. In other words, each letter will be replaced by a letter that's a unique number of letters removed from it in the alphabet.

For example, suppose someone has to encrypt the message "Hello," and they use a one-time pad with the values 7, 17, 24, 9, 11.

H E L L O

7 17 24 9 11

Whereas before we simply moved up one position for each letter (letter + 1), now we move a different number of places in the alphabet for each letter. We add 7 to the first letter, H; we add 17 to the second letter; and so on. For any calculations that take us past Z, we simply go back to the beginning of the alphabet and keep adding.

H E L L O

7 17 24 9 11

O V J U Z

Starting from the plaintext "Hello," we now have the ciphertext "Ovjuz," using the key "7, 17, 24, 9, 11."

For communication via a one-time pad to work, both sides of the conversation have to use the same key for each individual message ([symmetric encryption](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)), although a different key is used every time there's a new message. Although to any third parties "Ovjuz" looks like random nonsense, the person who receives the ciphertext "Ovjuz" will know to use the key "7, 17, 24, 9, 11" to decrypt it (subtracting instead of adding):

O V J U Z

7 17 24 9 11

H E L L O

Thus, a simple message can be altered by a string of random data, a key, in order to be encrypted or decrypted.

## Keys in modern encryption

Although the above examples of early cryptography illustrate how using a random string of information to turn plaintext into ciphertext works, cryptographic keys today are far more complex.

For instance, a website's [public key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) might be something like:

04 CE D7 61 49 49 FD 4B 35 8B 1B 86 BC A3 C5 BC D8 20 6E 31 17 2D 92 8A B7 34 F4 DB 11 70 4E 49 16 61 FC AE FA 7F BA 6F 0C 05 53 74 C6 79 7F 81 12 8A F7 E2 5E 6C F5 FA 10 69 6B 67 D9 D5 96 51 B0 (_Copied in 2019 from the cloudflare.com SSL certificate_)

This is much more complex than the "7 17 24 9 11" key we used above to encrypt "Hello."

Instead of simply adding or subtracting, modern encryption uses complex mathematical formulas known as _algorithms_. And instead of a simple string of random numbers for a key, modern keys are typically randomized even further.

This is the case for several reasons:

  * Computers are capable of far more complicated calculations in a shorter amount of time than human cryptographers, making more complex encryption not only possible, but necessary.

  * Computers can alter information at the binary level, the 1s and 0s that make up data, not just at the level of individual letters and numbers.

  * If encrypted data is not randomized enough, a computer program will be able to decrypt it. True randomness is extremely important for truly secure encryption.




Combined with an encryption algorithm, a cryptographic key will scramble a text beyond human recognition.

## How are keys used in SSL encryption (HTTPS)?

There are two kinds of encryption: symmetric encryption and [asymmetric encryption](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/), also known as [public key encryption](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/). In symmetric encryption, both sides of a conversation use the same key for turning plaintext into ciphertext and vice versa.

In asymmetric or public key encryption, the two sides of the conversation each use a different key. One key is called the public key, and one key is called the private key – thusly named because one of the parties keeps it secret and never shares it with anyone. When plaintext is encrypted with the public key, only the private key can decrypt it, not the public key.

[SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/) (or [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), as it is called today), is an encryption protocol used to keep Internet communications secure, and a website that is served over [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) instead of [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) uses this kind of encryption. In TLS/SSL, a website or web application will have both a public key and a private key. The public key is shared publicly in the website's [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) for anyone to see. The private key is installed on the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) and never shared.

TLS/SSL communication sessions begin with a [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/), during which the website and the client use the public key and the private key in order to generate new keys, which are called [session keys](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/). These session keys are then used by both sides to encrypt their messages back and forth.

Thus, TLS starts with asymmetric encryption (with two keys) and moves to symmetric encryption (with one key). Both sides use the same keys during the communication session, but when they start a new session, they will generate new keys together.
