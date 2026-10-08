---
url: https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/
title: What is email spoofing? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:00.798174+00:00
---

# What is email spoofing? | Learning Center

> Source: https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is email spoofing? 

Email spoofing is the creation of email messages with a forged sender address, commonly used in phishing attacks. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define email spoofing 
  * Understand how spoofing works technically 
  * Learn about anti-spoofing measures 



Related content  [ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)

On this page

  * Article Summary:

  * What is email spoofing?

  * How does email spoofing work?

  * How to protect against email spoofing

  * How does email authentication fit into email security?




## Article Summary:

  * Email spoofing involves forging sender addresses to deceive recipients, often serving as a primary mechanism for phishing attacks and the distribution of malicious malware payloads.
  * Attackers exploit vulnerabilities in the Simple Mail Transfer Protocol (SMTP) to masquerade as trusted entities, making preventing email spoofing essential for maintaining organizational security and trust.
  * Implementing robust email authentication protocols like SPF, DKIM, and DMARC effectively verifies sender identity, blocking unauthorized messages and protecting users from sophisticated domain-based impersonation threats.



## What is email spoofing?

In [email](https://www.cloudflare.com/learning/email-security/what-is-email/) spoofing, an attacker uses an email header to mask their own identity and impersonate a legitimate sender. (An email header is a code snippet that contains important details about the message such as the sender, the recipient, and tracking data.)

While email spoofing is a specific tactic involving the forging of email header information, attackers can use other tactics to achieve similar results. For example, attackers may create an email domain that looks very similar to the legitimate sender's domain, in hope that recipients will not notice the error. An example would be using the domain '@1egitimatecompany.com' rather than '@legitimatecompany.com.' Attackers may also change the display name to impersonate a sender: for example, sending malicious emails from 'LegitimateCEOName@gmail.com' rather than 'LegitimateCEOName@legitimatecompany.com.' 

The key difference between these techniques is that successful email spoofing attempts will present as legitimate domains — like cloudflare.com — as opposed to a misspelled domain (janeexecutive@jan3scompany.com) or an address not associated with the domain at all (janetherealceo@gmail.com). This article will focus specifically on emails with forged headers. 

Email spoofing falls under the larger [domain spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/) umbrella. In domain spoofing, attackers will attempt to fake a website name (or email address), generally as part of [phishing](https://www.cloudflare.com/learning/access-management/phishing-attack/) attacks. Domain spoofing extends beyond email and can be used to create fake websites or fraudulent advertisements. 

## How does email spoofing work?

Attackers use scripts to forge the fields an email recipient can see. These fields are found within the email header and include the “from” address and the “reply-to” address. Here’s an example of what these fields could look like in a spoofed email:

  * **From:** “Legitimate Sender” email@legitimatecompany.com 
  * **Reply-to:** email@legitimatecompany.com



Forging these fields is possible because the email transmission protocol [Simple Mail Transfer Protocol (SMTP)](https://www.cloudflare.com/learning/email-security/what-is-smtp/) does not have a built-in method for authenticating email addresses. In fact, the sender’s and recipient's email addresses exist in two places within an email: the header and the SMTP envelope. The email header includes the fields that the recipient sees. The SMTP envelope, however, contains the information servers use to deliver an email to the correct address. But these fields do not have to match for an email to send successfully. Because the SMTP envelope never checks the header and the recipient cannot see the information in the envelope, email spoofing is relatively easy. 

Because a spoofed email appears to come from a legitimate sender, recipients may be tricked into divulging sensitive information, clicking malicious links, or taking other actions they otherwise would not. For this reason, email spoofing is commonly used in phishing attacks. 

In some cases, attackers will use other tactics to bolster the credibility of a spoofed email domain. This may include copying a company’s logo, branded art, and other design elements, or using messages and language that feel relevant to the imitated company.

## How to protect against email spoofing 

Email recipients can follow these steps to ensure they do not fall for email spoofing:

  * **Be wary of messages encouraging action quickly or urgently:** Recipients should be suspicious of any unexpected or unprompted emails asking for personal information, payment, or other immediate action. For example, an out-of-the-blue prompt to change login information for an application should be considered suspicious. 
  * **Inspect email headers:** Many email clients offer a way to view an email’s header. For example, [in Gmail](https://it.umn.edu/services-technologies/how-tos/gmail-view-email-headers), clicking “Show original” on an individual email will reveal the email header. Once viewing the header, look for the “Received” section. If a different domain than the one in the “From” address appears, the email is likely forged. 
  * **Use software that filters spoofed messages:** Anti-spam software can require authentication for incoming emails, thereby blocking spoofing attempts.



Domain owners can also take action to prevent attackers from sending messages from their domain. To do so, organizations can create [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) records specifically for authentication. These include:

  * **[SPF records](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/):** A Sender Policy Framework (SPF) record lists the servers that are authorized to send emails from a particular domain. This way, if someone made up an email address associated with a domain, it would not be listed on the SPF record and would not pass authentication. 
  * **[DKIM records](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/):** DomainKeys Identified Mail (DKIM) records use a pair of cryptographic keys for authentication: one that is public and one that is private. The public key is stored in the DKIM record and the private key digitally signs the DKIM header. Spoofed emails from a domain with a DKIM record will not be signed with the correct cryptographic keys and will therefore fail authentication. 
  * **[DMARC records](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/):** Domain-based Message Authentication Reporting and Conformance (DMARC) records contain DMARC policies, which tell email servers what to do after checking SPF and DKIM records. Domain owners can set rules about whether to block, allow, or deliver messages based on these checks. Because DMARC policies review against other authentication policies and allow domain owners to set more specific rules, these records add another layer of protection against email spoofing. 



At the organizational level, security leaders can also take steps to protect employees from email spoofing by implementing phishing and [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/) protection. 

## How does email authentication fit into email security? 

While email authentication can help protect against email spoofing, it is not a comprehensive [email security solution](https://www.cloudflare.com/sase/use-cases/email-security-services/). For example, email authentication does not account for other common phishing techniques like lookalike domains or emails sent from legitimate domains that have been compromised. 

[Cloudflare Email Security](https://www.cloudflare.com/sase/products/email-security/) offers a more holistic approach. It preemptively crawls the Internet to identify attacker infrastructure, thereby preventing phishing attacks and securing inboxes. 
