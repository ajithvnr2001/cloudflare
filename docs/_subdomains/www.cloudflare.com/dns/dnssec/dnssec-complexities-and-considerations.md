---
url: https://www.cloudflare.com/dns/dnssec/dnssec-complexities-and-considerations/
title: DNSSEC Complexities and Considerations | Cloudflare
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (145 chars), fallback to crawl4ai)
fetched_at: 2026-10-08T07:22:17.067528+00:00
---

# DNSSEC Complexities and Considerations | Cloudflare

> Source: https://www.cloudflare.com/dns/dnssec/dnssec-complexities-and-considerations/

Preview Mode
[Documentation](https://staging.mrk.cfdata.org/mrk/redwood-blade-repository/)
# DNSSEC Complexities and Considerations
![dnssec logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3Zh69Q2hj2uY6WqgWcwkcS/e27ff686df7a092cfc2f41f072ca88cc/dnssec_logo.png)
DNSSEC is an extension to DNS: it provides a system of trust for DNS records. It’s a major change to one of the core components of the Internet. In this article, we examine some of the complications of DNSSEC, and what Cloudflare has done to reduce any negative impact they might have. The main issues are zone content exposure, key management, and the impact on DNS reflection/amplification attacks.
![dnssec logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3Zh69Q2hj2uY6WqgWcwkcS/e27ff686df7a092cfc2f41f072ca88cc/dnssec_logo.png)
## Zone Content Exposure
DNS is split into smaller pieces called zones. A zone typically starts at a [domain name](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/), and contains all records pertaining to the subdomains. Each zone is managed by a single manager. For example, cloudflare.com is a zone containing all DNS records for cloudflare.com and its subdomains (e.g. [www.cloudflare.com](http://www.cloudflare.com), api.cloudflare.com).
There is no directory service for subdomains in DNS so if you want to know if api.cloudflare.com exists, you have to ask a DNS server and that DNS server will end up asking cloudflare.com whether api.cloudflare.com exists. This is not true with DNSSEC. In some cases, enabling DNSSEC may expose otherwise obscured zone content. Not everyone cares about the secrecy of subdomains, and zone content may already be easily guessable because most sites have a ‘www’ subdomain; however, subdomains are sometimes used as login portals or other services that the site owner wants to keep private. A site owner may not want to reveal that “secretbackdoor.example.com” exists in order to protect that site from attackers.
![x ray specs](https://www.cloudflare.com/img/products/dns/dnssec/x-ray_specs.jpg)
The reason DNSSEC can expose subdomains has to do with how zones are signed. Historically, DNSSEC is used to sign static zones. A static zone is a complete set of records for a given domain. The DNSSEC signature records are created using the Key Signing Key (KSK) and Zone Signing Key (ZSK) in a central location and sent to the authoritative server to be published. This set of records allows an authoritative server to answer any question it is asked, including questions about subdomains that don’t exist.
Unlike standard DNS, where the server returns an unsigned NXDOMAIN (Non-Existent Domain) response when a subdomain does not exist, DNSSEC guarantees that every answer is signed. This is done with a special record that serves as a proof of non-existence called the NextSECure (NSEC) record. An NSEC record can be used to say: “there are no subdomains between subdomains X and subdomain Y.” By filling the gap between every domain in the zone, NSEC provides a way to answer any query with a static record. The NSEC record also lists what Resource Record types exist at each name.
For statically signed zones, there are, by definition, a fixed number of records. Since each NSEC record points to the next, this results in a finite ‘ring’ of NSEC records that covers all the subdomains. Anyone can ‘walk’ a zone by following one NSEC record to the next until they know all subdomains. This method can be used to reveal all of the names in that zone---possibly exposing internal information.
Suppose there is a DNSSEC-enabled zone called example.com, with subdomains public.example.com and secret.example.com. Adding NSEC records will reveal the existence of all subdomains.
Asking for the NSEC record of example.com gives the following:

```

```
example.com. NSEC public.example.com. A NS SOA TXT AAAA RRSIG NSEC DNSKEY

```

```

Asking for public.example.com gives the following NSEC record:

```

```
public.example.com. NSEC secret.example.com. A TXT AAAA RRSIG NSEC

```

```

Asking for secret.example.com gives the following NSEC record:

```

```
secret.example.com. NSEC example.com. A TXT AAAA RRSIG NSEC

```

```

The first one is for the zone top/apex, and says that the name “example.com” exists and the next name is “public.example.com”. The public.example.com record says that the next name is “secret.example.com” revealing the existence of a private subdomain. The “secret.example.com” says the next record is “example.com” completing the chain of subdomains. Therefore, with a few queries anybody can know the complete set of records in the zone.
Technically, DNS records are not supposed to be secret, but in practice they are sometimes considered so. Subdomains have been used to keep things (such as a corporate login page) private for a while, and suddenly revealing the contents of the zone file may be unexpected and unappreciated.
Before DNSSEC the only way to discover the contents of names in a zone was to either query for them, or attempt to perform a transfer of the zone from one of the authoritative servers. Zone Transfers (AXFR) are frequently blocked. NSEC’s alternatative, NSEC3, was introduced to fight zone enumeration concerns, but even NSEC3 can be used to reveal the existence of subdomains.
![dnssec nsec stat](https://www.cloudflare.com/img/products/dns/dnssec/dnssec_nsec_stat.png)
_[Most domains under .ch use NSEC3](http://securityblog.switch.ch/2013/02/19/dnssec-deployment-in-ch/)_
The NSEC3 record is like an NSEC record, but, rather than a signed gap of domain names for which there are no answers to the question, NSEC3 provides a signed gap of hashes of domain names. This was intended to prevent zone enumeration. Thus, the NSEC3 chain for a zone containing “example.com” and “[www.example.com”](http://www.example.com%E2%80%9D) could be (each NSEC3 record is on 3 lines for clarity):

```

```
231SPNAMH63428R68U7BV359PFPJI2FC.example.com. NSEC3 1 0 3 ABCDEF
NKDO8UKT2STOL6EJRD1EKVD1BQ2688DM
A NS SOA TXT AAAA RRSIG DNSKEY NSEC3PARAM

```

```

```

```
NKDO8UKT2STOL6EJRD1EKVD1BQ2688DM.example.com. NSEC3 1 0 3 ABCDEF
231SPNAMH63428R68U7BV359PFPJI2FC
A TXT AAAA RRSIG

```

```

Where 

```
231SPNAMH63428R68U7BV359PFPJI2FC
```
is the salted hash of 
```
example.com
```
and 
```
NKDO8UKT2STOL6EJRD1EKVD1BQ2688DM
```
is the salted hash of 
```
www.example.com
```
. This is reminiscent of the way [password databases work](https://blog.cloudflare.com/keeping-passwords-safe-by-staying-up-to-date/). 
The first line of the NSEC3 record contains the “name” of the zone after it has been hashed, the number of hash rounds and salt used in the hashing are the two last parameters on the first line “3 ABCDEF”. The “1 0” stands for digest algorithm (1 means SHA-1) and if the zone uses Opt-out (0 means no). The second line is the “next hashed name in the zone”, the third line lists the types at the name. You can see the “next name” at the first NSEC3 record matches the name on the second NSEC3 record and the “next name” on that one completes the chain.
For NSEC enumeration, you can create the full list of domains by starting to guess at possible names in the domain. If the zone has around 100 domain names, it will take around 100 requests to enumerate the entire zone. With NSEC3, when you request a record that does not exist, a signed NSEC3 record is returned with the next zone present ordered alphabetically by hash. Checking if the next query name candidate fits in one of the known gaps allows anyone to discover the full chain in around 100 queries. There are many tools that can do this computation for you, including [a plug-in to nmap](http://nmap.org/nsedoc/scripts/dns-nsec3-enum.html)
With the hashes that correspond to all the valid names in the zone, a dictionary attack can be used to figure out the real names. Short names are easily guessed, and by using a dictionary, longer names can be revealed as existing without having to flood the authoritative nameservers with guesses. Tools like [HashCat](http://hashcat.net/oclhashcat/) make this easy to do in software, and the popularity of bitcoin has dramatically lowered the price of hashing-specific hardware. There is a burgeoning cottage industry of devices built to compute cryptographic hashes. The Tesla Password cracker (below) is just one example of these off-the shelf devices.
![tesla cracker](https://www.cloudflare.com/img/products/dns/dnssec/tesla-cracker.jpg)
_The Teslsa Cracker_
Because hashing is cheap, zone privacy is only slightly improved when using NSEC3 as designed; the amount of protection a name gets is proportional to its unguessability.
In short, NSEC is like revealing plaintext passwords, and NSEC3 is like revealing a Unix-style passwords file. Neither technique is very secure. With NSEC3 a subdomain is only as private as it is hard to guess.
This vulnerability can be mitigated by a techniques introduced in RFCs 4470 and 4471 (<https://tools.ietf.org/html/rfc4470> and <https://tools.ietf.org/html/rfc4471>) called “DNSSEC white lies”; this was implemented by Dan Kaminsky for demonstration purposes. When a request comes in for a domain that is not present, instead of providing an NSEC3 record of the next real domain, an NSEC3 record of the next hash alphabetically is presented. This does not break the NSEC3 guarantee that there are no domains whose hash fits lexicographically between the NSEC3 response and the question.
You can only implement NSEC3 or NSEC “white lies” if signatures can be computed in real-time in response to questions. Traditionally, static zone records for DNS resolution are created offline, and all the records with signatures stored in a zone file. This file is then read by a live DNS server allowing it to answer questions about the zone.
Cloudflare’s DNSSEC implementation leverages [ECDSA’s efficient signature generation](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/) to sign DNSSEC records on-the-fly.
## Key Management
DNSSEC was designed to operate in various modes, each providing different security, performance and convenience tradeoffs. Live signing solves the zone content exposure problem in exchange for less secure key management. 
The most common DNSSEC mode is offline signing of static zones. This allows the signing system to be highly protected from external threats by keeping the private keys on a machine that is not connected to the network. This operating model works well when the DNS information does not change often. 
Another common operating mode is centralized online signing. If you sign data in restricted access, dedicated DNS signing systems, it allows DNS data to change and get published quickly. Some operators run DNS signing on their main DNS servers. Just like offline signing of static zones, this mode follows the central signing model, i.e., a single (or replicated) central signer does all the signing and data gets propagated from it to the actual authoritative DNS servers. 
A more radical mode is to allow the actual authoritative DNS servers to sign data on the fly when needed, this allows a number of new features including geographically dependant information signed where the answer is generated. The downside is that now the keying material is on many different machines that have direct access to the Internet. Doing live signing at the edge introduces new problems such as key distribution and places extra computing requirements on the nodes. 
Recently, a bug known as [Heartbleed](https://blog.cloudflare.com/answering-the-critical-question-can-you-get-private-ssl-keys-using-heartbleed/) was found that opened a major security hole in server applications. It was caused by a coding error in OpenSSL that created a remote memory disclosure vulnerability. This bug allowed remote attackers to extract cryptographic keys from Internet-facing servers. Remote memory exposure bug are just one of the many threats to private key security when the key is being used in an active process such as DNSSEC live signing. The more a machine is exposed to the Internet, the more vectors of attack there are. Offline signing machines have a much smaller window of exposure to such threats. 
One way to keep keys secure is to use a hardware-backed solution such as a Hardware Security Module (HSM). The major drawback for this is cost – HSMs are very expensive (and slow). This is one of the stickiest points for running DNS servers that are spread out geographically in order to be close to their customers. Running an HSM in every server location can not only be expensive, but there can also be [legal complications](http://www.kslaw.com/imageserver/KSPublic/library/publication/2011articles/11-11WorldECRCloutierCohen.pdf) too. 
Another solution to protect keys from remote disclosure is to offload cryptographic operations into trusted component of the system. This is where having a [custom DNS server](https://blog.cloudflare.com/cloudflare-fastest-free-dns-among-fastest-dns/) that can offload cryptography can come in handy. 
Key management for DNSSEC is similar to key management for TLS and has similar challenges. Earlier this year, we introduced [Keyless SSL](https://blog.cloudflare.com/keyless-ssl-the-nitty-gritty-technical-details/) to help improve key security for TLS. We are looking at extending Keyless SSL to provide the advantages of remote key servers for DNSSEC live-signing. 
## Reflection/Amplification Threat
Operators running an authoritative DNS server are often nervous their server will be used as a conduit for malicious distributed denial of service (DDoS) attacks. This stems from the fact that DNS uses UDP, a stateless protocol.
In TCP, each connection begins with a three-way handshake. This ensures that the IP address of both parties is known and correct before starting a connection. In UDP, there is no such handshake: messages are just sent directly to an IP with an unverified ‘from’ IP address. If an attacker can craft a UDP packet that says ‘hi, from IP X’ to a server, the server will typically respond by sending a UDP packet to X. Choosing X as a victim’s IP address instead of the sender’s is called UDP ‘spoofing’. By spoofing a victim, an attacker can cause a server that responds to UDP requests to flood the victim with ‘reflected’ traffic. This applies as much to authoritative servers as to open recursive resolvers.
DNSSEC also works over UDP, and the answers to DNS queries can be very long, containing multiple DNSKEY and RRSIG records. This is an attractive target for attackers since it allows them to ‘amplify’ their reflection attacks. If a small volume of spoofed UDP DNSSEC requests is sent to nameservers, the victim will receive a large volume of reflected traffic. Sometimes this is enough to overwhelm the victim’s server, and cause a denial of service.
Asking for a TLD that does not exist from a root server returns an answer that is around 100 bytes, the signed answer for the same question is about 650 bytes or an amplification factor of 6.5. The root is signed using a 1,024 bit RSA key and uses NSEC for negative answers. Asking for a domain that does not exist in a TLD using NSEC3 signed with 1,024 bit key will yield an amplification factor of around 10. There are other queries that can yield even higher amplification factors, the most effective being the “ANY” query.
Like many services, DNS can also work over TCP. There is a ‘truncation’ flag that can be sent back to a resolver to indicate that TCP is required. This would fix the issue of DNS reflection at the cost of slower DNS requests. This solution is not practical at the moment since 16% of resolvers don’t respect the TCP truncation flag, and [4% don’t try a second server](http://www.circleid.com/posts/20130820_a_question_of_dns_protocols/).
Another option to reduce the size of responses is to use [Elliptic Curve Digital Signature Algorithm (ECDSA)](https://www.cloudflare.com/dns/dnssec/ecdsa-and-dnssec/) keys instead of traditional RSA keys. ECDSA keys are much smaller than RSA keys of equivalent strength, and they produce smaller signatures making DNSSEC responses much smaller, reducing the amplification factor. Google Public DNS added support for ECDSA in late 2014, and several others have followed suit since then.
Support for TCP and ECDSA is still lagging behind general DNSSEC support, so traditional anti-abuse methods can be used instead. This includes [Resource Rate Limiting (RRL)](https://kb.isc.org/article/AA-01000/0/A-Quick-Introduction-to-Response-Rate-Limiting.html) and other heuristics.
To protect against reflection attacks, Cloudflare is working on a multi-pronged approach. First, by using attack identification heuristics and anti-abuse techniques that we are currently using in our DNS server, and second by reducing the amplification factor of DNSSEC responses. Ways to reduces the maximum amplification factor includes only replying to “ANY” requests over TCP, using smaller ECDSA keys when possible, and reducing the frequency of key rollovers.
## Conclusions
Cloudflare is aware of the complexity introduced by DNSSEC with respect to zone privacy, key management, and reflection/amplification risk. With smart engineering decisions, and operational controls in place, the dangers of DNSSEC can be prevented.
##  Setting Up Cloudflare Is Easy 
  
  

Set up a domain in less than 5 minutes. Keep your hosting provider. No code changes required. 
* * *
### Cloudflare Pricing
Everyone’s Internet application can benefit from using Cloudflare. Pick a plan that fits your needs.
* * *
### Free
For personal websites, blogs, and anyone who wants to explore Cloudflare.
* * *
### $0/month
Add-ons billed monthly
[ADD A WEBSITE](https://dash.cloudflare.com/sign-up)
* * *
[Learn More](https://www.cloudflare.com/plans/#overview)
* * *
### Pro
For professional websites, blogs, and portfolios requiring basic security and performance.
* * *
### $20/month
Billed $240 annually or $25/mo billed monthly
[GET PRO](https://dash.cloudflare.com/sign-up?pt=p)
* * *
[Learn More](https://www.cloudflare.com/plans/pro/)
* * *
### Business
For small eCommerce websites and businesses requiring advanced security and performance, PCI compliance, and prioritized email support.
* * *
### $200/month
Billed $2400 annually or $250/mo billed monthly
[GET BUSINESS](https://dash.cloudflare.com/sign-up?pt=b)
* * *
[Learn More](https://www.cloudflare.com/plans/business/)
* * *
### Enterprise
For companies requiring enterprise-grade security and performance, prioritized 24/7/365 phone, email, or chat support, and guaranteed uptime.
* * *
### Contact Us
Billed annually
[GET IN TOUCH](https://www.cloudflare.com/plans/enterprise/contact/)
* * *
[Learn More](https://www.cloudflare.com/plans/enterprise/)
* * *
### Trusted by millions of Internet properties
[View case studies](https://www.cloudflare.com/case-studies/)
![Mars logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/1Xar1H4WcFHHkHRDzMypMh/1f8989ae11cb464cc640c7121d0be9a6/logo_mars_trusted-by_gray.svg)
![L'Oréal logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/4xn47h0gWiUSwJ0PU3Ysvk/683779108bfd6eeb62fbac5135780fe6/logo_loreal_trusted-by_gray.svg)
![Logo doordash trusted by gray](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3fy2mc73AF9xqD18C5760R/f46ab68d38c9adb30a639f69589d8af0/doordash_134.png)
![Logo garmin trusted by gray](https://cf-assets.www.cloudflare.com/slt3lc6tev37/6VUhUMEcvn3L3j88LttHzC/b2cf2b702aad874db9cb61b0028e9c40/logo_garmin_trusted-by_gray.svg)
![IBM logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/OMwO1Fr8BxHVum0iBbatc/979c1807f5810edc903d4b07c18e0cb0/logo_ibm_trusted-by_gray.svg)
![Logo 23andme trusted by gray](https://cf-assets.www.cloudflare.com/slt3lc6tev37/2TfcZ86qvZor2xtI2z4Vvr/ef54112582296119f4296869c34ba025/logo_23andme_color_32px-wrapper.svg)
![Shopify logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/6XVeELky7fceWRpfBvN8qr/4e13aa3d8dd73e1f091f3de966fdc9cb/logo_shopify_trusted-by_gray.svg)
![Logo lending tree trusted by gray](https://cf-assets.www.cloudflare.com/slt3lc6tev37/7lhZTNuuLxtB38r8n1VORb/9fbfad924669a02deb97668b9c8d163b/logo_lending-tree_color_32px-wrapper.svg)
![LabCorp logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/1AsuJijKk8EMH5s1ae56nx/b13406881aa864b7e17b2233a0d090ef/logo_labcorp_trusted-by_gray.svg)
![NCR logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/26kszL2y2X7zTR2edZPDUY/1a9d00bc8c441346e6dd06bd82204972/logo_ncr_gray_32px-wrapper.svg)
![Thomson Reuters logo](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3JniCZlkcKI9iHgormG8j3/b94cf97c93844f2db74d566fc512aef1/logo_thomson-reuters_gray_32px-wrapper.svg)
![Logo zendesk trusted by gray](https://cf-assets.www.cloudflare.com/slt3lc6tev37/5YRPa33UFrfL2zoZd2AXTq/658995f16c7ee4818875c254c18573d3/logo_zendesk_gray_32px-wrapper.svg)
GETTING STARTED
  * [Free plans](https://www.cloudflare.com/plans/free/)
  * [Small business plans](https://www.cloudflare.com/small-business/)
  * [For enterprises](https://www.cloudflare.com/enterprise/)
  * [Get a recommendation](https://www.cloudflare.com/about-your-website/)
  * [Request a demo](https://www.cloudflare.com/plans/enterprise/demo/)
  * [Contact sales](https://www.cloudflare.com/plans/enterprise/contact/)


SOLUTIONS
  * [Connectivity cloud](https://www.cloudflare.com/connectivity-cloud/)
  * [Application services](https://www.cloudflare.com/application-services/)
  * [SASE and workspace security](https://www.cloudflare.com/sase/)
  * [Network services](https://www.cloudflare.com/network-services/)
  * [Developer platform](https://www.cloudflare.com/developer-platform/)


SUPPORT
  * [Help center](https://support.cloudflare.com)
  * [Customer support](https://dash.cloudflare.com/?to=/:account/support)
  * [Community forum](https://community.cloudflare.com)
  * [Developers Discord ](https://discord.com/invite/cloudflaredev)
  * [Lost account access?](https://developers.cloudflare.com/support/account-management-billing/common-account-questions/login-and-account-issues/)
  * [Cloudflare status](https://www.cloudflarestatus.com/)


COMPLIANCE
  * [Compliance resources](https://www.cloudflare.com/trust-hub/compliance-resources/)
  * [Trust](https://www.cloudflare.com/trust-hub/)
  * [GDPR](https://www.cloudflare.com/trust-hub/gdpr/)
  * [Responsible AI](https://www.cloudflare.com/trust-hub/responsible-ai/)
  * [Transparency report](https://www.cloudflare.com/transparency/)
  * [Report abuse](https://www.cloudflare.com/trust-hub/abuse-approach/)


PUBLIC INTEREST
  * [Project Galileo](https://www.cloudflare.com/galileo/)
  * [Athenian Project](https://www.cloudflare.com/athenian/)
  * [Cloudflare for Campaigns](https://www.cloudflare.com/campaigns/)
  * [Project Fairshot](https://www.cloudflare.com/fair-shot/)


COMPANY
  * [About Cloudflare](https://www.cloudflare.com/about-overview/)
  * [Network map](https://www.cloudflare.com/network/)
  * [Our team](https://www.cloudflare.com/people/)
  * [Logos & press kit](https://www.cloudflare.com/press/press-kit/)
  * [Diversity, equity, & inclusion](https://www.cloudflare.com/diversity-equity-and-inclusion/)
  * [Impact/ESG](https://www.cloudflare.com/impact/)


[](https://www.facebook.com/cloudflare "Facebook")[](https://x.com/cloudflare "X")[](https://www.linkedin.com/company/cloudflare "LinkedIn")[](https://www.youtube.com/cloudflare "Youtube")[](https://instagram.com/cloudflare "Instagram")
© 2026 Cloudflare, Inc.[Privacy Policy](https://www.cloudflare.com/privacypolicy/)[Terms of Use](https://www.cloudflare.com/website-terms/)[Report Security Issues](https://www.cloudflare.com/disclosure/)![privacy options](https://www.cloudflare.com/img/privacyoptions.svg)Cookie Preferences[Trademark](https://www.cloudflare.com/trademark/)
![](https://5bav82-m.ns1pcdn.net/a/t128.jpg?r=66692649)![](https://1xtvhvx-m.ns1pcdn.net/a/t128.jpg?r=32767442)![](https://ns1p-aws-backed.global.ssl.fastly.net/a/t128.jpg?r=1184237)![](https://1lmnv6z-m.ns1pcdn.net/a/t128.jpg?r=49314925)![](https://1xtsor1-m.ns1pcdn.net/a/t128.jpg?r=53304490)![](https://fastly.jsdelivr.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=76653031)![](https://testingcf.jsdelivr.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=37880831)![](https://jsdelivr.b-cdn.net/gh/jimaek/testobjects@0.0.1/r20-100KB.png?r=96810018)![](https://9y49n2-m.ns1pcdn.net/a/t128.jpg?r=65625024)![](https://1a4s4dv-m.ns1pcdn.net/a/t128.jpg?r=59857479)![](https://kgnvry-ns1p.b-cdn.net/a/t128.jpg?r=75118405)![](https://benchmarks.cdn-c.compute-pipe.com/r20-100KB.png?r=41055430)![](https://benchmark.1e100cdn.net/r20-100KB.png?r=18700387)![](https://benchmarks.cdn.compute-pipe.com/r20-100KB.png?r=75445805)![](https://cedexis-test.akamaized.net/img/r20-100KB.png?r=48330758)![](https://benchmarks.cdn-b.compute-pipe.com/r20-100KB.png?r=91682776)
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b60e5d5e-6618-48fc-8fa2-ac106d5d7f98&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8adefcce-bff4-46b7-b1da-1e456445d576&restricted_data_use=restrict_optimization&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fdns%2Fdnssec%2Fdnssec-complexities-and-considerations%2F&tw_engaged_ms=154&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444048934-751291570&twpid=tw.1791444048934.805112577849113746&txn_id=nvldc&type=javascript&version=2.4.11)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=b60e5d5e-6618-48fc-8fa2-ac106d5d7f98&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8adefcce-bff4-46b7-b1da-1e456445d576&restricted_data_use=restrict_optimization&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fdns%2Fdnssec%2Fdnssec-complexities-and-considerations%2F&tw_engaged_ms=154&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444048934-751291570&twpid=tw.1791444048934.805112577849113746&txn_id=nvldc&type=javascript&version=2.4.11)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=592da6b9-e40b-4940-ae21-a282bd170a84&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8adefcce-bff4-46b7-b1da-1e456445d576&restricted_data_use=restrict_optimization&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fdns%2Fdnssec%2Fdnssec-complexities-and-considerations%2F&tw_engaged_ms=31&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444048934-751291570&twpid=tw.1791444048934.805112577849113746&txn_id=pomsv&type=javascript&version=2.4.11)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%262%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=592da6b9-e40b-4940-ae21-a282bd170a84&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8adefcce-bff4-46b7-b1da-1e456445d576&restricted_data_use=restrict_optimization&tw_ch_fvl=HeadlessChrome%2F153.0.8010.12%2CNot_A%20Brand%2F8.0.0.0%2CChromium%2F153.0.8010.12&tw_document_href=https%3A%2F%2Fwww.cloudflare.com%2Fdns%2Fdnssec%2Fdnssec-complexities-and-considerations%2F&tw_engaged_ms=31&tw_iframe_status=0&tw_pid_src=2&tw_session_count=1&tw_session_id=1791444048934-751291570&twpid=tw.1791444048934.805112577849113746&txn_id=pomsv&type=javascript&version=2.4.11)
