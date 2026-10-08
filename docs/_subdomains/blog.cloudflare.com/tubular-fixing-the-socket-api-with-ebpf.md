---
url: https://blog.cloudflare.com/tubular-fixing-the-socket-api-with-ebpf/
title: Production ready eBPF, or how we fixed the BSD socket API | Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:55:40.804394+00:00
---

# Production ready eBPF, or how we fixed the BSD socket API | Cloudflare Blog

> Source: https://blog.cloudflare.com/tubular-fixing-the-socket-api-with-ebpf/

[Blog](https://blog.cloudflare.com/)

[eBPF](https://blog.cloudflare.com/tag/ebpf/)[Go](https://blog.cloudflare.com/tag/go/)[Linux](https://blog.cloudflare.com/tag/linux/)

3 TagsShow 3 tags

  * Post Tags
  * [eBPF](https://blog.cloudflare.com/tag/ebpf/)[Go](https://blog.cloudflare.com/tag/go/)[Linux](https://blog.cloudflare.com/tag/linux/)
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



[eBPF](https://blog.cloudflare.com/tag/ebpf/)[Go](https://blog.cloudflare.com/tag/go/)[Linux](https://blog.cloudflare.com/tag/linux/)

February 17, 2022

# Production ready eBPF, or how we fixed the BSD socket API

![Lorenz Bauer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VA693P7KJCJ0XQB6BJ93.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Lorenz Bauer](https://blog.cloudflare.com/author/lorenz-bauer/)

13 minute read

COPY URL

![BLOG-990 Embedded Image - yJC2F5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46AQK0CX5CFJVS8G26A9D8.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAjls4jVtAi11OjF9Xjl9Xj15SjFxKhlpFkFs+kmFLl29in3pxo350oXlrl21di2BOkltEl2dVo35xr5CFtpWJsY5/o3trkGZWlVxGm2pYqYV3uJmMvp+RuZeHqYJxlGlYmF5EnWpUqYJxtZSEu5qJt5OAqH9slmhUmmA+nGdKondgqoRwr4l0rYNtonVdlWVLm2E4m2Q/m2pMnXBWoHNZoHFVm2lLlGFAnGE1mmI5mGRBl2ZImWhKm2dImGRCk187)

As we develop new products, we often push our operating system - Linux - beyond what is commonly possible. A common theme has been relying on [eBPF](https://ebpf.io/what-is-ebpf/) to build technology that would otherwise have required modifying the kernel. For example, we’ve built [DDoS mitigation](https://blog.cloudflare.com/l4drop-xdp-ebpf-based-ddos-mitigations/) and a [load balancer](https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/) and use it to [monitor our fleet of servers](https://blog.cloudflare.com/introducing-ebpf_exporter/).

This software usually consists of a small-ish eBPF program written in C, executed in the context of the kernel, and a larger user space component that loads the eBPF into the kernel and manages its lifecycle. We’ve found that the ratio of eBPF code to userspace code differs by an order of magnitude or more. We want to shed some light on the issues that a developer has to tackle when dealing with eBPF and present our solutions for building rock-solid production ready applications which contain eBPF.

For this purpose we are open sourcing the production tooling we’ve built for the [sk_lookup hook](https://www.kernel.org/doc/html/latest/bpf/prog_sk_lookup.html) we contributed to the Linux kernel, called **tubular**. It exists because [we’ve outgrown the BSD sockets API](https://blog.cloudflare.com/its-crowded-in-here/). To deliver some products we need features that are just not possible using the standard API.

  * Our services are available on millions of IPs.
  * Multiple services using the same port on different addresses have to coexist, e.g. [1.1.1.1](https://1.1.1.1/) resolver and our authoritative DNS.
  * Our Spectrum product [needs to listen on all 2^16 ports](https://blog.cloudflare.com/how-we-built-spectrum/).



The source code for tubular is at <https://github.com/cloudflare/tubular>, and it allows you to do all the things mentioned above. Maybe the most interesting feature is that you can change the addresses of a service on the fly:

## How tubular works

`tubular` sits at a critical point in the Cloudflare stack, since it has to inspect every connection terminated by a server and decide which application should receive it.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-990 Embedded Image - u8FZMO](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487QP72JESZQZ4Y8JBR2DZ.png&w=715&h=171&f=webp&fit=cover&position=center)

Failure to do so will drop or misdirect connections hundreds of times per second. So it has to be incredibly robust during day to day operations. We had the following goals for tubular:

  * **Releases must be unattended and happen online.** tubular runs on thousands of machines, so we can’t babysit the process or take servers out of production.
  * **Releases must fail safely.** A failure in the process must leave the previous version of tubular running, otherwise we may drop connections.
  * **Reduce the impact of (userspace) crashes.** When the inevitable bug comes along we want to minimise the blast radius.



In the past we had built a proof-of-concept control plane for sk_lookup called [inet-tool](https://github.com/majek/inet-tool), which proved that we could get away without a persistent service managing the eBPF. Similarly, tubular has `tubectl`: short-lived invocations make the necessary changes and persisting state is handled by the kernel in the form of [eBPF maps](https://www.kernel.org/doc/html/latest/bpf/maps.html). Following this design gave us crash resiliency by default, but left us with the task of mapping the user interface we wanted to the tools available in the eBPF ecosystem.

## The tubular user interface

tubular consists of a BPF program that attaches to the sk_lookup hook in the kernel and userspace Go code which manages the BPF program. The `tubectl` command wraps both in a way that is easy to distribute.

`tubectl` manages two kinds of objects: bindings and sockets. A binding encodes a rule against which an incoming packet is matched. A socket is a reference to a TCP or UDP socket that can accept new connections or packets.

Bindings and sockets are "glued" together via arbitrary strings called labels. Conceptually, a binding assigns a label to some traffic. The label is then used to find the correct socket.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-990 Embedded Image - qM2Z52](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WWMWHBF5VDKPBDFKPQ2H.png&w=715&h=117&f=webp&fit=cover&position=center)

### Adding bindings

To create a binding that steers port 80 (aka HTTP) traffic destined for 127.0.0.1 to the label “foo” we use `tubectl bind`:
    
    
    $ sudo tubectl bind "foo" tcp 127.0.0.1 80

Due to the power of sk_lookup we can have much more powerful constructs than the BSD API. For example, we can redirect connections to all IPs in 127.0.0.0/24 to a single socket:
    
    
    $ sudo tubectl bind "bar" tcp 127.0.0.0/24 80

A side effect of this power is that it's possible to create bindings that "overlap":
    
    
    1: tcp 127.0.0.1/32 80 -> "foo"
    2: tcp 127.0.0.0/24 80 -> "bar"

The first binding says that HTTP traffic to localhost should go to “foo”, while the second asserts that HTTP traffic in the localhost subnet should go to “bar”. This creates a contradiction, which binding should we choose? tubular resolves this by defining precedence rules for bindings:

  1. A prefix with a longer mask is more specific, e.g. 127.0.0.1/32 wins over 127.0.0.0/24.
  2. A port is more specific than the port wildcard, e.g. port 80 wins over "all ports" (0).



Applying this to our example, HTTP traffic to all IPs in 127.0.0.0/24 will be directed to bar, except for 127.0.0.1 which goes to foo.

### Getting ahold of sockets

`sk_lookup` needs a reference to a TCP or a UDP socket to redirect traffic to it. However, a socket is usually accessible only by the process which created it with the socket syscall. For example, an HTTP server creates a TCP listening socket bound to port 80. How can we gain access to the listening socket?

A fairly well known solution is to make processes cooperate by passing socket file descriptors via [SCM_RIGHTS](https://blog.cloudflare.com/know-your-scm_rights/) messages to a tubular daemon. That daemon can then take the necessary steps to hook up the socket with `sk_lookup`. This approach has several drawbacks:

  1. Requires modifying processes to send SCM_RIGHTS
  2. Requires a tubular daemon, which may crash



There is another way of getting at sockets by using systemd, provided [socket activation](https://www.freedesktop.org/software/systemd/man/systemd.socket.html) is used. It works by creating an additional service unit with the correct [Sockets](https://www.freedesktop.org/software/systemd/man/systemd.service.html#Sockets=) setting. In other words: we can leverage systemd oneshot action executed on creation of a systemd socket service, registering the socket into tubular. For example:
    
    
    [Unit]
    Requisite=foo.socket
    
    [Service]
    Type=oneshot
    Sockets=foo.socket
    ExecStart=tubectl register "foo"

Since we can rely on systemd to execute `tubectl` at the correct times we don't need a daemon of any kind. However, the reality is that a lot of popular software doesn't use systemd socket activation. Dealing with systemd sockets is complicated and doesn't invite experimentation. Which brings us to the final trick: [pidfd_getfd](https://www.man7.org/linux/man-pages/man2/pidfd_getfd.2.html):

> The `pidfd_getfd()` system call allocates a new file descriptor in the calling process. This new file descriptor is a duplicate of an existing file descriptor, targetfd, in the process referred to by the PID file descriptor pidfd.

We can use it to iterate all file descriptors of a foreign process, and pick the socket we are interested in. To return to our example, we can use the following command to find the TCP socket bound to 127.0.0.1 port 8080 in the httpd process and register it under the "foo" label:
    
    
    $ sudo tubectl register-pid "foo" $(pidof httpd) tcp 127.0.0.1 8080

It's easy to wire this up using systemd's [ExecStartPost](https://www.freedesktop.org/software/systemd/man/systemd.service.html#ExecStartPre=) if the need arises.
    
    
    [Service]
    Type=forking # or notify
    ExecStart=/path/to/some/command
    ExecStartPost=tubectl register-pid $MAINPID foo tcp 127.0.0.1 8080

## Storing state in eBPF maps

As mentioned previously, tubular relies on the kernel to store state, using [BPF key / value data structures also known as maps](https://prototype-kernel.readthedocs.io/en/latest/bpf/ebpf_maps.html). Using the [BPF_OBJ_PIN syscall](https://www.kernel.org/doc/html/latest/userspace-api/ebpf/syscall.html) we can persist them in /sys/fs/bpf:
    
    
    /sys/fs/bpf/4026532024_dispatcher
    ├── bindings
    ├── destination_metrics
    ├── destinations
    ├── sockets
    └── ...

The way the state is structured differs from how the command line interface presents it to users. Labels like “foo” are convenient for humans, but they are of variable length. Dealing with variable length data in BPF is cumbersome and slow, so the BPF program never references labels at all. Instead, the user space code allocates numeric IDs, which are then used in the BPF. Each ID represents a (`label`, `domain`, `protocol`) tuple, internally called `destination`.

For example, adding a binding for "foo" `tcp 127.0.0.1` ... allocates an ID for ("`foo`", `AF_INET`, `TCP`). Including domain and protocol in the destination allows simpler data structures in the BPF. Each allocation also tracks how many bindings reference a destination so that we can recycle unused IDs. This data is persisted into the destinations hash table, which is keyed by (Label, Domain, Protocol) and contains (ID, Count). Metrics for each destination are tracked in destination_metrics in the form of per-CPU counters.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-990 Embedded Image - xJHxwS](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47BVCKPFCAHK07PP9DB4ZR.png&w=715&h=238&f=webp&fit=cover&position=center)

`bindings` is a [longest prefix match (LPM) trie](https://en.wikipedia.org/wiki/Trie) which stores a mapping from (`protocol`, `port`, `prefix`) to (`ID`, `prefix length`). The ID is used as a key to the sockets map which contains pointers to kernel socket structures. IDs are allocated in a way that makes them suitable as an array index, which allows using the simpler BPF sockmap (an array) instead of a socket hash table. The prefix length is duplicated in the value to work around shortcomings in the BPF API.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-990 Embedded Image - SYzNUi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K9TR96AQDHR1SY3RXQRW.png&w=715&h=423&f=webp&fit=cover&position=center)

## Encoding the precedence of bindings

As discussed, bindings have a precedence associated with them. To repeat the earlier example:
    
    
    1: tcp 127.0.0.1/32 80 -> "foo"
    2: tcp 127.0.0.0/24 80 -> "bar"

The first binding should be matched before the second one. We need to encode this in the BPF somehow. One idea is to generate some code that executes the bindings in order of specificity, a technique we’ve used to great effect in [l4drop](https://blog.cloudflare.com/l4drop-xdp-ebpf-based-ddos-mitigations/):
    
    
    1: if (mask(ip, 32) == 127.0.0.1) return "foo"
    2: if (mask(ip, 24) == 127.0.0.0) return "bar"
    ...

This has the downside that the program gets longer the more bindings are added, which slows down execution. It's also difficult to introspect and debug such long programs. Instead, we use a specialised BPF longest prefix match (LPM) map to do the hard work. This allows inspecting the contents from user space to figure out which bindings are active, which is very difficult if we had compiled bindings into BPF. The LPM map uses a trie behind the scenes, so [lookup has complexity proportional to the length of the key](https://en.wikipedia.org/wiki/Trie#Searching) instead of linear complexity for the “naive” solution.

However, using a map requires a trick for encoding the precedence of bindings into a key that we can look up. Here is a simplified version of this encoding, which ignores IPv6 and uses labels instead of IDs. To insert the binding `tcp 127.0.0.0/24 80` into a trie we first convert the IP address into a number.
    
    
    127.0.0.0    = 0x7f 00 00 00

Since we're only interested in the first 24 bits of the address we, can write the whole prefix as
    
    
    127.0.0.0/24 = 0x7f 00 00 ??

where “?” means that the value is not specified. We choose the number 0x01 to represent TCP and prepend it and the port number (80 decimal is 0x50 hex) to create the full key:
    
    
    tcp 127.0.0.0/24 80 = 0x01 50 7f 00 00 ??

Converting `tcp 127.0.0.1/32 80` happens in exactly the same way. Once the converted values are inserted into the trie, the LPM trie conceptually contains the following keys and values.
    
    
    LPM trie:
            0x01 50 7f 00 00 ?? = "bar"
            0x01 50 7f 00 00 01 = "foo"

To find the binding for a TCP packet destined for 127.0.0.1:80, we again encode a key and perform a lookup.
    
    
    input:  0x01 50 7f 00 00 01   TCP packet to 127.0.0.1:80
    ---------------------------
    LPM trie:
            0x01 50 7f 00 00 ?? = "bar"
               y  y  y  y  y
            0x01 50 7f 00 00 01 = "foo"
               y  y  y  y  y  y
    ---------------------------
    result: "foo"
    
    y = byte matches

The trie returns “foo” since its key shares the longest prefix with the input. Note that we stop comparing keys once we reach unspecified “?” bytes, but conceptually “bar” is still a valid result. The distinction becomes clear when looking up the binding for a TCP packet to 127.0.0.255:80.
    
    
    input:  0x01 50 7f 00 00 ff   TCP packet to 127.0.0.255:80
    ---------------------------
    LPM trie:
            0x01 50 7f 00 00 ?? = "bar"
               y  y  y  y  y
            0x01 50 7f 00 00 01 = "foo"
               y  y  y  y  y  n
    ---------------------------
    result: "bar"
    
    n = byte doesn't match

In this case "foo" is discarded since the last byte doesn't match the input. However, "bar" is returned since its last byte is unspecified and therefore considered to be a valid match.

## Observability with minimal privileges

Linux has the powerful ss tool (part of iproute2) available to inspect socket state:
    
    
    $ ss -tl src 127.0.0.1
    State      Recv-Q      Send-Q           Local Address:Port           Peer Address:Port
    LISTEN     0           128                  127.0.0.1:ipp                 0.0.0.0:*

With tubular in the picture this output is not accurate anymore. `tubectl` bindings makes up for this shortcoming:
    
    
    $ sudo tubectl bindings tcp 127.0.0.1
    Bindings:
     protocol       prefix port label
          tcp 127.0.0.1/32   80   foo

Running this command requires super-user privileges, despite in theory being safe for any user to run. While this is acceptable for casual inspection by a human operator, it's a dealbreaker for observability via pull-based monitoring systems like Prometheus. The usual approach is to expose metrics via an HTTP server, which would have to run with elevated privileges and be accessible to the Prometheus server somehow. Instead, BPF gives us the tools to enable read-only access to tubular state with minimal privileges.

The key is to carefully set file ownership and mode for state in /sys/fs/bpf. Creating and opening files in /sys/fs/bpf uses [BPF_OBJ_PIN and BPF_OBJ_GET](https://www.kernel.org/doc/html/latest/userspace-api/ebpf/syscall.html#bpf-subcommand-reference). Calling BPF_OBJ_GET with BPF_F_RDONLY is roughly equivalent to open(O_RDONLY) and allows accessing state in a read-only fashion, provided the file permissions are correct. tubular gives the owner full access but restricts read-only access to the group:
    
    
    $ sudo ls -l /sys/fs/bpf/4026532024_dispatcher | head -n 3
    total 0
    -rw-r----- 1 root root 0 Feb  2 13:19 bindings
    -rw-r----- 1 root root 0 Feb  2 13:19 destination_metrics

It's easy to choose which user and group should own state when loading tubular:
    
    
    $ sudo -u root -g tubular tubectl load
    created dispatcher in /sys/fs/bpf/4026532024_dispatcher
    loaded dispatcher into /proc/self/ns/net
    $ sudo ls -l /sys/fs/bpf/4026532024_dispatcher | head -n 3
    total 0
    -rw-r----- 1 root tubular 0 Feb  2 13:42 bindings
    -rw-r----- 1 root tubular 0 Feb  2 13:42 destination_metrics

There is one more obstacle, [systemd mounts /sys/fs/bpf](https://github.com/systemd/systemd/blob/b049b48c4b6e60c3cbec9d2884f90fd4e7013219/src/shared/mount-setup.c#L111-L112) in a way that makes it inaccessible to anyone but root. Adding the executable bit to the directory fixes this.
    
    
    $ sudo chmod -v o+x /sys/fs/bpf
    mode of '/sys/fs/bpf' changed from 0700 (rwx------) to 0701 (rwx-----x)

Finally, we can export metrics without privileges:
    
    
    $ sudo -u nobody -g tubular tubectl metrics 127.0.0.1 8080
    Listening on 127.0.0.1:8080
    ^C

There is a caveat, unfortunately: truly unprivileged access requires unprivileged BPF to be enabled. Many distros have taken to disabling it via the unprivileged_bpf_disabled sysctl, in which case scraping metrics does require CAP_BPF.

## Safe releases

tubular is distributed as a single binary, but really consists of two pieces of code with widely differing lifetimes. The BPF program is loaded into the kernel once and then may be active for weeks or months, until it is explicitly replaced. In fact, a reference to the program (and link, see below) is persisted into /sys/fs/bpf:
    
    
    /sys/fs/bpf/4026532024_dispatcher
    ├── link
    ├── program
    └── ...

The user space code is executed for seconds at a time and is replaced whenever the binary on disk changes. This means that user space has to be able to deal with an "old" BPF program in the kernel somehow. The simplest way to achieve this is to compare what is loaded into the kernel with the BPF shipped as part of tubectl. If the two don't match we return an error:
    
    
    $ sudo tubectl bind foo tcp 127.0.0.1 80
    Error: bind: can't open dispatcher: loaded program #158 has differing tag: "938c70b5a8956ff2" doesn't match "e007bfbbf37171f0"

`tag` is the truncated hash of the instructions making up a BPF program, which the kernel makes available for every loaded program:
    
    
    $ sudo bpftool prog list id 158
    158: sk_lookup  name dispatcher  tag 938c70b5a8956ff2
    ...

By comparing the tag tubular asserts that it is dealing with a supported version of the BPF program. Of course, just returning an error isn't enough. There needs to be a way to update the kernel program so that it's once again safe to make changes. This is where the persisted link in /sys/fs/bpf comes into play. `bpf_links` are used to attach programs to various BPF hooks. "Enabling" a BPF program is a two-step process: first, load the BPF program, next attach it to a hook using a bpf_link. Afterwards the program will execute the next time the hook is executed. By updating the link we can change the program on the fly, in an atomic manner.
    
    
    $ sudo tubectl upgrade
    Upgraded dispatcher to 2022.1.0-dev, program ID #159
    $ sudo bpftool prog list id 159
    159: sk_lookup  name dispatcher  tag e007bfbbf37171f0
    …
    $ sudo tubectl bind foo tcp 127.0.0.1 80
    bound foo#tcp:[127.0.0.1/32]:80

Behind the scenes the upgrade procedure is slightly more complicated, since we have to update the pinned program reference in addition to the link. We pin the new program into /sys/fs/bpf:
    
    
    /sys/fs/bpf/4026532024_dispatcher
    ├── link
    ├── program
    ├── program-upgrade
    └── ...

Once the link is updated we [atomically rename](https://www.man7.org/linux/man-pages/man2/rename.2.html) program-upgrade to replace program. In the future we may be able to [use RENAME_EXCHANGE](https://lkml.kernel.org/netdev/20211028094724.59043-5-lmb@cloudflare.com/t/) to make upgrades even safer.

## Preventing state corruption

So far we’ve completely neglected the fact that multiple invocations of `tubectl` could modify the state in /sys/fs/bpf at the same time. It’s very hard to reason about what would happen in this case, so in general it’s best to prevent this from ever occurring. A common solution to this is [advisory file locks](https://gavv.github.io/articles/file-locks/#differing-features). Unfortunately it seems like BPF maps don't support locking.
    
    
    $ sudo flock /sys/fs/bpf/4026532024_dispatcher/bindings echo works!
    flock: cannot open lock file /sys/fs/bpf/4026532024_dispatcher/bindings: Input/output error

This led to a bit of head scratching on our part. Luckily it is possible to flock the directory instead of individual maps:
    
    
    $ sudo flock --exclusive /sys/fs/bpf/foo echo works!
    works!

Each `tubectl` invocation likewise invokes [`flock()`](https://www.man7.org/linux/man-pages//man2/flock.2.html), thereby guaranteeing that only ever a single process is making changes.

## Conclusion

tubular is in production at Cloudflare today and has simplified the deployment of [Spectrum](https://www.cloudflare.com/products/cloudflare-spectrum/) and our [authoritative DNS](https://www.cloudflare.com/dns/). It allowed us to leave behind limitations of the BSD socket API. However, its most powerful feature is that [the addresses a service is available on can be changed on the fly](https://research.cloudflare.com/publications/Fayed2021/). In fact, we have built tooling that automates this process across our global network. Need to listen on another million IPs on thousands of machines? No problem, it’s just an HTTP POST away.

_Interested in working on tubular and our L4 load balancer_ _[unimog](https://blog.cloudflare.com/unimog-cloudflares-edge-load-balancer/)? We are_ _[hiring in our European offices](https://boards.greenhouse.io/cloudflare/jobs/3232234?gh_jid=3232234)._

On this page

Discuss Online

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Ftubular-fixing-the-socket-api-with-ebpf%2F&t=Production%20ready%20eBPF%2C%20or%20how%20we%20fixed%20the%20BSD%20socket%20API)[](https://x.com/intent/post?text=Production+ready+eBPF%2C+or+how+we+fixed+the+BSD+socket+API&url=https%3A%2F%2Fblog.cloudflare.com%2Ftubular-fixing-the-socket-api-with-ebpf%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Ftubular-fixing-the-socket-api-with-ebpf%2F)[](https://bsky.app/intent/compose?text=Production+ready+eBPF%2C+or+how+we+fixed+the+BSD+socket+API+https%3A%2F%2Fblog.cloudflare.com%2Ftubular-fixing-the-socket-api-with-ebpf%2F)[](https://mastodonshare.com/?text=Production+ready+eBPF%2C+or+how+we+fixed+the+BSD+socket+API&url=https%3A%2F%2Fblog.cloudflare.com%2Ftubular-fixing-the-socket-api-with-ebpf%2F)[](https://www.threads.net/intent/post?text=Production+ready+eBPF%2C+or+how+we+fixed+the+BSD+socket+API+https%3A%2F%2Fblog.cloudflare.com%2Ftubular-fixing-the-socket-api-with-ebpf%2F)

## Related tags

[eBPF](https://blog.cloudflare.com/tag/ebpf/)[Go](https://blog.cloudflare.com/tag/go/)[Linux](https://blog.cloudflare.com/tag/linux/)

Follow on Social Media

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.
