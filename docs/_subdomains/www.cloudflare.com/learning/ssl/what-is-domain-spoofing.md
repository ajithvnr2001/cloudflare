---
url: https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/
title: What Is Domain Spoofing? | Website and Email Spoofing
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:59.694013+00:00
---

# What Is Domain Spoofing? | Website and Email Spoofing

> Source: https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  What is domain spoofing? | Website and email spoofing 

Domain spoofing involves faking a website name or email name so that unsecure or malicious websites and emails appear to be safe. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what a domain is 
  * Learn about website spoofing 
  * Learn about email spoofing 
  * Explore ways to protect against domain spoofing 



Related content  [ How does SSL work? | SSL certificates and TLS ](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)

On this page

  * Article Summary:

  * What is domain spoofing?

  * What is a domain?

  * What are the main types of domain spoofing?

    * Website/URL spoofing

    * Email spoofing

    * Domain spoofing in advertising

  * How can users protect themselves from domain spoofing?

  * How can companies stop their domains from being spoofed?

  * FAQs

    * What is domain spoofing?

    * What is the difference between website spoofing and email spoofing?

    * How do attackers make a fake URL look like a real one?

    * How can I tell if a website is spoofed?

    * What steps can companies take to prevent their domains from being spoofed?

    * Is domain spoofing the same as DNS spoofing?




## Article Summary:

  * Domain spoofing involves faking website URLs or email addresses to deceive users. Attackers use these tactics in phishing campaigns to steal credentials, deliver malware, or commit advertising fraud.

  * Attackers often employ homograph attacks, using visually similar Unicode characters to create deceptive URLs. Carefully inspecting site URLs and verifying SSL certificate details can help users identify these malicious clones.

  * While stopping domain spoofing is difficult, organizations can improve security by implementing DMARC and DKIM protocols for emails. Using SSL certificates further validates website legitimacy for visiting users.




## What is domain spoofing?

Domain spoofing is when cyber criminals fake a website name or email domain to try to fool users. The goal of domain spoofing is to trick a user into interacting with a malicious email or a phishing website as if it were legitimate. Domain spoofing is like a con artist who shows someone fake credentials to gain their trust before taking advantage of them.

Domain spoofing is often used in [phishing attacks](https://www.cloudflare.com/learning/access-management/phishing-attack/). The goal of a phishing attack is to steal personal information, such as account login credentials or credit card details, to trick the victim into sending money to the attacker, or to trick a user into downloading [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/). Domain spoofing can also be used to carry out ad fraud by tricking advertisers into paying for ads shown on websites other than the websites they think they're paying for.

Domain spoofing is distinct from [DNS spoofing or cache poisoning](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/), and also from [BGP hijacking](https://www.cloudflare.com/learning/security/glossary/bgp-hijacking/). These are other ways to direct a user to the wrong website that are more complex than simply faking the name.

## What is a domain?

A domain, or more correctly [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/), is the full name of a website. "cloudflare.com" is one example of a domain name. For companies and organizations, the domain appears within email addresses of employees after the "@" symbol. A personal email account may use "gmail.com" or "yahoo.com" as its domain, but a company email will usually use the company's website. (To learn more about domains, see [What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/))

## What are the main types of domain spoofing?

#### Website/URL spoofing

Website spoofing is when an attacker builds a website with a URL that closely resembles, or even copies, the URL of a legitimate website that a user knows and trusts. In addition to spoofing the URL, the attacker may copy the content and style of a website, complete with images and text.

To imitate a URL, attackers can use characters from other languages or Unicode characters that look almost exactly the same as regular ASCII characters. (This is called a [homograph attack](https://www.xudongz.com/blog/2017/idn-phishing/).) Less convincing spoofed URLs may add or substitute regularly used characters to the URL and hope that users don't notice.

![Domain spoofing example](https://images.ctfassets.net/slt3lc6tev37/3HsnmyXh6cduer2FTurZmh/392d82ecd242de77208a7386c376d8b3/domain-spoofing-example.png)Domain spoofing example

These fake websites are typically used for criminal activities like phishing. A fake login page with a seemingly legitimate URL can trick a user into submitting their login credentials. Spoofed websites can also be used for hoaxes or pranks.

#### Email spoofing

Email spoofing is when an attacker uses a fake email address with the domain of a legitimate website. This is possible because domain verification is not built into the Simple Mail Transfer Protocol (SMTP), the protocol that email is built on. Email security protocols that were developed more recently, such as DMARC and DKIM, provide greater verification.

Attackers will often use email spoofing in phishing attacks. An attacker will spoof a domain name to convince users that the phishing email is legitimate. An email that seems to come from a company representative is more convincing at first glance than an email from some random domain.

The goal of the phishing attack could be to get users to visit a certain website, to download malware, to open a malicious email attachment, to enter account credentials, or to transfer money to an account the attacker controls.

Email spoofing is often paired with website spoofing, as the email may lead to a spoofed website where users are supposed to enter their username and password for the targeted account.

#### Domain spoofing in advertising

Ad fraud perpetrators fake the name of websites they own to obscure the real source of their traffic and offer their spoofed domains for bidding by advertisers. Then the display ads end up on an undesirable website instead of the website that advertisers wanted.

## How can users protect themselves from domain spoofing?

**Be mindful of the source.** Is the link from an email? Was the email expected? Unexpected requests and warnings are often from scammers.

**Take a close look at the URL.** Are there any extra characters that don't belong? Try copy and pasting the URL into a new tab: does it still look the same? (This can detect homograph attacks.)

**Make sure there's an SSL certificate.** An [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) is a text file that identifies a website and aids in encrypting traffic to and from the website. SSL certificates are usually issued by an external certificate authority, and before issuing one, the certificate authority will verify that the party requesting the certificate actually owns that domain name (although sometimes such verification is [fairly minimal](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)). Almost all legitimate websites these days will have an SSL certificate.

**Check the SSL certificate, if there is one.** Is the domain listed on the SSL certificate the name that one would expect? (To see the SSL certificate in Chrome, click on the padlock in the URL bar, then click "Certificate.") A spoofed website may have a real SSL certificate – but for the spoofed domain name, not for the actual domain name.

**Bookmark important websites.** Keep an in-browser bookmark of each legitimate website. Clicking on the bookmark, instead of following a link or typing the URL, ensures the correct URL loads each time. For instance, instead of typing "mybank.com" or performing a Google search for the bank's website, create a bookmark for the website.

## How can companies stop their domains from being spoofed?

SSL certificate can help make website spoofing more difficult for attackers, as they will then have to register for a spoofed SSL certificate in addition to registering the spoofed domain. (Cloudflare offers [free SSL certificates](https://www.cloudflare.com/application-services/products/ssl/).)

Unfortunately, there isn't a way to stop domain spoofing in email. Companies can add more verification to the emails they send via DMARC, DKIM, and other protocols, but external parties can still send fake emails using their domain without this verification.

## FAQs

#### What is domain spoofing?

Domain spoofing occurs when cyber criminals impersonate a legitimate website name or email domain to deceive users. The goal is to gain a user's trust so they will interact with malicious content, such as a phishing site or a fraudulent email, as if it were authentic.

#### What is the difference between website spoofing and email spoofing?

Website spoofing involves building a fake site with a URL that looks nearly identical to a trusted one, often copying the original's design and images to trick users into entering credentials. Email spoofing involves sending messages from a fake address that appears to use a legitimate person's or company's domain.

#### How do attackers make a fake URL look like a real one?

Attackers often use homograph attacks, where they substitute regular characters with Unicode or foreign language characters that look almost identical. Other methods include adding or swapping similar-looking characters in the URL, hoping that victims will not notice the subtle difference.

#### How can I tell if a website is spoofed?

You should always check for an SSL certificate, which helps authenticate web servers. While a spoofed site might have a certificate, it will be issued for the fake domain, not the real one. You can also verify the URL by copying and pasting it into a new tab to see if the characters change, or by looking for unexpected characters that do not belong.

#### What steps can companies take to prevent their domains from being spoofed?

While it is difficult to stop spoofing entirely, companies can make it harder for attackers by using SSL certificates, which require a verification process. For email, organizations can implement security protocols like DMARC and DKIM to provide better verification for the messages they send.

#### Is domain spoofing the same as DNS spoofing?

Domain spoofing is a relatively simple technique of faking a name or appearance. DNS spoofing (or cache poisoning) and BGP hijacking are more technically complex ways to redirect a user to the wrong website by manipulating the underlying infrastructure of the Internet.
