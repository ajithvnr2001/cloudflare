---
url: https://www.cloudflare.com/learning/bots/what-is-ad-fraud/
title: What Is Ad Fraud? | Ad Click Fraud
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:51.175071+00:00
---

# What Is Ad Fraud? | Ad Click Fraud

> Source: https://www.cloudflare.com/learning/bots/what-is-ad-fraud/

[ Learning Center ](https://www.cloudflare.com/learning/) / bots

##  What is ad fraud? | Ad click fraud 

Online advertising fraud is a major issue for digital ad networks. Click fraud is a common type of ad fraud used to scam ad networks. 

[Learning Center](https://www.cloudflare.com/learning)/bots/[How CAPTCHAs work | What does CAPTCHA mean?](https://www.cloudflare.com/learning/bots/how-captchas-work/)[How is an Internet bot constructed?](https://www.cloudflare.com/learning/bots/how-is-an-internet-bot-constructed/)[How to manage good bots | Good bots vs. bad bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/)[What is a bot?](https://www.cloudflare.com/learning/bots/what-is-a-bot/)[What is a bot attack?](https://www.cloudflare.com/learning/bots/what-is-a-bot-attack/)[What is a chatbot?](https://www.cloudflare.com/learning/bots/what-is-a-chatbot/)[What is a social media bot? | Social media bot definition](https://www.cloudflare.com/learning/bots/what-is-a-social-media-bot/)[What is a spam bot? | How spam comments and spam messages spread](https://www.cloudflare.com/learning/bots/what-is-a-spambot/)[What is a web crawler? | How web spiders work](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/)[What is ad fraud? | Ad click fraud](https://www.cloudflare.com/learning/bots/what-is-ad-fraud/)[What is bot traffic? | How to stop bot traffic](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/)[What is click fraud? | How click bots work](https://www.cloudflare.com/learning/bots/what-is-click-fraud/)[What is data scraping?](https://www.cloudflare.com/learning/bots/what-is-data-scraping/)[What is rate limiting? | Rate limiting and bots](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)[What is robots.txt? | How a robots.txt file works](https://www.cloudflare.com/learning/bots/what-is-robots-txt/)[What is bot management?](https://www.cloudflare.com/learning/bots/what-is-bot-management/)[What is credential stuffing?](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/)[What is content scraping?](https://www.cloudflare.com/learning/bots/what-is-content-scraping/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand what ad fraud is 
  * Learn about the different types of ad fraud, and how bots can be used for ad fraud 
  * Explore the differences between click fraud and ad fraud 



Related content  [ What is a spam bot? | How spam comments and spam messages spread ](https://www.cloudflare.com/learning/bots/what-is-a-spambot/)[ What is bot traffic? | How to stop bot traffic ](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/)[ How to manage good bots | Good bots vs. bad bots ](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/)[ What is a bot? ](https://www.cloudflare.com/learning/bots/what-is-a-bot/)[ What is bot management? ](https://www.cloudflare.com/learning/bots/what-is-bot-management/)

On this page

  * What is ad fraud?

  * What kinds of online advertising fraud are there?

  * How does bot-driven ad fraud work?

  * How is ad fraud related to click fraud?

  * How can bot management detect and prevent ad fraud?




## What is ad fraud?

Ad fraud is any attempt to defraud digital advertising networks for financial gain. Scammers often use [bots](https://www.cloudflare.com/learning/bots/what-is-a-bot/) to carry out ad fraud, but not always – there are a number of methods that scammers can use to trick advertisers and ad networks into paying them. Ad fraud that uses bots is typically [click fraud](https://www.cloudflare.com/learning/bots/what-is-click-fraud/).

## What kinds of online advertising fraud are there?

There are a variety of ways that cyber criminals can carry out ad fraud. Some of the methods include:

  * **Hidden ads:** When an ad is shown in such a way that the user doesn't actually see it. This kind of fraud targets ad networks that pay based on impressions (views), not clicks.

  * **Click hijacking:** This is when an attacker redirects a click on one ad to be a click for a different ad, effectively "stealing" the click. For this fraud attack to work, the attacker has to compromise the user's computer, the ad publisher's website, or a proxy server.


![Ad fraud click hijacking - attacker replaces Joe](https://images.ctfassets.net/slt3lc6tev37/4s5xt13tvwZsURN95LRj4C/4ad074bfe1d59f6a1b45ead1b75dd0f1/ad_fraud_click_hijacking.png)Ad fraud click hijacking - attacker replaces Joe

  * **Fake app installation:** Ads are often shown within applications, especially mobile apps. For this fraud method, teams of people (often in click farms*) install apps thousands of times and interact with them in bulk.

![Click farm app download - dozens of app downloads at once](https://images.ctfassets.net/slt3lc6tev37/3XWlTQTDvCq4UdTsamZfI4/69b478d0e546e2bf40db3bbfb95f7df2/click_farm_app_download.png)Click farm app download - dozens of app downloads at once

  * **Botnet ad fraud:** Scammers can use botnets to generate thousands of fake clicks on an ad, or fake visits to a website displaying the ads. See below for more on how this works.



*A click farm is a group of low-paid workers who click en masse on targeted links, usually at the direction of scammers or cyber attackers.

## How does bot-driven ad fraud work?

Scammers can use click bots to produce fake clicks on digital ads that appear on properties the scammers own, generating revenue for them.

Click bots are programmed to imitate real users and click on certain links. Often these bots are distributed across multiple devices in a [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/). In this way they appear more legitimate, since each bot will have a different [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) because it's coming from a different device.

A botnet is a group of Internet-connected devices that have been compromised by an attacker. Each device will have a bot installed on it, possibly in addition to other [malware](https://www.cloudflare.com/learning/ddos/glossary/malware/).

## How is ad fraud related to click fraud?

Often, ad fraud is a type of click fraud. Click fraud is a broader term that covers all kinds of use cases for fake clicks. It is typically carried out either by click bots or by a click farm – [social media bots](https://www.cloudflare.com/learning/bots/what-is-a-social-media-bot/) can be responsible for it as well. [Learn more about click fraud.](https://www.cloudflare.com/learning/bots/what-is-click-fraud/)

## How can bot management detect and prevent ad fraud?

[Cloudflare Bot Management](https://www.cloudflare.com/application-services/products/bot-management/) can use [machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) to judge user behavior against a baseline, and identify the "users" that are likely to actually be bots. Malicious bot activity can be filtered out, while real users and [good bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/) are allowed to continue interacting with a web property like normal.

Smaller sites can gain more visibility into and control over ad fraud with [Super Bot Fight Mode](https://www.cloudflare.com/pg-lp/bot-mitigation-fight-mode?utm_campaign=pgg221s-pl-super-bot-fight-lc), now available on Cloudflare Pro and Business plans.
