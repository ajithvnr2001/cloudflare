---
url: https://blog.cloudflare.com/fr-fr/workers-production-safety/
title: Nouveaux outils pour la s\u00e9curit\u00e9 de la production : d\u00e9ploiements graduels, Stack Traces, contr\u00f4le du volume de requ\u00eates et nouveaux SDK | Le blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:28.122652+00:00
---

# Nouveaux outils pour la sécurité de la production : déploiements graduels, Stack Traces, contrôle du volume de requêtes et nouveaux SDK | Le blog Cloudflare

> Source: https://blog.cloudflare.com/fr-fr/workers-production-safety/

[Blog](https://blog.cloudflare.com/fr-fr/)

[Cloudflare Workers](https://blog.cloudflare.com/fr-fr/tag/workers/)[Developer Week](https://blog.cloudflare.com/fr-fr/tag/developer-week/)[Observability](https://blog.cloudflare.com/fr-fr/tag/observability/)+2Afficher 2 étiquettes supplémentaires

5 tagsAfficher 5 tags

  * Tags de l’article
  * [Cloudflare Workers](https://blog.cloudflare.com/fr-fr/tag/workers/)[Developer Week](https://blog.cloudflare.com/fr-fr/tag/developer-week/)[Rate Limiting (FR)](https://blog.cloudflare.com/fr-fr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/fr-fr/tag/sdk/)
  * Toutes les étiquettes
  * Tags correspondants
  * Aucun tag trouvé
  * [1.1.1.1](https://blog.cloudflare.com/fr-fr/tag/1-1-1-1/)
  * [Acquisitions](https://blog.cloudflare.com/fr-fr/tag/acquisitions/)
  * [Protection avancée contre les attaques DDoS](https://blog.cloudflare.com/fr-fr/tag/advanced-ddos/)
  * [État de préparation aux agents](https://blog.cloudflare.com/fr-fr/tag/agent-readiness/)
  * [Agents](https://blog.cloudflare.com/fr-fr/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/fr-fr/tag/agents-week/)
  * [IA](https://blog.cloudflare.com/fr-fr/tag/ai/)
  * [AI Bots (FR)](https://blog.cloudflare.com/fr-fr/tag/ai-bots/)
  * [AI Gateway (FR)](https://blog.cloudflare.com/fr-fr/tag/ai-gateway/)
  * [Recherche par IA](https://blog.cloudflare.com/fr-fr/tag/ai-search/)
  * [AI Week](https://blog.cloudflare.com/fr-fr/tag/ai-week/)
  * [AI-SPM](https://blog.cloudflare.com/fr-fr/tag/ai-spm/)
  * [Always Online (FR)](https://blog.cloudflare.com/fr-fr/tag/always-online/)
  * [AMD (FR)](https://blog.cloudflare.com/fr-fr/tag/amd/)
  * [Données analytiques](https://blog.cloudflare.com/fr-fr/tag/analytics/)
  * [Anonymous (FR)](https://blog.cloudflare.com/fr-fr/tag/anonymous/)
  * [Anycast (FR)](https://blog.cloudflare.com/fr-fr/tag/anycast/)
  * [API](https://blog.cloudflare.com/fr-fr/tag/api/)
  * [Sécurité des API](https://blog.cloudflare.com/fr-fr/tag/api-security/)
  * [Sécurité des applications](https://blog.cloudflare.com/fr-fr/tag/application-security/)
  * [Services pour applications](https://blog.cloudflare.com/fr-fr/tag/application-services/)
  * [Athenian Project (FR)](https://blog.cloudflare.com/fr-fr/tag/athenian-project/)
  * [Attaques](https://blog.cloudflare.com/fr-fr/tag/attacks/)
  * [Automatisation](https://blog.cloudflare.com/fr-fr/tag/automation/)
  * [Awards (FR)](https://blog.cloudflare.com/fr-fr/tag/awards/)
  * [AWS](https://blog.cloudflare.com/fr-fr/tag/aws/)
  * [Bêta](https://blog.cloudflare.com/fr-fr/tag/beta/)
  * [Semaine anniversaire](https://blog.cloudflare.com/fr-fr/tag/birthday-week/)
  * [Gestion des bots](https://blog.cloudflare.com/fr-fr/tag/bot-management/)
  * [Botnet (FR)](https://blog.cloudflare.com/fr-fr/tag/botnet/)
  * [Bots](https://blog.cloudflare.com/fr-fr/tag/bots/)
  * [Browser Rendering](https://blog.cloudflare.com/fr-fr/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/fr-fr/tag/browser-run/)
  * [Bug Bounty (FR)](https://blog.cloudflare.com/fr-fr/tag/bug-bounty/)
  * [Cache](https://blog.cloudflare.com/fr-fr/tag/cache/)
  * [CASB](https://blog.cloudflare.com/fr-fr/tag/casb/)
  * [Réseau de diffusion de contenu (CDN)](https://blog.cloudflare.com/fr-fr/tag/cdn/)
  * [Certificate Authority (FR)](https://blog.cloudflare.com/fr-fr/tag/certificate-authority/)
  * [Certification](https://blog.cloudflare.com/fr-fr/tag/certification/)
  * [China (FR)](https://blog.cloudflare.com/fr-fr/tag/china/)
  * [CIO Week](https://blog.cloudflare.com/fr-fr/tag/cio-week/)
  * [CISA (FR)](https://blog.cloudflare.com/fr-fr/tag/cisa/)
  * [Sans client](https://blog.cloudflare.com/fr-fr/tag/clientless/)
  * [Cloud Email Security](https://blog.cloudflare.com/fr-fr/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/fr-fr/tag/cloudflare-access/)
  * [Cloudflare Calls](https://blog.cloudflare.com/fr-fr/tag/cloudflare-calls/)
  * [Cloudflare for Startups](https://blog.cloudflare.com/fr-fr/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/fr-fr/tag/gateway/)
  * [Cloudflare One](https://blog.cloudflare.com/fr-fr/tag/cloudflare-one/)
  * [Cloudflare Pages](https://blog.cloudflare.com/fr-fr/tag/cloudflare-pages/)
  * [Cloudflare Queues](https://blog.cloudflare.com/fr-fr/tag/cloudflare-queues/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/fr-fr/tag/cloudflare-tunnel/)
  * [Cloudflare Workers](https://blog.cloudflare.com/fr-fr/tag/workers/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/fr-fr/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/fr-fr/tag/cloudforce-one/)
  * [Code Orange](https://blog.cloudflare.com/fr-fr/tag/code-orange/)
  * [Coinbase](https://blog.cloudflare.com/fr-fr/tag/coinbase/)
  * [Conformité](https://blog.cloudflare.com/fr-fr/tag/compliance/)
  * [Compression](https://blog.cloudflare.com/fr-fr/tag/compression/)
  * [Connectivity (FR)](https://blog.cloudflare.com/fr-fr/tag/connectivity/)
  * [Intégration cloud & cloud de connectivité](https://blog.cloudflare.com/fr-fr/tag/connectivity-cloud/)
  * [Services aux consommateurs](https://blog.cloudflare.com/fr-fr/tag/consumer-services/)
  * [Conteneurs](https://blog.cloudflare.com/fr-fr/tag/containers/)
  * [Journée de l'indépendance du contenu](https://blog.cloudflare.com/fr-fr/tag/content-independence-day/)
  * [Contexte](https://blog.cloudflare.com/fr-fr/tag/context/)
  * [Crawler Hints](https://blog.cloudflare.com/fr-fr/tag/crawler-hints/)
  * [CrowdStrike (FR)](https://blog.cloudflare.com/fr-fr/tag/crowdstrike/)
  * [Crypto Week (FR)](https://blog.cloudflare.com/fr-fr/tag/crypto-week/)
  * [Cryptographie](https://blog.cloudflare.com/fr-fr/tag/cryptography/)
  * [D1](https://blog.cloudflare.com/fr-fr/tag/d1/)
  * [Data Catalog](https://blog.cloudflare.com/fr-fr/tag/data-catalog/)
  * [Data Localization (FR)](https://blog.cloudflare.com/fr-fr/tag/data-localization/)
  * [Data Localization Suite (FR)](https://blog.cloudflare.com/fr-fr/tag/data-localization-suite/)
  * [Data Privacy Day (FR)](https://blog.cloudflare.com/fr-fr/tag/data-privacy-day/)
  * [Base de données](https://blog.cloudflare.com/fr-fr/tag/database/)
  * [Attaques DDoS](https://blog.cloudflare.com/fr-fr/tag/ddos/)
  * [Alertes d'attaques DDoS](https://blog.cloudflare.com/fr-fr/tag/ddos-alerts/)
  * [Rapports DDoS](https://blog.cloudflare.com/fr-fr/tag/ddos-reports/)
  * [Analyse approfondie](https://blog.cloudflare.com/fr-fr/tag/deep-dive/)
  * [Documentation destinée aux développeurs](https://blog.cloudflare.com/fr-fr/tag/developer-documentation/)
  * [Plateforme pour développeurs](https://blog.cloudflare.com/fr-fr/tag/developer-platform/)
  * [Developer Week](https://blog.cloudflare.com/fr-fr/tag/developer-week/)
  * [Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)
  * [DevOps (FR)](https://blog.cloudflare.com/fr-fr/tag/devops/)
  * [Digital Experience Monitoring (FR)](https://blog.cloudflare.com/fr-fr/tag/digital-experience-monitoring/)
  * [Diversity (FR)](https://blog.cloudflare.com/fr-fr/tag/diversity/)
  * [DLP](https://blog.cloudflare.com/fr-fr/tag/dlp/)
  * [DMARC (FR)](https://blog.cloudflare.com/fr-fr/tag/dmarc/)
  * [DNS](https://blog.cloudflare.com/fr-fr/tag/dns/)
  * [DNS Flood (FR)](https://blog.cloudflare.com/fr-fr/tag/dns-flood/)
  * [Dogfooding (FR)](https://blog.cloudflare.com/fr-fr/tag/dogfooding/)
  * [DoH (FR)](https://blog.cloudflare.com/fr-fr/tag/doh/)
  * [Durable Objects](https://blog.cloudflare.com/fr-fr/tag/durable-objects/)
  * [Early Hints (FR)](https://blog.cloudflare.com/fr-fr/tag/early-hints/)
  * [EC2 (FR)](https://blog.cloudflare.com/fr-fr/tag/ec2/)
  * [Sécurité des e-mails](https://blog.cloudflare.com/fr-fr/tag/email-security/)
  * [Emissions](https://blog.cloudflare.com/fr-fr/tag/emissions/)
  * [Ingénierie](https://blog.cloudflare.com/fr-fr/tag/engineering/)
  * [Entropie](https://blog.cloudflare.com/fr-fr/tag/entropy/)
  * [Fancy Bear (FR)](https://blog.cloudflare.com/fr-fr/tag/fancy-bear/)
  * [Forrester](https://blog.cloudflare.com/fr-fr/tag/forrester/)
  * [Foundation DNS (FR)](https://blog.cloudflare.com/fr-fr/tag/foundation-dns/)
  * [Lettre des fondateurs](https://blog.cloudflare.com/fr-fr/tag/founders-letter/)
  * [France (FR)](https://blog.cloudflare.com/fr-fr/tag/france/)
  * [Fraude](https://blog.cloudflare.com/fr-fr/tag/fraud/)
  * [Free (FR)](https://blog.cloudflare.com/fr-fr/tag/free/)
  * [Freedom of Speech (FR)](https://blog.cloudflare.com/fr-fr/tag/freedom-of-speech/)
  * [Front-end](https://blog.cloudflare.com/fr-fr/tag/front-end/)
  * [full-stack](https://blog.cloudflare.com/fr-fr/tag/full-stack/)
  * [Gartner (FR)](https://blog.cloudflare.com/fr-fr/tag/gartner/)
  * [Gatebot (FR)](https://blog.cloudflare.com/fr-fr/tag/gatebot/)
  * [GDPR (FR)](https://blog.cloudflare.com/fr-fr/tag/gdpr/)
  * [Disponibilité générale](https://blog.cloudflare.com/fr-fr/tag/general-availability/)
  * [IA générative](https://blog.cloudflare.com/fr-fr/tag/generative-ai/)
  * [Geo Key Manager (FR)](https://blog.cloudflare.com/fr-fr/tag/geo-key-manager/)
  * [Germany (FR)](https://blog.cloudflare.com/fr-fr/tag/germany/)
  * [GitHub](https://blog.cloudflare.com/fr-fr/tag/github/)
  * [Google Cloud](https://blog.cloudflare.com/fr-fr/tag/google-cloud/)
  * [HTTP2 (FR)](https://blog.cloudflare.com/fr-fr/tag/http2/)
  * [Hyperdrive](https://blog.cloudflare.com/fr-fr/tag/hyperdrive/)
  * [impact](https://blog.cloudflare.com/fr-fr/tag/impact/)
  * [Impact Week (FR)](https://blog.cloudflare.com/fr-fr/tag/impact-week/)
  * [Intel](https://blog.cloudflare.com/fr-fr/tag/intel/)
  * [Interconnection](https://blog.cloudflare.com/fr-fr/tag/interconnection/)
  * [Performances d'Internet](https://blog.cloudflare.com/fr-fr/tag/internet-performance/)
  * [Qualité d'Internet](https://blog.cloudflare.com/fr-fr/tag/internet-quality/)
  * [Coupure d'Internet](https://blog.cloudflare.com/fr-fr/tag/internet-shutdown/)
  * [Trafic Internet](https://blog.cloudflare.com/fr-fr/tag/internet-traffic/)
  * [Tendances Internet](https://blog.cloudflare.com/fr-fr/tag/internet-trends/)
  * [JAMstack (FR)](https://blog.cloudflare.com/fr-fr/tag/jamstack/)
  * [Jengo (FR)](https://blog.cloudflare.com/fr-fr/tag/jengo/)
  * [Killnet (FR)](https://blog.cloudflare.com/fr-fr/tag/killnet/)
  * [Amérique latine](https://blog.cloudflare.com/fr-fr/tag/latin-america/)
  * [LavaRand](https://blog.cloudflare.com/fr-fr/tag/lavarand/)
  * [Lazarus Group (FR)](https://blog.cloudflare.com/fr-fr/tag/lazarus-group/)
  * [La vie chez Cloudflare](https://blog.cloudflare.com/fr-fr/tag/life-at-cloudflare/)
  * [Lisbonne](https://blog.cloudflare.com/fr-fr/tag/lisbon/)
  * [LLM](https://blog.cloudflare.com/fr-fr/tag/llm/)
  * [Log4J (FR)](https://blog.cloudflare.com/fr-fr/tag/log4j/)
  * [Log4Shell (FR)](https://blog.cloudflare.com/fr-fr/tag/log4shell/)
  * [Logs (FR)](https://blog.cloudflare.com/fr-fr/tag/logs/)
  * [MCP](https://blog.cloudflare.com/fr-fr/tag/mcp/)
  * [Meris (FR)](https://blog.cloudflare.com/fr-fr/tag/meris/)
  * [Microsoft Azure (FR)](https://blog.cloudflare.com/fr-fr/tag/microsoft-azure/)
  * [Mirai](https://blog.cloudflare.com/fr-fr/tag/mirai/)
  * [Mobile (FR)](https://blog.cloudflare.com/fr-fr/tag/mobile/)
  * [Model Context Protocol,](https://blog.cloudflare.com/fr-fr/tag/model-context-protocol/)
  * [Multi-Cloud (FR)](https://blog.cloudflare.com/fr-fr/tag/multi-cloud/)
  * [MySQL](https://blog.cloudflare.com/fr-fr/tag/mysql/)
  * [NaaS (FR)](https://blog.cloudflare.com/fr-fr/tag/naas/)
  * [Network Interconnect (FR)](https://blog.cloudflare.com/fr-fr/tag/network-interconnect/)
  * [Network Protection (FR)](https://blog.cloudflare.com/fr-fr/tag/network-protection/)
  * [Services réseau](https://blog.cloudflare.com/fr-fr/tag/network-services/)
  * [NGINX](https://blog.cloudflare.com/fr-fr/tag/nginx/)
  * [Notifications (FR)](https://blog.cloudflare.com/fr-fr/tag/notifications/)
  * [Bureaux](https://blog.cloudflare.com/fr-fr/tag/offices/)
  * [Olympics (FR)](https://blog.cloudflare.com/fr-fr/tag/olympics/)
  * [Panne](https://blog.cloudflare.com/fr-fr/tag/outage/)
  * [Partenaires](https://blog.cloudflare.com/fr-fr/tag/partners/)
  * [PCI Certified (FR)](https://blog.cloudflare.com/fr-fr/tag/pci-certified/)
  * [Peering (FR)](https://blog.cloudflare.com/fr-fr/tag/peering/)
  * [Performances](https://blog.cloudflare.com/fr-fr/tag/performance/)
  * [Phishing](https://blog.cloudflare.com/fr-fr/tag/phishing/)
  * [Pipelines](https://blog.cloudflare.com/fr-fr/tag/pipelines/)
  * [Politique et juridique](https://blog.cloudflare.com/fr-fr/tag/policy/)
  * [Portugal](https://blog.cloudflare.com/fr-fr/tag/portugal/)
  * [Analyse post-incident](https://blog.cloudflare.com/fr-fr/tag/post-mortem/)
  * [Le post-quantique](https://blog.cloudflare.com/fr-fr/tag/post-quantum/)
  * [Confidentialité](https://blog.cloudflare.com/fr-fr/tag/privacy/)
  * [Nouveautés produits](https://blog.cloudflare.com/fr-fr/tag/product-news/)
  * [Projet Galileo](https://blog.cloudflare.com/fr-fr/tag/project-galileo/)
  * [Project Safekeeping (FR)](https://blog.cloudflare.com/fr-fr/tag/project-safekeeping/)
  * [Python (FR)](https://blog.cloudflare.com/fr-fr/tag/python/)
  * [Queues](https://blog.cloudflare.com/fr-fr/tag/queues/)
  * [R2 Super Slurper](https://blog.cloudflare.com/fr-fr/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/fr-fr/tag/cloudflare-radar/)
  * [Radar API (FR)](https://blog.cloudflare.com/fr-fr/tag/radar-api/)
  * [Éléments aléatoires](https://blog.cloudflare.com/fr-fr/tag/randomness/)
  * [Attaques avec demande de rançon](https://blog.cloudflare.com/fr-fr/tag/ransom-attacks/)
  * [Rapid Reset (FR)](https://blog.cloudflare.com/fr-fr/tag/rapid-reset/)
  * [Rate Limiting (FR)](https://blog.cloudflare.com/fr-fr/tag/rate-limiting/)
  * [Reading List (FR)](https://blog.cloudflare.com/fr-fr/tag/reading-list/)
  * [Temps réel](https://blog.cloudflare.com/fr-fr/tag/real-time/)
  * [Regional Services (FR)](https://blog.cloudflare.com/fr-fr/tag/regional-services/)
  * [Serveur d'inscription](https://blog.cloudflare.com/fr-fr/tag/registrar/)
  * [Recherche](https://blog.cloudflare.com/fr-fr/tag/research/)
  * [REvil (FR)](https://blog.cloudflare.com/fr-fr/tag/revil/)
  * [Gestion des risques](https://blog.cloudflare.com/fr-fr/tag/risk-management/)
  * [Routing (FR)](https://blog.cloudflare.com/fr-fr/tag/routing/)
  * [Rust](https://blog.cloudflare.com/fr-fr/tag/rust/)
  * [Saas (FR)](https://blog.cloudflare.com/fr-fr/tag/saas/)
  * [Sécurité SaaS](https://blog.cloudflare.com/fr-fr/tag/saas-security/)
  * [Sable (FR)](https://blog.cloudflare.com/fr-fr/tag/sable/)
  * [Sandbox](https://blog.cloudflare.com/fr-fr/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/fr-fr/tag/sase/)
  * [SDK](https://blog.cloudflare.com/fr-fr/tag/sdk/)
  * [Passerelle web sécurisée](https://blog.cloudflare.com/fr-fr/tag/secure-web-gateway/)
  * [Sécurité](https://blog.cloudflare.com/fr-fr/tag/security/)
  * [Centre de sécurité](https://blog.cloudflare.com/fr-fr/tag/security-center/)
  * [Security Posture (FR)](https://blog.cloudflare.com/fr-fr/tag/security-posture/)
  * [Gestion du niveau de sécurité](https://blog.cloudflare.com/fr-fr/tag/security-posture-management/)
  * [Security Service Edge (FR)](https://blog.cloudflare.com/fr-fr/tag/security-service-edge/)
  * [Security Week](https://blog.cloudflare.com/fr-fr/tag/security-week/)
  * [Serverless](https://blog.cloudflare.com/fr-fr/tag/serverless/)
  * [SIEM (FR)](https://blog.cloudflare.com/fr-fr/tag/siem/)
  * [SIM (FR)](https://blog.cloudflare.com/fr-fr/tag/sim/)
  * [South America (FR)](https://blog.cloudflare.com/fr-fr/tag/south-america/)
  * [Rapidité](https://blog.cloudflare.com/fr-fr/tag/speed/)
  * [Rapidité et fiabilité](https://blog.cloudflare.com/fr-fr/tag/speed-and-reliability/)
  * [Speed Week (FR)](https://blog.cloudflare.com/fr-fr/tag/speed-week/)
  * [Sports (FR)](https://blog.cloudflare.com/fr-fr/tag/sports/)
  * [SSE (FR)](https://blog.cloudflare.com/fr-fr/tag/sse/)
  * [Stockage](https://blog.cloudflare.com/fr-fr/tag/storage/)
  * [Sumo Logic (FR)](https://blog.cloudflare.com/fr-fr/tag/sumo-logic/)
  * [Supercloud (FR)](https://blog.cloudflare.com/fr-fr/tag/supercloud/)
  * [Sustainability (FR)](https://blog.cloudflare.com/fr-fr/tag/sustainability/)
  * [SYN Flood (FR)](https://blog.cloudflare.com/fr-fr/tag/syn-flood/)
  * [L’équipe](https://blog.cloudflare.com/fr-fr/tag/team/)
  * [Teams Dashboard (FR)](https://blog.cloudflare.com/fr-fr/tag/teams-dashboard/)
  * [Testing (FR)](https://blog.cloudflare.com/fr-fr/tag/testing/)
  * [Informations sur les menaces](https://blog.cloudflare.com/fr-fr/tag/threat-intelligence/)
  * [Opérations liées aux menaces](https://blog.cloudflare.com/fr-fr/tag/threat-operations/)
  * [Menaces](https://blog.cloudflare.com/fr-fr/tag/threats/)
  * [Tor (FR)](https://blog.cloudflare.com/fr-fr/tag/tor/)
  * [Transparence](https://blog.cloudflare.com/fr-fr/tag/transparency/)
  * [Tendances](https://blog.cloudflare.com/fr-fr/tag/trends/)
  * [Trust & Safety (FR)](https://blog.cloudflare.com/fr-fr/tag/trust-and-safety/)
  * [Serveur TURN](https://blog.cloudflare.com/fr-fr/tag/turn-server/)
  * [Vectorize (FR)](https://blog.cloudflare.com/fr-fr/tag/vectorize/)
  * [VoiP (FR)](https://blog.cloudflare.com/fr-fr/tag/voip/)
  * [Pare-feu WAF](https://blog.cloudflare.com/fr-fr/tag/waf/)
  * [Waiting Room (FR)](https://blog.cloudflare.com/fr-fr/tag/waiting-room/)
  * [WARP Connector (FR)](https://blog.cloudflare.com/fr-fr/tag/warp-connector/)
  * [WASM (FR)](https://blog.cloudflare.com/fr-fr/tag/wasm/)
  * [Pare-feu d'applications web](https://blog.cloudflare.com/fr-fr/tag/web-application-firewall/)
  * [WebAssembly (FR)](https://blog.cloudflare.com/fr-fr/tag/webassembly/)
  * [WebRTC](https://blog.cloudflare.com/fr-fr/tag/webrtc/)
  * [Workers AI](https://blog.cloudflare.com/fr-fr/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/fr-fr/tag/workers-launchpad/)
  * [Workers VPC](https://blog.cloudflare.com/fr-fr/tag/workers-vpc/)
  * [des flux de travail](https://blog.cloudflare.com/fr-fr/tag/workflows/)
  * [x402](https://blog.cloudflare.com/fr-fr/tag/x402/)
  * [Bilan de l'année](https://blog.cloudflare.com/fr-fr/tag/year-in-review/)
  * [Zero Day Threats (FR)](https://blog.cloudflare.com/fr-fr/tag/zero-day-threats/)
  * [Zero Trust](https://blog.cloudflare.com/fr-fr/tag/zero-trust/)
  * [Zero Trust Week (FR)](https://blog.cloudflare.com/fr-fr/tag/zero-trust-week/)



[Rate Limiting (FR)](https://blog.cloudflare.com/fr-fr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/fr-fr/tag/sdk/)

[Cloudflare Workers](https://blog.cloudflare.com/fr-fr/tag/workers/)[Developer Week](https://blog.cloudflare.com/fr-fr/tag/developer-week/)[Observability](https://blog.cloudflare.com/fr-fr/tag/observability/)[Rate Limiting (FR)](https://blog.cloudflare.com/fr-fr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/fr-fr/tag/sdk/)

4 avril 2024

# Nouveaux outils pour la sécurité de la production : déploiements graduels, Stack Traces, contrôle du volume de requêtes et nouveaux SDK

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/fr-fr/author/tanushree/) et [Jacob Bednarz](https://blog.cloudflare.com/fr-fr/author/jacob-bednarz/)

Lecture : 16 min.

Copier l'URL

Cet article est également disponible en [English](https://blog.cloudflare.com/workers-production-safety/), [Deutsch](https://blog.cloudflare.com/de-de/workers-production-safety/), [Español](https://blog.cloudflare.com/es-es/workers-production-safety/), [日本語](https://blog.cloudflare.com/ja-jp/workers-production-safety/), [한국어](https://blog.cloudflare.com/ko-kr/workers-production-safety/), [繁體中文](https://blog.cloudflare.com/zh-tw/workers-production-safety/) et [简体中文](https://blog.cloudflare.com/zh-cn/workers-production-safety/).

![New tools for production safety — Gradual deployments, Source maps, Rate Limiting, and new SDKs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FR4MNGHSCH0P7DD7P68W.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+//769vXz8fDw8vHx9PLy8u7u6+fl/////vz98vT16+7y6+7z7u/17ezw5+Tm/////f3/8PP55u315ez36O356Orz5OPq////////8vb+5/D65e/85+/+6Oz55Obv////////+f3/7/f/7Pb/7fb/7fL/6uz2////////////+///+P7/9/7/9fr/8vT8/////////////////////////P//+Pv/////////////////////////////+/3/)

L'édition 2024 de la Developer Week est consacrée à la préparation à la production. Le lundi 1er avril, nous avons [annoncé](https://blog.cloudflare.com/fr-fr/making-full-stack-easier-d1-ga-hyperdrive-queues-fr-fr/) que [D1](https://developers.cloudflare.com/d1/), [Queues](https://developers.cloudflare.com/queues/), [Hyperdrive](https://developers.cloudflare.com/hyperdrive/) et [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) sont désormais prêts pour le déploiement en production et accessibles en disponibilité générale. Le mardi 2 avril, nous avons effectué une [annonce](https://blog.cloudflare.com/fr-fr/workers-ai-ga-huggingface-loras-python-support-fr-fr/) identique au sujet de notre plateforme d'inférence [Workers AI](https://developers.cloudflare.com/workers-ai/). Et nous n'avons pas encore fini !

Cependant, l'état de préparation à la production ne dépend pas uniquement de l'ampleur et la fiabilité des services avec lesquels vous développez des solutions. Vous devez également disposer d'outils permettant d'apporter des modifications de manière sûre et fiable. Vous dépendez non seulement des outils que fournit Cloudflare, mais également de la capacité de contrôler et d'adapter précisément le comportement de Cloudflare aux besoins de votre application.

Aujourd'hui, nous annonçons cinq mises à jour conçues pour mettre davantage de puissance entre vos mains (les déploiements graduels, les traces d'appels mappées à la source dans Tail Workers, une nouvelle API de contrôle du volume de requêtes, de nouveaux SDK pour API et des mises à jour de Durable Objects), chacune développée en gardant à l'esprit les services de production essentiels à l'activité. Nous développons nous-mêmes nos produits avec Workers (notamment [Access](https://developers.cloudflare.com/cloudflare-one/policies/access/), [R2](https://developers.cloudflare.com/r2/), [KV](https://developers.cloudflare.com/kv/) [Waiting Room](https://developers.cloudflare.com/waiting-room/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Queues](https://developers.cloudflare.com/queues/) [Stream](https://developers.cloudflare.com/stream/) et bien d'autres), et nous dépendons nous-mêmes de chacune de ces nouvelles fonctionnalités pour nous assurer que nos services sont prêts pour la production – et nous sommes aujourd'hui ravis de les proposer à tous les utilisateurs.

### Déployez graduellement les modifications dans Workers et Durable Objects

Le déploiement d'une instance Workers est presque instantané ; en quelques secondes seulement, votre modification est en ligne [partout](https://www.cloudflare.com/network/).

Lorsque votre solution est prête pour un déploiement en production, chaque modification apportée comporte un risque plus important, tant en termes de volume que d'attentes. Vous devez respecter votre contrat de niveau de service (SLA) avec garantie de disponibilité de 99,99 %, ou vous avez un ambitieux objectif de niveau de service (SLO) de latence de P90. L'échec d'un déploiement traitant 100 % du trafic pendant 45 secondes peut entraîner des millions de requêtes infructueuses. Si elle est déployée en une seule fois, une modification subtile du code peut provoquer l'envoi d'un véritable déluge de tentatives à un backend déjà saturé. Ce sont les types de risques que nous prenons en compte et que nous atténuons nous-mêmes pour nos services développés sur Workers.

L'approche pour limiter ces risques consiste à déployer les changements graduellement – ce que l'on appelle communément des déploiements progressifs :

  1. La version actuelle de votre application s'exécute en production.
  2. Vous déployez la nouvelle version de votre application en production, mais vous n'acheminez qu'un petit pourcentage du trafic vers cette nouvelle version et vous attendez qu'elle « absorbe » la production, en surveillant les régressions et les bugs. Si un incident se produit, vous pouvez le détecter précocement, avec un faible pourcentage (par exemple, 1 %) du trafic, et vous pouvez rapidement effectuer une restauration.
  3. Vous augmentez ensuite progressivement le pourcentage de trafic, jusqu'à ce que la nouvelle version reçoive 100 % du trafic ; à ce stade, son déploiement est alors finalisé.



Aujourd'hui, nous proposons une méthode exceptionnelle pour déployer progressivement les modifications de code sur Workers et Durable Objects via l'[API Cloudflare](https://developers.cloudflare.com/api/operations/worker-deployments-list-deployments), l'[interface de ligne de commande Wrangler](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-wrangler) ou le [tableau de bord de Workers](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-the-cloudflare-dashboard). Les déploiements graduels entrent en phase de bêta ouverte ; vous pouvez utiliser les déploiements graduels avec n'importe quel compte Cloudflare ayant souscrit à l'[offre gratuite Workers](https://developers.cloudflare.com/workers/platform/pricing/#workers), et vous pourrez très prochainement commencer à utiliser les déploiements graduels avec des comptes Cloudflare ayant souscrit l'[offre payante de Workers](https://developers.cloudflare.com/workers/platform/pricing/#workers) et l'offre Enterprise. Une bannière sera affichée sur le tableau de bord Workers lorsque votre compte y aura accès.

Si vous exécutez simultanément deux versions de votre instance Workers ou votre instance Durable Objects dans votre environnement de production, vous souhaitez certainement pouvoir filtrer vos indicateurs, vos exceptions et journaux par version. Ceci peut vous aider à identifier rapidement les problèmes de production, lorsque la nouvelle version n'est déployée que pour un petit pourcentage du trafic, ou à comparer les indicateurs de performance, lorsque le trafic est réparti à parts égales. Nous avons également ajouté l'observabilité au niveau de la version à l'échelle de notre plateforme :

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Splitting traffic between different versions of a Worker.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4792EFMEWR5SFVJAMDC49A.png&w=715&h=353&f=webp&fit=cover&position=center)

  * Vous pouvez filtrer les analyses de données par version depuis le tableau de bord Workers et via l'[API GraphQL Analytics](https://developers.cloudflare.com/analytics/graphql-api/).
  * Les événements [Workers Trace Events](https://developers.cloudflare.com/workers/observability/logging/logpush/) et [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) incluent l'identifiant de version de votre instance Workers, ainsi que des champs facultatifs de message de version et d'identifiant de version.
  * Lorsque vous utilisez [wrangler tail](https://developers.cloudflare.com/workers/wrangler/commands/#tail) pour afficher les journaux en direct, vous pouvez afficher les journaux pour une version spécifique.
  * Vous pouvez accéder à l'identifiant, au message et à la balise de version depuis le code de votre instance Workers, en configurant la [liaison des métadonnées de version](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/).



Vous pouvez également souhaiter vous assurer que chaque client ou utilisateur ne voit qu'une version cohérente de votre instance Workers. Nous avons ajouté l'[affinité de version](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity), afin d'assurer que les requêtes associées à un identifiant particulier (telles que l'utilisateur, la session ou tout autre identifiant unique) soient toujours traitées par une version cohérente de votre instance Workers. L'[affinité de session](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity), lorsqu'elle est utilisée avec le [moteur d'ensembles de règles](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#setting-cloudflare-workers-version-key-using-ruleset-engine), vous offre un contrôle total sur le mécanisme et l'identifiant utilisés pour garantir la « persistance ».

Les déploiements graduels entrent dans la phase de bêta ouverte. Tandis que nous progressons vers la disponibilité générale, nous nous employons à déployer les fonctionnalités suivantes :

  * **Remplacements de version.** Invoquez une version spécifique de votre instance Workers afin de réaliser des tests avant de l'utiliser pour servir du trafic de production. Cela vous permettra d'effectuer des déploiements bleu/vert.
  * **Cloudflare Pages.** Laissez le système CI/CD de Cloudflare Pages faire évoluer automatiquement les déploiements à votre place.
  * **Restaurations automatiques.** Revenez automatiquement en arrière lorsque le taux d'erreurs augmente pour une nouvelle version de votre instance Workers.



Nous sommes impatients d'entendre vos commentaires ! Utilisez [ce formulaire de commentaires](https://www.cloudflare.com/lp/developer-week-deployments/) pour nous faire part de vos réflexions ou contactez-nous sur notre [Discord pour développeurs](https://discord.gg/HJvPcPcN), sur le canal #workers-gradual-deployments-beta.

### Traces de pile mappées à la source dans Tail Workers

L'état de préparation à la production exige d'assurer le suivi des erreurs et des exceptions, avec l'objectif de les réduire à zéro. Lorsqu'une erreur se produit, la première chose que vous souhaitez généralement examiner est la [trace d'appels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack) de l'erreur – c'est-à-dire les fonctions spécifiques qui ont été appelées, dans quel ordre, depuis quelle ligne et quel fichier, et avec quels arguments.

La plupart du code JavaScript (pas uniquement exécuté sur Workers, mais sur toutes les plateformes) est d'abord groupé, souvent compilé de source à source (ou « transpilé »), puis minifié avant d'être déployé en production. Cette opération se déroule en tâche de fond, afin de créer des bundles plus petits, permettant d'optimiser les performances et de convertir le code Typescript en code JavaScript, si nécessaire.

Si vous avez déjà vu une exception renvoyer une trace d'appels telle que /src/index.js:1:342, cela signifie que l'erreur s'est produite au 342e caractère du code minifié de votre fonction... ce qui n'est évidemment pas très utile pour le débogage.

Les [cartes des sources](https://web.dev/articles/source-maps) permettent de résoudre ce problème : elles renvoient le code compilé et minifié au code original que vous avez écrit. Les cartes des sources sont combinées avec la trace d'appels renvoyée par le runtime JavaScript, afin de présenter une trace de pile lisible par l'humain. Par exemple, la trace d'appels suivante montre que l'instance Workers a reçu une valeur null inattendue à la ligne 30 du fichier down.ts. Il s'agit d'un point de départ utile pour le débogage, et vous pouvez approfondir l'examen de la trace d'appels afin de comprendre les fonctions qui ont été appelées, et dont la définition a entraîné la valeur null.

Voici comment elle fonctionne :
    
    
    Unexpected input value: null
      at parseBytes (src/down.ts:30:8)
      at down_default (src/down.ts:10:19)
      at Object.fetch (src/index.ts:11:12)

  1. Si vous définissez upload_source_maps = true dans le fichier [wrangler.toml](https://developers.cloudflare.com/workers/wrangler/configuration/), Wrangler génère et transfère automatiquement tout fichier de carte des sources lorsque vous exécutez [wrangler deploy](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) ou [wrangler versions upload](https://developers.cloudflare.com/workers/wrangler/commands/#versions).
  2. Lorsque votre instance Workers lance une exception non détectée, nous récupérons la carte de sources et nous l'utilisons pour mapper la trace d'appels de l'exception avec les lignes du code source original de votre instance Workers.
  3. Vous pouvez ensuite visualiser cette trace de pile désobfusquée dans les [journaux en temps réel](https://developers.cloudflare.com/workers/observability/logging/real-time-logs/) ou dans [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/).



À partir d'aujourd'hui, la version bêta ouverte vous permet de transférer des cartes des sources vers Cloudflare lorsque vous déployez votre instance Workers. Pour faire vos premiers pas, [vous pouvez commencer par lire la documentation](https://developers.cloudflare.com/workers/observability/source-maps), et à partir du 15 avril, le runtime Workers commencera à utiliser les cartes des sources pour désobfusquer les traces d'appels. Lorsque les traces d'appels mappées à la source seront disponibles, nous afficherons une notification sur le tableau de bord de Cloudflare et nous publierons un message sur le [compte X Cloudflare Developers](https://twitter.com/CloudflareDev?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor).

### Nouvelle API de contrôle du volume de requêtes API dans Workers

Une API n'est prête pour la production que si elle dispose d'une fonctionnalité offrant un [contrôle du volume de requêtes](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/) raisonnable. Au fur et à mesure que vous développez votre solution, la complexité et la diversité des contrôles que vous devez appliquer pour équilibrer les besoins de clients spécifiques, protéger l'intégrité de votre service ou appliquer et ajuster les limites dans des scénarios spécifiques augmentent également. L'API de Cloudflare est confrontée à ce défi : chacun de nos dizaines de produits, comportant chacun de nombreux points de terminaison d'API, peut avoir besoin d'appliquer différents contrôles du volume de requêtes.

Depuis 2017, vous pouvez configurer les [règles de contrôle du volume de requêtes](https://developers.cloudflare.com/waf/rate-limiting-rules/) sur Cloudflare. Jusqu'à aujourd'hui, toutefois, la seule façon de contrôler cette fonctionnalité était depuis le tableau de bord Cloudflare ou via l'API Cloudflare. Il n'était pas possible de définir un comportement au niveau du _runtime_ ou, dans une instance Workers, d'écrire du code qui interagit directement avec le contrôle du volume de requêtes. Vous pouviez uniquement choisir d'appliquer ou non le contrôle du volume à une requête avant qu'elle n'atteigne votre instance Workers.

Aujourd'hui, nous inaugurons une nouvelle API, en version bêta ouverte, qui vous permet d'accéder directement au contrôle du volume de requêtes depuis votre instance Workers. Elle est ultra-rapide, conçue sur la base de memcached, et très simple à ajouter à votre instance Workers. Par exemple, la configuration suivante définit un contrôle du volume de requêtes de 100 requêtes sur une période de 60 secondes :

Ensuite, dans votre instance Workers, vous pouvez appeler la méthode de contrôle du volume de requêtes pour la liaison RATE_LIMITER, en fournissant une clé de votre choix. Compte tenu de la configuration ci-dessus, ce code renverra un code d'état de réponse [HTTP 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) si plus de 100 requêtes vers un chemin spécifique sont transmises dans un délai de 60 secondes :
    
    
    [[unsafe.bindings]]
    name = "RATE_LIMITER"
    type = "ratelimit"
    namespace_id = "1001" # An identifier unique to your Cloudflare account
    
    # Limit: the number of tokens allowed within a given period, in a single Cloudflare location
    # Period: the duration of the period, in seconds. Must be either 60 or 10
    simple = { limit = 100, period = 60 } 

Maintenant que Workers peut se connecter directement à un magasin de données comme memcached, que pouvons-nous fournir d'autre ? Des compteurs ? Des verrous ? Un [cache en mémoire](https://github.com/cloudflare/workerd/pull/1666) ? Le contrôle du volume de requêtes est la première des nombreuses primitives que nous envisageons de fournir dans Workers, afin de répondre aux questions que nous recevons, depuis des années, sur l'emplacement où devrait résider un état partagé temporaire couvrant plusieurs [isolats](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates) Workers. Si aujourd'hui, vous comptez intégrer l'état à la portée globale de votre instance Workers, nous développons actuellement de meilleures primitives, conçues pour des scénarios d'utilisation spécifiques.
    
    
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

L'API de contrôle du volume de requêtes dans Workers est en version bêta ouverte, et vous pouvez commencer en [consultant la documentation](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit).

### Nouveaux SDK générés automatiquement pour l'API de Cloudflare

L'état de préparation à la production implique d'évoluer de l'approche consistant à effectuer des modifications en cliquant sur des boutons dans un tableau de bord vers une approche programmatique, en utilisant un service « d'infrastructure en tant que code » tel que [Terraform](https://github.com/cloudflare/terraform-provider-cloudflare) ou [Pulumi](https://github.com/pulumi/pulumi-cloudflare) ou en transmettant directement des requêtes d'API, soit par vos propres moyens, soit par l'intermédiaire d'un SDK.

L'[API de Cloudflare](https://developers.cloudflare.com/api/) est colossale et reçoit continuellement de nouvelles fonctionnalités ; en moyenne, nous [mettons à jour nos schémas d'API entre 20 et 30 fois par jour](https://github.com/cloudflare/api-schemas/activity). Jusqu'à présent toutefois, nos SDK d'API ont fait l'objet d'un développement et d'une maintenance manuels, et nous ressentions donc un besoin urgent d'automatiser cette approche.

C'est ce que nous avons fait, et nous annonçons aujourd'hui de nouveaux SDK pour l'API Cloudflare dans trois langages ([Typescript](https://github.com/cloudflare/cloudflare-typescript), [Python](https://github.com/cloudflare/cloudflare-python) et [Go](https://github.com/cloudflare/cloudflare-go)) ; d'autres langages seront pris en charge prochainement.

Chaque SDK est généré automatiquement avec l'[API Stainless](https://www.stainlessapi.com/), sur la base des [schémas OpenAPI](https://github.com/cloudflare/api-schemas) qui définissent la structure et les fonctionnalités de chacun de nos points de terminaison d'API. Cela signifie que lorsque nous ajoutons une nouvelle fonctionnalité à l'API Cloudflare, pour n'importe quel produit Cloudflare, ces SDK d'API sont automatiquement régénérés et de nouvelles versions sont publiées, garantissant qu'elles sont correctes et à jour.

Vous pouvez installer les SDK en exécutant l'une des commandes suivantes :

Si vous utilisez Terraform ou Pulumi, dans l'envers du décor, le fournisseur Terraform de Cloudflare utilise actuellement le [SDK Go](https://github.com/cloudflare/cloudflare-go) existant, non automatisé. Lorsque vous exécutez terraform apply, le fournisseur Terraform de Cloudflare détermine quelles requêtes d'API doivent être transmises et dans quel ordre, puis les exécute à l'aide du SDK Go.
    
    
    // Typescript
    npm install cloudflare
    
    // Python
    pip install cloudflare
    
    // Go
    go get -u github.com/cloudflare/cloudflare-go/v2

Le nouveau SDK Go généré automatiquement ouvre la voie à une prise en charge plus complète de Terraform pour tous les produits Cloudflare, fournissant ainsi un ensemble de base d'outils dont vous pouvez avoir l'assurance qu'ils sont à la fois corrects et à jour des dernières modifications de l'API. Nous nous dirigeons vers un avenir où chaque fois qu'une équipe produit de Cloudflare crée une nouvelle fonctionnalité exposée via l'API Cloudflare, elle est automatiquement prise en charge par les SDK. Attendez-vous à de nouvelles mises à jour tout au long de l'année 2024.

### Disponibilité générale des analyses de données de l'espace de noms de Durable Objects et de WebSocket Hibernation

Nous développons un grand nombre de nos produits, parmi lesquels [Waiting Room](https://developers.cloudflare.com/waiting-room/), [R2](https://developers.cloudflare.com/r2/) et [Queues](https://developers.cloudflare.com/queues/), ainsi que des plateformes telles [PartyKit](https://www.partykit.io/), avec [Durable Objects](https://developers.cloudflare.com/durable-objects/). Durable Objects est désormais déployé dans le monde entier, avec une nouvelle prise en charge pour la région Océanie ; vous pouvez considérer la solution comme un ensemble de singletons d'instances Workers pouvant fournir un point de coordination unique et un [état persistant](https://developers.cloudflare.com/durable-objects/api/transactional-storage-api/). Ces éléments sont parfaits pour les applications qui nécessitent une coordination en temps réel des utilisateurs, à l'image des chats interactifs ou de l'édition collaborative. Croyez-en la parole d'Atlassian :

> _Parmi les nouvelles fonctionnalités que nous proposons figurent les_ _[tableaux blancs de Confluence](https://www.atlassian.com/software/confluence/whiteboards), qui offrent un moyen libre de capturer le travail non structuré (par exemple, un brainstorming ou une planification précoce) avant qu'il ne soit documenté de manière plus formelle par les équipes. L'équipe a envisagé de nombreuses options pour la collaboration en temps réel, et a finalement décidé d'utiliser la solution Durable Objects de Cloudflare. Durable Objects s'est avéré être fantastiquement bien adapté à cet espace problématique, en proposant une combinaison unique de fonctionnalités qui nous a permis de simplifier considérablement notre infrastructure et d'évoluer facilement vers un grand nombre d'utilisateurs. –_ [_Atlassian_](https://www.atlassian.com/software/confluence/whiteboards)

Nous n'avions auparavant pas exposé les tendances analytiques associées dans le tableau de bord, ce qui rendait difficile la compréhension des modèles d'utilisation et des taux d'erreur dans un [espace de noms Durable Objects](https://developers.cloudflare.com/durable-objects/configuration/access-durable-object-from-a-worker/#generate-ids-randomly), à moins d'utiliser directement l'[API GraphQL Analytics](https://developers.cloudflare.com/analytics/graphql-api/). Le [tableau de bord Durable Objects](https://dash.cloudflare.com/?to=/:account/workers/durable-objects) a maintenant été remanié, vous permettant d'approfondir les indicateurs autant que vous le souhaitez.

Dès le [premier jour](https://blog.cloudflare.com/introducing-workers-durable-objects), Durable Objects a pris en charge les [protocoles WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), permettant à de nombreux clients de se connecter directement à une instance Durable Objects pour l'envoi et la réception de messages.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2305 Embedded Image - tUWMOW](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NGJQ7SMHCNME7M5TATPN.png&w=715&h=557&f=webp&fit=cover&position=center)

Cependant, il arrive que l'application client ouvre une connexion WebSocket, puis cesse de faire que ce soit. Pensez à cet onglet que vous avez laissé ouvert dans votre navigateur pendant les cinq dernières heures, sans y revenir ; s'il utilise les protocoles WebSocket pour envoyer et recevoir des messages, il dispose en réalité d'une connexion TCP de longue durée qui n'est utilisée pour rien. Si cette connexion est établie à une instance Durable Objects, cette dernière doit continuer à fonctionner en attendant qu'un événement se produise, en consommant de la mémoire et en vous coûtant de l'argent.

C'est pour résoudre ce problème que nous avons initialement [lancé WebSocket Hibernation](https://blog.cloudflare.com/workers-pricing-scale-to-zero). Aujourd'hui, nous annonçons que cette fonctionnalité a quitté la phase bêta, et qu'elle est désormais proposée en disponibilité générale. Avec WebSocket Hibernation, vous définissez une réponse automatique à utiliser pendant l'hibernation et vous sérialisez l'état afin qu'il survive à l'hibernation. Cela fournit à Cloudflare les données entrantes dont nous avons besoin pour maintenir les connexions WebSocket ouvertes depuis les clients, tout en « mettant en hibernation » l'instance Durable Objects, afin qu'elle ne fonctionne pas activement et que le temps d'inactivité ne vous soit pas facturé. Le résultat est que votre état est toujours disponible en mémoire lorsque vous en avez réellement besoin, mais qu'il n'est pas conservé inutilement lorsque ce n'est pas le cas. Tant que votre instance Durable Objects est en hibernation, même si des clients actifs sont toujours connectés par le biais d'une instance de protocole WebSocket, cette durée ne vous sera pas facturée.

En outre, les développeurs nous ont fait part de leurs commentaires concernant les coûts des messages WebSocket entrants transmis à Durable Objects, qui privilégie les messages plus petits et plus fréquents pour les communications en temps réel. À partir d'aujourd'hui, les messages WebSocket entrants seront facturés à l'équivalent de 1/20e d'une requête (au lieu d'un message équivalent à une requête, comme c'était le cas jusqu'à présent). Voici un [exemple de tarification](https://developers.cloudflare.com/durable-objects/platform/pricing/#example-4) :

.tg {border-collapse:collapse;border-color:#ccc;border-spacing:0;} .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top} .tg .tg-4kyp{color:#0E101A;text-align:left;vertical-align:top} .tg .tg-bhdc{color:#0E101A;font-weight:bold;text-align:left;vertical-align:top}

| WebSocket Connection Requests | Incoming WebSocket Messages | Billed Requests | Request Billing  
---|---|---|---|---  
Before | 10K | 432M | 432,010,000 | $64.65  
After | 10K | 432M | 21,610,000 | $3.09  
  
Requêtes de connexion WebSocket

Messages WebSocket entrants

Requêtes facturées

Facturation des requêtes

Avant

10K

432M

432 010 000

$64.65

Après

10K

432M

21 610 000

$3.09

### Prêt pour la production, sans la complexité liée à la production

Jusqu'à présent, l'état de préparation à la production sur la nouvelle génération de plateformes cloud exigeait de ralentir la vitesse de livraison. Cela nécessitait d'assembler de nombreux outils déconnectés ou de mettre à l'arrêt des équipes entières afin d'intervenir sur les plateformes internes, et d'adapter vos propres couches de productivité à des plateformes dont la complexité était problématique.

La plateforme pour développeurs de Cloudflare est désormais mature et prête pour la production. Nous nous engageons à proposer une plateforme intégrée, sur laquelle les produits opèrent ensemble de manière intuitive et où il n'existe pas 10 façons différentes de faire une même chose, sans nécessiter une matrice de compatibilité pour aider les utilisateurs à comprendre les services qui fonctionnent ensemble. Chacune de ces mises à jour illustre cette démarche, en intégrant de nouvelles fonctionnalités aux différents produits et composants de la plateforme de Cloudflare.

À cette fin, nous voulons que vous nous disiez non seulement ce que vous voulez voir ensuite, mais également les aspects que nous pourrions encore simplifier, ou encore de quelle manière nos produits pourraient mieux fonctionner ensemble. Dites-nous ce que nous pourrions faire de plus ; le [Discord pour développeurs de Cloudflare](https://discord.cloudflare.com/) est toujours ouvert.

Sur cette page

Discuter en ligne

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fworkers-production-safety%2F&t=Nouveaux%20outils%20pour%20la%20s%C3%A9curit%C3%A9%20de%20la%20production%20%3A%20d%C3%A9ploiements%20graduels%2C%20Stack%20Traces%2C%20contr%C3%B4le%20du%20volume%20de%20requ%C3%AAtes%20et%20nouveaux%20SDK)[](https://x.com/intent/post?text=Nouveaux+outils+pour+la+s%C3%A9curit%C3%A9+de+la+production+%3A+d%C3%A9ploiements+graduels%2C+Stack+Traces%2C+contr%C3%B4le+du+volume+de+requ%C3%AAtes+et+nouveaux+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fworkers-production-safety%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fworkers-production-safety%2F)[](https://bsky.app/intent/compose?text=Nouveaux+outils+pour+la+s%C3%A9curit%C3%A9+de+la+production+%3A+d%C3%A9ploiements+graduels%2C+Stack+Traces%2C+contr%C3%B4le+du+volume+de+requ%C3%AAtes+et+nouveaux+SDK+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fworkers-production-safety%2F)[](https://mastodonshare.com/?text=Nouveaux+outils+pour+la+s%C3%A9curit%C3%A9+de+la+production+%3A+d%C3%A9ploiements+graduels%2C+Stack+Traces%2C+contr%C3%B4le+du+volume+de+requ%C3%AAtes+et+nouveaux+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fworkers-production-safety%2F)[](https://www.threads.net/intent/post?text=Nouveaux+outils+pour+la+s%C3%A9curit%C3%A9+de+la+production+%3A+d%C3%A9ploiements+graduels%2C+Stack+Traces%2C+contr%C3%B4le+du+volume+de+requ%C3%AAtes+et+nouveaux+SDK+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fworkers-production-safety%2F)

## Tags associés

[Cloudflare Workers](https://blog.cloudflare.com/fr-fr/tag/workers/)[Developer Week](https://blog.cloudflare.com/fr-fr/tag/developer-week/)[Observability](https://blog.cloudflare.com/fr-fr/tag/observability/)[Rate Limiting (FR)](https://blog.cloudflare.com/fr-fr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/fr-fr/tag/sdk/)

Suivre sur les réseaux sociaux

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Jacob Bednarz](https://blog.cloudflare.com/fr-fr/author/jacob-bednarz/)

[](https://jacobbednarz.com)




## Abonnez-vous pour recevoir les notifications de nouveaux articles

Adresse e-mail

Nous ne partagerons jamais votre adresse e-mail.

S'abonner

Merci pour votre inscription ! Vérifiez votre boîte de réception pour confirmer.
