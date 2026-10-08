---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/
title: What is a DNS DMARC record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:07.579605+00:00
---

# What is a DNS DMARC record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS DMARC record? 

DMARC is an important part of email security. DMARC policies are stored within DNS TXT records. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain why DMARC is used 
  * Describe a DMARC policy 
  * Understand how DNS TXT records are used for DMARC 



Related content  [ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)

On this page

  * What is DMARC?

  * What is a DMARC policy?

  * What is a DMARC report?

  * What is a DMARC record?

  * What about domains that do not send emails?

  * How to set up DMARC records with Cloudflare




## What is DMARC?

Domain-based Message Authentication Reporting and Conformance (DMARC) is a method of authenticating email messages. A DMARC policy tells a receiving email server what to do after checking a domain's [Sender Policy Framework (SPF)](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) and [DomainKeys Identified Mail (DKIM)](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/) records, which are additional email authentication methods.

DMARC and other email authentication methods are necessary in order to prevent email [spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/). Every email address has a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/), which is the portion of the address that comes after the "@" symbol. Malicious parties and spammers sometimes try to send emails from a domain that they are not authorized to use — like someone writing the wrong return address on a letter. They may do this to try to trick users (as in a [phishing attack](https://www.cloudflare.com/learning/access-management/phishing-attack/)), among other reasons.

Together, DMARC, DKIM, and SPF function like a background check on email senders, to make sure they really are who they say they are.

For example, imagine a spammer sends an email from the address "[trustworthy@example.com](mailto:trustworthy@example.com)," despite the fact that they are not authorized to send email from the "example.com" domain. The spammer would do this by replacing the "From" header in the email with "[trustworthy@example.com](mailto:trustworthy@example.com)" — they would not send an email from the actual example.com email server. Email servers that receive this email can use DMARC, SPF, and DKIM to discover that this is an unauthorized email, and they can mark the email message as spam or refuse to deliver it.

Sign up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is a DMARC policy?

A DMARC policy determines what happens to an email after it is checked against SPF and DKIM records. An email either passes or fails SPF and DKIM. The DMARC policy determines if failure results in the email being marked as spam, getting blocked, or being delivered to its intended recipient. (Email servers may still mark emails as spam if there is no DMARC record, but DMARC provides clearer instructions on when to do so.)

Example.com's domain policy could be:

"If an email fails the DKIM and SPF tests, mark it as spam."

These policies are not recorded as human-readable sentences, but rather as machine-readable commands so that email services can interpret them automatically. That DMARC policy would actually look like:
    
    
    `v=DMARC1; p=quarantine; adkim=s; aspf=s;`
    

What does this mean?

  * `v=DMARC1` indicates that this TXT record contains a DMARC policy and should be interpreted as such by email servers.

  * `p=quarantine` indicates that email servers should "quarantine" emails that fail DKIM and SPF — considering them to be potentially spam. Other possible settings for this include `p=none`, which allows emails that fail to still go through, and `p=reject`, which instructs email servers to block emails that fail.

  * `adkim=s` means that DKIM checks are "strict." This can also be set to "relaxed" by changing the `s` to an `r`, like `adkim=r`.

  * `aspf=s` is the same as `adkim=s`, but for SPF.

  * Note that `aspf` and `adkim` are optional settings. The `p=` attribute is what indicates what email servers should do with emails that fail SPF and DKIM.




If the example.com administrator wanted to make this policy even stricter and signal more strongly to email servers to consider unauthorized messages spam, they would adjust the "p=" attribute like so:
    
    
    `v=DMARC1; p=reject; adkim=s; aspf=s;`
    

Essentially, this says: "If an email fails the DKIM and SPF tests, do not deliver it."

Report

Secure your DNS infrastructure

[Get the report →](https://www.cloudflare.com/lp/dns-and-the-threat-of-ddos/)

## What is a DMARC report?

DMARC policies can contain instructions to send reports about emails that pass or fail DKIM or SPF. Typically, administrators set up reports to be sent to a third-party service that boils them down to a more digestible form, so administrators are not overwhelmed with information. DMARC reports are extremely important because they give administrators the information they need to decide how to adjust their DMARC policies — for instance, if their legitimate emails are failing SPF and DKIM, or if a spammer is trying to send illegitimate emails.

The example.com administrator would add the `rua` part of this policy to send their DMARC reports to a third-party service (with an email address of "[third-party-example@example.com](mailto:third-party-example@example.com)"):
    
    
    `v=DMARC1; p=reject; adkim=s; aspf=s; rua=mailto:third-party-example@example.com;`
    

## What is a DMARC record?

A DMARC record stores a domain's DMARC policy. DMARC records are stored in the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) as [DNS TXT records](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/). A DNS TXT record can contain almost any text a domain administrator wants to associate with their domain. One of the ways DNS TXT records are used is to store DMARC policies.

(Note that a DMARC record is a DNS TXT record that contains a DMARC policy, not a specialized type of [DNS record](https://www.cloudflare.com/learning/dns/dns-records/).)

Example.com's DMARC policy might look like this:

Name Type Content TTL

`_dmarc.example.com` `TXT` `v=DMARC1; p=quarantine; adkim=r; aspf=r; rua=mailto:third-party-example@example.com;` `32600`

Within this TXT record, the DMARC policy is contained in the "Content" field.

## What about domains that do not send emails?

Domains that do not send emails should still have a DMARC record in order to prevent spammers from using the domain. The DMARC record should have a DMARC policy that rejects all emails that fail SPF and DKIM — which should be all emails sent by that domain.

In other words, if example.com was not configured to send email, all emails would fail SPF and DKIM and be rejected.

## How to set up DMARC records with Cloudflare

For help setting up this record in Cloudflare, use the [Email Security DNS Wizard](https://developers.cloudflare.com/dmarc-management/security-records/).

_Learn more about DNS records for email:_

  * [DNS SPF record](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)

  * [DNS DKIM record](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)

  * [DNS MX record](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)

  * [DNS TXT record](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)




DMARC is described further in [RFC 7489](https://datatracker.ietf.org/doc/html/rfc7489).
