---
url: https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/
title: What is Anycast? | How does Anycast work? | Cloudflare
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (142 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:27:08.380537+00:00
---

# What is Anycast? | How does Anycast work? | Cloudflare

> Source: https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/

Preview Mode
[Documentation](https://staging.mrk.cfdata.org/mrk/redwood-blade-repository/)
# What is Anycast? | How does Anycast work?
Anycast is a network addressing and routing method in which incoming requests can be routed to a variety of different locations.
#### Learning Objectives
After reading this article you will be able to:
  * Explain Anycast network routing
  * Differentiate between Anycast and Unicast
  * See how Anycast mitigates DDoS attacks


Related Content
* * *
[What is a CDN? ](https://www.cloudflare.com/en-gb/learning/cdn/what-is-a-cdn/)[CDN performance](https://www.cloudflare.com/en-gb/learning/cdn/performance/)[Origin server](https://www.cloudflare.com/en-gb/learning/cdn/glossary/origin-server/)[What is an edge server?](https://www.cloudflare.com/en-gb/learning/cdn/glossary/edge-server/)[What is a CDN data center?](https://www.cloudflare.com/en-gb/learning/cdn/glossary/data-center/)
#### Want to keep learning?
Subscribe to theNET, Cloudflare's monthly recap of the Internet's most popular insights!
Email: *
Must be a valid business email.
Subscribe to theNET
The information you provide to Cloudflare is governed by the terms of our [Privacy Policy](https://www.cloudflare.com/privacypolicy/).
Copy article link 
## What is Anycast?
Anycast is a network addressing and routing method in which incoming requests can be routed to a variety of different locations or “nodes.” In the context of a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), Anycast typically routes incoming traffic to the nearest [data center](https://www.cloudflare.com/learning/cdn/glossary/data-center/) with the capacity to process the request efficiently. Selective routing allows an Anycast network to be resilient in the face of high traffic volume, network congestion, and [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/).
![Anycast CDN diagram](https://www.cloudflare.com/img/learning/cdn/glossary/anycast/anycast-cdn.png)
## How does Anycast work?
Anycast network routing is able to route incoming connection requests across multiple data centers. When requests come into a single [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) associated with the Anycast network, the network distributes the data based on some prioritization methodology. The selection process behind choosing a particular data center will typically be optimized to reduce [latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) by selecting the data center with the shortest distance from the requester. Anycast is characterized by a 1-to-1 of many association, and is one of the 5 main network protocol methods used in the Internet protocol.
## Why use an Anycast network?
If many requests are made simultaneously to the same [origin server](https://www.cloudflare.com/learning/cdn/glossary/origin-server/), the server may become overwhelmed with traffic and be unable to respond efficiently to additional incoming requests. With an Anycast network, instead of one origin server taking the brunt of the traffic, the load can also be spread across other available data centers, each of which will have servers capable of processing and responding to the incoming request. This [routing](https://www.cloudflare.com/learning/network-layer/what-is-routing/) method can prevent an origin server from extending capacity and avoids service interruptions to clients requesting content from the origin server.
## What is the difference between Anycast and Unicast?
Most of the Internet works via a routing scheme called Unicast. Under Unicast, every node on the network gets a unique IP address. Home and office networks use Unicast; when a computer is connected to a wireless network and gets a message saying the IP address is already in use, an IP address conflict has occurred because another computer on the same Unicast network is already using the same IP. In most cases, that isn't allowed.
![Unicast CDN diagram](https://www.cloudflare.com/img/learning/cdn/glossary/anycast/unicast-cdn.png)
When a CDN is using a Unicast address, traffic is routed directly to the specific node. This creates a vulnerability when the network experiences extraordinary traffic such as during a DDoS attack. Because the traffic is routed directly to a particular data center, the location or its surrounding infrastructure may become overwhelmed with traffic, potentially resulting in [denial-of-service](https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/) to legitimate requests.
Using Anycast means the network can be extremely resilient. Because traffic will find the best path, an entire data center can be taken offline and traffic will automatically flow to a proximal data center.
## How does an Anycast network mitigate a DDoS attack?
After other DDoS mitigation tools filter out some of the attack traffic, Anycast distributes the remaining attack traffic across multiple data centers, preventing any one location from becoming overwhelmed with requests. If the capacity of the Anycast network is greater than the attack traffic, the attack is effectively mitigated. In most DDoS attacks, many compromised "zombie" or [“bot”](https://www.cloudflare.com/learning/bots/what-is-a-bot/) computers are used to form what is known as a [botnet](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/). These machines can be scattered around the web and generate so much traffic that they can overwhelm a typical Unicast-connected machine.
![Anycast/Unicast under attack](https://www.cloudflare.com/img/learning/cdn/glossary/anycast/anycast-unicast-botnet-attack.png)
A properly Anycasted CDN increases the surface area of the receiving network so that the unfiltered denial-of-service traffic from a distributed botnet will be absorbed by each of the CDN’s data centers. As a result, as a network continues to grow in size and capacity it becomes harder and harder to launch an effective DDoS against anyone using the CDN.
It is not easy to setup a true Anycasted network. Proper implementation requires that a CDN provider maintains their own network hardware, builds direct relationships with their upstream carriers, and tunes their networking routes to ensure traffic doesn't "flap" between multiple locations. This [Cloudflare blog post](https://blog.cloudflare.com/cloudflares-architecture-eliminating-single-p/) explains how Cloudflare uses Anycast to load balance without load balancers.
#### Subscribe to theNET
Receive a monthly recap of the most popular Internet insights!
Email: *
Must be a valid business email.
Subscribe
The information you provide to Cloudflare is governed by the terms of our [Privacy Policy](https://www.cloudflare.com/privacypolicy/).
GETTING STARTED
  * [Free plans](https://www.cloudflare.com/plans/free/)
  * [Small business plans](https://www.cloudflare.com/small-business/)
  * [For enterprises](https://www.cloudflare.com/enterprise/)
  * [Get a recommendation](https://www.cloudflare.com/about-your-website/)
  * [Request a demo](https://www.cloudflare.com/plans/enterprise/demo/)
  * [Contact sales](https://www.cloudflare.com/plans/enterprise/contact/)


About CDNs
  * [What is a CDN? ](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
  * [What is a reverse proxy?](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)
  * [Static vs. dynamic caching](https://www.cloudflare.com/learning/cdn/caching-static-and-dynamic-content/)


CDN Features
  * [CDN performance](https://www.cloudflare.com/learning/cdn/performance/)
  * [CDN SSL TLS security](https://www.cloudflare.com/learning/cdn/cdn-ssl-tls-security/)
  * [CDN reliability](https://www.cloudflare.com/learning/cdn/cdn-load-balance-reliability/)
  * [CDN benefits summary](https://www.cloudflare.com/learning/cdn/cdn-benefits/)
  * [CDN for WordPress](https://www.cloudflare.com/learning/cdn/cdn-for-wordpress/)


CDN Servers
  * [What is a data center?](https://www.cloudflare.com/learning/cdn/glossary/data-center/)
  * [What is an edge server?](https://www.cloudflare.com/learning/cdn/glossary/edge-server/)
  * [What is an origin server?](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)


CDN Glossary
  * [Anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/)
  * [Internet exchange point (IXP)](https://www.cloudflare.com/learning/cdn/glossary/internet-exchange-point-ixp/)
  * [Round-trip time (RTT)](https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/)
  * [Time-to-live (TTL)](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/)
  * [Cache control](https://www.cloudflare.com/learning/cdn/glossary/what-is-cache-control/)
  * [GSLB](https://www.cloudflare.com/learning/cdn/glossary/global-server-load-balancing-gslb/)
  * [Common CDN issues](https://www.cloudflare.com/learning/cdn/common-cdn-issues/)


Learning Center Navigation
  * [Learning Center Home](https://www.cloudflare.com/learning/)
  * [DDoS Learning Center](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/)
  * [What is DNS Learning Center](https://www.cloudflare.com/learning/dns/what-is-dns/)
  * [Security Learning Center](https://www.cloudflare.com/learning/security/what-is-web-application-security/)
  * [Performance Learning Center](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)
  * [Serverless Learning Center](https://www.cloudflare.com/learning/serverless/what-is-serverless/)
  * [SSL Learning Center](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
  * [Bots Learning Center](https://www.cloudflare.com/learning/bots/what-is-a-bot/)
  * [Cloud Learning Center](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)
  * [Access Management Learning Center](https://www.cloudflare.com/learning/access-management/what-is-identity-and-access-management/)
  * [Network Layer Learning Center](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)
  * [Privacy Learning Center](https://www.cloudflare.com/learning/privacy/what-is-data-privacy/)
  * [Video Streaming Learning Center](https://www.cloudflare.com/learning/video/what-is-streaming/)
  * [Email Security Learning Center](https://www.cloudflare.com/learning/email-security/what-is-email-security/)
  * [AI Learning Center](https://www.cloudflare.com/learning/ai/what-is-artificial-intelligence/)


[](https://www.facebook.com/cloudflare "Facebook")[](https://x.com/cloudflare "X")[](https://www.linkedin.com/company/cloudflare "LinkedIn")[](https://www.youtube.com/cloudflare "Youtube")[](https://instagram.com/cloudflare "Instagram")
© 2026 Cloudflare, Inc.[Privacy Policy](https://www.cloudflare.com/privacypolicy/)[Terms of Use](https://www.cloudflare.com/website-terms/)[Report Security Issues](https://www.cloudflare.com/disclosure/)![privacy options](https://www.cloudflare.com/img/privacyoptions.svg)Cookie Preferences[Trademark](https://www.cloudflare.com/trademark/)
![](https://benchmarks.cdn.compute-pipe.com/r20-100KB.png?r=77408335)![](https://benchmarks.cdn-c.compute-pipe.com/r20-100KB.png?r=65872007)![](https://benchmark.1e100cdn.net/r20-100KB.png?r=13263539)![](https://cedexis-test.akamaized.net/img/r20-100KB.png?r=70546653)![](https://benchmarks.cdn-b.compute-pipe.com/r20-100KB.png?r=53614770)![](https://1a4s4dv-m.ns1pcdn.net/a/t128.jpg?r=28035218)![](https://9y49n2-m.ns1pcdn.net/a/t128.jpg?r=94709824)![](https://kgnvry-ns1p.b-cdn.net/a/t128.jpg?r=12734534)![](https://ns1p-aws-backed.global.ssl.fastly.net/a/t128.jpg?r=61197452)![](https://1xtsor1-m.ns1pcdn.net/a/t128.jpg?r=67811148)![](https://1lmnv6z-m.ns1pcdn.net/a/t128.jpg?r=91312822)![](https://1xtvhvx-m.ns1pcdn.net/a/t128.jpg?r=64890231)![](https://5bav82-m.ns1pcdn.net/a/t128.jpg?r=43578197)![](https://fastly.jsdelivr.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=84650572)![](https://testingcf.jsdelivr.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=46403099)![](https://jsdelivr.b-cdn.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=24631219)
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=93dd371a-62b2-4b51-aa25-9291836d364b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&restricted_data_use=restrict_optimization&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=175&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=nvldc&type=javascript&version=2.4.11)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=93dd371a-62b2-4b51-aa25-9291836d364b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&restricted_data_use=restrict_optimization&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=175&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=nvldc&type=javascript&version=2.4.11)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=52b58f33-6645-46a5-88c5-5a24050bfe53&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&restricted_data_use=restrict_optimization&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=37&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=pomsv&type=javascript&version=2.4.11)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=52b58f33-6645-46a5-88c5-5a24050bfe53&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&restricted_data_use=restrict_optimization&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=37&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=pomsv&type=javascript&version=2.4.11)![](https://t.co/i/adsct?bci=4&cv=100%261&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=2&event_id=f4f88d4c-f05a-4056-a077-f11e348fa94c&events=%5B%5B%22auto_long_site_dwell%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=10003&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=pomsv&type=javascript&version=2.4.11)![](https://analytics.twitter.com/i/adsct?bci=4&cv=100%261&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=2&event_id=f4f88d4c-f05a-4056-a077-f11e348fa94c&events=%5B%5B%22auto_long_site_dwell%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=10003&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=pomsv&type=javascript&version=2.4.11)![](https://t.co/i/adsct?bci=4&cv=100%261&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=2&event_id=9376e357-b0a1-41cf-9743-6d3dd1f171c2&events=%5B%5B%22auto_long_site_dwell%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=10008&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=nvldc&type=javascript&version=2.4.11)![](https://analytics.twitter.com/i/adsct?bci=4&cv=100%261&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=2&event_id=9376e357-b0a1-41cf-9743-6d3dd1f171c2&events=%5B%5B%22auto_long_site_dwell%22%2C%7B%7D%5D%5D&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=bb2c6e4e-9192-4173-8b1b-682dce096639&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fen-gb%2Flearning%2Fcdn%2Fglossary%2Fanycast-network%2F&tw_engaged_ms=10008&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444308241-989774699&twpid=tw.1791444308241.753584116167573095&txn_id=nvldc&type=javascript&version=2.4.11)
