---
url: https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/
title: How to protect domains that do not send email
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:09.150108+00:00
---

# How to protect domains that do not send email

> Source: https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  How to protect domains that do not send email 

Creating these specific DNS records helps protect domains that do not send emails from being used in domain spoofing attacks. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Learn what DNS records can help protect domains that do not send emails 
  * Describe how these types of DNS records work 
  * Understand the major components of these types of DNS records 



On this page

  * How to protect domains that do not send emails

  * What are the different types of DNS TXT records used for email authentication?

  * What do these DNS records look like?




## How to protect domains that do not send emails

Domains that do not send emails can still be used in email [spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/) or [phishing attacks](https://www.cloudflare.com/learning/access-management/phishing-attack/), but there are specific types of [DNS text (TXT)](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/) records that can be used to stifle attackers. Each of these records sets rules for how unauthorized emails should be treated by mail servers, making it harder for attackers to exploit these domains.

A DNS TXT record allows domain administrators to enter text into the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/). DNS TXT records are used for processes like email authentication because they can store important information that servers can use to confirm whether or not a domain has authorized an email sender to send messages on its behalf.

Examples of domains that do not send emails include domains [purchased](https://www.cloudflare.com/products/registrar/) to protect a brand name or for a future business. Defunct, legacy domains also have no reason to send emails and could benefit from these types of records.

## What are the different types of DNS TXT records used for email authentication?

There are three main types of DNS TXT records used for email authentication. Each of them differs slightly in how they work:

  * **[Sender Policy Framework (SPF)](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)** records list all of the IP addresses and domain names that are authorized to send emails on behalf of the domain.

    * **[DomainKeys Identified Mail (DKIM)](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)** records provide a digital signature to authenticate whether or not the sender actually authorized the email. This digital signature also helps prevent [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/), in which attackers intercept communications and alter messages for nefarious purposes.

    * **[Domain-based Message Authentication, Reporting and Conformance (DMARC)](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)** records hold a domain’s DMARC policy. DMARC is a system for authenticating emails by checking a domain’s SPF and DKIM records. The DMARC policy states whether emails that fail SPF or DKIM checks should be marked as spam, blocked, or allowed to go through.




## What do these DNS records look like?

Because these DNS records all function slightly differently, each of their components are unique.

**SPF**

SPF records can be formatted to protect domains against attempted phishing attacks by rejecting any emails sent from the domain. To do so, an SPF record must use the following format.
    
    
    `v=spf1 -all`
    

*_Note, SPF records are set directly on the domain itself, meaning they do not require a special subdomain._

Here is what the individual components of this record mean:

  * `v=spf1` lets the server know that the record contains an SPF policy. All SPF records must begin with this component.

    * The indicator `-all` tells the server what to do with non-compliant emails or any senders that are not explicitly listed in the SPF record. With this type of SPF record, no IP addresses or domains are allowed, so `-all` states that all non-compliant emails will be rejected. For this type of record, all emails are considered non-compliant because there are no accepted IP addresses or domains.



**DKIM**

DKIM records protect domains by ensuring emails were actually authorized by the sender using a public key and a private key. DKIM records store the public key that the email server then uses to authenticate that the email signature was authorized by the sender. For domains that do not send emails, the DKIM record should be configured without an associated public key. Below is an example:

Name Type Content

`*._domainkey.example.com` `TXT` `v=DKIM1; p=`

  * `*._domainkey.example.com` is the specialized name for the DKIM record (where “example.com” should be replaced with your domain). In this example, the asterisk (referred to as the wildcard) is being used as the selector, which is a specialized value that the email service provider generates and uses for the domain. The selector is part of the DKIM header and the email server uses it to perform the DKIM lookup in the DNS. The wildcard covers all possible values for the selector.

  * `TXT` indicates the DNS record type.

  * `v=DKIM1` sets the version number and tells the server that this record references a DKIM policy.

    * The `p` value helps authenticate emails by tying a signature to its public key. In this DKIM record, the `p` value should be empty because there is no signature/public key to tie back to.

**DMARC**




DMARC policies can also help protect domains that do not send emails by rejecting all emails that fail SPF and DKIM. In this case, all emails sent from a domain not configured to send emails would fail SPF and DKIM checks. Below is an example of how to format a policy this way:

Name Type Content

`_dmarc.example.com` `TXT` `v=DMARC1;p=reject;sp=reject;adkim=s;aspf=s`

  * The name field ensures that the record is set on the subdomain called `_dmarc.example.com`, which is required for DMARC policies.

    * `TXT` indicates the DNS record type.

    * `v=DMARC1` tells the server that this DNS record contains a DMARC policy.

  * `p=reject` indicates that email servers should reject emails that fail DKIM and SPF checks.

  * `adkim=s` represents something called the alignment mode. In this case, the alignment mode is set to “s” for strict. Strict alignment mode means that the server of the email domain that contains the DMARC record must exactly match the domain in the `From` header of the email. If it does not, the DKIM check fails.

  * `aspf=s` serves the same purpose as `adkim=s`, but for SPF alignment.




The Cloudflare Email Security DNS Wizard makes it simple to set up the correct DNS TXT records and block spammers from using a domain. [Read more about the Wizard here](https://blog.cloudflare.com/tackling-email-spoofing/).
