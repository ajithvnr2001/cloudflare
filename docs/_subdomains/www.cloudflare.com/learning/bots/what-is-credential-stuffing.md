---
url: https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/
title: What is credential stuffing? | Learning Center
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:56.209550+00:00
---

# What is credential stuffing? | Learning Center

> Source: https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/

[ Learning Center ](https://www.cloudflare.com/learning/) / bots

##  What is credential stuffing? 

Credential stuffing is a cyberattack that uses stolen login credentials from one breach to gain access to accounts on other services. 

[Learning Center](https://www.cloudflare.com/learning)/bots/[How CAPTCHAs work | What does CAPTCHA mean?](https://www.cloudflare.com/learning/bots/how-captchas-work/)[How is an Internet bot constructed?](https://www.cloudflare.com/learning/bots/how-is-an-internet-bot-constructed/)[How to manage good bots | Good bots vs. bad bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/)[What is a bot?](https://www.cloudflare.com/learning/bots/what-is-a-bot/)[What is a bot attack?](https://www.cloudflare.com/learning/bots/what-is-a-bot-attack/)[What is a chatbot?](https://www.cloudflare.com/learning/bots/what-is-a-chatbot/)[What is a social media bot? | Social media bot definition](https://www.cloudflare.com/learning/bots/what-is-a-social-media-bot/)[What is a spam bot? | How spam comments and spam messages spread](https://www.cloudflare.com/learning/bots/what-is-a-spambot/)[What is a web crawler? | How web spiders work](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/)[What is ad fraud? | Ad click fraud](https://www.cloudflare.com/learning/bots/what-is-ad-fraud/)[What is bot traffic? | How to stop bot traffic](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/)[What is click fraud? | How click bots work](https://www.cloudflare.com/learning/bots/what-is-click-fraud/)[What is data scraping?](https://www.cloudflare.com/learning/bots/what-is-data-scraping/)[What is rate limiting? | Rate limiting and bots](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)[What is robots.txt? | How a robots.txt file works](https://www.cloudflare.com/learning/bots/what-is-robots-txt/)[What is bot management?](https://www.cloudflare.com/learning/bots/what-is-bot-management/)[What is credential stuffing?](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/)[What is content scraping?](https://www.cloudflare.com/learning/bots/what-is-content-scraping/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define credential stuffing 
  * Understand how credential stuffing differs from brute force 
  * Learn how to prevent credential stuffing attacks 



Related content  [ What is a bot? ](https://www.cloudflare.com/learning/bots/what-is-a-bot/)

On this page

  * What is credential stuffing?

  * What makes credential stuffing effective?

  * What’s the difference between credential stuffing and brute force attacks?

  * How to prevent credential stuffing

    * How users can prevent credential stuffing

    * How companies can prevent credential stuffing




## What is credential stuffing?

Credential stuffing is a cyber attack in which credentials obtained from a [data breach](https://www.cloudflare.com/learning/security/what-is-a-data-breach/) on one service are used to attempt to log in to another unrelated service.

![Credential Stuffing Example](https://images.ctfassets.net/slt3lc6tev37/7063QaY9i4PTXesgUmpoYk/cd8e741be8731bca5494bc14d03a134c/credential-stuffing.png)

For example, an attacker may take a list of usernames and passwords obtained from a breach of a major department store, and use the same login credentials to try and log in to the site of a national bank. The attacker is hoping that some fraction of those department store customers also have an account at that bank, and that they reused the same usernames and passwords for both services.

Credential stuffing is widespread thanks to [massive lists of breached credentials](https://www.cloudflare.com/the-net/credential-stuffing/) being traded and sold on the black market. The proliferation of these lists, combined with advancements in credential stuffing tools that use [bots](https://www.cloudflare.com/learning/bots/what-is-a-bot/) to get around traditional login protections, have made credential stuffing a popular [attack vector](https://www.cloudflare.com/learning/security/glossary/attack-vector/).

## What makes credential stuffing effective?

Statistically speaking, credential stuffing attacks have a very low rate of success. Many estimates have this rate at about 0.1%, meaning that for every thousand accounts an attacker attempts to crack, they will succeed roughly once. The sheer volume of the credential collections being traded by attackers makes credential stuffing worth it, in spite of the low success rate.

These collections contain millions and in some cases billions of login credentials. If an attacker has one million sets of credentials, this could yield around 1,000 successfully cracked accounts. If even a small percentage of the cracked accounts yields profitable data (often in the form of credit card numbers or sensitive data that can be used in [phishing](https://www.cloudflare.com/learning/security/threats/phishing-attack/) attacks), then the attack is worthwhile. On top of that, the attacker can repeat the process using the same sets of credentials on numerous different services.

Advances in bot technology also make credential stuffing a viable attack. Security features built into web application login forms often include deliberate time delays and banning the [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) of users who have repeated failed login attempts. Modern credential stuffing software circumvents these protections by using bots to simultaneously attempt several logins that appear to come from a variety of device types and originate from different IP addresses. The malicious bot's goal is to make the attacker’s login attempts indistinguishable from typical login traffic, and it’s very effective. 

Often times the only indication the victimized company has that they are being attacked is the rise in the overall volume of login attempts. Even then, the victimized company will have difficulty stopping these attempts without impacting the ability of legitimate users to log in to the service.

The main reason that credential stuffing attacks are effective is that people reuse passwords. Studies suggest that a majority of users, by some estimates as high as 85%, reuse the same login credentials for multiple services. As long as this practice continues, credential stuffing will remain fruitful.

## What’s the difference between credential stuffing and brute force attacks?

[OWASP](https://www.cloudflare.com/learning/security/threats/owasp-top-10/) categorizes credential stuffing as a subset of [brute force attacks](https://www.cloudflare.com/learning/security/threats/brute-force-attack/). But, strictly speaking, credential stuffing is very different from traditional brute force attacks. Brute force attacks attempt to guess passwords with no context or clues, using characters at random sometimes combined with common password suggestions. Credential stuffing uses exposed data, dramatically reducing the number of possible correct answers.

A good defense against brute force attacks is a strong password consisting of several characters and including uppercase letters, numbers, and special characters. But password strength does not protect against credential stuffing. It doesn’t matter how strong a password is – if it’s shared across different accounts then credential stuffing can compromise it.

## How to prevent credential stuffing

#### How users can prevent credential stuffing

From a user’s point of view, defending against credential stuffing is pretty straightforward. Users should always use unique passwords for each different service (an easy way to achieve this is with a password manager). If a user always uses unique passwords, credential stuffing will not work against their accounts. As an added measure of security, users are encouraged to always enable [two-factor authentication](https://www.cloudflare.com/learning/access-management/what-is-two-factor-authentication/) when it’s available.

#### How companies can prevent credential stuffing

Stopping credential stuffing is a more complex challenge for companies who run authentication services. Credential stuffing occurs as a result of data breaches at other companies. A company victimized by a credential stuffing attack has not necessarily had their security compromised.

A company can suggest that its users provide unique passwords but cannot effectively enforce this as a rule. Some applications will run a submitted password against a database of known compromised passwords before accepting the password as a measure against credential stuffing, but this isn’t foolproof – the user could be reusing a password from a service that is yet to be breached.

Providing added login security features can help mitigate credential stuffing. Enabling features like [two-factor authentication](https://www.cloudflare.com/learning/access-management/what-is-two-factor-authentication) and requiring users to fill out [captchas](https://www.cloudflare.com/learning/bots/how-captchas-work/) when logging in both also help stop malicious bots. While these are both features that inconvenience users, many would agree that [minimizing the security threat](https://www.cloudflare.com/cybersecurity/) is worth the inconvenience.

The strongest protection against credential stuffing is a bot management service. Bot management uses rate limiting combined with an IP reputation database to stop malicious bots from making login attempts without impacting legitimate logins. [Cloudflare Bot Management](https://www.cloudflare.com/application-services/products/bot-management/), which gathers data from 25 million average requests per second routed through the Cloudflare network, can identify and stop credential-stuffing bots with very high accuracy.For organizations that want the same bot-blocking abilities but do not need an enterprise solution, [Super Bot Fight Mode](https://www.cloudflare.com/pg-lp/bot-mitigation-fight-mode?utm_campaign=pgg221s-pl-super-bot-fight-lc) is now available on Cloudflare Pro and Business plans. With Super Bot Fight Mode, smaller organizations can take advantage of increased visibility and control over their bot traffic. 
