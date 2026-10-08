---
url: https://blog.cloudflare.com/de-de/workers-production-safety/
title: Neue Tools f\u00fcr die Produktionssicherheit \u2014 Gradual Deployments, Source Maps, Rate Limiting und neue SDKs | Der Cloudflare-Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:29.119325+00:00
---

# Neue Tools für die Produktionssicherheit — Gradual Deployments, Source Maps, Rate Limiting und neue SDKs | Der Cloudflare-Blog

> Source: https://blog.cloudflare.com/de-de/workers-production-safety/

[Blog](https://blog.cloudflare.com/de-de/)

[Cloudflare Workers](https://blog.cloudflare.com/de-de/tag/workers/)[Developer Week](https://blog.cloudflare.com/de-de/tag/developer-week/)[Observability](https://blog.cloudflare.com/de-de/tag/observability/)+22 weitere Tags anzeigen

5 Tags5 Tags anzeigen

  * Beitragstags
  * [Cloudflare Workers](https://blog.cloudflare.com/de-de/tag/workers/)[Developer Week](https://blog.cloudflare.com/de-de/tag/developer-week/)[Rate Limiting (DE)](https://blog.cloudflare.com/de-de/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/de-de/tag/sdk/)
  * Alle Tags
  * Passende Tags
  * Keine Tags gefunden
  * [1.1.1.1](https://blog.cloudflare.com/de-de/tag/1-1-1-1/)
  * [Übernahmen](https://blog.cloudflare.com/de-de/tag/acquisitions/)
  * [Erweiterte DDoS-Abwehr](https://blog.cloudflare.com/de-de/tag/advanced-ddos/)
  * [Agententauglichkeit](https://blog.cloudflare.com/de-de/tag/agent-readiness/)
  * [Agents](https://blog.cloudflare.com/de-de/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/de-de/tag/agents-week/)
  * [AI](https://blog.cloudflare.com/de-de/tag/ai/)
  * [AI Bots (DE)](https://blog.cloudflare.com/de-de/tag/ai-bots/)
  * [AI Gateway (DE)](https://blog.cloudflare.com/de-de/tag/ai-gateway/)
  * [KI-Suche](https://blog.cloudflare.com/de-de/tag/ai-search/)
  * [AI Week](https://blog.cloudflare.com/de-de/tag/ai-week/)
  * [Verwaltung der Sicherheitsvorkehrungen für KI](https://blog.cloudflare.com/de-de/tag/ai-spm/)
  * [Always Online (DE)](https://blog.cloudflare.com/de-de/tag/always-online/)
  * [AMD (DE)](https://blog.cloudflare.com/de-de/tag/amd/)
  * [Analysen](https://blog.cloudflare.com/de-de/tag/analytics/)
  * [Anonymous (DE)](https://blog.cloudflare.com/de-de/tag/anonymous/)
  * [Anycast (DE)](https://blog.cloudflare.com/de-de/tag/anycast/)
  * [API](https://blog.cloudflare.com/de-de/tag/api/)
  * [API-Sicherheit](https://blog.cloudflare.com/de-de/tag/api-security/)
  * [Anwendungssicherheit](https://blog.cloudflare.com/de-de/tag/application-security/)
  * [Anwendungsservices](https://blog.cloudflare.com/de-de/tag/application-services/)
  * [Athenian Project (DE)](https://blog.cloudflare.com/de-de/tag/athenian-project/)
  * [Angriffe](https://blog.cloudflare.com/de-de/tag/attacks/)
  * [Automatisierung](https://blog.cloudflare.com/de-de/tag/automation/)
  * [AWS](https://blog.cloudflare.com/de-de/tag/aws/)
  * [Beta](https://blog.cloudflare.com/de-de/tag/beta/)
  * [Birthday Week](https://blog.cloudflare.com/de-de/tag/birthday-week/)
  * [Black Friday (DE)](https://blog.cloudflare.com/de-de/tag/black-friday/)
  * [Bot-Management](https://blog.cloudflare.com/de-de/tag/bot-management/)
  * [Botnet (DE)](https://blog.cloudflare.com/de-de/tag/botnet/)
  * [Bots](https://blog.cloudflare.com/de-de/tag/bots/)
  * [Browser-Rendering](https://blog.cloudflare.com/de-de/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/de-de/tag/browser-run/)
  * [Bug Bounty (DE)](https://blog.cloudflare.com/de-de/tag/bug-bounty/)
  * [Cache](https://blog.cloudflare.com/de-de/tag/cache/)
  * [CASB](https://blog.cloudflare.com/de-de/tag/casb/)
  * [CDN](https://blog.cloudflare.com/de-de/tag/cdn/)
  * [Certificate Authority (DE)](https://blog.cloudflare.com/de-de/tag/certificate-authority/)
  * [Zertifizierung](https://blog.cloudflare.com/de-de/tag/certification/)
  * [China (DE)](https://blog.cloudflare.com/de-de/tag/china/)
  * [CIO Week](https://blog.cloudflare.com/de-de/tag/cio-week/)
  * [CISA (DE)](https://blog.cloudflare.com/de-de/tag/cisa/)
  * [Clientlos](https://blog.cloudflare.com/de-de/tag/clientless/)
  * [Cloud Email Security](https://blog.cloudflare.com/de-de/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/de-de/tag/cloudflare-access/)
  * [Cloudflare Calls](https://blog.cloudflare.com/de-de/tag/cloudflare-calls/)
  * [Cloudflare für Startups](https://blog.cloudflare.com/de-de/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/de-de/tag/gateway/)
  * [Cloudflare One](https://blog.cloudflare.com/de-de/tag/cloudflare-one/)
  * [Cloudflare Pages](https://blog.cloudflare.com/de-de/tag/cloudflare-pages/)
  * [Cloudflare Queues](https://blog.cloudflare.com/de-de/tag/cloudflare-queues/)
  * [Tunnel von Cloudflare](https://blog.cloudflare.com/de-de/tag/cloudflare-tunnel/)
  * [Cloudflare Workers](https://blog.cloudflare.com/de-de/tag/workers/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/de-de/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/de-de/tag/cloudforce-one/)
  * [Code Orange](https://blog.cloudflare.com/de-de/tag/code-orange/)
  * [Coinbase](https://blog.cloudflare.com/de-de/tag/coinbase/)
  * [Compliance](https://blog.cloudflare.com/de-de/tag/compliance/)
  * [Compression](https://blog.cloudflare.com/de-de/tag/compression/)
  * [Connectivity (DE)](https://blog.cloudflare.com/de-de/tag/connectivity/)
  * [Connectivity Cloud](https://blog.cloudflare.com/de-de/tag/connectivity-cloud/)
  * [Verbraucherdienste](https://blog.cloudflare.com/de-de/tag/consumer-services/)
  * [Container](https://blog.cloudflare.com/de-de/tag/containers/)
  * [Content Independence Day](https://blog.cloudflare.com/de-de/tag/content-independence-day/)
  * [Kontext](https://blog.cloudflare.com/de-de/tag/context/)
  * [Crawler Hints](https://blog.cloudflare.com/de-de/tag/crawler-hints/)
  * [CrowdStrike (DE)](https://blog.cloudflare.com/de-de/tag/crowdstrike/)
  * [Crypto Week (DE)](https://blog.cloudflare.com/de-de/tag/crypto-week/)
  * [Kryptographie](https://blog.cloudflare.com/de-de/tag/cryptography/)
  * [D1](https://blog.cloudflare.com/de-de/tag/d1/)
  * [Data Catalog](https://blog.cloudflare.com/de-de/tag/data-catalog/)
  * [Data Localization (DE)](https://blog.cloudflare.com/de-de/tag/data-localization/)
  * [Data Localization Suite (DE)](https://blog.cloudflare.com/de-de/tag/data-localization-suite/)
  * [Data Privacy Day (DE)](https://blog.cloudflare.com/de-de/tag/data-privacy-day/)
  * [Datenbank](https://blog.cloudflare.com/de-de/tag/database/)
  * [DDoS](https://blog.cloudflare.com/de-de/tag/ddos/)
  * [DDoS-Warnungen](https://blog.cloudflare.com/de-de/tag/ddos-alerts/)
  * [DDoS-Berichte](https://blog.cloudflare.com/de-de/tag/ddos-reports/)
  * [Umfassende Analyse](https://blog.cloudflare.com/de-de/tag/deep-dive/)
  * [Dokumentation für Entwickler](https://blog.cloudflare.com/de-de/tag/developer-documentation/)
  * [Entwicklerplattform](https://blog.cloudflare.com/de-de/tag/developer-platform/)
  * [Developer Week](https://blog.cloudflare.com/de-de/tag/developer-week/)
  * [Entwickler](https://blog.cloudflare.com/de-de/tag/developers/)
  * [DevOps (DE)](https://blog.cloudflare.com/de-de/tag/devops/)
  * [Digital Experience Monitoring (DE)](https://blog.cloudflare.com/de-de/tag/digital-experience-monitoring/)
  * [Diversity (DE)](https://blog.cloudflare.com/de-de/tag/diversity/)
  * [DLP](https://blog.cloudflare.com/de-de/tag/dlp/)
  * [DMARC (DE)](https://blog.cloudflare.com/de-de/tag/dmarc/)
  * [DNS](https://blog.cloudflare.com/de-de/tag/dns/)
  * [DNS Flood (DE)](https://blog.cloudflare.com/de-de/tag/dns-flood/)
  * [Dogfooding (DE)](https://blog.cloudflare.com/de-de/tag/dogfooding/)
  * [DoH (DE)](https://blog.cloudflare.com/de-de/tag/doh/)
  * [Durable Objects](https://blog.cloudflare.com/de-de/tag/durable-objects/)
  * [Early Hints (DE)](https://blog.cloudflare.com/de-de/tag/early-hints/)
  * [EC2 (DE)](https://blog.cloudflare.com/de-de/tag/ec2/)
  * [Egress (DE)](https://blog.cloudflare.com/de-de/tag/egress/)
  * [E-Mail-Sicherheit](https://blog.cloudflare.com/de-de/tag/email-security/)
  * [Emissions](https://blog.cloudflare.com/de-de/tag/emissions/)
  * [Technik](https://blog.cloudflare.com/de-de/tag/engineering/)
  * [Entropie](https://blog.cloudflare.com/de-de/tag/entropy/)
  * [Forrester](https://blog.cloudflare.com/de-de/tag/forrester/)
  * [Foundation DNS (DE)](https://blog.cloudflare.com/de-de/tag/foundation-dns/)
  * [Brief der Gründer](https://blog.cloudflare.com/de-de/tag/founders-letter/)
  * [Betrug](https://blog.cloudflare.com/de-de/tag/fraud/)
  * [Free (DE)](https://blog.cloudflare.com/de-de/tag/free/)
  * [Freedom of Speech (DE)](https://blog.cloudflare.com/de-de/tag/freedom-of-speech/)
  * [Front-End](https://blog.cloudflare.com/de-de/tag/front-end/)
  * [Full Stack](https://blog.cloudflare.com/de-de/tag/full-stack/)
  * [Gartner (DE)](https://blog.cloudflare.com/de-de/tag/gartner/)
  * [Gatebot (DE)](https://blog.cloudflare.com/de-de/tag/gatebot/)
  * [GDPR (DE)](https://blog.cloudflare.com/de-de/tag/gdpr/)
  * [Allgemein Verfügbar](https://blog.cloudflare.com/de-de/tag/general-availability/)
  * [Generative KI](https://blog.cloudflare.com/de-de/tag/generative-ai/)
  * [Geo Key Manager (DE)](https://blog.cloudflare.com/de-de/tag/geo-key-manager/)
  * [Germany (DE)](https://blog.cloudflare.com/de-de/tag/germany/)
  * [GitHub](https://blog.cloudflare.com/de-de/tag/github/)
  * [Google Cloud](https://blog.cloudflare.com/de-de/tag/google-cloud/)
  * [HTTP2 (DE)](https://blog.cloudflare.com/de-de/tag/http2/)
  * [Hyperdrive](https://blog.cloudflare.com/de-de/tag/hyperdrive/)
  * [Auswirkung](https://blog.cloudflare.com/de-de/tag/impact/)
  * [Impact Week (DE)](https://blog.cloudflare.com/de-de/tag/impact-week/)
  * [Intel](https://blog.cloudflare.com/de-de/tag/intel/)
  * [Interconnection](https://blog.cloudflare.com/de-de/tag/interconnection/)
  * [Internet-Performance](https://blog.cloudflare.com/de-de/tag/internet-performance/)
  * [Internetqualität](https://blog.cloudflare.com/de-de/tag/internet-quality/)
  * [Internetabschaltung](https://blog.cloudflare.com/de-de/tag/internet-shutdown/)
  * [Internet-Traffic](https://blog.cloudflare.com/de-de/tag/internet-traffic/)
  * [Internet-Trends](https://blog.cloudflare.com/de-de/tag/internet-trends/)
  * [IWD (DE)](https://blog.cloudflare.com/de-de/tag/iwd/)
  * [JAMstack (DE)](https://blog.cloudflare.com/de-de/tag/jamstack/)
  * [Jengo (DE)](https://blog.cloudflare.com/de-de/tag/jengo/)
  * [Killnet (DE)](https://blog.cloudflare.com/de-de/tag/killnet/)
  * [Lateinamerika](https://blog.cloudflare.com/de-de/tag/latin-america/)
  * [LavaRand](https://blog.cloudflare.com/de-de/tag/lavarand/)
  * [Karriere](https://blog.cloudflare.com/de-de/tag/life-at-cloudflare/)
  * [Lissabon](https://blog.cloudflare.com/de-de/tag/lisbon/)
  * [LLM](https://blog.cloudflare.com/de-de/tag/llm/)
  * [Log4J (DE)](https://blog.cloudflare.com/de-de/tag/log4j/)
  * [Log4Shell (DE)](https://blog.cloudflare.com/de-de/tag/log4shell/)
  * [Logs (DE)](https://blog.cloudflare.com/de-de/tag/logs/)
  * [MCP](https://blog.cloudflare.com/de-de/tag/mcp/)
  * [Microsoft Azure (DE)](https://blog.cloudflare.com/de-de/tag/microsoft-azure/)
  * [Mirai](https://blog.cloudflare.com/de-de/tag/mirai/)
  * [Mobile (DE)](https://blog.cloudflare.com/de-de/tag/mobile/)
  * [Model Kontext Protokoll,](https://blog.cloudflare.com/de-de/tag/model-context-protocol/)
  * [Multi-Cloud (DE)](https://blog.cloudflare.com/de-de/tag/multi-cloud/)
  * [MySQL](https://blog.cloudflare.com/de-de/tag/mysql/)
  * [NaaS (DE)](https://blog.cloudflare.com/de-de/tag/naas/)
  * [Network Interconnect (DE)](https://blog.cloudflare.com/de-de/tag/network-interconnect/)
  * [Network Protection (DE)](https://blog.cloudflare.com/de-de/tag/network-protection/)
  * [Netzwerk-Services](https://blog.cloudflare.com/de-de/tag/network-services/)
  * [NGINX](https://blog.cloudflare.com/de-de/tag/nginx/)
  * [Notifications (DE)](https://blog.cloudflare.com/de-de/tag/notifications/)
  * [Firmenstandorte](https://blog.cloudflare.com/de-de/tag/offices/)
  * [Olympics (DE)](https://blog.cloudflare.com/de-de/tag/olympics/)
  * [Ausfall](https://blog.cloudflare.com/de-de/tag/outage/)
  * [Partner](https://blog.cloudflare.com/de-de/tag/partners/)
  * [PCI Certified (DE)](https://blog.cloudflare.com/de-de/tag/pci-certified/)
  * [Peering (DE)](https://blog.cloudflare.com/de-de/tag/peering/)
  * [Performance](https://blog.cloudflare.com/de-de/tag/performance/)
  * [Phishing](https://blog.cloudflare.com/de-de/tag/phishing/)
  * [Pipelines](https://blog.cloudflare.com/de-de/tag/pipelines/)
  * [Politik & Rechtliches](https://blog.cloudflare.com/de-de/tag/policy/)
  * [Portugal](https://blog.cloudflare.com/de-de/tag/portugal/)
  * [Post-mortem-Analyse](https://blog.cloudflare.com/de-de/tag/post-mortem/)
  * [Post-Quanten-Kryptographie](https://blog.cloudflare.com/de-de/tag/post-quantum/)
  * [Datenschutz](https://blog.cloudflare.com/de-de/tag/privacy/)
  * [Produkt-News](https://blog.cloudflare.com/de-de/tag/product-news/)
  * [Projekt Galileo](https://blog.cloudflare.com/de-de/tag/project-galileo/)
  * [Project Safekeeping (DE)](https://blog.cloudflare.com/de-de/tag/project-safekeeping/)
  * [Python (DE)](https://blog.cloudflare.com/de-de/tag/python/)
  * [Queues](https://blog.cloudflare.com/de-de/tag/queues/)
  * [R2 Super Slurper](https://blog.cloudflare.com/de-de/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/de-de/tag/cloudflare-radar/)
  * [Radar API (DE)](https://blog.cloudflare.com/de-de/tag/radar-api/)
  * [Zufälligkeit](https://blog.cloudflare.com/de-de/tag/randomness/)
  * [Ransom-Angriffe](https://blog.cloudflare.com/de-de/tag/ransom-attacks/)
  * [Rapid Reset (DE)](https://blog.cloudflare.com/de-de/tag/rapid-reset/)
  * [Rate Limiting (DE)](https://blog.cloudflare.com/de-de/tag/rate-limiting/)
  * [RDDoS (DE)](https://blog.cloudflare.com/de-de/tag/rddos/)
  * [Reading List (DE)](https://blog.cloudflare.com/de-de/tag/reading-list/)
  * [Echtzeit](https://blog.cloudflare.com/de-de/tag/real-time/)
  * [Regional Services (DE)](https://blog.cloudflare.com/de-de/tag/regional-services/)
  * [Registrar](https://blog.cloudflare.com/de-de/tag/registrar/)
  * [Forschung](https://blog.cloudflare.com/de-de/tag/research/)
  * [REvil (DE)](https://blog.cloudflare.com/de-de/tag/revil/)
  * [Risikomanagement](https://blog.cloudflare.com/de-de/tag/risk-management/)
  * [Routing (DE)](https://blog.cloudflare.com/de-de/tag/routing/)
  * [Rust](https://blog.cloudflare.com/de-de/tag/rust/)
  * [SaaS (DE)](https://blog.cloudflare.com/de-de/tag/saas/)
  * [SaaS-Sicherheit](https://blog.cloudflare.com/de-de/tag/saas-security/)
  * [Sable (DE)](https://blog.cloudflare.com/de-de/tag/sable/)
  * [Sandbox](https://blog.cloudflare.com/de-de/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/de-de/tag/sase/)
  * [SDK](https://blog.cloudflare.com/de-de/tag/sdk/)
  * [Secure Web Gateway](https://blog.cloudflare.com/de-de/tag/secure-web-gateway/)
  * [Sicherheit](https://blog.cloudflare.com/de-de/tag/security/)
  * [Security Center](https://blog.cloudflare.com/de-de/tag/security-center/)
  * [Security Posture (DE)](https://blog.cloudflare.com/de-de/tag/security-posture/)
  * [Verwaltung des Sicherheitsniveaus](https://blog.cloudflare.com/de-de/tag/security-posture-management/)
  * [Security Service Edge (DE)](https://blog.cloudflare.com/de-de/tag/security-service-edge/)
  * [Security Week](https://blog.cloudflare.com/de-de/tag/security-week/)
  * [Serverless](https://blog.cloudflare.com/de-de/tag/serverless/)
  * [SIEM (DE)](https://blog.cloudflare.com/de-de/tag/siem/)
  * [SIM (DE)](https://blog.cloudflare.com/de-de/tag/sim/)
  * [South America (DE)](https://blog.cloudflare.com/de-de/tag/south-america/)
  * [Geschwindigkeit](https://blog.cloudflare.com/de-de/tag/speed/)
  * [Speed & Zuverlässigkeit](https://blog.cloudflare.com/de-de/tag/speed-and-reliability/)
  * [Speed Week (DE)](https://blog.cloudflare.com/de-de/tag/speed-week/)
  * [Sports (DE)](https://blog.cloudflare.com/de-de/tag/sports/)
  * [SSE (DE)](https://blog.cloudflare.com/de-de/tag/sse/)
  * [Speicherung](https://blog.cloudflare.com/de-de/tag/storage/)
  * [Sumo Logic (DE)](https://blog.cloudflare.com/de-de/tag/sumo-logic/)
  * [Supercloud (DE)](https://blog.cloudflare.com/de-de/tag/supercloud/)
  * [Sustainability (DE)](https://blog.cloudflare.com/de-de/tag/sustainability/)
  * [SYN Flood (DE)](https://blog.cloudflare.com/de-de/tag/syn-flood/)
  * [Das Team](https://blog.cloudflare.com/de-de/tag/team/)
  * [Teams Dashboard (DE)](https://blog.cloudflare.com/de-de/tag/teams-dashboard/)
  * [Testing (DE)](https://blog.cloudflare.com/de-de/tag/testing/)
  * [Bedrohungsinformationen](https://blog.cloudflare.com/de-de/tag/threat-intelligence/)
  * [Maßnahmen zur Bedrohungsbekämpfung](https://blog.cloudflare.com/de-de/tag/threat-operations/)
  * [Bedrohungen](https://blog.cloudflare.com/de-de/tag/threats/)
  * [Transparenz](https://blog.cloudflare.com/de-de/tag/transparency/)
  * [Trends](https://blog.cloudflare.com/de-de/tag/trends/)
  * [Trust & Safety (DE)](https://blog.cloudflare.com/de-de/tag/trust-and-safety/)
  * [TURN-Server](https://blog.cloudflare.com/de-de/tag/turn-server/)
  * [Vectorize (DE)](https://blog.cloudflare.com/de-de/tag/vectorize/)
  * [VoIP (DE)](https://blog.cloudflare.com/de-de/tag/voip/)
  * [WAF](https://blog.cloudflare.com/de-de/tag/waf/)
  * [Waiting Room (DE)](https://blog.cloudflare.com/de-de/tag/waiting-room/)
  * [WARP Connector (DE)](https://blog.cloudflare.com/de-de/tag/warp-connector/)
  * [WASM (DE)](https://blog.cloudflare.com/de-de/tag/wasm/)
  * [Web Application Firewall](https://blog.cloudflare.com/de-de/tag/web-application-firewall/)
  * [WebAssembly (DE)](https://blog.cloudflare.com/de-de/tag/webassembly/)
  * [WebRTC](https://blog.cloudflare.com/de-de/tag/webrtc/)
  * [Workers AI](https://blog.cloudflare.com/de-de/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/de-de/tag/workers-launchpad/)
  * [Workers VPC](https://blog.cloudflare.com/de-de/tag/workers-vpc/)
  * [Workflows](https://blog.cloudflare.com/de-de/tag/workflows/)
  * [x402](https://blog.cloudflare.com/de-de/tag/x402/)
  * [Das Jahr im Rückblick](https://blog.cloudflare.com/de-de/tag/year-in-review/)
  * [Zero Day Threats (DE)](https://blog.cloudflare.com/de-de/tag/zero-day-threats/)
  * [Zero Trust](https://blog.cloudflare.com/de-de/tag/zero-trust/)
  * [Zero Trust Week (DE)](https://blog.cloudflare.com/de-de/tag/zero-trust-week/)



[Rate Limiting (DE)](https://blog.cloudflare.com/de-de/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/de-de/tag/sdk/)

[Cloudflare Workers](https://blog.cloudflare.com/de-de/tag/workers/)[Developer Week](https://blog.cloudflare.com/de-de/tag/developer-week/)[Observability](https://blog.cloudflare.com/de-de/tag/observability/)[Rate Limiting (DE)](https://blog.cloudflare.com/de-de/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/de-de/tag/sdk/)

4\. April 2024

# Neue Tools für die Produktionssicherheit — Gradual Deployments, Source Maps, Rate Limiting und neue SDKs

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/de-de/author/tanushree/) und [Jacob Bednarz](https://blog.cloudflare.com/de-de/author/jacob-bednarz/)

Lesezeit: 14 Min.

URL kopieren

Dieser Beitrag ist auch verfügbar in [English](https://blog.cloudflare.com/workers-production-safety/), [Español](https://blog.cloudflare.com/es-es/workers-production-safety/), [Français](https://blog.cloudflare.com/fr-fr/workers-production-safety/), [日本語](https://blog.cloudflare.com/ja-jp/workers-production-safety/), [한국어](https://blog.cloudflare.com/ko-kr/workers-production-safety/), [繁體中文](https://blog.cloudflare.com/zh-tw/workers-production-safety/) und [简体中文](https://blog.cloudflare.com/zh-cn/workers-production-safety/).

![New tools for production safety — Gradual deployments, Source maps, Rate Limiting, and new SDKs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FR4MNGHSCH0P7DD7P68W.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+//769vXz8fDw8vHx9PLy8u7u6+fl/////vz98vT16+7y6+7z7u/17ezw5+Tm/////f3/8PP55u315ez36O356Orz5OPq////////8vb+5/D65e/85+/+6Oz55Obv////////+f3/7/f/7Pb/7fb/7fL/6uz2////////////+///+P7/9/7/9fr/8vT8/////////////////////////P//+Pv/////////////////////////////+/3/)

In der Developer Week 2024 dreht sich alles um die Production Readiness (also „Einsatzfähigkeit“ bzw. „Marktreife“ Ihres entwickelten Produkts). Am Montag, den 1. April, haben wir [bekannt gegeben](https://blog.cloudflare.com/de-de/making-full-stack-easier-d1-ga-hyperdrive-queues-de-de/), dass [D1](https://developers.cloudflare.com/d1/), [Queues](https://developers.cloudflare.com/queues/), [Hyperdrive](https://developers.cloudflare.com/hyperdrive/), und [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) für die Markteinführung bereit und allgemein verfügbar sind. Am Dienstag, den 2. April, [gaben](https://blog.cloudflare.com/workers-ai-ga-huggingface-loras-python-support) wir dasselbe über unsere Inferenzplattform bekannt, [Workers AI](https://developers.cloudflare.com/workers-ai/). Und wir sind noch lange nicht fertig.

Bei der Production Readiness bzw. Marktreife Ihrer Entwicklungen geht es nicht nur um den Umfang und die Zuverlässigkeit der Dienste, mit denen Sie entwickeln. Sie brauchen auch Werkzeuge, um Änderungen sicher und zuverlässig durchzuführen. Sie verlassen sich nicht nur auf das, was Cloudflare bietet, sondern auch darauf, dass Sie das Verhalten von Cloudflare genau steuern und an die Bedürfnisse Ihrer Anwendung anpassen können.

Heute kündigen wir fünf Updates an, die Ihnen mehr Möglichkeiten bieten: Gradual Deployments, Stack Traces mit Source Maps in Tail Workers, eine neue Rate Limiting-API, brandneue API-SDKs und Neuerungen für Durable Objects – alle mit Blick auf geschäftskritische Produktionsdienste. Wir entwickeln unsere eigenen Produkte mit Workers, einschließlich [Access](https://developers.cloudflare.com/cloudflare-one/policies/access/), [R2](https://developers.cloudflare.com/r2/), [KV](https://developers.cloudflare.com/kv/), [Waiting Room](https://developers.cloudflare.com/waiting-room/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Queues](https://developers.cloudflare.com/queues/), [Stream](https://developers.cloudflare.com/stream/) und mehr. Wir verlassen uns selbst auf jede dieser neuen Funktionen, um sicherzustellen, dass unsere Produkte bereit für die Produktivsetzung sind – und jetzt freuen wir uns, sie allen zur Verfügung stellen zu können.

### Schrittweise Implementierung von Änderungen an Workers und Durable Objects

Die Bereitstellung eines Worker erfolgt nahezu sofort – in wenigen Sekunden ist die Änderung [überall](https://www.cloudflare.com/network/) live.

Wenn Sie den breiten Einsatz am Markt erreichen, birgt jede Änderung, die Sie vornehmen, ein größeres Risiko, sowohl in Bezug auf das Volumen als auch auf die Erwartungen. Sie müssen Ihr SLA für 99,99 % Verfügbarkeit erfüllen oder haben ein ambitioniertes SLO mit P90-Latenz. Eine fehlerhafte Bereitstellung, die 45 Sekunden lang für 100 % des Datenverkehrs aktiv ist, kann Millionen von fehlgeschlagenen Anfragen bedeuten. Eine geringfügige Codeänderung kann bei einem überlasteten Backend zu einer Flut von Wiederholungsversuchen führen, wenn sie auf einmal eingeführt wird. Dies sind die Arten von Risiken, die wir selbst für unsere eigenen, auf Workers basierenden Dienste in Betracht ziehen und mindern.

Diese Risiken lassen sich durch eine schrittweise Implementierung von Änderungen verringern, die manchmal auch als rollierende oder fortlaufende Bereitstellung („rolling deployment“) bezeichnet wird.

  1. Die aktuelle Version Ihrer Anwendung befindet sich im Produktivbetrieb
  2. Sie schalten die neue Version Ihrer Anwendung produktiv, leiten aber nur einen kleinen Prozentsatz des Datenverkehrs an diese neue Version weiter und warten, bis sie im Produktivbetrieb langsam „eingesickert“ ist, wobei Sie auf Regressionen und Fehler achten. Wenn etwas Schlimmes passiert, haben Sie es bei einem geringen Prozentsatz frühzeitig erkannt (z. B. 1 %) des Traffic-Aufkommens und können es schnell wieder auf die alte Version zurücksetzen.
  3. Sie erhöhen den prozentualen Anteil des Datenverkehrs schrittweise, bis die neue Version 100 % erreicht und dann vollständig eingeführt wird.



Mit dem heutigen Tag schaffen wir eine erstklassige Möglichkeit, Codeänderungen schrittweise auf Workers und Durable Objects über die [Cloudflare API](https://developers.cloudflare.com/api/operations/worker-deployments-list-deployments), die [Wrangler CLI](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-wrangler) oder das [Workers Dashboard](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-the-cloudflare-dashboard) zu implementieren. Gradual Deployments geht in die Open Beta-Phase – Sie können Gradual Deployments mit jedem Cloudflare-Konto nutzen, der im [Workers Free-Tarif](https://developers.cloudflare.com/workers/platform/pricing/#workers) ist, und sehr bald werden Sie Gradual Deployments auch mit Cloudflare Accounts im [Workers Paid](https://developers.cloudflare.com/workers/platform/pricing/#workers) und Enterprise-Tarif nutzen können. Sie werden ein Banner auf dem Workers Dashboard sehen, sobald Ihr Konto Zugang hat.

Wenn Sie zwei Versionen Ihres Workers oder Durable Objects gleichzeitig im Produktivbetrieb laufen lassen, möchten Sie mit Sicherheit in der Lage sein, Ihre Metriken, Ausnahmen und Protokolle nach Version zu filtern. Dies kann Ihnen helfen, Probleme in der Produktivnutzung frühzeitig zu erkennen, wenn die neue Version nur für einen kleinen Prozentsatz des Traffics ausgerollt wird, oder Performance-Metriken zu vergleichen, wenn der Traffic 50/50 aufgeteilt wird. Unsere Plattform bietet jetzt auch Beobachtbarkeit auf Versionsebene:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Splitting traffic between different versions of a Worker.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4792EFMEWR5SFVJAMDC49A.png&w=715&h=353&f=webp&fit=cover&position=center)

  * Sie können die Analysen im Workers-Dashboard und über die [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) nach Version filtern.
  * [Workers Trace Events](https://developers.cloudflare.com/workers/observability/logging/logpush/) und [Tail Worker](https://developers.cloudflare.com/workers/observability/logging/tail-workers/)-Ereignisse enthalten die Versions-ID Ihrer Worker sowie optionale Felder für Versionsmeldungen und Versionskennzeichen.
  * Wenn Sie [Wrangler Tail](https://developers.cloudflare.com/workers/wrangler/commands/#tail) verwenden, um Live-Protokolle anzuzeigen, können Sie Protokolle für eine bestimmte Version anzeigen.
  * Sie können vom Code Ihres Workers aus auf Versions-ID, Nachricht und Tag zugreifen, indem Sie die [Bindung der Version-Metadaten](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/) konfigurieren.



Vielleicht möchten Sie auch sicherstellen, dass jeder Client oder Benutzer nur eine einheitliche Version Ihres Workers sieht. Wir haben [Version Affinity](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity) hinzugefügt, sodass Anfragen, die mit einer bestimmten Kennung verbunden sind (z. B. Benutzer, Sitzung oder eine andere eindeutige ID), immer von einer einheitlichen Version Ihres Workers verarbeitet werden. Die [Sitzungsaffinität](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity) gibt Ihnen in Verbindung mit der [Ruleset Engine](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#setting-cloudflare-workers-version-key-using-ruleset-engine) die volle Kontrolle über den Mechanismus und die Kennung (Identifikator), um die Durchgängigkeit zu gewährleisten.

Gradual Deployments geht jetzt in die Open Beta-Phase. Damit wir schon bald die allgemeine Verfügbarkeit erreichen, arbeiten wir daran, folgende Funktionen zu unterstützen:

  * **Überschreiben von Versionen.** Rufen Sie eine bestimmte Version Ihres Workers auf, um ihn zu testen, bevor er für den Live-Traffic eingesetzt wird. So können Sie Blau/Grün-Bereitstellungen („Blue-Green Deployments“) erstellen.
  * **Cloudflare Pages.** Lassen Sie das CI/CD-System in Cloudflare Pages die Bereitstellungen automatisch in Ihrem Namen durchführen.
  * **Automatische Rollbacks.** Führen Sie automatisch ein Rollback durch, wenn die Fehlerrate für eine neue Version Ihres Workers ansteigt.



Wir freuen uns auf Ihr Feedback! Teilen Sie uns Ihre Meinung über [dieses](https://www.cloudflare.com/lp/developer-week-deployments/) Feedback-Formular mit oder melden Sie sich in unserem [Entwickler-Discord](https://discord.gg/HJvPcPcN) im Kanal #workers-gradual-deployments-beta.

### Stack Traces mit Source Maps in Tail Workers

Production Readiness bedeutet, Fehler und Ausnahmen zu verfolgen und zu versuchen, sie auf null zu reduzieren. Wenn ein Fehler auftritt, sollten Sie sich als erstes den [Stack Trace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack) des Fehlers ansehen – die spezifischen Funktionen, die aufgerufen wurden, in welcher Reihenfolge, von welcher Zeile und Datei und mit welchen Argumenten.

Der meiste JavaScript-Code – nicht nur auf Workers, sondern plattformübergreifend – wird zunächst gebündelt, oft transpiliert und dann verkleinert, bevor es zur Produktivsetzung kommt. Dies geschieht im Hintergrund, um kleinere Pakete zur Optimierung der Performance zu erstellen und bei Bedarf von Typescript in Javascript zu konvertieren.

Wenn Sie jemals eine Ausnahme gesehen haben, die einen Stack-Trace wie z.B.: /src/index.js:1:342 ausgibt, bedeutet dies, dass der Fehler beim 342. Zeichen des minimierten Codes Ihrer Funktion aufgetreten ist. Das ist für die Fehlersuche natürlich nicht sehr hilfreich.

[Source Maps](https://web.dev/articles/source-maps) lösen dieses Problem – sie führen den kompilierten und verkleinerten Code auf den ursprünglichen Code zurück, den Sie geschrieben haben. Source Maps werden mit dem von der JavaScript-Laufzeitumgebung zurückgegebenen Stack-Trace kombiniert, um Ihnen einen für Menschen lesbaren Stack-Trace zu präsentieren. Der folgende Stack-Trace zeigt zum Beispiel, dass der Worker in Zeile 30 der Dateidown.ts einen unerwarteten Nullwert erhalten hat. Dies ist ein nützlicher Ausgangspunkt für die Fehlersuche. Sie können den Stack-Trace weiter nach unten verfolgen, um nachzuvollziehen, welche Funktionen aufgerufen wurden, die zu dem Nullwert geführt haben.

Unser Erfolgsgeheimnis:
    
    
    Unexpected input value: null
      at parseBytes (src/down.ts:30:8)
      at down_default (src/down.ts:10:19)
      at Object.fetch (src/index.ts:11:12)

  1. Wenn Sie upload_source_maps = true in Ihrer [wrangler.toml](https://developers.cloudflare.com/workers/wrangler/configuration/) setzen, wird automatisch alle Source-Map-Dateien erzeugen und hochladen, wenn Sie [wrangler deploy](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) oder [wrangler versions upload](https://developers.cloudflare.com/workers/wrangler/commands/#versions) ausführen.
  2. Wenn Ihr Worker eine nicht abgefangene Ausnahme auslöst, holen wir die Source Map und verwenden sie, um die Stack-Trace der Ausnahme auf Zeilen des ursprünglichen Quellcodes Ihres Workers zurückzuführen.
  3. Sie können diesen entschleierten Stack-Trace dann in [Echtzeitprotokollen](https://developers.cloudflare.com/workers/observability/logging/real-time-logs/) oder in [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) anzeigen.



Ab heute, in der Open Beta, können Sie Source Maps zu Cloudflare hochladen, wenn Sie Ihren Worker bereitstellen – [lesen Sie dazu die Dokumentation](https://developers.cloudflare.com/workers/observability/source-maps). Und ab dem 15. April wird die Workers-Laufzeit beginnen, Source Maps zu verwenden, um Stack Traces zu entschleiern. Wir werden eine Benachrichtigung im Cloudflare-Dashboard und auf unserem [X-Konto für Cloudflare Developers](https://twitter.com/CloudflareDev?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) posten, wenn Stack Traces mit Source Maps verfügbar sind.

### Neue Rate Limiting-API in Workers

Eine API kann nur dann produktiv gesetzt werden, wenn sie über eine sinnvolle [Durchsatzbegrenzung](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/) verfügt. Und je mehr Sie wachsen, desto komplexer und vielfältiger werden die Grenzen, die Sie durchsetzen müssen, um die Bedürfnisse bestimmter Kunden auszugleichen, den Zustand Ihres Dienstes zu schützen oder Grenzen in bestimmten Szenarien durchzusetzen und anzupassen. Die eigene API von Cloudflare steht vor dieser Herausforderung – jedes unserer Dutzende von Produkten, jedes mit vielen API-Endpunkten, muss möglicherweise unterschiedliche Durchsatzbegrenzungen durchsetzen.

Seit 2017 können Sie bei Cloudflare [Regeln zur Durchsatzbegrenzung](https://developers.cloudflare.com/waf/rate-limiting-rules/) konfigurieren. Aber bis heute konnten Sie dies nur im Cloudflare-Dashboard oder über die Cloudflare-API steuern. Es war nicht möglich, das Verhalten zur _Laufzeit_ zu definieren oder Code in Worker zu schreiben, der direkt mit den Durchsatzbegrenzungen interagiert – Sie konnten nur kontrollieren, ob eine Anfrage im Durchsatz begrenzt ist oder nicht, bevor sie Ihren Worker erreicht.

Heute stellen wir eine neue API in der Open Beta-Phase vor, mit der Sie direkt von Ihrem Worker aus auf die Durchsatzbegrenzungen zugreifen können. Es ist blitzschnell, wird von memcached unterstützt und lässt sich ganz einfach zu Ihrem Worker hinzufügen. In der folgenden Konfiguration wird beispielsweise ein Durchsatzlimit von 100 Anfragen innerhalb eines Zeitraums von 60 Sekunden festgelegt:

Dann können Sie in Ihrem Worker die Limit-Methode für die RATE_LIMITER-Bindung aufrufen und einen Schlüssel Ihrer Wahl angeben. Mit der obigen Konfiguration gibt dieser Code einen [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) 429-Antwortstatuscode zurück, wenn innerhalb von 60 Sekunden mehr als 100 Anfragen an einen bestimmten Pfad gestellt werden:
    
    
    [[unsafe.bindings]]
    name = "RATE_LIMITER"
    type = "ratelimit"
    namespace_id = "1001" # An identifier unique to your Cloudflare account
    
    # Limit: the number of tokens allowed within a given period, in a single Cloudflare location
    # Period: the duration of the period, in seconds. Must be either 60 or 10
    simple = { limit = 100, period = 60 } 

Nun kann Workers also eine direkte Verbindung zu einem Datenspeicher wie memcached herstellen. Was könnten wir nun noch anbieten? Zähler? Sperren? Einen [In-Memory Cache](https://github.com/cloudflare/workerd/pull/1666)? Rate Limiting ist die erste von vielen Primitiven, die wir in Workers bereitstellen wollen, und die sich mit der Frage befassen, wo ein temporärer gemeinsamer Status, der sich über viele Worker-[Isolates](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates) erstreckt, gespeichert werden soll. Wenn Sie sich heute darauf verlassen, den Status in den globalen Bereich Ihres Workers zu legen, sollten Sie wissen: wir arbeiten an besseren Primitiven, die speziell für bestimmte Anwendungsfälle entwickelt werden.
    
    
    export default {
      async fetch(request, env) {
        const { pathname } = new URL(request.url)
    
        const { success } = await env.RATE_LIMITER.limit({ key: pathname })
        if (!success) {
          return new Response(`429 Failure – rate limit exceeded for ${pathname}`, { status: 429 })
        }
    
        return new Response(`Success!`)
      }
    }

Die Rate Limiting-API in Workers befindet sich in der Open Beta-Phase. Setzen Sie jetzt die ersten Schritte, indem Sie [die Dokumentationen lesen](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit).

### Neue automatisch generierte SDKs für die API von Cloudflare

Production Readiness bedeutet, dass Sie Änderungen nicht mehr durch Anklicken von Schaltflächen in einem Dashboard vornehmen, sondern programmatisch, mit einem Infrastructure-as-Code-Ansatz wie [Terraform](https://github.com/cloudflare/terraform-provider-cloudflare) oder [Pulumi](https://github.com/pulumi/pulumi-cloudflare) oder durch direkten API-Aufruf, entweder selbst oder über ein SDK.

Die [Cloudflare-API](https://developers.cloudflare.com/api/) ist riesig und es kommen ständig neue Funktionen hinzu – im Durchschnitt [aktualisieren](https://github.com/cloudflare/api-schemas/activity) wir unsere API-Schemata zwischen 20- und 30-mal pro Tag. Bislang wurden unsere API-SDKs jedoch manuell erstellt und gewartet, weshalb wir dies unbedingt zeitnahe automatisieren wollten.

Das haben wir getan, und heute kündigen wir neue Client-SDKs für die Cloudflare-API in drei Sprachen an – [Typescript](https://github.com/cloudflare/cloudflare-typescript), [Python](https://github.com/cloudflare/cloudflare-python) und [Go](https://github.com/cloudflare/cloudflare-go) – und weitere Sprachen werden schon bald unterstützt.

Jedes SDK wird automatisch mit [Stainless API](https://www.stainlessapi.com/) generiert, basierend auf den [OpenAPI-Schemata](https://github.com/cloudflare/api-schemas), die die Struktur und die Fähigkeiten jedes unserer API-Endpunkte definieren. Das bedeutet, dass diese API-SDKs automatisch neu generiert und neue Versionen veröffentlicht werden, wenn wir der Cloudflare-API neue Funktionen für alle Cloudflare-Produkte hinzufügen, um sicherzustellen, dass sie korrekt und aktuell sind.

Sie können die SDKs installieren, indem Sie einen der folgenden Befehle ausführen:

Wenn Sie Terraform oder Pulumi nutzt, verwendet der Terraform Provider von Cloudflare im Hintergrund derzeit das bestehende, nicht automatisierte [Go SDK](https://github.com/cloudflare/cloudflare-go). Wenn Sie terraform apply ausführen, bestimmt der Cloudflare Terraform Provider, welche API-Aufrufe in welcher Reihenfolge zu tätigen sind, und führt diese unter Verwendung des Go SDK aus.
    
    
    // Typescript
    npm install cloudflare
    
    // Python
    pip install cloudflare
    
    // Go
    go get -u github.com/cloudflare/cloudflare-go/v2

Das neue, automatisch generierte Go-SDK ebnet den Weg zu einer umfassenderen Terraform-Unterstützung für alle Cloudflare-Produkte und bietet eine Basis von Tools, von denen man sicher sein kann, dass sie sowohl korrekt als auch auf dem neuesten Stand der API-Änderungen sind. Wir arbeiten an einer Zukunft, in der jedes Mal, wenn ein Produktteam bei Cloudflare eine neue Funktion entwickelt, die über die Cloudflare-API zugänglich ist, diese automatisch von den SDKs unterstützt wird. Im Laufe des Jahres 2024 erwarten Sie weitere Neuigkeiten zu diesem Thema.

### Namespace-Analytics in Durable Object und WebSocket Hibernation allgemein verfügbar

Viele unserer eigenen Produkte, darunter [Waiting Room](https://developers.cloudflare.com/waiting-room/), [R2](https://developers.cloudflare.com/r2/) und [Queues](https://developers.cloudflare.com/queues/), sowie Plattformen wie [PartyKit](https://www.partykit.io/), werden mit [Durable Objects](https://developers.cloudflare.com/durable-objects/) entwickelt. Weltweit eingesetzt, einschließlich der neu hinzugefügten Unterstützung für Ozeanien, können Sie sich Durable Objects wie singuläre Workers vorstellen, die einen einzigen Koordinationspunkt bereitstellen und den Status [beibehalten können](https://developers.cloudflare.com/durable-objects/api/transactional-storage-api/). Sie eignen sich perfekt für Anwendungen, die eine Echtzeit-Benutzerkoordination erfordern, wie z. B. interaktive Chats oder kollaborative Bearbeitung. Sehen Sie sich an, was Atlassian diesbezüglich zu sagen hat:

> _Eine unserer neuen Funktionen sind_ _[Confluence-Whiteboards](https://www.atlassian.com/software/confluence/whiteboards), die eine freie Möglichkeit bieten, unstrukturierte Tätigkeiten wie Brainstorming und frühe Planung zu erfassen, bevor die Teams sie formeller dokumentieren. Das Team prüfte viele Optionen für die Zusammenarbeit in Echtzeit und entschied sich schließlich für Durable Objects von Cloudflare. Durable Objects haben sich als fantastische Lösung für dieses Problemfeld erwiesen, mit einer einzigartigen Kombination von Funktionalitäten, die es uns ermöglicht haben, unsere Infrastruktur stark zu vereinfachen und leicht auf eine große Anzahl von Benutzern zu skalieren._ -[_Atlassian_](https://www.atlassian.com/software/confluence/whiteboards)

Bisher haben wir im Dashboard keine zugehörigen analytischen Trends angezeigt, wodurch es schwierig war, die Nutzungsmuster und Fehlerraten innerhalb eines [Durable Objects-Namespace](https://developers.cloudflare.com/durable-objects/configuration/access-durable-object-from-a-worker/#generate-ids-randomly) zu verstehen, es sei denn, Sie haben die [GraphQL Analytics-API](https://developers.cloudflare.com/analytics/graphql-api/) direkt verwendet. Das [Dashboard für Durable Objects](https://dash.cloudflare.com/?to=/:account/workers/durable-objects) wurde nun überarbeitet und ermöglicht es Ihnen, Metriken aufzuschlüsseln so detailliert wie nötig zu analysieren.

Vom [ersten Tag an](https://blog.cloudflare.com/introducing-workers-durable-objects) hat Durable Objects [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) unterstützt, sodass sich viele Clients direkt mit einem Durable Object verbinden können, um Nachrichten zu senden und zu empfangen.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2305 Embedded Image - tUWMOW](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NGJQ7SMHCNME7M5TATPN.png&w=715&h=557&f=webp&fit=cover&position=center)

Manchmal öffnen Client-Anwendungen jedoch eine WebSocket-Verbindung und...machen dann irgendwann gar nichts mehr. Denken Sie an den Browser-Tab, den Sie in den letzten 5 Stunden in Ihrem Browser geöffnet hatten, aber nicht mehr angesehen haben. Wenn er WebSockets zum Senden und Empfangen von Nachrichten verwendet, hat er praktisch eine langlebige TCP-Verbindung, die für nichts verwendet wird. Wenn diese Verbindung zu einem Durable Object besteht, muss das Durable Object weiterlaufen und darauf warten, dass etwas passiert. Das verbraucht Speicherplatz und kostet Sie Geld.

Wir haben [WebSocket Hibernation eingeführt](https://blog.cloudflare.com/workers-pricing-scale-to-zero), um dieses Problem zu lösen, und heute geben wir bekannt, dass diese Funktion die Beta-Phase verlassen hat und nun allgemein verfügbar ist. Mit WebSocket Hibernation legen Sie eine automatische Antwort fest, die während des Ruhezustands verwendet wird, und serialisieren den Status so, dass er den Ruhezustand überdauert. Dadurch erhält Cloudflare die Eingaben, die wir benötigen, um offene WebSocket-Verbindungen von Clients aufrechtzuerhalten, während das Durable Object in den Ruhezustand versetzt wird, sodass es nicht aktiv ausgeführt und Ihnen keine Leerlaufzeit in Rechnung gestellt wird. Dadurch ist Ihr Status immer dann im Speicher verfügbar, wenn Sie ihn tatsächlich benötigen, und wird nicht unnötig aufbewahrt, wenn er nicht benötigt wird. Solange sich Ihr Durable Object im Ruhezustand befindet, werden Ihnen keine Kosten für die Dauer in Rechnung gestellt, selbst wenn noch aktive Clients über einen WebSocket verbunden sind.

Außerdem haben wir Feedback von Entwicklern und Entwicklerinnen zu den Kosten eingehender WebSocket-Nachrichten an Durable Objects erhalten, die kleinere, häufigere Nachrichten für die Echtzeitkommunikation bevorzugen. Ab heute werden eingehende WebSocket-Nachrichten mit dem Äquivalent von 1/20 einer Anfrage berechnet (im Gegensatz zu 1 Nachricht als Äquivalent für 1 Anfrage, wie es bisher war). Nachfolgend ein [Preisbeispiel](https://developers.cloudflare.com/durable-objects/platform/pricing/#example-4):

.tg {border-collapse:collapse;border-color:#ccc;border-spacing:0;} .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top} .tg .tg-4kyp{color:#0E101A;text-align:left;vertical-align:top} .tg .tg-bhdc{color:#0E101A;font-weight:bold;text-align:left;vertical-align:top}

| WebSocket Connection Requests | Incoming WebSocket Messages | Billed Requests | Request Billing  
---|---|---|---|---  
Before | 10K | 432M | 432,010,000 | $64.65  
After | 10K | 432M | 21,610,000 | $3.09  
  
WebSocket-Verbindungsanfragen

Eingehende WebSocket-Nachrichten

Abgerechnete Anfragen

Verrechnete Kosten für Anfragen

Vorher

10.000

432 Mio.

432.010.000

64,65 USD

Nachher

10.000

432 Mio.

21.610.000

3,09 USD

### Bereit zur Produktivsetzung, ohne die Komplexität des Produktivstarts

Damit Sie Ihre Entwicklungen auf den Cloud-Plattformen produktiv schalten konnten, mussten Sie bislang die Geschwindigkeit der Veröffentlichung drosseln. Hierfür mussten Sie meist ein Flickwerk an unzusammenhängenden Tools zusammenfügen oder ganze Teams für die Arbeit an internen Plattformen zusammenstellen. Sie mussten Ihre eigenen produktiven Ebenen auf Plattformen nachrüsten, die Ihnen Steine in den Weg legten.

Die Entwicklungsplattform von Cloudflare ist ausgereift und bereit für den Produktivbetrieb. Sie wurde als integrierte Plattform konzipiert, auf der Produkte intuitiv miteinander eingesetzt werden können. Es gibt keine überflüssigen Möglichkeiten zur Kombination von Tools, deren gemeinsame Verwendung nur über eine mühsame Kompatibilitätsmatrix erschlossen werden könnte. Jedes dieser Updates stellt dies unter Beweis, indem neue Funktionen in alle Produkte und Teile der Cloudflare-Plattform integriert werden.

Darum möchten wir von Ihnen nicht nur wissen, was Sie als Nächstes sehen möchten, sondern auch, welche Aspekte unserer Plattform wir Ihrer Ansicht nach noch einfacher gestalten bzw. in welchen Bereichen unsere Tools noch besser gemeinsam eingesetzt werden könnten. Wir freuen uns auf Ihr Input – jederzeit gerne im [Cloudflare Developers-Discord](https://discord.cloudflare.com/).

Auf dieser Seite

Online diskutieren

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fde-de%2Fworkers-production-safety%2F&t=Neue%20Tools%20f%C3%BCr%20die%20Produktionssicherheit%20%E2%80%94%20Gradual%20Deployments%2C%20Source%20Maps%2C%20Rate%20Limiting%20und%20neue%20SDKs)[](https://x.com/intent/post?text=Neue+Tools+f%C3%BCr+die+Produktionssicherheit+%E2%80%94+Gradual+Deployments%2C+Source+Maps%2C+Rate+Limiting+und+neue+SDKs&url=https%3A%2F%2Fblog.cloudflare.com%2Fde-de%2Fworkers-production-safety%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fde-de%2Fworkers-production-safety%2F)[](https://bsky.app/intent/compose?text=Neue+Tools+f%C3%BCr+die+Produktionssicherheit+%E2%80%94+Gradual+Deployments%2C+Source+Maps%2C+Rate+Limiting+und+neue+SDKs+https%3A%2F%2Fblog.cloudflare.com%2Fde-de%2Fworkers-production-safety%2F)[](https://mastodonshare.com/?text=Neue+Tools+f%C3%BCr+die+Produktionssicherheit+%E2%80%94+Gradual+Deployments%2C+Source+Maps%2C+Rate+Limiting+und+neue+SDKs&url=https%3A%2F%2Fblog.cloudflare.com%2Fde-de%2Fworkers-production-safety%2F)[](https://www.threads.net/intent/post?text=Neue+Tools+f%C3%BCr+die+Produktionssicherheit+%E2%80%94+Gradual+Deployments%2C+Source+Maps%2C+Rate+Limiting+und+neue+SDKs+https%3A%2F%2Fblog.cloudflare.com%2Fde-de%2Fworkers-production-safety%2F)

## Verwandte Tags

[Cloudflare Workers](https://blog.cloudflare.com/de-de/tag/workers/)[Developer Week](https://blog.cloudflare.com/de-de/tag/developer-week/)[Observability](https://blog.cloudflare.com/de-de/tag/observability/)[Rate Limiting (DE)](https://blog.cloudflare.com/de-de/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/de-de/tag/sdk/)

Folgen Sie uns auf Social Media

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Jacob Bednarz](https://blog.cloudflare.com/de-de/author/jacob-bednarz/)

[](https://jacobbednarz.com)




## Abonnieren Sie Benachrichtigungen über neue Beiträge

E-Mail-Adresse

Wir geben Ihre E-Mail-Adresse niemals weiter.

Abonnieren

Vielen Dank für das Abonnement! Überprüfen Sie Ihren Posteingang, um die Anmeldung zu bestätigen.
