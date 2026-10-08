---
url: https://www.cloudflare.com/learning/dns/what-is-anycast-dns/
title: What is Anycast DNS? | How Anycast Works With DNS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:53.112406+00:00
---

# What is Anycast DNS? | How Anycast Works With DNS

> Source: https://www.cloudflare.com/learning/dns/what-is-anycast-dns/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is Anycast DNS? | How Anycast works with DNS 

Anycast helps speed up the DNS resolution process for users and ensures DNS reliability. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand how Anycast works 
  * Learn how Anycast makes DNS resolving faster and more efficient 
  * Explain why Anycast helps mitigate DNS flood DDoS attacks 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)

On this page

  * What is Anycast DNS?

  * What is Anycast?

  * How does Anycast DNS work?

  * How does DNS resolving work without Anycast?

  * How does Anycast DNS provide resilience against DDoS attacks?




## What is Anycast DNS?

In Anycast, one IP address can apply to many servers. Anycast DNS means that any one of a number of [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) servers can respond to DNS queries, and typically the one that is geographically closest will provide the response. This reduces [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/), improves uptime for the DNS resolving service, and provides protection against [DNS flood DDoS attacks](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/).

## What is Anycast?

Typically, any device or server that connects directly to the Internet will have a unique [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). Communication between network-connected devices is 1-to-1; each communication goes from one specific device to the targeted device on the other end of the communication. [Anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) networks, in contrast, allow multiple servers on the network to use the same IP address, or set of IP addresses. Communication with an Anycast network is 1-to-many.

![Anycast DNS](https://images.ctfassets.net/slt3lc6tev37/4RamH3Ez7CEQ4RpSd24Op7/caa741afc2b02e81f3b81dc39708b729/anycast-dns.svg)Anycast DNS

Ordinarily, an IP address functions like a street address: it specifies the one specific location where the message is going. But suppose a friend had multiple residences around the country. Imagine a letter addressed to one of her houses could go to any one of those other houses based on which one was closest to the sender, even though the letter was addressed to a house in another city. This is sort of how Anycast routing works: one IP address can be associated with multiple locations.

For example, a request to an IP address within the [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) can be responded to by any data center Cloudflare operates, instead of one specific server. For more on Anycast and how a CDN can use it, see "[What is Anycast?](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)"

## How does Anycast DNS work?

DNS stands for domain name system, and it's the system that translates [domain names](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) (the names of websites) into alphanumeric IP addresses that machines can read. This is known as "resolving" a domain name, and DNS resolvers are the servers that manage the resolving. When a user wants to load a website, the client device needs to query a DNS resolver for the IP address of that website.

Anycast makes DNS resolving much faster. With Anycast DNS, a DNS query will go to a network of DNS resolvers rather than to one specific resolver, and will be routed to whichever resolver is closest and available. DNS queries and responses will follow optimized paths in order to answer queries as quickly as possible.

Anycast also helps keep DNS resolving services highly available. If one DNS resolver goes offline, queries can still be answered by other resolvers in the network.

Cloudflare offers DNS resolving on our distributed CDN with data centers in 335+ cities. Because the CDN is Anycast, DNS queries can be resolved from any data center in the network. Any DNS resolver in the network can respond to any DNS query.

## How does DNS resolving work without Anycast?

If a DNS resolving service does not use Anycast, it likely uses unicast routing. In unicast routing, every [DNS server](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/) has one IP address, and every DNS query goes to a specific server. If that resolver is down or unavailable, the client will have to query additional DNS resolvers, adding time to the DNS resolving process.

## How does Anycast DNS provide resilience against DDoS attacks?

[DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) can target DNS resolvers via [DNS flood attacks](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/). These attacks usually use large botnets of IoT devices to overwhelm or "flood" DNS resolvers with DNS queries. (A DNS flood attack is different from a [DNS amplification attack](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/), which uses open DNS resolvers to amplify DDoS attacks. In such an attack, the resolvers themselves are not the target.)

![Anycast vs Unicast](https://www.cloudflare.com/img/learning/cdn/glossary/anycast/anycast-unicast-botnet-attack.png)Anycast vs Unicast

Anycast networks provide [DDoS protection](https://www.cloudflare.com/ddos/) because traffic can be spread across the whole network. To put it another way, a request to one IP address can be answered by many servers, so thousands of requests that would overwhelm one server are divided up among many servers. Anycast DNS is therefore not susceptible to most DNS flood attacks, and [Cloudflare DNS](https://www.cloudflare.com/dns/) services are resilient to DDoS attacks for this reason.
