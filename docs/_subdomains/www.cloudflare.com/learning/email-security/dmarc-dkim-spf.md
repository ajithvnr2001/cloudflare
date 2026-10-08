---
url: https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/
title: What are DMARC, DKIM, and SPF?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:06.064845+00:00
---

# What are DMARC, DKIM, and SPF?

> Source: https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What are DMARC, DKIM, and SPF? 

SPF, DKIM, and DMARC help authenticate email senders by verifying that the emails came from the domain that they claim to be from. These three authentication methods are important for preventing spam, phishing attacks, and other email security risks. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Describe how SPF, DKIM, and DMARC work 
  * Explain how these methods help authenticate email senders 
  * Understand the types of DNS records used in SPF, DKIM, and DMARC 



Related content  [ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ How to stop spam emails ](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[ How to prevent phishing ](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[ What is business email compromise (BEC)? ](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[ When are email attachments safe to open? ](https://www.cloudflare.com/learning/email-security/email-attachments/)

On this page

  * What are DMARC, DKIM, and SPF?

  * How does SPF work?

  * How does DKIM work?

  * How does DMARC work?

  * Where are SPF, DKIM, and DMARC records stored?

  * How to check if an email has passed SPF, DKIM, and DMARC

  * How to set up DMARC, DKIM, and SPF for a domain

  * How to easily set up these records in Cloudflare




## What are DMARC, DKIM, and SPF?

DMARC, DKIM, and SPF are three email [authentication](https://www.cloudflare.com/learning/access-management/what-is-authentication/) methods. Together, they help prevent spammers, [phishers](https://www.cloudflare.com/learning/access-management/phishing-attack/), and other unauthorized parties from sending [emails](https://www.cloudflare.com/learning/email-security/what-is-email/) on behalf of a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)* they do not own.

DKIM and SPF can be compared to a business license or a doctor's medical degree displayed on the wall of an office — they help demonstrate legitimacy.

Meanwhile, DMARC tells mail servers what to do when DKIM or SPF fail, whether that is marking the failing emails as "[spam](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)," delivering the emails anyway, or dropping the emails altogether.

Domains that have not set up SPF, DKIM, and DMARC correctly may find that their emails get quarantined as spam, or are not delivered to their recipients. They are also in danger of having spammers impersonate them.

*_A domain, roughly speaking, is a website address like "example.com". Domains form the second half of an email address:[alice@example.com](mailto:alice@example.com), for instance._

Report

2026 Security Signals Report

[Get the report →](https://www.cloudflare.com/lp/security-signals-report/2026/)

## How does SPF work?

Sender Policy Framework (SPF) is a way for a domain to list all the servers they send emails from. Think of it like a publicly available employee directory that helps someone to confirm if an employee works for an organization.

[SPF records](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) list all the [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of all the servers that are allowed to send emails from the domain, just as an employee directory lists the names of all employees for an organization. Mail servers that receive an email message can check it against the SPF record before passing it on to the recipient's inbox.

Sign Up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## How does DKIM work?

DomainKeys Identified Mail (DKIM) enables domain owners to automatically "sign" emails from their domain, just as the signature on a check helps confirm who wrote the check. The DKIM "signature" is a digital signature that uses cryptography to mathematically verify that the email came from the domain.

Specifically, DKIM uses [public key cryptography](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/):

  * A [DKIM record](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/) stores the domain's _public key_ , and mail servers receiving emails from the domain can check this record to obtain the public [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)

  * The _private key_ is kept secret by the sender, who signs the email's header with this key

  * Mail servers receiving the email can verify that the sender's private key was used by applying the public key




## How does DMARC work?

Domain-based Message Authentication Reporting and Conformance (DMARC) tells a receiving email server what to do given the results after checking SPF and DKIM. A domain's DMARC policy can be set in a variety of ways — it can instruct mail servers to quarantine emails that fail SPF or DKIM (or both), to reject such emails, or to deliver them.

DMARC policies are stored in [DMARC records](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/). A DMARC record can also contain instructions to send reports to domain administrators about which emails are passing and failing these checks. DMARC reports give administrators the information they need to decide how to adjust their DMARC policies (for example, what to do if legitimate emails are erroneously getting marked as spam).

## Where are SPF, DKIM, and DMARC records stored?

SPF, DKIM, and DMARC records are stored in the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/), which is publicly available. The DNS's main use is matching web addresses to IP addresses, so that computers can find the correct servers for loading content over the Internet without human users having to memorize long alphanumeric addresses. The DNS can also store a variety of [records](https://www.cloudflare.com/learning/dns/dns-records/) associated with a domain, including alternate names for that domain ([CNAME records](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)), IPv6 addresses ([AAAA records](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)), and reverse DNS records for domain lookups ([PTR records](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)).

DKIM, SPF, and DMARC records are all stored as [DNS TXT records](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/). A DNS TXT record stores text that a domain owner wants to associate with the domain. This record can be used in a variety of ways, since it can contain any arbitrary text. DKIM, SPF, and DMARC are three of several applications for DNS TXT records.

## How to check if an email has passed SPF, DKIM, and DMARC

Most email clients provide an option labeled "Show details" or "Show original" that displays the full version of an email, including its header. The header — typically a long block of text above the body of the email — is where mail servers append the results of SPF, DKIM, and DMARC.

Reading through the dense header can be tricky. Users viewing it on a browser can click "Ctrl+F" or "Command+F" and type "spf," "dkim," or "dmarc" to find these results.

The relevant text might look like:
    
    
    `
    arc=pass (i=1 spf=pass spfdomain=example.com dkim=pass
    dkdomain=example.com dmarc=pass fromdomain=example.com);
    `
    

The appearance of the word "pass" in the text above indicates that the email has passed an authentication check. "spf=pass," for example, means the email did not fail SPF; it came from an authorized server with an IP address that is listed in the domain's SPF record.

In this example, the email passed all three of SPF, DKIM, and DMARC, and the mail server was able to confirm it really came from example.com and not an impostor.

It is important to note that these records themselves do not enforce the domain's policies or authenticate the emails. The mail servers have to check them and apply them correctly for the records to have any effect.

It is also important to note that domain owners need to configure their SPF, DKIM, and DMARC records properly themselves — both in order to prevent spam from their domain, and to make sure that legitimate emails from their domain are not marked as spam. Web hosting services do not necessarily do this automatically. Even domains that do not send emails should at least have DMARC records so that spammers cannot pretend to send emails from that domain.

## How to set up DMARC, DKIM, and SPF for a domain

DMARC, DKIM, and SPF have to be set up in the domain's DNS settings. Administrators can contact their DNS provider — or, their web hosting platform may provide a tool that enables them to upload and edit DNS records. For more details on how these records work, see our articles about them:

  * [SPF DNS records](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)

  * [DKIM DNS records](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)

  * [DMARC DNS records](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)




## How to easily set up these records in Cloudflare

To set up these records in Cloudflare, use the [Email Security DNS Wizard](https://developers.cloudflare.com/dmarc-management/security-records/).
