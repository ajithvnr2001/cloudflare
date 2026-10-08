---
url: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/
title: DDoS Protection \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:42.729606+00:00
---

# DDoS Protection · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Default traffic security](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/)
  5. /DDoS Protection



# DDoS Protection

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ddos/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare automatically detects and mitigates DDoS attacks using its [Autonomous Edge](https://developers.cloudflare.com/ddos-protection/about/components/#autonomous-edge), which is always-on. `Advanced` protections are reserved for Magic Transit customers.

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




Refer to the learning path [Prevent DDoS attacks](https://developers.cloudflare.com/learning-paths/prevent-ddos-attacks/concepts/) to dive deeper into this subject.

[PreviousOverview](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/)[NextBrowser Integrity](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/browser-integrity/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/default-traffic-security/ddos.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
