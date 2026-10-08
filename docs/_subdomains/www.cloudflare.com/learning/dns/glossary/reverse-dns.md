---
url: https://www.cloudflare.com/learning/dns/glossary/reverse-dns/
title: What is reverse DNS?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:16.434841+00:00
---

# What is reverse DNS?

> Source: https://www.cloudflare.com/learning/dns/glossary/reverse-dns/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is reverse DNS? 

A reverse DNS lookup takes an IP address and returns the domain name associated with that IP. A forward DNS lookup does just the opposite. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe a reverse DNS lookup 
  * Outline uses for reverse DNS lookups 
  * Understand what PTR records are and how they store IP addresses 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)[ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)

On this page

  * What is reverse DNS?

  * How does reverse DNS work?

  * What are reverse DNS lookups used for?




## What is reverse DNS?

A reverse [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) lookup is a DNS query for the [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) associated with a given [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). This accomplishes the opposite of the more commonly used forward DNS lookup, in which the DNS system is queried to return an IP address.

Standards from the Internet Engineering Task Force (IETF) [suggest](https://tools.ietf.org/html/rfc1912) that every domain should be capable of reverse DNS lookup, but as reverse lookups are not critical to the normal function of the Internet, they are not a hard requirement. As such, reverse DNS lookups are not universally adopted.

## How does reverse DNS work?

Reverse DNS lookups query DNS servers for a PTR (pointer) record; if the server does not have a [PTR record](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/), it cannot resolve a reverse lookup. PTR records store IP addresses with their segments reversed, and they append ".in-addr.arpa" to that. For example if a domain has an IP address of 192.0.2.1, the PTR record will store the domain's information under 1.2.0.192.in-addr.arpa.

In IPv6, the latest version of the Internet Protocol, PTR records are stored within the ".ip6.arpa" domain instead of ".in-addr.arpa."

## What are reverse DNS lookups used for?

Reverse lookups are commonly used by email servers. Email servers check and see if an email message came from a valid server before bringing it onto their network. Many email servers will reject messages from any server that does not support reverse lookups or from a server that is highly unlikely to be legitimate. Spammers often use IP addresses from hijacked machines, which means there will be no PTR record. Or, they may use dynamically assigned IP addresses that lead to server domains with highly generic names.

Logging software also employs reverse lookups in order to provide users with human-readable domains in their log data, as opposed to a bunch of numeric IP addresses.
