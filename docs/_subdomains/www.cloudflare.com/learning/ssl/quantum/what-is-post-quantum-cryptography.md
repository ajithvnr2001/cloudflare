---
url: https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/
title: What is post-quantum cryptography (PQC)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:34.156951+00:00
---

# What is post-quantum cryptography (PQC)?

> Source: https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is post-quantum cryptography (PQC)? 

Post-quantum cryptography (PQC) is a set of cryptographic algorithms that are designed to resist attack by quantum computers, which will be much more powerful than classical computers. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define post-quantum cryptography (PQC) 
  * Explain how quantum computing could threaten current encryption algorithms 
  * Identify key approaches and concepts within PQC 
  * Understand how to prepare for PQC adoption 
  * Recognize how Cloudflare and the industry are working toward a quantum-safe Internet 



Related content  [ What is encryption? ](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[ What is a cryptographic key? ](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[ What is TLS (Transport Layer Security)? ](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)

On this page

  * What is post-quantum cryptography?

  * What is the purpose of post-quantum cryptography?

  * How could quantum computers break current cryptography?

  * Why implement PQC now?

  * What are the important concepts in PQC?

    * Post-quantum key exchange

    * Post-quantum certificates

  * What are the threats and challenges associated with quantum computers and PQC?

    * Harvest now, decrypt later

    * Performance and network impacts of PQC

  * How to prepare for PQC adoption

    * Migrate key exchange first

    * Phase in post-quantum certificates

  * How Cloudflare is helping customers adopt PQC

  * FAQs

    * What is quantum-safe encryption?

    * What does &quot

    * What are the NIST post-quantum standards?

    * How does quantum computing threaten current cryptography?

    * Why is proactive quantum readiness important?




## What is post-quantum cryptography (PQC)?

Post-quantum cryptography (PQC) refers to cryptographic algorithms designed to be secure against an attack by a powerful quantum computer. Although large-scale [quantum computers](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/) are still in development, "harvest now, decrypt later" (HNDL) threats mean that organizations must start planning for a quantum-safe future today.

PQC aims to ensure confidential data remains secure even when extremely powerful quantum computers make current encryption methods obsolete. If encryption is like putting private information in a bank vault, then PQC is like a stronger door for the bank vault, a door that remains locked even when bank robbers have access to more advanced tools.

The U.S. National Institute of Standards and Technology (NIST) has finalized its initial set of post-quantum cryptographic standards:

  * **For post-quantum key exchange (confidentiality):** Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)

  * **For post-quantum certificates/digital signatures (authentication & integrity):** Module-Lattice-Based Digital Signature Algorithm (ML-DSA) and and Stateless Hash-Based Digital Signature Algorithm (SLH-DSA)




Additional algorithms are under development as researchers continue to work on creating cryptographic methods that will remain secure well into the future.

Outdated encryption protocols like TLS 1.1 and TLS 1.2 do not use PQC algorithms for their digital signatures and key exchanges, potentially putting data at risk.

## What is the purpose of post-quantum cryptography?

Today, [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) is widely used to protect information from those who should not have access to it. Basically, encryption scrambles data so that it is unreadable except by parties that have the key for unscrambling it. Encryption can protect digital data both in transit, as it moves from one place to another, and at rest, when it is stored on a hard disk. But quantum computers, once operational, could undo many widely deployed encryption methods.

Just as modern encryption protects data in transit and at rest from classical computing attacks, [post-quantum cryptography](https://www.cloudflare.com/the-net/quantum-computing/) ensures that when future quantum computers gain the ability to break current encryption standards (e.g., RSA, Elliptic Curve), sensitive data will remain secure. PQC is therefore essential for shielding data from malicious parties, for [complying with future data regulations](https://www.cloudflare.com/learning/privacy/what-is-data-compliance/), and for safeguarding online [data privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) protections like [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/).

## How could quantum computers break current cryptography?

Most modern encryption — including RSA and Elliptic Curve Cryptography (ECC) — relies on mathematical problems that are believed to be extraordinarily hard for classical computers to solve, like factoring large integers or computing discrete logarithms. However, by harnessing quantum phenomena like superposition and entanglement, quantum computers can run algorithms that factor large integers exponentially faster than classical computers. They will be able to solve problems that classical computers, practically speaking, cannot.

Even if quantum hardware is not yet advanced enough to do so, adversaries can record encrypted traffic now and decrypt it later when quantum technology improves. This is often referred to as harvest now, decrypt later, or HNDL.

## Why implement PQC now?

**Quantum timeline:** [Experts predict](https://globalriskinstitute.org/publication/2024-quantum-threat-timeline-report/) that cryptographically relevant quantum computers (CRQC) — those capable of breaking current [public-key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) algorithms — may only be 10-15 years away, though research breakthroughs could accelerate this. Implementing PQC in every system could take almost this long.

**Long-term data sensitivity:** Encrypted communications captured now can be stored until quantum decryption is possible. For organizations needing multi-decade confidentiality (e.g., financial institutions, governments), waiting until quantum computers exist would be too late. An example that affects everyone is the prospect of every password ever used becoming fully visible. And then consider how few people regularly change their passwords.

**Regulatory compliance:** Various governments and standards bodies are rolling out guidelines, encouraging quantum readiness by as early as 2025-2026 for some agencies. For instance, the US government issued an executive order in [January 2025](https://www.federalregister.gov/documents/2025/01/17/2025-01470/strengthening-and-promoting-innovation-in-the-nations-cybersecurity) requiring federal agencies to begin preparing for PQC.

## What are the important concepts in PQC?

#### Post-quantum key exchange

A [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) exchange is how two parties (e.g., a website and a web browser) agree on a shared secret key for encrypting their communication. Post-quantum key exchanges are built on quantum-resistant problems that quantum computers (and classical computers) are not expected to solve in a feasible amount of time. This ensures session confidentiality so that if passive attackers intercept the data, they cannot decrypt it later — even with quantum capabilities.

ML-KEM is an NIST-approved post-quantum cryptography algorithm that uses a post-quantum key exchange. (Diffie-Hellman is not a post-quantum key exchange.)

#### Post-quantum certificates

Digital certificates (e.g., X.509 or [SSL certificates](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)) verify _who_ you are connecting to, preventing impersonation or tampering. Post-quantum certificates use quantum-safe signature algorithms (like ML-DSA/Dilithium, SLH-DSA/SPHINCS+). This helps ensure that the parties in a digital connection are authenticated, and that data integrity is not violated.

Currently, post-quantum certificates are much larger in size than typical certificates, causing performance or compatibility issues with some network devices. Organizations and browsers often focus on post-quantum key exchange first, planning to introduce post-quantum certificates as the technology matures and standards stabilize.

## What are the threats and challenges associated with quantum computers and PQC?

#### Harvest now, decrypt later (HNDL)

This tactic involves intercepting and recording encrypted traffic today for future decryption once a quantum computer can break existing cryptographic algorithms. While large quantum computers do not yet exist, the interception of high-value data is happening now. This data can also impact authentication, as it could contain tokens and passwords.

#### Performance and network impacts of PQC

Post-quantum algorithms can produce larger handshake messages, which may:

  * Slow down [TLS handshakes](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) slightly

  * Trigger issues with older or misconfigured network devices expecting smaller certificates or key sizes

  * Increase [bandwidth](https://www.cloudflare.com/learning/cdn/how-cdns-reduce-bandwidth-cost/) usage if many short connections occur in rapid succession (e.g., [API requests](https://www.cloudflare.com/learning/security/api/what-is-api-call/))




[Modernized networks](https://www.cloudflare.com/learning/network-layer/how-to-prepare-for-network-modernization-projects/) and [cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)-based optimizations (such as large numbers of distributed points of presence) can help reduce or nearly eliminate these challenges in real-world usage.

## How to prepare for PQC adoption

#### Migrate key exchange first

  * **Prioritize confidentiality** against HNDL threats by migrating to post-quantum key exchange (e.g., ML-KEM)

  * **Maintain classical signatures** for certificates temporarily if post-quantum certificates cause network or performance issues

  * **Symmetric cryptography** like AES does not need to be migrated: Grover's algorithm, which is often claimed to weaken AES, is not actually practical

  * **Monitor performance** to identify any legacy devices that need upgrades




#### Phase in post-quantum certificates

  * **Plan a phased deployment**

  * **Inventory all certificate usage** in your environment (web servers, APIs, mobile apps, IoT devices, etc.).

  * **Update policies and internal processes** around certificate issuance and rotation; large organizations may have thousands of certificates to replace or upgrade




## How Cloudflare is helping customers adopt PQC

  * **Production-scale PQC:** A significant portion of Cloudflare’s TLS traffic already uses post-quantum key exchange, thanks to browser support (Chrome, Firefox, Edge) and Cloudflare’s edge deployment

  * **Edge network advantage:** Cloudflare’s [globally distributed network of data centers](https://www.cloudflare.com/network/) reduces performance overhead by terminating TLS closer to end users, minimizing latency from larger post-quantum handshakes

  * **Simple migration:** Customers can enable PQC without overhauling every [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/); Cloudflare handles encryption at the edge

  * **Zero Trust capabilities:** Beyond browser-to-cloud encryption, [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) already supports PQC connections, and Cloudflare’s [Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/) endpoint agent will soon support internal traffic

  * **Future post-quantum certificates:** As post-quantum signature algorithms mature, Cloudflare plans to roll out post-quantum certificates to further secure authentication




To summarize, Cloudflare already deploys post-quantum cryptography at scale and can help any organization transition smoothly. [Get in touch with Cloudflare](https://www.cloudflare.com/plans/enterprise/contact/) to learn how to safeguard infrastructure against quantum attacks — before they become reality.

Or, learn more about Cloudflare's latest efforts to prepare for quantum computing's threat to encryption methods [on the Cloudflare blog](https://blog.cloudflare.com/tag/post-quantum/).

## FAQs

#### What is quantum-safe encryption?

Quantum-safe encryption — more properly called quantum-resistant encryption — uses cryptographic algorithms specifically designed to withstand attacks from quantum computers. The goal of quantum-resistant encryption is to keep sensitive data secure even when current encryption methods become vulnerable. Quantum-resistant encryption is part of the field of post-quantum cryptography (PCQ).

#### What does "harvest now, decrypt later" (HNDL) mean?

"Harvest now, decrypt later" refers to attackers intercepting and storing encrypted data today with the intention of decrypting it in the future, once quantum computers can break current encryption methods.

#### What are the NIST post-quantum standards?

NIST’s initial post-quantum cryptographic standards include ML-KEM for key exchange, and ML-DSA and SLH-DSA for digital signatures. These methods are designed to be resistant to quantum-based attacks.

#### How does quantum computing threaten current cryptography?

Quantum computers can solve certain mathematical problems — like factoring large numbers — much faster than classical computers, potentially breaking today's widely used encryption methods.

#### Why is proactive quantum readiness important?

Proactive quantum readiness is crucial because experts predict quantum computers capable of breaking today’s encryption could arrive in 10–15 years, and migrating to quantum-resistant systems may take just as long. Delaying preparation could put sensitive data at risk.
