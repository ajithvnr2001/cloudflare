---
url: https://www.cloudflare.com/learning/dns/common-dns-issues/
title: Common DNS issues and how to fix them
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:03.838892+00:00
---

# Common DNS issues and how to fix them

> Source: https://www.cloudflare.com/learning/dns/common-dns-issues/

[ Learning Center ](https://www.cloudflare.com/learning/) / DNS

##  Common DNS issues and how to fix them 

Sometimes a website or application does not work properly because of DNS issues, including improperly configured DNS records, latency, or malicious attacks. 

[Learning Center](https://www.cloudflare.com/learning)/DNS/[Common DNS issues and how to fix them](https://www.cloudflare.com/learning/dns/common-dns-issues/)[What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)[What is DNS fast flux?](https://www.cloudflare.com/learning/dns/dns-fast-flux/)[DNS over TLS vs. DNS over HTTPS | Secure DNS](https://www.cloudflare.com/learning/dns/dns-over-tls/)[DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)[DNS AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/)[What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)[What is a DNS DKIM record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/)[What is a DNS DMARC record?](https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/)[What is a DNS MX record?](https://www.cloudflare.com/learning/dns/dns-records/dns-mx-record/)[DNS NS record](https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/)[What is a DNS PTR record?](https://www.cloudflare.com/learning/dns/dns-records/dns-ptr-record/)[What is a DNS SOA record?](https://www.cloudflare.com/learning/dns/dns-records/dns-soa-record/)[What is a DNS SPF record?](https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/)[What is a DNS SRV record?](https://www.cloudflare.com/learning/dns/dns-records/dns-srv-record/)[What is a DNS TXT record?](https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/)[DNS DNSKEY and DS Records](https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/)[How to protect domains that do not send email ](https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/)[ECDSA: The missing piece of DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/ecdsa-and-dnssec/)[How does DNSSEC work?](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/)[The DNSSEC Root Signing Ceremony](https://www.cloudflare.com/learning/dns/dnssec/root-signing-ceremony/)[Universal DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/universal-dnssec/)[How to choose the best domain name registrar](https://www.cloudflare.com/learning/dns/glossary/choose-the-best-domain-name-registrar/)[DNS root server](https://www.cloudflare.com/learning/dns/glossary/dns-root-server/)[What is a DNS zone?](https://www.cloudflare.com/learning/dns/glossary/dns-zone/)[Dynamic DNS](https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/)[What happens to expired domains?](https://www.cloudflare.com/learning/dns/glossary/expired-domains/)[What is a premium domain?](https://www.cloudflare.com/learning/dns/glossary/premium-domains/)[Primary vs secondary DNS](https://www.cloudflare.com/learning/dns/glossary/primary-secondary-dns/)[What is reverse DNS?](https://www.cloudflare.com/learning/dns/glossary/reverse-dns/)[What is round-robin DNS?](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/)[What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)[What is a domain name registrar?](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/)[What is my IP address?](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/)[How much does a domain name cost?](https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/)[How to buy a domain name](https://www.cloudflare.com/learning/dns/how-to-buy-a-domain-name/)[How to transfer a domain name](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/)[What is a top-level domain (TLD)?](https://www.cloudflare.com/learning/dns/top-level-domain/)[What is 1.1.1.1?](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1)[What is a DNS server?](https://www.cloudflare.com/learning/dns/what-is-a-dns-server/)[What is a DNS server? (1) (PAYGO TEST)](https://www.cloudflare.com/learning/dns/what-is-a-dns-server-1-paygo-test/)[What is Anycast DNS? | How Anycast works with DNS](https://www.cloudflare.com/learning/dns/what-is-anycast-dns/)[What is cybersquatting?](https://www.cloudflare.com/learning/dns/what-is-cybersquatting/)[What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)[What is domain hijacking?](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/)[What is domain privacy?](https://www.cloudflare.com/learning/dns/what-is-domain-privacy/)[What is recursive DNS?](https://www.cloudflare.com/learning/dns/what-is-recursive-dns/)[DNS security](https://www.cloudflare.com/learning/dns/dns-security/)[DNS server types](https://www.cloudflare.com/learning/dns/dns-server-types/)[DNS records](https://www.cloudflare.com/learning/dns/dns-records/)

######  Learning objectives 

After reading this article you will be able to: 

  * Explain what DNS does 
  * Understand how to fix common DNS issues 
  * Understand where 'DNS_PROBE_FINISHED_NXDOMAIN' errors come from 



Related content  [ What is DNS? ](https://www.cloudflare.com/learning/dns/what-is-dns/)[ DNS records ](https://www.cloudflare.com/learning/dns/dns-records/)

On this page

  * Common DNS issues and how to fix them

  * Incorrect DNS records

  * Time-to-live is set too high

  * DNS DDoS attack

  * High latency

  * DNS cache poisoning

  * Domain hijacking

  * What does it mean when page visitors receive a &#39

    * What does &#39

  * How does Cloudflare help prevent these DNS issues?




## Common DNS issues and how to fix them

The Domain Name System, or [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/), maps [domain names](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) to [IP addresses](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) so that people can use web apps without memorizing precise network addresses. DNS is used for storing lots of other information associated with a domain as well — for instance, where to direct [emails](https://www.cloudflare.com/learning/email-security/what-is-email/). DNS can cause issues if it is not set up properly, if attackers are targeting it, or if other technical challenges occur. Here is an overview of some of the most common DNS issues website administrators are likely to face.

## Incorrect DNS records

The DNS records for the domain could be configured incorrectly. If the domain is misspelled in the records, if the wrong IP address is listed on the record, or if other essential information is missing or wrong, DNS will likely fail to resolve.

In addition to these basic errors, several types of DNS records are associated with a domain. Issues with those records could cause DNS errors. For instance, a domain could have an [A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/) but lack an [AAAA record](https://www.cloudflare.com/learning/dns/dns-records/dns-aaaa-record/), causing DNS resolution to initially fail for clients that use IPv6. Or, if the client is trying to reach an alternate domain (e.g. "blog.example.com" instead of "[www.example.com](http://www.example.com)"), the domain's [CNAME record](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/) might not point to the right place.

To fix this error, site administrators should check the DNS records in their hosting provider or DNS provider's dashboard and make sure there are no errors. The DNS records then need to be fetched by DNS resolvers — the servers that reply to DNS queries — for the most up-to-date versions to be in the system. As long as the TTL is not set too high (see below) this should not take too long.

## Time-to-live (TTL) is set too high

All DNS records contain a time-to-live (TTL)*, which is a count of the number of seconds for which a server may consider the record valid before having to re-query for an update. Essentially, TTL is like a "use by" date on a packaged food item: records are considered usable until the TTL time ends.

If the TTL is set too high, servers will wait too long to check for an update to DNS records. This means any changes will spread very slowly across the domain name system. Browsers might try to reach sites at the wrong IP address if DNS records have been updated for a domain but they have not received the updates.

To avoid this DNS issue, be sure TTLs are not too large: typically, the absolute maximum value is 86400 (counted in seconds, this equates to 24 hours), but most TTLs are much shorter (6 hours or less). The exact TTL for a record should depend on how often and quickly that record is expected to be updated in the future. ([See information on TTL for Cloudflare DNS records](https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/).)

In addition, some DNS resolvers allow domain administrators to force a refresh of their caches for a domain — [you can do so for Cloudflare's 1.1.1.1 here](https://one.one.one.one/purge-cache/). But doing so does not flush all caches of all resolvers worldwide, so this is not a replacement for setting TTLs properly.

**[TTL](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/) is used in other areas of networking as well, such as routing and caching.*

## DNS DDoS attack

[Distributed denial-of-service (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) attacks aim to do just what their name says: deny service. DDoS attacks bombard the target with junk traffic so that legitimate users cannot use the service. These attacks can make a website, application, [API](https://www.cloudflare.com/learning/security/api/what-is-an-api/), or server unavailable for minutes or hours at a time.

When the DDoS target is DNS itself, browsers will be unable to resolve domains, which means users cannot load websites and apps, since their IP address cannot be found. A major attack of this kind took place in [2016](https://en.wikipedia.org/wiki/DDoS_attacks_on_Dyn), when an attack on Dyn left users in many parts of the world without the ability to use the Internet. Smaller DDoS attacks on DNS occur regularly and can be more targeted.

Avoid this problem by ensuring each domain's DNS provider has [DDoS protection](https://www.cloudflare.com/ddos/) in place, or by implementing DDoS mitigation for self-hosted DNS resolution.

## High latency

[Latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/) is the time it takes for data to go from one point to another. High amounts of latency result in slow responses — or even request timeouts that terminate the connection.

Network congestion can cause latency, but the biggest culprit is often server location. DNS queries are pretty lightweight relative to other web traffic, but a faraway DNS resolver means a user might have to wait many seconds while the request travels to the server and the response comes back from the server. This problem might come up when users are attempting to load web content from an unexpected location or a different region of the world than normal, far from a DNS provider's network of servers.

To fix high DNS latency, use a DNS provider that has points of presence close to Internet users all over the globe. [Learn about the Cloudflare global network](https://www.cloudflare.com/network/).

## DNS cache poisoning

In [DNS cache poisoning](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/) attacks, a malicious party tricks a DNS resolver into caching an incorrect IP address for a domain. The result is that users trying to load that domain are instead directed to the IP address supplied by the attacker.

Adopting [DNSSEC](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/) is a way to prevent unverified data from entering DNS resolver caches. DNSSEC authenticates messages between DNS servers (without DNSSEC, DNS operates on a principle of trust, which attackers can exploit).

## Domain hijacking

A [domain hijacking](https://www.cloudflare.com/learning/dns/what-is-domain-hijacking/) attack is when attackers alter the DNS records associated with a domain. Often they do this by getting domain registrars to [transfer domains](https://www.cloudflare.com/learning/dns/how-to-transfer-a-domain-name/) to them. As a result, site visitors may load the wrong webpage — often a malicious one — or the domain can fail to resolve altogether.

Applying domain locks at both the [registrar](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name-registrar/) and registry level can make DNS hijacking considerably more difficult for attackers.

## What does it mean when page visitors receive a 'DNS_PROBE_FINISHED_NXDOMAIN' error?

"NXDOMAIN" is computer-speak for "nonexistent domain." Essentially, this error means that as far as the user's device can tell, the domain does not exist — like trying to call a nonexistent phone number or send a package to a city that does not exist.

This is a broad error that can be caused by the problems listed above, as well as problems on the client side (the device on which the person is trying to load the website):

  * The client could be disconnected from the Internet

  * There could be a typo in the URL that the client is trying to reach

  * The browser DNS cache needs to be refreshed

  * The client's default DNS resolver might be down




Users can try reconnecting to their local network, hard-refreshing the webpage (Ctrl/Command + Shift + R), opening it in a different browser, or changing their DNS settings to use a different resolver (Cloudflare offers the highly reliable [1.1.1.1](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/) DNS resolver for free).

#### What does 'DNS server not responding' mean?

An "NXDOMAIN" error may result in a "This site can't be reached" or "DNS server not responding" message in the browser. As described above, a number of problems can cause this error message.

## How does Cloudflare help prevent these DNS issues?

For people and businesses running web apps, most of these issues can be fixed or mitigated by adopting Cloudflare, which proxies traffic to websites and uses the latest security measures to protect against DDoS attacks, DNS hijacking, DNS cache poisoning, and DNS misconfigurations. [See Cloudflare plans to get started](https://www.cloudflare.com/plans).

Need more support with DNS and network issues? [Join the Cloudflare Community](https://community.cloudflare.com/t/community-tip-dns-network-faq-read-me-first/248900/4?q=cdn&utm_campaign=learningcenter&utm_content=dns_troubleshooting_lp) for free support and insights from other Cloudflare users.
