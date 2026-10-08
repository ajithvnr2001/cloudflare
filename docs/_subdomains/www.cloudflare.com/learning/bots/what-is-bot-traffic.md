---
url: https://www.cloudflare.com/learning/bots/what-is-bot-traffic/
title: What Is Bot Traffic? | How to Stop Bot Traffic
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:54.164824+00:00
---

# What Is Bot Traffic? | How to Stop Bot Traffic

> Source: https://www.cloudflare.com/learning/bots/what-is-bot-traffic/

[ Learning Center ](https://www.cloudflare.com/learning/) / bots

##  What is bot traffic? | How to stop bot traffic 

Bot traffic is non-human traffic to a website. While some bot traffic is beneficial, abusive bot traffic can be very disruptive. 

[Learning Center](https://www.cloudflare.com/learning)/bots/[How CAPTCHAs work | What does CAPTCHA mean?](https://www.cloudflare.com/learning/bots/how-captchas-work/)[How is an Internet bot constructed?](https://www.cloudflare.com/learning/bots/how-is-an-internet-bot-constructed/)[How to manage good bots | Good bots vs. bad bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/)[What is a bot?](https://www.cloudflare.com/learning/bots/what-is-a-bot/)[What is a bot attack?](https://www.cloudflare.com/learning/bots/what-is-a-bot-attack/)[What is a chatbot?](https://www.cloudflare.com/learning/bots/what-is-a-chatbot/)[What is a social media bot? | Social media bot definition](https://www.cloudflare.com/learning/bots/what-is-a-social-media-bot/)[What is a spam bot? | How spam comments and spam messages spread](https://www.cloudflare.com/learning/bots/what-is-a-spambot/)[What is a web crawler? | How web spiders work](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/)[What is ad fraud? | Ad click fraud](https://www.cloudflare.com/learning/bots/what-is-ad-fraud/)[What is bot traffic? | How to stop bot traffic](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/)[What is click fraud? | How click bots work](https://www.cloudflare.com/learning/bots/what-is-click-fraud/)[What is data scraping?](https://www.cloudflare.com/learning/bots/what-is-data-scraping/)[What is rate limiting? | Rate limiting and bots](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)[What is robots.txt? | How a robots.txt file works](https://www.cloudflare.com/learning/bots/what-is-robots-txt/)[What is bot management?](https://www.cloudflare.com/learning/bots/what-is-bot-management/)[What is credential stuffing?](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/)[What is content scraping?](https://www.cloudflare.com/learning/bots/what-is-content-scraping/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define bot traffic. 
  * Understand how to identify bot traffic. 
  * Outline the negative consequences of malicious bots. 
  * Learn how to stop bot traffic. 



Related content  [ What is a bot? ](https://www.cloudflare.com/learning/bots/what-is-a-bot/)[ What is bot management? ](https://www.cloudflare.com/learning/bots/what-is-bot-management/)[ What is credential stuffing? ](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/)[ What is content scraping? ](https://www.cloudflare.com/learning/bots/what-is-content-scraping/)[ What is data scraping? ](https://www.cloudflare.com/learning/bots/what-is-data-scraping/)

On this page

  * What is bot traffic?

  * How can bot traffic be identified?

  * How can bot traffic hurt analytics?

  * How to filter bot traffic from Google Analytics

  * How can bot traffic hurt performance?

  * How can bot traffic be bad for business?

  * How can websites manage bot traffic?

  * FAQs

    * What is bot traffic?

    * How can I tell if my website is receiving bot traffic?

    * Are all bots bad?

    * How can bot traffic negatively affect my website?

    * How can I manage bot traffic on my site?

    * What is a robots.txt file?




## What is bot traffic?

Bot traffic describes any non-human traffic to a website or an app. The term bot traffic often carries a negative connotation, but in reality bot traffic is not necessarily good or bad; it all depends on the purpose of the [bots](https://www.cloudflare.com/learning/bots/what-is-a-bot/) and the preferences of the website operator.

Some bots are essential for useful services such as search engines and digital assistants (e.g. Siri, Alexa). Most companies welcome these sorts of bots on their sites.

Other bots can be malicious, for example those used for the purposes of [credential stuffing](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/), [data scraping](https://www.cloudflare.com/learning/bots/what-is-data-scraping/), and launching [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/). Even some of the more benign ‘bad’ bots, such as unauthorized web crawlers, can be a nuisance because they can disrupt site analytics and generate click fraud.

It is believed that over 40% of all Internet traffic is comprised of bot traffic, and a significant portion of that is malicious bots. This is why so many organizations are looking for ways to manage the bot traffic coming to their sites.

## How can bot traffic be identified?

Web engineers can look directly at network requests to their sites and identify likely bot traffic. An integrated web analytics tool, such as Google Analytics or Heap, can also help to detect bot traffic.

The following analytics anomalies are the hallmarks of bot traffic:

  * **Abnormally high pageviews:** If a site undergoes a sudden, unprecedented and unexpected spike in pageviews, it’s likely that there are bots clicking through the site.

  * **Abnormally high bounce rate:** The bounce rate identifies the number of users that come to a single page on a site and then leave the site before clicking anything on the page. An unexpected lift in the bounce rate can be the result of bots being directed at a single page.

  * **Surprisingly high or low session duration:** Session duration, or the amount of time users stay on a website, should remain relatively steady. An unexplained increase in session duration could be an indication of bots browsing the site at an unusually slow rate. Conversely, an unexpected drop in session duration could be the result of bots that are clicking through pages on the site much faster than a human user would.

  * **Junk conversions:** A surge in phony-looking conversions, such as account creations using gibberish email addresses or contact forms submitted with fake names and phone numbers, can be the result of form-filling bots or spam bots.

  * **Spike in traffic from an unexpected location:** A sudden spike in users from one particular region, particularly a region that’s unlikely to have a large number of people who are fluent in the native language of the site, can be an indication of bot traffic.




Under Attack?

Comprehensive protection against cyber attacks

[Talk to an expert](https://www.cloudflare.com/under-attack-hotline/)

## How can bot traffic hurt analytics?

As mentioned above, unauthorized bot traffic can impact analytics metrics such as page views, bounce rate, session duration, geolocation of users, and [conversions](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/). These deviations in metrics can create a lot of frustration for the site owner; it is very hard to measure the performance of a site that’s being flooded with bot activity. Attempts to improve the site, such as A/B testing and conversion rate optimization, are also crippled by the statistical noise created by bots.

## How to filter bot traffic from Google Analytics

Google Analytics does provide an option to “exclude all hits from known bots and spiders” ([spiders](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/) are search engine bots that crawl webpages). If the source of the bot traffic can be identified, users can also provide a specific list of IPs to be ignored by Google Analytics.

While these measures will stop some bots from disrupting analytics, they will not stop all bots. Furthermore, most malicious bots pursue an objective besides disrupting traffic analytics, and these measures do nothing to mitigate harmful bot activity outside of preserving analytics data.

## How can bot traffic hurt performance?

Sending massive amounts of bot traffic is a very common way for attackers to launch a DDoS attack. During some types of DDoS attacks, so much attack traffic is directed at a website that the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) becomes overloaded, and the site becomes slow or altogether unavailable for legitimate users.

## How can bot traffic be bad for business?

Some websites can be financially crippled by malicious bot traffic, even if their performance is unaffected. Sites that rely on advertising and sites that sell merchandise with limited inventory are particularly vulnerable.

For sites that serve ads, bots that land on the site and click on various elements of the page can trigger fake ad clicks; this is known as [click fraud](https://www.cloudflare.com/learning/bots/what-is-click-fraud/). While this may initially result in a boost in ad revenue, online advertising networks are very good at detecting bot clicks. If they suspect a website is committing click fraud, they will take action, usually in the form of banning that site and its owner from their network. For this reason, owners of sites that host ads need to be ever-wary of bot click fraud.

Sites with limited inventory can be targeted by inventory hoarding bots. As the name suggests, these bots go to [e-commerce sites](https://www.cloudflare.com/retail/) and dump tons of merchandise into their shopping carts, making that merchandise unavailable for purchase by legitimate shoppers. In some cases this can also trigger unnecessary restocking of inventory from a supplier or manufacturer. The inventory hoarding bots never make a purchase; they are simply designed to disrupt the availability of inventory.

Many websites have relied on producing original content to attract user traffic and generate revenue from that traffic, sometimes from ads. The spike in usage of [AI](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/) tools in the 2020s has negatively impacted such business models. AI tools use original content from the web to train their underlying [large language models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/), build search indexes for use in connection with those models, and retrieve content in real time in response to user prompts. Users who receive responses from LLMs may never visit the websites on whose content the response was based. AI crawler bots that source original content can also impose direct costs on website operators, as they can send lots of requests for webpages.

## How can websites manage bot traffic?

The first step to stopping or managing bot traffic to a website is for a website administrator to declare their preferences in a [robots.txt file](https://www.cloudflare.com/learning/bots/what-is-robots-txt/). Robots.txt files provide instructions for bots crawling the page, and they can be configured to instruct bots that they should not visit or interact with certain webpages. But it should be noted that only some bots abide by the rules in robots.txt files; those files do not actually prevent bots from crawling websites. Cloudflare offers a sophisticated [managed robots.txt service](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/) to help website administrators express their preferences to crawler operators.

To [police traffic from AI crawler bots](https://www.cloudflare.com/the-net/ai-secure/), website operators should use a service like [AI Audit from Cloudflare](https://developers.cloudflare.com/ai-audit/). This service allows website operators to either [allow or block AI crawlers](https://www.cloudflare.com/the-net/building-cyber-resilience/regain-control-ai-crawlers/) ([blocking](https://www.cloudflare.com/learning/ai/how-to-block-ai-crawlers/) means the AI crawlers cannot access content for any purpose). AI Audit’s [pay per crawl](https://www.cloudflare.com/paypercrawl-signup/) feature also lets website operators charge AI bot operators for crawling, if they wish to do so.

A number of other tools also can mitigate abusive bot traffic. A rate limiting solution, like Cloudflare's [WAF](https://www.cloudflare.com/application-services/products/waf/) product, can detect and prevent high-volume, abusive bot traffic originating from a single IP address.

Network engineers also can review traffic, manually identifying suspicious network requests originating from a range of IP addresses and all requests from those IP addresses. This is a very labor-intensive process, however, and it is unlikely to stop the majority of malicious bot traffic that a website may face.

Separate from rate limiting and direct engineer intervention, the easiest and most effective way to stop bad bot traffic is with a [bot management](https://www.cloudflare.com/learning/bots/what-is-bot-management/) solution. A bot management solution can leverage intelligence and use behavioral analysis to stop malicious bots before they ever reach a website. For example, [Cloudflare Bot Management](https://www.cloudflare.com/application-services/products/bot-management/) uses intelligence from millions of Internet properties and applies [machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) to proactively identify and stop bot abuse. [Super Bot Fight Mode](https://www.cloudflare.com/pg-lp/bot-mitigation-fight-mode?utm_campaign=pgg221s-pl-super-bot-fight-lc), available on Pro and Business plans, offers smaller organizations similar visibility and control over their bot traffic.

## FAQs

#### What is bot traffic?

Bot traffic refers to any non-human activity on a website or application. Bot traffic is not inherently good or bad; it depends on the purpose of the bot, with some bots being essential for services like search engines and others being malicious.

#### How can I tell if my website is receiving bot traffic?

You can identify bot traffic by looking for anomalies in your website analytics. Key signs include abnormally high pageviews or bounce rates, sudden changes in session duration, a spike in junk conversions, or a sudden surge in traffic from an unexpected geographic location.

#### Are all bots bad?

Some bots are beneficial and even essential. For example, search engine bots (also called spiders or crawlers) are necessary for a website to be indexed and appear in search results. However, malicious bots can perform harmful actions like scraping data, stuffing credentials, and launching DDoS attacks.

#### How can bot traffic negatively affect my website?

Malicious bot traffic can hurt your website in several ways. It can skew your analytics, making it difficult to measure performance. Malicious bots can also harm site performance by overloading your server. For businesses, bots can commit click fraud on ads or hoard inventory on ecommerce sites, disrupting sales.

#### How can I manage bot traffic on my site?

A starting point is to use a robots.txt file to provide instructions to bots, though this is not a foolproof method as malicious bots will ignore it. More effective tools include rate limiting to block high-volume traffic and, most effectively, a dedicated bot management solution that uses machine learning and behavioral analysis to distinguish between good and bad bots.

#### What is a robots.txt file?

A robots.txt file is a set of instructions for bots that visit your website. In this file, you can specify rules, such as which pages bots are not allowed to crawl. While good bots will follow these rules, many bad bots will not.
