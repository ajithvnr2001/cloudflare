---
url: https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/
title: ECDSA: The missing piece of DNSSEC
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:08.677507+00:00
---

# ECDSA: The missing piece of DNSSEC

> Source: https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  ECDSA: The missing piece of DNSSEC 

DNSSEC is a complicated topic, and making things even more confusing is the availability of several standard security algorithms for signing DNS records, defined by IANA. Algorithm 13 is a variant of the Elliptic Curve Digital Signing Algorithm (ECDSA). While currently used by less than 0.01% of domains, we’d like to argue that ECDSA helped us eliminate the final two barriers for widespread DNSSEC adoption: zone enumeration and DDoS amplification. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what is ECDSA 
  * Explore how ECDSA is used in DNSSEC 
  * Compare the performance of ECDSA and RSA 
  * Understand the benefits of using ECDSA over RSA for DNSSEC 



On this page

  * ECDSA &amp

  * ECDSA vs. RSA Performance

  * DDoS Amplification

  * ECDSA vs. RSA Response Size

  * Current State of ECDSA and DNSSEC

  * DNSSEC Security Algorithms in the Root Zone

  * The Alexa One Million

  * Drawbacks of ECDSA

  * Conclusion




DNSSEC is a [complicated topic](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/), and making things even more confusing is the availability of several standard security algorithms for signing DNS records, [defined by IANA](http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml). Algorithm 13 is a variant of the [Elliptic Curve Digital Signing Algorithm](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/) (ECDSA). While currently used by less than 0.01% of domains, we’d like to argue that ECDSA helped us eliminate the final two barriers for widespread DNSSEC adoption: zone enumeration and DDoS amplification.

Zone enumeration is prevented by live signing, and this is only computationally efficient with the fast signature generation of ECDSA. Elliptic curves also produce significantly smaller keys and signatures than their RSA counterparts, which means responses to DNS queries are smaller. This greatly reduces the amplification factor of DNS-based DDoS attacks.

## ECDSA & DNSSEC - Zone Enumeration

DNSSEC introduces authenticated denial-of-existence via NSEC and NSEC3 records. However, as we discussed in [DNSSEC Complexities and Considerations](https://www.cloudflare.com/dns/dnssec/dnssec-complexities-and-considerations/), both NSEC and NSEC3 allow attackers to walk the zone. The solution is a clever technique called “DNSSEC white lies” (described in RFCs [4470](https://www.ietf.org/rfc/rfc4470.txt) and [4471](https://www.ietf.org/rfc/rfc4471.txt)), but it can only be implemented if DNSSEC records are signed on-the-fly.

RSA is the most widespread signing algorithm is DNSSEC, partly because it’s the only required algorithm defined by the protocol. Unfortunately, live signing with RSA is prohibitively expensive.

## ECDSA vs. RSA Performance

The performance gains of ECDSA are dramatic. It’s 10x less computationally expensive to generate an ECDSA signature than a comparable RSA signature. This makes live signing (and DNSSEC white lies) feasible, even at scale.

During our DNSSEC beta (with less than a 1,000 domains signed), Cloudflare has been answering tens of thousands of DNSSEC queries per second. That comes out to over 1 billion queries a day, and we sign all of the necessary RRSIG records on-the-fly. Having a signing algorithm that’s 10x faster than RSA makes a big difference when it comes to load on our DNSSEC servers.

When we started working with ECDSA, the OpenSSL implementation we used was in Go. Considering all the signing that we’re doing, optimizing signature generation was a serious priority. So, we re-wrote the ECDSA implementation is low-level assembly, and now it’s over 20x faster than it was in Go. That code is open sourced and will make it into Go 1.7 so that the entire crypto community can take advantage of our optimizations. [Learn more](https://blog.cloudflare.com/go-crypto-bridging-the-performance-gap/)

## DDoS Amplification

Cloudflare is the [largest](https://www.datanyze.com/market-share/dns/Alexa%20top%201M/cloudflare-dns-market-share) managed DNS provider in the world. What we really don’t want is to turn our DNSSEC servers into an amplification vector for distributed denial-of-service (DDoS) attacks. Every time you request a record from a DNSSEC server, it also returns the signature associated with that record, as well as the public key used to verify that signature. That’s potentially a lot of information.

Making the response size for DNSSEC queries as small as possible is an important requirement to prevent abuse of our DNS infrastructure by would-be attackers. The small size of ECDSA keys and signatures goes a long way towards that end.

## ECDSA vs. RSA Response Size

Achieving 128-bit security with ECDSA requires a 256-bit key, while a comparable RSA key would be 3072 bits. That’s a 12x amplification factor just from the keys. You can read more about why cryptographic keys are different sizes in [this blog post](https://blog.cloudflare.com/why-are-some-keys-small/).

But, most RSA keys are not 3072 bits, so a 12x amplification factor may not be the most realistic figure. Let’s take a look at a worst-case real-world scenario for DDoS amplification, which is a negative response (NSEC record). For a [domain behind Cloudflare](https://www.cloudflare.com/products/registrar/) (which uses ECDSA signatures and DNSSEC white lies), a typical DNSSEC response is 377 bytes. Compare this to 1075 bytes for a domain not using ECDSA or DNSSEC white lies.

When you consider the fact that every other large-scale DNSSEC implementation relies on RSA signatures, it’s unappealing for an attacker to leverage our DNSSEC infrastructure as a DDoS vector.

## Current State of ECDSA and DNSSEC

ECDSA solves major problems in DNSSEC, but it’s barely leveraged by the global DNSSEC community. We took a brief look at ECDSA adoption in the root DNS zone and the Alexa one million.

## DNSSEC Security Algorithms in the Root Zone

First, we examined the root DNS zone to see which DNSSEC algorithms the top level domains are using. The following table shows the security algorithms specified by the DS records in the root zone file:

`curl -s http://www.internic.net/domain/root.zone | awk '$4 == "DS" { print $6}' | sort -n | uniq -c`

## The Alexa One Million

We performed a similar analysis for the Alexa one million, which gives us a decent cross section of global Internet traffic:

Algorithm Number of DS records signed

1 (RSA/MD5) 1

3 (DSA/SHA1) 10

5 (RSA/SHA-1) 3322

7 (RSASHA1-NSEC3-SHA1) 5083

8 (RSA/SHA-256) 7003

10 (RSA/SHA-512) 201

13 (ECDSA Curve P-256 with SHA-256) 23

The most striking revelation is that only 15,643 of the 1,000,000 websites are DNSSEC-enabled in any capacity. Of that 1.5%, only 23 zones are signed with Algorithm 13. And, over half of those Algorithm 13 zones are behind the Cloudflare network. That means there’s less than a dozen zones in the Alexa one million using ECDSA outside of Cloudflare. This supports [Roland van Rijswijk-Deij et al.’s](http://www.sigcomm.org/sites/default/files/ccr/papers/2015/October/0000000-0000002.pdf) findings that 99.99% of signed domains in .com, .net, and [.org](https://www.cloudflare.com/application-services/products/registrar/buy-org-domains/) use RSA.

So, why is Algorithm 13 usage so low, especially given the fact that it solves such major problems in DNSSEC? Well, RSA was introduced with DNSSEC from the very beginning of the protocol. ECDSA is a new cryptographic algorithm, and resolvers, registrars, and registries are still catching up.

## Drawbacks of ECDSA

ECDSA is not without its trade-offs. According to [Roland van Rijswijk-Deij et al](http://www.sigcomm.org/sites/default/files/ccr/papers/2015/October/0000000-0000002.pdf)., only 80% of resolvers support ECDSA validation. This number is growing, but it means that if we switched the entire DNSSEC Internet onto ECDSA right now, DNSSEC validation would fail for millions of Internet users everyday and fall back to returning unverified DNS records.

Furthermore, while ECDSA signature creation is faster than RSA, signature validation is actually much slower. Roland van Rijswijk-Deij et al. showed that, even with the ECDSA optimizations that we contributed to OpenSSL, ECDSA is still 6.6 times slower than 1024-bit RSA (which is the most common algorithm used for zone-signing keys). This is a serious problem, because overloading DNS resolvers could potentially slow down the entire Internet.

## Conclusion

There’s one very important caveat to all this Algorithm 13 discussion: only 1.5% of web properties support DNSSEC in any capacity. Not all [registrars](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/) support DNSSEC, and adding support is not trivial. They need to allow their users to upload DS records, which, in turn, need to be uploaded to the registry by the registrar. We’re working to make this an [automated process](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/) so the registrant doesn’t even need to upload the DS record, but it still requires intervention by the registrar.

The good news is, we’re trending in the right direction. Over the last 12 months, DNSSEC in general has seen a decent amount of growth. And, in the three weeks between our public DNSSEC beta and our Universal DNSSEC announcement, Hover, OVH, Metaname, Internet.bs, and the .NZ registry have added support for Algorithm 13.

We believe that DNSSEC is an essential technology for the modern web and that ECDSA makes global DNSSEC adoption a real possibility. Hopefully, we’ll continue seeing support for Algorithm 13 from registrars and registries, big and small.
