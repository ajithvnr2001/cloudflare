---
url: https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/
title: Universal DNSSEC
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:09.530478+00:00
---

# Universal DNSSEC

> Source: https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  Universal DNSSEC 

DNSSEC improves the trust and integrity of DNS. Often referred to as the phone book of the Internet, DNS translates domain names into numeric Internet addresses. However, DNS is a fundamentally insecure protocol. It does not guarantee where DNS records come from, and it accepts any address given to it, no questions asked. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what DNSSEC is 
  * Understand the importance of DNSSEC 
  * Learn how Cloudflare makes the deployment of DNSSEC easy 



On this page

  * What Is DNSSEC?

  * Why Does DNSSEC Matter?

  * Introducing Universal DNSSEC

  * DNSSEC at Scale

  * Cloudflare Makes DNSSEC Easy




Cloudflare offers easy-to-use DNSSEC, and it only takes a few minutes to set up.

[Sign Up Now](https://dash.cloudflare.com/sign-up)

## What Is DNSSEC?

DNSSEC adds a layer of security to an otherwise insecure protocol by verifying DNS records using cryptographic signatures. By checking the signature associated with a record, DNS resolvers can verify that the requested information comes from its authoritative nameserver and not a man-in-the-middle attacker. With DNSSEC, those visiting your domain are guaranteed to see the content on your website and not somebody else’s web server.

Learn more about [how DNSSEC works](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/).

## Why Does DNSSEC Matter?

DNS cache poisoning and answer forgery has been a known vulnerability in the global DNS infrastructure since the beginning of DNS, for example the well-known [Kaminsky attack](https://blog.cloudflare.com/dnssec-an-introduction/). Cache poisoning occurs when an attacker tricks a DNS nameserver into storing incorrect records. Until the cache entry expires, that nameserver will return the fake DNS records to everyone else that asks.

This allows an attacker to hijack traffic to your website. Instead of being directed to your website when they type your domain into a web browser, your visitors are routed to somebody else’s server without even knowing something went wrong. Attackers can use DNS hijacking for phishing schemes, serving unsolicited advertisements, monitoring web traffic, and blocking access to specific domains.

If you care about the integrity and reputation of your website, you should care about DNSSEC.

## Introducing Universal DNSSEC

DNSSEC adds a layer of security to an otherwise insecure protocol by verifying DNS records using cryptographic signatures. By checking the signature associated with a record, DNS resolvers can verify that the requested information comes from its authoritative nameserver and not a man-in-the-middle attacker. With DNSSEC, those visiting your domain are guaranteed to see the content on your website and not somebody else’s web server.

With Universal DNSSEC, your web property will benefit from:
    
    
    - Protection from DNS man-in-the-middle attacks
    

  * Protection from DNS zone enumeration

  * A user-friendly solution for meeting .bank, .trust, and .gov TLD requirements




DNSSEC prevents man-in-the-middle attacks by establishing a chain of trust all the way up to the root DNS nameservers. This chain of trust ensures that the DNS records a visitor asked for haven’t been tampered with en-route.

Cloudflare’s unique DNSSEC implementation leverages [elliptic curve cryptography](https://www.cloudflare.com/dns/dnssec/ecdsa-and-dnssec/) to prevent attackers from walking your zone and discovering private DNS records.

Top-level domains (TLDs) like .bank and .trust are designed to convey trust to visitors. This is accomplished by requiring domain owners to follow various security protocols, including DNSSEC. Implementing DNSSEC on your own can be a difficult, error-prone process. Cloudflare lets you fulfill your DNSSEC requirement with only a few clicks.

## DNSSEC at Scale

Cloudflare protects billions of requests a day with DNSSEC. That’s hundreds of millions of people a week protected from DNS cache poisoning and man-in-the-middle attacks.

Universal DNSSEC is built on top of the Cloudflare network, which has withstood some of the largest DDoS attacks in the world. We’ve even taken [special precautions](https://www.cloudflare.com/dns/dnssec/ecdsa-and-dnssec/) to make sure our DNSSEC implementation isn’t abused for DDoS amplification attacks. You can rest assured that your DNS records are returned to visitors quickly and efficiently, even when your website is under attack.

## Cloudflare Makes DNSSEC Easy

Universal DNSSEC is now available to all websites on Cloudflare, for free. We’ll do all the heavy lifting by signing your zone and managing the keys. [Protecting your domain](https://www.cloudflare.com/products/registrar/) from DNS forgeries is just a few clicks away. All you need to do is enable DNSSEC in your Cloudflare dashboard and add one DNS record to your [registrar](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/).
    
    
    - Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/login) and select your account and domain.
    

  * Go to **DNS** > **Settings**.

  * For **DNSSEC** , click **Enable DNSSEC**.

  * In the dialog, you have access to several necessary values to help you create a **DS** record at your registrar. Once you close the dialog, you can access this information by clicking **DS record** on the **DNSSEC** card.


![enabling-dnssec](https://images.ctfassets.net/slt3lc6tev37/tWn6gFRYsRWZgtx2Nf25k/38ff5ca1897784c3d55d9e565fec1edd/Universal-DNSSEC-instructions-image.png)enabling-dnssec

Once your registrar publishes the DS record, your domain will be DNSSEC-enabled. You can verify your DNSSEC configuration with the third-party [DNSViz](http://dnsviz.net/) tool.

Universal DNSSEC is designed to work seamlessly with all other Cloudflare security and performance features, including Universal SSL, a global CDN, and automatic web content optimization.
