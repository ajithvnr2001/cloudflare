---
url: https://www.cloudflare.com/learning/dns/dns-server-types/
title: DNS server types | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:21:23.151249+00:00
---

# DNS server types | Learning Center

> Source: https://www.cloudflare.com/learning/dns/dns-server-types/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  DNS server types 

Learn about the different types of DNS servers including recursive resolvers, root nameservers, TLD nameservers, and authoritative nameservers. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Differentiate between DNS server types 
  * Understand the role of each server in DNS resolution 
  * Explain what a recursive resolver does 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)[ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)

On this page

  * What are the different types of DNS server?

  * What is a DNS recursive resolver?

  * What is a DNS root nameserver?

  * What is a TLD nameserver?

  * What is an authoritative nameserver?




## What are the different types of DNS server?

All DNS servers fall into one of four categories: Recursive resolvers, [root nameservers](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/), TLD nameservers, and authoritative nameservers. In a typical DNS lookup (when there is no [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) in play), these four DNS servers work together in harmony to complete the task of delivering the [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) for a specified [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) to the client (the client is usually a stub resolver - a simple resolver built into an operating system).

## What is a DNS recursive resolver?

![DNS recursive resolver](https://www.cloudflare.com/img/learning/dns/dns-server-types/recursive-resolver.png)

A recursive resolver (also known as a DNS recursor) is the first stop in a DNS query. The recursive resolver acts as a middleman between a client and a DNS nameserver. After receiving a DNS query from a web client, a recursive resolver will either respond with cached data, or send a request to a root nameserver, followed by another request to a TLD nameserver, and then one last request to an authoritative nameserver. After receiving a response from the authoritative nameserver containing the requested IP address, the recursive resolver then sends a response to the client.

During this process, the recursive resolver will cache information received from authoritative nameservers. When a client requests the IP address of a domain name that was recently requested by another client, the resolver can circumvent the process of communicating with the nameservers, and just deliver the client the requested record from its cache.

Most Internet users use a recursive resolver provided by their ISP, but there are other options available; for example [Cloudflare's 1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/).

## What is a DNS root nameserver?

![DNS root nameserver](https://www.cloudflare.com/img/learning/dns/dns-server-types/root-nameserver.png)

The 13 DNS root nameservers are known to every recursive resolver, and they are the first stop in a recursive resolver’s quest for DNS records. A root server accepts a recursive resolver’s query which includes a domain name, and the root nameserver responds by directing the recursive resolver to a TLD nameserver, based on the extension of that domain (.com, .net, .org, etc.). The root nameservers are overseen by a nonprofit called the Internet Corporation for Assigned Names and Numbers (ICANN).

Note that while there are 13 root nameservers, that does not mean that there are only 13 machines in the root nameserver system. There are 13 types of root nameservers, but there are multiple copies of each one all over the world, which use [Anycast routing](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) to provide speedy responses. If you added up all the instances of root nameservers, you’d have over 600 different servers.

## What is a TLD nameserver?

![DNS TLD nameserver](https://www.cloudflare.com/img/learning/dns/dns-server-types/tld-nameserver.png)

A TLD nameserver maintains information for all the domain names that share a common domain extension, such as .com, .net, or whatever comes after the last dot in a URL. For example, a .com TLD nameserver contains information for every website that ends in ‘.com’. If a user was searching for google.com, after receiving a response from a root nameserver, the recursive resolver would then send a query to a .com TLD nameserver, which would respond by pointing to the authoritative nameserver (see below) for that domain.

Management of TLD nameservers is handled by the Internet Assigned Numbers Authority (IANA), which is a branch of ICANN. The IANA breaks up the TLD servers into two main groups:

  * Generic top-level domains: These are domains that are not country specific, some of the best-known generic TLDs include .com, [.org](https://www.cloudflare.com/application-services/products/registrar/buy-org-domains/), .net, .edu, and .gov.
  * Country code top-level domains: These include any domains that are specific to a country or state. Examples include .uk, .us, .ru, and .jp.



There is actually a third category for infrastructure domains, but it is almost never used. This category was created for the .arpa domain, which was a transitional domain used in the creation of modern DNS; its significance today is mostly historical.

## What is an authoritative nameserver?

![DNS authoritative nameserver](https://www.cloudflare.com/img/learning/dns/dns-server-types/authoritative-nameserver.png)

When a recursive resolver receives a response from a TLD nameserver, that response will direct the resolver to an authoritative nameserver. The authoritative nameserver is usually the resolver’s last step in the journey for an IP address. The authoritative nameserver contains information specific to the domain name it serves (e.g. google.com) and it can provide a recursive resolver with the IP address of that server found in the [DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/), or if the domain has a [CNAME record](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/) (alias) it will provide the recursive resolver with an alias domain, at which point the recursive resolver will have to perform a whole new DNS lookup to procure a record from an authoritative nameserver (often an A record containing an IP address). [Cloudflare DNS](https://www.cloudflare.com/dns/) distributes authoritative nameservers, which come with Anycast routing to make them more reliable.
