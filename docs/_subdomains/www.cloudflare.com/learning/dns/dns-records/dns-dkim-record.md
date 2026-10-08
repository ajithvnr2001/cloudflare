---
url: https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/
title: What is a DNS DKIM record?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:07.240066+00:00
---

# What is a DNS DKIM record?

> Source: https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  What is a DNS DKIM record? 

A DKIM record is a specialized DNS TXT record that stores the public key used to verify an email's authenticity. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe how DKIM helps stop email spam 
  * View an example DKIM record 
  * Explain how DKIM headers work 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)

On this page

  * What is DKIM?

  * How does DKIM work?

  * What is a DKIM record?

    * Name

    * Content

    * Record type and TTL

  * What is a DKIM header? How does a DKIM signature work?

  * How does DKIM relate to DMARC?

  * How to set up DKIM records in Cloudflare




## What is DKIM?

DomainKeys Identified Mail (DKIM) is a method of email authentication that helps prevent spammers and other malicious parties from [impersonating a legitimate domain](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/).

All email addresses have a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) — the part of the address after the "@" symbol. Spammers and attackers may try to impersonate a domain when sending emails to carry out [phishing attacks](https://www.cloudflare.com/learning/access-management/phishing-attack/) or other scams.

Suppose Chuck wants to trick Alice, who works for example.com, into sending him confidential company information. He could send her an email that seems to be coming from "[bob@example.com](mailto:bob@example.com)" to fool her into thinking he also works for example.com.

DKIM, along with [Sender Policy Framework (SPF)](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) and [Domain-based Message Authentication Reporting and Conformance (DMARC)](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/), makes it much more difficult for attackers to impersonate domains in this way. Emails that do not pass DKIM and SPF get marked as "spam" or are not delivered by email servers. If example.com has DKIM, SPF, and DMARC set up for their domain, then Alice will probably never even see Chuck's malicious email because it will either go to her spam folder or be rejected by the email server altogether.

Report

2024 IDC Marketscape for Edge Delivery Services

[Get the report →](https://www.cloudflare.com/lp/idc-marketscape-for-worldwide-commercial-edge-delivery-services-2024/)

## How does DKIM work?

There are two main aspects of DKIM: the DKIM record, which is stored in the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) records for the domain, and the DKIM header, which is attached to all emails from the domain.

DKIM uses digital signature schemes based on [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) to authenticate where an email came from, that it actually came from a server that sends emails from that domain. A pair of cryptographic keys are used: a private key for the sender to sign messages, and a public key for the receiver to verify signatures. A receiver cannot use the public key to sign messages, and vice versa.

The email provider generates the public key and private key. They give the public key to the domain owner, who stores the public key in a publicly available DNS record — the DKIM record.

All emails sent from that domain include a DKIM header, which contains a section of data that is signed with the private key: this is called a "digital signature." An email server can check the DKIM DNS record, obtain the public key, and use the public key to verify the digital signature.

This process also ensures that the email has not been changed in transit. The digital signature will not be verified if email headers or the email body have been altered — like a tamper-proof seal on a canister of medicine.

Sign Up

Free DNS included with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/lp/pg-all-plans-dns/)

## What is a DKIM record?

A DKIM record stores the DKIM public key — a randomized string of characters that is used to verify anything signed with the private key. Email servers query the domain's DNS records to see the DKIM record and view the public key.

A DKIM record is really a [DNS TXT ("text") record](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/). TXT records can be used to store any text that a domain administrator wants to associate with their domain. DKIM is one of many uses for this type of DNS record. (In some cases, domains have stored their DKIM records as [CNAME](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/) records that point to the key instead; however, the [official RFC](https://datatracker.ietf.org/doc/html/rfc6376/) requires these records to be TXT.)

Here is an example of a DKIM DNS TXT record:

Name Type Content TTL

`big-email._domainkey.example.com` `TXT` `v=DKIM1; p=76E629F05F70 9EF665853333 EEC3F5ADE69A 2362BECE4065 8267AB2FC3CB 6CBE` `6000`

#### Name

Unlike most DNS TXT records, DKIM records are stored under a specialized name, not just the name of the domain. DKIM record names follow this format:
    
    
    `[selector]._domainkey.[domain]`
    

The `selector` is a specialized value issued by the email service provider used by the domain. It is included in the DKIM header to enable an email server to perform the required DKIM lookup in the DNS. The `domain` is the email domain name. `._domainkey.` is included in all DKIM record names.

To look up the DKIM record, email servers use the DKIM selector provided by the email service provider, not just the domain name. Suppose example.com uses Big Email as their email service provider, and suppose Big Email uses the DKIM selector `big-email`. Most of example.com's DNS records would be named `example.com`, but their DKIM DNS record would be under the name `big-email._domainkey.example.com`, which is listed in the example above.

#### Content

This is the part of the DKIM DNS record that lists the public key. In the example above, `v=DKIM1` indicates that this TXT record should be interpreted as DKIM, and the public key is everything after `p=`.

#### Record type and TTL

These are standard fields in DNS records. `TXT` indicates that this is a DNS TXT record. "TTL" stands for time to live (measured in seconds), and it indicates how long this record should be considered valid before it needs to be refreshed. DKIM records generally have a TTL of several minutes.

## What is a DKIM header? How does a DKIM signature work?

The sending email server creates its digital signature using email headers, the email body (actually a hash of the email body — read more below), and its private key. This digital signature is attached to the email as part of the DKIM header.

The DKIM header is one of many headers that are attached to an email. Most email applications do not show the header when displaying an email unless the user selects certain options. In Gmail, for example, users can view an email's header by clicking on the three vertical dots in the upper right of the email, then clicking "Show original."

Here is an example of a DKIM header:
    
    
    v=1; a=rsa-sha256;
    d=example.com; s=big-email;
    h=from:to:subject;
      bh=uMixy0BsCqhbru4fqPZQdeZY5Pq865sNAnOAxNgUS0s=;
      b=LiIvJeRyqMo0gngiCygwpiKphJjYezb5kXBKCNj8DqRVcCk7obK6OUg4o+EufEbB
    tRYQfQhgIkx5m70IqA6dP+DBZUcsJyS9C+vm2xRK7qyHi2hUFpYS5pkeiNVoQk/Wk4w
    ZG4tu/g+OA49mS7VX+64FXr79MPwOMRRmJ3lNwJU=
    

  * `v=` shows which version of DKIM is in use.

  * `d=` is the domain name of the sender.

  * `s=` is the selector that the receiving server should use to look up the DNS record.

  * `h=` lists the header fields that are used to create the digital signature, or `b`. In this case, the from, to, and subject headers are used. If Bob sent an email to Alice using the example.com domain and the subject line was "Recipe for cheesecake," the content used here would be "[bob@example.com](mailto:bob@example.com)" + "[alice@example.com](mailto:alice@example.com)" + "Recipe for cheesecake". (This content would also be canonicalized — put into a standardized format.)

  * `bh=` is the hash of the email body. A hash is the result of a specialized mathematical function called a hash function. This is included so that the receiving email server can compute the signature before the entire email body loads, since email bodies can be any length and loading it may take a long time in some cases.

  * `a=` is the algorithm used to compute the digital signature, or `b`, as well as generate the hash of the email body, or `bh`. In this example, RSA-SHA-256 is in use (RSA using SHA-256 as the hash function for the digital signature, and SHA-256 for the body hash).

  * `b=` is the **digital signature** , generated from `h` and `bh` and signed with the private key.




The digital signature (`b=`) allows the receiving server to 1. authenticate the sending server and 2. ensure integrity — that the email has not been tampered with.

The receiving server does this by taking the same content that is listed in `h=` plus the body hash (`bh=`) and using the public key from the DKIM record to check if the digital signature is valid. If the correct private key was used and if the content (headers and body) has not been altered, the email passes the DKIM check.

## How does DKIM relate to DMARC?

DMARC is an email authentication method built on top of DKIM and SPF. DMARC describes what to do with an email that fails SPF and DKIM. Together, SPF, DKIM, and DMARC help prevent email spam and email spoofing. Like DKIM records, DMARC policies are stored as DNS TXT records.

## How to set up DKIM records in Cloudflare

To quickly set this record up in Cloudflare, use the [Email Security DNS Wizard](https://developers.cloudflare.com/dmarc-management/security-records/).

_Learn more about DNS records for email:_

  * [DNS SPF record](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)

  * [DNS DMARC record](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)

  * [DNS MX record](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)

  * [DNS TXT record](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)




To learn more about DKIM, see [RFC 6376](https://datatracker.ietf.org/doc/html/rfc6376/).
