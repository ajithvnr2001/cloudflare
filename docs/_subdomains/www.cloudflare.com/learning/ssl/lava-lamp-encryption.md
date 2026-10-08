---
url: https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/
title: How Do Lava Lamps Help with Internet Encryption?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:29.578067+00:00
---

# How Do Lava Lamps Help with Internet Encryption?

> Source: https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  How do lava lamps help with Internet encryption? 

Cloudflare translates photos of 100 lava lamps into random data for use in SSL encryption. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn why randomness is necessary for encryption keys 
  * Explain why computers can't create randomness on their own 
  * Understand how a computer uses random inputs to generate random outputs 
  * Learn what a cryptographic seed is 
  * Understand how lava lamps create the random data necessary for a cryptographic seed 



Related content  [ What is encryption? ](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[ How does public key cryptography work? ](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[ What is asymmetric encryption? ](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)

On this page

  * Why does Cloudflare use lava lamps to help with encryption?

  * What does &#39

  * Why can&#39

  * How can a computer use random, real-world inputs to generate random data?

  * What is a cryptographically secure pseudorandom number generator?

  * What is a cryptographic seed?

  * Are the lava lamps the only source for the cryptographic seed?

  * What is entropy?

  * What if someone stands in front of the lava lamps?

  * What if someone shuts off or damages the camera?

  * Do all Cloudflare offices have the lava lamp wall?

  * Was Cloudflare the first company to use lava lamps for encryption?




## Why does Cloudflare use lava lamps to help with encryption?

Randomness is extremely important for secure [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/). Each new key that a computer uses to encrypt data must be truly random, so that an attacker won't be able to figure out the key and decrypt the data. However, computers are designed to provide predictable, logical outputs based on a given input. They aren't designed to produce the random data needed for creating unpredictable [encryption keys](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/).

To produce the unpredictable, chaotic data necessary for strong encryption, a computer must have a source of random data. The "real world" turns out to be a great source for randomness, because events in the physical world are unpredictable.

As one might expect, lava lamps are consistently random. The "lava" in a lava lamp never takes the same shape twice, and as a result, observing a group of lava lamps is a great source for random data.

![Cloudflare Lava Lamp Wall](https://blog.cloudflare.com/content/images/2017/11/lava-lamps.jpg)Cloudflare Lava Lamp Wall

To collect this data, Cloudflare has arranged about 100 lava lamps on one of the walls in the lobby of the Cloudflare headquarters and mounted a camera pointing at the lamps. The camera takes photos of the lamps at regular intervals and sends the images to Cloudflare servers. All digital images are really stored by computers as a series of numbers, with each pixel having its own numerical value, and so each image becomes a string of totally random numbers that the Cloudflare servers can then use as a starting point for creating secure encryption keys.

Thus, with the help of lava lamps, Cloudflare is able to offer extremely strong (and sufficiently random) [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)/[TLS encryption](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) to its customers. This is especially important considering that millions of Internet properties use Cloudflare.

eBook

5 Ways to Maximize Security & Performance

[Get the eBook →](https://www.cloudflare.com/lp/five-ways-maximize-performance/)ebook

Everywhere security for every phase of the attack lifecycle

[Read the ebook →](https://www.cloudflare.com/lp/everywhere-security-ebook/)

## What does 'random' mean in the context of cryptography?

In cryptography, random does not just mean statistically random; it also means unpredictable.

Encrypted data should look like totally random data, since predictable data can be guessed. If there is any pattern – if certain values are used for encryption more than others, or if values appear in a certain order consistently – then mathematical analysis will pick up on the pattern and allow an attacker to have a much easier time guessing the key used for encryption. Essentially, if encrypted data is predictable, it might as well already be compromised.

The process of [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) itself is a predictable one: Encrypted data plus the right key equals decrypted data, and the decrypted data is the same as it was before it was encrypted. But the encryption keys used have to be unpredictable.

To understand why unpredictability is so important, imagine two poker players: Bob always bets when he has good cards and folds (declines to match other players' bets) when he has bad cards. Alice, meanwhile, mixes up her betting strategy so that there's no discernable pattern to it: sometimes she bets when she has good cards, sometimes she contents herself with matching other players' bets, and sometimes she even bluffs by betting big when she has bad cards. When Alice and Bob enter the same poker tournament, Alice lasts much longer than Bob does, because Bob is too predictable. Opponents quickly figure out when Bob has good cards and react accordingly. Even though they can't see his cards, they can discern roughly what cards he's holding.

Similarly, even though attackers can't see the "cards" – or, the encrypted content – that's sent over a network, they can guess it if the method for concealing the content is too predictable.

## Why can't computers create randomness?

Computers run on logic. A computer program is based on if-then statements: If certain conditions are met, then perform this specified action. The same input into a program results in the same output every time.

This is by design. An input should lead to an expected output, not an unexpected one. Imagine the chaos if a printer printed random text that was different from the text in the document that was sent to the printer, or if smartphones were to call a different phone number than the one the user entered. Computers are only useful because of their (relative) reliability and predictability. However, that predictability is a liability when it comes to generating secure encryption keys.

Some computer programs are good at simulating randomness, but not good enough at it for creating encryption keys.

Sign Up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## How can a computer use random, real-world inputs to generate random data?

A software program called a pseudorandom number generator (PRNG) is able to take an unpredictable input and use it to generate unpredictable outputs. Theoretically, a PRNG can produce unlimited random outputs from a random input.

Such an algorithm is called "pseudorandom" and not "random" because its outputs are not actually completely random. Why is this the case? There are 2 main reasons:

  * When given the same seed to start with twice in a row, a PRNG will produce the exact same results.

  * It's difficult to prove if the results it generates will be completely random the entire time (if the PRNG runs indefinitely).




Because of reason No. 2, the algorithm continually needs new inputs of randomness. A random input is known as a "cryptographic seed."

## What is a cryptographically secure pseudorandom number generator?

A cryptographically secure pseudorandom number generator, or CSPRNG, is a PRNG that meets more stringent standards, making it safer to use for cryptography. A CSPRNG meets two requirements that PRNGs may not necessarily meet:

  * It has to pass certain statistical randomness tests to prove unpredictability.

  * An attacker must not be able to predict the outputs of the CSPRNG even if they have partial access to the program.




Like a PRNG, a CSPRNG needs random data (the cryptographic seed) as a starting point from which to produce more random data.

To generate encryption keys for SSL/TLS encryption, Cloudflare uses a CSPRNG, with data collected from the lava lamps as part of the cryptographic seed.

## What is a cryptographic seed?

A cryptographic seed is the data that a CSPRNG starts with for generating random data. Although a CSPRNG could theoretically produce unlimited random outputs from a single cryptographic seed, it is far more secure to regularly refresh the cryptographic seed. An attacker may eventually compromise the initial cryptographic seed – and remember, a CSPRNG will produce the exact same outputs again if it is fed the same seed, so the attacker could then duplicate the random outputs. Additionally, even the most rigorously tested CSPRNG is not guaranteed to produce unpredictable results indefinitely.

With the lava lamps, Cloudflare has a continual source for new cryptographic seed data. Each image the camera takes of the lamps is different, resulting in a different random sequence of numerical values that can be used as a seed.

## Are the lava lamps the only source for the cryptographic seed?

Many operating systems have their own sources of random data for use in cryptographic seeds, for instance from user actions (mouse movements, typing on a keyboard, etc.), although they obtain this data relatively slowly. Cloudflare mixes the random data obtained from the lava lamps with data generated by the Linux operating system on two different machines in order to maximize entropy when creating cryptographic seeds for SSL/TLS encryption.

## What is entropy?

In general, "entropy" means disorder or chaos. But entropy has a specific meaning in cryptography: it refers to unpredictability. Cryptographers will actually measure how much entropy a given set of data has in terms of the number of bits of entropy. Because of this, Cloudflare refers to the lava lamp wall as the "Wall of Entropy."

## What if someone stands in front of the lava lamps?

Because the lava lamp wall is in the busy lobby of the Cloudflare headquarters, this happens all the time. People come and go in the lobby, walking by or stopping to talk in front of the lamps. Such obstructions become part of the randomness that the camera captures, so people partially blocking the camera's view of the lava lamps actually helps generate entropy.

## What if someone shuts off or damages the camera?

If this happens, Cloudflare still has two other sources for randomization from the Linux operating system running on Cloudflare servers. In addition, Cloudflare has easy physical access to the camera because it's in a Cloudflare-owned space, and Cloudflare can quickly turn it back on or replace it as needed.

## Do all Cloudflare offices have the lava lamp wall?

Cloudflare has offices in cities around the world, and several of them have their own methods for generating random data from real-world inputs. London takes photos of a double-pendulum system mounted in the office (a pendulum connected to a pendulum, the movements of which are mathematically unpredictable). The Austin office features hanging translucent rainbow mobiles, which twist and shift in response to random events that disturb the airflow (such as doors opening and closing) and are captured periodically on camera. And, the Lisbon Cloudflare office features a display of 50 wave machines, also photographed periodically.

## Was Cloudflare the first company to use lava lamps for encryption?

Surprisingly, no – a company called Silicon Graphics designed a similar system called "Lavarand" in 1996, although the patent has since expired.

**To learn more about the Cloudflare lava lamp wall** check out these blog posts:

  * [Randomness 101: LavaRand in Production](https://blog.cloudflare.com/randomness-101-lavarand-in-production/)

  * [LavaRand in Production: The Nitty-Gritty Technical Details](https://blog.cloudflare.com/lavarand-in-production-the-nitty-gritty-technical-details/)

  * [Harnessing chaos in Cloudflare offices: Austin's mesmerizing mobiles](https://blog.cloudflare.com/harnessing-office-chaos/)

  * [Chaos in Cloudflare’s Lisbon office: securing the Internet with wave motion](https://blog.cloudflare.com/chaos-in-cloudflare-lisbon-office-securing-the-internet-with-wave-motion/)




See [this page to learn how to use free SSL encryption from Cloudflare](https://www.cloudflare.com/application-services/products/ssl/).
