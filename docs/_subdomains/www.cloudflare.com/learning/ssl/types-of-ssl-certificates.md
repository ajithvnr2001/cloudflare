---
url: https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/
title: Types of SSL Certificates | SSL Certificate Types Explained
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:42.279641+00:00
---

# Types of SSL Certificates | SSL Certificate Types Explained

> Source: https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  Types of SSL certificates: SSL certificate types explained 

There are several types of different SSL certificates. While all provide the same level of TLS encryption, they serve different purposes and are used in different contexts. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the different types of SSL (TLS) certificates 
  * Learn about the different SSL certificate validation levels 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)

On this page

  * What does an SSL certificate do?

  * What are the different types of SSL certificates?

    * Single Domain SSL Certificates

    * Wildcard SSL Certificates

    * Multi-Domain SSL Certificates

  * What are SSL certificate validation levels?

    * Domain Validation SSL Certificates

    * Organization Validation SSL Certificates

    * Extended Validation SSL Certificates




## What does an SSL certificate do?

An [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) (more accurately called a [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) certificate), is necessary for a website to have [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) encryption. An SSL certificate contains the website's [public key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/), the [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) it's issued for, the issuing certificate authority's digital signature, and other important information. It's used for authenticating an origin server's identity, which helps prevent [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/), domain spoofing, and other methods attackers use to impersonate a website and trick users.

HTTPS creates an encrypted connection between a user's browser and the web server they are communicating with, protecting the communications from being intercepted. SSL certificates are necessary for establishing this encrypted connection (see [What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) to learn more).

## What are the different types of SSL certificates?

#### Single Domain SSL Certificates

A single-domain SSL certificate applies to one domain and one domain only. It cannot be used to authenticate any other domain, not even subdomains of the domain it is issued for.

All pages on this domain are also secured with the certificate; for instance, if cloudflare.com has a single-domain certificate, then cloudflare.com/learning (the Learning Center main page) is also covered by that certificate.

![Single Domain SSL Certificate](https://images.ctfassets.net/slt3lc6tev37/ND4BUNi8xaqKuKcYEfbXo/e05775718674775f2241d89c6333ab52/single-domain-ssl-certificate.svg)Single Domain SSL Certificate

#### Wildcard SSL Certificates

Wildcard SSL certificates are for a single domain and all its subdomains. A subdomain is under the umbrella of the main domain. Usually subdomains will have an address that begins with something other than 'www.'

For example, [www.cloudflare.com](http://www.cloudflare.com) has a number of subdomains, including blog.cloudflare.com, support.cloudflare.com, and developers.cloudflare.com. Each is a subdomain under the main cloudflare.com domain.

![Wildcard SSL Certificate](https://images.ctfassets.net/slt3lc6tev37/7uh7zF2RnXoBNGblm7fYfM/20d4aed32e69d6b420385e752e522ea4/wildcard-ssl-certificate.svg)Wildcard SSL Certificate

A single Wildcard SSL certificate can apply to all of these subdomains. Any subdomain will be listed in the SSL certificate. Users can see a list of subdomains covered by a particular certificate by clicking on the padlock in the URL bar of their browser, then clicking on "Certificate" (in Chrome) to view the certificate's details.

#### Multi-Domain SSL Certificates (MDC)

A multi-domain SSL certificate, or MDC, lists multiple distinct domains on one certificate. With an MDC, domains that are not subdomains of each other can share a certificate.

![Multi-Domain SSL Certificate](https://images.ctfassets.net/slt3lc6tev37/41egOiqMSGKk0tbChVC3HT/fa4517eacbe2bcd874a93e7926482850/multi-domain-ssl-certificate.svg)Multi-Domain SSL Certificate

## What are SSL certificate validation levels?

A bank doesn't issue a loan to someone before performing a credit check. Similarly, before a certificate authority (CA) issues an SSL certificate to an organization, they have to validate the organization; it has to be proven that the organization actually owns and operates the domain. This is what's known as SSL certificate validation.

However, there are different levels of validation, ranging from bare minimum validation to thorough background investigations. An SSL certificate from any of these validation levels provides the same degree of TLS encryption; the only difference is how thoroughly the CA has authenticated the organization's identity.

#### Domain Validation SSL Certificates

Domain Validation is the least-stringent level of validation. To obtain one of these SSL certificates, an organization only has to prove they control the domain. They can do this by altering the [DNS record](https://www.cloudflare.com/learning/dns/dns-records/) associated with the domain, or sometimes just by sending the CA an email. Often the process is automated.

This level of validation is the cheapest. It's a good option for blogs, portfolio sites, or for [small businesses](https://www.cloudflare.com/small-business/) that are just looking to quickly launch HTTPS, especially if a business doesn't sell products via its website (e.g. a restaurant or coffee shop).

#### Organization Validation SSL Certificates

Organization Validation involves a manual vetting process: The CA will contact the organization requesting the SSL certificate, and they may do some further investigating. Organization Validation SSL certificates will contain the organization's name and address, making them more trustworthy for users than Domain Validation certificates.

#### Extended Validation SSL Certificates

![Multi-Domain SSL Certificate](https://images.ctfassets.net/slt3lc6tev37/2mkpUOPzl2jEPEERn2e57B/3b180ecab3ff7e0a5da1706434722573/ssl-certificate-secure-browsing.png)Multi-Domain SSL Certificate

Extended Validation involves a full background check of the organization. The CA will make sure that the organization exists and is legally registered as a business, that they actually are present at the address they list, and so on. This validation level takes the longest and costs the most.

Learn more about [how to get a free SSL/TLS certificate from Cloudflare](https://www.cloudflare.com/application-services/products/ssl/).
