---
url: https://blog.cloudflare.com/tag/bugs/
title: Posts tagged \"Bugs\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:25.084161+00:00
---

# Posts tagged "Bugs" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/bugs/

TAG

# Bugs

[Subscribe to Bugs RSS feed](https://blog.cloudflare.com/tag/bugs/rss)

January 14, 2026## [What came first: the CNAME or the A record?](https://blog.cloudflare.com/cname-a-record-order-dns-standards/)

A recent change to 1.1.1.1 accidentally altered the order of CNAME records in DNS responses, breaking resolution for some clients. This post explores the technical root cause, examines the source code of affected resolvers, and dives into the inherent ambiguities of the DNS RFCs.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

January 27, 2025## [Over 700 million events/second: How we make sense of too much data](https://blog.cloudflare.com/how-we-make-sense-of-too-much-data/)

Here we explain how we made our data pipeline scale to 700 million events per second while becoming more resilient than ever before. We share some math behind the approach and some of the designs.

![Constantin Pan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4569HHEF9XM981Y3Q8T9FF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jim Hawkridge](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455228FF3J2XW973RTKHR2.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Constantin Pan](https://blog.cloudflare.com/author/constantin-pan/) and [Jim Hawkridge](https://blog.cloudflare.com/author/jim-hawkridge/)

April 3, 2023## [mTLS client certificate revocation vulnerability with TLS Session Resumption](https://blog.cloudflare.com/mtls-client-certificate-revocation-vulnerability-with-tls-session-resumption/)

This blog post outlines the root cause analysis and solution for a bug found in Cloudflare’s mTLS implementation

![Rushil Mehra](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3J65XQ6KWWMTYQHZMX9VC2Q.01M3J65YDX7BCSBDQXBR3P2B20.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Rushil Mehra](https://blog.cloudflare.com/author/rushil-mehra/)

January 18, 2018## [However improbable: The story of a processor bug](https://blog.cloudflare.com/however-improbable-the-story-of-a-processor-bug/)

Processor problems have been in the news lately, due to the Meltdown and Spectre vulnerabilities. But generally, engineers writing software assume that computer hardware operates in a reliable, well-understood fashion, and that any problems lie on the software side of the software-hardware divide.

![David Wragg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XD7ZQXDH99ANVA1Z9814.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[David Wragg](https://blog.cloudflare.com/author/david-wragg/)

January 8, 2018## [An Explanation of the Meltdown/Spectre Bugs for a Non-Technical Audience](https://blog.cloudflare.com/meltdown-spectre-non-technical/)

Last week the news of two significant computer bugs was announced. They've been dubbed Meltdown and Spectre and they take advantage of very technical systems that modern CPUs have implemented to make computers extremely fast. 

![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[John Graham-Cumming](https://blog.cloudflare.com/author/john-graham-cumming/)

March 1, 2017## [Quantifying the Impact of "Cloudbleed"](https://blog.cloudflare.com/quantifying-the-impact-of-cloudbleed/)

Last Thursday we released details on a bug in Cloudflare's parser impacting our customers. It was an extremely serious bug that caused data flowing through Cloudflare's network to be leaked onto the Internet.

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/author/matthew-prince/)

February 23, 2017## [Incident report on memory leak caused by Cloudflare parser bug](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/)

Last Friday, Tavis Ormandy from Google’s Project Zero contacted Cloudflare to report a security problem with our edge servers. He was seeing corrupted web pages being returned by some HTTP requests run through Cloudflare.

![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[John Graham-Cumming](https://blog.cloudflare.com/author/john-graham-cumming/)

January 1, 2017## [How and why the leap second affected Cloudflare DNS](https://blog.cloudflare.com/how-and-why-the-leap-second-affected-cloudflare-dns/)

At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRDNS to panic. 

![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[John Graham-Cumming](https://blog.cloudflare.com/author/john-graham-cumming/)

July 18, 2016## [CloudFlare sites protected from httpoxy](https://blog.cloudflare.com/cloudflare-sites-protected-from-httpoxy/)

We have rolled out automatic protection for all customers for the the newly announced vulnerability called httpoxy.

![Ben Cartwright-Cox](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JRW455ZSS2HPKWZYCHWF.png&w=64&h=64&f=webp&fit=cover&position=center)

[Ben Cartwright-Cox](https://blog.cloudflare.com/author/ben-cartwright-cox/)

October 29, 2015## [Creative foot-shooting with Go RWMutex](https://blog.cloudflare.com/creative-foot-shooting-with-go-rwmutex/)

Hi, I'm Filippo and today I managed to surprise myself! (And not in a good way.) I'm developing a new module ("filter" as we call them) for RRDNS, CloudFlare's Go DNS server. 

![Filippo Valsorda](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GAVR9Z506KS1WDKSMTBM.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Filippo Valsorda](https://blog.cloudflare.com/author/filippo/)

September 8, 2015## [Weird bug of the day: Twitter in-app browser can't visit site](https://blog.cloudflare.com/weird-bug-of-the-day-twitter-in-app-browser-cant-visit-site/)

We keep a close eye on tweets that mention CloudFlare because sometimes we get early warning about odd errors that we are not seeing ourselves through our monitoring systems. Towards the end of August we saw a small number of tweets like this one:

![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[John Graham-Cumming](https://blog.cloudflare.com/author/john-graham-cumming/)

March 19, 2015## [OpenSSL Security Advisory of 19 March 2015](https://blog.cloudflare.com/openssl-security-advisory-of-19-march-2015/)

Today there were multiple vulnerabilities released in OpenSSL, a cryptographic library used by CloudFlare (and most sites on the Internet).

![Ryan Lackey](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48VDKVD3X51CYH8NVERR3Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ryan Lackey](https://blog.cloudflare.com/author/rdl/)

September 30, 2014## [Inside Shellshock: How hackers are using it to exploit systems](https://blog.cloudflare.com/inside-shellshock/)

On Wednesday of last week, details of the Shellshock bash bug emerged. This bug started a scramble to patch computers, servers, routers, firewalls, and other computing appliances using vulnerable versions of bash.

![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[John Graham-Cumming](https://blog.cloudflare.com/author/john-graham-cumming/)

April 11, 2014## [Answering the Critical Question: Can You Get Private SSL Keys Using Heartbleed?](https://blog.cloudflare.com/answering-the-critical-question-can-you-get-private-ssl-keys-using-heartbleed/)

Below is what we thought as of 12:27pm UTC. To verify our belief we crowd sourced the investigation. It turns out we were wrong. While it takes effort, it is possible to extract private SSL keys.

![Nick Sullivan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NXK9203HP874YB09STY7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nick Sullivan](https://blog.cloudflare.com/author/nick-sullivan/)

April 7, 2014## [Staying ahead of OpenSSL vulnerabilities](https://blog.cloudflare.com/staying-ahead-of-openssl-vulnerabilities/)

Today a new vulnerability was announced in OpenSSL 1.0.1 that allows an attacker to reveal up to 64kB of memory to a connected client or server (CVE-2014-0160). We fixed this vulnerability last week before it was made public. 

![Nick Sullivan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44NXK9203HP874YB09STY7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nick Sullivan](https://blog.cloudflare.com/author/nick-sullivan/)

November 18, 2011## [Cloudflare Tips: Troubleshooting Common Problems](https://blog.cloudflare.com/cloudflare-tips-troubleshooting-common-problems/)

Debugging technical issues online can be tricky. There are many moving pieces; it can be an isolated network connection with the ISP, an issue with your server or one of CloudFlare's data centers could be temporarily having a problem.

![Damon Billian](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XAY34J72NG2YRX9237JB.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Damon Billian](https://blog.cloudflare.com/author/damon-billian/)
