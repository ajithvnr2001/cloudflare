---
url: https://developers.cloudflare.com/ddos-protection/about/attack-coverage/
title: DDoS attack coverage \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.230164+00:00
---

# DDoS attack coverage · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/about/attack-coverage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /[About](https://developers.cloudflare.com/ddos-protection/about/)
  4. /Attack coverage



# Attack coverage

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/about/attack-coverage/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGetting additional DNS protectionEmail-based attacks

The [DDoS Attack Protection managed rulesets](https://developers.cloudflare.com/ddos-protection/managed-rulesets/) provide protection against a variety of DDoS attacks across L3/4 (layers 3/4) and L7 of the OSI model. Cloudflare constantly updates these managed rulesets to improve the attack coverage, increase the mitigation consistency, cover new and emerging threats, and ensure cost-efficient mitigations.

[Advanced TCP Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/), [Advanced DNS Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/), and [Programmable Flow Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/programmable-flow-protection/) are available to Magic Transit customers. Advanced TCP Protection provides additional protection against sophisticated TCP-based DDoS attacks. Advanced DNS Protections protects against sophisticated and fully randomized DNS attacks. Programmable Flow Protection mitigates UDP-based attacks by executing a customer-defined program.

As a general guideline, various Cloudflare products operate on different open systems interconnection (OSI) layers and you are protected up to the layer on which your service operates. You can customize the DDoS settings on the layer in which you onboarded. For example, since the CDN/WAF service is a Layer 7 (HTTP/HTTPS) service, Cloudflare provides protection from DDoS attacks on L7 downwards, including L3/4 attacks.

Note

For Magic Transit customers, Cloudflare provides some L7 protection with a L3 service (like the Advanced DNS Protection system that is available for Magic Transit customers. DNS is considered a L7 protocol).

The following table includes a sample of covered attack vectors:

OSI Layer | Ruleset / Feature | Example of covered DDoS attack vectors  
---|---|---  
L3/4 | [Network-layer DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/network/) | ACK floods  
BitTorrent reflection attack  
Carpet Bombing attacks  
CHARGEN reflection attacks  
DNS amplification attack  
DNS Garbage Flood  
DNS NXDOMAIN flood  
DNS Query flood  
DTLS amplification attacks  
ESP flood  
GRE floods  
ICMP flood attack  
Jenkins amplification attacks  
Lantronix reflection attacks  
mDNS DDoS attacks  
Memcached amplification attacks  
Mirai and Mirai-variant L3/4 attacks  
MSSQL reflection attacks  
NetBios DDoS attacks  
Out of state TCP attacks  
Protocol violation attacks  
QUIC flood attack  
Quote of the Day (QOTD) reflection attacks  
RST flood  
SIP attacks  
SNMP flood attack  
SPSS reflection attacks  
SSDP reflection attacks  
SYN floods  
SYN-ACK reflection attack  
TeamSpeak 3 floods  
Ubiquity reflection attacks  
UDP flood attack  
VxWorks DDoS attacks  
  
For more DNS protection options, refer to [Getting additional DNS protection](https://developers.cloudflare.com/ddos-protection/about/attack-coverage/#getting-additional-dns-protection).  
L3/4 | [Advanced TCP Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/) 1 | Fully randomized and spoofed ACK floods, SYN floods, SYN-ACK reflection attacks, and other sophisticated TCP-based DDoS attacks  
L7 (DNS) | [Advanced DNS Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/) 1 | Sophisticated and fully randomized DNS attacks, including Water Torture attacks, Random-prefix attacks, and DNS laundering attacks.  
L7 (HTTP/S) | [HTTP DDoS Attack Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/http/) | Cache busting attacks  
Carpet Bombing attacks  
HTTP Continuation flood  
HTTP flood attack  
HTTP/2 MadeYouReset  
HTTP/2 Rapid Reset  
HULK attack  
Known DDoS botnets  
LOIC attack  
Mirai and Mirai-variant HTTP attacks  
Slowloris attack  
TLS/SSL exhaustion attacks  
TLS/SSL negotiation attacks  
WordPress pingback attack  
  
  
## Footnotes

  1. Available to Magic Transit customers. ↩ ↩2




## Getting additional DNS protection

The Network-layer DDoS Attack Protection managed ruleset provides protection against some types of DNS attacks.

Magic Transit customers have access to [Advanced DNS Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/) Beta. Other customers might consider the following options:

  * Use Cloudflare as your authoritative DNS provider ([primary DNS](https://developers.cloudflare.com/dns/zone-setups/full-setup/) or [secondary DNS](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/)).
  * If you are running your own nameservers, use [DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/) to get additional protection against DNS attacks like random prefix attacks.



## Email-based attacks

DDoS Protection covers web and network protocols, including TCP, UDP, DNS, and HTTP/S. It does not cover email protocols such as SMTP, IMAP, or POP3.

For protection against email-borne threats such as phishing and malware, refer to [Email Security](https://developers.cloudflare.com/email-security/).

[PreviousMain components](https://developers.cloudflare.com/ddos-protection/about/components/)[NextOverview](https://developers.cloudflare.com/ddos-protection/managed-rulesets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/about/attack-coverage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
