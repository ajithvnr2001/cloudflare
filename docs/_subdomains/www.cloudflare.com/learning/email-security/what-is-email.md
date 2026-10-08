---
url: https://www.cloudflare.com/learning/email-security/what-is-email/
title: What is email? | Email definition
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:00.441582+00:00
---

# What is email? | Email definition

> Source: https://www.cloudflare.com/learning/email-security/what-is-email/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is email? | Email definition 

Electronic mail, or ‘email,’ is a digital communication method that uses electronic devices to deliver messages. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define ‘email’ 
  * Understand the risks of sending and receiving emails 
  * Learn how to practice good email security hygiene 



Related content  [ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ What is the Simple Mail Transfer Protocol (SMTP)? ](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[ What is email spoofing? ](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)[ How to stop spam emails ](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[ How to prevent phishing ](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)

On this page

  * What is email?

  * How does email work?

  * What are the parts of an email?

    * SMTP envelope

    * Header

    * Body

  * What is an email client?

  * What is an email address?

    * Local-part

    * Domain

  * Is email secure?

  * How does Cloudflare help secure email?




## What is email?

Electronic mail, commonly shortened to “email,” is a communication method that uses electronic devices to deliver messages across computer networks. "Email" refers to both the delivery system and individual messages that are sent and received.

Email has existed in some form since the 1970s, when programmer Ray Tomlinson created a way to transmit messages between computer systems on the Advanced Research Projects Agency Network (ARPANET). Modern forms of email became available for widespread public use with the development of email client software (e.g. Outlook) and web browsers, the latter of which enables users to send and receive messages over the Internet using web-based email clients (e.g. Gmail).

Today, email is one of the most popular methods of digital communication. Its prevalence and security vulnerabilities also make it an appealing vehicle for cyber attacks like [phishing](https://www.cloudflare.com/learning/access-management/phishing-attack/), [domain spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/), and [business email compromise (BEC)](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/).

## How does email work?

Email messages are sent from software programs and web browsers, collectively referred to as email ‘clients.’ Individual messages are routed through multiple servers before they reach the recipient’s email server, similar to the way a traditional letter might travel through several post offices before it reaches its recipient’s mailbox.

Once an email message has been sent, it follows several steps to its final destination:

  * The sender’s mail server, also called a Mail Transfer Agent (MTA), initiates a [Simple Mail Transfer Protocol (SMTP)](https://www.cloudflare.com/learning/email-security/what-is-smtp/) connection.

  * The SMTP checks the email envelope data — the text that tells the server where to send a message — for the recipient’s email address, then uses the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) to translate the domain name into an IP address.

  * The SMTP looks for a [mail exchange (MX)](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/) server associated with the recipient’s domain name. If one exists, the email is forwarded to the recipient’s mail server.

  * The email is stored on the recipient’s mail server and may be accessed via the Post Office Protocol (POP)* or [Internet Message Access Protocol (IMAP)](https://www.cloudflare.com/learning/email-security/what-is-imap/). These two protocols function slightly differently: POP downloads the email to the recipient’s device and deletes it from the mail server, while IMAP stores the email within the email client, allowing the recipient to access it from any connected device.




To continue the postal system analogy, imagine Alice writes a thank-you note to Bob. She hands the letter to the mail carrier (MTA), who brings it to the post office to be sorted. At the post office, a processing clerk (SMTP) verifies the address written on the envelope. If the address appears to be written correctly and corresponds to a location that can receive mail (MX server), another mail carrier delivers the letter to Bob’s mailbox. After picking up the mail, Bob might keep the note in his desk drawer, where he can only access it at that location (POP) or put it in his pocket to read at any location (IMAP).

*_The current version of the POP protocol is named POP3._

Report

2026 Security Signals Report

[Get the report →](https://www.cloudflare.com/lp/security-signals-report/2026/)

## What are the parts of an email?

An individual email is made up of three primary components: the SMTP envelope, the header, and the body.

#### SMTP envelope

The SMTP “envelope” is the data communicated between servers during the email delivery process. It consists of the sender’s email address and the recipient’s email address. This envelope data tells the mail server where to send the message, just as a mail carrier references the address on an envelope in order to deliver a letter to the correct location. During the email delivery process, this envelope is discarded and replaced every time the email is transferred to a different server.

#### Header

Like the SMTP envelope, the email header provides critical information about the sender and recipient. Most of the time, the header matches the information provided in the SMTP envelope, but this may not always be the case. For instance, a scammer may disguise the source of a message by using a legitimate email address in the header of an email. Because the recipient only sees the header and body of an email — not the envelope data — they may not know the message is malicious.

The header may also contain a number of optional fields that allow the recipient to reply to, forward, categorize, archive, or delete the email. Other header fields include the following:

  * The **‘Date’** field contains the date the email is sent. This is a mandatory header field.

  * The **‘From’** field contains the email address of the sender. If the email address is associated with a display name, that may be shown in this field as well. This is also a mandatory header field.

  * The **‘To’** field contains the email address of the recipient. If the email address is associated with a display name, that may be shown in this field as well.

  * The **‘Subject’** field contains any contextual information about the message the sender wants to include. It is displayed as a separate line above the body of an email.

  * The **‘Cc’ (carbon copy)** field allows the sender to send a copy of the email to additional recipients. The recipients marked in the ‘To’ field can see the email address(es) listed in the ‘Cc’ field.

  * The **‘Bcc’ (blind carbon copy)** field allows the sender to send a copy of the email to additional recipients. The recipients marked in the ‘To’ field cannot see the email address(es) listed in the ‘Bcc’ field.




#### Body

The body of an email contains any information the sender wishes to send: text, images, links, videos, and/or other [file attachments](https://www.cloudflare.com/learning/email-security/email-attachments/), provided that they do not exceed the email client’s size restrictions. Alternatively, an email can be sent without any information in the body field.

Depending on the options provided by the email client, the body of an email can be formatted in plain text or HTML. Plain text emails do not contain any special formatting (like non-black font colors) or multimedia (like images). They are compatible with all devices and email clients. HTML emails _do_ allow formatting and multimedia within the body field, though some HTML elements may get flagged as spam by email filtering systems or may not display properly on incompatible devices or clients.

Sign Up

Security & speed with any Cloudflare plan

[Start for free →](https://www.cloudflare.com/plans/)

## What is an email client?

An email client is a software program or web application* that enables users to send, receive, and store emails. Popular email clients include Outlook, Gmail, and Apple Mail.

Software- and web-based email clients each have advantages and disadvantages. Desktop email clients often come with more robust security capabilities, streamline email management across multiple accounts, provide offline access, and allow users to back up emails to their computers. By contrast, web-based clients are usually cheaper and easier to access — since users can log in to their account from any web browser — but are reliant on an Internet connection and can be more susceptible to cyber attacks.

*_Originally, ‘email’ referred to desktop email clients and ‘webmail’ referred to web-based email clients. Today, the term ‘email’ encompasses both systems._

## What is an email address?

An email address is a unique string of characters that identifies an email account, or ‘mailbox,’ where messages can be sent and received. Email addresses are formatted in three distinct parts: a local-part, an “@” symbol, and a [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/).

For example, in the email address **[employee@example.com](mailto:employee@example.com)** , “employee” denotes the local-part and “example.com” denotes the domain.

Imagine addressing a letter: the domain signifies the city where the recipient lives, while the local-part specifies the street and house number at which the letter can be received.

#### Local-part

The local-part tells the server the final location of an email message. It may include a combination of letters, numbers, and certain punctuation marks (like underscores). The maximum number of characters for an email address (including both the local-part and domain) is 320, though the recommended length is capped at 254 characters.

#### Domain

The domain may be a domain name, like example.com, or an IP address, like 192.0.2.0. In the former case, the SMTP protocol uses DNS to translate a domain name into its IP address before delivering the message to the next server.

Like the local-part, the domain also has to adhere to certain formatting requirements established by the Internet Engineering Task Force (IETF). Approved domain names may include a combination of uppercase and lowercase letters, numbers, and hyphens. An email address can also be formatted with an IP address in brackets instead of a domain name, although this is rare. The character limit for a domain name is 63.

## Is email secure?

Although email is often used to exchange confidential information, it is not a secure system by design. This makes it an attractive target for attackers, who may intercept an unencrypted message, spread [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/), or impersonate legitimate organizations. Other email security threats include [social engineering](https://www.cloudflare.com/learning/security/threats/social-engineering-attack/), domain spoofing, [ransomware](https://www.cloudflare.com/learning/security/ransomware/what-is-ransomware/), spam, and more.

One of email’s most significant vulnerabilities is its lack of built-in [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/), leaving the contents of an email visible to any unauthorized party that might intercept or otherwise gain access to the message.

In an attempt to make email more secure, many email clients offer one of two basic encryption capabilities: [Transport Layer Security encryption](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) (or ‘TLS encryption’) and [end-to-end encryption](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/) (or 'E2EE'). During TLS encryption, messages are encrypted during transit (from user to server or server to user), and the email service provider retains possession of the private key used to set up this encryption. The email service provider can therefore see the unencrypted contents of the email. During end-to-end encryption (from user to user), messages can only be decrypted by the sender and recipient of the email.

For a complete rundown of email security best practices, see [What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)

## How does Cloudflare help secure email?

Cloudflare Email Security is a [cloud-based email security solution](https://www.cloudflare.com/sase/use-cases/email-security-services/) that helps prevent a number of email threats, including phishing, malware, [Business Email Compromise (BEC)](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/), and email supply chain attacks. It uses robust [machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) models to identify risks before they reach user inboxes, and integrates with common cloud email providers to enhance existing detection and mitigation capabilities.

Learn how Cloudflare helps [enhance email security](https://www.cloudflare.com/sase/products/email-security/).
