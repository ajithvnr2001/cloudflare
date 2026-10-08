---
url: https://www.cloudflare.com/learning/dns/glossary/dns-root-server/
title: DNS Root Server
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:12.633257+00:00
---

# DNS Root Server

> Source: https://www.cloudflare.com/learning/dns/glossary/dns-root-server/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  DNS root server 

A DNS root server is the first stop in a DNS lookup. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a DNS root server 
  * Understand how the 13 root server networks are distributed worldwide 
  * Outline how a resolver communicates with root servers 



Related content  [ DNS server types ](https://www.cloudflare.com/learning/dns/dns-server-types/)

On this page

  * What is a DNS root server?

  * Why are there only 13 DNS root server addresses?

  * Who operates DNS root servers?

  * How do resolvers find DNS root servers?

  * What happens if a DNS root server becomes unavailable?




## What is a DNS root server?

The administration of the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) is structured in a hierarchy using different managed areas or [“zones”](https://www.cloudflare.com/learning/dns/glossary/dns-zone/), with the root zone at the very top of that hierarchy. Root servers are DNS nameservers that operate in the root zone. These servers can directly answer queries for records stored or cached within the root zone, and they can also refer other requests to the appropriate [Top Level Domain (TLD) server](https://www.cloudflare.com/learning/dns/dns-server-types/). The TLD servers are the DNS server group one step below root servers in the DNS hierarchy, and they are an integral part of resolving DNS queries.

![DNS Heirarchy](https://www.cloudflare.com/img/learning/dns/glossary/dns-root-server/dns-root-server.png)DNS Heirarchy

During an uncached DNS query, whenever a user enters a web address into their browser, this action triggers a DNS lookup, and all DNS lookups start at the root zone. Once the lookup hits the root zone, the lookup will then travel down the hierarchy of the DNS system, first hitting the TLDs servers, then the servers for specific domains (and possibly subdomains) until it finally hits the [authoritative nameserver](https://www.cloudflare.com/learning/dns/dns-server-types/) for the correct domain, which contains the numerical [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of the website being sought. This IP address is then returned to the client. Interestingly, despite the number of steps required, this process can happen very quickly.

Root servers are an essential part of the infrastructure of the Internet; web browsers and many other internet tools would not work without them. There are 13 different IP addresses that serve the DNS root zone, and hundreds of redundant root servers exist around the globe to handle requests to the root zone.

## Why are there only 13 DNS root server addresses?

A common misconception is that there are only 13 root servers in the world. In reality there are many more, but still only 13 IP addresses used to query the different root server networks. Limitations in the original architecture of DNS require there to be a maximum of 13 server addresses in the root zone. In the early days of the Internet, there was only one server for each of the 13 IP addresses, most of which were located in the United States.

Today each of the 13 IP addresses has several servers, which use [Anycast routing](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) to distribute requests based on load and proximity. Right now there are over 600 different DNS root servers distributed across every populated continent on earth.

## Who operates DNS root servers?

The Internet Corporation for Assigned Names and Numbers (ICANN) operates servers for one of the 13 IP addresses in the root zone and delegated operation of the other 12 IP addresses to various organizations including NASA, the University of Maryland, and Verisign, which is the only organization that operates two of the root IP addresses. Cloudflare actually helps provide DNS Anycast services to one of the root servers known as the F-Root; Cloudflare supplies additional F-Root instances under contract with ISC (the F-Root operator). [Learn more about how Cloudflare supports the F-Root.](https://blog.cloudflare.com/f-root/)

## How do resolvers find DNS root servers?

Since the DNS root zone is at the top of the DNS hierarchy, recursive resolvers cannot be directed to them in a DNS lookup. Because of this, every DNS resolver has a list of the 13 IP root server addresses built into its software. Whenever a DNS lookup is initiated, the recursor’s first communication is with one of those 13 IP addresses.

## What happens if a DNS root server becomes unavailable?

Thanks to the use of Anycast routing and heavy redundancy, the root servers are very reliable. But on rare occasions a root server will have to update its IP address. In this case, recursive resolvers can continue using the other 12 IP addresses in the root zone to perform DNS lookups until their software is updated with the correct addresses of all 13 servers. Since resolvers will retry until they reach a working root server, there is no disruption to the normal operations of the Internet when one root server is down. Learn more about how [Cloudflare DNS](https://www.cloudflare.com/dns/) uses Anycast routing to improve reliability.
