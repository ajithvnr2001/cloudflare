---
url: https://blog.cloudflare.com/fr-fr/technical-breakdown-http2-rapid-reset-ddos-attack/
title: HTTP/2 Rapid Reset : anatomie de l'attaque record | Le blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:18.640517+00:00
---

# HTTP/2 Rapid Reset : anatomie de l'attaque record | Le blog Cloudflare

> Source: https://blog.cloudflare.com/fr-fr/technical-breakdown-http2-rapid-reset-ddos-attack/

[Blog](https://blog.cloudflare.com/fr-fr/)

[Attaques](https://blog.cloudflare.com/fr-fr/tag/attacks/)[Attaques DDoS](https://blog.cloudflare.com/fr-fr/tag/ddos/)[Sécurité](https://blog.cloudflare.com/fr-fr/tag/security/)+2Afficher 2 étiquettes supplémentaires

5 tagsAfficher 5 tags

  * Tags de l’article
  * [Attaques](https://blog.cloudflare.com/fr-fr/tag/attacks/)[Attaques DDoS](https://blog.cloudflare.com/fr-fr/tag/ddos/)[Sécurité](https://blog.cloudflare.com/fr-fr/tag/security/)[Tendances](https://blog.cloudflare.com/fr-fr/tag/trends/)
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



[Tendances](https://blog.cloudflare.com/fr-fr/tag/trends/)[Vulnerabilities](https://blog.cloudflare.com/fr-fr/tag/vulnerabilities/)

[Attaques](https://blog.cloudflare.com/fr-fr/tag/attacks/)[Attaques DDoS](https://blog.cloudflare.com/fr-fr/tag/ddos/)[Sécurité](https://blog.cloudflare.com/fr-fr/tag/security/)[Tendances](https://blog.cloudflare.com/fr-fr/tag/trends/)[Vulnerabilities](https://blog.cloudflare.com/fr-fr/tag/vulnerabilities/)

10 octobre 2023

# HTTP/2 Rapid Reset : anatomie de l'attaque record

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Julien Desgats](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490NXEPS0Y3GYM6MEBDP98.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/fr-fr/author/lucas/) et [Julien Desgats](https://blog.cloudflare.com/fr-fr/author/julien-desgats/)

Lecture : 24 min.

Copier l'URL

Cet article est également disponible en [English](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/), [Deutsch](https://blog.cloudflare.com/de-de/technical-breakdown-http2-rapid-reset-ddos-attack/), [Español](https://blog.cloudflare.com/es-es/technical-breakdown-http2-rapid-reset-ddos-attack/), [日本語](https://blog.cloudflare.com/ja-jp/technical-breakdown-http2-rapid-reset-ddos-attack/), [한국어](https://blog.cloudflare.com/ko-kr/technical-breakdown-http2-rapid-reset-ddos-attack/), [繁體中文](https://blog.cloudflare.com/zh-tw/technical-breakdown-http2-rapid-reset-ddos-attack/) et [简体中文](https://blog.cloudflare.com/zh-cn/technical-breakdown-http2-rapid-reset-ddos-attack/).

![BLOG-2023 Embedded Image - mLN7qf](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48WDXXVR9MBXJX2BC6M78M.png&w=1600&h=901&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9PLz5+br4uPt5Ofz6O3z6+/v////////7Orx19bm0NHn2Nvu5Ojx6+/w////////5OPxxsXivsDiztHq4eTx7fDy////////4+P0wcHkurzjztDs5Of08fT2////////7Oz6z9Dty8zt29307fD69/r7////////+vr/5uf65OX67/D/+fz//v//////////////+vv/+fr/////////////////////////////////////////////)

À compter du 25 août 2023, nous avons commencé à observer des attaques HTTP inhabituellement volumineuses frappant bon nombre de nos clients. Ces attaques ont été détectées et atténuées par notre système anti-DDoS automatisé. Il n'a pas fallu longtemps pour que ces attaques atteignent des tailles record, pour finir par culminer à un peu plus de 201 millions de requêtes par seconde, soit un chiffre près de trois fois supérieur à la [précédente attaque la plus volumineuse que nous ayons enregistrée](https://blog.cloudflare.com/fr-fr/cloudflare-mitigates-record-breaking-71-million-request-per-second-ddos-attack-fr-fr/).

_Vous êtes victime d'une attaque ou avez besoin d'une protection supplémentaire ?[Cliquez ici pour demander de l'aide](https://www.cloudflare.com/h2/)._  


Le fait que l'acteur malveillant soit parvenu à générer une attaque d'une telle ampleur à l'aide d'un botnet de tout juste 20 000 machines s'avère préoccupant. Certains botnets actuels se composent de centaines de milliers ou de millions de machines. Comme qu'Internet dans son ensemble ne reçoit habituellement qu'entre 1 et 3 milliards de requêtes chaque seconde, il n'est pas inconcevable que l'utilisation de cette méthode puisse concentrer l'intégralité du nombre de requêtes du réseau sur un petit nombre de cibles.

## **Détecti** on et att**énuation**

Il s'agissait d'un nouveau vecteur d'attaque évoluant à une échelle sans précédent, mais les protections Cloudflare existantes ont largement pu absorber le plus gros de ces attaques. Si nous avons constaté au départ un certain impact sur le trafic client (environ 1 % des requêtes ont été touchées pendant la vague d'attaques initiale), nous avons ensuite pu perfectionner nos méthodes d'atténuation afin de bloquer l'attaque pour n'importe quel client Cloudflare sans affecter nos systèmes.

Nous avons remarqué ces attaques en même temps que deux autres acteurs majeurs du secteur : Google et AWS. Nous nous sommes attelés au renforcement des systèmes de Cloudflare afin de nous assurer qu'aujourd'hui tous nos clients sont protégés contre cette nouvelle méthode d'attaque DDoS sans impact sur ces derniers. Nous avons également participé, avec Google et AWS, à une révélation coordonnée de l'attaque aux prestataires affectés et aux fournisseurs d'infrastructure essentielle.

Cette attaque a été rendue possible par l'abus de certaines fonctionnalités du protocole HTTP/2 et des détails de mise en œuvre des serveurs (voir la [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) pour plus d'informations). Comme l'attaque tire parti d'une faiblesse sous-jacente du protocole HTTP/2, nous pensons que tous les fournisseurs qui ont déployé le HTTP/2 subiront l'attaque. Ce constat comprend tous les serveurs web modernes. Aux côtés de Google et d'AWS, nous avons divulgué la méthode d'attaque aux fournisseurs de serveurs web qui, nous l'espérons, déploieront les correctifs. Entre temps, la meilleure défense consiste à utiliser un service d'atténuation des attaques DDoS tel que Cloudflare en amont de chaque réseau en contact avec Internet ou de chaque serveur d'API.

Cet article s'intéressera en profondeur aux détails du protocole HTTP/2, la fonctionnalité exploitée par les acteurs malveillants pour générer ces attaques d'envergure, ainsi qu'aux stratégies d'atténuation que nous avons appliquées pour nous assurer que tous nos clients sont protégés. Nous espérons qu'en publiant ces détails d'autres serveurs web et services affectés disposeront des informations dont ils ont besoin pour mettre en œuvre ces stratégies d'atténuation. En outre, l'équipe chargée des normes du protocole HTTP/2, de même que les équipes travaillant sur les futures normes web, pourront mieux concevoir ces dernières afin d'empêcher de telles attaques.

## Détails de l'att**aque RST**

Le protocole d'application HTTP sous-tend Internet. La norme [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) est commune à toutes les versions de HTTP : l'architecture générale, la terminologie et les aspects de protocole, comme les messages de requête et de réponse, les méthodes, les codes d'état, les champs d'en-tête et de trailer, le contenu des messages et bien d'autres. Chaque version individuelle de HTTP définit la manière dont la sémantique est transformée au « format conversation » (wire) pour l'échange sur Internet. Un client doit, par exemple, sérialiser un message de requête en données binaires avant de l'envoyer. Le serveur l'analyse ensuite et le retransforme en message qu'il peut traiter.

[Le protocole HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html) utilise une forme textuelle de sérialisation. Les messages de requête et de réponse sont échangés sous la forme d'un flux de caractères ASCII, envoyé via une couche de transport fiable, comme le TCP, selon le [format](https://www.rfc-editor.org/rfc/rfc9112.html#section-2.1) suivant (dans lequel CRLF signifie retour chariot et saut de ligne) :
    
    
     HTTP-message   = start-line CRLF
                       *( field-line CRLF )
                       CRLF
                       [ message-body ]

Une requête GET très simple pour <https://blog.cloudflare.com/> ressemblerait, par exemple, à ceci sur la conversation :

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

Et la réponse ressemblerait à ce qui suit :

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

Ce format encapsule les messages sur la conversation, pour indiquer qu'il est possible d'utiliser une unique connexion TCP pour échanger plusieurs requêtes et réponses. Le format nécessite toutefois que chaque message soit envoyé en entier. En outre, afin de faire entrer correctement en corrélation les requêtes avec les réponses, un ordre strict se révèle nécessaire. Les messages peuvent donc être échangés de manière sérielle et ne peuvent pas être multiplexés. Deux requêtes GET, pour `https://blog.cloudflare.com/` et `https://blog.cloudflare.com/page/2/`,, se présenteraient ainsi sous la forme suivante :

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLFGET /page/2/ HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

Et les réponses :

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>CRLFHTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

Les pages web nécessitent davantage d'interactions HTTP compliquées que ces exemples. Lorsque vous visitez le blog de Cloudflare, votre navigateur charge plusieurs scripts, styles et ressources multimédias. Si vous accédez à la page d'accueil à l'aide du protocole HTTP/1.1 et que vous décidez rapidement de vous rendre sur la page 2, votre navigateur a le choix entre deux options. Soit attendre l'ensemble des réponses en attente pour la page que vous ne souhaitez plus consulter avant de démarrer la page 2, soit annuler les requêtes en transit en mettant fin à la connexion TCP et en établissant une nouvelle connexion. Aucune de ces options ne s'avère particulièrement pratique. Les navigateurs ont tendance à contourner ces limitations en gérant un pool de connexions TCP (jusqu'à 6 par hôte) et en mettant en œuvre une logique complexe de répartition des requêtes au sein du pool.

[Le protocole HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) répond à bon nombre des problèmes du HTTP/1.1. Chaque message HTTP est sérialisé sous la forme d'un ensemble de trames HTTP/2 disposant d'un type, d'une longueur, de marqueurs, d'un identifiant (ID) de flux et d'un contenu. L'ID de flux indique clairement quels octets sur la conversation s'appliquent à un message donné, afin de permettre le multiplexage et la concurrence en toute sécurité. Les flux sont bidirectionnels. Les clients envoient des trames et les serveurs répondent par des trames utilisant le même ID.

En HTTP/2, notre requête GET pour <https://blog.cloudflare.com> serait échangée sur l'ID de flux 1, le client envoyant une trame [HEADERS](https://www.rfc-editor.org/rfc/rfc9113#name-headers) et le serveur répondant par une trame HEADERS, suivies par une ou plusieurs trames [DATA](https://www.rfc-editor.org/rfc/rfc9113#name-data). Comme les requêtes du client utilisent toujours des ID de flux impairs, les requêtes suivantes utiliseront donc les ID de flux 3, 5 et ainsi de suite. Les réponses peuvent être transmises dans n'importe quel ordre et les trames provenant de flux différents peuvent être entrelacées.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - x9QxRg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49B9T4FFZW2YJF9EFMJGRE.png&w=715&h=221&f=webp&fit=cover&position=center)

Le multiplexage et la concurrence des flux constituent de puissantes fonctionnalités du protocole HTTP/2. Elles permettent l'utilisation plus efficace d'une unique connexion TCP. Le HTTP/2 optimise la récupération de ressources, notamment lorsqu'elle est associée à la [priorisation](https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/). En réciproque, le fait de faciliter le lancement de vastes quantités de tâches parallèles aux clients peut accroître le pic de demande de ressources serveur par rapport au HTTP/1.1. Il s'agit là d'un vecteur évident de déni de service.

Afin de proposer quelques garde-fous, le HTTP/2 avance la notion de maximum de [flux concurrents](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2) actifs. Le paramètre [SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_FRAME_SIZE) permet à un serveur d'annoncer sa limite de concurrence. Par exemple, si le serveur annonce une limite de 100, seules 100 requêtes pourront être actives à un moment donné. Si un client tente d'ouvrir un flux au-delà de cette limite, ce dernier devra être rejeté par le serveur à l'aide d'une trame [RST_STREAM](https://www.rfc-editor.org/rfc/rfc9113#section-6.4). Le rejet d'un flux n'affecte pas les autres flux en transit sur la connexion.

La réalité de l'affaire est un peu plus compliquée. Les flux présentent un [cycle de vie](https://www.rfc-editor.org/rfc/rfc9113#section-5.1). Vous trouverez ci-dessous un schéma de l'état d'un flux HTTP/2. Le client et le serveur gèrent leurs propres vues de l'état d'un flux. L'envoi ou la réception de trames HEADERS, DATA et RST_STREAM déclenchent les transitions. Les vues de l'état d'un flux sont indépendantes, mais restent synchronisées.

Les trames HEADERS et DATA intègrent un marqueur END_STREAM qui, lorsqu'il est défini sur la valeur 1 (true), peut déclencher une transition d'état.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - dgpLal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45G749M08PSFAAXZRQE5DQ.png&w=715&h=515&f=webp&fit=cover&position=center)

Examinons ceci plus en détail avec un exemple de requête GET sans contenu de message. Le client envoie la requête sous la forme d'une trame HEADERS comportant le marqueur END_STREAM défini sur 1. Il déclenche en premier lieu la transition de l'état « idle » (à l'arrêt) à « open » (ouvert), avant de déclencher immédiatement une transition vers l'état « half-closed » (mi-fermé). L'état « half-closed » du client indique qu'il ne peut plus envoyer de trames HEADERS ou DATA, mais uniquement des trames [WINDOW_UPDATE](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.9), [PRIORITY](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.3) ou RST_STREAM. Il peut toutefois recevoir n'importe quelle trame.

Une fois que le serveur reçoit et analyse la trame HEADERS, il fait passer l'état du flux d'« idle » à « open », puis à « half-closed », afin de correspondre à celui du client. L'état « half-closed » du serveur indique qu'il peut envoyer n'importe quelle trame, mais qu'il ne peut recevoir que des trames WINDOW_UPDATE, PRIORITY ou RST_STREAM.

La réponse à la requête GET contient un contenu de message, aussi le serveur envoie-t-il une trame HEADERS comportant le marqueur END_STREAM défini sur 0, puis une trame DATA comportant le marqueur END_STREAM défini sur 1. La trame DATA déclenche la transition du flux de half-closed à closed (fermé) sur le serveur. Lorsque le client la reçoit, il lance également sa transition vers l'état « closed ». Une fois un flux fermé, plus aucune trame ne peut être envoyée ou reçue.

En appliquant ce cycle de vie dans le contexte de la concurrence, le protocole HTTP/2 [précise](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2-2) :

_Les flux à l'état « open » ou dans l'un des deux états « half-closed » comptent dans le nombre maximum de flux qu'un point de terminaison est autorisé à ouvrir. Les flux dans l'un de ces trois états comptent à l'égard de la limite annoncée dans le paramètre_ _[SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS)._

En théorie, la limite de concurrence est utile. Certains facteurs pratiques entravent toutefois son efficacité, que nous aborderons plus tard dans cet article.

### **A** nnula**tion de requête HTTP/2**

Un peu plus tôt, nous avons évoqué l'annulation de requêtes en transit par le client. Le protocole HTTP/2 prend cette fonctionnalité en charge de manière plus efficace que le HTTP/1.1. Plutôt que de devoir abandonner la connexion dans son ensemble, un client peut désormais envoyer une trame RST_STREAM pour un seul flux. Cette dernière demande au serveur de mettre fin au traitement de la requête et d'abandonner la réponse. Cette opération libère des ressources serveur et permet d'éviter de gaspiller de la bande passante.

Reprenons notre exemple précédent, avec les trois requêtes. Cette fois, le client annule la requête sur le flux 1 après l'envoi de toutes les trames HEADERS. Le serveur analyse la trame RST_STREAM avant d'être prêt à diffuser la réponse et, à la place, ne répond qu'aux flux 3 et 5 :

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - alylDM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48VGZF708M4TQDMQVJN3F2.png&w=715&h=225&f=webp&fit=cover&position=center)

L'annulation de requête constitue une fonctionnalité bien utile. Lorsque vous parcourez une page web comportant plusieurs images, par exemple, un navigateur web peut annuler les images qui ne sont pas affichées dès l'ouverture. Les images qui lui parviennent peuvent donc être chargées plus rapidement. Le protocole HTTP/2 rend ce comportement bien plus efficace par rapport au HTTP/1.1.

Un flux de requête annulé passe rapidement par tous les états du cycle de vie d'un flux. La trame HEADERS envoyée par le client, comportant le marqueur END_STREAM défini sur 1, passe de l'état « idle » à « open », puis à « half-closed », avant que la trame RST_STREAM ne déclenche immédiatement sa transition de l'état « half-closed » à « closed ».

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - FOxdTz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SPXM07R6QG2B8FEXJCHJ.png&w=715&h=515&f=webp&fit=cover&position=center)

Souvenez-vous que seuls les flux à l'état « open » ou « half-closed » sont comptabilisés dans la limite de concurrence du flux. Lorsqu'un client annule un flux, il regagne instantanément la capacité d'ouvrir un autre flux à la place et peut immédiatement envoyer une nouvelle requête. C'est là le cœur du fonctionnement de la vulnérabilité [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487).

### **Des réinitialisations ra** pides **conduisant à un déni de service**

Le processus d'annulation de requête du protocole HTTP/2 peut être utilisé de manière abusive en réinitialisant rapidement un nombre illimité de flux. Lorsqu'un serveur HTTP/2 peut traiter des trames client-sent RST_STREAM et leur faire changer d'état suffisamment rapidement, ces réinitialisations rapides ne posent pas de problème. Les soucis commencent lorsqu'une quelconque forme de retard ou de latence apparaît lors du nettoyage. Le client peut avoir à traiter un nombre de requêtes si important que les tâches s'accumulent, en entraînant une consommation excessive de ressources sur le serveur.

Une architecture de déploiement HTTP courante consiste à exécuter un proxy HTTP/2 ou un équilibreur de charge en amont des autres composants. Lorsqu'une requête client arrive, elle est rapidement retransmise et la tâche réelle est effectuée sous forme d'activité asynchrone à un autre endroit. Cette opération permet au proxy de traiter le trafic client très efficacement. Toutefois, cette séparation des préoccupations peut compliquer la phase de nettoyage des tâches en cours pour le proxy. Ce type de déploiement est donc plus susceptible de rencontrer des problèmes en cas de réinitialisations rapides.

Lorsque les [proxys inverses](https://www.rfc-editor.org/rfc/rfc9110#section-3.7-6) de Cloudflare traitent du trafic client entrant HTTP/2, ils copient les données du socket de la connexion au sein d'un tampon et traitent ces données en tampon dans l'ordre. Chaque requête est lue (trames HEADERS et DATA) et transmise à un service en amont. Lorsque les trames RST_STREAM sont lues, l'état local de la requête est abandonné et l'amont est notifié de l'annulation de la requête. Les proxys répètent ensuite le processus jusqu'à ce que toutes les données en tampon aient été traitées. Cette logique peut toutefois être utilisée de manière abusive : si un client malveillant commence à envoyer une énorme chaîne de requêtes, qu'il réinitialise au début d'une connexion, nos serveurs s'empresseront de toutes les lire. Cette situation engendrera alors une pression sur les serveurs en amont, au point qu'ils se retrouveront incapables de traiter les nouvelles requêtes entrantes.

Un point important à souligner est que la concurrence de flux ne peut pas, par elle-même, atténuer les réinitialisations rapides. Le client peut créer des requêtes afin de produire des taux de requêtes élevés, peu importe la valeur choisie par le serveur pour le paramètre [SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS).

### **Anatomie d'une** réin**itialisation rapide**

Voici un exemple de réinitialisation rapide (Rapid Reset) reproduite à l'aide d'un client de démonstration de faisabilité tentant d'envoyer un total de 1 000 requêtes. J'ai utilisé un serveur du commerce ne disposant d'aucune mesure d'atténuation et écoutant le port 443 au sein d'un environnement de test. Le trafic est disséqué à l'aide de Wireshark et filtré pour ne montrer que le trafic HTTP/2, pour plus de clarté. [Téléchargez la pcap](http://staging.blog.mrk.cfdata.org/content/images/rapidreset.pcapng) pour suivre la démonstration.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - WbJayy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46CJJHBWXXWMSQCY94SYWG.png&w=715&h=35&f=webp&fit=cover&position=center)

Il est un peu difficile à analyser, en raison du grand nombre de trames. Nous pouvons en obtenir un résumé rapide à l'aide de l'outil HTTP/2 de Wireshark, disponible sous « Statistics » (Statistiques) :

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - hiRPjv](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JCSEZW1GJBEZC3CJVBK1.png&w=715&h=219&f=webp&fit=cover&position=center)

La première trame de cette trace, dans le paquet 14, est la trame SETTINGS du serveur, qui annonce un nombre maximum de flux concurrents de 100. Dans le paquet 15, le client envoie quelques trames de contrôle, puis commence à envoyer des requêtes, rapidement réinitialisées. La première trame HEADERS fait 26 octets de long, tandis que toutes les trames HEADERS suivantes ne mesurent que 9 octets. Cette différence de taille est due à une technologie de compression nommée [HPACK](https://blog.cloudflare.com/hpack-the-silent-killer-feature-of-http-2/). Au total, le paquet 15 contient 525 requests, remontant le long du flux 1051.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - 4zuXCV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497JBM72881G9RYDWRT2C6.png&w=619&h=593&f=webp&fit=cover&position=center)

Curieusement, la trame RST_STREAM du flux 1051 ne rentre pas dans le paquet 15. Nous voyons donc, dans le paquet 16, le serveur répondre par une erreur 404. Le client envoie ensuite la trame RST_STREAM dans le paquet 17, avant de passer à l'envoi des 475 requêtes suivantes.

Veuillez noter que bien que le serveur ait annoncé 100 flux concurrents, les deux paquets envoyés par le client comportaient bien plus de trames HEADERS. Le client n'a pas attendu le trafic de retour du serveur, il n'était limité que par la taille des paquets qu'il pouvait envoyer. Aucune trame RST_STREAM du serveur n'apparaît dans cette trace, un constat qui indique que le serveur n'a pas observé de violation du nombre de flux concurrents.

## **Im** pac**t sur les clients**

Comme mentionné plus haut, lorsque les requêtes sont annulées, les services en amont sont notifiés et peuvent abandonner ces dernières avant de gaspiller trop de ressources sur leur traitement. C'est ce qui s'est passé dans cette attaque, au cours de laquelle les requêtes malveillantes n'ont jamais été retransmises aux serveurs d'origine. Toutefois, l'ampleur de ces attaques a engendré des effets.

Tout d'abord, lorsque le taux de requêtes entrantes a atteint des pics jamais encore observés jusqu'ici, nous avons reçu des signalements de niveaux élevés d'erreurs 502 observées par les clients. C'est ce qui s'est produit dans nos datacenters les plus impactés, car ils avaient du mal à traiter toutes les requêtes. Notre réseau est conçu pour faire face aux attaques d'envergure, mais cette vulnérabilité a révélé une faiblesse au sein de notre infrastructure. Intéressons-nous de plus près aux détails, en nous concentrant sur la manière dont les requêtes entrantes sont traitées lorsqu'elles arrivent dans l'un de nos datacenters :

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - ZsURSu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45571VPJA9ST5WBRH9KPG8.png&w=715&h=269&f=webp&fit=cover&position=center)

Nous pouvons voir que notre infrastructure se compose d'une chaîne de différents serveurs de proxy aux responsabilités différentes. Plus particulièrement, lorsqu'un client se connecte à Cloudflare pour envoyer du trafic HTTPS, ce dernier passe en premier par notre proxy de déchiffrement TLS, qui déchiffre le trafic TLS et traite le trafic HTTP 1, 2 ou 3, avant de le transmettre à notre proxy de « logique métier ». Ce dernier est responsable du chargement de l'ensemble des paramètres pour chaque client, puis du routage correct des requêtes vers les autres services d'amont. Plus important encore dans le cas qui nous intéresse, il est également responsable des fonctionnalités de sécurité. C'est là que l'atténuation des attaques sur la couche 7 est mise en œuvre.

Le problème avec ce vecteur d'attaque réside dans le fait qu'il parvient à envoyer un grand nombre de requêtes de manière très rapide, sur chaque connexion. Chacune d'elles devait être retransmise au proxy de logique métier avant que nous n'ayons l'occasion de la bloquer. Lorsque le volume de requêtes s'est révélé supérieur à la capacité de notre proxy, le pipeline reliant ces deux services a atteint son niveau de saturation dans certains de nos serveurs.

Quand cette situation se produit, le proxy TLS ne peut plus se connecter à son proxy d'amont. C'est pourquoi certains de nos clients ont vu s'afficher une erreur « 502 Bad Gateway » lors des attaques les plus graves. Il est important de noter qu'à la date d'aujourd'hui, les journaux utilisés pour produire les analyses HTTP sont également émis par notre proxy de logique métier. En conséquence, ces erreurs ne sont pas visibles au sein du tableau de bord Cloudflare. Nos tableaux de bord internes révèlent qu'environ 1 % des requêtes ont été affectées lors de la vague d'attaques initiale (avant la mise en œuvre des mesures d'atténuation), avec un pic se situant autour de 12 % pendant quelques secondes lors de l'attaque la plus massive, le 29 août. Le graphique suivant montre la proportion de ces erreurs sur une période de deux heures au cours de l'attaque :

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - cDLXgV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H86FX527NRYXEFG5HNZH.png&w=715&h=442&f=webp&fit=cover&position=center)

Nous nous sommes efforcés de réduire ce nombre de manière considérable les jours suivants, comme nous le détaillons plus loin dans cet article. Ce nombre aujourd'hui est effectivement de zéro, à la fois grâce aux modifications apportées à notre pile et à nos mesures d'atténuation, qui ont drastiquement réduit la taille de ces attaques.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - AfViXl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW484F1GN0TB062910TF1AD8.png&w=715&h=442&f=webp&fit=cover&position=center)

### **Erreurs 4** 99 e**t les défis liés à la concurrence des flux HTTP/2**

Un autre symptôme signalé par certains clients réside dans l'augmentation des erreurs 499. La raison est ici quelque peu différente et se trouve liée à la concurrence de flux maximale au sein d'une connexion HTTP/2, comme détaillée précédemment dans l'article.

Les paramètres HTTP/2 sont échangés au début d'une connexion à l'aide de trames SETTINGS. En l'absence de réception d'un paramètre explicite, ce sont les valeurs par défaut qui s'appliquent. Lorsqu'un client établit une connexion HTTP/2, il peut soit attendre la trame SETTINGS d'un serveur (lent), soit présupposer les valeurs par défaut et commencer à envoyer des requêtes (rapide). Pour le paramètre SETTINGS_MAX_CONCURRENT_STREAMS, la valeur par défaut est, dans les faits, illimitée (les ID de flux s'appuient sur un espace mathématique de 31 bits et les requêtes utilisent les nombres impairs. la limite réelle est donc établie à 1 073 741 824). La spécification recommande qu'un serveur ne propose pas moins de 100 flux concurrents. Les clients sont généralement axés sur la vitesse. Ils n'ont donc pas tendance à attendre les paramètres du serveur et ce fait entraîne en quelque sorte une situation de compétition. Ils « parient » sur la limite que le serveur pourrait avoir choisie. S'ils se trompent, la requête sera rejetée et devra être renvoyée. Le fait de parier sur un ensemble numérique de 1 073 741 824 nombres s'avère pour le moins absurde. Pour contrebalancer cette situation, de nombreux clients décident de se limiter à l'émission de 100 flux concurrents, dans l'espoir que les serveurs suivent la recommandation de la spécification. Si les serveurs ont sélectionné une valeur inférieure à 100, le pari du client échoue et les flux sont réinitialisés.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - VLKjcD](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46456QGGZGE6J54D0S0W49.png&w=715&h=246&f=webp&fit=cover&position=center)

Un serveur pourrait réinitialiser un flux pour de nombreuses raisons en dehors d'un dépassement de la limite de concurrence. Le HTTP/2 est strict et nécessite qu'un flux soit fermé (closed) en cas d'erreurs d'interprétation ou d'erreurs logiques. En 2019, Cloudflare a développé plusieurs mesures d'atténuation en réponse aux [vulnérabilités DoS du protocole HTTP/2](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/). Plusieurs de ces vulnérabilités résultaient d'un mauvais comportement de la part du client, qui poussait le serveur à réinitialiser un flux. Une stratégie très efficace pour freiner ces clients consiste à compter le nombre de réinitialisations du serveur au cours d'une connexion puis, lorsque ce chiffre dépasse un certain seuil, de mettre un terme à cette dernière à l'aide d'une trame [GOAWAY](https://www.rfc-editor.org/rfc/rfc9113#section-6.8). Les clients peuvent commettre une ou deux erreurs au cours d'une connexion et il s'agit là d'un constat acceptable. Un client qui commet trop d'erreurs est probablement soit défectueux, soit malveillant, et le fait de mettre fin à la connexion répond aux deux cas.

En réponse aux attaques DoS permises par la vulnérabilité [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487), Cloudflare a réduit la concurrence de flux maximale à 64. Avant d'effectuer cette modification, nous n'avions pas conscience que les clients n'attendaient pas la trame SETTINGS et supposaient à la place que la concurrence était fixée à 100. Certaines pages web, comme les galeries d'images, entraînent effectivement l'envoi immédiat de 100 requêtes par le navigateur au début d'une connexion. Malheureusement, les 36 flux au-delà de notre limite devaient être réinitialisés et cette opération déclenchait les compteurs de nos mesures d'atténuation. Nous interrompions donc des connexions sur des clients légitimes, avec pour résultat un échec total du chargement des pages. Dès que nous avons constaté ce problème d'interopérabilité, nous avons de nouveau fixé la concurrence de flux maximale à 100.

## **Act** ions c**ôté Cloudflare**

En 2019, nous avons découvert plusieurs [vulnérabilités DoS](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/) liées à l'implémentation du protocole HTTP/2. Cloudflare a développé et déployé une série de mesures de détection et d'atténuation en réponse. La vulnérabilité [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) est une différente manifestation de la vulnérabilité HTTP/2. Toutefois, pour l'atténuer, nous avons pu étendre les protections existantes afin de surveiller les trames RST_STREAM envoyées par les clients et de mettre fin aux connexions lorsque ces dernières étaient utilisées à des fins abusives. Les scénarios d'utilisation légitimes des trames RST_STREAM par les clients n'ont pas été affectés.

En plus d'un correctif direct, nous avons mis en œuvre plusieurs améliorations du serveur concernant le traitement des trames HTTP/2 et du code de répartition des requêtes. Le serveur de logique métier a, en outre, fait l'objet de perfectionnements au niveau de la mise en file d'attente et de la planification. Ces derniers réduisent le travail inutile et améliorent la réponse aux annulations. Ensemble, ces mesures diminuent l'impact des divers schémas d'abus potentiels, tout en accordant plus d'espace au serveur pour traiter les requêtes avant d'atteindre la saturation.

### **Atténu** er le**s attaques à un moment plus précoce**

Cloudflare dispose déjà de systèmes en place permettant d'atténuer efficacement les attaques de très grande ampleur à l'aide de méthodes moins coûteuses. L'une d'elles se nomme « IP Jail » (Prison IP). En cas d'attaques hypervolumétriques, ce système collecte les adresses IP des clients participant à l'attaque et les empêche de se connecter à la propriété attaquée, que ce soit au niveau de l'adresse IP ou de notre proxy TLS. Ce système demande toutefois quelques secondes pour être pleinement efficace. Au cours de ces précieuses secondes, les serveurs d'origine sont déjà protégés, mais notre infrastructure doit encore absorber l'ensemble des requêtes HTTP. Comme ce nouveau botnet ne dispose dans les faits d'aucune période de démarrage, nous devons pouvoir neutraliser ces attaques avant qu'elles ne deviennent un problème.

Pour y parvenir, nous avons étendu le système IP Jail afin qu'il protège l'intégralité de notre infrastructure. Une fois une adresse IP « en prison », nous l'empêchons non seulement de se connecter à la propriété attaquée, mais interdisons également aux adresses IP correspondants d'utiliser le HTTP/2 pour se connecter à un autre domaine sur Cloudflare pendant quelque temps. Comme de tels abus du protocole ne sont pas possibles à l'aide du HTTP/1.x, l'acteur malveillant se trouve sévèrement limité dans sa capacité à conduire des attaques d'envergure, tandis qu'un client légitime partageant la même adresse IP ne constaterait d'une très légère diminution des performances pendant ce temps. Les mesures d'atténuation basées sur l'IP constituent un outil pour le moins brutal. C'est pourquoi nous devons faire preuve d'une extrême prudence lorsque nous les utilisons à grande échelle et chercher à éviter les faux positifs autant que possible. De même, comme la durée de vie d'une adresse IP donnée au sein d'un botnet est généralement courte, l'atténuation à long terme risque davantage de nuire que d'aider. Le graphique suivant montre l'évolution du nombre d'adresses IP lors de l'attaque dont nous avons été témoins :

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - zEcUBs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BMWNAXCMETHFB5FB79WB.png&w=715&h=348&f=webp&fit=cover&position=center)

Il apparaît très clairement que les nouvelles adresses IP repérées lors d'une journée donnée disparaissent très rapidement après l'attaque.

Le fait que ces actions se déroulent dans notre proxy TLS, à l'entrée de notre pipeline HTTPS, permet d'économiser des ressources considérables par rapport à notre système d'atténuation de couche 7 habituel. Cette situation nous a permis de supporter ces attaques d'autant plus facilement et, aujourd'hui, le nombre d'erreurs 502 aléatoires dues à ces botnets a été réduit à zéro.

### **Améliora** tions **en matière d'observabilité**

L'un des autres fronts sur lequel nous avons apporté des modifications est celui de l'observabilité. Le fait de renvoyer des erreurs aux clients sans que ces dernières soient visibles dans les outils d'analyse des clients se révèle pour le moins insatisfaisant. Fort heureusement, nous avons lancé un projet visant à réorganiser ces systèmes bien avant les attaques récentes. Il permettra à terme à chaque service compris au sein de notre infrastructure de journaliser ses propres données, au lieu de s'en remettre à notre proxy de logique métier pour consolider et émettre les données de journalisation. Cet incident a fait ressortir l'importance de ce travail, dans le cadre duquel nous redoublons d'efforts.

Nous travaillons également à une meilleure journalisation au niveau de la connexion, afin de nous permettre de repérer ce type d'abus de protocole bien plus rapidement, afin d'améliorer nos capacités d'atténuation des attaques DDoS.

## **Co** nclu**sion**

Si l'attaque à laquelle cet article est consacré constituait sans conteste la dernière attaque record à ce jour, nous savons que ce ne sera pas la dernière. Alors que les attaques gagnent chaque jour en sophistication, Cloudflare travaille avec acharnement aux moyens d'identifier les nouvelles menaces de manière proactive, en déployant des contremesures sur notre réseau mondial afin de protéger nos millions de clients, immédiatement et automatiquement.

Cloudflare fournit une protection contre les attaques DDoS gratuite, totalement illimitée et sans surcoût lié à l'utilisation à l'ensemble de ses clients, et ce depuis 2017. Nous proposons en outre une gamme de fonctionnalités de sécurité supplémentaires afin de répondre aux besoins des entreprises de toutes les tailles. [Contactez-nous](https://www.cloudflare.com/h2) si vous n'êtes pas sûr de savoir si vous êtes protégé ou si vous souhaitez comprendre comment vous pourriez l'être.

Sur cette page

Discuter en ligne

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F&t=HTTP%2F2%20Rapid%20Reset%20%3A%20anatomie%20de%20l%27attaque%20record)[](https://x.com/intent/post?text=HTTP%2F2+Rapid+Reset+%3A+anatomie+de+l%27attaque+record&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://bsky.app/intent/compose?text=HTTP%2F2+Rapid+Reset+%3A+anatomie+de+l%27attaque+record+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://mastodonshare.com/?text=HTTP%2F2+Rapid+Reset+%3A+anatomie+de+l%27attaque+record&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.threads.net/intent/post?text=HTTP%2F2+Rapid+Reset+%3A+anatomie+de+l%27attaque+record+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)

## Tags associés

[Attaques](https://blog.cloudflare.com/fr-fr/tag/attacks/)[Attaques DDoS](https://blog.cloudflare.com/fr-fr/tag/ddos/)[Sécurité](https://blog.cloudflare.com/fr-fr/tag/security/)[Tendances](https://blog.cloudflare.com/fr-fr/tag/trends/)[Vulnerabilities](https://blog.cloudflare.com/fr-fr/tag/vulnerabilities/)

Suivre sur les réseaux sociaux

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Abonnez-vous pour recevoir les notifications de nouveaux articles

Adresse e-mail

Nous ne partagerons jamais votre adresse e-mail.

S'abonner

Merci pour votre inscription ! Vérifiez votre boîte de réception pour confirmer.
