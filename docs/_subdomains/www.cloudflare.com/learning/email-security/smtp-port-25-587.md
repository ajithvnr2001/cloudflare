---
url: https://www.cloudflare.com/learning/email-security/smtp-port-25-587/
title: What SMTP port should be used? Port 25, 587, or 465?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:38.196484+00:00
---

# What SMTP port should be used? Port 25, 587, or 465?

> Source: https://www.cloudflare.com/learning/email-security/smtp-port-25-587/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What SMTP port should be used? Port 25, 587, or 465? 

Although port 465 is the recommended port for secure SMTP email transmission, some systems sometimes rely on ports 25, 587, or 2525. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Identify the correct port for SMTP 
  * Explain the differences between ports 25, 465, 587, and 2525 
  * Understand why nonstandard ports are sometimes used for email 



Related content  [ What is the Simple Mail Transfer Protocol (SMTP)? ](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[ What is IMAP? ](https://www.cloudflare.com/learning/email-security/what-is-imap/)[ What is email encryption? ](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[ What is business email compromise (BEC)? ](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)

On this page

  * What SMTP port should be used?

  * What is SMTP?

  * What is an SMTP port?

  * How does SMTP Secure work?

    * SMTPS on port 465

    * SMTPS vs. end-to-end email encryption

  * What ports do POP3 and IMAP use?

  * When is port 2525 used?

    * Why email ports may be blocked




## What SMTP port should be used?

Originally, the [Simple Mail Transfer Protocol (SMTP)](https://www.cloudflare.com/learning/email-security/what-is-smtp/) used port 25. Today, SMTP should instead use port 465 — this is the default port for encrypted email transmissions using SMTP Secure (SMTPS).

Port 465 is today the recommended choice for SMTPS, as it uses Implicit TLS and offers better protection against certain attacks. Port 587, which uses STARTTLS, remains widely supported and is still commonly used for encrypted email submission. Some email service providers also offer SMTP over port 2525 as a fallback option when standard ports are blocked by [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/) or network policies.

## What is SMTP?

SMTP is the [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/), or set of rules for formatting data, that helps emails travel across the Internet. It transfers emails from mail server to mail server until they reach their final destination. At that point, other protocols are used to retrieve the emails and allow users to read them.

(Like [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/), SMTP is an [application layer](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) protocol that runs on top of [TCP/IP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/).)

Sign up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is an SMTP port?

Most networking protocols (like SMTP) are designed to go to a specific port. In networking, a [port](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) is a virtual location within a computer.

A port is somewhat like a mail slot in a large building, with each mail slot belonging to a different resident within the building. Addressing mail to the entire building does not ensure delivery, as the wrong resident might receive the mail and discard it. Instead, mail has to be addressed to the specific mail slot owned by the addressee. Similarly, a computer may not know what to do with network data that does not indicate a port. But the computer can receive data directed at a specific port and pass it to the correct application or process.

An SMTP port is the port designated for use by SMTP — as stated above, this has been ports 25, 465, 587, and 2525 at various times and in various situations.

Demo

Multi-channel phishing threat defense

[Watch the demo →](https://www.cloudflare.com/lp/multi-channel-phishing-demo/)

## How does SMTP Secure (SMTPS) work?

SMTPS is more secure than regular SMTP because it encrypts emails, authenticates emails, and prevents data tampering. It does these three things by using the [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) protocol.

  * **Encryption:** TLS encrypts data as it traverses a network. [Encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) is the process of scrambling data so that only parties with the correct decryption [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/) can unscramble and view the data. This keeps the data secure as it travels through untrusted environments like the Internet.

    * **Authentication:** TLS uses digital signatures to ensure that network traffic comes from the place it claims to be from. Without this step, computers will accept data from impostors, attackers, or other malicious parties.

    * **Email integrity:** Digital signatures also help ensure that data has not been tampered with.




The recommended default port for SMTPS is port 465.

#### SMTPS on port 465

In the 1990s, some email service providers began to use SMTPS with [Secure Sockets Layer (SSL)](https://www.cloudflare.com/learning/ssl/what-is-ssl/), which was the original version of TLS that has now been deprecated. They designated port 465 for this purpose, even though no official Internet bodies had sanctioned such use of that port. (Port usage is standardized to ensure communication is possible between diverse computers and networks.)

SMTPS has since been updated by additional defining documents known as RFCs. In 2011, [RFC 6409](https://www.rfc-editor.org/rfc/rfc6409) designated port 587 for use with SMTPS, which is why some services use that port. However, [RFC 8314](https://www.rfc-editor.org/rfc/rfc6409) in 2018 recommended implementing SMTPS via Implicit TLS at default port 465.

#### SMTPS vs. end-to-end email encryption

While SMTPS is more secure and [private](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) than using no encryption or authentication, it only encrypts emails as they move from sender to mail server and between mail servers. A mail server on an email's path receives the email in unencrypted form before re-encrypting it to pass it to the next server. This is like if a postal service transferred the contents of an envelope to a new envelope as it passed through each post office, leaving the envelope's contents briefly exposed.

Some email senders prefer to use [end-to-end encryption (E2EE)](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/). E2EE ensures that only the sender and the recipient of an email can view it in decrypted form. It keeps email contents private from all intermediaries, including the mail servers on the email's path. This process is similar to an envelope that remains sealed until it reaches the addressee.

SMTPS does not enable E2EE. Instead, protocols like Pretty Good Privacy (PGP) or Secure/Multipurpose Internet Mail Extensions (S/MIME) can be used for E2EE. To learn more, see [What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)

## What ports do POP3 and IMAP use?

While SMTP sends emails, the Post Office Protocol (POP3) and [Internet Message Access Protocol (IMAP)](https://www.cloudflare.com/learning/email-security/what-is-imap/) retrieve them, enabling recipients to read or download them. Much like SMTP, these protocols have both encrypted (via TLS) and unencrypted versions:

  * Unencrypted IMAP uses port 143, while encrypted IMAP uses port 993

  * Unencrypted POP3 uses port 110, while encrypted POP3 uses port 995




## When is port 2525 used?

Some email services offer SMTP delivery over port 2525 in case the above ports are blocked. However, this port is not standard for email and is not officially associated with SMTP.

#### Why email ports may be blocked

Some servers do not support all versions of SMTP and the other email protocols — for instance, older services may not be configured to receive TLS-encrypted traffic at port 465 or 587. Additionally, network administrators sometimes deny access to these ports to block attack traffic and spam, or to stop users from running their own mail servers.

While blocking port 25 or other email ports may prevent some spam and phishing attacks, malicious and unwanted emails are still likely to get through. Sophisticated [business email compromise (BEC)](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/) attacks, in particular, are often well-disguised within acceptable email traffic. To counteract this, Cloudflare Email Security stops sophisticated email-based attacks by detecting threats in advance. [Read more about Cloudflare Email Security](https://www.cloudflare.com/sase/products/email-security/).
