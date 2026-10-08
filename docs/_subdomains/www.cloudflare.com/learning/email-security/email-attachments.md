---
url: https://www.cloudflare.com/learning/email-security/email-attachments/
title: When are email attachments safe to open?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:09.782321+00:00
---

# When are email attachments safe to open?

> Source: https://www.cloudflare.com/learning/email-security/email-attachments/

[ Learning Center ](https://www.cloudflare.com/learning/) / email security

##  When are email attachments safe to open? 

Email attachments can contain malware. It is important to confirm who sent an attachment, why they sent it, and what it will do before opening or downloading it. 

[Learning Center](https://www.cloudflare.com/learning)/email security/[What is business email compromise (BEC)?](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[What are DMARC, DKIM, and SPF?](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)[When are email attachments safe to open?](https://www.cloudflare.com/learning/email-security/email-attachments/)[How to prevent phishing](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[How to stop spam emails](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[What is a secure email gateway (SEG)?](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/)[What SMTP port should be used? Port 25, 587, or 465?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)[What is a mail server?](https://www.cloudflare.com/learning/email-security/what-is-a-mail-server/)[What is email? | Email definition](https://www.cloudflare.com/learning/email-security/what-is-email/)[What is email encryption?](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[What is email fraud?](https://www.cloudflare.com/learning/email-security/what-is-email-fraud/)[What is email routing?](https://www.cloudflare.com/learning/email-security/what-is-email-routing/)[What is email security?](https://www.cloudflare.com/learning/email-security/what-is-email-security/)[What is IMAP?](https://www.cloudflare.com/learning/email-security/what-is-imap/)[What is the Simple Mail Transfer Protocol (SMTP)?](https://www.cloudflare.com/learning/email-security/what-is-smtp/)[What is vendor email compromise (VEC)?](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/)[What is vishing? | Preventing vishing attacks](https://www.cloudflare.com/learning/email-security/what-is-vishing/)[How to identify a phishing email](https://www.cloudflare.com/learning/email-security/how-to-identify-phishing-email/)[What is email spoofing?](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain the risks of opening email attachments 
  * Understand when email attachments might be safe to open 
  * Describe the types of email attachments that lead to malware infections 



Related content  [ What is business email compromise (BEC)? ](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/)[ How to prevent phishing ](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/)[ How to stop spam emails ](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/)[ What is email encryption? ](https://www.cloudflare.com/learning/email-security/what-is-email-encryption/)[ What is email security? ](https://www.cloudflare.com/learning/email-security/what-is-email-security/)

On this page

  * When are email attachments safe to open?

  * Why are email attachments dangerous?

  * Which email attachments are generally safe to open?

  * When are email attachments not safe to open?

  * What kinds of email attachments can contain malware?

  * What is a file extension?

  * How do attackers embed macros, scripts, and other dangerous content in common files?

    * Office files

    * PDFs

    * Archive files

    * Other files

  * What are some of the ransomware attacks that have used email attachments?

  * What other attacks use email attachments?

  * Do secure email gateways block malicious email attachments?




## When are email attachments safe to open?

The ability to attach files to emails is useful, but it also introduces risk. Email attachments from malicious parties may contain [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/), which can lead to a hack or [data breach](https://www.cloudflare.com/learning/security/what-is-a-data-breach/). There is no foolproof way to know if an email attachment is safe to open — but unexpected attachments from unknown persons are most likely to be dangerous.

## Why are email attachments dangerous?

An email attachment is a file sent with an [email](https://www.cloudflare.com/learning/email-security/what-is-email/) — like a gift that comes with a card. Almost any kind of file can be attached to an email; usually the only limitation is how large of a file, or how many files, an email client is willing to accept. But like any file that is sent over a network, email attachments can sometimes contain dangerous or malicious content that can infect a device with malware.

Attackers often attempt to distribute malware by attaching it to emails. Sometimes they attach malware as an executable (EXE) file and try to trick the email recipient into downloading and opening the file, which runs the malware. Other times they might bury a malicious script in a harmless-seeming file, like a Microsoft Word document (DOC, DOCX) or an archive file (ZIP, RAR, etc.). Once the script executes, it downloads and installs malware, or performs some other malicious action. Finally, attackers may disguise malware or scripts inside file types that seem unlikely to contain them, like images or video files.

Imagine an email attachment as a wrapped gift and the email it is attached to as a card that comes with it. Someone who receives the gift cannot tell what is inside it until they open it. Similarly, it is impossible to be sure of what an email attachment actually contains. And unfortunately, because almost anyone in the world can send emails to each other, this means all email attachments have to be treated with suspicion. This is the case even if the accompanying email — the "card" in the analogy — seems to be from a trusted person.

## Which email attachments are generally safe to open?

As with any aspect of security, there is no way to guarantee that any given file is safe. However, answering the following questions can help determine if an email attachment should be trusted. If the answer to any of them is "no," it is wise for users to contact the purported sender — or to contact their organization's security team.

  * **Do you know the sender?** Email attachments from a known source are more likely to be trustworthy than email attachments from an unknown source. Someone that the recipient has never met is far less likely to have a legitimate reason for sending an email attachment — just as one is not likely to receive birthday presents from strangers.

  * **Can you confirm the sender actually sent the email?** Sometimes, malicious parties will impersonate a known and trusted sender, even someone in the recipient's contact list or organization. They can do this by faking or [spoofing](https://www.cloudflare.com/learning/email-security/what-is-email-spoofing/) the sender email address, or by [breaking into the sender's inbox](https://www.cloudflare.com/learning/access-management/account-takeover/) and sending the email on their behalf.

  * **Did you expect the email?** Unexpected emails are often an indicator of an attack attempt. Most malicious emails are not expected — no one wants to get hacked, after all.

  * **Did you expect the email to have an attachment?** Even if the email itself is expected, an unexpected or irrelevant attachment could be malicious.

  * **Is the attachment an expected file type?** For example, if the sender says they have attached or will attach an image, but the file received is a PDF or an EXE, this may be a sign that the file should not be trusted.




If all of these questions can be answered in the affirmative, the email attachment is more likely, but still not guaranteed, to be safe.

## When are email attachments not safe to open?

The questions in the previous section are a good starting point for identifying potentially dangerous attachments. Additional indicators that a message may be unsafe to open include the following:

  * **Urgency:** Attackers want the people who receive their emails to act quickly, before they have time to question or investigate further. The email may demand that the recipient quickly downloads or opens the attachment.

  * **Email is sent to large group or unknown recipients:** Attackers sometimes cast as wide a net as possible to make it more likely that someone will download the malicious attachment. They do this by sending the malicious email to long lists of recipients or large group email aliases. They may try to conceal how many people the email is sent to by using BCC and leaving the "To" field blank.

  * **Unusual writing style in email:** Spelling and grammar errors are a common sign that an email may be from a scammer. But sometimes, legitimate senders also ignore these conventions. Recipients should compare the email to the sender's typical email writing style. In addition, if the email is about topics that the sender does not usually address, the email may not actually be from the supposed sender.

  * **Lack of personalized greeting:** Attackers do not always have time to target their victims one at a time. A generic greeting, or a missing greeting, could be a sign that the email is not legitimate. (This is not always the case — particularly in [spear phishing](https://www.cloudflare.com/learning/access-management/spear-phishing/) and [business email compromise](https://www.cloudflare.com/learning/email-security/business-email-compromise-bec/) attacks, email threats are sometimes highly targeted and personalized.)

  * **The attached file contains malware:** Many email providers will identify possible malware with anti-malware analysis and flag dangerous attachments — a clear sign that the email should not be opened.




## What kinds of email attachments can contain malware?

Any type of file can contain malicious code. Archive files, PDFs, Microsoft Word documents, and Microsoft Excel spreadsheets have been used in many malware attacks. However, attackers are not limited to these file types. Anything from images to text files can be dangerous.

One of the most obviously dangerous file types is the executable file. Executable files are programming instructions that a computer carries out when the files are opened. It is rare that a legitimate sender will attach executable code in an email — usually a software program will be sent some other way. Executable files have an EXE file extension (on Windows) or an APP file extension (on Mac).

## What is a file extension?

A file extension is the text that follows the period (or full stop) at the end of a file name. For example, in the file name "quiche-recipe.doc", the file extension is .doc or DOC. File extensions indicate the file type — a DOC file extension indicates that this is a Microsoft Word document.

File extensions can be faked or forged. Identifying the file extension is not a reliable way to determine if a file is safe or not.

Other common file extensions to know include, but are not limited to:

  * Microsoft Word: .doc, .docx (DOC, DOCX)

  * Microsoft Excel: .xls, .xlsx (XLS, XLSX)

  * Adobe Acrobat PDF: .pdf (PDF)

  * Executable files: .exe, .app (EXE, APP)

  * Archive files: .zip, .rar, .iso (ZIP, RAR, ISO)

  * Image files: .jpeg, .png, .gif (JPEG, PNG, GIF)

  * Audio files: .mp3, .wav (MP3, WAV)

  * Web files: .html, .css, .js (HTML, CSS, JavaScript)

  * Plain text files: .txt (TXT)




## How do attackers embed macros, scripts, and other dangerous content in common files?

#### Office files

A macro is an executable script for use within Microsoft Office files such as Word and Excel. While macros have many legitimate uses, they have also been used in attacks. If an email attachment asks the recipient to enable macros, it may be malicious.

#### PDFs

Attackers can embed malicious JavaScript within PDFs, along with links to dangerous websites or cloud-hosted files controlled by attackers.

#### Archive files

An archive file is a file format for storing one or more files in a wrapper, along with metadata about the files. Archive files are often compressed as well to make them more portable. An archive file is just a wrapper for the file(s) within — anything could be inside. This makes them convenient for attackers, who can conceal a malicious file inside an archive file, then trick a user into downloading the file and opening its contents.

#### Other files

Unsafe scripts and links can be included in almost any type of file — either directly in the file or hidden in its metadata. In addition, attackers can fake a file extension so that a malicious file seems to be an image, an audio file, a video file, a TXT file, or some other type of file that a user might be more likely to trust.

## What are some of the ransomware attacks that have used email attachments?

Many [ransomware](https://www.cloudflare.com/learning/security/ransomware/what-is-ransomware/) attacks over the years have entered an organization or reached the victim's computer through an email attachment. Examples include:

  * [Petya ransomware](https://www.cloudflare.com/learning/security/ransomware/petya-notpetya-ransomware/) often spread via emails to HR departments with fake job applications attached as PDFs.

  * Early on, [Maze ransomware](https://www.cloudflare.com/learning/security/ransomware/maze-ransomware/) spread to its victims via malicious email attachments. (This method may still be used, but Maze also spreads through [RDP vulnerability](https://www.cloudflare.com/learning/access-management/rdp-security-risks/) exploits and other [attack vectors](https://www.cloudflare.com/learning/security/glossary/attack-vector/).)

  * The REvil ransomware group has been observed using malicious email attachments to spread ransomware.




Some ransomware attacks do not use email attachments directly, but instead piggyback on top of previous attacks that took place using email attachments. [Ryuk ransomware](https://www.cloudflare.com/learning/security/ransomware/ryuk-ransomware/) often enters an organization through a TrickBot infection, which in turn often spreads via the Emotet botnet. (Such multi-layered attacks are common and demonstrate the variety of actions available to an attacker once they gain a foothold in an organization's network.) Emotet has most commonly spread using malicious Word documents attached to emails.

## What other attacks use email attachments?

Any script or malware can be hidden in an email attachment, which then allows attackers to gain access to networks, steal confidential data, and carry out other malicious actions. Once the email attachment has been opened by its recipient, it can be used to spread spyware, adware, worms, or even [botnets](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/).

## Do secure email gateways block malicious email attachments?

[Secure email gateways](https://www.cloudflare.com/learning/email-security/secure-email-gateway-seg/) filter out unsafe email traffic, including [spam](https://www.cloudflare.com/learning/email-security/how-to-stop-spam-emails/), [phishing emails](https://www.cloudflare.com/learning/email-security/how-to-prevent-phishing/), and dangerous email attachments. Many secure email gateways include anti-malware scanning capabilities, enabling them to identify malware inside attached files. They also maintain lists of known threats and block all emails from them.

But secure email gateways are not a guarantee against email attachment-based attacks. New types of malware may not be detected; emails sent from trusted or unknown sources may not be blocked; and even known malicious content sometimes can get through defenses.

Many organizations try to avoid using email attachments altogether, and instead use secure file upload portals or share links to files in the cloud (which come with their own risks). Additional strategies to reduce the threat posed by email attachments include:

  * [Email security services](https://www.cloudflare.com/sase/use-cases/email-security-services/) that proactively identify email attack infrastructure, including domains and servers, can block attacks before they begin. [Cloudflare Email Security](https://www.cloudflare.com/sase/products/email-security/) takes this approach.

  * [Secure web gateways](https://www.cloudflare.com/learning/access-management/what-is-a-secure-web-gateway/), [DNS filtering](https://www.cloudflare.com/learning/access-management/what-is-dns-filtering/), and [URL filtering](https://www.cloudflare.com/learning/access-management/what-is-url-filtering/) can block requests from email attachments to the attackers' servers, often a necessary step for downloading the actual [malicious payload](https://www.cloudflare.com/learning/security/glossary/malicious-payload/) that the attacker wants to install.

  * [Zero Trust Network Architecture (ZTNA)](https://www.cloudflare.com/learning/access-management/what-is-ztna/) quickly isolates the damage if an infection does enter via an email attachment, preventing [lateral movement](https://www.cloudflare.com/learning/security/glossary/what-is-lateral-movement/).




Even with the myriad communications apps available today, email remains the most-used communication method for many organizations, making email security crucial for protection from attacks. Learn more about [email security](https://www.cloudflare.com/learning/email-security/what-is-email-security/).
