---
url: https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/
title: What is a mail server?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:47.112555+00:00
---

# What is a mail server?

> Source: https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is a mail server? 

A mail server sends and receives email messages using outgoing and incoming email protocols. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define ‘mail server’ 
  * Understand how a mail server works 
  * Learn which email protocols mail servers use 



Related content  [ What is email? | Email definition ](https://www.cloudflare.com/learning/email-security/what-is-email/)[ What is the Simple Mail Transfer Protocol (SMTP)? ](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[ What is IMAP? ](https://www.cloudflare.com/learning/email-security/what-is-imap/)[ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ What is a secure email gateway (SEG)? ](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)

On this page

  * What is a mail server?

  * What is a mail client?

  * How do mail servers deliver email messages?

  * What is the difference between a mail client and a mail server?

  * Is an email provider a mail client or a mail server?

  * Do mail servers block malicious email messages?




## What is a mail server?

A mail server (sometimes called an email server) is a software program that sends and receives email. Often, it is used as a blanket term for both mail transfer agents (MTA) and mail delivery agents (MDA), each of which perform a slightly different function.

Mail servers play a crucial role in the email delivery process. Without them, users would have no way of transferring those messages to and from other mail clients.

## What is a mail client?

Mail servers send messages from one mail client to another. A mail client (also called an _email client_ or _message user agent_) is a web-based or desktop application that receives and stores email messages. Some of the most widely-used mail clients include Microsoft Outlook, Gmail, and Apple Mail.

## How do mail servers deliver email messages?

Email messages are sent and received using two types of mail servers: outgoing mail servers, or _mail transfer agents_ (MTA), and incoming mail servers, or _mail delivery agents_ (MDA). MTAs retrieve outgoing email messages from the sender’s mail client, then deliver them to MDAs, which are responsible for temporarily storing and delivering email messages to the recipient’s mail client.

Mail servers deliver email messages between mail clients by using email [protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/), which tell the server how to process incoming requests, where to forward the messages, and how to deliver them to the intended mail client.

When sending an email from one client to another, the MTA uses an outgoing mail protocol, like the [Simple Mail Transfer Protocol (SMTP)](https://www.cloudflare.com/learning/email-security/what-is-smtp/), to check the sender’s email envelope* data and determine where the message needs to be sent. SMTP does this by using the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) to translate the recipient’s domain into an [IP address](https://www.cloudflare.com/learning/network-layer/internet-protocol/).

Then, it locates a mail delivery agent by querying [mail exchange (MX)](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/) records. The MX record tells the server how to route the message to its final destination. Once the MX record returns the appropriate destination, the MDA uses an incoming mail protocol, like the [Internet Message Access Protocol (IMAP)](https://www.cloudflare.com/learning/email-security/what-is-imap/) or Post Office Protocol Version 3 (POP3), to retrieve the email message from the mail server and deliver it to the specified mail client (or clients).

For an in-depth explanation of the email delivery process, see [What is email?](https://www.cloudflare.com/learning/email-security/what-is-email/)

*_An_ email envelope _contains the sender and recipient’s email addresses, among other data SMTP needs in order to transfer an email message from server to server._

## What is the difference between a mail client and a mail server?

While mail clients and mail servers are both used to send and receive email messages, they are not the same. A mail client is an application that allows users to retrieve, store, and format emails to be sent. Mail servers, meanwhile, are software programs that use email protocols to move email messages between mail clients.

To illustrate this difference, imagine that Alice wants to send Carol a letter. Alice addresses the letter to Carol, then leaves it in their mailbox. A postal worker retrieves the letter from the mailbox and delivers it to a post office, where it is sorted and transferred to the correct location. Finally, another postal worker delivers the letter to Carol’s mailbox, where it can be stored until they are ready to retrieve it.

Similarly, a user may write and address an email to its intended recipient (or recipients), but the mail server, like the postal worker, is responsible for accepting the message, transferring it to an incoming mail server, then delivering it to the correct inbox, where it is stored.

## Is an email provider a mail client or a mail server?

Most email providers offer mail client services to their users. While email providers rely on mail servers to exchange messages between clients, they do not always make mail servers available to users as a free or paid service.

For example, consider two popular email providers: Google and Apple. As of 2023, Google offers both a mail client (Gmail) and mail server (Gmail SMTP Server). Gmail allows users to store, retrieve, and send emails, while Gmail SMTP Server gives users access to a wider range of features, like sending email messages from third-party clients (e.g. Microsoft Outlook). Apple, on the other hand, only provides a mail client called Apple Mail.

## Do mail servers block malicious email messages?

Because any type of message can be sent over email, attackers often use it to send phishing messages, malware, or other dangerous content. Most mail servers do little to prevent attacks like this, aside from ensuring that emails came from the location that they claim to be from (via DKIM, DMARC, and SPF).

To solve for this [security gap](https://www.cloudflare.com/learning/email-security/what-is-email-security/), some email providers scan emails for suspicious elements, filter spam, and implement encryption to prevent attackers from accessing and manipulating messages.

Cloudflare Email Security is a [cloud-based email security solution](https://www.cloudflare.com/sase/use-cases/email-security-services/) that preemptively blocks phishing attempts, quarantines fraudulent communications, and blocks campaigns across a wide range of attack vectors. Learn more about [Cloudflare Email Security](https://www.cloudflare.com/sase/products/email-security/).
