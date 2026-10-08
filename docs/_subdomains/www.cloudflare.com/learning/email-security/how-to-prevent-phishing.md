---
url: https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/
title: How to prevent phishing
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:26.702876+00:00
---

# How to prevent phishing

> Source: https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  How to prevent phishing 

Phishing prevention tools and email security best practices can be used to help block phishing attacks. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain how email is used in phishing attacks 
  * Identify common elements of a phishing email 
  * Learn strategies for phishing prevention 



Related content  [ What is email? | Email definition ](https://www.cloudflare.com/learning/email-security/what-is-email/)[ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[ What is the Simple Mail Transfer Protocol (SMTP)? ](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[ What is email spoofing? ](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)[ How to stop spam emails ](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)

On this page

  * Article Summary:

  * How is email used to carry out a phishing attack?

  * How to identify a phishing attack

  * How to prevent phishing attacks

  * How does Cloudflare protect against phishing attacks?

  * FAQs

    * How can I identify a potential phishing email?

    * What is the best way to handle personal information over email?

    * How can email security protocols help prevent phishing?

    * What are some technical solutions for blocking phishing attacks?

    * What should I do if an email seems suspicious but I&#39




## Article Summary:

  * Implement essential email security protocols like SPF, DKIM, and DMARC records to verify domains, preventing phishing attempts and unauthorized attackers from successfully spoofing your brand's identity.

  * Utilize a secure web gateway and browser isolation services to filter harmful traffic, block known malware, and safely execute suspicious links or attachments in the cloud.

  * Always identify phishing red flags, such as urgent language or generic greetings, and independently confirm sensitive requests with the sender via a secondary, secure communication channel.




## How is email used to carry out a phishing attack?

Phishing is a cyber attack in which an attacker conceals their true identity in order to deceive the victim into completing a desired action. Often, a phishing attack uses [email](https://www.cloudflare.com/learning/email-security/what-is-email/) to convince targets that a message is coming from a trusted source, like a reputable financial institution or an employer. Because the message appears legitimate, the user may be more likely to share valuable account data or engage with [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/) — typically presented as an attachment or link — camouflaged within the email.

Some phishing tactics attempt to collect information directly from the recipient by claiming that an account has been breached in some way (e.g. fraudulent password reset requests) or by offering a monetary reward (e.g. fake gift cards). Other phishing emails contain malware within the attachments or links that appear in the body of the email, which can infect other devices or networks once a user interacts with them.

When successful, a phishing attempt allows attackers to steal user credentials, infiltrate a network, commit data theft, or take more extreme action against a victim (e.g. carrying out a [ransomware](https://www.cloudflare.com/learning/security/ransomware/what-is-ransomware/) attack).

To learn more about phishing techniques, see [What is a phishing attack?](https://www.cloudflare.com/learning/access-management/phishing-attack/)

## How to identify a phishing attack

Because phishing emails are designed to imitate legitimate individuals and organizations, they may be difficult to identify at first glance. Here are some common warning signs to watch out for:

  * **The email does not pass SPF, DKIM, or DMARC checks.** Three [DNS](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/) records — [Sender Policy Framework (SPF)](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/), [DomainKeys Identified Mail (DKIM)](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/), and [Domain-based Message Authentication Reporting and Conformance (DMARC)](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/) — are used to authenticate the origin of an email. When an email message does not pass one or more of these checks, it is often marked as spam or not delivered to its intended recipient. For this reason, it is uncommon to find legitimate emails in spam folders.

  * **The sender’s email address is not associated with a legitimate domain name.** The domain should match the name of the organization the email claims to come from. For example, if all email addresses from Legitimate Internet Company are formatted as “[employee@legitinternetcompany.com](mailto:employee@legitinternetcompany.com),” a counterfeit email might be sent from a similar-sounding address like “[employee@legitinternetco.com](mailto:employee@legitinternetco.com).”

  * **A generic greeting is used in place of a name.** Words like “customer,” “account holder,” or “dear” may be a sign that the email is part of a mass phishing attempt, rather than a personal message from a legitimate sender.

  * **There is a time limit or uncharacteristic sense of urgency.** Phishing emails often generate a false sense of urgency to convince users to take action. For instance, they may promise a gift card if the user responds within 24 hours, or allege a data breach to get the user to update their password. It is rare for these tactics to be tied to real deadlines or consequences, as they are intended to overwhelm a user into taking action before they become suspicious.

  * **The body message is full of errors.** Poor grammar, spelling, and sentence structure may hint that an email is not from a reputable source.

  * **Links in the body message do not match the sender’s domain.** Most legitimate requests will not direct users to a website that is different from the sender’s domain. By contrast, phishing attempts often redirect users to a malicious site or mask malicious links in the email body.

  * **The CTA includes a link to the sender’s website.** Even when links appear to point to legitimate websites, they may redirect victims to a malicious site or trigger a malware download. Most reputable organizations will not ask users to disclose sensitive information (e.g. credit card numbers) by clicking on a link.*




In general, the more sophisticated a phishing attempt is, the less likely it is that these elements will appear in an email. For instance, some phishing emails use the logos and graphics of well-known companies to make their message look legitimate, while other attackers may code the entire body field as a malicious hyperlink.

**Exceptions to this rule may include password reset requests and account verification. Phishing attempts may also fake these types of requests, however, so it’s wise to double-check the sender’s email address before clicking on anything.**

Under Attack?

Comprehensive protection against cyber attacks

[Talk to an expert](https://www.cloudflare.com/under-attack-hotline/)

## How to prevent phishing attacks

As with any kind of unsolicited email (often referred to as ‘spam’), phishing emails cannot be completely eliminated by a security tool or filtering service. However, there are several actions users can take to diminish the chances of a successful attack:

  * **Evaluate emails for suspicious elements.** Email headers may reveal deceptively-worded sender names or email addresses, while the body may include attachments and links that camouflage malicious code. Users should err on the side of caution when opening a message from an unfamiliar sender.

  * **Do not share personal information.** Even when communicating with a trusted individual, personal information — e.g. Social Security numbers, bank information, passwords, etc. — should never be exchanged in the body of an email.

  * **Block spam.** Most email clients come with built-in spam filters, but third-party filtering services can give users more granular control over their email. Other [recommendations for avoiding email spam](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/) include unsubscribing from mailing lists, refusing to open spam emails, and keeping email addresses private (i.e. not listing them on an organization’s external-facing website).

  * **Use email security protocols.** Email authentication methods like SPF, DKIM, and DMARC records help verify the source of an email. Domain owners can configure these records to make it difficult for attackers to impersonate their domains in a [domain spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/) attack.

  * **Run a browser isolation service.** [Browser isolation](https://www.cloudflare.com/learning/access-management/what-is-browser-isolation/) services isolate and execute browser code in the cloud, protecting users from triggering malware attachments and links that may be delivered through a web-based email client.

  * **Filter harmful traffic with a secure web gateway.** A [secure web gateway (SWG)](https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/) inspects data and network traffic for known malware, then blocks incoming requests according to predetermined security policies. It can also be configured to prevent users from downloading files (like those that may be attached to a phishing email) or sharing sensitive data.

  * **Verify the message with the sender.** If an email message still seems suspicious, it may be necessary to independently confirm the message was sent by a legitimate individual or organization. There are several verification methods that can be used to do this, like a phone call or text message. When in doubt, ask the sender if there is a more secure way to transmit any sensitive information they may have requested.




## How does Cloudflare protect against phishing attacks?

Cloudflare Email Security detects and blocks phishing attempts in real time. It proactively scans the Internet for attack infrastructure and campaigns, uncovers email fraud attempts, and provides visibility into compromised accounts and domains.

Learn how to protect against phishing attacks with [Cloudflare Email Security](https://www.cloudflare.com/sase/products/email-security/).

## FAQs

#### How can I identify a potential phishing email?

It is not always possible to tell if an email is a phishing email or not, so the safest approach is to take one's time and respond slowly when receiving an email that seems to require immediate action. In particular, if an email is unexpected, creates a sense of urgency, or aims to collect more personal data than seems necessary, it might be a phishing email. It is also a good idea to check with the supposed sender over a separate channel to make sure the email really came from them.

#### What is the best way to handle personal information over email?

Because email inboxes can be compromised and some email services do not provide encryption, you should never exchange personal information like Social Security numbers, bank details, or passwords within the body of an email. This applies even when you are communicating with a trusted individual. Use a secure web form or communicate this information using a phone call instead.

#### How can email security protocols help prevent phishing?

Email authentication protocols such as SPF, DKIM, and DMARC help to verify an email's source. Domain owners can set up these records to make it much more difficult for attackers to impersonate their domains in a phishing attack.

#### What are some technical solutions for blocking phishing attacks?

Several technologies can help defend against phishing. A browser isolation service can execute browser code in the cloud to protect users from malicious links or attachments in web-based email. A secure web gateway (SWG) can inspect traffic for known malware and block harmful requests based on security policies. And an email security service that uses machine learning to examine email traffic can be trained to identify potential phishing emails and either mark them as spam or block them altogether.

#### What should I do if an email seems suspicious but I'm not sure?

If you are still unsure about an email, you should try to independently confirm that the message was sent by a legitimate person or organization. You can use other verification methods, like a phone call or a text message, to ask the sender if the email is authentic.
