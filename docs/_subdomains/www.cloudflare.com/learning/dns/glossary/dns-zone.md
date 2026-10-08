---
url: https://www.cloudflare.com/learning/dns/glossary/dns-zone/
title: What is a DNS Zone?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:13.041959+00:00
---

# What is a DNS Zone?

> Source: https://www.cloudflare.com/learning/dns/glossary/dns-zone/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS zone? 

DNS zones break up the DNS into a clear hierarchy. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a DNS zone 
  * Differentiate between a DNS zone and a DNS server 
  * Identify three kinds of DNS zones 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)[ DNS security ](https://www.cloudflare.com/learning/dns/dns-security/)[ DNS server types ](https://www.cloudflare.com/learning/dns/dns-server-types/)

On this page

  * What is a DNS zone?

  * What is a DNS zone file?

  * What is a Reverse Lookup Zone?




## What is a DNS zone?

[The DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) is broken up into many different zones. These zones differentiate between distinctly managed areas in the DNS namespace. A DNS zone is a portion of the DNS namespace that is managed by a specific organization or administrator. A DNS zone is an administrative space which allows for more granular control of DNS components, such as [authoritative nameservers](https://www.cloudflare.com/learning/dns/dns-server-types/#authoritative-nameserver). The [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) name space is a hierarchical tree, with the DNS root domain at the top. A DNS zone starts at a domain within the tree and can also extend down into subdomains so that multiple subdomains can be managed by one entity.

A common mistake is to associate a DNS zone with a domain name or a single [DNS server](https://www.cloudflare.com/learning/dns/dns-server-types/). In fact, a DNS zone can contain multiple subdomains and multiple zones can exist on the same server. DNS zones are not necessarily physically separated from one another, zones are strictly used for delegating control.

For example, imagine a hypothetical zone for the cloudflare.com domain and three of its subdomains: support.cloudflare.com, community.cloudflare.com, and blog.cloudflare.com. Suppose the blog is a robust, independent site that needs separate administration, but the support and community pages are more closely associated with cloudflare.com and can be managed in the same zone as the primary domain. In this case, cloudflare.com as well as the support and community sites would all be in one zone, while blog.cloudflare.com would exist in its own zone.

![DNS Zone](https://www.cloudflare.com/img/learning/dns/glossary/dns-zone/dns-zone.png)DNS Zone

All of the information for a zone is stored in what’s called a DNS zone file, which is the key to understanding how a DNS zone operates.

## What is a DNS zone file?

A zone file is a plain text file stored in a DNS server that contains an actual representation of the zone and contains all the records for every domain within the zone. Zone files must always start with a [Start of Authority (SOA) record](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/), which contains important information including contact information for the zone administrator.

## What is a Reverse Lookup Zone?

A [reverse lookup zone](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/) contains mapping from an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) to the host (the opposite function of most DNS zones). These zones are used for troubleshooting, spam filtering, and [bot](https://www.cloudflare.com/learning/bots/what-is-a-bot/) detection.

Learn more about [Cloudflare's DNS](https://www.cloudflare.com/dns/)
