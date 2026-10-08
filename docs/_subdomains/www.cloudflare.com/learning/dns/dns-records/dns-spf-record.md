---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/
title: What is a DNS SPF record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:07.949001+00:00
---

# What is a DNS SPF record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS SPF record? 

SPF records are a type of DNS TXT record commonly used for email authentication. SPF records include a list of IP addresses and domains authorized to send emails from that domain. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define a DNS SPF record 
  * Explain the benefits of a DNS SPF record 
  * Understand a DNS SPF record’s components 



Related content  [ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)

On this page

  * What is a DNS SPF record?

  * How does a mail server check an SPF record?

  * What does an SPF record look like?

  * Why are SPF records used?

  * How to set up SPF records in Cloudflare




## What is a DNS SPF record?

A sender policy framework (SPF) record is a type of DNS TXT record that lists all the servers authorized to send emails from a particular domain. A DNS TXT (“text”) record lets a domain administrator enter arbitrary text into the Domain Name System (DNS). TXT records were initially created for the purpose of including important notices regarding the domain, but have since evolved to serve other purposes.

SPF records were originally created because the standard protocol used for email — the Simple Mail Transfer Protocol ([SMTP](https://datatracker.ietf.org/doc/html/rfc5321)) — does not inherently authenticate the “from” address in an email. This means that without SPF or other authentication records, an attacker can easily impersonate a sender and trick the recipient into taking action or sharing information they otherwise would not.

Think of SPF records like a guest list that is managed by a door attendant. If someone is not on the list, the door attendant will not let them in. Similarly, if an SPF record does not have a sender’s IP address or domain on its list, the receiving server (door attendant) will either not deliver those emails or mark them as spam.

SPF records are just one of many [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)-based mechanisms that can help email servers confirm whether an email comes from a trusted source. Domain-based Message Authentication Reporting and Conformance ([DMARC](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)) and DomainKeys Identified Mail ([DKIM](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)) are two other mechanisms used for email authentication.

It is worth noting that, at one point, SPF records had a dedicated DNS record type. The dedicated record type has since been [deprecated](https://datatracker.ietf.org/doc/html/rfc7208#section-3.1) and only TXT records are to be used.

Report

2024 IDC Marketscape for Edge Delivery Services

[Get the report →](https://www.cloudflare.com/lp/idc-marketscape-for-worldwide-commercial-edge-delivery-services-2024/)

## How does a mail server check an SPF record?

Mail servers go through a relatively simple process when checking an SPF record:

  * Server One sends an email. Its IP address is _192.0.2.0_ and the return-path the email uses is [email@returnpath.com](mailto:email@returnpath.com). (A return-path address is different from the “from” address and is used specifically for collecting and processing bounced messages.)

  * The mail server that is receiving the message (Server Two) takes the return-path domain and searches for its SPF record.

  * If Server Two finds an SPF record for the return-path’s [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/), it searches the SPF record for Server One’s IP address in its list of authorized senders. If the IP address is listed in the SPF record, the SPF check passes and the email will go through. If the IP address is not listed in the SPF record, the SPF check fails. In this case, the email will be rejected or marked as spam.


Sign Up

Free DNS included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/lp/pg-all-plans-dns/)

## What does an SPF record look like?

SPF records must follow certain standards in order for the server to understand how to interpret its contents. Here is an example of the core components of an SPF record:
    
    
    `v=spf1 ip4:192.0.2.0 ip4:192.0.2.1 include:examplesender.email -all`
    

This example lets the server know what type of record this is, states the approved IP addresses and a third-party for this domain, and tells the server what to do with non-compliant emails. Let’s break down how the individual components accomplish this:

  * `v=spf1` tells the server that this contains an SPF record. Every SPF record must begin with this string.

  * Then comes the “guest list” portion of the SPF record or the list of authorized IP addresses. In this example, the SPF record is telling the server that `ip4:192.0.2.0` and `ip4:192.0.2.1` are authorized to send emails on behalf of the domain.

  * `include:examplesender.net` is an example of the include tag, which tells the server what third-party organizations are authorized to send emails on behalf of the domain. This tag signals that the content of the SPF record for the included domain (examplesender.net) should be checked and the IP addresses it contains should also be considered authorized. Multiple domains can be included within an SPF record but this tag will only work for valid domains.

    * Finally, `-all` tells the server that addresses not listed in the SPF record are not authorized to send emails and should be rejected.
  * Alternative options here include `~all`, which states that unlisted emails will be marked as insecure or spam but still accepted, and, less commonly, `+all`, which signifies that any server can send emails on behalf of your domain.




While the example used in this article is fairly straightforward, SPF records can certainly be more complex. Here are just a few things to keep in mind to ensure SPF records are valid:

  * There cannot be more than one SPF record associated with a domain.

  * The record must end with the `all` component or include a `redirect=` component (which indicates that the SPF record is hosted by another domain).

  * An SPF record cannot contain uppercase characters.




Check out the [official SPF record documentation](https://datatracker.ietf.org/doc/html/rfc7208) for more information.

## Why are SPF records used?

There are many reasons domain operators use SPF records:

  * **Preventing attacks:** If emails are not authenticated, companies and email recipients are at risk for [phishing](https://www.cloudflare.com/learning/access-management/phishing-attack/) attacks, spam emails, and email spoofing. With SPF records, it is harder for attackers to imitate a domain, reducing the likelihood of these attacks.

  * **Improving email deliverability:** Domains without a published SPF record may have their emails bounce or be marked as spam. Over time, bounced emails or emails marked as spam can hurt a domain’s ability to reach their audience’s inboxes, compromising efforts to communicate with customers, employees, and other entities.

  * **DMARC compliance:** DMARC is an email validation system that helps ensure that emails are sent only by authorized users. DMARC policies dictate what servers should do with emails that fail SPF and DKIM checks. Based on the DMARC policy instructions, those emails will either be marked as spam, rejected, or delivered as normal. Domain administrators receive reports about their email activity that help them make adjustments to their policy.




## How to set up SPF records in Cloudflare

To easily set up SPF records in Cloudflare, use the [Email Security DNS Wizard](https://developers.cloudflare.com/dmarc-management/security-records/).

_Learn more about DNS records for email:_

  * [DMARC record](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)

    * [DNS DKIM record](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)

    * [DNS MX record](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)

    * [DNS TXT record](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)



