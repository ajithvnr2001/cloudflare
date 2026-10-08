---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/
title: DNS NS record
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:07.769954+00:00
---

# DNS NS record

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  DNS NS record 

The NS record indicates which DNS server is authoritative. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define NS records 
  * Explain when NS records should be updated 



On this page

  * What is a DNS NS record?

  * What is a nameserver?

  * When should NS records be updated or changed?




## What is a DNS NS record?

NS stands for ‘nameserver,’ and the nameserver record indicates which [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) server is authoritative for that [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) (i.e. which server contains the actual [DNS records](https://www.cloudflare.com/learning/dns/dns-records/)). Basically, NS records tell the Internet where to go to find out a domain's [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). A domain often has multiple NS records which can indicate [primary and secondary nameservers](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/) for that domain. Without properly configured NS records, users will be unable to load a website or application.

Here is an example of an NS record:

example.com record type: value: TTL

@ NS ns1.exampleserver.com 21600

Note that NS records can never point to a [canonical name (CNAME) record](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/).

## What is a nameserver?

A nameserver is a type of DNS server. It is the server that stores all DNS records for a domain, including [A records](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/), [MX records](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/), or CNAME records.

Almost all domains rely on multiple nameservers to increase reliability: if one nameserver goes down or is unavailable, DNS queries can go to another one. Typically there is one primary nameserver and several secondary nameservers, which store exact copies of the DNS records in the primary server. Updating the primary nameserver will trigger an update of the secondary nameservers as well.

When multiple nameservers are used (as in most cases), NS records should list more than one server. Learn more about [DNS servers](https://www.cloudflare.com/learning/dns/dns-server-types/).

## When should NS records be updated or changed?

Domain administrators should update their NS records when they need to change their domain's nameservers. For instance, some cloud providers provide nameservers and require their customers to point to them.

Admins may also wish to update their NS records if they want a subdomain to use different nameservers. In the example above, the nameserver for example.com is ns1.exampleserver.com. If the example.com admin wanted blog.example.com to resolve via a ns2.exampleserver.com instead, they could set this up by updating the NS record.

When NS records are updated, it may take several hours for the changes to be replicated throughout the DNS.
