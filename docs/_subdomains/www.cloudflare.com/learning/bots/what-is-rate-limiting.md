---
url: https://www.cloudflare.com/learning/bots/what-is-rate-limiting/
title: What Is Rate Limiting? | Rate Limiting and Bot
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:10.817339+00:00
---

# What Is Rate Limiting? | Rate Limiting and Bot

> Source: https://www.cloudflare.com/learning/bots/what-is-rate-limiting/

[ Learning Center ](https://www.cloudflare.com/learning/) / bots

##  What is rate limiting? | Rate limiting and bots 

Rate limiting blocks users, bots, or applications that are over-using or abusing a web property. Rate limiting can stop certain kinds of bot attacks. 

[Learning Center](https://www.cloudflare.com/learning)/bots/[How CAPTCHAs work | What does CAPTCHA mean?](https://www.cloudflare.com/learning/bots/how-captchas-work/)[How is an Internet bot constructed?](https://www.cloudflare.com/learning/bots/how-is-an-internet-bot-constructed/)[How to manage good bots | Good bots vs. bad bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/)[What is a bot?](https://www.cloudflare.com/learning/bots/what-is-a-bot/)[What is a bot attack?](https://www.cloudflare.com/learning/bots/what-is-a-bot-attack/)[What is a chatbot?](https://www.cloudflare.com/learning/bots/what-is-a-chatbot/)[What is a social media bot? | Social media bot definition](https://www.cloudflare.com/learning/bots/what-is-a-social-media-bot/)[What is a spam bot? | How spam comments and spam messages spread](https://www.cloudflare.com/learning/bots/what-is-a-spambot/)[What is a web crawler? | How web spiders work](https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/)[What is ad fraud? | Ad click fraud](https://www.cloudflare.com/learning/bots/what-is-ad-fraud/)[What is bot traffic? | How to stop bot traffic](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/)[What is click fraud? | How click bots work](https://www.cloudflare.com/learning/bots/what-is-click-fraud/)[What is data scraping?](https://www.cloudflare.com/learning/bots/what-is-data-scraping/)[What is rate limiting? | Rate limiting and bots](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)[What is robots.txt? | How a robots.txt file works](https://www.cloudflare.com/learning/bots/what-is-robots-txt/)[What is bot management?](https://www.cloudflare.com/learning/bots/what-is-bot-management/)[What is credential stuffing?](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/)[What is content scraping?](https://www.cloudflare.com/learning/bots/what-is-content-scraping/)

######  Learning objectives 

After reading this article you will be able to: 

  * Understand the purpose of rate limiting 
  * Learn how rate limiting works 
  * Learn some practical applications of rate limiting 
  * Explain the difference between rate limiting and other kinds of bot management 



Related content  [ What is click fraud? | How click bots work ](https://www.cloudflare.com/learning/bots/what-is-click-fraud/)[ What is bot traffic? | How to stop bot traffic ](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/)[ What is bot management? ](https://www.cloudflare.com/learning/bots/what-is-bot-management/)[ How to manage good bots | Good bots vs. bad bots ](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/)[ What is a spam bot? | How spam comments and spam messages spread ](https://www.cloudflare.com/learning/bots/what-is-a-spambot/)

On this page

  * What is rate limiting?

  * What kinds of bot attacks are stopped by rate limiting?

  * How does rate limiting work?

  * What is an IP address?

  * How does rate limiting work with user logins?

  * How does rate limiting work for APIs?

  * How do social media platforms like X and Instagram use rate limiting?

  * What is the difference between bot management and rate limiting?

  * FAQs

    * What is rate limiting?

    * How does rate limiting work?

    * What types of bot attacks can rate limiting help stop?

    * Why is rate limiting used for user logins?

    * How is rate limiting applied to APIs?

    * What is the difference between rate limiting and bot management?




## What is rate limiting?

![Rate limiting on speed limit sign next to road - 75 requests per minute](https://images.ctfassets.net/slt3lc6tev37/2gsdcTziAsmnUhQRiwrn5u/0f022b566241195b26d07cab66f6a90b/what_is_rate_limiting_illustration.svg)Rate limiting on speed limit sign next to road - 75 requests per minute

Rate limiting is a strategy for limiting network traffic. It puts a cap on how often someone can repeat an action within a certain timeframe – for instance, trying to log in to an account. Rate limiting can help stop certain kinds of malicious [bot activity](https://www.cloudflare.com/learning/bots/what-is-a-bot/). It can also reduce strain on web servers. However, rate limiting is not a complete solution for [managing bot activity](https://www.cloudflare.com/learning/bots/what-is-bot-management/).

## What kinds of bot attacks are stopped by rate limiting?

Rate limiting is often employed to stop [bad bots](https://www.cloudflare.com/learning/bots/how-to-manage-good-bots/) from negatively impacting a website or application. Bot attacks that rate limiting can help mitigate include:

  * [Brute force attacks](https://www.cloudflare.com/learning/bots/brute-force-attack/)

  * [DoS](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/) and [DDoS](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attacks

  * [Web scraping](https://www.cloudflare.com/learning/bots/what-is-data-scraping/)




Rate limiting also protects against [API](https://www.cloudflare.com/learning/security/api/what-is-an-api/) overuse, which is not necessarily malicious or due to bot activity, but is important to prevent nonetheless.

## How does rate limiting work?

Rate limiting runs within an application, rather than running on the web server itself. Typically, rate limiting is based on tracking the IP addresses that requests are coming from, and tracking how much time elapses between each request. The [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) is the main way an application identifies who or what is making the request.

A rate limiting solution measures the amount of time between each request from each IP address, and also measures the number of requests within a specified timeframe. If there are too many requests from a single IP within the given timeframe, the rate limiting solution will not fulfill the IP address's requests for a certain amount of time.

Essentially, a rate-limited application will say, "Hey, slow down," to unique users that are making requests at a rapid rate. This is comparable to a police officer who pulls over a driver for exceeding the road's speed limit, or to a parent who tells their child not to eat so much candy in such a short span of time.

## What is an IP address?

An IP address is the unique numerical (or, in IPv6, alphanumerical) identifier assigned to any device that connects to the Internet. Every device will have its own IP address for as long as it's online, and like a physical street address or a phone number, this enables devices to send messages back and forth. A traditional (IPv4) address looks like this: 198.41.129.1

For user devices, IP addresses are typically not permanent, because there are not enough IP addresses to go around in IPv4. Instead, the user's Internet service provider (ISP) will dynamically assign addresses as devices connect to the Internet.

A rate limiting solution may use an IP address as a basis for determining which devices are making too many requests and should be temporarily blocked.

## How does rate limiting work with user logins?

Users may find themselves locked out of an account if they unsuccessfully attempt to log in too many times in a short amount of time. This occurs when a website has login rate limiting in place.

This precaution exists, not to frustrate users who have forgotten their passwords, but to block [brute force attacks](https://www.cloudflare.com/learning/bots/brute-force-attack/) in which a bot tries thousands of different passwords in order to guess the correct one and break into the account. If a bot can only make 3 or 4 login attempts an hour, then such an attack is statistically unlikely to be successful.

Rate limiting on a login page can be applied according to the IP address of the user trying to log in, or according to the user's username. Ideally it would use a combination of the two, because:

  * If rate limiting is only applied by IP address, brute force attackers could bypass this by attempting logins from multiple IP addresses (perhaps by using a [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/)).

  * If it's only done by username, any attacker that has a list of known usernames can try a variety of commonly used passwords with those usernames and is likely to successfully break into at least a few accounts, all from the same IP address.




Because rate limiting is necessary to prevent these brute force attacks, users who can't remember their passwords may be rate limited along with malicious bots. Users will likely see a "too many login attempts" message of some sort and be prompted to try again within a specified timeframe, or be advised that they are locked out of their accounts altogether.

## How does rate limiting work for APIs?

An API, or application programming interface, is a way to request functionality from a program. APIs are invisible to most users, but they're extremely important for applications to function properly. For example, a restaurant's website could rely upon the API of a table reservation service to enable customers to make reservations online. Or, an [ecommerce platform](https://www.cloudflare.com/retail/) could integrate a shipping company's API to provide users with accurate shipping costs.

Every time an API responds to a request, the owner of that API has to pay for compute time: the server resources required for code to run and produce a response to that API request. In the example above, the restaurant's API integration will cause the table reservation service to pay for compute time whenever a restaurant customer makes a reservation.

For this reason, any application or service that offers an API for developers will have limitations on how many [API calls](https://www.cloudflare.com/learning/security/api/what-is-api-call/) can be made per hour or day by each unique user. In this way, third-party developers don't overuse an API.

Rate limiting can also motivate developers to pay more for leveraging the API: often they can only make so many API calls before paying more for the API service.

Rate limiting for APIs helps protect against malicious bot attacks as well. An attacker can use bots to make so many repeated calls to an API that it renders the service unavailable for anyone else, or crashes the service altogether. This is a type of DoS or DDoS attack.

## How do social media platforms like X (Twitter) and Instagram use rate limiting?

Social media platform rate limiting is often similar to API rate limiting. Any third-party application that integrates X (formerly known as Twitter), for instance, can only refresh to look for new posts or messages a certain amount of times per hour. Instagram has similar limits for third-party apps. This is why users may occasionally encounter "rate limit exceeded" messages.

## What is the difference between bot management and rate limiting?

Rate limiting is fairly one dimensional: While useful, it can only stop very specific types of bot activity. Additionally, rate limiting is not just for bots, but for limiting usage in general. [Cloudflare Rate Limiting](https://www.cloudflare.com/application-services/products/rate-limiting/), for instance, protects against DDoS attacks, API abuse, and brute force attacks, but it doesn't necessarily mitigate other forms of malicious bot activity, and it doesn't distinguish between good bots and bad bots.

In contrast, bot management can holistically detect bot activity in general. For instance, [Cloudflare Bot Management](https://www.cloudflare.com/application-services/products/bot-management/) uses [machine learning](https://www.cloudflare.com/learning/ai/what-is-machine-learning/) to identify likely bots, which enables it to block a wider variety of bot attacks (like [credential stuffing](https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/), [spam posting](https://www.cloudflare.com/learning/bots/what-is-a-spambot/), inventory hoarding, etc.).Smaller organizations can also block bad bots with [Super Bot Fight Mode](https://www.cloudflare.com/pg-lp/bot-mitigation-fight-mode?utm_campaign=pgg221s-pl-super-bot-fight-lc), available on the Cloudflare Pro and Business plans.

## FAQs

#### What is rate limiting?

Rate limiting is a security strategy used to control network traffic by putting a cap on how many times someone can repeat an action within a certain amount of time. Rate limiting can help stop certain kinds of malicious bot activity and reduce strain on web servers.

#### How does rate limiting work?

A rate limiting solution typically tracks the IP addresses of incoming requests and measures the time between each request from a single IP address. If too many requests are made from one IP address within a set timeframe, the solution will temporarily stop fulfilling requests from that source.

#### What types of bot attacks can rate limiting help stop?

Rate limiting is often used to mitigate abusive bot behavior such as brute force attacks, denial of service (DoS and DDoS) attacks, and web scraping.

#### Why is rate limiting used for user logins?

Websites use rate limiting on their login pages to block brute force attacks. If a user unsuccessfully tries to log in too many times in a short period, they are temporarily locked out. This prevents a bot from trying thousands of different passwords to break into an account.

#### How is rate limiting applied to APIs?

Rate limiting solutions protect APIs from overuse and malicious bot attacks. An attacker could use bots to make so many repeated calls to an API that the service becomes unavailable or crashes. Rate limiting prevents this by capping the number of requests an API will accept in a given timeframe.

#### What is the difference between rate limiting and bot management?

Rate limiting is a specific tactic that is effective for stopping only certain types of bot activity. In contrast, a bot management solution is a more comprehensive approach that can holistically detect and manage all kinds of malicious bot activity.
