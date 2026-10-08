---
url: https://www.cloudflare.com/learning/ssl/common-errors/
title: SSL certificate errors and how to fix them
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:04.641137+00:00
---

# SSL certificate errors and how to fix them

> Source: https://www.cloudflare.com/learning/ssl/common-errors/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  SSL certificate errors and how to fix them 

If a website's SSL certificate is expired or incorrect, web users may be dissuaded from loading the website. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what SSL, or TLS, is and does 
  * List common SSL errors 
  * Understand how to fix these errors 



Related content  [ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is TLS (Transport Layer Security)? ](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[ What is encryption? ](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What does 'Your connection is not private' mean? ](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)

On this page

  * SSL certificate errors and how to fix them

  * What is an SSL error?

  * SSL certificate is not trusted

  * Wrong TLS version

  * Expired SSL certificate

  * SSL common name mismatch error

  * Host server does not use SNI

  * How does Cloudflare eliminate SSL certificate errors?




## SSL certificate errors and how to fix them

[Secure Sockets Layer (SSL)](https://www.cloudflare.com/learning/ssl/what-is-ssl/) is a [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) for [encrypting](https://www.cloudflare.com/learning/ssl/what-is-encryption/) and authenticating data traveling between clients and servers on the Internet. The updated version of the protocol is called [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/).

SSL/TLS relies on the use of an [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/), which is a data file hosted on a web server that helps encrypt traffic and verify the server's identity. The server and the client (the device used by a person trying to reach the website hosted on the server) use the SSL certificate to establish symmetric [encryption keys](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) and begin a secure, encrypted transmission — all in a matter of milliseconds. Encrypting the data passing between users and servers helps to prevent data compromises, allowing websites to retain user trust and meet compliance requirements.

## What is an SSL error?

SSL/TLS certificate problems can stop users from safely loading and accessing websites and applications. Below are some of the common SSL certificate errors (or TLS errors) that users and website administrators may encounter.

## SSL certificate is not trusted

Most SSL certificates are issued, and signed, by an external organization called a certificate authority. Self-signed certificates are often not trusted by browsers, since no external authority verified the certificate. A certificate authority may also not be recognized by the browser for some other reason: SSL certificates issued by Symantec, for example, are [no longer trusted](https://developers.google.com/search/blog/2018/04/distrust-of-symantec-pki-immediate) by major browsers. This SSL certificate error can result in a "[Your connection is not private](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)" message in the browser, which can prevent users from visiting the website.

Getting an SSL certificate from a more widely supported certificate authority can fix this error. (Cloudflare, for instance, offers [SSL certificates for free](https://www.cloudflare.com/application-services/products/ssl/) that are trusted by all browsers.)

## Wrong TLS version

The Internet community has updated the SSL/TLS protocol many times over the years to fix vulnerabilities and make the authentication process faster — the name change from SSL to TLS reflects this.

Many web services have started to enforce the usage of the latest protocols. The most current and widely used version of TLS is [TLS 1.3](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3/), with TLS 1.2 remaining in use as well.

For web hosts and websites configured to only accept the most secure protocols, clients must support TLS 1.2 at minimum or else the TLS handshake cannot take place as planned. (The error "a fatal error occurred while creating a TLS client credential" may be observed in such cases.) A user should make sure the browser and operating system on their device support the newest, most secure versions of TLS to avoid this SSL certificate error.

## Expired SSL certificate

Just as some government-issued identification documents like passports expire after a certain number of years, SSL certificates have to be renewed periodically. This helps ensure that the same entity still operates the web service in question, just like updating one's passport photo helps to confirm one's identity. An expired SSL certificate will not be trusted by a client's web browser, so the [TLS handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) cannot proceed and no secure connection can be established.

To fix this SSL issue, web administrators need to make sure their SSL certificates are all up to date for their [domains](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) and subdomains.

This error can also occur if the client's clock is incorrect: In such a case, the client's browser may not be able to tell if the SSL certificate has expired. Resetting the clock on the client device fixes the error in such cases.

## SSL common name mismatch error

A name mismatch error occurs when the name on the SSL certificate does not match the URL entered by the client. This can happen if the user has entered a different [top-level domain](https://www.cloudflare.com/learning/dns/top-level-domain/) than expected, typed "www" when that name is not listed on the certificate, or misspelled the domain in some other way. A name mismatch can also occur if the website operator has mislabeled their certificate or has failed to include all the public-facing names of their domain. Finally, a common name mismatch error can happen when either the client or the server does not support the SNI extension (more on this below).

To avoid this error, website administrators should make sure they spell the domain correctly on their SSL certificates. Additionally, the Subject Alternative Name (SAN) section of the SSL certificate should list all the legitimate alternative presentations of the domain name.

## Host server does not use SNI

[Server Name Indication (SNI)](https://www.cloudflare.com/learning/ssl/what-is-sni/) is an extension to the TLS protocol for use when multiple domains are hosted on one server. When a client starts a connection, it is connecting directly to a server (indicated by an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)). That server could be hosting multiple websites — like an apartment building in which multiple residents live.

SNI is an extension that, to continue the analogy, puts an apartment number on the address so that the server knows to which website — or "apartment" — to direct the request for an SSL connection. But if the request to the server does not use SNI, the server might show the wrong SSL certificate to clients initiating a connection, resulting in a common name mismatch error.

To avoid this error, website administrators should use web hosts that support the latest TLS protocols, including SNI (and [encrypted SNI](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)).

## How does Cloudflare eliminate SSL certificate errors?

Cloudflare helps website operators avoid these errors by automatically managing and renewing certificates for all customer websites. Making sure certificates are not expired can be a full-time job when organizations have dozens, hundreds, or millions of subdomains to manage. But Cloudflare automates this process.

Learn about Cloudflare SSL certificate options on the [Plans page](https://www.cloudflare.com/plans/). For additional help, [join the Cloudflare Community](https://community.cloudflare.com/t/communitytip-security-faq-read-me-first/248922?q=cdn&utm_campaign=learningcenter&utm_content=ssl_troubleshooting_lp) for free support and insights from other Cloudflare users.
