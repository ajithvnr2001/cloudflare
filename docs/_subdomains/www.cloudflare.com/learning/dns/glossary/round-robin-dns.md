---
url: https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/
title: What Is Round-Robin DNS?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:16.876960+00:00
---

# What Is Round-Robin DNS?

> Source: https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is round-robin DNS? 

Round-robin DNS is a load balancing technique that involves using several different IP addresses for a single domain name. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe round-robin DNS 
  * Outline the pros and cons of using round-robin DNS for load balancing 



Related content  [ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)[ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)

On this page

  * What is round-robin DNS?

  * What are the drawbacks of Round-Robin DNS?




## What is round-robin DNS?

Round-robin [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) is a load balancing technique where the balancing is done by a type of DNS server called an [authoritative nameserver](https://www.cloudflare.com/learning/dns/dns-server-types/), rather than using a dedicated piece of load-balancing hardware. Round-robin DNS can be used when a website or service has their content hosted on several redundant web servers; when the DNS authoritative nameserver is queried for an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), the server hands out a different address each time, operating on a rotation. This is particularly useful when the redundant web servers are geographically separated, making traditional load-balancing difficult. Round-robin is known for it’s ease of implementation, but it also has strong drawbacks.

A DNS server with round-robin enabled will have multiple different [A records](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/), each with the same domain name but a different IP address. Each time the DNS server is queried, it sends the IP address to which it most recently responded with to the back of the queue, operating on a loop. The IP addresses in a round-robin DNS server are like baseball players in a batting lineup: each one gets a turn and then is moved to the back of the line.

## What are the drawbacks of Round-Robin DNS?

The round-robin method doesn’t always provide evenly-distributed load balancing because of both DNS [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) and [client-side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/) caching. If a user makes a DNS query to a particularly high traffic [recursive resolver](https://www.cloudflare.com/learning/dns/dns-server-types/) for a particular website, that resolver will cache the website’s IP, potentially sending a heavy amount of traffic to that one IP.

Another drawback is that round-robin cannot be depended upon for site reliability; if one of the servers goes down, the DNS server will still keep that server’s IP in the round-robin rotation. So if there are 6 servers and one is taken offline, one in six users will be denied service. In addition, round-robin DNS does not account for server load, transaction time, geographical distance, and other factors that traditional load balancing can be configured for.

Some advanced round-robin services have methods to overcome a few of the drawbacks, such as the ability to detect unresponsive servers and take them out of the round-robin rotation, but there is no way around the caching issue. Many DNS providers, like [Cloudflare DNS](https://www.cloudflare.com/dns/) support round-robin DNS.
