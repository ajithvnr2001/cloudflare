---
url: https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/
title: Dynamic DNS
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:12.957281+00:00
---

# Dynamic DNS

> Source: https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  Dynamic DNS 

Dynamic DNS can help ensure that DNS queries work even if the web service being sought has recently switched IP addresses. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define dynamic DNS 
  * Understand why there is a need for dynamic DNS 



Related content  [ DNS security ](https://www.cloudflare.com/learning/dns/dns-security/)

On this page

  * What is dynamic DNS?

  * Why do some IP addresses change?

  * How does dynamic DNS work?

  * How to set up dynamic DNS in Cloudflare

  * FAQs

    * What is dynamic DNS?

    * How does the DDNS process work?

    * Why do IP addresses change for some users?

    * Who typically needs a dynamic DNS solution?

    * What happens to a website if its IP address changes without DDNS?




## What is dynamic DNS (DDNS)?

Many web properties, such as [APIs](https://www.cloudflare.com/learning/security/api/what-is-an-api/) or websites, run on internet connections that have their [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) changed frequently; this creates a problem if the operators of those properties want to give a hosted resource a specific domain name, which must then store an IP address in [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) records. Dynamic DNS (DDNS) is a service that keeps the DNS updated with a web property's correct IP address, even if that IP address is constantly being updated.

For example, if a web administrator is operating a small website with a domain name of [www.example.com](http://www.example.com) and an IP address of 192.0.2.0, anytime another user enters [www.example.com](http://www.example.com) into their browser, the DNS will direct them to the server at 192.0.2.0. If the admin's ISP dynamically changes the IP to 192.0.2.1, a dynamic DNS service can automatically update the admin's DNS records so that other users trying to visit [www.example.com](http://www.example.com) will now go to the correct IP address.

Report

2024 IDC Marketscape for Edge Delivery Services

[Get the report →](https://www.cloudflare.com/lp/idc-marketscape-for-worldwide-commercial-edge-delivery-services-2024/)

## Why do some IP addresses change?

In the early days of the Internet, IP addresses rarely changed, which made management of domains a lot simpler. But the rapid growth of the web and home computers with Internet access created a shortage of available IP addresses. This led to the Dynamic Host Configuration Protocol (DHCP), which lets ISPs assign IPs to their users dynamically. ISPs will typically maintain a shared pool of IP addresses and assign or 'lease' them to users as needed, for the duration of their connection or until a maximum amount of time has been reached. Although the introduction of IPV6 alleviated the IP address shortage, ISPs still often use DHCP because it is more cost-efficient than providing static IPs.

Large enterprises that run major web services require their ISPs to give them unchanging or 'static' IP addresses so they can operate using standard DNS practices. In contrast, smaller services tend to see their IP addresses changed by their ISPs quite frequently, so they require a dynamic DNS solution to keep their DNS records up to date. These smaller services can include [small business websites](https://www.cloudflare.com/small-business/), [personal websites](https://www.cloudflare.com/personal/), DVRs, and security cameras.

Sign Up

Free DNS included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/lp/pg-all-plans-dns/)

## How does dynamic DNS work?

There are a number of companies who offer dynamic DNS services with varying features and technologies. One very common method of enabling dynamic DNS is by providing users with software which runs on their computer or [router](https://www.cloudflare.com/learning/network-layer/what-is-a-router/). This software communicates with the dynamic DNS service provider anytime the IP addresses provided by the ISP is updated, and the dynamic DNS provider in turn updates the DNS with those changes, providing almost instant updates.

## How to set up dynamic DNS in Cloudflare

For help setting up dynamic DNS in Cloudflare, refer to [Dynamically update DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/).

## FAQs

#### What is dynamic DNS (DDNS)?

Dynamic DNS is a service that ensures DNS records stay current with a web property's correct IP address, even when that address changes frequently. This is particularly useful for websites or APIs that use service providers that update their IP addresses constantly.

#### How does the DDNS process work?

Many DDNS providers use software that runs on a router or computer to monitor the connection. Whenever the Internet Service Provider (ISP) updates the IP address, this software notifies the DDNS provider, which then updates the DNS records almost instantly to reflect the change.

#### Why do IP addresses change for some users?

Most ISPs use the Dynamic Host Configuration Protocol (DHCP) to assign IP addresses from a shared pool, leasing them to users for a set time or for the duration of a connection. This practice addresses the shortage of available IPv4 addresses and remains common today because it is more cost-efficient for ISPs than providing static IPv6 addresses.

#### Who typically needs a dynamic DNS solution?

While large enterprises often pay for unchanging static IP addresses, smaller services usually receive frequently changing addresses from their ISPs. DDNS is ideal for small business websites, personal sites, DVRs, and security cameras that need to remain accessible under a consistent domain name.

#### What happens to a website if its IP address changes without DDNS?

Without DDNS, the DNS would continue to direct visitors to the old, inactive IP address. For example, if a site moves from 192.0.2.0 to 192.0.2.1, anyone typing in the domain name would fail to reach the server until the DNS record is manually updated.
