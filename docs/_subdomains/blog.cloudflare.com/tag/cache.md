---
url: https://blog.cloudflare.com/tag/cache/
title: Posts tagged \"Cache\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:25.463994+00:00
---

# Posts tagged "Cache" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/cache/

TAG

# Cache

[Subscribe to Cache RSS feed](https://blog.cloudflare.com/tag/cache/rss)

September 22, 2026## [We just shipped support for the ugliest part of HTTP: Vary](https://blog.cloudflare.com/vary-support/)

Vary support is now available in Cache Rules on every plan. You can normalize known negotiation headers, pass exact values through to the origin when those small differences matter, or bypass cache when the variation is too unpredictable.

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Zaidoon Abd Al Hadi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VAC8T0NPDPFZ06GAZW3H.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/) and [Zaidoon Abd Al Hadi](https://blog.cloudflare.com/author/zaidoon/)

September 1, 2026## [How we could save petabytes of cache storage with Zstandard and Pingora](https://blog.cloudflare.com/cache-transcoding/)

Could we get more cache space with the same hardware? We prototyped compression inside Cloudflare's cache to find out.

![Aashi Patel](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1DAS9K7XE8D5EDSDRZEZ3GK.01M1DASACDGC9T1MJWP4T8VT3A.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Aashi Patel](https://blog.cloudflare.com/author/aashi-patel/)

July 30, 2026## [Dogfooding at scale: migrating cdnjs to Cloudflare’s Developer Platform](https://blog.cloudflare.com/cdnjs-dev-platform-migration/)

We moved cdnjs, serving 9 billion requests a day, entirely onto Cloudflare's Developer Platform. That means we’re running one of the Internet's busiest open-source CDNs on our own building blocks, and we pushed Workflows and Workers limits higher for everyone.

![Simona Badoiu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49BY2VVWXQKZQA2SJ3N42J.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Simona Badoiu](https://blog.cloudflare.com/author/simona-badoiu/)

July 23, 2026## [Introducing Cache Response Rules](https://blog.cloudflare.com/introducing-cache-response-rules/)

Perhaps you’ve seen something that should sail out of cache get dragged back to the origin by a stray Set-Cookie or Cache-Control, headers that can be difficult to change on the origin itself. Cache Response Rules is the fix, applied at the right time.

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Anthony Turcios](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KY7YXQR9B85CTTBSQ2JN7BGD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/) and [Anthony Turcios](https://blog.cloudflare.com/author/anthony-turcios/)

July 10, 2026## [Improving Smart Tiered Cache for Public Cloud Regions](https://blog.cloudflare.com/smart-tiered-cache-for-public-clouds/)

Smart Tiered Cache allows for precise upper tier selection for origins hosted on AWS, GCP, Azure, and Oracle Cloud with customer-provided cloud region hints.

![Chenxi Zhang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KXJM6F0PHPE4PQMNC0W1H579.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Chenxi Zhang](https://blog.cloudflare.com/author/chenxi-zhang/)

July 6, 2026## [Your Worker can now have its own cache in front of it](https://blog.cloudflare.com/workers-cache/)

We are launching Workers Cache, a regionally tiered cache that sits directly in front of your Worker entrypoints. Infinitely composable, configured via standard HTTP headers

![Dan Lapid](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49J56Y8QNB56HN77FKK7EM.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Connor Harwood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PA3429BFXAR99YP0Z2ZX.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dan Lapid](https://blog.cloudflare.com/author/dan-lapid/) and [Connor Harwood](https://blog.cloudflare.com/author/connor-harwood/)

April 2, 2026## [Why we're rethinking cache for the AI era](https://blog.cloudflare.com/rethinking-cache-ai-humans/)

The explosion of AI-bot traffic, representing over 10 billion requests per week, has opened up new challenges and opportunities for cache design. We look at some of the ways AI bot traffic differs from humans, how this impacts CDN cache, and some early ideas for how Cloudflare is designing systems to improve the AI and human experience.

![Avani Wildani](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NPKGY3CPBB5DZ8GVR1B0.webp&w=64&h=64&f=webp&fit=cover&position=center)![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)

[Avani Wildani](https://blog.cloudflare.com/author/avani-wildani/) and [Suleman Ahmad](https://blog.cloudflare.com/author/suleman/)

September 29, 2025## [15 years of helping build a better Internet: a look back at Birthday Week 2025](https://blog.cloudflare.com/birthday-week-2025-wrap-up/)

Rust-powered core systems, post-quantum upgrades, developer access for students, PlanetScale integration, open-source partnerships, and our biggest internship program ever — 1,111 interns in 2026.

![Nikita Cano](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AJSY9DYK5N26JP1Q24B7.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Korinne Alpers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JYW3RAS2PS81KW2DNQWC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nikita Cano](https://blog.cloudflare.com/author/nikita/) and [Korinne Alpers](https://blog.cloudflare.com/author/korinne-alpers/)

July 17, 2025## [Quicksilver v2: evolution of a globally distributed key-value store (Part 2)](https://blog.cloudflare.com/quicksilver-v2-evolution-of-a-globally-distributed-key-value-store-part-2-of-2/)

This is part two of a story about how we overcame the challenges of making a complex system more scalable.

![Marten van de Sanden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464B70R8CFS8A6919SP2YY.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Anton Dort-Golts](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KTYJ5PFB99PQJMDY0BW5.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Marten van de Sanden](https://blog.cloudflare.com/author/marten-van-de-sanden/) and [Anton Dort-Golts](https://blog.cloudflare.com/author/anton-dort-golts/)

July 10, 2025## [Quicksilver v2: evolution of a globally distributed key-value store (Part 1)](https://blog.cloudflare.com/quicksilver-v2-evolution-of-a-globally-distributed-key-value-store-part-1/)

This blog post is the first of a series, in which we share our journey in redesigning Quicksilver — Cloudflare’s distributed key-value store that serves over 3 billion keys per second globally. 

![Anton Dort-Golts](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KTYJ5PFB99PQJMDY0BW5.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marten van de Sanden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW464B70R8CFS8A6919SP2YY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Anton Dort-Golts](https://blog.cloudflare.com/author/anton-dort-golts/) and [Marten van de Sanden](https://blog.cloudflare.com/author/marten-van-de-sanden/)

April 1, 2025## [“You get Instant Purge, and you get Instant Purge!” — all purge methods now available to all customers](https://blog.cloudflare.com/instant-purge-for-all/)

Following up on having the fastest purge in the industry, we have now increased Instant Purge quotas across all Cloudflare plans. 

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Connor Harwood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PA3429BFXAR99YP0Z2ZX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Zaidoon Abd Al Hadi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VAC8T0NPDPFZ06GAZW3H.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/), [Connor Harwood](https://blog.cloudflare.com/author/connor-harwood/), and [Zaidoon Abd Al Hadi](https://blog.cloudflare.com/author/zaidoon/)

December 26, 2024## [Sometimes I cache: implementing lock-free probabilistic caching](https://blog.cloudflare.com/sometimes-i-cache/)

If you want to know what cache revalidation is, how it works, and why it can involve rolling a die, read on. This blog post presents a lock-free probabilistic approach to cache revalidation, along 

![Thibault Meunier](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CG4C7M8Y2P7VRAYHW2RV.png&w=64&h=64&f=webp&fit=cover&position=center)

[Thibault Meunier](https://blog.cloudflare.com/author/thibault/)

September 30, 2024## [Wrapping up another Birthday Week celebration](https://blog.cloudflare.com/birthday-week-2024-wrap-up/)

Recapping all the big announcements made during 2024’s Birthday Week.

![Kelly May Johnston](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46WM5TMV3Y8S91FG1PQJ01.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Brendan Irvine-Broque](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H9641F9RZN2BA8BPX7HK.JPG&w=64&h=64&f=webp&fit=cover&position=center)

[Kelly May Johnston](https://blog.cloudflare.com/author/kelly-may-johnston/) and [Brendan Irvine-Broque](https://blog.cloudflare.com/author/brendan-irvine-broque/)

September 25, 2024## [Introducing Speed Brain: helping web pages load 45% faster](https://blog.cloudflare.com/introducing-speed-brain/)

Speed Brain uses the Speculation Rules API to prefetch content for the user's likely next navigations. The goal is to download a web page to the browser before a user navigates to it. 

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![William Woodhead](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47K5WQG2GRE7VVT4GEYZ7G.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/), [Suleman Ahmad](https://blog.cloudflare.com/author/suleman/), and [William Woodhead](https://blog.cloudflare.com/author/william/)

September 24, 2024## [Instant Purge: invalidating cached content in under 150ms](https://blog.cloudflare.com/instant-purge/)

We’ve built the fastest cache purge in the industry by offering a global purge latency for purge by tags, hostnames, and prefixes of less than 150ms on average (P50), representing a 90% improvement. 

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Tim Kornhammar](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46H0DZHMY1AQ9DEM3HVEJ7.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Connor Harwood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PA3429BFXAR99YP0Z2ZX.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/), [Tim Kornhammar](https://blog.cloudflare.com/author/tim-kornhammar/), and [Connor Harwood](https://blog.cloudflare.com/author/connor-harwood/)

October 24, 2023## [Cache Rules are now GA: precision control over every part of your cache](https://blog.cloudflare.com/cache-rules-go-ga/)

Today, we're thrilled to share that Cache Rules, along with several other Rules products, are generally available (GA). But that’s not all — we're also introducing new configuration options for Cache Rules

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/)

September 28, 2023## [Cloudflare Integrations Marketplace introduces three new partners: Sentry, Momento and Turso](https://blog.cloudflare.com/cloudflare-integrations-marketplace-new-partners-sentry-momento-turso/)

We introduced integrations with Supabase, PlanetScale, Neon and Upstash. Today, we are thrilled to introduce our newest additions to Cloudflare’s Integrations Marketplace – Sentry, Turso and Momento

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/author/tanushree/)

June 1, 2023## [Reduce latency and increase cache hits with Regional Tiered Cache](https://blog.cloudflare.com/introducing-regional-tiered-cache/)

Regional Tiered Cache provides an additional layer of caching for Enterprise customers who have a global traffic footprint and want to serve content faster by avoiding network latency when there is a cache miss in a lower-tier, resulting in an upper-tier fetch in a data center located far away

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/author/alex/) and [Andrew Hauck](https://blog.cloudflare.com/author/andrew-hauck/)

Load more
