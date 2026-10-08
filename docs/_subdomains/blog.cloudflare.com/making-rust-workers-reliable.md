---
url: https://blog.cloudflare.com/making-rust-workers-reliable/
title: Making Rust Workers reliable: panic and abort recovery in wasm\u2011bindgen | Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:39.328633+00:00
---

# Making Rust Workers reliable: panic and abort recovery in wasm‑bindgen | Cloudflare Blog

> Source: https://blog.cloudflare.com/making-rust-workers-reliable/

[Blog](https://blog.cloudflare.com/)

[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developers](https://blog.cloudflare.com/tag/developers/)+8Show 8 more tags

11 TagsShow 11 tags

  * Post Tags
  * [Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developers](https://blog.cloudflare.com/tag/developers/)[Engineering](https://blog.cloudflare.com/tag/engineering/)[Internship Experience](https://blog.cloudflare.com/tag/internship-experience/)[Open Source](https://blog.cloudflare.com/tag/open-source/)[Reliability](https://blog.cloudflare.com/tag/reliability/)[Rust](https://blog.cloudflare.com/tag/rust/)[Rust Workers](https://blog.cloudflare.com/tag/rust-workers/)[WASM](https://blog.cloudflare.com/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/tag/webassembly/)
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



[Engineering](https://blog.cloudflare.com/tag/engineering/)[Internship Experience](https://blog.cloudflare.com/tag/internship-experience/)[Open Source](https://blog.cloudflare.com/tag/open-source/)[Reliability](https://blog.cloudflare.com/tag/reliability/)[Rust](https://blog.cloudflare.com/tag/rust/)[Rust Workers](https://blog.cloudflare.com/tag/rust-workers/)[WASM](https://blog.cloudflare.com/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/tag/webassembly/)

[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developers](https://blog.cloudflare.com/tag/developers/)[Engineering](https://blog.cloudflare.com/tag/engineering/)[Internship Experience](https://blog.cloudflare.com/tag/internship-experience/)[Open Source](https://blog.cloudflare.com/tag/open-source/)[Reliability](https://blog.cloudflare.com/tag/reliability/)[Rust](https://blog.cloudflare.com/tag/rust/)[Rust Workers](https://blog.cloudflare.com/tag/rust-workers/)[WASM](https://blog.cloudflare.com/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/tag/webassembly/)

April 22, 2026

# Making Rust Workers reliable: panic and abort recovery in wasm‑bindgen

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/author/guy-bedford/), [Hood Chatham](https://blog.cloudflare.com/author/hood/), and [Logan Gatlin](https://blog.cloudflare.com/author/logan-gatlin/)

10 minute read

COPY URL

This post is also available in [日本語](https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/), [한국어](https://blog.cloudflare.com/ko-kr/making-rust-workers-reliable/), [繁體中文](https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/), and [简体中文](https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/).

![BLOG-3145 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HQEZP84STFXFD0H3EBY7.png&w=2048&h=1152&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88O7x3uLt3eXz6e758/L19u/r//////7+5Ofzx9XuxNb01uP66ez38u7t//////7/2OH2rsjwqMj2w9j93+f77+3x////////1eL6psf0nsX6vdf/3uj/8PD2////////4Oz/t9T6sdT/y+P/5/H/9/f7////////8fr/1en/0ur/5Pb/9v7/////////////////7fr/7Pz/+P//////////////////////9///9v//////////////)

[_Rust Workers_](https://developers.cloudflare.com/workers/languages/rust/) run on the Cloudflare Workers platform by compiling Rust to WebAssembly, but as we’ve found, WebAssembly has some sharp edges. When things go wrong with a panic or an unexpected abort, the runtime can be left in an undefined state. For users of Rust Workers, panics were historically fatal, poisoning the instance and possibly even bricking the Worker for a period of time.

While we were able to detect and mitigate these issues, there remained a small chance that a Rust Worker would unexpectedly fail and cause other requests to fail along with it. An unhandled Rust abort in a Worker affecting one request might escalate into a broader failure affecting sibling requests or even continue to affect new incoming requests. The root cause of this was in wasm-bindgen, the core project that generates the Rust-to-JavaScript bindings Rust Workers depend on, and its lack of built-in recovery semantics.

In this post, we’ll share how the latest version of Rust Workers handles comprehensive Wasm error recovery that solves this abort-induced sandbox poisoning. This work has been contributed back into [_wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen) as part of our collaboration within the wasm-bindgen organization [_formed last year_](https://blog.rust-lang.org/inside-rust/2025/07/21/sunsetting-the-rustwasm-github-org/). First with `panic=unwind` support, which ensures that a single failed request never poisons other requests, and then with abort recovery mechanisms that guarantee Rust code on Wasm can never re-execute after an abort. 

## Initial recovery mitigations

Our initial attempts to address reliability in this area focused on understanding and containing failures caused by Rust panics and aborts in production Rust Workers. We introduced a custom Rust panic handler that tracked failure state within a Worker and triggered full application reinitialization before handling subsequent requests. On the JavaScript side, this required wrapping the Rust-JavaScript call boundary using Proxy‑based indirection to ensure that all entrypoints were consistently encapsulated. We also made targeted modifications to the generated bindings to correctly reinitialize the WebAssembly module after a failure.

While this approach relied on custom JavaScript logic, it demonstrated that reliable recovery was achievable and eliminated the persistent failure modes we were seeing in practice. This solution was shipped by default to all workers‑rs users starting in version 0.6, and it laid the groundwork for the more general, upstreamed abort recovery mechanisms described in the sections that follow.

## Implementing `panic=unwind` with WebAssembly Exception Handling

The abort recovery mechanisms described above ensure that a Worker can survive a failure, but they do so by reinitializing the entire application. For stateless request handlers, this is fine. But for workloads that hold meaningful state in memory, such as Durable Objects, reinitialization means losing that state entirely. A single panic in one request could wipe the in-memory state being used by other concurrent requests.

In most native Rust environments, panics can be unwound, allowing destructors to run and the program to recover without losing state. In WebAssembly, things historically looked very different. Rust compiled to Wasm via `wasm32-unknown-unknown` defaults to `panic=abort`, so a panic inside a Rust Worker would abruptly trap with an `unreachable` instruction and exit Wasm back to JS with a `WebAssembly.RuntimeError`.

To recover from panics without discarding instance state, we needed `panic=unwind` support for `wasm32-unknown-unknown` in wasm-bindgen, made possible by the WebAssembly Exception Handling proposal, which gained wide engine support in 2023.

We start by compiling with `RUSTFLAGS='-Cpanic=unwind' cargo build -Zbuild-std`, which rebuilds the standard library with unwind support and generates code with proper panic unwinding. For example:
    
    
    struct HasDropA;
    struct HasDropB;
    extern "C" {
        fn imported_func();
    }
    
    fn some_func() {
        let a = HasDropA;
        let b = HasDropB;
        imported_func();
    }

compiles to WebAssembly as:
    
    
    try
      call <imported_func>
    catch_all
      call <drop_b>
      call <drop_a>
      rethrow
    end
    call <drop_b>
    call <drop_a>

This ensures that even if `imported_func()` panics, destructors still run. Similarly, `std::panic::catch_unwind(|| some_func())` compiles into:
    
    
    try
      call <some_func>
      ;; set result to Ok(return value)
    catch
      try
        call <std::panicking::catch_unwind::cleanup>
        ;; set result to Err(panic payload)
      catch_all
        call <core::panicking::cannot_unwind>
        unreachable
      end
    end

Getting this to work end-to-end required several changes to the wasm-bindgen toolchain. The WebAssembly parser Walrus did not know how to handle try/catch instructions, so we added support for them. The descriptor interpreter also needed to be taught how to evaluate code containing exception handling blocks. At that point, the full application could be built with `panic=unwind`.

The final step was modifying the exports generated by wasm-bindgen to catch panics at the Rust-JavaScript boundary and surface them as JavaScript `PanicError` exceptions. One subtlety: Rust will catch foreign exceptions and abort when unwinding through `extern "C"` functions, so exports needed to be marked `extern "C-unwind"` to explicitly allow unwinding across the boundary. For futures, a panic rejects the JavaScript `Promise` with a `PanicError`.

Closures required special attention to ensure unwind safety was properly checked, via a new `MaybeUnwindSafe` trait that checks `UnwindSafe` only when built with `panic=unwind`. This quickly exposed a problem, though: many closures capture references that remain after an unwind, making them inherently unwind-unsafe. To avoid a situation where users are encouraged to incorrectly wrap closures in `AssertUnwindSafe` just to satisfy the compiler, we added `Closure::new_aborting` variants, which terminate on panic instead of unwinding in cases where unwind safety can't be guaranteed.

With panic unwinding enabled:

  * Panics in exported Rust functions are caught by wasm-bindgen
  * Panics surface to JavaScript as PanicError exceptions
  * Async exports reject their returned promises with a PanicError
  * Rust destructors run correctly
  * The WebAssembly instance remains valid and reusable



The full details of the approach and how to use it in wasm-bindgen are covered in the latest guide page for [_Wasm Bindgen: Catching Panics_](https://wasm-bindgen.github.io/wasm-bindgen/reference/catch-unwind.html).

## Abort recovery

Even with `panic=unwind` support, aborts still happen - out-of-memory errors being one common cause. Because aborts can’t unwind, there is no possibility of state recovery at all, but we can at least detect and recover from aborts for future operations to avoid invalid state erroring subsequent requests.

Panic unwind support introduced a new problem for abort recovery. When we receive an error from Wasm we don’t know if it came from an `extern “C-unwind”` foreign error, or if it was a genuine abort. Aborts can take many shapes in WebAssembly.

We had two options to solve this technically: either mark all errors which are definitely aborts, or mark all errors which are definitely unwinds. Either could have worked but we chose the latter. Since our foreign exception handling was directly using raw WAT-level (WebAssembly text format) Exception Handling instructions already, we found it easier to implement exception tags for foreign exceptions to distinguish them from aborting non-unwind-safe exceptions.

With the ability to clearly distinguish between recoverable and non-recoverable errors thanks to this `Exception.Tag` feature in WebAssembly Exception Handling, we were able to then integrate both a new abort handler and abort reentrancy guards.  
  
A new abort hook, `set_on_abort`, can be used at initialization time to attach a handler that recovers accordingly for the platform embedding’s needs.

Hardening panic and abort handling is critical to avoiding invalid execution state. WebAssembly allows deeply interleaved call stacks, where Wasm can call into JavaScript and JavaScript can re-enter Wasm at arbitrary depths, while alongside this, multiple tasks can be functioning in the same instance. Previously, an abort occurring in one task or nested stack was not guaranteed to invalidate higher stacks through JS, leading to undefined behavior. Care was required to ensure we can guarantee the execution model, and contribution in this space remains ongoing.

While aborts are never ideal, and reinitialization on failure is an absolute worst-case scenario, implementing critical error recovery as the last line of defense ensures execution correctness and that future operations will be able to succeed. The invalid state does not persist, ensuring a single failure does not cascade into multiple failures.

## Extension: abort reinitialization for wasm-bindgen libraries

While we were working on this, we realized that this is a common problem for libraries used by JS that are built with wasm-bindgen, and that they would also benefit from attaching an abort handler to be able to perform recovery.

But when building Wasm as an ES module and importing it directly (e.g. via `import { func } from ‘wasm-dep’`), it’s not clear what the recovery mechanism would be for a Wasm abort while calling `func()` for an already-linked and initialized library that is in a user JS application.

While not strictly a Rust Workers use case, our team also supports JS-based Workers users who run Rust-backed Wasm library dependencies. If we could fix this problem at the same time, that could indirectly also benefit Wasm usage on the Cloudflare Workers platform.

To support automatic abort recovery for Wasm library use cases, we added support for an experimental reinitialization mechanism into wasm‑bindgen, `--reset-state-function`. This exposes a function that allows the Rust application to effectively request that it reset its internal Wasm instance back to its initial state for the next call, without requiring consumers of the generated bindings to reimport or recreate them. Class instances from the old instance will throw as their handles become orphaned, but new classes can then be constructed. The JS application using a Wasm library is errored but not bricked.

The full technical details of this feature and how to use it in wasm-bindgen are covered in the new wasm-bindgen guide section [_Wasm Bindgen: Handling Aborts_](https://wasm-bindgen.github.io/wasm-bindgen/reference/handling-aborts.html).

## Maturing the Rust Wasm Exception Handling ecosystem

Upstream contributions for this work did not stop at the wasm-bindgen project. Building for Wasm with `panic=unwind` still requires an experimental nightly Rust target, so we’ve also been working to advance Rust’s Wasm support for WebAssembly Exception Handling to help bring this to stable Rust.

During the development of WebAssembly Exception Handling, a late‑stage specification change resulted in two variants: [_legacy exception handling_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/legacy/Exceptions.md) and the final modern [_exception handling "with exnref"_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md). Today, Rust’s WebAssembly targets still default to emitting code for the legacy variant. While legacy exception handling is widely supported, it is now deprecated.

Modern WebAssembly Exception Handling is supported as of the following JS platform releases:

Runtime| Version| Release Date  
---|---|---  
v8| 13.8.1| April 28, 2025  
workerd| v1.20250620.0| June 19, 2025  
Chrome| 138| June 28, 2025  
Firefox| 131| October 1, 2024  
Safari| 18.4| March 31, 2025  
Node.js| 25.0.0| October 15, 2025  
  
As we were investigating the support matrix, the largest concern ended up being the Node.js 24 LTS release schedule, which would have left the entire ecosystem stuck on legacy WebAssembly Exception Handling until April 2028.

Having discovered this discrepancy, we were able to backport modern exception handling to the Node.js 24 release, and even backport the fixes needed to make it work on the Node.js 22 release line to ensure support for this target. This should allow the modern Exception Handling proposal to become the default target next year.

Over the coming months, we’ll be working to make the transition to stable `panic=unwind` and modern Exception Handling as invisible as possible to end users.

While these long‑term investments in the ecosystem take time, they help build a stronger foundation for the Rust WebAssembly community as a whole, and we’re glad to be able to contribute to these improvements.

## Using panic unwind in Rust Workers

As of version 0.8.0 of Rust Workers, we have a new `--panic-unwind` flag, which can be added to the build command, following the [_instructions here_](https://github.com/cloudflare/workers-rs?tab=readme-ov-file#panic-recovery-with---panic-unwind).

With this flag, panics can be fully recovered, and abort recovery will use the new abort classification and recovery hook mechanism. We highly recommend upgrading and trying it out for a more stable Rust Workers experience, and plan to make `panic=unwind` the default in a subsequent release. Users remaining on `panic=abort` will still continue to take advantage of the previous custom recovery wrapper handling from 0.6.0.

## Committing to Rust Workers stability

This work is part of our ongoing effort towards a stable release for Rust Workers. By solving these sharp edges of the Wasm platform foundations at their root, and contributing back to the ecosystem where it makes sense, we build stronger foundations not just for our platform, but the entire Rust, JS, and Wasm ecosystem.

We have a number of future improvements planned for Rust Workers, and we’ll soon be sharing updates on this additional work, including wasm-bindgen generics and automated bindgen, which Guy Bedford from our team previewed in a talk on [_Rust & JS Interoperability at Wasm.io_](https://www.youtube.com/watch?v=zlSJY8Qv5XI) last month.

Find us in **#rust‑on‑workers** on the [_Cloudflare Discord_](https://discord.com/invite/cloudflaredev). We also welcome feedback and discussion and especially all new contributors to the [_workers-rs_](https://github.com/cloudflare/workers-rs) and [_wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen) GitHub projects.

On this page

Discuss Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fmaking-rust-workers-reliable%2F&t=Making%20Rust%20Workers%20reliable%3A%20panic%20and%20abort%20recovery%20in%20wasm%E2%80%91bindgen)[](https://x.com/intent/post?text=Making+Rust+Workers+reliable%3A+panic+and+abort+recovery+in+wasm%E2%80%91bindgen&url=https%3A%2F%2Fblog.cloudflare.com%2Fmaking-rust-workers-reliable%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fmaking-rust-workers-reliable%2F)[](https://bsky.app/intent/compose?text=Making+Rust+Workers+reliable%3A+panic+and+abort+recovery+in+wasm%E2%80%91bindgen+https%3A%2F%2Fblog.cloudflare.com%2Fmaking-rust-workers-reliable%2F)[](https://mastodonshare.com/?text=Making+Rust+Workers+reliable%3A+panic+and+abort+recovery+in+wasm%E2%80%91bindgen&url=https%3A%2F%2Fblog.cloudflare.com%2Fmaking-rust-workers-reliable%2F)[](https://www.threads.net/intent/post?text=Making+Rust+Workers+reliable%3A+panic+and+abort+recovery+in+wasm%E2%80%91bindgen+https%3A%2F%2Fblog.cloudflare.com%2Fmaking-rust-workers-reliable%2F)

## Related tags

[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developers](https://blog.cloudflare.com/tag/developers/)[Engineering](https://blog.cloudflare.com/tag/engineering/)[Internship Experience](https://blog.cloudflare.com/tag/internship-experience/)[Open Source](https://blog.cloudflare.com/tag/open-source/)[Reliability](https://blog.cloudflare.com/tag/reliability/)[Rust](https://blog.cloudflare.com/tag/rust/)[Rust Workers](https://blog.cloudflare.com/tag/rust-workers/)[WASM](https://blog.cloudflare.com/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/tag/webassembly/)

Follow on Social Media

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.
