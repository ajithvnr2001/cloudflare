---
url: https://www.cloudflare.com/learning/email-security/what-is-smtp/
title: What is the Simple Mail Transfer Protocol (SMTP)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:13.010104+00:00
---

# What is the Simple Mail Transfer Protocol (SMTP)?

> Source: https://www.cloudflare.com/learning/email-security/what-is-smtp/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is the Simple Mail Transfer Protocol (SMTP)? 

The Simple Mail Transfer Protocol (SMTP) is a networking standard for sending emails. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how the Simple Mail Transfer Protocol (SMTP) works 
  * Understand SMTP commands, servers, and envelopes 
  * Define Extended SMTP (ESMTP) 



Related content  [ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ What is email? | Email definition ](https://www.cloudflare.com/learning/email-security/what-is-email/)[ How to stop spam emails ](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[ How to prevent phishing ](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[ What is email spoofing? ](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

On this page

  * What is the Simple Mail Transfer Protocol?

  * How does SMTP work?

  * What is an SMTP envelope?

  * What are SMTP commands?

  * What is an SMTP server?

  * What port does SMTP use?

  * SMTP vs. IMAP and POP

  * What is Extended SMTP?

  * What is Cloudflare Email Routing?




## What is the Simple Mail Transfer Protocol (SMTP)?

The Simple Mail Transfer Protocol (SMTP) is a technical standard for transmitting electronic mail ([email](https://www.cloudflare.com/learning/email-security/what-is-email/)) over a network. Like other [networking protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/), SMTP allows computers and servers to exchange data regardless of their underlying hardware or software. Just as the use of a standardized form of addressing an envelope allows the postal service to operate, SMTP standardizes the way email travels from sender to recipient, making widespread email delivery possible.

SMTP is a mail delivery protocol, not a mail retrieval protocol. A postal service delivers mail to a mailbox, but the recipient still has to retrieve the mail from the mailbox. Similarly, SMTP delivers an email to an email provider's mail server, but separate protocols are used to retrieve that email from the mail server so the recipient can read it.

## How does SMTP work?

All networking protocols follow a predefined process for exchanging data. SMTP defines a process for exchanging data between an email client and a mail server. An email client is what a user interacts with: the computer or web application where they access and send emails. A mail server is a specialized computer for sending, receiving, and forwarding emails; users do not interact directly with mail servers.

Here is a summary of what passes between the email client and the mail server for an email to begin sending:

  * **SMTP connection opened:** Since SMTP uses the Transmission Control Protocol (TCP) as its transport protocol, this first step begins with a TCP connection between client and server. Next, the email client begins the email sending process with a specialized "Hello" command (HELO or EHLO, described below). **Email data transferred:** The client sends the server a series of commands accompanied with the actual content of the email: the email header (including its destination and subject line), the email body, and any additional components. **Mail Transfer Agent (MTA):** The server runs a program called a Mail Transfer Agent (MTA). The MTA checks the domain of the recipient's email address, and if it differs from the sender's, it queries the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) to find the recipient's [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). This is like a post office looking up a mail recipient's zip code. **Connection closed:** The client alerts the server when transmission of data is complete, and the server closes the connection. At this point the server will not receive additional email data from the client unless the client opens a new SMTP connection.



Usually, this first email server is not the actual email's final destination. The server, having received the email from the client, repeats this SMTP connection process with another mail server. That second server does the same, until finally the email reaches the recipient's inbox on a mail server controlled by the recipient's email provider.

Compare this process to the way a piece of mail travels from sender to recipient. A mail carrier does not take a letter directly from the sender to its recipient. Instead, the mail carrier brings the letter back to their post office. The post office ships the letter to another post office in another town, then another, and so on until the letter reaches the recipient. Similarly, emails go from server to server via SMTP until they arrive at the recipient's inbox.

## What is an SMTP envelope?

The SMTP "envelope" is the set of information that the email client sends the mail server about where the email comes from and where it is going. The SMTP envelope is distinct from the email header and body and is not visible to the email recipient.

## What are SMTP commands?

SMTP commands are predefined text-based instructions that tell a client or server what to do and how to handle any accompanying data. Think of them as buttons the client can press to get the server to accept data correctly.

  * `HELO/EHLO`: These commands say "Hello" and start off the SMTP connection between client and server. "`HELO`" is the basic version of this command; "`EHLO`" is for a specialized type of SMTP.

  * `MAIL FROM`: This tells the server who is sending the email. If Alice were trying to email her friend Bob, a client might send "MAIL FROM:[alice@example.com](mailto:alice@example.com)".

  * `RCPT TO`: This command is for listing the email's recipients. A client can send this command multiple times if there are multiple recipients. In the example above, Alice's email client would send "RCPT TO:[bob@example.com](mailto:bob@example.com)".

  * `DATA`: This precedes the content of the email, like:



    
    
    `
    DATA
    Date: Mon, 4 April 2022
    From: Alice alice@example.com
    Subject: Eggs benedict casserole
    To: Bob bob@example.com
    
    Hi Bob,
    I will bring the eggs benedict casserole recipe on Friday.
    -Alice
    .
    `
    

  * `RSET`: This command resets the connection, removing all previously transferred information without closing the SMTP connection. `RSET` is used if the client sent incorrect information.

  * `QUIT`: This ends the connection.




## What is an SMTP server?

An SMTP server is a mail server that can send and receive emails using the SMTP protocol. Email clients connect directly with the email provider's SMTP server to begin sending an email. Several different software programs run on an SMTP server:

  * **Mail submission agent (MSA):** The MSA receives emails from the email client.

  * **Mail transfer agent (MTA):** The MTA transfers emails to the next server in the delivery chain. As described above, it may query the DNS to find the recipient domain's [mail exchange (MX) DNS record](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/) if necessary.

  * **Mail delivery agent (MDA):** The MDA receives emails from MTAs and stores them in the recipient's email inbox.




## What port does SMTP use?

In networking, a [port](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) is the virtual point where network data is received; think of it as the apartment number in the address of a piece of mail. Ports help computers sort networking data to the correct applications. [Network security](https://www.cloudflare.com/learning/network-layer/network-security/) measures like [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/) can block unnecessary ports to prevent the sending and receiving of malicious data.

Historically, SMTP only used port 25. Today, [port 25 is still in use for SMTP, but it can also use ports 465, 587, and 2525](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/).

  * **Port 25** is most used for connections between SMTP servers. Firewalls for end user networks often block this port today, since spammers try to abuse it to send large amounts of spam.

  * **Port 465** was once designated for use by SMTP with [Secure Sockets Layer (SSL)](https://www.cloudflare.com/learning/ssl/what-is-ssl/) encryption. But SSL was replaced by [Transport Layer Security (TLS)](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), and modern email systems therefore do not use this port. It only appears in legacy (outdated) systems.

  * **Port 587** is now the default port for email submission. SMTP communications via this port use TLS encryption.

  * **Port 2525** is not officially associated with SMTP, but some email services offer SMTP delivery over this port in case the above ports are blocked.




## SMTP vs. IMAP and POP

The [Internet Message Access Protocol (IMAP)](https://www.cloudflare.com/learning/email-security/what-is-imap/) and Post Office Protocol (POP) are used to deliver the email to its final destination. The email client has to retrieve email from the final mail server in the chain in order to display the email to the user. The client uses IMAP or POP instead of SMTP for this purpose.

To understand the difference between SMTP and IMAP/POP, consider the difference between a plank of wood and a rope. A length of wood can be used to push something forward, but not pull it in. A rope can pull an item, but cannot push it. Similarly, SMTP "pushes" email to a mail server, but IMAP and POP "pull" it the rest of the way to the user's application.

## What is Extended SMTP (ESMTP)?

Extended Simple Mail Transfer Protocol (ESMTP) is a version of the protocol that expands upon its original capabilities, enabling the sending of email attachments, the use of TLS, and other capabilities. Almost all email clients and email services use ESMTP, not basic SMTP.

ESMTP has some additional commands, including "`EHLO`", an "extended hello" message that enables the use of ESMTP at the start of the connection.

## What is Cloudflare Email Routing?

Cloudflare Email Routing is designed to simplify creating and managing email addresses, without needing to keep an eye on additional mailboxes. With Email Routing, users can create any number of custom email addresses to use in situations where they do not want to share their primary email address. Emails are then routed to their preferred email inbox, without ever having to expose the primary email address.

Cloudflare Email Routing works by modifying the SMTP envelope of an email, leaving the header and body unaltered. To learn more, [read our blog post](https://blog.cloudflare.com/introducing-email-routing/).
