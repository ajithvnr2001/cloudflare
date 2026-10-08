---
url: https://www.cloudflare.com/learning/dns/dns-records/
title: DNS records | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:06.746445+00:00
---

# DNS records | Learning Center

> Source: https://www.cloudflare.com/learning/dns/dns-records/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  DNS records 

DNS records are instructions that live in authoritative DNS servers providing information about a domain including its IP address. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain what a DNS record is 
  * Identify common DNS record types (A, AAAA, CNAME, MX, TXT) 
  * Understand when to use each record type 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)[ DNS server types ](https://www.cloudflare.com/learning/dns/dns-server-types/)

On this page

  * What is a DNS record?

  * What are the most common types of DNS record?

  * What are some of the less commonly used DNS records?




## What is a DNS record?

[DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) records (aka zone files) are instructions that live in authoritative [DNS servers](https://www.cloudflare.com/learning/dns/dns-server-types/) and provide information about a domain including what [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) is associated with that domain and how to handle requests for that domain. These records consist of a series of text files written in what is known as DNS syntax. DNS syntax is just a string of characters used as commands that tell the DNS server what to do. All DNS records also have a ‘[TTL](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)’, which stands for time-to-live, and indicates how often a DNS server will refresh that record.

You can think of a set of DNS records like a business listing on Yelp. That listing will give you a bunch of useful information about a business such as their location, hours, services offered, etc. All domains are required to have at least a few essential DNS records for a user to be able to access their website using a [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/), and there are several optional records that serve additional purposes.

Report

2024 IDC Marketscape for Edge Delivery Services

[Get the report](https://www.cloudflare.com/lp/idc-marketscape-for-worldwide-commercial-edge-delivery-services-2024/)

## What are the most common types of DNS record?

  * **A record** \- The record that holds the IP address of a domain. [Learn more about the A record.](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)
  * **AAAA record** \- The record that contains the IPv6 address for a domain (as opposed to A records, which list the IPv4 address). [Learn more about the AAAA record.](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)
  * **CNAME record** \- Forwards one domain or subdomain to another domain, does NOT provide an IP address. [Learn more about the CNAME record.](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)
  * **MX record** \- Directs mail to an email server. [Learn more about the MX record.](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)
  * **TXT record** \- Lets an admin store text notes in the record. These records are often used for email security. [Learn more about the TXT record.](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)
  * **NS record** \- Stores the name server for a DNS entry. [Learn more about the NS record.](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)
  * **SOA record** \- Stores admin information about a domain. [Learn more about the SOA record.](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)
  * **SRV record** \- Specifies a port for specific services. [Learn more about the SRV record.](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)
  * **PTR record** \- Provides a domain name in reverse-lookups. [Learn more about the PTR record.](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)



Sign Up

Free DNS included with any Cloudflare plan

[Start for free](https://www.cloudflare.com/lp/pg-all-plans-dns/)

## What are some of the less commonly used DNS records?

  * **AFSDB record** \- This record is used for clients of the Andrew File System (AFS) developed by Carnegie Melon. The AFSDB record functions to find other AFS cells.
  * **APL record** \- The ‘address prefix list’ is an experiment record that specifies lists of address ranges.
  * **CAA record** \- This is the ‘certification authority authorization’ record, it allows domain owners state which certificate authorities can issue certificates for that domain. If no CAA record exists, then anyone can issue a certificate for the domain. These records are also inherited by subdomains.
  * **DNSKEY record** \- The ‘[DNS Key Record](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)’ contains a [public key](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) used to verify [Domain Name System Security Extension (DNSSEC)](https://www.cloudflare.com/learning/dns/dns-security/) signatures.
  * **CDNSKEY record** \- This is a child copy of the DNSKEY record, meant to be transferred to a parent.
  * **CERT record** \- The ‘certificate record’ stores public key certificates.
  * **DCHID record** \- The ‘DHCP Identifier’ stores info for the Dynamic Host Configuration Protocol (DHCP), a standardized network protocol used on IP networks.
  * **DNAME record** \- The ‘delegation name’ record creates a domain alias, just like CNAME, but this alias will redirect all subdomains as well. For instance if the owner of ‘example.com’ bought the domain ‘website.net’ and gave it a DNAME record that points to ‘example.com’, then that pointer would also extend to ‘blog.website.net’ and any other subdomains.
  * **HIP record** \- This record uses ‘Host identity protocol’, a way to separate the roles of an IP address; this record is used most often in mobile computing.
  * **IPSECKEY record** \- The ‘IPSEC key’ record works with the [Internet Protocol Security (IPSEC)](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/), an end-to-end security protocol framework and part of the Internet Protocol Suite [(TCP/IP)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/).
  * **LOC record** \- The ‘location’ record contains geographical information for a domain in the form of longitude and latitude coordinates.
  * **NAPTR record** \- The ‘name authority pointer’ record can be combined with an [SRV record](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/) to dynamically create URI’s to point to based on a regular expression.
  * **NSEC record** \- The ‘next secure record’ is part of DNSSEC, and it’s used to prove that a requested DNS resource record does not exist.
  * **RRSIG record** \- The ‘resource record signature’ is a record to store digital signatures used to authenticate records in accordance with DNSSEC.
  * **RP record** \- This is the ‘responsible person’ record and it stores the email address of the person responsible for the domain.
  * **SSHFP record** \- This record stores the ‘SSH public key fingerprints’; SSH stands for Secure Shell and it’s a cryptographic networking protocol for secure communication over an unsecure network.



Cloudflare DNS is an authoritative DNS service that offers the fastest response time and advanced security. Cloudflare DNS supports a wide variety of DNS records, plus additional services like easy [DMARC](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/), [DKIM](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/), and [SPF](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) configuration. Cloudflare also offers [1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/), a free DNS resolver that is fast and private. Learn about Cloudflare's [authoritative DNS service](https://www.cloudflare.com/dns/), or about [managing DNS records in Cloudflare](https://support.cloudflare.com/hc/en-us/articles/360019093151-Managing-DNS-records-in-Cloudflare).
