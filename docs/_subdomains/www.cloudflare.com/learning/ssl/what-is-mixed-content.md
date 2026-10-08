---
url: https://www.cloudflare.com/learning/ssl/what-is-mixed-content/
title: What Is Mixed Content? | HTTP vs. HTTPS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:05.791086+00:00
---

# What Is Mixed Content? | HTTP vs. HTTPS

> Source: https://www.cloudflare.com/learning/ssl/what-is-mixed-content/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is mixed content? 

Mixed content occurs when TLS-protected sites contain elements that are loaded over the unsecure HTTP protocol. This creates a vulnerability that attackers can exploit. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe the conditions that produce mixed content 
  * Differentiate between passive and active mixed content 
  * Understand how mixed content can be prevented 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What is TLS (Transport Layer Security)? ](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[ What is HTTPS? ](https://www.cloudflare.com/learning/ssl/what-is-https/)[ Why use HTTPS? ](https://www.cloudflare.com/learning/ssl/why-use-https/)

On this page

  * What is mixed content?

  * What’s the difference between passive/display mixed content and active mixed content?

  * Why don’t browsers just block all mixed content?

  * How can mixed content errors be fixed?




## What is mixed content?

With [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (also known as [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)), Internet communication is [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/), creating a more secure browsing experience. Users can easily identify TLS-encrypted sites because they have ‘https://’ in the URL instead of ‘http://’. But in some instances, an [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) site can also contain some elements that are loaded using the plaintext [HTTP protocol](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/). This creates a condition known as mixed content, sometimes referred to as ‘HTTP over HTTPS’.

![Mixed Content in a Browser](https://images.ctfassets.net/slt3lc6tev37/36LjFGezJ07DTI52fNr2XB/f113e971685d8e160f740f51b4951aea/mixed-content.png)Mixed Content in a Browser

With mixed content, users will be under the impression that they are on a secure, encrypted connection because they are on an HTTPS-protected site, but the unencrypted elements of the page create vulnerabilities, opening up those users to malicious activity such as unauthorized tracking and [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/). The severity of the vulnerability depends on whether the mixed content is passive or active.

## What’s the difference between passive/display mixed content and active mixed content?

**Passive/Display Mixed Content:** In this case, the unencrypted HTTP content is restricted to encapsulated elements on the site that cannot interact with the rest of the page – for example, images or videos. For example, an attacker can block or replace an image loaded over HTTP, but wouldn’t be able to modify the rest of the page.

**Active Mixed Content:** In this case, elements or dependencies that can interact with and alter the entire webpage are served over HTTP. These include dependencies like JavaScript files and API requests.

Active mixed content presents a more severe threat than passive/display mixed content; when compromised, it allows an attacker to take over an entire webpage, collect sensitive user input such as login credentials, serve the user a spoofed page, or redirect the user to an attacker’s site.

Most modern web browsers provide warnings in the developer console for mixed content, as well as blocking the more dangerous types of mixed content. Each browser has its own set of rules, but generally speaking, active mixed content is much more likely to be blocked.

Although passive/display mixed content poses less of a threat, it still provides an opportunity for attackers to compromise privacy and track user activity. Furthermore, since a lot of browsers allow some forms of passive mixed content and only provide users with mixed content warnings in the developer console, many users will be unaware that they are being exposed to mixed content.

![Mixed Content Errors in Chrome](https://images.ctfassets.net/slt3lc6tev37/3QrW4ClgkSb1lNdKysdjto/81977f91736a801e8d892a2406d0f92d/Screen_Shot_2019-01-14_at_4.53.45_PM.png)Mixed Content Errors in Chrome

Users on antiquated web browsers are particularly vulnerable, as these browsers may not block mixed content at all.

## Why don’t browsers just block all mixed content?

An unfortunately large number of popular websites serve mixed content in one form or another. A web browser that blocks all mixed content would be delivering a very narrow version of the web to their users. Until more websites clean up this issue, browsers must compromise by permitting some of the less severe forms of mixed content.

## How can mixed content errors be fixed?

Web developers own the responsibility for eliminating mixed content. Over time, web browsers have become more and more restrictive in regards to mixed content, and this trend will only continue. It is therefore imperative that developers eliminate mixed content if they want web browsers to continue displaying their site.

The fix for mixed content is quite simple: Web developers need to ensure that every resource on their page is loaded over HTTPS. In practice, this can prove tricky, as modern websites often load several different resources from various places.

A good tool for developers to spot all instances of mixed content on their pages is the Google Chrome developer console. Developers can also check their source code for instances of resources, such as API calls and libraries, that are loaded using an ‘http://’ URL. In some cases, the solution is simply replacing the ‘http://’ URL with ‘https://’. But first, it must be verified that an HTTPS version of that resource is available. If an encrypted version of the resource isn’t available, it will either need to be replaced or removed altogether.
