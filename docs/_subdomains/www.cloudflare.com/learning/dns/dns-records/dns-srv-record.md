---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/
title: What is a DNS SRV record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:08.311072+00:00
---

# What is a DNS SRV record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS SRV record? 

The SRV record is used for special services like VoIP. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the purpose of an SRV record. 
  * Learn what information goes in an SRV record 
  * Understand ports 



On this page

  * What is a DNS SRV record?

  * What is a port?

  * What goes in an SRV record?

  * What is the difference between priority and weight in SRV records?




## What is a DNS SRV record?

The [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/) "service" (SRV) record specifies a host and port for specific services such as [voice over IP (VoIP)](https://www.cloudflare.com/learning/video/what-is-voip/), instant messaging, and so on. Most other [DNS records](https://www.cloudflare.com/learning/dns/dns-records/) only specify a server or an [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/), but SRV records include a port at that IP address as well. Some [Internet protocols](https://www.cloudflare.com/learning/network-layer/internet-protocol/) require the use of SRV records in order to function.

## What is a port?

In networking, [ports](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) are virtual places that designate what processes network traffic goes to within a computer. Ports allow computers to easily differentiate between different kinds of traffic: VoIP streams go to a different port than email messages, for instance, even though both reach a computer over the same Internet connection. Much like IP addresses, all ports are assigned a number.

Certain Internet protocols, such as IMAP, SIP, and XMPP, need to connect to a specific port in addition to connecting with a specific server. SRV records are how a port can be specified within the DNS.

## What goes in an SRV record?

An SRV record contains the following information. Here, we list example values for each field.

service XMPP

proto* TCP

name** example.com

TTL 86400

class IN

type SRV

priority 10

weight 5

port 5223

target server.example.com

**Short for "protocol," as in transport protocol.

**[Domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/).*

However, SRV records are actually formatted in this way:
    
    
    `_service._proto.name. TTL class type of record priority weight port target.`
    

So our example SRV record would actually look like:
    
    
    `_xmpp._tcp.example.com. 86400 IN SRV 10 5 5223 server.example.com.`
    

In the above example, "_xmpp" indicates the type of service (the XMPP protocol) and "_tcp" indicates the [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) transport protocol, while "example.com" is the host, or the domain name. "Server.example.com" is the target server and "5223" indicates the port within that server.

SRV records must point to an [A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/) (in IPv4) or an [AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/) (in IPv6). The server name they list cannot be a [CNAME](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/). So "server.example.com" must lead directly to an A or AAAA record under that name.

## What is the difference between priority and weight in SRV records?

SRV records indicate the "priority" and "weight" of the various servers they list. The "priority" value in an SRV record enables administrators to prioritize one server that supports the given service over another. A server with a lower priority value will receive more traffic than other servers. However, the "weight" value is similar: a server with a higher weight will receive more traffic than other servers with the same priority.

The main difference between them is that priority is looked at first. If there are three servers, Server A, Server B, and Server C, and they have respective priorities of 10, 20, and 30, then their "weight" does not matter. The service will always query Server A first.

But suppose Servers A, B, and C all have a priority of 10 — how will a service choose between them? This is where weight becomes a factor: if Server A has a "weight" value of 5 and Servers B and C have a "weight" value of 3 and 2, Server A will receive the most traffic, Server B will receive the second-most traffic, and Server C the third-most.
