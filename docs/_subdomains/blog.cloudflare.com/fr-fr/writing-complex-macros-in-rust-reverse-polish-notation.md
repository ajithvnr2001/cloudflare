---
url: https://blog.cloudflare.com/fr-fr/writing-complex-macros-in-rust-reverse-polish-notation/
title: \u00c9crire des macros complexes dans Rust : Notation polonaise inverse (RPN) | Le blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:21.768402+00:00
---

# Écrire des macros complexes dans Rust : Notation polonaise inverse (RPN) | Le blog Cloudflare

> Source: https://blog.cloudflare.com/fr-fr/writing-complex-macros-in-rust-reverse-polish-notation/

[Blog](https://blog.cloudflare.com/fr-fr/)

[Cloudflare Polish](https://blog.cloudflare.com/fr-fr/tag/cloudflare-polish/)[Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)[Programming](https://blog.cloudflare.com/fr-fr/tag/programming/)+1Afficher 1 étiquettes supplémentaires

4 tagsAfficher 4 tags

  * Tags de l’article
  * [Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)[Rust](https://blog.cloudflare.com/fr-fr/tag/rust/)
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



[Rust](https://blog.cloudflare.com/fr-fr/tag/rust/)

[Cloudflare Polish](https://blog.cloudflare.com/fr-fr/tag/cloudflare-polish/)[Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)[Programming](https://blog.cloudflare.com/fr-fr/tag/programming/)[Rust](https://blog.cloudflare.com/fr-fr/tag/rust/)

31 janvier 2018

# Écrire des macros complexes dans Rust : Notation polonaise inverse (RPN)

![Ingvar Stepanyan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HXZCX2W0E3TV8QJY1YTY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ingvar Stepanyan](https://blog.cloudflare.com/fr-fr/author/ingvar-stepanyan/)

Lecture : 10 min.

Copier l'URL

Cet article est également disponible en [English](https://blog.cloudflare.com/writing-complex-macros-in-rust-reverse-polish-notation/), [Deutsch](https://blog.cloudflare.com/de-de/writing-complex-macros-in-rust-reverse-polish-notation/), [Español](https://blog.cloudflare.com/es-es/writing-complex-macros-in-rust-reverse-polish-notation/), [한국어](https://blog.cloudflare.com/ko-kr/writing-complex-macros-in-rust-reverse-polish-notation/) et [简体中文](https://blog.cloudflare.com/zh-cn/writing-complex-macros-in-rust-reverse-polish-notation/).

![Writing complex macros in Rust: Reverse Polish Notation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49FSNFEYMC4YKNMQ9ZPHFY.jpg&w=640&h=427&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAVmVuTmBtO1drNFRtQ1xzU2Z4V2p4UWl2anV+YW96TmN1Rl91VGd7ZHKCZ3aDYHN/eoSNcX2JXnCBVWp/Y3OGcn6OdoKPb3+KgYuWeIWSZnmKXnSJbHyRe4eZfouad4iVfIiZdISWZXuQYHqSboKafIyhfo+id42dbX+WaH2UXXqUXXyYaoWgd42meJCmcY6iXHORWHSRU3eVWH2bZYWjcIupcI6oaY6lU26OUXCQT3WVVn2cY4WlbYupbI2pZo6m)

(_Ceci est une publication croisée d'un tutoriel_ [_publié à l'origine_](https://rreverser.com/writing-complex-macros-in-rust/) _sur mon blog personnel_)

Rust dispose, entre autres fonctionnalités intéressantes, d’un puissant système de macro. Malheureusement, même après la lecture de The Book et de divers tutoriels, lorsque j'ai essayé d'implémenter une macro impliquant le traitement de listes complexes d'éléments différents, j'ai toujours eu du mal à comprendre comment y parvenir. Et il a fallu un certain temps pour arriver à ce moment de « déclic », et j’ai commencé à mal utiliser les macros pour tout :) (ok, pas tout comme dans _i-am-using-macros-because-i-dont-want-to-use-functions-and-specify-types-and-lifetimes everything comme j'ai vu certaines personnes le faire, mais n'importe où c'est réellement utile)_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Rust with a macro lens](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47AZAKFG11R2WFAJH521KV.jpg&w=640&h=427&f=webp&fit=cover&position=center)

Voici donc mon point de vue sur la description des principes sous-jacents à l’écriture de ces macros. Cela suppose que vous ayez lu la section [Macros](https://doc.rust-lang.org/book/first-edition/macros.html) du The Book et que vous maîtrisiez bien les définitions de macros de base et les types de jetons.

Je prendrai une [notation polonaise inverse](https://en.wikipedia.org/wiki/Reverse_Polish_notation) comme exemple pour ce tutoriel. C'est intéressant parce que c'est assez simple, vous le connaissez peut-être déjà à l'école. Et, pourtant, pour le mettre en œuvre de manière statique au moment de la compilation, vous devez déjà utiliser une approche par macros récursive.

La notation polonaise inverse (également appelée notation postfixe) utilise une pile pour toutes ses opérations, de sorte que n’importe quel opérande est placé sur la pile et que n’importe quel opérateur _[binaire]_ extrait deux opérandes de la pile, évalue le résultat et le restitue. Donc, une expression comme celle-ci :

`2 3 + 4 *`
    
    
    2 3 + 4 *

se traduit par :

  1. Mettez `2` sur la pile.
  2. Mettez `3` sur la pile.
  3. Prenez les deux dernières valeurs de la pile ( `3` et `2`), appliquez l'opérateur `+` et restituez le résultat ( `5`) sur la pile.
  4. Mettez `4` sur la pile.
  5. Prenez les deux dernières valeurs de la pile ( `4` et `5`), appliquez l'opérateur `*` ( `4 * 5` ) et restituez le résultat ( `20`) sur la pile.
  6. En fin d'expression, la valeur unique sur la pile est le résultat ( `20`).



Dans une notation infixe plus courante, utilisée en mathématiques et dans la plupart des langages de programmation modernes, l'expression ressemblerait à `(2 + 3) * 4`.

Écrivons donc une macro qui évaluerait RPN au moment de la compilation en la convertissant en une notation infixe comprise par Rust.
    
    
    macro_rules! rpn {
      // TODO
    }
    
    println!("{}", rpn!(2 3 + 4 *)); // 20

Commençons par placer des chiffres sur la pile.

Actuellement, les macros n'autorisent pas les littéraux de correspondance, et `expr` ne fonctionnera pas pour nous car il peut accidentellement faire correspondre une séquence comme `2 + 3 ...` au lieu de prendre un seul chiffre. Nous allons donc recourir à `tt`, un matcher de combinaison générique qui correspond à un seul arbre de jetons (qu'il s'agisse d'un jeton primitif tel que littérale/identifiant/durée de vie/ etc. ou une expression mise entre parenthèses `()` / `[]` / `{}` \- contenant plus de jetons) :
    
    
    macro_rules! rpn {
      ($num:tt) => {
        // TODO
      };
    }

Maintenant, nous allons avoir besoin d'une variable pour la pile.

Les macros ne peuvent pas utiliser de vraies variables, car nous voulons que cette pile n'existe qu'au moment de la compilation. Donc, au lieu de cela, l’astuce est d’avoir une autre séquence de jetons qui peut être distribuée et utilisée comme une sorte d’accumulateur.

Dans notre cas, représentons-la comme une séquence de `expr` séparée par des virgules (puisque nous l'utilisons non seulement pour les nombres simples, mais également pour les expressions infixes intermédiaires) et encapsulons-la entre crochets pour la séparer du reste de l'entrée :
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt) => {
        // TODO
      };
    }

Maintenant, une séquence de jetons n'est pas vraiment une variable. Vous ne pouvez pas la modifier sur place et faire quelque chose après. Au lieu de cela, vous pouvez créer une nouvelle copie de cette séquence de jetons avec les modifications nécessaires et rappeler de manière récurrente la même macro.

Si vous êtes habitué au langage fonctionnel ou avez déjà travaillé avec une bibliothèque qui fournissait des données immuables auparavant, ces deux approches, à-savoir : la mutation de données par la création d’une copie modifiée et le traitement de listes avec une récursion, vous sont probablement déjà familières :
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt) => {
        rpn!([ $num $(, $stack)* ])
      };
    }

Maintenant, le cas avec un seul chiffre est plutôt improbable et peu intéressant pour nous, nous devrons donc faire correspondre tout ce qui suit ce chiffre sous la forme d'une séquence de zéro ou plusieurs jetons `tt`, qui peut être placée à la prochaine utilisation de notre macro pour une correspondance et un traitement plus poussés :
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
          rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

À ce stade, le support des opérateurs est toujours manquant. Comment réalisons-nous la correspondance des opérateurs ?

Si notre RPN est une séquence de jetons que nous voudrions traiter exactement de la même manière, nous pourrions simplement utiliser une liste telle que `$($ token: tt)*`. Malheureusement, cela ne nous donnerait pas la possibilité de parcourir la liste et de placer un opérande ou d’appliquer un opérateur en fonction de chaque jeton.

The Book dit que « le système de macros ne traite pas du tout l'ambiguïté de l'analyse », et c'est vrai pour une seule branche de macros. Nous ne pouvons pas faire correspondre une séquence de nombres suivie d’un opérateur comme `$ ($ num: tt) * +` car `+` est également un jeton valide et peut être associé au groupe `tt`, mais c’est là que les macros récursives peuvent à nouveau aider.

Si vous avez différentes branches dans votre définition de macro, Rust les essaiera une par une, afin que nous puissions placer nos branches d'opérateurs avant les branches numériques et ainsi éviter tout conflit :
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] + $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] - $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] * $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] / $($rest:tt)*) => {
        // TODO
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

Comme je le disais plus tôt, les opérateurs sont appliqués aux deux derniers chiffres de la pile, nous devrons donc les faire correspondre séparément, « évaluer » le résultat (construire une expression infixe régulière) et le replacer :
    
    
    macro_rules! rpn {
      ([ $b:expr, $a:expr $(, $stack:expr)* ] + $($rest:tt)*) => {
        rpn!([ $a + $b $(, $stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] - $($rest:tt)*) => {
        rpn!([ $a - $b $(, $stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] * $($rest:tt)*) => {
        rpn!([ $a * $b $(,$stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] / $($rest:tt)*) => {
        rpn!([ $a / $b $(,$stack)* ] $($rest)*)
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

Je ne suis pas vraiment amateur de répétitions aussi évidentes, mais, comme avec les littéraux, il n'y a pas de type de jeton spécial pour faire correspondre les opérateurs.

Toutefois, ce que nous pouvons faire est d’ajouter un assistant responsable de l’évaluation et de lui déléguer toute branche d’opérateur explicite.

Dans les macros, vous ne pouvez pas vraiment utiliser un assistant externe, mais la seule chose dont vous pouvez être sûr, c'est que vos macros sont déjà à portée. L'astuce habituelle consiste donc à avoir une branche dans la même macro « marquée » avec une séquence de jetons unique, et de l’appeler récursivement comme nous le faisions dans les branches normales.

Utilisons `@op` comme ce marqueur et acceptons tous les opérateurs via `tt` à l’intérieur ( `tt` serait sans ambiguïté dans ce contexte car nous ne passerons que des opérateurs à cet assistant).

Et la pile n'a plus besoin d'être développée dans chaque branche distincte. Puisque nous l'avons déjà enveloppée dans des crochets `[]`, elle peut être comparée à n'importe quel autre arbre de jetons `(tt)`, puis passée dans notre aide :
    
    
    macro_rules! rpn {
      (@op [ $b:expr, $a:expr $(, $stack:expr)* ] $op:tt $($rest:tt)*) => {
        rpn!([ $a $op $b $(, $stack)* ] $($rest)*)
      };
    
      ($stack:tt + $($rest:tt)*) => {
        rpn!(@op $stack + $($rest)*)
      };
      
      ($stack:tt - $($rest:tt)*) => {
        rpn!(@op $stack - $($rest)*)
      };
    
      ($stack:tt * $($rest:tt)*) => {
        rpn!(@op $stack * $($rest)*)
      };
      
      ($stack:tt / $($rest:tt)*) => {
        rpn!(@op $stack / $($rest)*)
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

Désormais, tous les jetons sont traités par les branches correspondantes et nous devons simplement gérer le cas final lorsque la pile contient un seul élément et qu'il ne reste plus de jetons :
    
    
    macro_rules! rpn {
      // ...
      
      ([ $result:expr ]) => {
        $result
      };
    }

À ce stade, si vous appelez cette macro avec une pile vide et une expression RPN, le résultat produit sera déjà correct :

[Terrain de jeu](https://play.rust-lang.org/?gist=cd56f6d7335e2d27c05e7fa89545b2cd&version=stable)
    
    
    println!("{}", rpn!([] 2 3 + 4 *)); // 20

`println!("{}", rpn!([] 2 3 + 4 *)); // 20`

Toutefois, notre pile est un détail d'implémentation et il ne faut vraiment pas que tous les consommateurs transmettent une pile vide. Nous allons donc ajouter une autre branche fourre-tout à la fin qui servirait de point d'entrée et ajouter `[]` automatiquement :
    
    
    macro_rules! rpn {
      // ...
    
      ($($tokens:tt)*) => {
        rpn!([] $($tokens)*)
      };
    }
    
    println!("{}", rpn!(2 3 + 4 *)); // 20

[Terrain de jeu](https://play.rust-lang.org/?gist=d94abc0e20aa5c7f689706af06fd1923&version=stable)
    
    
    println!("{}", rpn!(15 7 1 1 + - / 3 * 2 1 1 + + -)); // 5

Notre macro fonctionne même pour des expressions plus complexes, comme celle [de la page Wikipédia au sujet de la RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Example) !

`println!("{}", rpn!(15 7 1 1 + - / 3 * 2 1 1 + + -)); // 5`

### **Gestion d'erreur**
    
    
     println!("{}", rpn!(2 3 7 + 4 *));

Maintenant, tout semble fonctionner de manière fluide pour les expressions RPN correctes, mais pour qu'une macro soit prête pour la production, nous devons nous assurer qu'elle peut également gérer les entrées non valides avec un message d'erreur raisonnable.
    
    
    error[E0277]: the trait bound `[{integer}; 2]: std::fmt::Display` is not satisfied
      --> src/main.rs:36:20
       |
    36 |     println!("{}", rpn!(2 3 7 + 4 *));
       |                    ^^^^^^^^^^^^^^^^^ `[{integer}; 2]` cannot be formatted with the default formatter; try using `:?` instead if you are using a format string
       |
       = help: the trait `std::fmt::Display` is not implemented for `[{integer}; 2]`
       = note: required by `std::fmt::Display::fmt`

Tout d'abord, essayons d'insérer un autre chiffre au milieu et voyons ce qui se passe :

Résultat :

D'accord, cela ne semble résolument pas utile car il ne fournit aucune information pertinente sur l'erreur réelle dans l'expression.
    
    
    #![feature(trace_macros)]
    
    macro_rules! rpn { /* ... */ }
    
    fn main() {
      trace_macros!(true);
      let e = rpn!(2 3 7 + 4 *);
      trace_macros!(false);
      println!("{}", e);
    }

Afin de comprendre ce qui s'est passé, nous devrons déboguer nos macros. Pour cela, nous utiliserons une fonctionnalité [`trace_macros`](https://doc.rust-lang.org/unstable-book/language-features/trace-macros.html) (et, comme pour toute autre fonctionnalité optionnelle du compilateur, vous aurez besoin d’une version Nightly de Rust). Nous ne voulons pas tracer l’appel `println!`, nous allons donc séparer notre calcul RPN en une variable :
    
    
    note: trace_macro
      --> src/main.rs:39:13
       |
    39 |     let e = rpn!(2 3 7 + 4 *);
       |             ^^^^^^^^^^^^^^^^^
       |
       = note: expanding `rpn! { 2 3 7 + 4 * }`
       = note: to `rpn ! ( [  ] 2 3 7 + 4 * )`
       = note: expanding `rpn! { [  ] 2 3 7 + 4 * }`
       = note: to `rpn ! ( [ 2 ] 3 7 + 4 * )`
       = note: expanding `rpn! { [ 2 ] 3 7 + 4 * }`
       = note: to `rpn ! ( [ 3 , 2 ] 7 + 4 * )`
       = note: expanding `rpn! { [ 3 , 2 ] 7 + 4 * }`
       = note: to `rpn ! ( [ 7 , 3 , 2 ] + 4 * )`
       = note: expanding `rpn! { [ 7 , 3 , 2 ] + 4 * }`
       = note: to `rpn ! ( @ op [ 7 , 3 , 2 ] + 4 * )`
       = note: expanding `rpn! { @ op [ 7 , 3 , 2 ] + 4 * }`
       = note: to `rpn ! ( [ 3 + 7 , 2 ] 4 * )`
       = note: expanding `rpn! { [ 3 + 7 , 2 ] 4 * }`
       = note: to `rpn ! ( [ 4 , 3 + 7 , 2 ] * )`
       = note: expanding `rpn! { [ 4 , 3 + 7 , 2 ] * }`
       = note: to `rpn ! ( @ op [ 4 , 3 + 7 , 2 ] * )`
       = note: expanding `rpn! { @ op [ 4 , 3 + 7 , 2 ] * }`
       = note: to `rpn ! ( [ 3 + 7 * 4 , 2 ] )`
       = note: expanding `rpn! { [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [  ] [ 3 + 7 * 4 , 2 ] )`
       = note: expanding `rpn! { [  ] [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [ [ 3 + 7 * 4 , 2 ] ] )`
       = note: expanding `rpn! { [ [ 3 + 7 * 4 , 2 ] ] }`
       = note: to `[(3 + 7) * 4, 2]`

[Terrain de jeu](https://play.rust-lang.org/?gist=610bc0c241aacda3d30a916f89b244cd&version=nightly)
    
    
       = note: expanding `rpn! { [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [  ] [ 3 + 7 * 4 , 2 ] )`

Dans le résultat, nous verrons désormais comment notre macro est évaluée de manière récursive, étape par étape :

Si nous examinons attentivement la trace, nous remarquons que le problème provient de ces étapes :

Puisque `[3 + 7 * 4, 2]` ne correspondait pas à la branche `([$ result: expr]) => ...` comme expression finale, il a été attrapé par notre dernière branche fourre-tout `($ ($ tokens: tt) *) => ...` à la place, précédée d'une pile vide `[]` puis l'original `[3 + 7 * 4, 2]` a été comparé au `$num:tt` générique et placé sur la pile en tant que valeur finale unique.

Afin d'éviter que cela ne se produise, insérons une autre branche entre ces deux dernières qui correspondrait à n'importe quelle pile.

Elle ne serait touchée que lorsque nous n'aurions plus de jetons, mais la pile n'avait pas une valeur finale exacte. Nous pouvons donc la traiter comme une erreur de compilation et générer un message d'erreur plus utile à l'aide d'une macro [`compile_error`](https://doc.rust-lang.org/std/macro.compile_error.html) intégrée.
    
    
    macro_rules! rpn {
      // ...
    
      ([ $result:expr ]) => {
        $result
      };
    
      ([ $($stack:expr),* ]) => {
        compile_error!(concat!(
          "Could not find final value for the expression, perhaps you missed an operator? Final stack: ",
          stringify!([ $($stack),* ])
        ))
      };
    
      ($($tokens:tt)*) => {
        rpn!([] $($tokens)*)
      };
    }

Notez que nous ne pouvons pas utiliser `format!` dans ce contexte puisqu'il utilise des API d'exécution pour formater une chaîne. Nous devrons plutôt nous limiter aux macros `concat!` et `stringify!` intégrés pour formater un message :
    
    
    error: Could not find final value for the expression, perhaps you missed an operator? Final stack: [ (3 + 7) * 4 , 2 ]
      --> src/main.rs:31:9
       |
    31 |         compile_error!(concat!("Could not find final value for the expression, perhaps you missed an operator? Final stack: ", stringify!([$($stack),*])))
       |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...
    40 |     println!("{}", rpn!(2 3 7 + 4 *));
       |                    ----------------- in this macro invocation

[Terrain de jeu](https://play.rust-lang.org/?gist=e56be9422387bcae54aab3b8405a11e7&version=stable)

Le message d'erreur est maintenant plus significatif et contient au moins quelques détails sur l'état actuel du progrès :
    
    
    println!("{}", rpn!(2 3 + *));

Mais que se passe-t-il si, au contraire, nous manquons un numéro ?
    
    
    error: expected expression, found `@`
      --> src/main.rs:15:14
       |
    15 |         rpn!(@op $stack * $($rest)*)
       |              ^
    ...
    40 |     println!("{}", rpn!(2 3 + *));
       |                    ------------- in this macro invocation

[Terrain de jeu](https://play.rust-lang.org/?gist=ce40630b8c1aa610c46b94557fdc9905&version=stable)

`println!("{}", rpn!(2 3 + *));`

Malheureusement, celui-ci n'est toujours pas très utile :
    
    
    macro_rules! rpn {
      (@op [ $b:expr, $a:expr $(, $stack:expr)* ] $op:tt $($rest:tt)*) => {
        rpn!([ $a $op $b $(, $stack)* ] $($rest)*)
      };
    
      (@op $stack:tt $op:tt $($rest:tt)*) => {
        compile_error!(concat!(
          "Could not apply operator `",
          stringify!($op),
          "` to the current stack: ",
          stringify!($stack)
        ))
      };
    
      // ...
    }

Si vous essayez d'utiliser trace_macros, même si cela ne développera pas la pile pour une raison quelconque, heureusement, ce qui se passe est relativement clair. `@op` a des conditions très spécifiques quant à ce qui doit être mis en correspondance (il attend au moins deux valeurs sur la pile) et, quand il ne les obtient pas, `@op` est apparié par le même bien trop gourmand `$num:tt` et placé sur la pile.
    
    
    error: Could not apply operator `*` to the current stack: [ 2 + 3 ]
      --> src/main.rs:9:9
       |
    9  |         compile_error!(concat!("Could not apply operator ", stringify!($op), " to current stack: ", stringify!($stack)))
       |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...
    46 |     println!("{}", rpn!(2 3 + *));
       |                    ------------- in this macro invocation

Pour éviter cela, encore une fois, nous allons ajouter une autre branche pour correspondre à tout ce qui commence par `@op` et qui ne correspondait pas déjà, et produire une erreur de compilation :

[Terrain de jeu](https://play.rust-lang.org/?gist=8729a8f3c96fa58ed62d35804c48782d&version=stable)

Essayons encore une fois :

Beaucoup mieux ! Désormais, notre macro peut évaluer n’importe quelle expression RPN au moment de la compilation et gère gracieusement les erreurs les plus courantes. Invoquons-la un jour et disons qu’elle est prête pour la production :)

Nous pourrions ajouter de nombreuses autres petites améliorations mais j'aimerais les laisser en dehors de ce tutoriel de démonstration.

N'hésitez pas à me dire si cela a été utile et/ou quels sujets vous souhaiteriez voir davantage couvert[sur Twitter](https://twitter.com/RReverser) !

Sur cette page

Discuter en ligne

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F&t=%C3%89crire%20des%20macros%20complexes%20dans%20Rust%20%3A%20Notation%20polonaise%20inverse%20%28RPN%29)[](https://x.com/intent/post?text=%C3%89crire+des+macros+complexes+dans+Rust+%3A+Notation+polonaise+inverse+%28RPN%29&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://bsky.app/intent/compose?text=%C3%89crire+des+macros+complexes+dans+Rust+%3A+Notation+polonaise+inverse+%28RPN%29+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://mastodonshare.com/?text=%C3%89crire+des+macros+complexes+dans+Rust+%3A+Notation+polonaise+inverse+%28RPN%29&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://www.threads.net/intent/post?text=%C3%89crire+des+macros+complexes+dans+Rust+%3A+Notation+polonaise+inverse+%28RPN%29+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)

## Tags associés

[Cloudflare Polish](https://blog.cloudflare.com/fr-fr/tag/cloudflare-polish/)[Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)[Programming](https://blog.cloudflare.com/fr-fr/tag/programming/)[Rust](https://blog.cloudflare.com/fr-fr/tag/rust/)

Suivre sur les réseaux sociaux

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Abonnez-vous pour recevoir les notifications de nouveaux articles

Adresse e-mail

Nous ne partagerons jamais votre adresse e-mail.

S'abonner

Merci pour votre inscription ! Vérifiez votre boîte de réception pour confirmer.
