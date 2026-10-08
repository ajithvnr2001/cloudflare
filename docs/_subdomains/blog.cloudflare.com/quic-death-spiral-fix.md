---
url: https://blog.cloudflare.com/quic-death-spiral-fix/
title: When \"idle\" isn't idle: how a Linux kernel optimization became a QUIC bug | Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:38.159566+00:00
---

# When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug | Cloudflare Blog

> Source: https://blog.cloudflare.com/quic-death-spiral-fix/

[Blog](https://blog.cloudflare.com/)

[Congestion Control](https://blog.cloudflare.com/tag/congestion-control/)[Debugging](https://blog.cloudflare.com/tag/debugging/)[HTTP3](https://blog.cloudflare.com/tag/http3/)+4Show 4 more tags

7 TagsShow 7 tags

  * Post Tags
  * [Congestion Control](https://blog.cloudflare.com/tag/congestion-control/)[Debugging](https://blog.cloudflare.com/tag/debugging/)[HTTP3](https://blog.cloudflare.com/tag/http3/)[Networking](https://blog.cloudflare.com/tag/networking/)[QUIC](https://blog.cloudflare.com/tag/quic/)[QUICHE](https://blog.cloudflare.com/tag/quiche/)[Rust](https://blog.cloudflare.com/tag/rust/)
  * All tags
  * Matching tags
  * No tags found
  * [1.1.1.1](https://blog.cloudflare.com/tag/1-1-1-1/)
  * [2FA](https://blog.cloudflare.com/tag/2fa/)
  * [Abuse](https://blog.cloudflare.com/tag/abuse/)
  * [Access](https://blog.cloudflare.com/tag/access/)
  * [Access Control Lists (ACLs)](https://blog.cloudflare.com/tag/access-control-lists-acls/)
  * [Accessibility](https://blog.cloudflare.com/tag/accessibility/)
  * [Account Takeover](https://blog.cloudflare.com/tag/account-takeover/)
  * [Acquisitions](https://blog.cloudflare.com/tag/acquisitions/)
  * [Addressing](https://blog.cloudflare.com/tag/addressing/)
  * [Advanced Certificate Manager](https://blog.cloudflare.com/tag/advanced-certificate-manager/)
  * [Advanced DDoS](https://blog.cloudflare.com/tag/advanced-ddos/)
  * [Advertising](https://blog.cloudflare.com/tag/advertising/)
  * [Aegis](https://blog.cloudflare.com/tag/aegis/)
  * [AEO](https://blog.cloudflare.com/tag/aeo/)
  * [Africa](https://blog.cloudflare.com/tag/africa/)
  * [Afroflare](https://blog.cloudflare.com/tag/afroflare/)
  * [Agent Cloud](https://blog.cloudflare.com/tag/agent-cloud/)
  * [Agent Development Lifecycle](https://blog.cloudflare.com/tag/agent-development-lifecycle/)
  * [Agent Readiness](https://blog.cloudflare.com/tag/agent-readiness/)
  * [Agents](https://blog.cloudflare.com/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/tag/agents-week/)
  * [Agents Week 2026](https://blog.cloudflare.com/tag/agents-week-2026/)
  * [AI](https://blog.cloudflare.com/tag/ai/)
  * [AI Bots](https://blog.cloudflare.com/tag/ai-bots/)
  * [AI Gateway](https://blog.cloudflare.com/tag/ai-gateway/)
  * [AI Search](https://blog.cloudflare.com/tag/ai-search/)
  * [AI WAF](https://blog.cloudflare.com/tag/ai-waf/)
  * [AI Week](https://blog.cloudflare.com/tag/ai-week/)
  * [AI-SPM](https://blog.cloudflare.com/tag/ai-spm/)
  * [Alertmanager](https://blog.cloudflare.com/tag/alertmanager/)
  * [Always Online](https://blog.cloudflare.com/tag/always-online/)
  * [AMD](https://blog.cloudflare.com/tag/amd/)
  * [AMP](https://blog.cloudflare.com/tag/amp-tag/)
  * [Analytics](https://blog.cloudflare.com/tag/analytics/)
  * [Anonymous](https://blog.cloudflare.com/tag/anonymous/)
  * [Anti Malware](https://blog.cloudflare.com/tag/anti-malware/)
  * [Anycast](https://blog.cloudflare.com/tag/anycast/)
  * [API](https://blog.cloudflare.com/tag/api/)
  * [API Gateway](https://blog.cloudflare.com/tag/api-gateway/)
  * [API Security](https://blog.cloudflare.com/tag/api-security/)
  * [API Shield](https://blog.cloudflare.com/tag/api-shield/)
  * [APJC](https://blog.cloudflare.com/tag/apjc/)
  * [Apple](https://blog.cloudflare.com/tag/apple/)
  * [Application Security](https://blog.cloudflare.com/tag/application-security/)
  * [Application Services](https://blog.cloudflare.com/tag/application-services/)
  * [Area 1 Security](https://blog.cloudflare.com/tag/area-1-security/)
  * [Argo Smart Routing](https://blog.cloudflare.com/tag/argo/)
  * [ASCII](https://blog.cloudflare.com/tag/ascii/)
  * [Asia](https://blog.cloudflare.com/tag/asia/)
  * [Athenian Project](https://blog.cloudflare.com/tag/athenian-project/)
  * [Atlassian](https://blog.cloudflare.com/tag/atlassian/)
  * [Attacks](https://blog.cloudflare.com/tag/attacks/)
  * [Audit Logs](https://blog.cloudflare.com/tag/audit-logs/)
  * [Austin](https://blog.cloudflare.com/tag/austin/)
  * [Australia](https://blog.cloudflare.com/tag/australia/)
  * [Authentication](https://blog.cloudflare.com/tag/authentication/)
  * [Authy](https://blog.cloudflare.com/tag/authy/)
  * [Auto Rag](https://blog.cloudflare.com/tag/auto-rag/)
  * [Automatic HTTPS](https://blog.cloudflare.com/tag/automatic-https/)
  * [Automatic Platform Optimization](https://blog.cloudflare.com/tag/automatic-platform-optimization/)
  * [Automation](https://blog.cloudflare.com/tag/automation/)
  * [AutoMinify](https://blog.cloudflare.com/tag/autominify/)
  * [Awards](https://blog.cloudflare.com/tag/awards/)
  * [AWS](https://blog.cloudflare.com/tag/aws/)
  * [Baidu](https://blog.cloudflare.com/tag/baidu/)
  * [Bandwidth Alliance](https://blog.cloudflare.com/tag/bandwidth-alliance/)
  * [Bandwidth Costs](https://blog.cloudflare.com/tag/bandwidth-costs/)
  * [Best Practices](https://blog.cloudflare.com/tag/best-practices/)
  * [Beta](https://blog.cloudflare.com/tag/beta/)
  * [Better Internet](https://blog.cloudflare.com/tag/better-internet/)
  * [BGP](https://blog.cloudflare.com/tag/bgp/)
  * [Billing](https://blog.cloudflare.com/tag/billing/)
  * [Birthday Week](https://blog.cloudflare.com/tag/birthday-week/)
  * [Black Friday](https://blog.cloudflare.com/tag/black-friday/)
  * [Blackbird](https://blog.cloudflare.com/tag/blackbird/)
  * [Bot Fight Mode](https://blog.cloudflare.com/tag/bot-fight-mode/)
  * [Bot Management](https://blog.cloudflare.com/tag/bot-management/)
  * [Botnet](https://blog.cloudflare.com/tag/botnet/)
  * [Bots](https://blog.cloudflare.com/tag/bots/)
  * [BPF](https://blog.cloudflare.com/tag/bpf/)
  * [Brand](https://blog.cloudflare.com/tag/brand/)
  * [Brand Protection](https://blog.cloudflare.com/tag/brand-protection/)
  * [Brazil](https://blog.cloudflare.com/tag/brazil/)
  * [Browser Insights](https://blog.cloudflare.com/tag/browser-insights/)
  * [Browser Rendering](https://blog.cloudflare.com/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/tag/browser-run/)
  * [Bug Bounty](https://blog.cloudflare.com/tag/bug-bounty/)
  * [Bugs](https://blog.cloudflare.com/tag/bugs/)
  * [BYOIP](https://blog.cloudflare.com/tag/byoip/)
  * [Cache](https://blog.cloudflare.com/tag/cache/)
  * [Cache Purge](https://blog.cloudflare.com/tag/cache-purge/)
  * [Cache Reserve](https://blog.cloudflare.com/tag/cache-reserve/)
  * [Cache Rules](https://blog.cloudflare.com/tag/cache-rules/)
  * [California](https://blog.cloudflare.com/tag/california/)
  * [Canada](https://blog.cloudflare.com/tag/canada/)
  * [Cap'n Proto](https://blog.cloudflare.com/tag/capn-proto/)
  * [CAPTCHA](https://blog.cloudflare.com/tag/captcha/)
  * [Careers](https://blog.cloudflare.com/tag/careers/)
  * [CASB](https://blog.cloudflare.com/tag/casb/)
  * [Categories](https://blog.cloudflare.com/tag/categories/)
  * [CDN](https://blog.cloudflare.com/tag/cdn/)
  * [CDNJS](https://blog.cloudflare.com/tag/cdnjs/)
  * [Certificate Authority](https://blog.cloudflare.com/tag/certificate-authority/)
  * [Certificate Pinning](https://blog.cloudflare.com/tag/certificate-pinning/)
  * [Certificate Transparency](https://blog.cloudflare.com/tag/certificate-transparency/)
  * [Certification](https://blog.cloudflare.com/tag/certification/)
  * [CFSSL](https://blog.cloudflare.com/tag/cfssl/)
  * [Challenge Page](https://blog.cloudflare.com/tag/challenge-page/)
  * [ChatGPT](https://blog.cloudflare.com/tag/chatgpt/)
  * [China](https://blog.cloudflare.com/tag/china/)
  * [China Network](https://blog.cloudflare.com/tag/china-network/)
  * [Christmas](https://blog.cloudflare.com/tag/christmas/)
  * [Chrome](https://blog.cloudflare.com/tag/chrome/)
  * [CIO Week](https://blog.cloudflare.com/tag/cio-week/)
  * [CISA](https://blog.cloudflare.com/tag/cisa/)
  * [Claire](https://blog.cloudflare.com/tag/claire/)
  * [CLI](https://blog.cloudflare.com/tag/cli/)
  * [ClickHouse](https://blog.cloudflare.com/tag/clickhouse/)
  * [Clientless](https://blog.cloudflare.com/tag/clientless/)
  * [Clientless Web Isolation](https://blog.cloudflare.com/tag/clientless-web-isolation/)
  * [Cloud Connector](https://blog.cloudflare.com/tag/cloud-connector/)
  * [Cloud Email Security](https://blog.cloudflare.com/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/tag/cloudflare-access/)
  * [Cloudflare Apps](https://blog.cloudflare.com/tag/cloudflare-apps/)
  * [Cloudflare Area 1](https://blog.cloudflare.com/tag/cloudflare-area-1/)
  * [Cloudflare Calls](https://blog.cloudflare.com/tag/cloudflare-calls/)
  * [Cloudflare Email Service](https://blog.cloudflare.com/tag/cloudflare-email-services/)
  * [Cloudflare for Campaigns](https://blog.cloudflare.com/tag/cloudflare-for-campaigns/)
  * [Cloudflare for SaaS](https://blog.cloudflare.com/tag/cloudflare-for-saas/)
  * [Cloudflare for Startups](https://blog.cloudflare.com/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/tag/gateway/)
  * [Cloudflare History](https://blog.cloudflare.com/tag/cloudflare-history/)
  * [Cloudflare Images](https://blog.cloudflare.com/tag/cloudflare-images/)
  * [Cloudflare Media Platform](https://blog.cloudflare.com/tag/cloudflare-media-platform/)
  * [Cloudflare Meetups](https://blog.cloudflare.com/tag/cloudflare-meetups/)
  * [Cloudflare Network](https://blog.cloudflare.com/tag/cloudflare-network/)
  * [Cloudflare One](https://blog.cloudflare.com/tag/cloudflare-one/)
  * [Cloudflare One Client](https://blog.cloudflare.com/tag/cloudflare-one-client/)
  * [Cloudflare One User Risk Score](https://blog.cloudflare.com/tag/cloudflare-one-user-risk-score/)
  * [Cloudflare One Week](https://blog.cloudflare.com/tag/cloudflare-one-week/)
  * [Cloudflare OS](https://blog.cloudflare.com/tag/cloudflare-os/)
  * [Cloudflare Pages](https://blog.cloudflare.com/tag/cloudflare-pages/)
  * [Cloudflare Polish](https://blog.cloudflare.com/tag/cloudflare-polish/)
  * [Cloudflare Queues](https://blog.cloudflare.com/tag/cloudflare-queues/)
  * [Cloudflare Realtime](https://blog.cloudflare.com/tag/cloudflare-realtime/)
  * [Cloudflare Stream](https://blog.cloudflare.com/tag/cloudflare-stream/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/tag/cloudflare-tunnel/)
  * [Cloudflare TV](https://blog.cloudflare.com/tag/cloudflare-tv/)
  * [Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)
  * [Cloudflare Workers (PT)](https://blog.cloudflare.com/tag/cloudflare-workers-pt/)
  * [Cloudflare Workers KV](https://blog.cloudflare.com/tag/cloudflare-workers-kv/)
  * [Cloudflare Workers KV (ES)](https://blog.cloudflare.com/tag/cloudflare-workers-kv-es/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/tag/cloudforce-one/)
  * [Cloudy](https://blog.cloudflare.com/tag/cloudy/)
  * [Code Orange](https://blog.cloudflare.com/tag/code-orange/)
  * [Coinbase](https://blog.cloudflare.com/tag/coinbase/)
  * [Colombia](https://blog.cloudflare.com/tag/colombia/)
  * [Community](https://blog.cloudflare.com/tag/community/)
  * [Compliance](https://blog.cloudflare.com/tag/compliance/)
  * [Compression](https://blog.cloudflare.com/tag/compression/)
  * [Config Rules](https://blog.cloudflare.com/tag/config-rules/)
  * [Configuration Management](https://blog.cloudflare.com/tag/configuration-management/)
  * [Congestion Control](https://blog.cloudflare.com/tag/congestion-control/)
  * [Connectivity](https://blog.cloudflare.com/tag/connectivity/)
  * [Connectivity Cloud](https://blog.cloudflare.com/tag/connectivity-cloud/)
  * [Consumer Services](https://blog.cloudflare.com/tag/consumer-services/)
  * [Containers](https://blog.cloudflare.com/tag/containers/)
  * [Content Independence Day](https://blog.cloudflare.com/tag/content-independence-day/)
  * [Content Scanning](https://blog.cloudflare.com/tag/content-scanning/)
  * [Context](https://blog.cloudflare.com/tag/context/)
  * [Core](https://blog.cloudflare.com/tag/core/)
  * [COVID-19](https://blog.cloudflare.com/tag/covid-19/)
  * [Crawler Hints](https://blog.cloudflare.com/tag/crawler-hints/)
  * [CrowdStrike](https://blog.cloudflare.com/tag/crowdstrike/)
  * [Crypto Week](https://blog.cloudflare.com/tag/crypto-week/)
  * [Cryptography](https://blog.cloudflare.com/tag/cryptography/)
  * [CSAM Reporting](https://blog.cloudflare.com/tag/csam-reporting/)
  * [Customer Success](https://blog.cloudflare.com/tag/customer-success/)
  * [Customer Zero](https://blog.cloudflare.com/tag/customer-zero/)
  * [Customers](https://blog.cloudflare.com/tag/customers/)
  * [CVE](https://blog.cloudflare.com/tag/cve/)
  * [CVE-2023-50387](https://blog.cloudflare.com/tag/cve-2023-50387/)
  * [Cyber Readiness](https://blog.cloudflare.com/tag/cyber-readiness/)
  * [Cybersecurity](https://blog.cloudflare.com/tag/cybersecurity/)
  * [D1](https://blog.cloudflare.com/tag/d1/)
  * [Dashboard](https://blog.cloudflare.com/tag/dashboard-tag/)
  * [Data](https://blog.cloudflare.com/tag/data/)
  * [Data Catalog](https://blog.cloudflare.com/tag/data-catalog/)
  * [Data Center](https://blog.cloudflare.com/tag/data-center/)
  * [Data Localization](https://blog.cloudflare.com/tag/data-localization/)
  * [Data Localization Suite](https://blog.cloudflare.com/tag/data-localization-suite/)
  * [Data Loss](https://blog.cloudflare.com/tag/data-loss/)
  * [Data Loss Prevention](https://blog.cloudflare.com/tag/data-loss-prevention/)
  * [Data Platform](https://blog.cloudflare.com/tag/data-platform/)
  * [Data Privacy Day](https://blog.cloudflare.com/tag/data-privacy-day/)
  * [Data Protection](https://blog.cloudflare.com/tag/data-protection/)
  * [Data Sovereignty](https://blog.cloudflare.com/tag/data-sovereignty/)
  * [Data Transfer Bucket](https://blog.cloudflare.com/tag/data-transfer-bucket/)
  * [Database](https://blog.cloudflare.com/tag/database/)
  * [DDoS](https://blog.cloudflare.com/tag/ddos/)
  * [DDoS Alerts](https://blog.cloudflare.com/tag/ddos-alerts/)
  * [DDoS Reports](https://blog.cloudflare.com/tag/ddos-reports/)
  * [Debugging](https://blog.cloudflare.com/tag/debugging/)
  * [Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)
  * [Descaler](https://blog.cloudflare.com/tag/descaler/)
  * [Design](https://blog.cloudflare.com/tag/design/)
  * [Deskope](https://blog.cloudflare.com/tag/deskope/)
  * [Developer Documentation](https://blog.cloudflare.com/tag/developer-documentation/)
  * [Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)
  * [Developer Spotlight](https://blog.cloudflare.com/tag/developer-spotlight/)
  * [Developer Week](https://blog.cloudflare.com/tag/developer-week/)
  * [Developers](https://blog.cloudflare.com/tag/developers/)
  * [Developers Storage](https://blog.cloudflare.com/tag/developers-storage/)
  * [Device Security](https://blog.cloudflare.com/tag/device-security/)
  * [DevOps](https://blog.cloudflare.com/tag/devops/)
  * [DEX](https://blog.cloudflare.com/tag/dex/)
  * [Digital Experience Monitoring](https://blog.cloudflare.com/tag/digital-experience-monitoring/)
  * [Digital Forensics](https://blog.cloudflare.com/tag/digital-forensics/)
  * [Disrupt](https://blog.cloudflare.com/tag/disrupt/)
  * [Distributed](https://blog.cloudflare.com/tag/distributed/)
  * [Distributed Systems](https://blog.cloudflare.com/tag/distributed-systems/)
  * [Distributed Web](https://blog.cloudflare.com/tag/distributed-web/)
  * [Diversity](https://blog.cloudflare.com/tag/diversity/)
  * [DLP](https://blog.cloudflare.com/tag/dlp/)
  * [DMARC](https://blog.cloudflare.com/tag/dmarc/)
  * [DNS](https://blog.cloudflare.com/tag/dns/)
  * [DNS Filtering](https://blog.cloudflare.com/tag/dns-filtering/)
  * [DNS Flood](https://blog.cloudflare.com/tag/dns-flood/)
  * [DNS Security](https://blog.cloudflare.com/tag/dns-security/)
  * [DNSSEC](https://blog.cloudflare.com/tag/dnssec/)
  * [Dogfooding](https://blog.cloudflare.com/tag/dogfooding/)
  * [DoH](https://blog.cloudflare.com/tag/doh/)
  * [Domain Rankings](https://blog.cloudflare.com/tag/domain-rankings/)
  * [Domain Scoped Roles](https://blog.cloudflare.com/tag/domain-scoped-roles/)
  * [dosd](https://blog.cloudflare.com/tag/dosd/)
  * [Drupal](https://blog.cloudflare.com/tag/drupal/)
  * [Due Process](https://blog.cloudflare.com/tag/due-process/)
  * [Durable Execution](https://blog.cloudflare.com/tag/durable-execution/)
  * [Durable Objects](https://blog.cloudflare.com/tag/durable-objects/)
  * [Early Hints](https://blog.cloudflare.com/tag/early-hints/)
  * [Earth Day](https://blog.cloudflare.com/tag/earth-day/)
  * [eBPF](https://blog.cloudflare.com/tag/ebpf/)
  * [EC2](https://blog.cloudflare.com/tag/ec2/)
  * [eCommerce](https://blog.cloudflare.com/tag/ecommerce/)
  * [Edge](https://blog.cloudflare.com/tag/edge/)
  * [Edge Computing](https://blog.cloudflare.com/tag/edge-computing/)
  * [Edge Database](https://blog.cloudflare.com/tag/edge-database/)
  * [Edge Rules](https://blog.cloudflare.com/tag/edge-rules/)
  * [Education](https://blog.cloudflare.com/tag/education/)
  * [Egress](https://blog.cloudflare.com/tag/egress/)
  * [Elastic](https://blog.cloudflare.com/tag/elastic/)
  * [Election Security](https://blog.cloudflare.com/tag/election-security/)
  * [Elections](https://blog.cloudflare.com/tag/elections/)
  * [Elliptic Curves](https://blog.cloudflare.com/tag/elliptic-curves/)
  * [Email](https://blog.cloudflare.com/tag/email/)
  * [Email Routing](https://blog.cloudflare.com/tag/email-routing/)
  * [Email Security](https://blog.cloudflare.com/tag/email-security/)
  * [Email Workers](https://blog.cloudflare.com/tag/email-workers/)
  * [EmDash](https://blog.cloudflare.com/tag/emdash/)
  * [Emissions](https://blog.cloudflare.com/tag/emissions/)
  * [Employee Resource Groups](https://blog.cloudflare.com/tag/employee-resource-groups/)
  * [Encrypted SNI](https://blog.cloudflare.com/tag/encrypted-sni/)
  * [Encryption](https://blog.cloudflare.com/tag/encryption/)
  * [Engineering](https://blog.cloudflare.com/tag/engineering/)
  * [Enterprise](https://blog.cloudflare.com/tag/enterprise/)
  * [Entropy](https://blog.cloudflare.com/tag/entropy/)
  * [EPYC](https://blog.cloudflare.com/tag/epyc/)
  * [Ethereum](https://blog.cloudflare.com/tag/ethereum/)
  * [Europe](https://blog.cloudflare.com/tag/europe/)
  * [European Union](https://blog.cloudflare.com/tag/european-union/)
  * [Events](https://blog.cloudflare.com/tag/events/)
  * [Exploit](https://blog.cloudflare.com/tag/exploit/)
  * [Facebook](https://blog.cloudflare.com/tag/facebook/)
  * [Fancy Bear](https://blog.cloudflare.com/tag/fancy-bear/)
  * [Fast Fonts](https://blog.cloudflare.com/tag/fast-fonts/)
  * [FCC](https://blog.cloudflare.com/tag/fcc/)
  * [Feature Flags](https://blog.cloudflare.com/tag/feature-flags/)
  * [FedRAMP](https://blog.cloudflare.com/tag/fedramp/)
  * [FedRAMP High](https://blog.cloudflare.com/tag/fedramp-high/)
  * [FedRAMP Moderate](https://blog.cloudflare.com/tag/fedramp-moderate/)
  * [Firefox](https://blog.cloudflare.com/tag/firefox/)
  * [Firewall](https://blog.cloudflare.com/tag/firewall/)
  * [Firmware](https://blog.cloudflare.com/tag/firmware/)
  * [Florida](https://blog.cloudflare.com/tag/florida/)
  * [Football](https://blog.cloudflare.com/tag/football/)
  * [Formal Methods](https://blog.cloudflare.com/tag/formal-methods/)
  * [Forrester](https://blog.cloudflare.com/tag/forrester/)
  * [Fortran](https://blog.cloudflare.com/tag/fortran/)
  * [Foundation DNS](https://blog.cloudflare.com/tag/foundation-dns/)
  * [Founders' Letter](https://blog.cloudflare.com/tag/founders-letter/)
  * [France](https://blog.cloudflare.com/tag/france/)
  * [Fraud](https://blog.cloudflare.com/tag/fraud/)
  * [Free](https://blog.cloudflare.com/tag/free/)
  * [Freedom of Speech](https://blog.cloudflare.com/tag/freedom-of-speech/)
  * [Front End](https://blog.cloudflare.com/tag/front-end/)
  * [Full Stack](https://blog.cloudflare.com/tag/full-stack/)
  * [Full Stack Week](https://blog.cloudflare.com/tag/full-stack-week/)
  * [Fun](https://blog.cloudflare.com/tag/fun/)
  * [GA Week](https://blog.cloudflare.com/tag/ga-week/)
  * [Gartner](https://blog.cloudflare.com/tag/gartner/)
  * [Gatebot](https://blog.cloudflare.com/tag/gatebot/)
  * [GDPR](https://blog.cloudflare.com/tag/gdpr/)
  * [Gen X](https://blog.cloudflare.com/tag/gen-x/)
  * [General Availability](https://blog.cloudflare.com/tag/general-availability/)
  * [Generative AI](https://blog.cloudflare.com/tag/generative-ai/)
  * [Geo Key Manager](https://blog.cloudflare.com/tag/geo-key-manager/)
  * [Germany](https://blog.cloudflare.com/tag/germany/)
  * [GitHub](https://blog.cloudflare.com/tag/github/)
  * [Go](https://blog.cloudflare.com/tag/go/)
  * [Google](https://blog.cloudflare.com/tag/google/)
  * [Google Analytics](https://blog.cloudflare.com/tag/google-analytics/)
  * [Google Cloud](https://blog.cloudflare.com/tag/google-cloud/)
  * [Google Workspace](https://blog.cloudflare.com/tag/google-workspace/)
  * [Government Innovation](https://blog.cloudflare.com/tag/government-innovation/)
  * [Grace Hopper](https://blog.cloudflare.com/tag/grace-hopper/)
  * [Grafana](https://blog.cloudflare.com/tag/grafana/)
  * [GraphQL](https://blog.cloudflare.com/tag/graphql/)
  * [Green](https://blog.cloudflare.com/tag/green/)
  * [Grinch](https://blog.cloudflare.com/tag/grinch/)
  * [Growth](https://blog.cloudflare.com/tag/growth/)
  * [gRPC](https://blog.cloudflare.com/tag/grpc/)
  * [Guest Post](https://blog.cloudflare.com/tag/guest-post/)
  * [Hackathon](https://blog.cloudflare.com/tag/hackathon/)
  * [Halloween](https://blog.cloudflare.com/tag/halloween/)
  * [Hardware](https://blog.cloudflare.com/tag/hardware/)
  * [HashiCorp](https://blog.cloudflare.com/tag/hashicorp/)
  * [Hertzbleed](https://blog.cloudflare.com/tag/hertzbleed/)
  * [Heuristics](https://blog.cloudflare.com/tag/heuristics/)
  * [History](https://blog.cloudflare.com/tag/history/)
  * [Holidays](https://blog.cloudflare.com/tag/holidays/)
  * [Holocaust](https://blog.cloudflare.com/tag/holocaust/)
  * [Hong Kong](https://blog.cloudflare.com/tag/hongkong/)
  * [Hosting Con](https://blog.cloudflare.com/tag/hostingcon/)
  * [Hostnames](https://blog.cloudflare.com/tag/hostnames/)
  * [HTTP2](https://blog.cloudflare.com/tag/http2/)
  * [HTTP3](https://blog.cloudflare.com/tag/http3/)
  * [HTTPS](https://blog.cloudflare.com/tag/https/)
  * [Human Rights](https://blog.cloudflare.com/tag/human-rights/)
  * [Hurricane](https://blog.cloudflare.com/tag/hurricane/)
  * [Hybrid Cloud](https://blog.cloudflare.com/tag/hybrid-cloud/)
  * [Hyperdrive](https://blog.cloudflare.com/tag/hyperdrive/)
  * [I'm Under Attack Mode](https://blog.cloudflare.com/tag/iuam/)
  * [IBM](https://blog.cloudflare.com/tag/ibm/)
  * [ICANN](https://blog.cloudflare.com/tag/icann/)
  * [iCloud Private Relay](https://blog.cloudflare.com/tag/icloud-private-relay/)
  * [Identity](https://blog.cloudflare.com/tag/identity/)
  * [IETF](https://blog.cloudflare.com/tag/ietf/)
  * [IETF Standards](https://blog.cloudflare.com/tag/ietf-standards/)
  * [IL4](https://blog.cloudflare.com/tag/il4/)
  * [Image Optimization](https://blog.cloudflare.com/tag/image-optimization/)
  * [Image Recognition](https://blog.cloudflare.com/tag/image-recognition/)
  * [Image Resizing](https://blog.cloudflare.com/tag/image-resizing/)
  * [Image Storage](https://blog.cloudflare.com/tag/image-storage/)
  * [Impact](https://blog.cloudflare.com/tag/impact/)
  * [Impact Week](https://blog.cloudflare.com/tag/impact-week/)
  * [Incident Report](https://blog.cloudflare.com/tag/incident-report/)
  * [Incident Response](https://blog.cloudflare.com/tag/incident-response/)
  * [India](https://blog.cloudflare.com/tag/india/)
  * [Indicators of Compromise](https://blog.cloudflare.com/tag/indicators-of-compromise/)
  * [Indonesian](https://blog.cloudflare.com/tag/indonesian-id/)
  * [Inference](https://blog.cloudflare.com/tag/inference/)
  * [Infrastructure](https://blog.cloudflare.com/tag/infrastructure/)
  * [Infrastructure as Code](https://blog.cloudflare.com/tag/infrastructure-as-code/)
  * [Insights](https://blog.cloudflare.com/tag/insights/)
  * [Intel](https://blog.cloudflare.com/tag/intel/)
  * [Interconnection](https://blog.cloudflare.com/tag/interconnection/)
  * [Internal DNS](https://blog.cloudflare.com/tag/internal-dns/)
  * [Internet Performance](https://blog.cloudflare.com/tag/internet-performance/)
  * [Internet Quality](https://blog.cloudflare.com/tag/internet-quality/)
  * [Internet Regulation](https://blog.cloudflare.com/tag/internet-regulation/)
  * [Internet Shutdown](https://blog.cloudflare.com/tag/internet-shutdown/)
  * [Internet Summit](https://blog.cloudflare.com/tag/internet-summit/)
  * [Internet Traffic](https://blog.cloudflare.com/tag/internet-traffic/)
  * [Internet Trends](https://blog.cloudflare.com/tag/internet-trends/)
  * [Internship Experience](https://blog.cloudflare.com/tag/internship-experience/)
  * [Intrusion Detection](https://blog.cloudflare.com/tag/intrusion-detection/)
  * [Investors](https://blog.cloudflare.com/tag/investors/)
  * [IoCs](https://blog.cloudflare.com/tag/iocs/)
  * [iOS](https://blog.cloudflare.com/tag/ios/)
  * [IoT](https://blog.cloudflare.com/tag/iot/)
  * [IPFS](https://blog.cloudflare.com/tag/ipfs/)
  * [IPsec](https://blog.cloudflare.com/tag/ipsec/)
  * [IPv4](https://blog.cloudflare.com/tag/ipv4/)
  * [IPv6](https://blog.cloudflare.com/tag/ipv6/)
  * [IRAP](https://blog.cloudflare.com/tag/irap/)
  * [Israel](https://blog.cloudflare.com/tag/israel/)
  * [Italy](https://blog.cloudflare.com/tag/italy/)
  * [IWD](https://blog.cloudflare.com/tag/iwd/)
  * [JAMstack](https://blog.cloudflare.com/tag/jamstack/)
  * [Japan](https://blog.cloudflare.com/tag/japan/)
  * [JavaScript](https://blog.cloudflare.com/tag/javascript/)
  * [Jengo](https://blog.cloudflare.com/tag/jengo/)
  * [Jengo Policy](https://blog.cloudflare.com/tag/jengo-policy/)
  * [Joomla](https://blog.cloudflare.com/tag/joomla/)
  * [Judeoflare](https://blog.cloudflare.com/tag/judeoflare/)
  * [Kafka](https://blog.cloudflare.com/tag/kafka/)
  * [Kernel](https://blog.cloudflare.com/tag/kernel/)
  * [Key Value](https://blog.cloudflare.com/tag/key-value/)
  * [Keyless SSL](https://blog.cloudflare.com/tag/keyless-ssl/)
  * [KeyTrap](https://blog.cloudflare.com/tag/keytrap/)
  * [Killnet](https://blog.cloudflare.com/tag/killnet/)
  * [Korea](https://blog.cloudflare.com/tag/korea/)
  * [Kubernetes](https://blog.cloudflare.com/tag/kubernetes/)
  * [LangChain](https://blog.cloudflare.com/tag/langchain/)
  * [Latency](https://blog.cloudflare.com/tag/latency/)
  * [Latin America](https://blog.cloudflare.com/tag/latin-america/)
  * [Latinflare](https://blog.cloudflare.com/tag/latinflare/)
  * [LavaRand](https://blog.cloudflare.com/tag/lavarand/)
  * [Lazarus group](https://blog.cloudflare.com/tag/lazarus-group/)
  * [Leaked Credential Checks](https://blog.cloudflare.com/tag/leaked-credential-checks/)
  * [Legal](https://blog.cloudflare.com/tag/legal/)
  * [Legal Patents Sable](https://blog.cloudflare.com/tag/legal-patents-sable/)
  * [LGBTQIA+](https://blog.cloudflare.com/tag/lgbtqia/)
  * [Life at Cloudflare](https://blog.cloudflare.com/tag/life-at-cloudflare/)
  * [Linux](https://blog.cloudflare.com/tag/linux/)
  * [Lisbon](https://blog.cloudflare.com/tag/lisbon/)
  * [Live Streaming](https://blog.cloudflare.com/tag/live-streaming/)
  * [Llama](https://blog.cloudflare.com/tag/llama/)
  * [LLM](https://blog.cloudflare.com/tag/llm/)
  * [Load Balancing](https://blog.cloudflare.com/tag/loadbalancing/)
  * [Localization](https://blog.cloudflare.com/tag/localization/)
  * [Log Push](https://blog.cloudflare.com/tag/log-push/)
  * [Log4J](https://blog.cloudflare.com/tag/log4j/)
  * [Log4Shell](https://blog.cloudflare.com/tag/log4shell/)
  * [Logging](https://blog.cloudflare.com/tag/logging/)
  * [Logs](https://blog.cloudflare.com/tag/logs/)
  * [LUA](https://blog.cloudflare.com/tag/lua/)
  * [Machine Learning](https://blog.cloudflare.com/tag/machine-learning/)
  * [Magecart](https://blog.cloudflare.com/tag/magecart/)
  * [Magic Firewall](https://blog.cloudflare.com/tag/magic-firewall/)
  * [Magic Network Monitoring](https://blog.cloudflare.com/tag/magic-network-monitoring/)
  * [Magic Transit](https://blog.cloudflare.com/tag/magic-transit/)
  * [Magic WAN](https://blog.cloudflare.com/tag/magic-wan/)
  * [Magic WAN Connector](https://blog.cloudflare.com/tag/magic-wan-connector/)
  * [Malicious JavaScript](https://blog.cloudflare.com/tag/malicious-javascript/)
  * [Malware](https://blog.cloudflare.com/tag/malware/)
  * [Managed Components](https://blog.cloudflare.com/tag/managed-components/)
  * [Managed Rules](https://blog.cloudflare.com/tag/managed-rules/)
  * [March of Cloudflare](https://blog.cloudflare.com/tag/march-of-cloudflare/)
  * [MASQUE](https://blog.cloudflare.com/tag/masque/)
  * [MCP](https://blog.cloudflare.com/tag/mcp/)
  * [Meerkat](https://blog.cloudflare.com/tag/meerkat/)
  * [MeetUp](https://blog.cloudflare.com/tag/meetup/)
  * [Meris](https://blog.cloudflare.com/tag/meris/)
  * [Message Protocol](https://blog.cloudflare.com/tag/message-protocol/)
  * [Mexico](https://blog.cloudflare.com/tag/mexico/)
  * [Micro-frontends](https://blog.cloudflare.com/tag/micro-frontends/)
  * [Microsoft](https://blog.cloudflare.com/tag/microsoft/)
  * [Microsoft 365](https://blog.cloudflare.com/tag/microsoft-365/)
  * [Microsoft Azure](https://blog.cloudflare.com/tag/microsoft-azure/)
  * [Middle East](https://blog.cloudflare.com/tag/middle-east/)
  * [Migration Hub](https://blog.cloudflare.com/tag/migration-hub/)
  * [Milestones](https://blog.cloudflare.com/tag/milestone/)
  * [Miniflare](https://blog.cloudflare.com/tag/miniflare/)
  * [Mirage](https://blog.cloudflare.com/tag/mirage/)
  * [Mirai](https://blog.cloudflare.com/tag/mirai/)
  * [Mitel](https://blog.cloudflare.com/tag/mitel/)
  * [Mitigation](https://blog.cloudflare.com/tag/mitigation/)
  * [Mixed Content Errors](https://blog.cloudflare.com/tag/mixed-content-errors/)
  * [MLops](https://blog.cloudflare.com/tag/mlops/)
  * [Mobile](https://blog.cloudflare.com/tag/mobile/)
  * [Mobile SDK](https://blog.cloudflare.com/tag/mobile-sdk/)
  * [Model Context Protocol](https://blog.cloudflare.com/tag/model-context-protocol/)
  * [Moldova](https://blog.cloudflare.com/tag/moldova/)
  * [Monitoring](https://blog.cloudflare.com/tag/monitoring/)
  * [Multi-Cloud](https://blog.cloudflare.com/tag/multi-cloud/)
  * [Multi-User](https://blog.cloudflare.com/tag/multi-user/)
  * [MySQL](https://blog.cloudflare.com/tag/mysql/)
  * [NaaS](https://blog.cloudflare.com/tag/naas/)
  * [Net Neutrality](https://blog.cloudflare.com/tag/net-neutrality/)
  * [Network](https://blog.cloudflare.com/tag/network/)
  * [Network Interconnect](https://blog.cloudflare.com/tag/network-interconnect/)
  * [Network Performance Update](https://blog.cloudflare.com/tag/network-performance-update/)
  * [Network Protection](https://blog.cloudflare.com/tag/network-protection/)
  * [Network Services](https://blog.cloudflare.com/tag/network-services/)
  * [Networking](https://blog.cloudflare.com/tag/networking/)
  * [New Year](https://blog.cloudflare.com/tag/new-year/)
  * [NGINX](https://blog.cloudflare.com/tag/nginx/)
  * [Ninjas](https://blog.cloudflare.com/tag/ninjas/)
  * [NIST](https://blog.cloudflare.com/tag/nist/)
  * [Node.js](https://blog.cloudflare.com/tag/node-js/)
  * [North America](https://blog.cloudflare.com/tag/north-america/)
  * [Notebooks](https://blog.cloudflare.com/tag/notebooks/)
  * [Notifications](https://blog.cloudflare.com/tag/notifications/)
  * [NSEC3](https://blog.cloudflare.com/tag/nsec3/)
  * [OAuth](https://blog.cloudflare.com/tag/oauth/)
  * [Observability](https://blog.cloudflare.com/tag/observability/)
  * [Oceania](https://blog.cloudflare.com/tag/oceania/)
  * [OCSP](https://blog.cloudflare.com/tag/ocsp/)
  * [Offices](https://blog.cloudflare.com/tag/offices/)
  * [Okta](https://blog.cloudflare.com/tag/okta/)
  * [Olympics](https://blog.cloudflare.com/tag/olympics/)
  * [Onboarding](https://blog.cloudflare.com/tag/onboarding/)
  * [Open API](https://blog.cloudflare.com/tag/open-api/)
  * [Open Source](https://blog.cloudflare.com/tag/open-source/)
  * [OpenAI](https://blog.cloudflare.com/tag/openai/)
  * [OpenBMC](https://blog.cloudflare.com/tag/open-bmc/)
  * [OpenDNS](https://blog.cloudflare.com/tag/opendns/)
  * [OpenSSL](https://blog.cloudflare.com/tag/openssl/)
  * [OpenTelemetry ](https://blog.cloudflare.com/tag/opentelemetry/)
  * [Optimization](https://blog.cloudflare.com/tag/optimization/)
  * [Origin Rules](https://blog.cloudflare.com/tag/origin-rules/)
  * [Outage](https://blog.cloudflare.com/tag/outage/)
  * [Oxy](https://blog.cloudflare.com/tag/oxy/)
  * [Pacific Northwest](https://blog.cloudflare.com/tag/pacific-northwest/)
  * [Page Rules](https://blog.cloudflare.com/tag/page-rules/)
  * [Page Shield](https://blog.cloudflare.com/tag/page-shield/)
  * [Parallels](https://blog.cloudflare.com/tag/parallels/)
  * [Partners](https://blog.cloudflare.com/tag/partners/)
  * [Partnership](https://blog.cloudflare.com/tag/partnerships/)
  * [Password-reuse](https://blog.cloudflare.com/tag/password-reuse/)
  * [Passwords](https://blog.cloudflare.com/tag/passwords/)
  * [Passwords (PT)](https://blog.cloudflare.com/tag/passwords-pt/)
  * [Patents](https://blog.cloudflare.com/tag/patents/)
  * [Pay Per Crawl](https://blog.cloudflare.com/tag/pay-per-crawl/)
  * [PAYGO](https://blog.cloudflare.com/tag/paygo/)
  * [Payments](https://blog.cloudflare.com/tag/payments/)
  * [PCI Certified](https://blog.cloudflare.com/tag/pci-certified/)
  * [Peering](https://blog.cloudflare.com/tag/peering/)
  * [Performance](https://blog.cloudflare.com/tag/performance/)
  * [Performance Optimization](https://blog.cloudflare.com/tag/performance-optimization/)
  * [Phishing](https://blog.cloudflare.com/tag/phishing/)
  * [php](https://blog.cloudflare.com/tag/php/)
  * [Phython](https://blog.cloudflare.com/tag/phython/)
  * [Pingora](https://blog.cloudflare.com/tag/pingora/)
  * [Pipelines](https://blog.cloudflare.com/tag/pipelines/)
  * [PlanetScale](https://blog.cloudflare.com/tag/planetscale/)
  * [Plans](https://blog.cloudflare.com/tag/plans/)
  * [Platform Engineering](https://blog.cloudflare.com/tag/platform-engineering/)
  * [Platform Week](https://blog.cloudflare.com/tag/platform-week/)
  * [Plesk](https://blog.cloudflare.com/tag/plesk/)
  * [Policy & Legal](https://blog.cloudflare.com/tag/policy/)
  * [Politics](https://blog.cloudflare.com/tag/politics/)
  * [Portugal](https://blog.cloudflare.com/tag/portugal/)
  * [Post Mortem](https://blog.cloudflare.com/tag/post-mortem/)
  * [Post-Quantum](https://blog.cloudflare.com/tag/post-quantum/)
  * [Postgres](https://blog.cloudflare.com/tag/postgres/)
  * [Precursor](https://blog.cloudflare.com/tag/precursor/)
  * [Prepared Statements](https://blog.cloudflare.com/tag/prepared-statements/)
  * [Prisma](https://blog.cloudflare.com/tag/prisma/)
  * [Privacy](https://blog.cloudflare.com/tag/privacy/)
  * [Privacy Pass](https://blog.cloudflare.com/tag/privacy-pass/)
  * [Privacy Week](https://blog.cloudflare.com/tag/privacy-week/)
  * [Private IP](https://blog.cloudflare.com/tag/private-ip/)
  * [Private Network](https://blog.cloudflare.com/tag/private-network/)
  * [Product Design](https://blog.cloudflare.com/tag/product-design/)
  * [Product News](https://blog.cloudflare.com/tag/product-news/)
  * [Programming](https://blog.cloudflare.com/tag/programming/)
  * [Programming (PT)](https://blog.cloudflare.com/tag/programming-pt/)
  * [Project Fair Shot](https://blog.cloudflare.com/tag/project-fair-shot/)
  * [Project Galileo](https://blog.cloudflare.com/tag/project-galileo/)
  * [Project Honey Pot](https://blog.cloudflare.com/tag/project-honey-pot/)
  * [Project Pangea](https://blog.cloudflare.com/tag/project-pangea/)
  * [Project Safekeeping](https://blog.cloudflare.com/tag/project-safekeeping/)
  * [Project Turpentine](https://blog.cloudflare.com/tag/project-turpentine/)
  * [Prometheus](https://blog.cloudflare.com/tag/prometheus/)
  * [Protocols](https://blog.cloudflare.com/tag/protocols/)
  * [Proudflare](https://blog.cloudflare.com/tag/proudflare/)
  * [Proxying](https://blog.cloudflare.com/tag/proxying/)
  * [Public Sector](https://blog.cloudflare.com/tag/public-sector/)
  * [Python](https://blog.cloudflare.com/tag/python/)
  * [Python Workers](https://blog.cloudflare.com/tag/python-workers/)
  * [Quantization](https://blog.cloudflare.com/tag/quantization/)
  * [Queues](https://blog.cloudflare.com/tag/queues/)
  * [QUIC](https://blog.cloudflare.com/tag/quic/)
  * [QUICHE](https://blog.cloudflare.com/tag/quiche/)
  * [Quicksilver](https://blog.cloudflare.com/tag/quicksilver/)
  * [R2](https://blog.cloudflare.com/tag/r2/)
  * [R2 Super Slurper](https://blog.cloudflare.com/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/tag/cloudflare-radar/)
  * [Radar Alerts](https://blog.cloudflare.com/tag/radar-alerts/)
  * [Radar API](https://blog.cloudflare.com/tag/radar-api/)
  * [Radar Maps](https://blog.cloudflare.com/tag/radar-maps/)
  * [Railgun](https://blog.cloudflare.com/tag/railgun/)
  * [Randomness](https://blog.cloudflare.com/tag/randomness/)
  * [Ransom Attacks](https://blog.cloudflare.com/tag/ransom-attacks/)
  * [Rapid Reset](https://blog.cloudflare.com/tag/rapid-reset/)
  * [Raspberry Pi](https://blog.cloudflare.com/tag/raspberry-pi/)
  * [Rate Limiting](https://blog.cloudflare.com/tag/rate-limiting/)
  * [RC4](https://blog.cloudflare.com/tag/rc4/)
  * [RDDoS](https://blog.cloudflare.com/tag/rddos/)
  * [React](https://blog.cloudflare.com/tag/react/)
  * [Reading List](https://blog.cloudflare.com/tag/reading-list/)
  * [Real-time](https://blog.cloudflare.com/tag/real-time/)
  * [Recruiting](https://blog.cloudflare.com/tag/recruiting/)
  * [Regional Services](https://blog.cloudflare.com/tag/regional-services/)
  * [Registrar](https://blog.cloudflare.com/tag/registrar/)
  * [Reliability](https://blog.cloudflare.com/tag/reliability/)
  * [Remote Browser Isolation](https://blog.cloudflare.com/tag/remote-browser-isolation/)
  * [Remote Desktop Protocol ](https://blog.cloudflare.com/tag/remote-desktop-protocol/)
  * [Remote Work](https://blog.cloudflare.com/tag/remote-work/)
  * [Replication](https://blog.cloudflare.com/tag/replication/)
  * [Research](https://blog.cloudflare.com/tag/research/)
  * [Resolver](https://blog.cloudflare.com/tag/resolver/)
  * [Restreaming](https://blog.cloudflare.com/tag/restreaming/)
  * [Retreat](https://blog.cloudflare.com/tag/retreat/)
  * [Reverse Engineering](https://blog.cloudflare.com/tag/reverse-engineering/)
  * [REvil](https://blog.cloudflare.com/tag/revil/)
  * [Risk Management](https://blog.cloudflare.com/tag/risk-management/)
  * [Road to Zero Trust](https://blog.cloudflare.com/tag/road-to-zero-trust/)
  * [Rocket Loader](https://blog.cloudflare.com/tag/rocketloader/)
  * [RocksDB](https://blog.cloudflare.com/tag/rocksdb/)
  * [Routing](https://blog.cloudflare.com/tag/routing/)
  * [Routing Security](https://blog.cloudflare.com/tag/routing-security/)
  * [RPC](https://blog.cloudflare.com/tag/rpc/)
  * [RPKI](https://blog.cloudflare.com/tag/rpki/)
  * [RRDNS](https://blog.cloudflare.com/tag/rrdns/)
  * [RSA](https://blog.cloudflare.com/tag/rsa/)
  * [Russia](https://blog.cloudflare.com/tag/russia/)
  * [Rust](https://blog.cloudflare.com/tag/rust/)
  * [Rust Workers](https://blog.cloudflare.com/tag/rust-workers/)
  * [SaaS](https://blog.cloudflare.com/tag/saas/)
  * [SAAS Security](https://blog.cloudflare.com/tag/saas-security/)
  * [Sable](https://blog.cloudflare.com/tag/sable/)
  * [Salt](https://blog.cloudflare.com/tag/salt/)
  * [Sampling](https://blog.cloudflare.com/tag/sampling/)
  * [Sandbox](https://blog.cloudflare.com/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/tag/sase/)
  * [Save The Web](https://blog.cloudflare.com/tag/savetheweb/)
  * [SDK](https://blog.cloudflare.com/tag/sdk/)
  * [Search Engine](https://blog.cloudflare.com/tag/search-engine/)
  * [Secrets Store](https://blog.cloudflare.com/tag/secrets-store/)
  * [Secure Web Gateway](https://blog.cloudflare.com/tag/secure-web-gateway/)
  * [Security](https://blog.cloudflare.com/tag/security/)
  * [Security Analytics](https://blog.cloudflare.com/tag/security-analytics/)
  * [Security Center](https://blog.cloudflare.com/tag/security-center/)
  * [Security Posture](https://blog.cloudflare.com/tag/security-posture/)
  * [Security Posture Management](https://blog.cloudflare.com/tag/security-posture-management/)
  * [Security Service Edge](https://blog.cloudflare.com/tag/security-service-edge/)
  * [Security Week](https://blog.cloudflare.com/tag/security-week/)
  * [security.txt](https://blog.cloudflare.com/tag/security-txt/)
  * [SEO](https://blog.cloudflare.com/tag/seo/)
  * [Server Push](https://blog.cloudflare.com/tag/server-push/)
  * [Serverless](https://blog.cloudflare.com/tag/serverless/)
  * [Serverless (PT)](https://blog.cloudflare.com/tag/serverless-pt/)
  * [Serverless AI](https://blog.cloudflare.com/tag/serverless-ai/)
  * [Serverless Week](https://blog.cloudflare.com/tag/serverless-week/)
  * [Servers](https://blog.cloudflare.com/tag/servers/)
  * [SIEM](https://blog.cloudflare.com/tag/siem/)
  * [Signed Exchanges (SXG)](https://blog.cloudflare.com/tag/signed-exchanges/)
  * [SIM](https://blog.cloudflare.com/tag/sim/)
  * [Singapore](https://blog.cloudflare.com/tag/singapore/)
  * [Single Sign On (SSO)](https://blog.cloudflare.com/tag/sso/)
  * [Smart Placement](https://blog.cloudflare.com/tag/smart-placement/)
  * [Smart Shield](https://blog.cloudflare.com/tag/smart-shield/)
  * [Snippets](https://blog.cloudflare.com/tag/snippets/)
  * [SOC as a Service](https://blog.cloudflare.com/tag/soc-as-a-service/)
  * [South Africa](https://blog.cloudflare.com/tag/south-africa/)
  * [South America](https://blog.cloudflare.com/tag/south-america/)
  * [Spain](https://blog.cloudflare.com/tag/spain/)
  * [spdy](https://blog.cloudflare.com/tag/spdy/)
  * [Spectrum](https://blog.cloudflare.com/tag/spectrum/)
  * [Speed](https://blog.cloudflare.com/tag/speed/)
  * [Speed & Reliability](https://blog.cloudflare.com/tag/speed-and-reliability/)
  * [Speed Brain](https://blog.cloudflare.com/tag/speed-brain/)
  * [Speed Week](https://blog.cloudflare.com/tag/speed-week/)
  * [Spoofing](https://blog.cloudflare.com/tag/spoofing/)
  * [Sports](https://blog.cloudflare.com/tag/sports/)
  * [SQL](https://blog.cloudflare.com/tag/sql/)
  * [SRE](https://blog.cloudflare.com/tag/sre/)
  * [SSE](https://blog.cloudflare.com/tag/sse/)
  * [SSH](https://blog.cloudflare.com/tag/ssh/)
  * [SSL](https://blog.cloudflare.com/tag/ssl/)
  * [Standards](https://blog.cloudflare.com/tag/standards/)
  * [Startup Enterprise Plan](https://blog.cloudflare.com/tag/startup-enterprise-plan/)
  * [Statistics](https://blog.cloudflare.com/tag/statistics/)
  * [StopTheHacker](https://blog.cloudflare.com/tag/stopthehacker/)
  * [Storage](https://blog.cloudflare.com/tag/storage/)
  * [Sumo Logic](https://blog.cloudflare.com/tag/sumo-logic/)
  * [Super Bowl](https://blog.cloudflare.com/tag/super-bowl/)
  * [Supercloud](https://blog.cloudflare.com/tag/supercloud/)
  * [Supply Chain Attacks](https://blog.cloudflare.com/tag/supply-chain-attacks/)
  * [Support](https://blog.cloudflare.com/tag/support/)
  * [Sustainability](https://blog.cloudflare.com/tag/sustainability/)
  * [SWAG](https://blog.cloudflare.com/tag/swag/)
  * [SWG](https://blog.cloudflare.com/tag/swg/)
  * [Swift](https://blog.cloudflare.com/tag/swift/)
  * [Switzerland](https://blog.cloudflare.com/tag/switzerland/)
  * [SXSW](https://blog.cloudflare.com/tag/sxsw/)
  * [SYN](https://blog.cloudflare.com/tag/syn/)
  * [SYN Flood](https://blog.cloudflare.com/tag/syn-flood/)
  * [Syria](https://blog.cloudflare.com/tag/syria/)
  * [TCP](https://blog.cloudflare.com/tag/tcp/)
  * [Team](https://blog.cloudflare.com/tag/team/)
  * [Teams Dashboard](https://blog.cloudflare.com/tag/teams-dashboard/)
  * [Tech Talks](https://blog.cloudflare.com/tag/tech-talks/)
  * [TechCrunch](https://blog.cloudflare.com/tag/techcrunch/)
  * [Technical Writing](https://blog.cloudflare.com/tag/technical-writing/)
  * [Terraform](https://blog.cloudflare.com/tag/terraform/)
  * [Testimonials](https://blog.cloudflare.com/tag/testimonials/)
  * [Testing](https://blog.cloudflare.com/tag/testing/)
  * [Texas](https://blog.cloudflare.com/tag/texas/)
  * [Thanksgiving](https://blog.cloudflare.com/tag/thanksgiving/)
  * [The Serverlist Newsletter](https://blog.cloudflare.com/tag/serverlist/)
  * [Threat Data](https://blog.cloudflare.com/tag/threat-data/)
  * [Threat Feeds](https://blog.cloudflare.com/tag/threat-feeds/)
  * [Threat Intelligence](https://blog.cloudflare.com/tag/threat-intelligence/)
  * [Threat Operations](https://blog.cloudflare.com/tag/threat-operations/)
  * [Threat Report](https://blog.cloudflare.com/tag/threat-report/)
  * [Threats](https://blog.cloudflare.com/tag/threats/)
  * [Tiered Cache](https://blog.cloudflare.com/tag/tiered-cache/)
  * [TikTok](https://blog.cloudflare.com/tag/tiktok/)
  * [TLS](https://blog.cloudflare.com/tag/tls/)
  * [TLS 1.3](https://blog.cloudflare.com/tag/tls-1-3/)
  * [Tools](https://blog.cloudflare.com/tag/tools/)
  * [Tor](https://blog.cloudflare.com/tag/tor/)
  * [Tracing](https://blog.cloudflare.com/tag/tracing/)
  * [Traffic](https://blog.cloudflare.com/tag/traffic/)
  * [Transform Rules](https://blog.cloudflare.com/tag/transform-rules/)
  * [Transparency](https://blog.cloudflare.com/tag/transparency/)
  * [Trends](https://blog.cloudflare.com/tag/trends/)
  * [Trust & Safety](https://blog.cloudflare.com/tag/trust-and-safety/)
  * [TTFB](https://blog.cloudflare.com/tag/ttfb/)
  * [TTL](https://blog.cloudflare.com/tag/ttl/)
  * [TURN](https://blog.cloudflare.com/tag/turn/)
  * [TURN Server](https://blog.cloudflare.com/tag/turn-server/)
  * [Turnstile](https://blog.cloudflare.com/tag/turnstile/)
  * [TypeScript](https://blog.cloudflare.com/tag/typescript/)
  * [UDP](https://blog.cloudflare.com/tag/udp/)
  * [Ukraine](https://blog.cloudflare.com/tag/ukraine/)
  * [United Kingdom](https://blog.cloudflare.com/tag/united-kingdom/)
  * [Universal SSL](https://blog.cloudflare.com/tag/universal-ssl/)
  * [URL Scanner](https://blog.cloudflare.com/tag/url-scanner/)
  * [USA](https://blog.cloudflare.com/tag/usa/)
  * [User Research](https://blog.cloudflare.com/tag/user-research/)
  * [VDI](https://blog.cloudflare.com/tag/vdi/)
  * [Vectorize](https://blog.cloudflare.com/tag/vectorize/)
  * [Vetflare](https://blog.cloudflare.com/tag/vetflare/)
  * [Video](https://blog.cloudflare.com/tag/video/)
  * [Visibility](https://blog.cloudflare.com/tag/visibility/)
  * [Vite](https://blog.cloudflare.com/tag/vite/)
  * [VoIP](https://blog.cloudflare.com/tag/voip/)
  * [VPC](https://blog.cloudflare.com/tag/vpc/)
  * [VPN](https://blog.cloudflare.com/tag/vpn/)
  * [Vulnerabilities](https://blog.cloudflare.com/tag/vulnerabilities/)
  * [WAF](https://blog.cloudflare.com/tag/waf/)
  * [WAF Attack Score](https://blog.cloudflare.com/tag/waf-attack-score/)
  * [WAF Rules](https://blog.cloudflare.com/tag/waf-rules/)
  * [Waiting Room](https://blog.cloudflare.com/tag/waiting-room/)
  * [WARP](https://blog.cloudflare.com/tag/warp/)
  * [WARP Connector](https://blog.cloudflare.com/tag/warp-connector/)
  * [WASM](https://blog.cloudflare.com/tag/wasm/)
  * [Web Application Firewall](https://blog.cloudflare.com/tag/web-application-firewall/)
  * [Web Asset Discovery](https://blog.cloudflare.com/tag/web-asset-discovery/)
  * [Web3](https://blog.cloudflare.com/tag/web3/)
  * [WebAssembly](https://blog.cloudflare.com/tag/webassembly/)
  * [Webinars](https://blog.cloudflare.com/tag/webinars/)
  * [WebMCP](https://blog.cloudflare.com/tag/webmcp/)
  * [WebP](https://blog.cloudflare.com/tag/webp/)
  * [WebRTC](https://blog.cloudflare.com/tag/webrtc/)
  * [WebSockets](https://blog.cloudflare.com/tag/websockets/)
  * [Wildebeest](https://blog.cloudflare.com/tag/wildebeest/)
  * [Womenflare](https://blog.cloudflare.com/tag/womenflare/)
  * [WordPress](https://blog.cloudflare.com/tag/wordpress/)
  * [Workers AI](https://blog.cloudflare.com/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/tag/workers-launchpad/)
  * [Workers Logs](https://blog.cloudflare.com/tag/workers-logs/)
  * [Workers Observability](https://blog.cloudflare.com/tag/workers-observability/)
  * [Workers Sites](https://blog.cloudflare.com/tag/workers-sites/)
  * [Workers Unbound](https://blog.cloudflare.com/tag/workers-unbound/)
  * [Workers VPC](https://blog.cloudflare.com/tag/workers-vpc/)
  * [Workflows](https://blog.cloudflare.com/tag/workflows/)
  * [World IPv6 Day](https://blog.cloudflare.com/tag/world-ipv6-day/)
  * [Wrangler](https://blog.cloudflare.com/tag/wrangler/)
  * [x402](https://blog.cloudflare.com/tag/x402/)
  * [Year in Review](https://blog.cloudflare.com/tag/year-in-review/)
  * [Z3](https://blog.cloudflare.com/tag/z3/)
  * [Zaraz](https://blog.cloudflare.com/tag/zaraz/)
  * [Zero Day Threats](https://blog.cloudflare.com/tag/zero-day-threats/)
  * [Zero Trust](https://blog.cloudflare.com/tag/zero-trust/)
  * [Zero Trust Week](https://blog.cloudflare.com/tag/zero-trust-week/)
  * [Zone Versioning](https://blog.cloudflare.com/tag/zone-versioning/)
  * [Artificial Intelligence](https://blog.cloudflare.com/tag/artificial-intelligence/)
  * [Workers](https://blog.cloudflare.com/tag/workers-1/)
  * [Client-Side Security](https://blog.cloudflare.com/tag/client-side-security/)
  * [Architecture](https://blog.cloudflare.com/tag/architecture/)
  * [Multi-tenant Secuity](https://blog.cloudflare.com/tag/multi-tenant-secuity/)
  * [Multi-tenant Security](https://blog.cloudflare.com/tag/multi-tenant-security/)
  * [cf](https://blog.cloudflare.com/tag/cf/)
  * [BEACON](https://blog.cloudflare.com/tag/beacon/)



[Networking](https://blog.cloudflare.com/tag/networking/)[QUIC](https://blog.cloudflare.com/tag/quic/)[QUICHE](https://blog.cloudflare.com/tag/quiche/)[Rust](https://blog.cloudflare.com/tag/rust/)

[Congestion Control](https://blog.cloudflare.com/tag/congestion-control/)[Debugging](https://blog.cloudflare.com/tag/debugging/)[HTTP3](https://blog.cloudflare.com/tag/http3/)[Networking](https://blog.cloudflare.com/tag/networking/)[QUIC](https://blog.cloudflare.com/tag/quic/)[QUICHE](https://blog.cloudflare.com/tag/quiche/)[Rust](https://blog.cloudflare.com/tag/rust/)

May 12, 2026

# When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug

![Esteban Carisimo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VSSKPEBK3K5ND6JZ67YP.webp&w=64&h=64&f=webp&fit=cover&position=center)![Antonio Vicente](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487NFE7AY4B70WNGYX9WZ9.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Esteban Carisimo](https://blog.cloudflare.com/author/esteban-carisimo/) and [Antonio Vicente](https://blog.cloudflare.com/author/antonio-vicente/)

13 minute read

COPY URL

This post is also available in [日本語](https://blog.cloudflare.com/ja-jp/quic-death-spiral-fix/) and [한국어](https://blog.cloudflare.com/ko-kr/quic-death-spiral-fix/).

![BLOG-3260 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VSCEX3RARQSM9H9JQNVR.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////787/Hy5enu6uzy8vL28/Ly7Ozp////////7PH14Ojx5Ov17/L58fP16+3s////////6/L53Oj14Ov57fP98fT57PDw////////7fb+3ev54e397vX/8/f+7/P0////////9Pv/5fD+6PL/9Pn/+Pv/8/f5/////////P//8Pb/8/f/+/7//v//+fv9////////////+fv/+/z//////////f7//////////////f3///7//////////v//)

CUBIC, standardized in [_RFC 9438_](https://www.rfc-editor.org/rfc/rfc9438.html), is the default congestion controller in Linux, and as a result governs how most TCP and QUIC connections on the public Internet probe for available bandwidth, back off when they detect loss, and recover afterward. At Cloudflare, our open-source implementation of QUIC,[ _quiche_](https://github.com/cloudflare/quiche), uses CUBIC as its default congestion controller, meaning this code is in the critical path for a significant share of the traffic we serve.

In this post, we’ll tell the story of a bug in which CUBIC's congestion window (cwnd) gets permanently pinned at its minimum and never recovers from a congestion collapse event.

The story starts with a [_Linux kernel change_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) aimed at bringing CUBIC into line with the app-limited exclusion described in [_RFC 9438 §4.2-12_](https://www.rfc-editor.org/rfc/rfc9438.html#section-4.2-12) — a fix to a real problem in TCP that, when ported to our QUIC implementation, surfaced unexpected behaviors in quiche. It has a happy ending: an elegant (near-)one-line fix that broke the cycle.

## CUBIC's logic in a nutshell

Before we dive into the core problem, a quick refresher on Congestion Control Algorithms (CCAs) may help to set the stage.

The central knob a CCA turns is the **congestion window** (`cwnd`): the sender-side cap on how many bytes can be in flight (sent but not yet acknowledged) at any moment. A larger `cwnd` lets the sender push more data per round trip; a smaller `cwnd` throttles it. Every loss-based CCA, CUBIC included, is ultimately a policy for how to grow `cwnd` when the network looks healthy and how to shrink it when it doesn't.

In essence, CCAs aim to maximize data transfer by inferring the "available bandwidth" of the network; because no one wants to pay for a 1 Gbps subscription and only use a fraction of it. The family of loss-based algorithms, to which CUBIC belongs, operate on a fundamental premise: (1) if there is no packet loss, increase the sending rate (i.e. increase the bandwidth utilization); (2) if there is loss, loss-based algorithms assume that the network's capacity has been exceeded, and the sender must back off (i.e. decrease the bandwidth utilization).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45F1EAW72WCHZ78GX5HT44.png&w=715&h=310&f=webp&fit=cover&position=center)

This logic is built on several assumptions that have been revisited over the years. However, we'll save that discussion for another time.

## The symptom: a test that fails 61% of the time

Our investigation started with the report of unexpected failures in our ingress proxy integration test pipeline. This erratic behavior appeared in tests where CUBIC was evaluated in a scenario of heavy loss in the early part of the connection. 

Recovery after congestion collapse is an uncommon regime, but it is exactly the regime a congestion controller exists to handle. Most congestion control tests exercise the steady-state and growth phases of an algorithm; far fewer probe what happens at minimum cwnd, after the connection has been beaten down. Bugs in this corner of the state space are invisible in throughput dashboards, undetectable by static review, and only surface when you deliberately drive a CCA into it and watch whether it can climb back out — which is exactly what this test did.

The simulated test setup includes the following details:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47XTRR7C32QNFXD4R2P2QP.png&w=715&h=224&f=webp&fit=cover&position=center)

  * Quiche HTTP/3 client and server running at locally (localhost)
  * RTT = 10ms (set up in the configuration)
  * A 10 MB file download over HTTP/3
  * Using CUBIC congestion control
  * With 30% random packet loss injected during the first two seconds
  * After two seconds, loss stops entirely
  * The test has a generous 10-second timeout to complete the download, which is expected to be completed in four or five seconds



The expected behavior is straightforward: CUBIC should take some hits during the loss phase, reduce its congestion window, and once loss stops, steadily ramp up and finish the download well within the timeout. Instead, we observed in multiple 100-time runs that around 60% of our tests were not able to complete the download within the generous 10-second timeout.

## The anomaly: 999 state transitions with zero loss

We instrumented[ _quiche's qlog_](https://github.com/cloudflare/quiche) output with packet loss events and built visualizations to understand what was happening inside the congestion controller:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FRE5WJ50JFBR32K8E6Y2.png&w=715&h=459&f=webp&fit=cover&position=center)

_Connection overview of a failing test. After T=2s, packet loss stops entirely — yet cwnd remains pinned at the minimum floor and the congestion state oscillates between recovery and congestion avoidance every ~14ms._

After the two-second (2000 ms) mark, packet loss stops entirely. However, the number of bytes in flight remains flat, which contradicts the core logic of the CUBIC algorithm: in the absence of loss, apply more gas to increase throttle (more bytes in our world). _This raises the question: if the network is no longer dropping packets, why is the congestion window failing to grow?_

When we zoom into that region, our analysis shows that CUBIC enters a rapid oscillation, shown in our plot as an extended recovery phase, between congestion avoidance state (the operational regime phase) and recovery state (the packet loss recovery state) — 999 transitions in approximately 6.7 seconds. That’s one transition every ~14ms — suspiciously close to the connection's RTT (10ms). Throughout this entire period, cwnd is locked at the minimum floor: 2700 bytes, or two full-size packets.

Clearly something in CUBIC's logic is misinterpreting the state of the connection. The key clue is the oscillation period: ~14ms matches the RTT. Whatever is triggering the recovery/avoidance flip is happening once per round trip, in lockstep with connection's ACK clock; the self-clocking rhythm in which each round-trip's ACKs from the client trigger the server's next send. Because this is a download (server to client), the ACKs in question travel client to server, and CUBIC's state machine runs on the server side: every time those ACKs land, bytes_in_flight drops to zero and the server sends the next two-packet burst, which is what triggers the bug.

To confirm this behavior was CUBIC-specific, we ran the same test with [_Reno_](https://dl.acm.org/doi/10.1145/235160.235162), another member of the loss-based family but with a different growth rate. The results were conclusive: 100% pass rate, showing Reno recovered cleanly after the loss phase, and revealing that this is a CUBIC-related bug.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TV8WPG06X3CYZXY26X0G.png&w=715&h=505&f=webp&fit=cover&position=center)

_Reno recovers cleanly after the loss phase ends at T=2s and completes the download by ~5s_

## Tracing the root cause

Loss-based algorithms have two pedals, gas and brake, with a difference in how they accelerate. Well, CUBIC comes with some extra features. Here we are going to focus on bytes_in_flight == 0.

### TCP CUBIC after idle (Linux, 2017)

To understand the bug, we first need to understand the optimization it came from. In 2017,an issue was found with Linux kernel's CUBIC implementation. The[ _commit message_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) explains:

> The epoch is only updated/reset initially and when experiencing losses. The delta "t" of `now - epoch_start` can be arbitrary large after app idle as well as the `bic_target`. Consequentially the slope (inverse of `ca->cnt`) would be really large, and eventually `ca->cnt` would be lower-bounded in the end to 2 to have delayed-ACK slow-start behavior.
> 
> This particularly shows up when `slow_start_after_idle` is disabled as a dangerous cwnd inflation (1.5 x RTT) after few seconds of idle time.

The **epoch** is the reference timestamp CUBIC uses to anchor its growth curve: `W_cubic(delta_t)` is parameterized by `delta_t = now - epoch_start`, and the epoch is reset whenever CUBIC restarts its growth function — most notably after a loss event reduces `cwnd`. Between resets, `delta_t` grows monotonically with wall-clock time.

When an application goes idle (stops sending) for a while and then resumes, the CUBIC growth function `W_cubic(delta_t)` computes `delta_t` as `now - epoch_start`, as illustrated in the figure below. Since the epoch wasn't updated during idle, `delta_t` is huge, producing an enormous target window — and CUBIC would immediately try to inflate `cwnd` to an unreasonable value.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45PX0PXQBDHX7JSR6WBDTA.png&w=715&h=452&f=webp&fit=cover&position=center)

Jana Iyengar's initial fix was to reset `epoch_start` when the application resumes sending. But Neal Cardwell [_pointed out_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) the flaw in that approach:

> …it would ask the CUBIC algorithm to recalculate the curve so that we again start growing steeply upward from where cwnd is now (as CUBIC does just after a loss). Ideally we'd want the cwnd growth curve to be the same shape, just shifted later in time by the amount of the idle period.

The elegant solution, authored by Eric Dumazet, Yuchung Cheng, and Neal Cardwell, was to shift the epoch forward by the idle duration rather than resetting it. This preserves the shape of the CUBIC growth curve — just sliding it in time so that the algorithm picks up where it left off.

### The port to quiche (2020)

When CUBIC was [_first implemented_](https://blog.cloudflare.com/cubic-and-hystart-support-in-quiche/) in quiche, this idle-period adjustment was ported. However, QUIC, which runs in the user space, doesn't have TCP's kernel-level [`_CA_EVENT_TX_START_`](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) callback. Instead, the quiche implementation checks for the idle condition inside `on_packet_sent()`:
    
    
    // cubic.rs — on_packet_sent() (simplified)
    /// Updates the state when a packet is sent.
    fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
        // If the sending burst is restarting (i.e., bytes_in_flight was zero before this send),
        // adjust the congestion recovery start time to account for the gap in sending.
        if bytes_in_flight == 0 {
            let delta = now - self.last_sent_time;
            self.congestion_recovery_start_time += delta;
        }
        // Record the time of this send event.
        self.last_sent_time = now;
    }

### Where it breaks: the QUIC difference

The fix ported to quiche included a bug in the original kernel change which was fixed by a [_followup change to the kernel cubic module_](https://github.com/torvalds/linux/commit/c2e7204d180f8efc80f27959ca9cf16fa17f67db) about a week later. The commit message for the second fix explains:

> `tcp_cubic`: do not set `epoch_start` in the future  
>  Tracking idle time in `bictcp_cwnd_event()` is imprecise, as `epoch_start`  
>  is normally set at ACK processing time, not at send time.
> 
> Doing a proper fix would need to add an additional state variable,  
>  and does not seem worth the trouble, given CUBIC bug has been there  
>  forever before Jana noticed it.
> 
> Let's simply not set `epoch_start` in the future, otherwise  
> `bictcp_update()` could overflow and CUBIC would again  
>  grow `cwnd` too fast.

As mentioned in the commit message, recovery start time is set during ACK processing, and the computation of the adjustment based on sent times can push the recovery start time into the future. This explains the oscillation between recovery and congestion avoidance seen on our test. The trap only consistently triggers when every incoming ACK drives bytes_in_flight all the way to zero — which in practice means cwnd has collapsed to its minimum (two packets) and the application has data ready to send another full window the moment an ACK arrives. Outside this regime, bytes_in_flight == 0 is less likely to hold on every send, so it is less likely to trigger the bug. 

Why doesn't this also happen at connection start? The bug only triggers when the connection exits slow-start and switches over to congestion avoidance. Before exiting slow-start, `congestion_recovery_start_time` is not set, so the buggy branch in `on_packet_sent` has no recovery boundary to advance. During slow start CUBIC's `cwnd` grows by the same Reno-style ack-based rule shared by all loss-based CCAs — the cubic curve and its sensitivity to `congestion_recovery_start_time` only enter the picture once the connection is in congestion avoidance, meaning the trap needs three things at once: a real loss event to set the recovery boundary, congestion avoidance to be running, and `cwnd` collapsed to the two-packet floor.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TRJWX5RY1QFR0DK4FV15.png&w=715&h=533&f=webp&fit=cover&position=center)

_The self-perpetuating recovery trap. At minimum cwnd, every ACK cycle triggers the idle period adjustment with an inflated delta._

At a minimum cwnd (two packets), the dynamics of the connection shift into a "death spiral" where the idle period optimization becomes a self-fulfilling prophecy. This trap operates in a continuous loop:

  1. **Send and ACK packets:** The sender transmits the entire two-packet window. After one RTT (~14ms), both packets are ACKed, causing bytes_in_flight to drop to zero.
  2. **False idle detection:** When the next burst is sent, on_packet_sent() sees bytes_in_flight == 0 and assumes the connection was idle, but it was congestion limited.
  3. **Inflated delta:** The calculation uses now - last_sent_time to determine the idle duration. When the congestion window (`cwnd`) is at its minimum, `last_sent_time` is the timestamp of the _start_ of the previous RTT cycle. Therefore, the resulting delta is approximately 14ms (the connection's RTT + additional rounding errors). This RTT-sized delta is incorrectly applied as the "idle" time. The _actual_ time the connection was idle (the processing gap between the last ACK arriving and the next packet being sent) is effectively 0. By measuring the full RTT instead of the true gap, the delta is inflated significantly, aggressively shifting the recovery start time forward, possibly into the future.
  4. **Perceived recovery:** Because the recovery start time is now in the future, the `in_congestion_recovery()` check returns true for every incoming ACK. Processing of the next ACK exits recovery and sets the recovery start to the ACK time which is larger than last_sent_time, making it likely for the congestion controller to push the recovery time into the future when doing the next send.
  5. **Stagnation:** Since CUBIC skips `cwnd` growth for any packet perceived to be in a recovery period, the window remains pinned at two packets — ensuring the pipe drains completely on the next ACK and restarting the cycle.



And this loop repeats for thousands of cycles until the accumulation of small deviations — from scheduler jitter and ACK processing variance — lets the <= boundary in `in_congestion_recovery()` slip behind the next packet's send time, breaking the cycle.

## The fix: measuring idle from the right moment

Fixing the death spiral involves measuring the idle duration from when bytes_in_flight actually transitioned to zero (the last ACK processed) rather than the last packet sent.

### The code change

  1. Add last_ack_time timestamp to the CUBIC state.
  2. Update that timestamp when ACKs arrive.
  3. Use it for the idle delta computation:


    
    
    // cubic.rs — on_packet_sent()
    fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
        // Check if the connection was idle before this packet was sent.
        if bytes_in_flight == 0 {
            if let Some(recovery_start_time) = r.congestion_recovery_start_time {
                // Measure idle from the most recent activity: either the
                // last ACK (approximating when bif hit 0) or the last data
                // send, whichever is later. Using last_sent_time alone
                // would inflate the delta by a full RTT when cwnd is small
                // and bif transiently hits 0 between ACK and send.
                let idle_start = cmp::max(cubic.last_ack_time, cubic.last_sent_time);
    
                if let Some(idle_start) = idle_start {
                    if idle_start < now {
                        let delta = now - idle_start;
                        r.congestion_recovery_start_time =
                            Some(recovery_start_time + delta);
                    }
                }
            }
    }

With the delta now reflecting the actual gap since the last ACK, the recovery boundary stops chasing the send time:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ASH8GZ33QEC3H67W7MMJ.png&w=715&h=369&f=webp&fit=cover&position=center)

_Old code: boundary advances one RTT per cycle, always landing on or ahead of the next send._

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4655NBGY57G0JX3FXN88XF.png&w=715&h=369&f=webp&fit=cover&position=center)

_Fix: boundary barely moves; the next send lands ahead of it and cwnd grows._

For genuinely idle connections, `last_ack_time` is far in the past and the same expression captures the full idle duration, the original epoch-shift behavior is preserved.

## Validation

With the fix applied, the 100% pass rate of our quiche testing suite was restored.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image11](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KFFNQ428RM6AY394S59B.png&w=715&h=506&f=webp&fit=cover&position=center)

_After the fix, cwnd grows along the expected CUBIC curve and the download completes in ~4-5 seconds._

We don't worry about the losses at the end of the connection — that's expected because we fully utilized the router's allocated buffer. In other words, we are fully utilizing the available bandwidth in this test case.

## Takeaways

  * **"Idle" is harder to define than it sounds.** Normal pipeline delays at small windows can look like idleness to simple checks.
  * **Minimum-cwnd dynamics are a unique corner case.** The bug was invisible at high speeds and only triggered after severe loss.
  * **The fix was surprisingly small compared to the complexity of the behavior.** After weeks of instrumenting qlogs and analyzing visualizations to find the root cause, the solution required changing just three lines of code. As we noted during the investigation: the effort to find the bug was massive, but the fix itself was basically one line of logic.



The fix described in this post has been contributed to **`_cloudflare/quiche_`** , Cloudflare's open-source implementation of QUIC and HTTP/3. Our CCA efforts go beyond loss-based algorithms: we also use quiche’s modular congestion control design to experiment with and tune our model-based [_BBRv3_](https://blog.cloudflare.com/new-standards/#congestion-control) implementation, now enabled for a growing percentage of our QUIC deployments. Stay tuned for further updates on QUIC congestion control implementation and performance. 

If you're interested in congestion control, transport protocols, or contributing to open-source networking code, check out the **quiche** repository. We're always looking for talented engineers who love digging into problems like these, please explore our[ _open positions_](https://www.cloudflare.com/careers/).

On this page

Discuss Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fquic-death-spiral-fix%2F&t=When%20%22idle%22%20isn%27t%20idle%3A%20how%20a%20Linux%20kernel%20optimization%20became%20a%20QUIC%20bug)[](https://x.com/intent/post?text=When+%22idle%22+isn%27t+idle%3A+how+a+Linux+kernel+optimization+became+a+QUIC+bug&url=https%3A%2F%2Fblog.cloudflare.com%2Fquic-death-spiral-fix%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fquic-death-spiral-fix%2F)[](https://bsky.app/intent/compose?text=When+%22idle%22+isn%27t+idle%3A+how+a+Linux+kernel+optimization+became+a+QUIC+bug+https%3A%2F%2Fblog.cloudflare.com%2Fquic-death-spiral-fix%2F)[](https://mastodonshare.com/?text=When+%22idle%22+isn%27t+idle%3A+how+a+Linux+kernel+optimization+became+a+QUIC+bug&url=https%3A%2F%2Fblog.cloudflare.com%2Fquic-death-spiral-fix%2F)[](https://www.threads.net/intent/post?text=When+%22idle%22+isn%27t+idle%3A+how+a+Linux+kernel+optimization+became+a+QUIC+bug+https%3A%2F%2Fblog.cloudflare.com%2Fquic-death-spiral-fix%2F)

## Related tags

[Congestion Control](https://blog.cloudflare.com/tag/congestion-control/)[Debugging](https://blog.cloudflare.com/tag/debugging/)[HTTP3](https://blog.cloudflare.com/tag/http3/)[Networking](https://blog.cloudflare.com/tag/networking/)[QUIC](https://blog.cloudflare.com/tag/quic/)[QUICHE](https://blog.cloudflare.com/tag/quiche/)[Rust](https://blog.cloudflare.com/tag/rust/)

Follow on Social Media

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.
