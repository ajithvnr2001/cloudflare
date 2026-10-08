---
url: https://blog.cloudflare.com/d1-read-replication-beta/
title: Sequential consistency without borders: How D1 implements global read replication | Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:53:17.668082+00:00
---

# Sequential consistency without borders: How D1 implements global read replication | Cloudflare Blog

> Source: https://blog.cloudflare.com/d1-read-replication-beta/

[Blog](https://blog.cloudflare.com/)

[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[D1](https://blog.cloudflare.com/tag/d1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)+4Show 4 more tags

7 TagsShow 7 tags

  * Post Tags
  * [Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[D1](https://blog.cloudflare.com/tag/d1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/tag/developer-week/)[Edge Database](https://blog.cloudflare.com/tag/edge-database/)[SQL](https://blog.cloudflare.com/tag/sql/)
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



[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/tag/developer-week/)[Edge Database](https://blog.cloudflare.com/tag/edge-database/)[SQL](https://blog.cloudflare.com/tag/sql/)

[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[D1](https://blog.cloudflare.com/tag/d1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/tag/developer-week/)[Edge Database](https://blog.cloudflare.com/tag/edge-database/)[SQL](https://blog.cloudflare.com/tag/sql/)

April 10, 2025

# Sequential consistency without borders: how D1 implements global read replication

![Justin Mazzola Paluska](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462TBPQQQGVSNE4R1Q55M1.png&w=64&h=64&f=webp&fit=cover&position=center)![Lambros Petrou](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47WA9G46YD5HZY63QTNT9A.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Justin Mazzola Paluska](https://blog.cloudflare.com/author/justin-mazzola-paluska/) and [Lambros Petrou](https://blog.cloudflare.com/author/lambros-petrou/)

19 minute read

COPY URL

![BLOG-2733 Feature Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ADESEJPK73KY57K3T0NX.png&w=1999&h=1126&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////97+/y4OLs3+Tv5+z07fHy7e/r////////7O3z2d3s1N3w3Of15u707O7t////////6+z209ruy9jy0+P44ez37O/w////////7vD61t3zy9v20+X84u/87vP1////////9vf/4ef52eb83+//6/b/9Pj6////////////8fT/7fT/8vz/+P//+/7+/////////////v///f//////////////////////////////////////////////)

Read replication of [D1 databases](https://www.cloudflare.com/developer-platform/products/d1/) is in public beta!

D1 read replication makes read-only copies of your database available in multiple regions across Cloudflare’s network. For busy, read-heavy applications like e-commerce websites, content management tools, and mobile apps:

  * D1 read replication lowers average latency by routing user requests to read replicas in nearby regions.
  * D1 read replication increases overall throughput by offloading read queries to read replicas, allowing the primary database to handle more write queries.



The main copy of your database is called the primary database and the read-only copies are called read replicas. When you enable replication for a D1 database, the D1 service automatically creates and maintains read replicas of your primary database. As your users make requests, D1 routes those requests to an appropriate copy of the database (either the primary or a replica) based on performance heuristics, the type of queries made in those requests, and the query consistency needs as expressed by your application.

All of this global replica creation and request routing is handled by Cloudflare at no additional cost.

To take advantage of read replication, your Worker needs to use the new D1 [_Sessions API_](https://developers.cloudflare.com/d1/best-practices/read-replication/). Click the button below to run a Worker using D1 read replication with this [_code example_](https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api-template) to see for yourself!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api-template)

## D1 Sessions API

D1’s read replication feature is built around the concept of database _sessions_. A session encapsulates all the queries representing one logical session for your application. For example, a session might represent all requests coming from a particular web browser or all requests coming from a mobile app used by one of your users. If you use sessions, your queries will use the appropriate copy of the D1 database that makes the most sense for your request, be that the primary database or a nearby replica.

The sessions implementation ensures [_sequential consistency_](https://jepsen.io/consistency/models/sequential) for all queries in the session, no matter what copy of the database each query is routed to. The sequential consistency model has important properties like "[_read my own writes_](https://jepsen.io/consistency/models/read-your-writes)" and "[_writes follow reads_](https://jepsen.io/consistency/models/writes-follow-reads)," as well as a total ordering of writes. The total ordering of writes means that every replica will see transactions committed in the same order, which is exactly the behavior we want in a transactional system. Said another way, sequential consistency guarantees that the reads and writes are executed in the order in which you write them in your code.

Some examples of consistency implications in real-world applications:

  * You are using an online store and just placed an order (write query), followed by a visit to the account page to list all your orders (read query handled by a replica). You want the newly placed order to be listed there as well.
  * You are using your bank’s web application and make a transfer to your electricity provider (write query), and then immediately navigate to the account balance page (read query handled by a replica) to check the latest balance of your account, including that last payment.



Why do we need the Sessions API? Why can we not just query replicas directly?

Applications using D1 read replication need the Sessions API because D1 runs on Cloudflare’s global network and there’s no way to ensure that requests from the same client get routed to the same replica for every request. For example, the client may switch from WiFi to a mobile network in a way that changes how their requests are routed to Cloudflare. Or the data center that handled previous requests could be down because of an outage or maintenance.

D1’s read replication is asynchronous, so it’s possible that when you switch between replicas, the replica you switch to lags behind the replica you were using. This could mean that, for example, the new replica hasn’t learned of the writes you just completed. We could no longer guarantee useful properties like “read your own writes”. In fact, in the presence of shifty routing, the only consistency property we could guarantee is that what you read had been committed at some point in the past ([_read committed_](https://jepsen.io/consistency/models/read-committed) consistency), which isn’t very useful at all!

Since we can’t guarantee routing to the same replica, we flip the script and use the information we get from the Sessions API to make sure whatever replica we land on can handle the request in a sequentially-consistent manner.

Here’s what the Sessions API looks like in a Worker:
    
    
    export default {
      async fetch(request: Request, env: Env) {
        // A. Create the session.
        // When we create a D1 session, we can continue where we left off from a previous    
        // session if we have that session's last bookmark or use a constraint.
        const bookmark = request.headers.get('x-d1-bookmark') ?? 'first-unconstrained'
        const session = env.DB.withSession(bookmark)
    
        // Use this session for all our Workers' routes.
        const response = await handleRequest(request, session)
    
        // B. Return the bookmark so we can continue the session in another request.
        response.headers.set('x-d1-bookmark', session.getBookmark())
    
        return response
      }
    }
    
    async function handleRequest(request: Request, session: D1DatabaseSession) {
      const { pathname } = new URL(request.url)
    
      if (request.method === "GET" && pathname === '/api/orders') {
        // C. Session read query.
        const { results } = await session.prepare('SELECT * FROM Orders').all()
        return Response.json(results)
    
      } else if (request.method === "POST" && pathname === '/api/orders') {
        const order = await request.json<Order>()
    
        // D. Session write query.
        // Since this is a write query, D1 will transparently forward it to the primary.
        await session
          .prepare('INSERT INTO Orders VALUES (?, ?, ?)')
          .bind(order.orderId, order.customerId, order.quantity)
          .run()
    
        // E. Session read-after-write query.
        // In order for the application to be correct, this SELECT statement must see
        // the results of the INSERT statement above.
        const { results } = await session
          .prepare('SELECT * FROM Orders')
          .all()
    
        return Response.json(results)
      }
    
      return new Response('Not found', { status: 404 })
    }

To use the Session API, you first need to create a session using the `withSession` method (**_step A_**). The `withSession` method takes a bookmark as a parameter, or a constraint. The provided constraint instructs D1 where to forward the first query of the session. Using `first-unconstrained` allows the first query to be processed by any replica without any restriction on how up-to-date it is. Using `first-primary` ensures that the first query of the session will be forwarded to the primary.
    
    
    // A. Create the session.
    const bookmark = request.headers.get('x-d1-bookmark') ?? 'first-unconstrained'
    const session = env.DB.withSession(bookmark)

Providing an explicit bookmark instructs D1 that whichever database instance processes the query has to be at least as up-to-date as the provided bookmark (in case of a replica; the primary database is always up-to-date by definition). Explicit bookmarks are how we can continue from previously-created sessions and maintain sequential consistency across user requests.

Once you’ve created the session, make queries like you normally would with D1. The session object ensures that the queries you make are sequentially consistent with regards to each other.
    
    
    // C. Session read query.
    const { results } = await session.prepare('SELECT * FROM Orders').all()

For example, in the code example above, the session read query for listing the orders (**_step C_**) will return results that are at least as up-to-date as the bookmark used to create the session (_**step A**)_.

More interesting is the write query to add a new order (**_step D_**) followed by the read query to list all orders (**_step E_**). Because both queries are executed on the same session, it is guaranteed that the read query will observe a database copy that includes the write query, thus maintaining sequential consistency.
    
    
    // D. Session write query.
    await session
      .prepare('INSERT INTO Orders VALUES (?, ?, ?)')
      .bind(order.orderId, order.customerId, order.quantity)
      .run()
    
    // E. Session read-after-write query.
    const { results } = await session
      .prepare('SELECT * FROM Orders')
      .all()

Note that we could make a single batch query to the primary including both the write and the list, but the benefit of using the new Sessions API is that you can use the extra read replica databases for your read queries and allow the primary database to handle more write queries.

The session object does the necessary bookkeeping to maintain the latest bookmark observed across all queries executed using that specific session, and always includes that latest bookmark in requests to D1. Note that any query executed without using the session object is not guaranteed to be sequentially consistent with the queries executed in the session.

When possible, we suggest continuing sessions across requests by including bookmarks in your responses to clients (**_step B_**), and having clients passing previously received bookmarks in their future requests.
    
    
    // B. Return the bookmark so we can continue the session in another request.
    response.headers.set('x-d1-bookmark', session.getBookmark())

This allows _all_ of a client’s requests to be in the same session. You can do this by grabbing the session’s current bookmark at the end of the request (`session.getBookmark()`) and sending the bookmark in the response back to the client in HTTP headers, in HTTP cookies, or in the response body itself.

### Consistency with and without Sessions API

In this section, we will explore the classic scenario of a read-after-write query to showcase how using the new D1 Sessions API ensures that we get sequential consistency and avoid any issues with inconsistent results in our application.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2733 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44YXQCNMBY1FJ6ZHVSJB67.png&w=715&h=473&f=webp&fit=cover&position=center)

The Client, a user Worker, sends a D1 write query that gets processed by the database primary and gets the results back. However, the subsequent read query ends up being processed by a database replica. If the database replica is lagging far enough behind the database primary, such that it does not yet include the first write query, then the returned results will be inconsistent, and probably incorrect for your application business logic.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2733 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XPVA5B0H92NCQAJTRXSR.png&w=715&h=473&f=webp&fit=cover&position=center)

Using the Sessions API fixes the inconsistency issue. The first write query is again processed by the database primary, and this time the response includes “**Bookmark 100** ”. The session object will store this bookmark for you transparently.

The subsequent read query is processed by database replica as before, but now since the query includes the previously received “**Bookmark 100** ”, the database replica will wait until its database copy is at least up-to-date as “**Bookmark 100** ”. Only once it’s up-to-date, the read query will be processed and the results returned, including the replica’s latest bookmark “**Bookmark 104** ”.

Notice that the returned bookmark for the read query is “**Bookmark 104** ”, which is different from the one passed in the query request. This can happen if there were other writes from other client requests that also got replicated to the database replica in-between the two queries our own client executed.

## Enabling read replication

To start using D1 read replication:

  1. Update your Worker to use the D1 Sessions API to tell D1 what queries are part of the same database session. The Sessions API works with databases that do not have read replication enabled as well, so it’s safe to ship this code even before you enable replicas. Here’s [_an example_](http://developers.cloudflare.com/d1/best-practices/read-replication/).
  2. [_Enable replicas_](https://developers.cloudflare.com/d1/best-practices/read-replication/#enable-read-replication) for your database via [_Cloudflare dashboard_](https://dash.cloudflare.com/?to=/:account/workers/d1) > Select D1 database > Settings.



D1 read replication is built into D1, and you don’t pay extra storage or compute costs for replicas. You incur the exact same D1 usage with or without replicas, based on `rows_read` and `rows_written` by your queries. Unlike other traditional database systems with replication, you don’t have to manually create replicas, including where they run, or decide how to route requests between the primary database and read replicas. Cloudflare handles this when using the Sessions API while ensuring sequential consistency.

Since D1 read replication is in beta, we recommend trying D1 read replication on a non-production database first, and migrate to your production workloads after validating read replication works for your use case.

If you don’t have a D1 database and want to try out D1 read replication, [_create a test database_](https://dash.cloudflare.com/?to=/:account/workers/d1/create) in the Cloudflare dashboard.

### Observing your replicas

Once you’ve enabled D1 read replication, read queries will start to be processed by replica database instances. The response of each query includes information in the nested `meta` object relevant to read replication, like `served_by_region` and `served_by_primary`. The first denotes the region of the database instance that processed the query, and the latter will be `true` if-and-only-if your query was processed by the primary database instance.

In addition, the [_D1 dashboard overview_](https://dash.cloudflare.com/?to=/:account/workers/d1/) for a database now includes information about the database instances handling your queries. You can see how many queries are handled by the primary instance or by a replica, and a breakdown of the queries processed by region. The example screenshots below show graphs displaying the number of queries executed and number of rows read by each region.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2733 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CCS6QSA0ZEMQAT0Z9B8B.png&w=715&h=307&f=webp&fit=cover&position=center)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2733 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TRMA51N9GFTV2ZM126FE.png&w=715&h=307&f=webp&fit=cover&position=center)

## Under the hood: how D1 read replication is implemented

D1 is implemented on top of SQLite-backed Durable Objects running on top of Cloudflare’s [_Storage Relay Service_](https://blog.cloudflare.com/sqlite-in-durable-objects/#under-the-hood-storage-relay-service).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2733 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45X3MFWBN4NG0FE941QZVY.png&w=715&h=265&f=webp&fit=cover&position=center)

D1 is structured with a 3-layer architecture. First is the binding API layer that runs in the customer’s Worker. Next is a stateless Worker layer that routes requests based on database ID to a layer of Durable Objects that handle the actual SQL operations behind D1. This is similar to how [_most applications using Cloudflare Workers and Durable Objects are structured_](https://developers.cloudflare.com/durable-objects/what-are-durable-objects/#durable-objects-in-cloudflare).

For a non-replicated database, there is exactly one Durable Object per database. When a user’s Worker makes a request with the D1 binding for the database, that request is first routed to a D1 Worker running in the same location as the user’s Worker. The D1 Worker figures out which D1 Durable Object backs the user’s D1 database and fetches an RPC stub to that Durable Object. The Durable Objects routing layer figures out where the Durable Object is located, and opens an RPC connection to it. Finally, the D1 Durable Object then handles the query on behalf of the user’s Worker using the Durable Objects SQL API.

In the Durable Objects SQL API, all queries go to a SQLite database on the local disk of the server where the Durable Object is running. Durable Objects run [_SQLite in WAL mode_](https://www.sqlite.org/wal.html). In WAL mode, every write query appends to a write-ahead log (the WAL). As SQLite appends entries to the end of the WAL file, a database-specific component called the Storage Relay Service _leader_ synchronously replicates the entries to 5 _durability followers_ on servers in different datacenters. When a quorum (at least 3 out of 5) of the durability followers acknowledge that they have safely stored the data, the leader allows SQLite’s write queries to commit and opens the Durable Object’s output gate, so that the Durable Object can respond to requests.

Our implementation of WAL mode allows us to have a complete log of all of the committed changes to the database. This enables a couple of important features in SQLite-backed Durable Objects and D1:

  * We identify each write with a [_Lamport timestamp_](https://en.wikipedia.org/wiki/Lamport_timestamp) we call a [_bookmark_](https://developers.cloudflare.com/d1/reference/time-travel/#bookmarks).
  * We construct databases anywhere in the world by downloading all of the WAL entries from cold storage and replaying each WAL entry in order.
  * We implement [_Point-in-time recovery (PITR)_](https://developers.cloudflare.com/d1/reference/time-travel/) by replaying WAL entries up to a specific bookmark rather than to the end of the log.



Unfortunately, having the main data structure of the database be a log is not ideal. WAL entries are in write order, which is often neither convenient nor fast. In order to cut down on the overheads of the log, SQLite _checkpoints_ the log by copying the WAL entries back into the main database file. Read queries are serviced directly by SQLite using files on disk — either the main database file for checkpointed queries, or the WAL file for writes more recent than the last checkpoint. Similarly, the Storage Relay Service snapshots the database to cold storage so that we can replay a database by downloading the most recent snapshot and replaying the WAL from there, rather than having to download an enormous number of individual WAL entries.

WAL mode is the foundation for implementing read replication, since we can stream writes to locations other than cold storage in real time.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2733 Image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49F20C6451X1Q7X1NECJ30.png&w=715&h=458&f=webp&fit=cover&position=center)

We implemented read replication in 5 major steps.

First, we made it possible to make replica Durable Objects with a read-only copy of the database. These replica objects boot by fetching the latest snapshot and replaying the log from cold storage to whatever bookmark primary database’s leader last committed. This basically gave us point-in-time replicas, since without continuous updates, the replicas never updated until the Durable Object restarted.

Second, we registered the replica leader with the primary’s leader so that the primary leader sends the replicas every entry written to the WAL at the same time that it sends the WAL entries to the durability followers. Each of the WAL entries is marked with a bookmark that uniquely identifies the WAL entry in the sequence of WAL entries. We’ll use the bookmark later.

Note that since these writes are sent to the replicas _before_ a quorum of durability followers have confirmed them, the writes are actually unconfirmed writes, and the replica leader must be careful to keep the writes hidden from the replica Durable Object until they are confirmed. The replica leader in the Storage Relay Service does this by implementing enough of SQLite’s [_WAL-index protocol_](https://www.sqlite.org/walformat.html#the_wal_index_file_format), so that the unconfirmed writes coming from the primary leader look to SQLite as though it’s just another SQLite client doing unconfirmed writes. SQLite knows to ignore the writes until they are confirmed in the log. The upshot of this is that the replica leader can write WAL entries to the SQLite WAL _immediately,_ and then “commit” them when the primary leader tells the replica that the entries have been confirmed by durability followers.

One neat thing about this approach is that writes are sent from the primary to the replica as quickly as they are generated by the primary, helping to minimize lag between replicas. In theory, if the write query was proxied through a replica to the primary, the response back to the replica will arrive at almost the same time as the message that updates the replica. In such a case, it looks like there’s no replica lag at all!

In practice, we find that replication is really fast. Internally, we measure _confirm lag_ , defined as the time from when a primary confirms a change to when the replica confirms a change. The table below shows the confirm lag for two D1 databases whose primaries are in different regions.

  
Replica Region |  Database A (Primary region: ENAM) |  Database B  
(Primary region: WNAM)  
---|---|---  
ENAM |  N/A |  30 ms  
WNAM |  45 ms |  N/A  
WEUR |  55 ms |  75 ms  
EEUR |  67 ms |  75 ms  
  
_Confirm lag for 2 replicated databases. N/A means that we have no data for this combination. The region abbreviations are the same ones used for[ _Durable Object location hints_](https://developers.cloudflare.com/durable-objects/reference/data-location/#supported-locations-1)._

The table shows that confirm lag is correlated with the network round-trip time between the data centers hosting the primary databases and their replicas. This is clearly visible in the difference between the confirm lag for the European replicas of the two databases. As airline route planners know, EEUR is [_appreciably further away_](http://www.gcmap.com/mapui?P=ewr-lhr,+ewr-waw) from ENAM than WEUR is, but from WNAM, both European regions (WEUR and EEUR) are [_about equally as far away_](http://www.gcmap.com/mapui?P=sjc-lhr,+sjc-waw). We see that in our replication numbers.

The exact placement of the D1 database in the region matters too. Regions like ENAM and WNAM are quite large in themselves. Database A’s placement in ENAM happens to be further away from most data centers in WNAM compared to database B’s placement in WNAM relative to the ENAM data centers. As such, database B sees slightly lower confirm lag.

Try as we might, we can’t beat the speed of light!

Third, we updated the Durable Object routing system to be aware of Durable Object replicas. When read replication is enabled on a Durable Object, two things happen. First, we create a set of replicas according to a replication policy. The current replication policy that D1 uses is simple: a static set of replicas in [_every region that D1 supports_](https://developers.cloudflare.com/d1/configuration/data-location/#available-location-hints). Second, we turn on a routing policy for the Durable Object. The current policy that D1 uses is also simple: route to the Durable Object replica in the region close to where the user request is. With this step, we have updateable read-only replicas, and can route requests to them!

Fourth, we updated D1’s Durable Object code to handle write queries on replicas. D1 uses SQLite to figure out whether a request is a write query or a read query. This means that the determination of whether something is a read or write query happens _after_ the request is routed. Read replicas will have to handle write requests! We solve this by instantiating each replica D1 Durable Object with a reference to its primary. If the D1 Durable Object determines that the query is a write query, it forwards the request to the primary for the primary to handle. This happens transparently, keeping the user code simple.

As of this fourth step, we can handle read and write queries at every copy of the D1 Durable Object, whether it's a primary or not. Unfortunately, as outlined above, if a user's requests get routed to different read replicas, they may see different views of the database, leading to a very weak consistency model. So the last step is to implement the Sessions API across the D1 Worker and D1 Durable Object. Recall that every WAL entry is marked with a bookmark. These bookmarks uniquely identify a point in (logical) time in the database. Our bookmarks are strictly monotonically increasing; every write to a database makes a new bookmark with a value greater than any other bookmark for that database.

Using bookmarks, we implement the Sessions API with the following algorithm split across the D1 binding implementation, the D1 Worker, and D1 Durable Object.

First up in the D1 binding, we have code that creates the `D1DatabaseSession` object and code within the `D1DatabaseSession` object to keep track of the latest bookmark.
    
    
    // D1Binding is the binding code running within the user's Worker
    // that provides the existing D1 Workers API and the new withSession method.
    class D1Binding {
      // Injected by the runtime to the D1 Binding.
      d1Service: D1ServiceBinding
    
      function withSession(initialBookmark) {
        return D1DatabaseSession(this.d1Service, this.databaseId, initialBookmark);
      }
    }
    
    // D1DatabaseSession holds metadata about the session, most importantly the
    // latest bookmark we know about for this session.
    class D1DatabaseSession {
      constructor(d1Service, databaseId, initialBookmark) {
        this.d1Service = d1Service;
        this.databaseId = databaseId;
        this.bookmark = initialBookmark;
      }
    
      async exec(query) {
        // The exec method in the binding sends the query to the D1 Worker
        // and waits for the the response, updating the bookmark as
        // necessary so that future calls to exec use the updated bookmark.
        var resp = await this.d1Service.handleUserQuery(databaseId, query, bookmark);
        if (isNewerBookmark(this.bookmark, resp.bookmark)) {
          this.bookmark = resp.bookmark;
        }
        return resp;
      }
    
      // batch and other SQL APIs are implemented similarly.
    }

The binding code calls into the D1 stateless Worker (`d1Service` in the snippet above), which figures out which Durable Object to use, and proxies the request to the Durable Object.
    
    
    class D1Worker {
      async handleUserQuery(databaseId, query) {
        var doId = /* look up Durable Object for databaseId */;
        return await this.D1_DO.get(doId).handleWorkerQuery(query, bookmark)
      }
    }

Finally, we reach the Durable Objects layer, which figures out how to actually handle the request.
    
    
    class D1DurableObject {
      async handleWorkerQuery(queries, bookmark) {
        var bookmark = bookmark ?? "first-primary";
        var results = {};
    
        if (this.isPrimaryDatabase()) {
          // The primary always has the latest data so we can run the
          // query without checking the bookmark.
          var result = /* execute query directly */;
          bookmark = getCurrentBookmark();
          results = result;
        } else {
          // This is running on a replica.
          if (bookmark === "first-primary" || isWriteQuery(query)) {
            // The primary must handle this request, so we'll proxy the
            // request to the primary.
            var resp = await this.primary.handleWorkerQuery(query, bookmark);
            bookmark = resp.bookmark;
            results = resp.results;
          } else {
            // The replica can handle this request, but only after the
            // database is up-to-date with the bookmark.
            if (bookmark !== "first-unconstrained") {
              await waitForBookmark(bookmark);
            }
            var result = /* execute query locally */;
            bookmark = getCurrentBookmark();
            results = result;
          }
        }
        return { results: results, bookmark: bookmark };
      }
    }

The D1 Durable Object first figures out if this instance can handle the query, or if the query needs to be sent to the primary. If the Durable Object can execute the query, it ensures that we execute the query with a bookmark at least as up-to-date as the bookmark requested by the binding.

The upshot is that the three pieces of code work together to ensure that all of the queries in the session see the database in a sequentially consistent order, because each new query will be blocked until it has seen the results of previous queries within the same session.

## Conclusion

D1’s new read replication feature is a significant step towards making globally distributed databases easier to use without sacrificing consistency. With automatically provisioned replicas in every region, your applications can now serve read queries faster while maintaining strong sequential consistency across requests, and keeping your application Worker code simple.

We’re excited for developers to explore this feature and see how it improves the performance of your applications. The public beta is just the beginning—we’re actively refining and expanding D1’s capabilities, including evolving replica placement policies, and your feedback will help shape what’s next.

Note that the Sessions API is only available through the [_D1 Worker Binding_](https://developers.cloudflare.com/d1/worker-api/) for now, and support for the HTTP REST API will follow soon.

Try out D1 read replication today by clicking the “Deploy to Cloudflare" button, check out [_documentation and examples_](http://developers.cloudflare.com/d1/best-practices/read-replication/), and let us know what you build in the [_D1 Discord channel_](https://discord.com/channels/595317990191398933/992060581832032316)!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api-template)

On this page

Discuss Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fd1-read-replication-beta%2F&t=Sequential%20consistency%20without%20borders%3A%20how%20D1%20implements%20global%20read%20replication)[](https://x.com/intent/post?text=Sequential+consistency+without+borders%3A+how+D1+implements+global+read+replication&url=https%3A%2F%2Fblog.cloudflare.com%2Fd1-read-replication-beta%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fd1-read-replication-beta%2F)[](https://bsky.app/intent/compose?text=Sequential+consistency+without+borders%3A+how+D1+implements+global+read+replication+https%3A%2F%2Fblog.cloudflare.com%2Fd1-read-replication-beta%2F)[](https://mastodonshare.com/?text=Sequential+consistency+without+borders%3A+how+D1+implements+global+read+replication&url=https%3A%2F%2Fblog.cloudflare.com%2Fd1-read-replication-beta%2F)[](https://www.threads.net/intent/post?text=Sequential+consistency+without+borders%3A+how+D1+implements+global+read+replication+https%3A%2F%2Fblog.cloudflare.com%2Fd1-read-replication-beta%2F)

## Related tags

[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[D1](https://blog.cloudflare.com/tag/d1/)[Deep Dive](https://blog.cloudflare.com/tag/deep-dive/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developer Week](https://blog.cloudflare.com/tag/developer-week/)[Edge Database](https://blog.cloudflare.com/tag/edge-database/)[SQL](https://blog.cloudflare.com/tag/sql/)

Follow on Social Media

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.
