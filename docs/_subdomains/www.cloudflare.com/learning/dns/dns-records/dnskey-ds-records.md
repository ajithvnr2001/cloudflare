---
url: https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/
title: DNS DNSKEY and DS Records
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:21:21.843691+00:00
---

# DNS DNSKEY and DS Records

> Source: https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  DNS DNSKEY and DS Records 

The DNSKEY and DS records are used by DNSSEC resolvers to verify the authenticity of DNS records. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the purpose of the DNSKEY record 
  * Understand the role the DS record plays in DNSSEC 



On this page

  * What are the DNSKEY and DS records?




## What are the DNSKEY and DS records?

The [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) is the phonebook of the Internet, but it was not designed with security in mind. For this reason, an optional security protocol called [DNSSEC](https://www.cloudflare.com/dns/dnssec/how-dnssec-works/) was created so that owners of web properties could better secure their applications. DNSSEC increases security by adding cryptographic signatures to DNS records; these signatures can be checked to verify that a record came from the correct DNS server.

For the implementation of these cryptographic signatures, two new [DNS record types](https://www.cloudflare.com/learning/dns/dns-records/) were created: DNSKEY and DS. The DNSKEY record contains a public signing key, and the DS record contains a hash* of a DNSKEY record.

Each DNSSEC zone is assigned a set of [zone](https://www.cloudflare.com/learning/dns/glossary/dns-zone/) signing keys (ZSK). This set includes a private and public ZSK. The private ZSK is used to sign the DNS records in that zone, and the public ZSK is used to verify the private one.

The public ZSK is published in a DNSSEC record, which is how it is provided to a DNSSEC resolver; the resolver will use the public ZSK to ensure the records from that zone are authentic. As an added layer of security, DNSSEC zones contain a second DNSKEY record containing a key signing key (KSK), which verifies the authenticity of the public ZSK.

The DS record is used to verify the authenticity of child zones** of DNSSEC zones. The DS key record on a parent zone contains a hash of the KSK in a child zone. A DNSSEC resolver can therefore verify the authenticity of the child zone by hashing its KSK record, and comparing that to what is in the parent zone's DS record.

*_A cryptographic hash is a one-way scrambling of alphanumeric input; hashes are often used for storing sensitive information like passwords on servers. For example, a hash of the input ‘cantguessthis’ is 18fe9934cf77a759eb2471f2b304708a. Every time ‘cantguessthis’ is put through the hashing function, it outputs the same hash. But there is no way to get the original input using just the hash. The hash on its own is essentially useless._

**_A child zone is a delegated subdomain of another zone. For instance, a URL of example.com could have child zones with domains like blog.example.com and mail.example.com._
