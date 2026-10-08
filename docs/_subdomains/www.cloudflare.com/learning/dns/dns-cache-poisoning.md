---
url: https://www.cloudflare.com/learning/dns/dns-cache-poisoning/
title: What is DNS cache poisoning? | DNS spoofing
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:06.156456+00:00
---

# What is DNS cache poisoning? | DNS spoofing

> Source: https://www.cloudflare.com/learning/dns/dns-cache-poisoning/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is DNS cache poisoning? | DNS spoofing 

Attackers can poison a DNS cache by tricking DNS resolvers into caching false information, with the result that the resolver sends the wrong IP address to clients, and users attempting to navigate to a website will be directed to the wrong place. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define DNS cache poisonings 
  * Understand how DNS caching works 
  * Explain how attackers can poison a DNS cache 
  * Understand how DNSSEC helps prevent DNS poisoning attacks 



Related content  [ DNS security ](https://www.cloudflare.com/learning/dns/dns-security/)[ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)

On this page

  * What is DNS cache poisoning?

  * What do DNS resolvers do?

  * How does DNS caching work?

  * How do attackers poison DNS caches?

  * DNS spoofing and censorship

  * How will DNSSEC help prevent DNS poisoning?




## What is DNS cache poisoning?

[DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) cache poisoning is the act of entering false information into a DNS cache, so that DNS queries return an incorrect response and users are directed to the wrong websites. DNS cache poisoning is also known as 'DNS spoofing.' [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) are the 'phone numbers' of the Internet, enabling web traffic to arrive in the right places. DNS resolver caches are like a directory that lists these phone numbers, and when they store faulty information, traffic goes to the wrong places until the [cached](https://www.cloudflare.com/learning/cdn/what-is-caching/) information is corrected. (Note that this does not actually disconnect the real websites from their real IP addresses.)

Because there is typically no way for DNS resolvers to verify the data in their caches, incorrect DNS information remains in the cache until the [time to live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/) expires, or until it is removed manually. A number of vulnerabilities make DNS poisoning possible, but the chief problem is that DNS was built for a much smaller Internet and based on a principle of trust (much like [BGP](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/)). A more secure DNS protocol called [DNSSEC](https://www.cloudflare.com/learning/dns/dns-security/) aims to solve some of these problems, but it has not been widely adopted yet.

## What do DNS resolvers do?

DNS resolvers provide clients with the IP address that is associated with a [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/). In other words, they take human-readable website addresses like 'cloudflare.com' and translate them into machine-readable IP addresses. When a user attempts to navigate to a website, their operating system sends a request to a DNS resolver. The DNS resolver responds with the IP address, and the web browser takes this address and initiates loading the website.

## How does DNS caching work?

A DNS resolver will save responses to IP address queries for a certain amount of time. In this way, the resolver can respond to future queries much more quickly, without needing to communicate with the many servers involved in the typical DNS resolution process. DNS resolvers save responses in their cache for as long as the designated [time to live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/) associated with that IP address allows them to.

DNS Uncached Response:

![DNS uncached response](https://www.cloudflare.com/img/learning/dns/dns-cache-poisoning/dns-uncached-response.svg)DNS uncached response

DNS Cached Response:

![DNS cached response](https://www.cloudflare.com/img/learning/dns/dns-cache-poisoning/dns-cached-response.svg)DNS cached response

## How do attackers poison DNS caches?

Attackers can poison DNS caches by impersonating [DNS nameservers](https://www.cloudflare.com/learning/dns/dns-server-types/), making a request to a DNS resolver, and then forging the reply when the DNS resolver queries a nameserver. This is possible because DNS servers use [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) instead of [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/), and because currently there is no verification for DNS information.

DNS Cache Poisoning Process:

![DNS Cache Poisoning Process](https://www.cloudflare.com/img/learning/dns/dns-cache-poisoning/dns-cache-poisoning-attack.svg)DNS Cache Poisoning Process

Poisoned DNS Cache:

![Poisoned DNS Cache](https://www.cloudflare.com/img/learning/dns/dns-cache-poisoning/dns-cache-poisoned.svg)Poisoned DNS Cache

Instead of using TCP, which requires both communicating parties to perform a 'handshake' to initiate communication, DNS requests and responses use UDP, or the User Datagram Protocol. With UDP, there is no guarantee that a connection is open or that the recipient is ready to receive. UDP is vulnerable to forging for this reason – an attacker can send a message via UDP and pretend it is a response from a legitimate server by forging the header data.

If a DNS resolver receives a forged response, it accepts and caches the data uncritically because there is no way to verify if the information is accurate and comes from a legitimate source. DNS was created in the early days of the Internet, when the only parties connected to it were universities and research centers. There was no reason to expect that anyone would try to spread fake DNS information.

Despite these major points of vulnerability in the DNS caching process, DNS poisoning attacks are not easy. Because the DNS resolver does actually query the authoritative nameserver, attackers have only a few milliseconds to send the fake reply before the real reply from the authoritative nameserver arrives.

Attackers also have to either know or guess a number of factors to carry out DNS spoofing attacks:

  * Which DNS queries are not cached by the targeted DNS resolver, so that the resolver will query the authoritative nameserver

  * What [port*](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) the DNS resolver is using – they used to use the same port for every query, but now they use a different, random port each time

  * The request ID number

  * Which authoritative nameserver the query will go to




Attackers could also gain access to the DNS resolver in some other way. If a malicious party operates, hacks, or gains physical access to a DNS resolver, they can more easily alter cached data.

*_In networking, a port is a virtual point of communication reception. Computers have multiple ports, each with their own number, and for computers to talk to each other, certain ports have to be designated for certain kinds of communication. For instance,[HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) communications always go to port 80, and [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/) always uses port 443_.

## DNS spoofing and censorship

Several governments have intentionally poisoned DNS caches within their countries in order to deny access to certain websites or web resources.

## How will DNSSEC help prevent DNS poisoning?

DNSSEC is short for Domain Name System Security Extensions, and it is a means of verifying DNS data integrity and origin. DNS was originally designed with no such verification, which is why DNS poisoning is possible.

Much like [TLS/SSL](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), DNSSEC uses [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) (a way of digitally signing information) to verify and authenticate data. DNSSEC extensions were published in 2005, but DNSSEC is not yet mainstream, leaving DNS still vulnerable to attacks.
