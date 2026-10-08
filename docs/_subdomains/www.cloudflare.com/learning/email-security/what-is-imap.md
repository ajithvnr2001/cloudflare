---
url: https://www.cloudflare.com/learning/email-security/what-is-imap/
title: What is IMAP?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:04.150713+00:00
---

# What is IMAP?

> Source: https://www.cloudflare.com/learning/email-security/what-is-imap/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is IMAP? 

Internet message access protocol (IMAP) is a protocol for receiving email that allows users to access their emails from different devices. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain what IMAP is 
  * Compare and contrast IMAP and POP3 
  * Understand IMAP's security vulnerabilities 



Related content  [ What is the Simple Mail Transfer Protocol (SMTP)? ](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[ What is business email compromise (BEC)? ](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[ What is email? | Email definition ](https://www.cloudflare.com/learning/email-security/what-is-email/)[ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ What is email spoofing? ](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

On this page

  * What is IMAP?

  * What is POP3?

  * IMAP vs. POP3

  * How does sending and receiving emails work with IMAP?

  * What are some of the security considerations for IMAP?

  * How does Cloudflare help secure email?




## What is IMAP?

The Internet Message Access Protocol (IMAP) is a protocol for receiving [email](https://www.cloudflare.com/learning/email-security/what-is-email/). [Protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) standardize technical processes so computers and servers can connect with each other regardless of whether or not they use the same hardware or software.

A key feature of IMAP is that it allows users to access their emails from any device. This is because IMAP acts as an intermediary between email servers and email clients, rather than downloading emails from the server onto the email client.

Compare this aspect of IMAP to the differences between using Microsoft Word and Google Docs. Microsoft Word documents are saved locally to a computer and can be transported via email attachments or USB drives, but they do not update dynamically. If, for example, Sally makes changes to their Word document, those modifications are only saved to Sally's computer (and not to the version Linda might have on her computer).

By comparison, Google Docs can be accessed via the Internet on different devices, and update dynamically when a user makes changes to a file. In this scenario, any change Sally makes to a shared file would be visible to Linda, even if they use different computers to access the same document.

Similarly, using IMAP, users can access their email accounts from different devices without any differences in experience, and do not necessarily need to be on the device where they originally read the email.

## What is POP3?

Post Office Protocol Version 3 (POP3) is an alternative protocol for receiving emails that downloads emails from the server to a local device. Using POP3, a recipient cannot access their emails again from a different device because they are stored locally and then deleted from the email server.

## IMAP vs. POP3

Here is a summary of some key differences between IMAP and POP3.

IMAP POP3

Users can access their emails from any device. By default, emails can only be accessed from the device they are downloaded on.

The server stores emails; IMAP acts as an intermediary between the server and the client. Once downloaded, emails are deleted from the server, unless otherwise configured.

Emails are not accessible offline. Emails are accessible offline but only on the device they were downloaded on.

The bodies of emails are not downloaded until a user clicks on them, but subject lines and sender names populate quickly in the email client. Emails are downloaded to the device by default, so messages may take longer to load.

IMAP requires more server space because emails are not automatically deleted from the server. POP3 conserves email server storage because emails are automatically deleted from the server.

## How does sending and receiving emails work with IMAP?

Here is a quick look at the process of sending and receiving emails with IMAP*:

**Sending emails:** The [Simple Mail Transfer Protocol (SMTP)](https://www.cloudflare.com/learning/email-security/what-is-smtp/) defines how emails are sent.

  * A [Transmission Control Protocol (TCP)](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) connection is set up between the client and email server. This connection lets the server know to expect an email.

  * The client sends a series of commands to the server, which include the email itself.

  * The email server uses its own program called the mail transfer agent (MTA) to check the email’s [domain name system (DNS) record](https://www.cloudflare.com/learning/dns/dns-records/) and find the recipient’s [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). The MTA translates the DNS record into an IP address so that it knows where to send the emails.

  * SMTP looks for a [mail exchange (MX) record](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/) associated with the recipient’s [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/). (The MX record is used to indicate how messages should be routed in accordance with SMTP.) If there is an MX record, then the email is sent to the corresponding email server.




**Retrieving emails:** IMAP defines how emails are received.

  * The email can be accessed within the email client and can be read from any device. Because IMAP is an intermediary between the email client and server, these emails can only be accessed with an Internet connection.

  * When a user signs in to their email client, the client connects with the email server to retrieve their messages. The user can see a preview of the email (with the subject line and sender information) but the actual message is not downloaded until a user clicks on the message.

  * The inbox owner’s emails will be available via the server and client connection until they are deleted.




*_Note that for the purposes of this example, IMAP is used to describe retrieving emails. However, this process looks slightly different when POP3 is implemented._

## What are some of the security considerations for IMAP?

With IMAP, emails are stored on the server by default, which could present issues if the server is compromised. However, unlike with POP3, IMAP users do not have to worry about their emails being destroyed if the device they are downloaded on is lost or damaged.

One of the biggest security issues with IMAP is that it transmits logins from the client to the server in plain text by default, meaning usernames and passwords are not [encrypted](https://www.cloudflare.com/learning/ssl/what-is-encryption/). (An encrypted login is obscured using complex mathematical equations so an attacker would not be able to understand it just by reading it.) This vulnerability can be protected against by configuring IMAP over the [transport layer security (TLS) protocol](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), which facilitates encrypted communication.

Another vulnerability associated with IMAP is that it is not inherently compatible with [multi-factor authentication (MFA)](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/). For this reason, IMAP can be exploited to [bypass MFA requirements](https://www.cloudflare.com/the-net/bypassing-mfa/) and make it easier for attackers to successfully conduct password-spraying attacks. (In password spraying, the attacker attempts different combinations of commonly used passwords and potential usernames.) Using third-party email clients that do not support authentication requirements or maintaining shared email accounts that cannot enforce MFA make organizations particularly vulnerable.

## How does Cloudflare help secure email?

Cloudflare offers an [Email Security service](https://www.cloudflare.com/sase/products/email-security/) solution that proactively identifies [phishing](https://www.cloudflare.com/learning/access-management/phishing-attack/) and other email-based attacks using machine learning. By integrating with common email providers, it improves upon existing protections against password-spraying and other attacks that IMAP can be vulnerable to.
