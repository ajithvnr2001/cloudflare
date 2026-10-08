---
url: https://blog.cloudflare.com/dns-cache-memory-optimization-1111/
title: How we saved 100 terabytes of memory by optimizing 1.1.1.1\u2019s DNS cache | Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:49.836255+00:00
---

# How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache | Cloudflare Blog

> Source: https://blog.cloudflare.com/dns-cache-memory-optimization-1111/

[Blog](https://blog.cloudflare.com/)

[1.1.1.1](https://blog.cloudflare.com/tag/1-1-1-1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)[DNS](https://blog.cloudflare.com/tag/dns/)+4Show 4 more tags

7 TagsShow 7 tags

  * Post Tags
  * [1.1.1.1](https://blog.cloudflare.com/tag/1-1-1-1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)[DNS](https://blog.cloudflare.com/tag/dns/)[Engineering](https://blog.cloudflare.com/tag/engineering/)[Optimization](https://blog.cloudflare.com/tag/optimization/)[Performance](https://blog.cloudflare.com/tag/performance/)[Rust](https://blog.cloudflare.com/tag/rust/)
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



[Engineering](https://blog.cloudflare.com/tag/engineering/)[Optimization](https://blog.cloudflare.com/tag/optimization/)[Performance](https://blog.cloudflare.com/tag/performance/)[Rust](https://blog.cloudflare.com/tag/rust/)

[1.1.1.1](https://blog.cloudflare.com/tag/1-1-1-1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)[DNS](https://blog.cloudflare.com/tag/dns/)[Engineering](https://blog.cloudflare.com/tag/engineering/)[Optimization](https://blog.cloudflare.com/tag/optimization/)[Performance](https://blog.cloudflare.com/tag/performance/)[Rust](https://blog.cloudflare.com/tag/rust/)

August 27, 2026

# How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

12 minute read

COPY URL

![](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M117Y6R8CDGVT4K2XX6VQ2YX.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////vf/3t/zwM3pvdDrz93y4Obz6efu/////vj/2d7ztcnnr8roxdnv2+Ty6Ojv//////v/2N/0r8flpcflvtju2ebz6evy////////3ub2ts/mrc7lxN7v3uz17vH1////////7PL6zN/qxd/q1+z06/f69/r6/////////f/+5vLv4/Pw7/36+//////+////////////+v/0+f/2///////////////////////////2///4////////////)

[ _Big Pineapple_](https://blog.cloudflare.com/big-pineapple-intro/), the platform behind [_1.1.1.1_](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/), [_Gateway DNS_](https://www.cloudflare.com/products/gateway/), [_DNS Firewall_](https://www.cloudflare.com/dns/dns-firewall/), [_AS112_](https://blog.cloudflare.com/the-as112-project/), and several other Cloudflare DNS services, stores over 250 billion DNS cache entries at any given time. At that scale, wasting a single byte per entry costs more than 250 gigabytes of memory across our fleet.

Five successive changes to how cache entries are stored in memory cut the per-entry footprint by over 50%. Across our fleet, these changes freed up roughly 100 terabytes of memory, equivalent to the amount of RAM in 130 of our [_Gen 13 servers_](https://blog.cloudflare.com/gen13-config/). The cache also got faster. Insert throughput rose 43% and lookup latency dropped 19%, as fewer allocations and better memory locality meant we did not trade speed for space.

## What we cache

On cold start, Big Pineapple starts out with an empty cache. As DNS queries arrive, the cache fills until it hits its maximum entry count, at which point we evict older or less popular items to make room.

The exact cache size varies by data center. When [_EDNS Client Subnet (ECS)_](https://en.wikipedia.org/wiki/EDNS_Client_Subnet) is in use, authoritative servers return different answers depending on the client's network, so we cache multiple versions of the same query. This increases both the number of entries and the memory each one consumes, making the optimizations in this post especially impactful for ECS-heavy locations.

Each item in the cache is a key-value pair. The key identifies what was queried:
    
    
    pub struct CacheKey {
        qname: Name,
        qtype: Rtype,
        authenticated: bool,
        tag: Vec<u8>,
    }

The value stores the DNS response itself: the answer, authority, and additional record sections, along with metadata like the creation time, a hit counter, and the Time-to-Live (TTL).
    
    
    pub struct CacheEntry {
        timestamp: UnixTimeStamp,
        pub inception: Instant,
        pub ttl: Ttl,
        pub hits: u32,
        pub answers: Vec<Record>,
        pub authority: Vec<Record>,
        pub additional: Vec<Record>,
        pub errors: Vec<ExtendedError>,
        ...
    }

Both structs have room for improvement. Several fields use types that carry overhead we don't need once the entry is stored.

## Benchmarking memory usage

To measure the impact of each change, we benchmark by filling the cache with randomly generated entries that roughly match the traffic distribution we see in production: 56% `A` records, 25% `AAAA`, and 19% `TXT`. Each entry contains between one and four records.

`TXT` records serve as a stand-in for all non-`A`/`AAAA` record types in the benchmark. Their size is randomized between 64 and 224 bytes, close to the average response size we see for variable-length record types.

We track memory usage using a [_custom allocator_](https://doc.rust-lang.org/std/alloc/trait.GlobalAlloc.html) that wraps Rust’s `System`[ _allocator_](https://doc.rust-lang.org/std/alloc/struct.System.html) and records the number and size of allocations per cache entry. Alongside memory, we measure insert throughput and lookup latency across the full cache flow to make sure memory savings don’t come at the cost of performance.

These inputs approximate production rather than reproduce it exactly. Process memory also depends on traffic mix, cache occupancy, allocator state, and memory used outside the cache. We therefore measured resident memory across production instances during the rollout.

## The cost of capacity

`Vec<T>` stores three fields: a pointer to heap-allocated data, the current length, and the total capacity. When you push an item, `Vec` checks whether the length exceeds the capacity and reallocates if needed. If there’s room, it just appends the item and increments the length.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/Pz69vb06+vq5ufm7Ozs8PDy6+rt3t3h///9+/r48O/t6+rq8O/w9fT27+7y4uHm///////99/Tz8vDw9/X2+/r89fT46eft/////////vv6+vf3/vz9/////fv/8O/0////////////////////////////+Pf7//////////////////////////////7/////////////////////////////////////////////////////////////////)![1.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1171ECV1YR5KPQ90P5KWCTQ.png&w=715&h=308&f=webp&fit=cover&position=center)

Once we store a DNS response in the cache, however, we never modify it again. The capacity field serves no purpose, but still costs 8 bytes per `Vec`. The over-allocated heap space is wasted as well, as a `Vec` with capacity for eight items but only five stored leaves three slots unused on the heap.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA9u7v8+fo7NrY6NPR6NrX6OLf4+Hg3NfY+/P09+3t8ODf69rX7ODd7ejl6Obl4Nzd//z8/fb29uno8eTi8+rn9PHv7+7t5+Tl/////////fX0+fDu+/bz/fz5+Pn48O7v//////////////z5///+////////+fn5////////////////////////////////////////////////////////////////////////////////////////////////)![2.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1171TF66D0RDY101KB6WX7J.png&w=715&h=299&f=webp&fit=cover&position=center)

Using `Box<[T]>` solves both problems. It can’t grow after creation, so it doesn’t need a capacity field or reserve space for future elements. The same applies to `String`, which also carries a capacity field. `Box<str>` drops it.

Each cache entry stores 8 `Vec` and `String` fields. Replacing them with `Box<[T]>` and `Box<str>` saves 8 bytes per field, 64 bytes per entry. It also eliminates the excess heap memory that `Vec` reserves for future growth. The combined savings add up to over 15 terabytes with over 250 billion cache entries.

## Fewer lists, fewer pointers

Rather than storing the answer, authority, and additional sections in separate lists, we can store a single list with offsets to the start of each section. Since DNS record counts per section fit in a `u16`, we can use a `u16` (2 bytes) for each offset, compared to the 8-byte pointer and 8-byte length that each separate `Box<[T]>` requires.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//7//fr79fLx7+7t7/Lx8PX17fHx5+jo/////vv89vPz8fDv8PTz8ff27vPz6Onq//////7++Pb28/Pz8/f28/n58PX26uzt////////+/r69/f39/r6+P399Pn57vDx//////////7++/v7/P/+/f//+v7+8/X2////////////////////////////+fr6/////////////////////////////f39//////////////////////////////7+)![3.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M11729F5HH4PQEXGEQBD4SKG.png&w=715&h=541&f=webp&fit=cover&position=center)

This removes two lists, each with an 8-byte pointer and 8-byte length, and replaces them with two 2-byte offsets, saving 28 bytes per entry.

These savings do not always map directly to the number of bytes removed from individual fields. Rust inserts [_padding to satisfy alignment requirements_](https://doc.rust-lang.org/nomicon/repr-rust.html) and rounds a struct’s size up to a multiple of its alignment. Removing a small field can therefore eliminate additional padding. For example, we also packed several boolean fields into a single [_bitflag_](https://docs.rs/bitflags/latest/bitflags/). This reduced the surrounding padding, causing the struct to shrink by more than the size of the individual booleans.

## Dropping the owner

Each DNS record has an owner, the domain the record belongs to. In many cases, this owner is identical to the domain being queried. For example, a query for `example.com A` returns two records with the same owner:
    
    
    $ dig example.com A
    
    ;; ANSWER SECTION:
    example.com.        300    IN    A        198.51.100.1
    example.com.        300    IN    A        198.51.100.2

But when a `CNAME` is involved, for example, the record owner can differ from the queried domain:
    
    
    $ dig example.com A
    
    ;; ANSWER SECTION:
    example.com.        300    IN    CNAME    cdn.example.com.
    cdn.example.com.    300    IN    A        198.51.100.1
    cdn.example.com.    300    IN    A        198.51.100.2

The DNS wire format handles repeated owners using name compression, as defined in [_RFC 1035_](https://datatracker.ietf.org/doc/html/rfc1035#section-4.1.4). Rather than encoding the same domain twice, subsequent occurrences store a 2-byte pointer to the first occurrence. A domain like `www.example.com` can encode just `www` followed by a pointer to where `example.com` already appeared in the message.

This works well on the wire, but in our cache we store the full owner name alongside each record. Following compression pointers during cache lookups is expensive on the hot path, so we trade memory for speed.

Most records, however, have an owner identical to the queried domain. For those, we can drop the owner entirely and infer it at read time. When the owner differs, such as the `A` records behind a `CNAME`, we store the full name.
    
    
    pub struct Record {
        owner: Option<Box<Name>>,
        class: Class,
        ttl: Ttl,
        rtype: Rtype,
        data: RecordData,
    }

When `owner` is `None`, response construction restores the queried domain from the cache key, avoiding a heap allocation. This means the record is no longer self-contained, but the cache key is already available during every lookup. When the owner differs, `Some` stores a pointer to the full name on the heap.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//74+/rz8PHo6uzj7e7o8fHt7+/s6enl///6+vz07/Po6e7j7PDq7/Ty7fLx5uvo///9+//28Pbp6vDk7PTt8Pn37ff35O/t///////79Pnt7vTo8Pjy8/388Pv85/Py////////+/309fjv9/v3+f//9///7/j4///////////8/fz4//79////////+vz8///////////////+////////////////////////////////////////////////)![4.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1172Q50SZ00545BWCNAAP2S.png&w=715&h=334&f=webp&fit=cover&position=center)

In practice, most cached records have an owner identical to the queried domain, so the majority require no heap allocation for the owner field.

## Enum sizing

Rust enums are [_sum types_](https://en.wikipedia.org/wiki/Algebraic_data_type): each variant can carry different data, but the enum is always the size of its largest variant.
    
    
    pub enum Option<T> {
        Some(T),
        None,
    }

`Option` is either `Some` and holds a value, or `None` and holds nothing. Both variants take the same amount of memory. The enum stores a tag indicating the active variant, followed by space large enough for the largest variant’s data. When the variant is `None`, that space is unused.

For record data, it seems natural to store each DNS record type as an enum variant:
    
    
    pub enum RecordData {
        A(Ipv4Addr),
        Aaaa(Ipv6Addr),
        Txt(Txt),
        Naptr(Naptr),
        Svcb(Svcb),
        // ...
    }

But the enum is always as large as its largest variant. In our case, that’s `NAPTR` at 136 bytes. It stores three variable-length text fields, a domain name, and two integers. As a result, the full enum, including the variant tag and padding, becomes 144 bytes.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8fbw7PLq4ure3ObY3+nc4+zj4uri3OLb8fbv7fLr5Ori3+be4ejh5ezm5Orm3+Xh9Pnx8fXu6e7p5enn5urp6u3s6e7t5urq/P/4+fz28vTz7u/x7/Dz8vP18vT27/L0/////////f39+fj7+vn9/fz//f3/+vv+////////////////////////////////////////////////////////////////////////////////////////////////)![5.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M11731ZGD3390K0YFH8CHPWC.png&w=715&h=213&f=webp&fit=cover&position=center)

An `A` record only needs 4 bytes, and an `AAAA` record needs 16 bytes. `A` and `AAAA` make up over 80% of our traffic, so most records waste over 120 bytes on padding. Since a single cache entry can store many records this quickly adds up.

### Boxing the variants

To solve this problem, we can box the larger variants of the enum, moving them to a separate heap allocation. The enum then stores an 8-byte pointer to the heap, where the data takes up only the size it actually requires.
    
    
    pub enum RecordData {
        // Small and common variants are stored inline
        A(Ipv4Addr),
        Aaaa(Ipv6Addr),
        // Large variants are stored on the heap
        Txt(Box<Txt>),
        Naptr(Box<Naptr>),
        Svcb(Box<Svcb>),
        // ...
    }

For `A` and `AAAA` records, this saves 120 bytes per record. Smaller variant types like `TXT` and `CNAME` also benefit. They still occupy the 24-byte enum, but their heap allocation is sized to their actual data rather than padded to 144 bytes. `NAPTR`, the largest variant, actually pays slightly more. It now adds the cost of a heap pointer and allocation overhead. But `NAPTR` records are rare in practice, so the tradeoff is worth it.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA6/Lr5e3p2OHk0t3d1+PY3+rU3unT1uHS8vfy7fLv4ujp3eXk4+vj6fHj6O/h3+bc+/369vn37fHw6u/t8PXw9vr08/fx6+3q/////v/+9/n39vj2/P78/////v7+9fX1/////////v/+/v79/////////////Pv9////////////////////////////////////////////////////////////////////////////////////////////////)![6.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1173F6HNANE82T98F4MZ2YE.png&w=715&h=350&f=webp&fit=cover&position=center)

But boxing the larger record variants introduces costs of its own.

### The costs of boxing

Boxing has two costs. The first is allocator overhead. Each boxed variant becomes a separate heap allocation, and allocators round up to the nearest size class. Big Pineapple uses [_jemalloc_](https://jemalloc.net/), an allocator designed for multithreaded, allocation-heavy workloads. jemalloc groups allocations of similar sizes into fixed-size bins. A `TXT` record requests 32 bytes and fits exactly into a 32-byte bin, wasting nothing, but an `MX` record requests 40 bytes and rounds up to 48, wasting 8 bytes.

The second cost is poor memory locality. Without boxing, the record enum values for a cache entry sit in a single contiguous allocation. With boxing, data for each boxed variant lives in a separate heap region. Reading it requires following a pointer, and when that pointer lands far from the rest of the entry, the CPU has to fetch a new cache line. With millions of cache entries, boxed data ends up scattered across the heap rather than packed together.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+/v59vf06+3p5Ojj5+no6+zt6urq5OPh9Pby7/Ht5eji4OPe4uXl5+jr5ubn4d/c7/Lt6u7n4uXd3eDb4ePl5ufs5eTn4N3Z8vbw7fHq5eng4uXg5ujr6+zz6+rt5uLe/v/8+f338fTt7vHs8vX2+Pn+9/b58e7r///////////+/f/8//////////////36////////////////////////////////////////////////////////////////)![7.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1173Y9TP7GJE9TZJ9P3G8R2.png&w=715&h=278&f=webp&fit=cover&position=center)

Neither cost is catastrophic on its own, but eliminating both, as the next section shows, yields a measurable improvement in both memory usage and lookup latency.

## Storing records in wire format

An obvious next step would be to store the full DNS response in wire format, patching only per-client fields like the message ID on each lookup. But this has drawbacks. DNSSEC records are only included when the client sets the [_DO (DNSSEC OK)_](https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/) flag. Storing a complete wire format message means either caching two variants, one with DNSSEC and one without, or filtering them out of an already-built message. There is also a cost to parsing the full message on every lookup, which the enum approach we just described avoids by storing already-parsed records.

As a middle ground, we store just the record data as raw bytes, while keeping the rest of the cache entry as structured fields. Instead of a list of parsed enum variants, we store the records as a single `Box<[u8]>` containing each record encoded as a 2-byte length prefix followed by its raw bytes.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA8fT57PHz5Orm4eni5u7p7PHx6+3u5OPk9vn98vX36u/s5+7n7PLu8fX17/Hy6efo/P7/+fv98vXy7/Tu8/j09/r69fb37+3t////////+Pr49vn0+vz5/f//+/v89PPy/////////f37+vv3/v/9////////+ff2/////////v78/Pz5////////////+/n4//////////38/fv4/////////////Pr5//////////37/Pv4/////////////Pr5)![8.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M11749PX9A28DBGYB03Z48HN.png&w=715&h=311&f=webp&fit=cover&position=center)

This eliminates the per-variant enum overhead and the boxed heap allocations from the previous optimization. The data also becomes packed contiguously, which improves CPU cache locality. The tradeoff is that records can no longer be randomly indexed. We have to iterate through the buffer sequentially. This adds some complexity for features like [_round-robin_](https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/) rotation of `A`/`AAAA` records, but since record counts per entry are small, the cost is negligible.

When building a DNS response from cached records, most record types can be copied directly from the buffer into the outgoing message. Previously, each parsed record had to be serialized field by field back into DNS wire format. The new layout skips that work for `A`, `AAAA`, `TXT`, and all DNSSEC record types by copying their encoded bytes directly. Only records containing domain names, such as `CNAME`, `NS`, `MX`, and `SOA`, still require parsing so we can apply DNS name compression. Since records that support direct copying make up the vast majority of our traffic, this change reduces work on the lookup path. Combined with improved memory locality, this reduced cache lookup latency by 5% in our benchmarks.

To build the record data buffer, we write into a reusable scratchspace buffer that persists across cache insertions. Since previous writes have already grown it, the buffer rarely needs to be reallocated. Records vary in size, so we do not know the exact buffer size until they have been serialized. Once the records are in the scratchspace buffer, we allocate a `Box<[u8]>` and `memcpy` the data into it. This replaces the separate allocation for each boxed record with one allocation for all record data. It also avoids the waste from shrinking a `Vec<u8>`, where the allocator may not be able to reclaim the unused tail of the original allocation. In our benchmark, this change alone increased cache insert throughput by 13%.

## The results

The production measurements show how the benchmarked per-entry savings translated to whole-process resident memory. The graph below shows p90, p98, and p99 memory usage across Big Pineapple instances. The first dashed line marks the start of the rollout on May 18, 2026, and the second marks its completion across all services on July 6, 2026. Each release introduced one or more of the optimizations described above, so memory usage dropped in steps rather than all at once.

As each release rolled out, restarted instances began with empty caches and consumed more memory as those caches filled. The stable plateaus therefore represent steady-state memory usage better than the initial dips.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAR01IQ0pEOUI9Mz44N0M7O0c/OkU+Mz05TFBJR0xGPEM9ND04N0A6O0U9OUI8Mjo2UFNKSk5GPkM9NDs2Nj02OkE5OD44LzUyUVJIS01EPUA5MjYxMjcxNzs0NTgyKy8sTk9ESEk/OTszKy8pLDApMjUsMTIrJygkSEg+QkI4MTQqIicdJCgeLC4lLCwkIyIbQ0I4PDwyKSwhFx8QGyIUJikeKCcdHxwSQD81OTkvJSkdERsIFx8PJCcbJiUbHRoO)![9.png](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M1174QR0ZH0HWEQBS50Q5641.png&w=715&h=333&f=webp&fit=cover&position=center)

Per-instance memory usage dropped across all percentiles. At p99, memory dropped from 9.3 GB to 5.3 GB, a 43% reduction in resident memory. At p90, memory dropped from 6.5 GB to 3.8 GB, a 42% reduction. Instances with fuller caches saw the largest absolute savings.

In our benchmarks, these five optimizations reduced the per-entry memory footprint from 953 bytes to 420 bytes, a 56% reduction. Per-entry allocations dropped from 1.1 KB to 461 bytes. The reductions measured in production are smaller because resident memory includes the cache alongside all other process data. After the rollouts settled, aggregate working-set memory across the fleet was roughly 100 terabytes lower.

Performance also improved. Cache insert throughput increased by 43%, while lookup latency dropped by 19%.

Metric| Before| After| Change  
---|---|---|---  
Per-entry net footprint| 953 bytes| 420 bytes| -56%  
Per-entry allocations| 1.1 KB| 461 bytes| -58%  
Cache insert throughput| 625,000 entries/s| 893,000 entries/s| +43%  
Cache lookup latency| 828 ns| 670 ns| -19%  
  
We plan to reinvest the freed memory into increasing cache capacity without increasing our memory usage, which improves cache hit rates and reduces upstream query volume. We're also exploring further optimizations to the cache itself.

To learn more about Big Pineapple, see [_How Rust and Wasm power Cloudflare's 1.1.1.1_](https://blog.cloudflare.com/big-pineapple-intro/). If you work on DNS or other large systems, share the optimizations that have worked for you in the [_Cloudflare Community_](https://community.cloudflare.com/) or on the [_Cloudflare Developers Discord_](https://discord.cloudflare.com/).

On this page

Discuss Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fdns-cache-memory-optimization-1111%2F&t=How%20we%20saved%20100%20terabytes%20of%20memory%20by%20optimizing%201.1.1.1%E2%80%99s%20DNS%20cache)[](https://x.com/intent/post?text=How+we+saved+100+terabytes+of+memory+by+optimizing+1.1.1.1%E2%80%99s+DNS+cache&url=https%3A%2F%2Fblog.cloudflare.com%2Fdns-cache-memory-optimization-1111%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fdns-cache-memory-optimization-1111%2F)[](https://bsky.app/intent/compose?text=How+we+saved+100+terabytes+of+memory+by+optimizing+1.1.1.1%E2%80%99s+DNS+cache+https%3A%2F%2Fblog.cloudflare.com%2Fdns-cache-memory-optimization-1111%2F)[](https://mastodonshare.com/?text=How+we+saved+100+terabytes+of+memory+by+optimizing+1.1.1.1%E2%80%99s+DNS+cache&url=https%3A%2F%2Fblog.cloudflare.com%2Fdns-cache-memory-optimization-1111%2F)[](https://www.threads.net/intent/post?text=How+we+saved+100+terabytes+of+memory+by+optimizing+1.1.1.1%E2%80%99s+DNS+cache+https%3A%2F%2Fblog.cloudflare.com%2Fdns-cache-memory-optimization-1111%2F)

## Related tags

[1.1.1.1](https://blog.cloudflare.com/tag/1-1-1-1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)[DNS](https://blog.cloudflare.com/tag/dns/)[Engineering](https://blog.cloudflare.com/tag/engineering/)[Optimization](https://blog.cloudflare.com/tag/optimization/)[Performance](https://blog.cloudflare.com/tag/performance/)[Rust](https://blog.cloudflare.com/tag/rust/)

Follow on Social Media

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.
