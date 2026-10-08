---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/
title: What is a DNS CNAME record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:06.999278+00:00
---

# What is a DNS CNAME record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS CNAME record? 

The DNS CNAME record works as an alias for domain names that share a single IP address. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand how CNAME records work in the context of a domain lookup 
  * Understand the relationship between CNAME records and A records 



Related content  [ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)[ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)

On this page

  * What is a DNS CNAME record?

  * Can a CNAME record point to another CNAME record?

  * What restrictions are there on using CNAME records?

    * No duplicate names

    * MX and NS records

  * When are CNAME records returned for non-CNAME queries?




## What is a DNS CNAME record?

A "canonical name" (CNAME) record points from an alias domain to a "canonical" domain. A CNAME record is used in lieu of an [A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/), when a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) or subdomain is an alias of another domain. All CNAME records must point to a domain, never to an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Imagine a scavenger hunt where each clue points to another clue, and the final clue points to the treasure. A domain with a CNAME record is like a clue that can point you to another clue (another domain with a CNAME record) or to the treasure (a domain with an A record).

For example, suppose blog.example.com has a CNAME record with a value of "example.com" (without the "blog"). This means when a [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) server hits the [DNS records](https://www.cloudflare.com/learning/dns/dns-records/) for blog.example.com, it actually triggers another DNS lookup to example.com, returning example.com’s IP address via its A record. In this case we would say that example.com is the canonical name (or true name) of blog.example.com.

Oftentimes, when sites have subdomains such as blog.example.com or shop.example.com, those subdomains will have CNAME records that point to a root domain (example.com). This way if the IP address of the host changes, only the DNS A record for the root domain needs to be updated and all the CNAME records will follow along with whatever changes are made to the root.

A frequent misconception is that a CNAME record must always resolve to the same website as the domain it points to, but this is not the case. The CNAME record only points the client to the same IP address as the root domain. Once the client hits that IP address, the web server will still handle the URL accordingly. So for instance, blog.example.com might have a CNAME that points to example.com, directing the client to example.com’s IP address. But when the client actually connects to that IP address, the web server will look at the URL, see that it is blog.example.com, and deliver the blog page rather than the home page.

Example of a CNAME record:

blog.example.com record type: value: TTL

@ CNAME is an alias of example.com 32600

In this example you can see that blog.example.com points to example.com, and assuming it is based on our [example A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/) we know that it will eventually resolve to the IP address 192.0.2.1.

Report

2026 Security Signals Report

[Get the report →](https://www.cloudflare.com/lp/security-signals-report/2026/)

## Can a CNAME record point to another CNAME record?

Pointing a CNAME record to another CNAME record is inefficient because it requires multiple DNS lookups before the domain can be loaded — which slows down the user experience — but it is possible. For example, blog.example.com could have a CNAME record that pointed to [www.example.com's](http://www.example.com's) CNAME record, which then pointed to example.com's A record.

CNAME for blog.example.com:

blog.example.com record type: value: TTL

@ CNAME is an alias of [www.example.com](http://www.example.com) 32600

Which points to a CNAME for [www.example.com](http://www.example.com):

[www.example.com](http://www.example.com) record type: value: TTL

@ CNAME is an alias of example.com 32600

This configuration adds an extra step to the DNS lookup process and should be avoided if possible. Instead, the CNAME records for both blog.example.com and [www.example.com](http://www.example.com) should point directly to example.com.

Fast & Secure DNS

Free DNS included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What restrictions are there on using CNAME records?

#### No duplicate names

No other DNS records can have the same name as any given CNAME record. What this means in practice is that other types of DNS records, like [MX](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/), [TXT](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/), A, or [SOA](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/), cannot be labeled with an alias for a domain. There also cannot be any other CNAME records with the same name.

If there is a CNAME on "blog.example.com" pointing to "example.com," there cannot be any other types of records on "blog.example.com" — they all have to be under "example.com."

Suppose Sam writes articles under the pseudonym "Mark." His legal documents, such as his birth certificate and passport, will still be under his real name, Sam, even though Mark and Sam are the same person. DNS records are similar: the alias domain can only point to the actual domain, and the "legal documents" (the other DNS records) have to be under that real domain.

There is one exception — and that is in the case of CNAME flattening, when a CNAME acts like an A/AAAA record. In fact, all proxied CNAME records behave this way. However, other records are still not permitted on the same name as a flattened CNAME record. [Learn more about CNAME flattening](https://developers.cloudflare.com/dns/cname-flattening/).

#### MX and NS records

MX and [NS records](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/) cannot point to a CNAME record; they have to point to an A record (for IPv4) or an [AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/) (for IPv6). An MX record is a mail exchange record that directs email to a mail server. An NS record is a "name server" record and indicates which DNS server is authoritative for that domain.

## When are CNAME records returned for non-CNAME queries?

As stated above, domains are not allowed, per DNS specifications, to have other DNS records on a name that already has a CNAME record.

For this reason, a query for another type of record, such as a TXT record, that uses the alias instead of the domain's true name will return a CNAME record instead of the requested record. The requester then needs to query the domain that the CNAME points to in order to get the desired record.

If Alice wants to view the TXT records for blog.example.com and sends a query for them, she will get the CNAME record back instead of the TXT record. She then needs to send a DNS query to the target of the CNAME record asking for the TXT record and will get a response if the target has a TXT record. This would be the case for other types of DNS record queries as well.

Learn more about [TXT records](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/).
