---
url: https://www.cloudflare.com/learning/email-security/what-is-email-routing/
title: What is email routing?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:00.674074+00:00
---

# What is email routing?

> Source: https://www.cloudflare.com/learning/email-security/what-is-email-routing/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is email routing? 

Email routing allows users to send different types of emails (such as marketing, transactional, or administrative) to separate accounts based on criteria such as the recipient’s address or department. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define email routing 
  * Explain why email routing is important and how to use it in different applications 
  * How Cloudflare Email Routing can enhance email experiences 



Related content  [ What is email? | Email definition ](https://www.cloudflare.com/learning/email-security/what-is-email/)[ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ When are email attachments safe to open? ](https://www.cloudflare.com/learning/email-security/email-attachments/)[ What is email encryption? ](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[ What is business email compromise (BEC)? ](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)

On this page

  * What is email routing?

  * How does email routing work?

  * Why is email routing important?

  * What are different ways to use email routing?

  * The anatomy of an email - and how email routing fits in

  * How does Cloudflare support email routing?




## What is email routing?

Email routing is the process of ensuring that the right messages get to the right recipients. It allows users to send different types of emails to separate accounts based on criteria such as the recipient’s address or department.

## How does email routing work?

Email routing is a process that helps send email messages from one inbox to another. Email essentially operates like a digital post office — he sender mails a letter, it goes into a series of trucks, and then arrives at the recipient’s mailbox. In a real-world postal context, individuals and businesses can set up various guidelines to determine which letters are routed or redirected to which people. Email routing works in the same way.

The first element of email routing is the relationship between the sender and the recipient. Sender-based routing assigns an email address to individual user accounts, and emails sent from within that account are routed accordingly. This type of system is usually used when one department within an organization uses its own domain (for example, @SalesTeam-CompanyName.com) for sending internal messages, but other departments (such as @companyname.com) use their company’s primary domain name.

Meanwhile, receiver-based routing relies on filters to determine which addresses should receive which type of message based on certain criteria (such as contact information). When a message is received by a filter server, it compares the sender’s IP address with the list of known recipients stored in memory or in a database. If it matches someone who should receive that kind of message, then the message is filtered and forwarded to them.

The second element of email routing is the pathway an email may take. Email routing can use inline, deferred, or transport-level forwarding pathways. Inline routing ties together individual mailboxes within a domain into an “inline flow.” An “inline flow” is the system that touches that email from the sender to the recipient. Deferred routing sends all incoming messages directly to a mailbox specified by the sender or contact, bypassing any other mailboxes in between and transport-level forwarding routes all emails sent through a specific transport server instead of going out through the general delivery system on the network.

## Why is email routing important?

Email routing is important because it ensures that the right messages get to the right individuals. Email routing streamlines the inbox and allows users to send different types of emails (such as marketing, transactional, or administrative) to separate accounts based on criteria such as the recipient’s address or department.

**For businesses:** Organizations prefer different email addresses for different types of inquiries, but find it difficult to control the recipients of these emails. As the business evolves, so do the types of inquiries. By configuring mailboxes and aliases quickly, companies can enhance business efficiency and increase productivity.

**For individual users:** Email routing enables individuals to create custom addresses for a variety of needs, so that they are not sharing private email addresses with newsletters, businesses or ecommerce sites. Email routing reduces clutter and may protect users from excessive marketing emails.

**For families:** With a family-specific domain, users can create custom addresses for each family member or for specific purposes, such as custom addresses for household bills.

## What are different ways to use email routing?

There are a variety of ways to use email routing. The below are just a few:

  * **Automate actions with triggers:** Automatically sending certain messages to specific recipients based on predetermined conditions. This can save time by ensuring that important messages reach the right people at the right time without having to search through inboxes.

  * **Create custom filters:** Creating customized filters for incoming mail so that only the emails that users want to see appear in their inboxes. This allows users to manage their mail load more effectively.

  * **Set up mailbox rules:** To specify how incoming mail should be handled — e.g. filed away immediately, sent directly to another folder, or deleted completely.

  * Configure server settings: Configure settings so that outgoing emails go through multiple services before reaching the final destination. This can help ensure that the message reaches its destination without errors or delays.

  * **Customer relationship management (CRM) segmentation:** Use segmentation from CRM systems or customer data to create targeted marketing campaigns. Users can tailor email content to specific audience segments based on unique preferences and interaction history.




## The anatomy of an email - and how email routing fits in

![Comparison between snail mail and email](https://images.ctfassets.net/slt3lc6tev37/4Y6fSnNq9K6UD8RdwtHxFA/7f34d6d3dd44516615ffb6f60fcc2cc2/snail-mail-vs-email.png)Comparison between snail mail and email

 _Image description: This image shows the technology behind an email, including the envelope and body and compares it to snail postage letters._

An email consists of the envelope, the header, and its body:

  * The envelope is part of the [Simple Mail Transfer Protocol (SMTP)](https://www.cloudflare.com/learning/email-security/what-is-smtp/) and tells the servers where the email is coming from and where it is supposed to be delivered. This is where email routing occurs by removing the original recipient and switching or adding the new recipient based on predetermined routing rules.

  * The headers contain information like the message travel path, date, and sender and recipients’ addresses, as well as other technical metadata such as [SPF](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/) pass results, [DKIM](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/) signatures, and [anti-spam](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/) scores. This is where email routing rules are reflected.

  * The body is where the email’s actual message lives. It can be in plain text or HTML, and may contain file attachments or be signed and encrypted. This is the message that is sent to the correct recipient based on email routing configurations.




To dive deeper into SMTP, [view a simplified diagram of how the SMTP protocol works.](https://blog.cloudflare.com/introducing-email-routing/)

![a diagram highlighting SMTP protocol](https://images.ctfassets.net/slt3lc6tev37/3F0NPsOCfq12eEsifj2Lak/184510e4b1dd5266c7e6bbec5fe141da/how-smtp-protocol-works.png)a diagram highlighting SMTP protocol

 _Image description: This diagram outlines how the three steps of an email message fit together._

What you see under “SMTP protocol” are considered “verbs” that the protocol supports. The SMTP Client is the sender, and the SMTP Server is the recipient. When you program email routing protocols, it essentially operates in the “RCPT To:”. This diagram illustrates the journey of an email from send to destination.

## How does Cloudflare support email routing?

Cloudflare Email Routing is a service that acts like an intelligent router at the transport layer, and ensures that SPF, DKIM, and other security or anti-spam protocols remain in place. It allows Cloudflare users to set up custom email addresses for their domains. Messages are received, handled according to the configured rules, and delivered to their final destination. Learn more about [Cloudflare Email Routing.](https://www.cloudflare.com/developer-platform/products/email-routing/)
