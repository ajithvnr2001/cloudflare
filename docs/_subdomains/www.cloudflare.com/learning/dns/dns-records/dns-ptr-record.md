---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/
title: What Is a DNS PTR Record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:07.696671+00:00
---

# What Is a DNS PTR Record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS PTR record? 

The PTR record is used for reverse DNS lookups. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the purpose of a PTR record 
  * Explain how PTR records are stored 
  * Explain some of the uses for PTR records 



On this page

  * What is a DNS PTR record?

  * How are DNS PTR records stored?

  * What are some of the main uses for PTR records?




## What is a DNS PTR record?

The [Domain Name System, or DNS](https://www.cloudflare.com/learning/dns/what-is-dns/), correlates [domain names](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) with [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). A DNS pointer record (PTR for short) provides the domain name associated with an IP address. A DNS PTR record is exactly the opposite of the ['A' record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/), which provides the IP address associated with a domain name.

DNS PTR records are used in [reverse DNS lookups](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/). When a user attempts to reach a domain name in their browser, a DNS lookup occurs, matching the domain name to the IP address. A reverse DNS lookup is the opposite of this process: it is a query that starts with the IP address and looks up the domain name.

Sign up

Free SSL included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## How are DNS PTR records stored?

_In IPv4:_

While DNS A records are stored under the given domain name, DNS PTR records are stored under the IP address — reversed, and with ".in-addr.arpa" added. For example, the PTR record for the IP address 192.0.2.255 would be stored under "255.2.0.192.in-addr.arpa".

"in-addr.arpa" has to be added because PTR records are stored within the .arpa top-level domain in the DNS. .arpa is a domain used mostly for managing network infrastructure, and it was [the first](https://tools.ietf.org/html/rfc881) top-level domain name defined for the Internet. (The name "arpa" dates back to the earliest days of the Internet: it takes its name from the Advanced Research Projects Agency (ARPA), which created ARPANET, an important precursor to the Internet.)

in-addr.arpa is the namespace within .arpa for reverse DNS lookups in IPv4.

_In IPv6:_

IPv6 addresses are constructed differently from IPv4 addresses, and IPv6 PTR records exist in a different namespace within .arpa. IPv6 PTR records are stored under the IPv6 address, reversed and converted into four-bit sections (as opposed to 8-bit sections, as in IPv4), plus ".ip6.arpa".

Report

Secure your DNS infrastructure

[Get the report →](https://www.cloudflare.com/lp/dns-and-the-threat-of-ddos/)

## What are some of the main uses for PTR records?

PTR records are used in reverse DNS lookups; common uses for reverse DNS include:

**Anti-spam:** Some email anti-spam filters use reverse DNS to check the domain names of email addresses and see if the associated IP addresses are likely to be used by legitimate email servers.

**Troubleshooting email delivery issues:** Because anti-spam filters perform these checks, email delivery problems can result from a misconfigured or missing PTR record. If a domain has no PTR record, or if the PTR record contains the wrong domain, email services may block all emails from that domain.

**Logging:** System logs typically record only IP addresses; a reverse DNS lookup can convert these into domain names for logs that are more human-readable.
