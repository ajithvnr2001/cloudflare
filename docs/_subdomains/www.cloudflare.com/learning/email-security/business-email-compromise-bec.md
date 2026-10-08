---
url: https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/
title: What is business email compromise (BEC)?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:01.436287+00:00
---

# What is business email compromise (BEC)?

> Source: https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is business email compromise (BEC)? 

Business email compromise (BEC) is an email-based social engineering attack that aims to defraud its victims. BEC attack campaigns often bypass traditional email filters. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define business email compromise (BEC) 
  * List some of the common features of BEC emails 
  * Describe methods for stopping BEC campaigns 



Related content  [ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ How to prevent phishing ](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[ What is email spoofing? ](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)[ How to stop spam emails ](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[ What is the Simple Mail Transfer Protocol (SMTP)? ](https://www.cloudflare.com/learning/email-security/what-is-smtp/)

On this page

  * Article Summary:

  * What is business email compromise?

  * Why are BEC attacks so hard to detect?

  * What do BEC emails usually contain?

  * Do secure email gateways block BEC campaigns?

  * What should users do when they suspect a BEC campaign?

  * What other technical measures can detect and block BEC attacks?

    * Advance phishing infrastructure detection

    * Machine learning analysis

    * Analyzing email threads

    * Natural language processing

  * How does Cloudflare Email Security detect BEC?

  * FAQs

    * Is business email compromise a social engineering attack?

    * What social engineering techniques are common in BEC emails?

    * How does email impersonation work in BEC attacks?

    * How do BEC attackers use urgency and authority to deceive victims?

    * How do attackers personalize BEC emails?

    * What does ‘low-volume attack’ mean in BEC campaigns?

    * Why are BEC emails harder to detect by traditional security tools?

    * How can machine learning help detect BEC attacks?

    * What is a multi-layer security approach for BEC prevention?




## Article Summary:

  * Business email compromise (BEC) is a sophisticated cybercrime where attackers impersonate trusted figures to trick employees into making unauthorized wire transfers or sharing sensitive corporate data.

  * Organizations can prevent BEC by implementing robust email security protocols, such as MFA and DMARC, alongside comprehensive employee training to identify social engineering tactics.

  * Effective protection against business email compromise involves using AI-driven security tools that analyze communication patterns to detect and block fraudulent messages before they reach an inbox.




## What is business email compromise (BEC)?

Business email compromise (BEC) is a type of [social engineering](https://www.cloudflare.com/learning/security/threats/social-engineering-attack/) attack that takes place over [email](https://www.cloudflare.com/learning/email-security/what-is-email/). In a BEC attack, an attacker falsifies an email message to trick the victim into performing some action — most often, transferring money to an account or location the attacker controls. BEC attacks differ from other types of email-based attacks in a couple of key areas:

  * They do not contain [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/), malicious links, or [email attachments](https://www.cloudflare.com/learning/email-security/email-attachments/)

  * They target specific individuals within organizations

  * They are personalized to the intended victim and often involve advance research of the organization in question




BEC attacks are particularly dangerous because they do not contain malware, malicious links, dangerous email attachments, or other elements an [email security](https://www.cloudflare.com/learning/email-security/what-is-email-security/) filter might identify. Emails used in a BEC attack typically contain nothing but text, which helps attackers camouflage them within normal email traffic.

In addition to bypassing email security filters, BEC emails are specifically designed to trick the recipient into opening them and taking action based on the message they contain. Attackers use personalization to tailor the email to the targeted organization. The attacker might impersonate someone the intended victim corresponds with regularly over email. Some BEC attacks even take place in the middle of an already-existing email thread.

Usually, an attacker will impersonate someone higher up in the organization to motivate the victim into carrying out the malicious request.

## Why are BEC attacks so hard to detect?

Other reasons BEC attacks are difficult to pinpoint may include the following:

  * **They are low-volume:** Unusual spikes in email traffic can alert email security filters to an attack in progress. But BEC attacks are extremely low-volume, often consisting of only one or two emails. They can be carried out without generating a spike in email traffic. This low volume enables a BEC campaign to regularly change its source IP address as well, making it harder to block the campaign.

  * **They use a legitimate source or domain:** Large-scale [phishing attacks](https://www.cloudflare.com/learning/access-management/phishing-attack/) often come from [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) that are quickly blocklisted. BEC attacks, because they are low volume, can use IP addresses that have a neutral or good reputation as their source. They also use [email domain spoofing](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/) to make it seem as if the emails come from a real person.

  * **They may actually come from a legitimate email account:** BEC attacks may use a previously compromised email inbox to send their malicious messages on a person's behalf without their knowledge, so the email may actually be coming from a legitimate email address. (This requires significantly more effort on the part of the attacker, but such an expenditure of focused effort is characteristic of BEC campaigns.)

  * **They pass DMARC checks:** Domain-based Message Authentication, Reporting and Conformance ([DMARC](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)) is a protocol for identifying emails that are sent from a domain without authorization. It helps prevent impersonation of a domain. BEC campaigns can pass DMARC for a couple of reasons: 1) organizations may not have configured DMARC to strictly block emails; 2) attackers may send emails from a legitimate source.




## What do BEC emails usually contain?

Usually, BEC emails contain a few lines of text and do not include links, attachments, or images. In those few lines, they aim to get the target to take the action they desire, whether that is transferring funds to a specific account or granting unauthorized access to protected data or systems.

Other common elements of a BEC email may include:

  * **Time sensitivity:** Words like "urgent," "quick," "reminder," "important," and "soon" often appear in BEC emails, especially in the subject line, to get the recipient to act as quickly as possible — before they realize they may be the target of a scam.

  * **Authoritative sender:** BEC attackers pose as someone important in the organization: the CFO or CEO, for example.

  * **Thorough impersonation of sender:** BEC emails may impersonate legitimate senders (e.g. an organization's CFO) by spoofing their email address, imitating the individual's writing style, or using other tactics to trick their victim.

  * **Providing a reason for the request:** Sometimes, to add legitimacy to what may be an unusual request, a BEC email will provide some reason for why the action is necessary. This also adds urgency to the request.

  * **Specific instructions:** Attackers provide clear instructions such as where the money is going and how much should be sent — a specific amount is more likely to sound legitimate. Attackers may include this information in the initial email, or in a follow-up email if the victim replies.

  * **Directions not to contact the purported sender:** If the intended victim can reach the supposed source of the BEC email over another communications channel, they may be able to identify the email as fake. To prevent this, attackers often instruct the victim not to contact the sender or confirm the request with anyone else, perhaps in the name of acting quickly.




## Do secure email gateways (SEGs) block BEC campaigns?

[A secure email gateway (SEG)](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/) is an [email security service](https://www.cloudflare.com/sase/use-cases/email-security-services/) that sits in between email providers and email users. They identify and filter out potentially malicious emails, just as a [firewall](https://www.cloudflare.com/learning/security/what-is-a-firewall/) removes malicious network traffic. SEGs offer additional protection on top of the built-in security measures that most email providers already offer (Gmail and Microsoft Outlook, for instance, have some basic protections already in place).

However, traditional SEGs struggle to detect well-constructed BEC campaigns for the reasons described above: low volume, lack of obviously malicious content, a seemingly legitimate source for the email, and so on.

For this reason, user training and additional email security measures are highly important for thwarting business email compromise.

## What should users do when they suspect a BEC campaign?

Unusual, unexpected, or sudden requests are a sign of a potential BEC attack. Users should report potential BEC messages to security operations teams. They can also double-check with the purported source of the email.

Imagine Accountant Bob receives an email from CFO Alice:

_Bob,_

_I need to send a customer some gift cards to their favorite pizza restaurant. Please purchase $10,000 in pizza gift cards and transfer them to this customer's email address:[customer@example.com](mailto:customer@example.com)_

_Please do this quickly. This is HIGHLY time-sensitive. We do not want to lose this customer._

_I am boarding a plane and will be out of reach for the next several hours._

_-Alice_

This request strikes Bob as unusual: delivering pizza gift cards to customers is not typically the job of the accounting department. He calls Alice, just in case she has not yet "boarded a plane." She picks up the phone and is unaware of the request she has supposedly just sent to him. Neither is she boarding a plane. Bob has just detected a BEC attack.

## What other technical measures can detect and block BEC attacks?

#### Advance phishing infrastructure detection

Some email security providers crawl the web in advance to detect command and control (C&C) servers, fake websites, and other elements attackers will use in a BEC campaign or phishing attack. This requires using [web crawler bots](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/) to scan large swaths of the Internet (search engines also use web crawler bots, but for different purposes). Identifying attack infrastructure in advance enables the provider to block the illegitimate emails right when they are sent, even if they might otherwise make it through security filters.

#### Machine learning analysis

[Machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) is a way to automate the process of predicting outcomes based on a large data set. It can be used to detect out-of-the-ordinary activity — for example, [Cloudflare Bot Management](https://www.cloudflare.com/application-services/products/bot-management/) uses machine learning as one method for identifying [bot](https://www.cloudflare.com/learning/bots/what-is-a-bot/) activity. For stopping BEC attacks, machine learning can help identify unusual requests, atypical email traffic patterns, and other anomalies.

#### Analyzing email threads

Since BEC attackers often try to reply to an existing thread to add legitimacy to their emails, some email security providers monitor threads to see if the "from" or "to" emails within a thread are changed suddenly.

#### Natural language processing

This means looking for key phrases within emails to learn what topics a given set of email contacts typically correspond about. For instance, it could be possible to track who a given person in an organization corresponds with about money transfers, customer relations, or any other topic. If Bob's received emails (from the example above) rarely deal with customer relations, the inclusion of phrases like "a customer" and "lose this customer" in the email from "Alice" could be a signal that the email is part of a BEC attack.

## How does Cloudflare Email Security detect BEC?

Cloudflare Email Security is designed to catch BEC attacks that most SEGs cannot detect. It does so using many of the methods described above: crawling the Internet for attack infrastructure, employing machine learning analysis, analyzing email threads, analyzing email content, and so on.

Email remains one of the biggest [attack vectors](https://www.cloudflare.com/learning/security/glossary/attack-vector/), making email security ever more crucial for organizations today. [Learn more about how Cloudflare Email Security works](https://www.cloudflare.com/sase/products/email-security/).

## FAQs

#### Is business email compromise (BEC) a social engineering attack?

A social engineering attack manipulates people into taking an action that favors the attacker. Business email compromise (BEC) is a social engineering attack that uses email to trick its victims — often into sending money or sensitive data to the attacker. BEC emails rely almost exclusively on manipulative social engineering techniques, so they do not usually contain the typical markers of a malicious email — such as dangerous links or untrusted attachments.

#### What social engineering techniques are common in BEC emails?

BEC emails often include plausible reasons for the unexpected requests. They inspire urgency in their recipients. The senders impersonate people of authority. And BEC emails discourage verification, urging their recipients not to check in with the purported sender before they take action. Combined, these techniques can get well-meaning people to take action before they have time to think. For instance, a scammer might pretend to be the CEO of the recipient's company and demand that the recipient transfer money into an account, or else they will be fired.

#### How does email impersonation work in BEC attacks?

In BEC attacks, the attacker pretends to be a trusted person — often a company executive — by spoofing email addresses or imitating writing styles, making their requests appear legitimate to the victim.

#### How do BEC attackers use urgency and authority to deceive victims?

Attackers create a sense of urgency, using words like “urgent,” “important,” or "reminder," and pose as high-ranking officials to pressure recipients into acting quickly without verifying the request.

#### How do attackers personalize BEC emails?

Attackers research organizations and individuals to craft tailored messages, often referencing real projects or people to make the email seem more believable.

#### What does ‘low-volume attack’ mean in BEC campaigns?

BEC attacks are low-volume, often involving just one or two emails. This makes them harder to detect, as there’s no spike in email traffic that would trigger security alerts.

#### Why are BEC emails harder to detect by traditional security tools?

BEC emails rarely contain malware, links, or attachments. To make the emails more believable, attackers may send them from trusted mail servers or email addresses. Since they often consist of plain text and mimic regular email traffic, traditional filters struggle to identify them as threats.

#### How can machine learning help detect BEC attacks?

Advanced security solutions use machine learning to analyze typical email traffic and identify anomalies that could indicate a BEC attack.

#### What is a multi-layer security approach for BEC prevention?

Effective BEC prevention combines technical defenses (like machine learning and email monitoring), user training, and processes for independent verification of unusual requests.
