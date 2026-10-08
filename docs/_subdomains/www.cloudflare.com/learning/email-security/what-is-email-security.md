---
url: https://www.cloudflare.com/learning/email-security/what-is-email-security/
title: What is email security? | Learning Center
method: crawl4ai+scrapegraph (scrapling: scrapling status 403)
fetched_at: 2026-10-08T08:05:02.705500+00:00
---

# What is email security? | Learning Center

> Source: https://www.cloudflare.com/learning/email-security/what-is-email-security/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  What is email security? 

Email security encompasses the techniques and technologies used to protect email accounts and communications from unauthorized access. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define email security 
  * Identify common email threats 
  * Understand email security best practices 



On this page

  * Article Summary:

  * What is email security?

  * What kinds of attacks occur via email?

    * Email domain spoofing

  * What is a phishing attack?

  * How are email attachments used in attacks?

  * What is spam?

  * How do attackers take over email accounts?

  * How does encryption protect email?

  * How do DNS records help prevent email attacks?

  * How can phishing attacks be stopped?




## Article Summary:

  * Email security protects sensitive information by implementing multi-layered defenses like encryption and authentication to prevent unauthorized access and stop advanced cyber threats from compromising corporate communication channels.
  * Comprehensive threat protection involves blocking diverse attacks, including phishing, malware, and business email compromise, while ensuring that outbound data remains secure through robust data loss prevention measures.
  * Securing email communications requires advanced filtering and cloud-based security layers that detect malicious attachments and fraudulent senders, maintaining a resilient and secure email environment for organizations.



## What is email security?

Email security is the process of preventing [email](https://www.cloudflare.com/learning/email-security/what-is-email/)-based cyber attacks and unwanted communications. It spans protecting inboxes from takeover, protecting domains from [spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/), stopping [phishing attacks](https://www.cloudflare.com/learning/access-management/phishing-attack/), preventing fraud, blocking [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/) delivery, filtering [spam](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/), and using [encryption](https://www.cloudflare.com/learning/ssl/what-is-encryption/) to protect the contents of emails from unauthorized persons.

Security and [privacy](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/) were not built into email when it was first invented, and despite email's importance as a communication method, these are still not built into email by default. As a result, email is a major [attack vector](https://www.cloudflare.com/learning/security/glossary/attack-vector/) for organizations large and small, and for individual people as well.

## What kinds of attacks occur via email?

Some of the common types of email attacks include:

  * **Fraud:** Email-based fraud attacks can take a variety of forms, from the classic advance-fee scams directed at everyday people to [business email compromise (BEC)](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/) messages that aim to trick large enterprise accounting departments into transferring money to illegitimate accounts. Often the attacker will use domain spoofing to make the request for funds look like it comes from a legitimate source.
  * **Phishing:** A phishing attack tries to get the victim to give the attacker sensitive information. Email phishing attacks may direct users to a fake webpage that collects credentials, or simply pressure the user to send the information to an email address secretly controlled by the attacker. Domain spoofing is also common in attacks like these.
  * **Malware:** Types of malware delivered over email include spyware, scareware, adware, and [ransomware](https://www.cloudflare.com/learning/security/ransomware/what-is-ransomware/), among others. Attackers can deliver malware via email in several different ways. One of the most common is including an email attachment that contains malicious code.
  * **Account takeover:** Attackers take over email inboxes from legitimate users for a variety of purposes, such as monitoring their messages, stealing information, or using legitimate email addresses to forward malware attacks and spam to their contacts.
  * **Email interception:** Attackers can intercept emails in order to steal the information they contain, or to carry out [on-path attacks](https://www.cloudflare.com/learning/security/threats/on-path-attack/) in which they impersonate both sides of a conversation to each other. The most common method for doing this is monitoring network [data packets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/) on wireless [local area networks (LANs)](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/), as intercepting an email as it transits the Internet is extremely difficult.



Report

2026 Security Signals Report

[Get the report](https://www.cloudflare.com/lp/security-signals-report/2026/)

#### Email domain spoofing

Email domain spoofing is important in several types of email-based attacks, as it allows attackers to send messages from legitimate-seeming addresses. This technique allows attackers to send an email with a forged "from" address. For example, if Chuck wants to trick Bob with an email, Chuck might send Bob an email from the domain "@trustworthy-bank.com," even though Chuck does not really own the domain "trustworthy-bank.com" or represent that organization.

## What is a phishing attack?

Phishing is an attempt to steal sensitive data, typically in the form of usernames, passwords, or other important account information. The phisher either uses the stolen information themselves, for instance to take over the user's accounts with their password, or sells the stolen information.

Phishing attackers disguise themselves as a reputable source. With an enticing or seemingly urgent request, an attacker lures the victim into providing information, just as a person uses bait while fishing.

Phishing often takes place over email. Phishers either try to trick people into emailing information directly, or link to a webpage they control that is designed to look legitimate (for instance, a fake login page where the user enters their password).

There are several types of phishing:

  * _[Spear phishing](https://www.cloudflare.com/learning/access-management/spear-phishing/)_ is highly targeted and often personalized to be more convincing.
  * _Whaling_ targets important or influential persons within an organization, such as executives. This is a major threat vector in enterprise email security.
  * Non-email phishing attacks include _vishing_ (phishing via phone call), _[smishing](https://www.cloudflare.com/learning/access-management/smishing/)_ (phishing via text message), and _social media phishing_.



An email security strategy can include several approaches for blocking phishing attacks. [Email security solutions](https://www.cloudflare.com/sase/use-cases/email-security-services/) can filter out emails from known bad [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/). They can block or remove links embedded within emails to stop users from navigating to phishing webpages. Or, they can use [DNS filtering](https://www.cloudflare.com/learning/access-management/what-is-dns-filtering/) to block these webpages. [Data loss prevention (DLP)](https://www.cloudflare.com/learning/access-management/what-is-dlp/) solutions can also block or redact outgoing messages containing sensitive information. (These capabilities are often bundled in a [SASE](https://www.cloudflare.com/learning/access-management/what-is-sase/) offering.)

Finally, an organization's employees should receive training on [how to recognize a phishing email](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/).

Sign Up

Security & speed with any Cloudflare plan

[Start for free](https://www.cloudflare.com/plans/)

## How are email attachments used in attacks?

[Email attachments](https://www.cloudflare.com/learning/email-security/email-attachments/) are a valuable feature, but attackers use this email capability to send malicious content to their targets, including malware.

One way they can do this is by simply attaching the malicious software as an .exe file, then tricking the recipient into opening the attachment. A far more common approach is to conceal malicious code within an innocent-seeming document, like a PDF or a Word file. Both these file types support the inclusion of code — such as macros — that attackers can use to perform some malicious action on the recipient's computer, like downloading and opening malware.

Many ransomware infections in recent years have started with an email attachment. For example:

  * [Ryuk ransomware](https://www.cloudflare.com/learning/security/ransomware/ryuk-ransomware/) often enters a network through a TrickBot or Emotet infection, both of which spread via email attachments
  * [Maze ransomware](https://www.cloudflare.com/learning/security/ransomware/maze-ransomware/) uses email attachments to gain a foothold within the victim's network
  * [Petya ransomware](https://www.cloudflare.com/learning/security/ransomware/petya-notpetya-ransomware/) attacks also usually started out with an email attachment



Part of email security involves blocking or neutralizing these malicious email attachments; this can involve scanning all emails with anti-malware to identify malicious code. In addition, users should be trained to ignore unexpected or unexplained email attachments. For web-based email clients, [browser isolation](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/) can also help nullify these attacks, as the malicious attachment is downloaded in a sandbox separate from the user's device.

## What is spam?

Spam is a term for unwanted or inappropriate email messages, sent without the recipient's permission. Almost all email providers offer some degree of spam filtering. But inevitably, some spam messages still reach user inboxes.

Spammers gain a bad "email sender reputation"* over time, leading to more and more of their messages getting marked as spam. For this reason they are often motivated to take over user inboxes, steal IP address space, or spoof domains in order to send spam that is not detected as spam.

Individuals and organizations can take several approaches to cut down on the spam they receive. They can reduce or eliminate public listings of their email addresses. They can implement a third-party spam filter on top of the filtering provided by their email service. And they can be consistent about marking spam emails as spam, in order to better train the filtering they do have.

*_If a large percentage of a sender’s emails are unopened or marked as spam by recipients, or if a sender’s messages bounce too much, ISPs and email services downgrade their email sender reputation._

## How do attackers take over email accounts?

Attackers can use a stolen inbox for a wide range of purposes, including sending spam, initiating phishing attacks, distributing malware, harvesting contact lists, or using the email address to steal more of the user's accounts.

They can use a number of methods to break into an email account:

  * **Purchasing lists of previously stolen credentials:** There have been many personal data breaches over the years, and lists of stolen username/password credentials circulate widely on the dark web. An attacker can purchase such a list and use the credentials to break into users' accounts, often via [credential stuffing](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/).
  * **Brute force attacks:** In a brute force attack, an attacker loads a login page and uses a bot to rapidly guess a user's credentials. [Rate limiting](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/) and limits on password entry effectively stop this method.
  * **Phishing attacks:** The attacker may have conducted a previous phishing attack to obtain the user's email account login credentials.
  * **Web browser infections:** Similar to an on-path attack, a malicious party can infect a user's web browser in order to see all the information they enter on webpages, including their email username and password.
  * **Spyware:** The attacker may have already infected the user's device and installed spyware to track everything they type, including their email username and password.



Using [multi-factor authentication (MFA)](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/) instead of single-factor password authentication is one way to protect inboxes from compromise. Enterprises may also want to require their users to go through a [single sign-on (SSO)](https://www.cloudflare.com/learning/access-management/what-is-sso/) service instead of logging directly into email.

## How does encryption protect email?

Encryption is the process of scrambling data so that only authorized parties can unscramble and read it. Encryption is like putting a sealed envelope around a letter so that only the recipient can read the letter's contents, even though any number of parties will handle the letter as it goes from sender to recipient.

Encryption is not built into email automatically; this means sending an email is like sending a letter with no envelope protecting its contents. Because emails often contain personal and confidential data, this can be a big problem.

Just as a letter does not instantly go from one person to another, emails do not go straight from the sender to the recipient. Instead, they traverse multiple connected networks and are [routed from mail server to mail server](https://blog.cloudflare.com/introducing-email-routing/) until they finally reach the recipient. Anyone in the middle of this process could intercept and read the email if it is not encrypted, including the email service provider. However, the most likely place for an email to be intercepted is close to the origin of the email, via a technique called packet sniffing (monitoring data packets on a network).

Encryption is like putting a sealed envelope around an email. Most email encryption works by using [public key cryptography (learn more)](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/). Some email encryption is [end-to-end](https://www.cloudflare.com/learning/privacy/what-is-end-to-end-encryption/); this protects email contents from the email service provider, in addition to any external parties.

## How do DNS records help prevent email attacks?

The [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) stores public records about a domain, including that domain's IP address. The DNS is essential for enabling users to connect to websites and send emails without memorizing long alphanumeric IP addresses.

There are specialized types of DNS records that help ensure emails are from a legitimate source, not an impersonator: [SPF records](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/), [DKIM records](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/), and [DMARC records](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/). Email service providers check emails against all three of these records to see if they are from the place they claim to be from and have not been altered in transit.

The Cloudflare Email DNS Security Wizard helps domain owners quickly and correctly configure these crucial DNS records. To learn more, see our [blog post](https://blog.cloudflare.com/tackling-email-spoofing/).

## How can phishing attacks be stopped?

Many email providers have some built-in phishing protection (and the DNS records listed above are usually one of the signals they look at for blocking phishing attempts). However, phishing emails still regularly get through to user inboxes. Many organizations employ additional phishing protection to better defend their users and networks.

Cloudflare Email Security offers cloud-based phishing protection. Cloudflare discovers phishing infrastructure in advance and analyzes traffic patterns to correlate attacks and identify phishing campaigns. [Read in more detail about how this anti-phishing service works](https://www.cloudflare.com/sase/products/email-security/).
