---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/
title: DNS A record
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:06.885304+00:00
---

# DNS A record

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  DNS A record 

The DNS A record points to the IP address for a given domain name. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the purpose of an A record 
  * Explain the main uses for A records 



On this page

  * What is a DNS A record?

  * When are DNS A records used?




## What is a DNS A record?

The "A" stands for "address" and this is the most fundamental type of [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) record: it indicates the [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of a given [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/). For example, if you pull the DNS records of cloudflare.com, the A record currently returns an IP address of: 104.17.210.9.

A records only hold IPv4 addresses. If a website has an IPv6 address, it will instead use an ["AAAA" record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/).

Here is an example of an A record:

example.com record type: value: TTL

@ A 192.0.2.1 14400

The "@" symbol in this example indicates that this is a record for the root domain, and the "14400" value is the [TTL (time to live)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/), listed in seconds. The default TTL for A records is 14,400 seconds. This means that if an A record gets updated, it takes 240 minutes (14,400 seconds) to take effect.

The vast majority of websites only have one A record, but it is possible to have several. Some higher profile websites will have several different A records as part of a technique called [round robin load balancing](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/), which can distribute request traffic to one of several IP addresses, each hosting identical content.

Sign up

Get DDoS protection with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## When are DNS A records used?

The most common usage of A records is IP address lookups: matching a domain name (like "cloudflare.com") to an IPv4 address. This enables a user's device to connect with and load a website, without the user memorizing and typing in the actual IP address. The user's web browser automatically carries this out by sending a query to a [DNS resolver](https://www.cloudflare.com/learning/dns/dns-server-types/).

DNS A records are also used for operating a Domain Name System-based Blackhole List (DNSBL). DNSBLs can help mail servers identify and block email messages from known spammer domains.

If you want to learn more about DNS A records, you can see the original 1987 RFC where A records and several other DNS record types are defined [here](https://tools.ietf.org/html/rfc1035). To learn more about how the Domain Name System works, see [What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)

Report

Secure your DNS infrastructure

[Get the report →](https://www.cloudflare.com/lp/dns-and-the-threat-of-ddos/)
