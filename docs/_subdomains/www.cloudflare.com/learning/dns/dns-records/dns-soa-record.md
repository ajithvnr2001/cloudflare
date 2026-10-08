---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/
title: What is a DNS SOA record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:07.826626+00:00
---

# What is a DNS SOA record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS SOA record? 

The SOA record contains important information about a domain and who is responsible for it. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the purpose of an SOA record 
  * Explain zone serial numbers and zone transfers 



On this page

  * What is a DNS SOA record?

  * What is a zone serial number?

  * What are the other parts of an SOA record?

  * What is a zone transfer?




## What is a DNS SOA record?

The [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) ‘start of authority’ (SOA) record stores important information about a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) or [zone](https://www.cloudflare.com/learning/dns/glossary/dns-zone/) such as the email address of the administrator, when the domain was last updated, and how long the server should wait between refreshes.

All DNS zones need an SOA record in order to conform to IETF standards. SOA records are also important for zone transfers.

Example of an SOA record:

name example.com

record type SOA

MNAME ns.primaryserver.com

RNAME admin.example.com

SERIAL 1111111111

REFRESH 86400

RETRY 7200

EXPIRE 4000000

TTL 11200

The 'RNAME' value here represents the administrator's email address, which can be confusing because it is missing the ‘@’ sign, but in an SOA record admin.example.com is the equivalent of [admin@example.com](mailto:admin@example.com).

Sign up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is a zone serial number?

In the DNS, a 'zone' is an area of control over namespace. A zone can include a single domain name, one domain and many subdomains, or many domain names. In some cases, 'zone' is essentially equivalent with 'domain,' but this is not always true.

A zone serial number is a version number for the SOA record. In the example above, the serial number is listed next to 'SERIAL.' When the serial number changes in a zone file, this alerts secondary nameservers that they should update their copies of the zone file via a zone transfer.

## What are the other parts of an SOA record?

  * MNAME: This is the name of the primary nameserver for the zone. Secondary servers that maintain duplicates of the zone's [DNS records](https://www.cloudflare.com/learning/dns/dns-records/) receive updates to the zone from this primary server.

  * REFRESH: The length of time (in seconds) secondary servers should wait before asking primary servers for the SOA record to see if it has been updated.

  * RETRY: The length of time a server should wait for asking an unresponsive primary nameserver for an update again.

  * EXPIRE: If a secondary server does not get a response from the primary server for this amount of time, it should stop responding to queries for the zone.


Report

Secure your DNS infrastructure

[Get the report →](https://www.cloudflare.com/lp/dns-and-the-threat-of-ddos/)

## What is a zone transfer?

A DNS zone transfer is the process of sending DNS record data from a [primary](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/) nameserver to a secondary nameserver. The SOA record is transferred first. The serial number tells the secondary server if its version needs to be updated. Zone transfers take place over the [TCP protocol](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/).

Learn more about various [DNS records](https://www.cloudflare.com/learning/dns/dns-records/).
