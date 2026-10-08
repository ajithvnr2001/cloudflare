---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/
title: What is a DNS MX record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:07.671732+00:00
---

# What is a DNS MX record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS MX record? 

The MX record directs emails to a mail exchange server. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the purpose of an MX record 
  * Learn how MX records fit into the process of sending an email 



On this page

  * What is a DNS MX record?

  * What is the process of querying an MX record?

  * What is a backup MX record?

  * Can MX records point to a CNAME?

  * How to set up MX records in Cloudflare




## What is a DNS MX record?

A DNS 'mail exchange' (MX) record directs email to a mail server. The MX record indicates how [email](https://www.cloudflare.com/learning/email-security/what-is-email/) messages should be routed in accordance with the Simple Mail Transfer Protocol ([SMTP](https://www.cloudflare.com/learning/email-security/what-is-smtp/), the standard protocol for all email).

Example of an MX record:

example.com record type: priority: value: TTL

@ MX 10 mailhost1.example.com 45000

@ MX 20 mailhost2.example.com 45000

The 'priority' numbers before the [domains](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) for these MX records indicate preference; the lower 'priority' value is preferred. The server will always try mailhost1 first because 10 is lower than 20. In the result of a message send failure, the server will default to mailhost2.

The email service could also configure this MX record so that both servers have equal priority and receive an equal amount of mail:

example.com record type: priority: value: TTL

@ MX 10 mailhost1.example.com 45000

@ MX 10 mailhost2.example.com 45000

This configuration enables the email provider to equally [balance the load](https://www.cloudflare.com/load-balancing/) between the two servers.

Sign up

Free DNS included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is the process of querying an MX record?

Message transfer agent (MTA) software is responsible for querying MX records. When a user sends an email, the MTA sends a DNS query to identify the mail servers for the email recipients. The MTA establishes an SMTP connection with those mail servers, starting with the prioritized domains (in the first example above, mailhost1).

## What is a backup MX record?

A backup MX record is just an MX record for a mail server with a higher 'priority' value (which means a lower priority), so that under normal circumstances mail will go to the more prioritized servers. In the first example above, mailhost2 would be the 'backup' server because email traffic will be handled by mailhost1 as long as it is up and running.

Report

Secure your DNS infrastructure

[Get the report →](https://www.cloudflare.com/lp/dns-and-the-threat-of-ddos/)

## Can MX records point to a CNAME?

A [CNAME](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/) record is used for referencing a domain's alias instead of its actual name. CNAME records typically point to an [A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/) (in IPv4) or AAAA record (in IPv6) for that domain. However, MX records have to point directly to a server's A record or [AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/). Pointing to a CNAME is forbidden by the [RFC documents that define](https://tools.ietf.org/html/rfc2181) how MX records function.

## How to set up MX records in Cloudflare

For help setting up MX records in Cloudflare, refer to [Set up email records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/).
