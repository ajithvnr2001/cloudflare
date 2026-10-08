---
url: https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/
title: What is quantum computing?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:34.297644+00:00
---

# What is quantum computing?

> Source: https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is quantum computing? 

Quantum computing uses quantum mechanics to perform some calculations much faster than traditional computers. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand quantum computing 
  * Compare qubits with bits 
  * Explain the potential impact of operational quantum computers 



Related content  [ What is encryption? ](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[ How do lava lamps help with Internet encryption? ](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[ What is asymmetric encryption? ](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[ What is TLS (Transport Layer Security)? ](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)

On this page

  * What is quantum computing?

  * What are bits and qubits?

  * What are the challenges of building quantum computers?

    * Interference from the outside environment

    * Error correction

    * Temperature

  * What impact would quantum computing have on the world?

    * Potential positive effects

    * Current encryption methods would break

  * What does Cloudflare do to prepare for quantum computing?

  * FAQs

    * What is quantum computing?

    * What makes a qubit different from a traditional bit?

    * Why are quantum computers so difficult to build and operate?

    * How could quantum computing affect modern digital security?

    * What are some potential positive uses for this technology?

    * What is Cloudflare doing to address the risks posed by quantum computing?




## What is quantum computing?

A quantum computer uses the properties of quantum mechanics to perform calculations. Quantum computers are much faster at certain types of calculations than classical computers (meaning any computing device in wide use today, like smartphones, servers, and desktop computers). Most importantly, quantum computing may be able to solve certain extremely difficult math problems that classic computing cannot efficiently solve at all, which would put current [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) methods at risk and expose sensitive data.

Imagine finding a chapter in a book by turning page by page until arriving at the desired place. Now imagine instead consulting the table of contents first, and almost instantly turning to the correct chapter. Quantum computing is more like the experience of using a table of contents: it examines all possible solutions to a calculation quickly and simultaneously, instead of trying different solutions until arriving at the correct one.

Technically, a classical computer can do any calculation that a quantum computer can do — given enough time. But a classical computer might need centuries or millennia to solve a problem a quantum computer could _theoretically_ solve in minutes.

In practice, researchers have produced just a handful of cases where a quantum computer solved a problem faster than a classical computer. Quantum computers are difficult to build and unstable once built. But if the challenges of constructing quantum computers are solved, quantum computing might permanently transform technology.

## What are bits and qubits?

A classical computer stores information in a series of bits. A bit is the smallest possible unit of information; its value is either 0 or 1.

A quantum computer stores information in qubits rather than bits. A qubit can have a value of 0, 1, or a mix of _both_ states (the technical term for such a mix is "superposition"). In fact, a qubit's value is _uncertain_ — unlike a classical bit, which is always known to be either 0 or 1. A qubit's value remains indeterminate until someone observes it.

As a result, a quantum computer can hold multiple states, or versions, of information at once. This enables it to process solutions to calculations at an exponentially faster pace compared to a regular computer — just as a team of people performing multiple tasks simultaneously will complete a project faster than one person doing all the tasks on their own.

Imagine a segment of information as a globe. A bit can sit either at the globe's north pole or south pole. A qubit can sit anywhere on the surface of the globe, vastly increasing the informational possibilities it can contain.

On a mechanical level, of course, bits and qubits are not actually globes. A bit is a tiny section of a computer that either holds an electrical charge (1) or does not hold an electrical charge (0). A qubit is the uncertain, unstable position of an electron within an atom.

## What are the challenges of building quantum computers?

To this point, very few quantum computers have been constructed. Those that have been built are small, unstable, and not usable outside of laboratory conditions.

This is because quantum computing faces a few major challenges:

#### Interference from the outside environment

Qubits are fragile. Noise, vibration, temperature changes, and electromagnetic waves can all inhibit or destroy the internal state of a qubit. To operate properly, quantum computers need to be in highly controlled environments that lack these and other types of interference. Such environments are difficult to construct and maintain outside of a laboratory.

Environmental factors impact classical computers as well — for instance, high temperatures or strong magnetic forces can slow or destroy a computer. But the problem is much more severe for quantum computers, to the point that it is uncertain if they can operate in real-world conditions.

(Eventually it may be possible to counteract interferences, just as a desktop computer's fan helps it counteract high temperatures.)

#### Error correction

Quantum computers are less stable in general than their classical counterparts. This makes them more prone to errors. All computers commit errors, which is why classical computers have built-in memory and processors dedicated to error correction. But quantum computers have to devote a lot more resources to error correction than classical computers, relative to their processing ability.

#### Temperature

To keep qubits stable, quantum computers have to be kept extremely cold — just a few degrees above absolute zero. Again, this makes it hard to operate them outside of highly controlled laboratory environments.

The result of these and other challenges is that very few quantum computers have been constructed with more than a handful of qubits. (A 256-qubit quantum computer was [announced](https://www.technologyreview.com/2021/11/17/1040243/quantum-computer-256-bit-startup/) in 2021, and one firm hopes to construct a 1,000-qubit quantum computer [by 2023](https://www.science.org/content/article/ibm-promises-1000-qubit-quantum-computer-milestone-2023).)

## What impact would quantum computing have on the world?

The full impact of quantum computing is difficult to determine, as it is still unclear if large-scale quantum computers are feasible, let alone if mass production of such computers is possible. This contrasts with classical computing — in most societies, miniature computers are used in almost all aspects of life, and many people carry the equivalent of a supercomputer in their pockets (as smartphones).

Powerful, stable quantum computers could have major positive impacts on society. But it is also clear that such computers would put [privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) and security at risk in new ways.

#### Potential positive effects

There are many possible applications of quantum computers. With more powerful computers, the financial industry may be able to help more accurately analyze and predict the stock market. Climatologists might be able to analyze and predict weather patterns more precisely. Transportation systems could become more efficient if quantum computers can better predict traffic patterns.

All these outcomes are still theoretical. And even if large-scale, highly stable quantum computers could be constructed, their processing results would still only be as accurate as the data they are fed. Even so, quantum computing could have a major positive impact on these or similar areas.

#### Current encryption methods would break

Today, sensitive information is often protected through the use of encryption. Encryption is the process of encoding a message using a key, so that no one can read the message except someone who has the key. Encryption protects personal data users enter on websites (through [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)), business data stored on hard disks and in servers, confidential government data, and other sensitive information.

Many types of encryption rely on difficult math problems, such as prime factorization, to protect data. The difficulty of these problems ensures that the encryption cannot be broken within a feasible amount of time. Although well-known algorithms for breaking encryption exist, it is always possible to use larger encryption keys, requiring exponentially more time (for classical computers) to find the key and break the encryption.

However, quantum computers can theoretically solve the hard problems used in currently deployed encryption methods. In this scenario, increasing key sizes does not strengthen the difficulty of the problem exponentially. Thus, breaking encryption could take significantly less time. This would allow quantum computers to break most current encryption methods, putting any encrypted data at risk of exposure.

## What does Cloudflare do to prepare for quantum computing?

Cloudflare is heavily involved with developing new quantum-resistant encryption methods that will protect sensitive information now and in the future: these methods are known as [post-quantum cryptography (PQC)](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/). This is part of Cloudflare’s larger commitment to help develop better Internet protocols, encryption standards, and privacy protections.

Cloudflare will continue contributing in this area. To learn more, see the [latest blog posts on quantum computing](https://blog.cloudflare.com/tag/post-quantum/) and encryption.

## FAQs

#### What is quantum computing?

Quantum computing uses the principles of quantum mechanics to complete certain calculations significantly faster than standard computing. While classical computers process tasks sequentially, a quantum computer can examine all possible solutions simultaneously. This capability could allow it to solve complex mathematical problems that are currently impossible for standard computers to solve in a timely manner.

#### What makes a qubit different from a traditional bit?

A traditional bit is the smallest unit of information in computing and is always in one of two states: 0 or 1. A qubit, however, can exist as a 0, a 1, or a superposition of both states at the same time. This uncertainty allows a quantum computer to hold multiple versions of information at once, enabling it to process data at an exponentially faster pace than a regular computer.

#### Why are quantum computers so difficult to build and operate?

Quantum computers are unstable and sensitive to their surroundings. Factors like temperature changes, vibrations, and electromagnetic waves can destroy a qubit's state. To function properly, these systems must be kept in highly controlled environments.

#### How could quantum computing affect modern digital security?

Most current encryption methods rely on math problems that are too difficult for classical computers to solve in a practical timeframe. Because quantum computers can solve these specific problems much faster, they could theoretically break the encryption that protects personal data, business records, and confidential government information.

#### What are some potential positive uses for this technology?

If researchers can build stable, large-scale quantum computers, they could transform various industries. Quantum computing would enable extremely fast analysis of huge volumes of data, potentially accelerating the work of medical researchers, scientists, or parties in other data-driven fields.

#### What is Cloudflare doing to address the risks posed by quantum computing?

Cloudflare is actively working on developing post-quantum cryptography (PQC). These are new, quantum-resistant encryption methods designed to keep sensitive information secure both now and in the future as quantum technology continues to advance.
