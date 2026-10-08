---
url: https://www.cloudflare.com/learning/ssl/why-use-https/
title: Why Use HTTPS?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:05:18.030406+00:00
---

# Why Use HTTPS?

> Source: https://www.cloudflare.com/learning/ssl/why-use-https/

[ Learning Center ](https://www.cloudflare.com/learning/) / SSL

##  Why use HTTPS? 

Browsers mark non-HTTPS sites as "Not secure", just one of many good reasons to secure a website. 

[Learning Center](https://www.cloudflare.com/learning)/SSL/[SSL certificate errors and how to fix them](https://www.cloudflare.com/learning/ssl/common-errors/)[What does 'Your connection is not private' mean?](https://www.cloudflare.com/learning/ssl/connection-not-private-explained/)[How does public key cryptography work?](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)[How does SSL work? | SSL certificates and TLS](https://www.cloudflare.com/learning/ssl/how-does-ssl-work/)[How does keyless SSL work?](https://www.cloudflare.com/learning/ssl/keyless-ssl/)[How do lava lamps help with Internet encryption?](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)[What is post-quantum cryptography (PQC)?](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/)[What is quantum computing?](https://www.cloudflare.com/learning/ssl/quantum/what-is-quantum-computing/)[What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)[Types of SSL certificates: SSL certificate types explained](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)[What happens in a TLS handshake? | SSL handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[What is a cryptographic key?](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/)[What is a session key? Session keys and TLS handshakes](https://www.cloudflare.com/learning/ssl/what-is-a-session-key/)[What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/)[What is domain spoofing? | Website and email spoofing](https://www.cloudflare.com/learning/ssl/what-is-domain-spoofing/)[What is encrypted SNI? | How ESNI works](https://www.cloudflare.com/learning/ssl/what-is-encrypted-sni/)[What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)[What is mixed content?](https://www.cloudflare.com/learning/ssl/what-is-mixed-content/)[What is mutual TLS (mTLS)?](https://www.cloudflare.com/learning/ssl/what-is-mutual-tls/)[What is SNI? How TLS server name indication works](https://www.cloudflare.com/learning/ssl/what-is-sni/)[What is SSL?](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[Why is HTTP not secure? | HTTP vs. HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)[Why use HTTPS?](https://www.cloudflare.com/learning/ssl/why-use-https/)[Why use TLS 1.3?](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3)[What is TLS?](https://www.cloudflare.com/learning/ssl/what-is-tls/)[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)

######  Learning objectives 

After reading this article you will be able to: 

  * Outline the changes to HTTPS traffic 
  * Explain the myths of HTTPS and the truth 
  * Understand the reasons to use HTTPS 



Related content  [ What is HTTPS? ](https://www.cloudflare.com/learning/ssl/what-is-https/)[ What is SSL? ](https://www.cloudflare.com/learning/ssl/what-is-ssl/)[ What is an SSL certificate? ](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)[ What happens in a TLS handshake? | SSL handshake ](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)[ How does keyless SSL work? ](https://www.cloudflare.com/learning/ssl/keyless-ssl/)

On this page

  * What is the difference between HTTP and HTTPS?

  * Reason No. 1: Website using HTTPS are more trustworthy for users.

    * Chrome and other browsers mark all HTTP websites as &quot

  * Reason No. 2: HTTPS is more secure, for both users and website owners.

  * Reason No. 3: HTTPS authenticates websites.

  * HTTPS myth-conceptions




## What is the difference between HTTP and HTTPS?

HTTPS is [HTTP](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/) with [TLS encryption](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/). HTTPS uses TLS ([SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)) to [encrypt](https://www.cloudflare.com/learning/ssl/what-is-encryption/) normal HTTP requests and responses, making it safer and more secure. A website that uses HTTPS has https:// in the beginning of its URL instead of http://, like <https://www.cloudflare.com>.

So, why should websites use [HTTPS](https://www.cloudflare.com/learning/ssl/what-is-https/)?

## Reason No. 1: Website using HTTPS are more trustworthy for users.

A website using HTTPS is like a restaurant displaying a "Pass" from the local food safety inspector: potential customers can trust that they can patronize the business without experiencing massively negative effects. And in this day and age, using HTTP is essentially like displaying a "Fail" food safety inspection sign: there's no guarantee that something terrible won't happen to a customer.

HTTPS uses the SSL/TLS protocol to encrypt communications so that attackers can't steal data. SSL/TLS also confirms that a website server is who it says it is, preventing impersonations. This stops multiple kinds of cyber attacks (just like food safety prevents illness).

Even though some users may be unaware of the benefits of SSL/TLS, modern browsers are making sure they're aware of the trustworthiness of a website no matter what.

#### Chrome and other browsers mark all HTTP websites as "not secure."

Google incrementally took steps to nudge websites towards incorporating HTTPS over a number of years. [Google also uses HTTPS as a quality factor](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html) in how they return search results; the more secure the website, the less likely the visitor will be making a mistake by clicking on the link Google provided.

Starting in July 2018 with the release of Chrome 68, all unsecured HTTP traffic has been flagged in the URL bar as “not secure”. This notification appears for all websites without a valid [SSL certificate](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/). Other browsers have followed suit.

## Reason No. 2: HTTPS is more secure, for both users and website owners.

With HTTPS, data is encrypted in transit in both directions: going to and coming from the [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/). The [protocol](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/) keeps communications secure so that malicious parties can't observe what data is being sent. As a result usernames and passwords can't be stolen in transit when users enter them into a form. If websites or web applications have to send sensitive or personal data to users (for instance, bank account information), encryption protects that data as well.

## Reason No. 3: HTTPS authenticates websites.

Users of rideshare apps such as Uber and Lyft don't have to get into an unfamiliar car on faith, just because the driver says they're there to pick them up. Instead the apps tell them information about the driver, like their name and appearance, what kind of car they drive, and the license plate number. User can check these things and be certain they are getting into the right car, even though every rideshare car is different and they've never seen the driver before.

Similarly, when a user navigates to a website, what they're actually doing is connecting to faraway computers that they don't know about, maintained by people they've never seen. An SSL certificate, which enables HTTPS, is like that driver information in the rideshare app. It represents external verification by a trustworthy third party that a web server is who it claims to be.

This prevents attacks in which an attacker impersonates or spoofs a website, making users think they're on the site they intended to reach when actually they're on a fake site. HTTPS authentication also does a lot to help a company website appear legitimate, and that influences user attitudes towards the company itself.

## HTTPS myth-conceptions

Many websites have been slow to adopt HTTPS. To explore why this is the case we have to look at the history.

When HTTPS initially began rolling out, proper implementation was hard, slow, and expensive; it was hard to implement properly, slowed down Internet requests, and increased costs by requiring expensive certificate services. None of these impediments remain true, but a lingering fear still exists for a lot of website owners, which has impeded some taking the leap into better security. Let’s explore some of the myths about HTTPS.

**"I don’t handle sensitive information on my website so I don’t need HTTPS"**

A common reason websites don’t implement security is because they think it’s overkill for their purposes. After all, if you’re not dealing with sensitive data, who cares if someone is snooping? There are a few reasons that this is an overly simplistic view on web security. For example, some Internet service providers will actually inject advertising into HTTP-served websites. These ads may or may not be in line with the content of the website, and can potentially be offensive, aside from the fact that the website provider has no creative input or share of the revenue. These injected ads are no longer feasible once a site is secured.

Modern web browsers now limit functionality for sites that are not secure. Important features that improve the quality of the website now require HTTPS. Geolocation, push notifications and the service workers needed to run progressive web applications (PWAs) all require heightened security. This makes sense; data such as a user’s [location is sensitive](https://developers.google.com/web/updates/2016/04/geolocation-on-secure-contexts-only/) and can be used for nefarious purposes.

**"I don’t want to damage my website's performance by increasing my page load times"**

Performance is an important factor in both user experience and how Google returns results in search. Understandably, increasing [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) is something to take seriously. Luckily, over time improvements have been made to HTTPS to reduce the performance overhead required to set up a encrypted connection.

When an HTTP connection occurs, there are a number of trips the connection needs to make between the client requesting the webpage and the server. Aside from the normal latency associated with a [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) handshake (shown in blue below), an additional TLS/SSL handshake (shown in yellow) must occur to use HTTPS.

![TCP handshake](https://www.cloudflare.com/img/learning/cdn/tls-ssl/tls-ssl-handshake.png)TCP handshake

Improvements have been implemented in TLS to reduce the total latency of creating a connection, including TLS session resumption and TLS false start.

By using session resumption a server can keep a connection alive for longer by resuming the same session for additional requests. Keeping the connection alive saves time spent renegotiating the connection when the client requires an uncached origin fetch, reducing the total [RTT](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/) by 50%.

Another improvement to the speed at which an encrypted channel can be created is to implement a process called TLS false start, which cuts down on the latency by sending the encrypted data before the client has finished authentication. For more information [explore how TLS/SSL works on a CDN](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/).

Finally, [TLS 1.3](https://www.cloudflare.com/learning/ssl/why-use-tls-1.3/) offers even more significant performance improvements. TLS handshakes in TLS 1.3 only require one round trip — and if the client has connected previously, _zero_ round trips. Signing up for Cloudflare makes it easy to activate TLS 1.3 for a web property.

**"It’s too expensive for me to implement HTTPS"**

At one point this may have been true, but now the cost is no longer a concern; Cloudflare [offers websites the ability to encrypt transit free of charge](https://www.cloudflare.com/application-services/products/ssl/). We were the first to provide SSL at no cost, and we continue to do so. By improving Internet security at large, we are able to help make the Internet safer and faster.

**"I’m going to lose search ranking while migrating my site to HTTPS"**

There are risks associated with website migration, and done improperly a negative SEO impact is possible. Potential pitfalls include website downtime, uncrawled webpages, and penalization for content duplication when two copies of the site exist at the same time. That said, websites can be migrated safely to HTTPS by following best practices.

Two of the most important migration practices are:

  1. using 301 redirects and 2) the proper placement of canonical tags. By using server 301 redirects on the HTTP site to point to the HTTPS version, a website tells Google to move to the new location for all search and indexing purposes. By placing canonical tags on the HTTPS site only, crawlers such as Googlebot will know that the new secure content should be considered canonical going forward.



If you have a large number of pages and are concerned that the recrawl will take too long, reach out to Google and tell them how much traffic you’re willing to put through your website. The network engineers will then crank up the crawl rate to help parse your site quickly and get it indexed.
