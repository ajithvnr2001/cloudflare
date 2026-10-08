---
url: https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/
title: Primary vs Secondary DNS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:16.467643+00:00
---

# Primary vs Secondary DNS

> Source: https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  Primary vs secondary DNS 

Primary DNS servers host controlling zone files, while secondary DNS servers are used for reliability and redundancy. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define what a primary DNS server does 
  * Understand the difference between a primary vs. secondary DNS server 
  * Understand the function of dynamic DNS (DDNS) 



Related content  [ DNS server types ](https://www.cloudflare.com/learning/dns/dns-server-types/)[ DNS security ](https://www.cloudflare.com/learning/dns/dns-security/)

On this page

  * What is a primary DNS server?

  * What is a secondary DNS server?

  * How is a primary DNS server configured?

  * What are the benefits of using a secondary DNS server?

  * What is dynamic DNS?

  * Does Cloudflare offer primary or secondary DNS?




## What is a primary DNS server?

[DNS](https://www.cloudflare.com/learning/dns/what-is-dns/), or the Domain Name System, translates domain names into [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) so users can easily navigate to sites on the Internet without having to memorize long, specific strings of numbers and letters.

In this system, a primary [DNS server](https://www.cloudflare.com/learning/dns/dns-server-types/) is a server that hosts a website’s primary [zone file](https://www.cloudflare.com/learning/dns/glossary/dns-zone/). This is a text database file that contains all of the authoritative information for a domain, including its IP address, the identity of the domain administrator, and various resource records. Resource records list domain names alongside their corresponding IP addresses, and can take several different forms:

  * **[A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/):** Directs a domain to an IPv4 address

  * **AAAA record:** Directs a domain to an IPv6 address

  * **[MX record](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/):** Assigns a mail server to a domain

  * **[NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/):** Identifies authoritative DNS servers for a domain




Primary servers are also responsible for making any necessary changes to a zone’s [DNS records](https://www.cloudflare.com/learning/dns/dns-records/). Once the primary server has completed the update, it can then pass along change requests to the secondary servers.

## What is a secondary DNS server?

Primary DNS servers contain all relevant resource records and handle DNS queries for a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/). By contrast, secondary DNS servers contain zone file copies that are read-only, meaning they cannot be modified. Instead of getting their information from local files, they receive pertinent information from a primary server in a communication process known as a zone transfer.

Zone transfers become more complicated when they are completed between multiple secondary servers. If several secondary servers are in use, one may be designated as a higher-tier secondary server so that it is capable of replicating zone file copies to the remaining pool of secondary servers.

## How is a primary DNS server configured?

A server administrator may choose to designate a DNS server as a primary or secondary server. In some cases, a server can be primary for one zone and secondary for another zone.

Although each zone is limited to one primary DNS server, it can have any number of secondary DNS servers. Maintaining one or more secondary servers ensures that queries can be resolved even if the primary server becomes unresponsive.

## What are the benefits of using a secondary DNS server?

Although secondary DNS servers are not necessary to complete DNS queries for a domain, it is standard practice (and required by many [registrars](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)) to establish at least one.

There are two main benefits of using a secondary DNS server:

  * **Redundancy and resiliency:** Relying on just one DNS server creates a single point of failure. If the primary server fails or is compromised by an [attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/), prospective visitors can no longer access the desired domain. Using secondary servers creates redundancy and makes it less likely that users will experience a disruption of service.

  * **Load balancing:** Secondary DNS servers can share the burden of incoming requests to the domain so that the primary server doesn’t get overloaded and cause a denial-of-service. They do this using [round-robin DNS](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/), a load balancing technique designed to send roughly equal amounts of traffic to each server.




## What is dynamic DNS?

[Dynamic DNS (DDNS)](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/) is a service that keeps IP addresses automatically updated. This is especially useful for smaller web properties (personal websites, small businesses, etc.) that are not assigned static IPs, but instead temporarily lease IPs from their Internet Service Provider (ISP).

Rather than making frequent manual changes to a domain’s IP address via the primary server, users can employ DDNS to automatically update their DNS records with the most current IP address that has been assigned to their domain.

## Does Cloudflare offer primary or secondary DNS?

Cloudflare offers a [managed DNS service](https://www.cloudflare.com/dns/) that can be configured in a hidden primary setup or as a secondary DNS service. In a hidden primary setup, users establish an unlisted primary server to store all zone files and changes, then enable one or more secondary servers to receive and resolve queries. Although the secondary servers essentially fulfill the function of a primary server, the hidden setup allows users to hide their origin IP and shield it from attacks.
