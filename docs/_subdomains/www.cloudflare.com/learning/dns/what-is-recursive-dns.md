---
url: https://www.cloudflare.com/learning/dns/what-is-recursive-dns/
title: What Is Recursive DNS?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:10.748791+00:00
---

# What Is Recursive DNS?

> Source: https://www.cloudflare.com/learning/dns/what-is-recursive-dns/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is recursive DNS? 

In DNS lookups, which match domain names to machine-readable IP addresses, the journey up the DNS tree can either be made by a DNS server or a client. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define recursive DNS 
  * Differentiate between a recursive and an iterative DNS query 
  * Understand the advantages and risks associated with recursive DNS queries 



Related content  [ DNS security ](https://www.cloudflare.com/learning/dns/dns-security/)[ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)[ What is a DNS server? ](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)

On this page

  * What is recursive DNS?

  * What is a DNS server?

  * What is the difference between recursion and iteration?

  * What are the advantages of recursive DNS?

  * What are the disadvantages of recursive DNS?

    * Recursive DNS servers and DNS amplification attacks

    * Recursive DNS servers and DNS cache poisoning attacks

  * How to support DNS queries that are both fast and secure




## What is recursive DNS?

A recursive [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) lookup is where one [DNS server](https://www.cloudflare.com/learning/dns/dns-server-types/) communicates with several other DNS servers to hunt down an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) and return it to the client. This is in contrast to an iterative DNS query, where the client communicates directly with each DNS server involved in the lookup. While this is a very technical definition, a closer look at the DNS system and the difference between recursion and iteration should help clear things up.

## What is a DNS server?

Whenever a user types a [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) (such as ‘cloudflare.com’) into their browser window, this triggers a DNS lookup. A series of remote computers known as DNS servers then find the IP address for that domain and return it to the user’s computer so that they can access the correct website.

Several different types of DNS servers must work in conjunction to complete a DNS lookup. A DNS resolver, DNS root server, DNS TLD server, and DNS authoritative nameserver must all provide information to complete the lookup. In the case of [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/), one of these servers may have saved the answer to a query during a previous lookup, and can then deliver it from memory.

For more on how a DNS lookup works, see [What is a DNS Server?](https://www.cloudflare.com/learning/dns/dns-server-types/)

## What is the difference between recursion and iteration?

Recursion and iteration are computer science terms that describe two different methods to solve a problem. In recursion, a program repeatedly calls itself until a condition is met, while in iteration, a set of instructions is repeated until a condition is met. This subtle difference is hard to illustrate without getting into code, but the key takeaway is that recursion is a solution that repeatedly calls upon itself.

For example, imagine that Jim lost his keys at home and is looking for a systematic way to find them. A recursive solution would be for Jim to keep looking for his keys until he finds them. Jim will start looking, and if he doesn’t find his keys, he will return to his original instruction to keep looking until he finds them. An iterative solution would be for Jim to to search one room for five minutes, then go back to his instructions and search the next room for five minutes, and continue this cycle until he either finds his keys or has gone through the entire list of rooms to search.

A deep understanding of recursion and iteration isn’t necessary to comprehend the difference between recursive and iterative DNS lookups: In a recursive lookup, a DNS server does the recursion and continues querying other DNS servers until it has an IP address to return to the client (often a user’s operating system). In an iterative DNS query, each DNS query responds directly to the client with an address for another DNS server to ask, and the client continues querying DNS servers until one of them responds with the correct IP address for the given domain.

Put another way, the client does a form of delegation in a recursive DNS query. It tells the DNS resolver, “Hey, I need the IP address for this domain, please hunt it down and don’t get back to me until you have it.” Meanwhile, in an iterative query, the client tells the DNS resolver, “Hey, I need the IP address for this domain. Please let me know the address of the next DNS server in the lookup process so I can look it up myself.”

## What are the advantages of recursive DNS?

Recursive DNS queries generally tend to resolve faster than iterative queries. This is due to caching. A recursive DNS server caches the final answer to every query it performs and saves that final answer for a certain amount of time (known as the [Time-To-Live](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)).

When a recursive resolver receives a query for an IP address it already has in its cache, it can rapidly provide the cached answer to the client without communicating with any other DNS servers. Quickly serving responses from the cache is very likely if a) the DNS server serves a lot of clients and/or b) the requested website is very popular.

## What are the disadvantages of recursive DNS?

Unfortunately, allowing recursive DNS queries on open DNS servers creates a security vulnerability, as this configuration can enable attackers to perform [DNS amplification attacks](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/) and [DNS cache poisoning](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/).

#### Recursive DNS servers and DNS amplification attacks

In a DNS amplification attack, an attacker typically uses a group of machines (known as a [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/)) to send a high volume of DNS queries using a [spoofed IP](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/) address. A spoofed IP address is like a forged return address; the attacker is sending requests from their own IP, but asking for the responses to go to the victim. In order to exacerbate the attack, the attacker also uses a technique called amplification, in which the spoofed request asks for a very long response. The victimized service will receive a flood of lengthy and unwanted DNS responses that can disrupt or even take down their servers. This is a type of [DDoS attack](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/).

This is kind of like a group of teenage pranksters calling a pizza place and each ordering a dozen pizzas. Instead of giving their own address for delivery, they give the address of an unsuspecting neighbor. The victim, who then receives a stream of large and unwanted pizza deliveries, will likely experience a lot of disruption in their day.

A DNS server that accepts recursive queries is needed to carry out this kind of attack, because the amplified DNS packets are responses to recursive DNS queries.

#### Recursive DNS servers and DNS cache poisoning attacks

In a DNS cache poisoning attack, when a recursive DNS server requests an IP address from another DNS server, an attacker intercepts the request and gives a fake response, which is often the IP address for a malicious website. Not only does the recursive DNS server send the original client this IP address, but the server will also save the response in its cache. Any user that requests an IP for the same domain name will be sent to the malicious website. If it’s a popular domain name and a popular DNS resolver, this attack could affect thousands of users.

In an iterative DNS query, the client directly asks each DNS server for the answer. Even if an attacker is able to send a forged response to the query, it will only affect a single client, which is generally not worth the attacker’s time.

## How to support DNS queries that are both fast and secure

[Cloudflare’s managed DNS](https://www.cloudflare.com/dns/) service generally resolves DNS queries faster than competitors' DNS or public DNS. Additionally, Cloudflare DNS supports DNSSEC, a stringent security protocol designed to keep DNS servers and queries safe.
