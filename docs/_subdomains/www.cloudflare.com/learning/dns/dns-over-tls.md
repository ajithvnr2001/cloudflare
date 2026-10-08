---
url: https://www.cloudflare.com/learning/dns/dns-over-tls/
title: DNS over TLS vs. DNS over HTTPS | Secure DNS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:21:27.280458+00:00
---

# DNS over TLS vs. DNS over HTTPS | Secure DNS

> Source: https://www.cloudflare.com/learning/dns/dns-over-tls/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  DNS over TLS vs. DNS over HTTPS | Secure DNS 

DNS queries are sent in plaintext, which means anyone can read them. DNS over HTTPS and DNS over TLS encrypt DNS queries and responses to keep user browsing secure and private. However, both approaches have their pros and cons. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand why DNS needs greater security, and why DNS privacy is important 
  * Learn how DNS over TLS and DNS over HTTPS work, and the differences between them 
  * Explain the pros and cons of both approaches 
  * Compare DNS over TLS/HTTPS to DNSSEC 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)[ DNS security ](https://www.cloudflare.com/learning/dns/dns-security/)[ What is DNS cache poisoning? | DNS spoofing ](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[ DNS server types ](https://www.cloudflare.com/learning/dns/dns-server-types/)

On this page

  * Why does DNS need additional layers of security?

  * What is DNS over TLS?

  * What is DNS over HTTPS?

  * Wait, doesn&#39

  * What is a port?

  * Which is better, DoT or DoH?

  * What is the difference between DNS over TLS/HTTPS and DNSSEC?




## Why does DNS need additional layers of security?

[DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) is the phonebook of the Internet; DNS resolvers translate human-readable domain names into machine-readable [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). By default, DNS queries and responses are sent in plaintext (via [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)), which means they can be read by networks, ISPs, or anybody able to monitor transmissions. Even if a website uses [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/), the DNS query required to navigate to that website is exposed.

This lack of [privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) has a huge impact on security and, in some cases, human rights; if DNS queries are not private, then it becomes easier for governments to censor the Internet and for attackers to stalk users' online behavior.

![Attacker views unsecured DNS traffic](https://images.ctfassets.net/slt3lc6tev37/5Cgzkxb8COyIZ9evqqGFyF/384df7ee28643474080bbcd564fc3cfa/dns-traffic-unsecured.svg)Attacker views unsecured DNS traffic

Think of a normal, unencrypted DNS query as being like a postcard sent through the mail: anyone handling the mail may happen to catch a glimpse of the text written on the back side, so it is not wise to mail a postcard that contains sensitive or private information.

DNS over [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) and DNS over HTTPS are two standards developed for encrypting plaintext DNS traffic in order to prevent malicious parties, advertisers, ISPs, and others from being able to interpret the data. Continuing the analogy, these standards aim to put an envelope around all postcards going through the mail, so that anyone can send a postcard without worrying that someone is snooping on what they are up to.

![DNS queries secured over TLS or HTTPS, attacker blocked](https://images.ctfassets.net/slt3lc6tev37/7qcyOJwWyOt4EVJykiIRTn/30e34453409eb42fa1ec36680609ad8d/dns-traffic-over-tls-https.svg)DNS queries secured over TLS or HTTPS, attacker blocked

## What is DNS over TLS?

DNS over TLS, or DoT, is a standard for encrypting DNS queries to keep them secure and private. DoT uses the same security protocol, TLS, that HTTPS websites use to encrypt and authenticate communications. (TLS is also known as "[SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/).") DoT adds TLS encryption on top of the user datagram protocol (UDP), which is used for DNS queries. Additionally, it ensures that DNS requests and responses are not tampered with or forged via [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/).

## What is DNS over HTTPS?

DNS over HTTPS, or DoH, is an alternative to DoT. With DoH, DNS queries and responses are encrypted, but they are sent via the [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) or [HTTP/2](https://www.cloudflare.com/learning/performance/http2-vs-http1.1/) protocols instead of directly over UDP. Like DoT, DoH ensures that attackers can't forge or alter DNS traffic. DoH traffic looks like other HTTPS traffic – e.g. normal user-driven interactions with websites and web apps – from a network administrator's perspective.

In February 2020, the Mozilla Firefox browser began enabling DoH for U.S. users by default. DNS queries from the Firefox browser are encrypted by DoH and go to either Cloudflare or NextDNS. Several other browsers also support DoH, although it is not turned on by default.

## Wait, doesn't HTTPS use TLS for encryption too? How are DNS over TLS and DNS over HTTPS different?

Each standard was developed separately and has its own RFC* documentation, but the most important difference between DoT and DoH is what [port](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) they use. DoT only uses port 853, while DoH uses port 443, which is the port that all other HTTPS traffic uses as well.

Because DoT has a dedicated port, anyone with network visibility can see DoT traffic coming and going, even though the requests and responses themselves are encrypted. In contrast, with DoH, DNS queries and responses are camouflaged within other HTTPS traffic, since it all comes and goes from the same port.

*_RFC stands for "Request for Comments", and an RFC is a collective attempt by developers, networking experts, and thought leaders to standardize an Internet technology or[protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/)._

## What is a port?

In networking, a port is a virtual place on a machine that is open to connections from other machines. Every networked computer has a standard number of ports, and each port is reserved for certain types of communication.

Think of ports for ships in a harbor: each shipping port is numbered, and different kinds of ships are supposed to go to specific shipping ports to unload cargo or passengers. Networking is the same way: certain types of communications are supposed to go to certain network ports. The difference is that the network ports are virtual; they are places for digital connections rather than physical connections.

## Which is better, DoT or DoH?

This is up for debate. From a [network security standpoint](https://www.cloudflare.com/the-net/future-of-networking/), DoT is arguably better. It gives network administrators the ability to monitor and block DNS queries, which is important for identifying and stopping malicious traffic. DoH queries, meanwhile, are hidden in regular HTTPS traffic, meaning they cannot easily be blocked without blocking all other HTTPS traffic as well.

However, from a privacy perspective, DoH is arguably preferable. With DoH, DNS queries are hidden within the larger flow of HTTPS traffic. This gives network administrators less visibility but provides users with more privacy.

[1.1.1.1, the free DNS resolver from Cloudflare](https://one.one.one.one/), supports both DoT and DoH.

## What is the difference between DNS over TLS/HTTPS and DNSSEC?

[DNSSEC](https://www.cloudflare.com/learning/dns/dns-security/) is a set of security extensions for verifying the identity of [DNS root servers](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/) and authoritative nameservers in communications with [DNS resolvers](https://www.cloudflare.com/learning/dns/dns-server-types/). It is designed to prevent [DNS cache poisoning](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/), among other attacks. It does not encrypt communications. DNS over TLS or HTTPS, on the other hand, does encrypt DNS queries. 1.1.1.1 supports [DNSSEC](https://www.cloudflare.com/dns/dnssec/how-dnssec-works/) as well.

To learn more about 1.1.1.1, see [What is 1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/)?
