---
url: https://blog.cloudflare.com/fr-fr/cloudflare-architecture-and-how-bpf-eats-the-world/
title: Architecture Cloudflare et la mani\u00e8re dont BPF d\u00e9vore le monde | Le blog Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:22.647155+00:00
---

# Architecture Cloudflare et la manière dont BPF dévore le monde | Le blog Cloudflare

> Source: https://blog.cloudflare.com/fr-fr/cloudflare-architecture-and-how-bpf-eats-the-world/

[Blog](https://blog.cloudflare.com/fr-fr/)

[Anycast (FR)](https://blog.cloudflare.com/fr-fr/tag/anycast/)[Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)[eBPF](https://blog.cloudflare.com/fr-fr/tag/ebpf/)+3Afficher 3 étiquettes supplémentaires

6 tagsAfficher 6 tags

  * Tags de l’article
  * [Anycast (FR)](https://blog.cloudflare.com/fr-fr/tag/anycast/)[Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)
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



[Linux](https://blog.cloudflare.com/fr-fr/tag/linux/)[Programming](https://blog.cloudflare.com/fr-fr/tag/programming/)[TCP](https://blog.cloudflare.com/fr-fr/tag/tcp/)

[Anycast (FR)](https://blog.cloudflare.com/fr-fr/tag/anycast/)[Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)[eBPF](https://blog.cloudflare.com/fr-fr/tag/ebpf/)[Linux](https://blog.cloudflare.com/fr-fr/tag/linux/)[Programming](https://blog.cloudflare.com/fr-fr/tag/programming/)[TCP](https://blog.cloudflare.com/fr-fr/tag/tcp/)

18 mai 2019

# Architecture Cloudflare et la manière dont BPF dévore le monde

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/fr-fr/author/marek-majkowski/)

Lecture : 11 min.

Copier l'URL

Cet article est également disponible en [English](https://blog.cloudflare.com/cloudflare-architecture-and-how-bpf-eats-the-world/), [Deutsch](https://blog.cloudflare.com/de-de/cloudflare-architecture-and-how-bpf-eats-the-world/), [Español](https://blog.cloudflare.com/es-es/cloudflare-architecture-and-how-bpf-eats-the-world/) et [简体中文](https://blog.cloudflare.com/zh-cn/cloudflare-architecture-and-how-bpf-eats-the-world/).

![Cloudflare architecture and how BPF eats the world](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4625EY4M7N1KRERTHTYMFT.jpg&w=950&h=512&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////8/Lr2cu3zrig3tHI8fDz9Pb96Ofs////8u/n1MSqyLCM282+8u/v9vb66Obn////8u7l0cCfxKp52sy29PDt+Pj56ebk////9/Pq1cWmx7GA3tG6+PXw/Pz87erm//////324NW908Oh5t7L/f34////8vLu////////7una4trF8O7h////////9/v6////////+fjw7+vg+frz/////////P///////////v748/Hp/P75/////////f//)

Récemment à la[Netdev 0x13](https://www.netdevconf.org/0x13/schedule.html), lors de la conférence sur les réseaux Linux à Prague, je suis[brièvement intervenu sur « Linux chez Cloudflare »](https://netdevconf.org/0x13/session.html?panel-industry-perspectives). La [discussion](https://speakerdeck.com/majek04/linux-at-cloudflare) a surtout porté sur BPF. Il semble, peu importe la question, que la réponse soit BPF.

Voici une transcription d'une version légèrement modifiée de cette discussion.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - 8PjjfZ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S032Z8BX2FVSVHN1SG1E.jpg&w=715&h=458&f=webp&fit=cover&position=center)

Chez Cloudflare, nous utilisons Linux sur nos serveurs. Nous exploitons deux catégories de centres de données : les grands centres de données « Principaux » qui traitent les journaux, analysent les attaques et effectuent les analyses informatiques, et le parc de serveurs « Edge » qui fournit du contenu client à partir de 180 emplacements dans le monde.

Dans cette présentation, nous allons nous concentrer sur les serveurs « Edge ». C'est ici que nous utilisons les dernières fonctionnalités de Linux, optimisons la performance et accordons une grande attention à la résilience DoS.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - yMZ8oK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457DSJSJ59D0H3MJMH3XD1.png&w=715&h=458&f=webp&fit=cover&position=center)

Notre service de périphérie est particulier en raison de la configuration de notre réseau. Nous avons largement recours au routage anycast. Anycast signifie que le même ensemble d'adresses IP est annoncé par tous nos centres de données.

Cette conception possède de grands avantages. Premièrement, elle garantit la vitesse optimale aux utilisateurs finaux. Où que vous vous trouviez, vous atteindrez toujours le centre de données le plus proche. Anycast nous aide par ailleurs à répartir le trafic DoS. Lors des attaques, chacun des emplacements reçoit une petite fraction du trafic total, ce qui facilite l'ingestion et le filtrage du trafic indésirable.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - UmJ9T6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473V4QZBVPZJYMTAATAPT0.jpg&w=715&h=291&f=webp&fit=cover&position=center)

Anycast nous permet de maintenir la même configuration de mise en réseau dans tous les centres de données périphériques. Nous avons appliqué la même conception dans nos centres de données. Notre pile de logiciels est uniforme sur tous les serveurs périphériques. Tous les logiciels sont exécutés sur tous les serveurs.

En principe, chaque machine peut gérer toutes les tâches, et nous exécutons de nombreuses tâches diverses et exigeantes. Nous avons une pile HTTP complète, des Cloudflare Workers magiques, deux ensembles de serveurs DNS (faisant autorité et résolveur), ainsi que de nombreuses autres applications publiques, telles que Spectrum et Warp.

Même si tous les logiciels sont exécutés sur tous les serveurs, les requêtes traversent généralement de nombreuses machines dans leur déplacement vers la pile. Par exemple, une requête HTTP peut être gérée par une machine différente au cours de chacune des 5 étapes du traitement.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - Nx55Rn](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW451J7QR62Z3DR15BGJ56NW.png&w=715&h=371&f=webp&fit=cover&position=center)

Laissez-moi vous expliquer les premières étapes du traitement des paquets entrants :

(1) Premièrement, les paquets atteignent notre routeur. Le routeur effectue l’ECMP et transmet les paquets sur nos serveurs Linux. Nous utilisons l’ECMP pour répartir chaque IP cible sur de nombreuses machines (au moins 16). Ceci est utilisé comme une technique d'équilibrage de charge rudimentaire.

(2) Sur les serveurs, nous ingérons des paquets avec XDP/eBPF. Dans XDP, nous passons par deux étapes. Tout d'abord, nous effectuons des atténuations DoS volumétriques, en éliminant les paquets appartenant à de très grandes attaques de couche 3.

(3) Ensuite, toujours dans XDP, nous effectuons un équilibrage de charge de couche 4. Tous les paquets non impliqués dans les attaques sont redirigés sur les machines. Ceci est utilisé pour contourner les problèmes ECMP, nous donne un équilibrage de charge à granularité fine et nous permet de mettre gracieusement les serveurs hors service.

(4) Après la redirection, les paquets atteignent une machine désignée. À ce stade, ils sont ingérés par la pile de réseau Linux normale, passent par le pare-feu iptables habituel et sont envoyés à un socket réseau approprié.

(5) Enfin, les paquets sont reçus par une application. Par exemple, les connexions HTTP sont gérées par un serveur de « protocole », chargé d'effectuer le cryptage TLS et de traiter les protocoles HTTP, HTTP/2 et QUIC.

C'est au cours de ces premières phases du traitement des requêtes que nous utilisons les nouvelles fonctionnalités les plus intéressantes de Linux. Nous pouvons regrouper les fonctionnalités modernes utiles en trois catégories :

  * Traitement DoS
  * L'équilibrage de charge
  * Répartition de socket



* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - LhKOKN](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XXKSKV58CVZ3KRAQ9HS5.png&w=715&h=255&f=webp&fit=cover&position=center)

Discutons du traitement DoS plus en détail. Comme mentionné précédemment, la première étape après le routage ECMP est la pile XDP de Linux où, entre autres, nous exécutons des mesures d'atténuation de DoS.

Historiquement, nos mesures d'atténuation des attaques volumétriques étaient exprimées dans la grammaire classique de BPF et de style iptables. Récemment, nous les avons adaptés pour qu'ils s'exécutent dans le contexte XDP/eBPF, ce qui s'est avéré étonnamment difficile. Lisez la suite de nos aventures :

  * [L4Drop : Atténuations XDP DDoS](https://blog.cloudflare.com/l4drop-xdp-ebpf-based-ddos-mitigations/)
  * [xdpcap : Capture de paquets XDP](https://blog.cloudflare.com/xdpcap/)
  * [Discours sur l'atténuation DoS basée sur XDP](https://netdevconf.org/0x13/session.html?talk-XDP-based-DDoS-mitigation) par Arthur Fabre
  * [XDP en pratique : intégration de XDP dans notre pipeline d’atténuation des attaques DDoS](https://netdevconf.org/2.1/papers/Gilberto_Bertin_XDP_in_practice.pdf) (PDF)



Au cours de ce projet, nous avons rencontré un certain nombre de limitations eBPF/XDP. L'une d'elles était le manque de primitives de concurrence. Il était très difficile de mettre en œuvre des choses comme des « seaux à jetons sans course ». Plus tard, nous avons découvert que [Julia Kartseva, ingénieure chez Facebook](http://vger.kernel.org/lpc-bpf2018.html#session-9), avait les mêmes problèmes. En février, ce problème a été résolu avec l'introduction de l’assistant bpf_spin_lock.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - WuSEbO](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457FM8E07AEFEMGNVWSCNK.png&w=715&h=251&f=webp&fit=cover&position=center)

Bien que nos défenses DoS volumétriques modernes soient réalisées dans la couche XDP, nous dépendons toujours d’iptables pour les atténuations de la couche d'application 7. Ici, les fonctionnalités d’un pare-feu de niveau supérieur sont utiles : connlimit, hashlimits et ipsets. Nous utilisons également le module xt_bpf iptables pour exécuter cBPF dans iptables, afin de faire correspondre les charges utiles des paquets. Nous en avons parlé par le passé :

  * [Leçons à tirer de la défense de l'indéfendable](https://speakerdeck.com/majek04/lessons-from-defending-the-indefensible) (PPT)
  * [Présentation des outils BPF](https://blog.cloudflare.com/introducing-the-bpf-tools/)



* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - mLDecw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48SS2ZE7FC30R5AKRSDFV9.png&w=715&h=370&f=webp&fit=cover&position=center)

Après XDP et iptables, nous avons une dernière couche de défense DoS côté noyau.

Prenons un cas où nos mesures d'atténuation UDP échouent. Dans un tel cas, nous pourrions nous retrouver avec un flux de paquets frappant notre socket UDP d'application. Cela pourrait provoquer un débordement du socket, entraînant une perte de paquets. Ceci est problématique. Les bons et les mauvais paquets seraient supprimés sans distinction. Pour des applications comme DNS, cela est catastrophique. Dans le passé, pour réduire les dommages, nous utilisions un socket UDP par adresse IP. Une inondation non atténuée était néfaste, mais, au moins, elle n’affectait pas le trafic vers les autres adresses IP du serveur.

De nos jours, l'architecture n'est plus adaptée. Nous exploitons plus de 30 000 adresses IP DNS et l’exécution de ce nombre de sockets UDP n'est pas optimal. Notre solution moderne consiste à exécuter un seul socket UDP ayant un filtre de socket eBPF complexe, à l'aide de l'option de socket SO_ATTACH_BPF. Nous avons parlé d’exécuter eBPF sur des sockets réseau dans des articles de blog précédents :

  * [eBPF, sockets, distance de saut et assemblage eBPF de l’écriture manuelle](https://blog.cloudflare.com/epbf_sockets_hop_distance/)
  * [SOCKMAP - Épissure TCP de l'avenir](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/)



Le taux eBPF mentionné limite les paquets. Il conserve l'état et le nombre de paquets dans une carte eBPF. Nous pouvons être certains qu'une seule adresse IP inondée n'affectera pas le reste du trafic. Cela fonctionne bien mais, lors du travail sur ce projet, nous avons trouvé un bogue plutôt inquiétant dans le vérificateur eBPF :

  * [eBPF ne peut pas compter ?!](https://blog.cloudflare.com/ebpf-cant-count/)



J'imagine qu'exécuter eBPF sur un socket UDP n'est pas chose commune.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - qUqTiR](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48N4A8AJ8A882QX9ZJW00H.png&w=715&h=224&f=webp&fit=cover&position=center)

Outre le DoS, dans XDP, nous exécutons également une couche d'équilibrage de charge de couche 4. C'est un nouveau projet et nous n'en avons pas encore beaucoup parlé. Sans entrer dans les détails, dans certains cas, nous devons effectuer une recherche de socket à partir de XDP.

Le problème est relativement simple, notre code doit rechercher dans la structure du noyau « socket » un 5-tuple extrait d'un paquet. Ceci est généralement facile, un assistant bpf_sk_lookup est disponible à cet effet. Sans surprise, il y a eu quelques complications. L'impossibilité de vérifier si un paquet ACK reçu était un élément valide d'un établissement de liaison à trois voies lorsque les cookies SYN sont activés constituait un des problèmes. Mon collègue Lorenz Bauer travaille sur l'ajout d'un support pour ce cas.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - Z5AQj3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AZSQVK6GMC8GCG3QWTPE.png&w=715&h=232&f=webp&fit=cover&position=center)

Après DoS et les couches d'équilibrage de charge, les paquets sont transmis à la pile Linux TCP/UDP habituelle. Nous faisons ici une répartition du socket. Par exemple, les paquets allant au port 53 sont transmis à un socket appartenant à notre serveur DNS.

Nous faisons de notre mieux pour utiliser les fonctionnalités de Linux vanilla, mais la situation devient complexe lorsque vous utilisez des milliers d'adresses IP sur les serveurs.

Il est relativement facile de convaincre Linux de router les paquets correctement avec [l’astuce « AnyIP »](https://blog.cloudflare.com/how-we-built-spectrum). S'assurer que les paquets sont envoyés à la bonne application est un autre problème. Malheureusement, la logique de répartition des sockets Linux standard n’est pas suffisamment flexible pour répondre à nos attentes. Pour les ports populaires, tels que TCP/80, nous souhaitons partager le port entre plusieurs applications, chacune le gérant sur une plage d'adresses IP différente. Linux ne prend pas cela en charge dans d’autres contextes. Vous pouvez appeler bind () soit sur une adresse IP spécifique, soit sur toutes les adresses IP (avec 0.0.0.0).

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - UyelYs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW454X48JSVW3F7W532P8XA0.png&w=715&h=260&f=webp&fit=cover&position=center)

Afin de résoudre ce problème, nous avons développé un correctif de noyau personnalisé qui ajoute [uneoption de socketSO_BINDTOPREFIX](http://patchwork.ozlabs.org/patch/602916/). Comme son nom l'indique, cela nous permet d'appeler bind () sur un préfixe IP sélectionné. Cela résout le problème de plusieurs applications partageant des ports populaires tels que 53 ou 80.

Ensuite, nous rencontrons un autre problème. Pour notre produit Spectrum, nous devons écouter sur tous les 65 535 ports. Utiliser autant de sockets d’écoute n’est pas une bonne idée (voir [notre vieux blog d’histoire de guerre](https://blog.cloudflare.com/revenge-listening-sockets/)), nous avons donc dû trouver une autre astuce. Après quelques expériences, nous avons appris à utiliser un module inconnu iptables TPROXY à cet effet. Lisez à ce sujet ici :

  * [Abuser du pare-feu de Linux : le piratage qui nous a permis de construire Spectrum](https://blog.cloudflare.com/how-we-built-spectrum/)



Cette configuration fonctionne mais nous n'aimons pas les règles de pare-feu supplémentaires. Nous travaillons à résoudre ce problème correctement, en étendant réellement la logique de répartition des sockets. Vous l'avez deviné, nous voulons étendre la logique de répartition des sockets en utilisant eBPF. Attendez-vous à quelques correctifs de notre part.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - ii0Zd0](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KF3RTD2RE4TT91W3GYVE.png&w=715&h=370&f=webp&fit=cover&position=center)

Ensuite, il existe un moyen d'utiliser eBPF pour améliorer les applications. Nous nous sommes récemment montrés enthousiastes à l'idée de faire l'épissure TCP avec SOCKMAP :

  * [SOCKMAP - Épissure TCP de l'avenir](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/)



Cette technique offre un grand potentiel pour améliorer la latence de la file d’attente sur de nombreux composants de notre pile logicielle. L'implémentation du SOCKMAP actuel n'est pas encore prête pour le moment idéal, mais le potentiel est vaste.

De même, les nouveaux crochets [TCP-BPF aka BPF_SOCK_OPS](https://netdevconf.org/2.2/papers/brakmo-tcpbpf-talk.pdf)offrent un excellent moyen d'inspecter les paramètres de performance des flux TCP. Cette fonctionnalité est extrêmement utile pour notre équipe performance.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - uXroGK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FV0YJYWWZR3691CB3DMV.jpg&w=715&h=458&f=webp&fit=cover&position=center)

Certaines fonctionnalités de Linux n'ont pas bien vieilli et nous devons les contourner. Par exemple, nous atteignons les limites des métriques de réseau. Ne vous méprenez pas, les métriques de réseau sont impressionnantes. Malheureusement, elles ne sont pas assez granulaires. Des éléments comme TcpExtListenDrops et TcpExtListenOverflows sont signalés en tant que compteurs globaux, alors que nous devons les connaître en fonction des applications.

Notre solution consiste à utiliser des sondes eBPF pour extraire les nombres directement à partir du noyau. Mon collègue Ivan Babrou a mis sur pied un exportateur de métriques Prometheus appelé « ebpf_exporter » pour faciliter ce travail. À lire :

  * [Présentation d’ebpf_exporter](https://blog.cloudflare.com/introducing-ebpf_exporter/)
  * <https://github.com/cloudflare/ebpf_exporter>



Avec « ebpf_exporter », nous pouvons générer toutes sortes de métriques détaillées. Il est très puissant et nous a sauvés à de nombreuses reprises.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - iWWQYL](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TQR7YWXSSVZCMA3HPKBA.png&w=715&h=280&f=webp&fit=cover&position=center)

Dans cette présentation, nous avons discuté de 6 couches de fichiers BPF s'exécutant sur nos serveurs périphériques :

  * Les atténuations DoS volumétriques s'exécutent sur XDP/eBPF
  * Iptables xt_bpf cBPF pour les attaques des couches applicatives
  * SO_ATTACH_BPF pour les limites de débit sur les sockets UDP
  * Équilibreur de charge, fonctionnant sur XDP
  * eBPF exécutant des assistants d'application tels que SOCKMAP pour l'épissure de sockets TCP et TCP-BPF pour les mesures TCP
  * « ebpf_exporter » pour les métriques granulaires



Et nous ne faisons que commencer ! Bientôt, nous en ferons plus avec la répartition de socket basée sur eBPF, eBPF fonctionnant sur la couche [Linux TC (Traffic Control)](https://linux.die.net/man/8/tc) et davantage d'intégration avec les points d’encrages cgroup eBPF. Ensuite, notre équipe SRE gère une liste de plus en plus longue de [scripts BCC](https://github.com/iovisor/bcc)utiles au débogage.

On a l'impression que Linux a cessé de développer de nouvelles API et que toutes les nouvelles fonctionnalités sont implémentées en tant que crochets et assistants eBPF. C'est bien et cela présente de gros avantages. Il est plus facile et plus sûr de mettre à niveau le programme eBPF que de recompiler un module du noyau. Des fonctionnalités comme TCP-BPF, exposant des données de traçage de performance de volume élevé, seraient probablement impossibles à mettre en œuvre sans eBPF.

Certains disent que « les logiciels dévorent le monde », je dirais que : « BPF dévore le logiciel ».

Sur cette page

Discuter en ligne

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F&t=Architecture%20Cloudflare%20et%20la%20mani%C3%A8re%20dont%20BPF%20d%C3%A9vore%20le%20monde)[](https://x.com/intent/post?text=Architecture+Cloudflare+et+la+mani%C3%A8re+dont+BPF+d%C3%A9vore+le+monde&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://bsky.app/intent/compose?text=Architecture+Cloudflare+et+la+mani%C3%A8re+dont+BPF+d%C3%A9vore+le+monde+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://mastodonshare.com/?text=Architecture+Cloudflare+et+la+mani%C3%A8re+dont+BPF+d%C3%A9vore+le+monde&url=https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://www.threads.net/intent/post?text=Architecture+Cloudflare+et+la+mani%C3%A8re+dont+BPF+d%C3%A9vore+le+monde+https%3A%2F%2Fblog.cloudflare.com%2Ffr-fr%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)

## Tags associés

[Anycast (FR)](https://blog.cloudflare.com/fr-fr/tag/anycast/)[Développeurs](https://blog.cloudflare.com/fr-fr/tag/developers/)[eBPF](https://blog.cloudflare.com/fr-fr/tag/ebpf/)[Linux](https://blog.cloudflare.com/fr-fr/tag/linux/)[Programming](https://blog.cloudflare.com/fr-fr/tag/programming/)[TCP](https://blog.cloudflare.com/fr-fr/tag/tcp/)

Suivre sur les réseaux sociaux

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Abonnez-vous pour recevoir les notifications de nouveaux articles

Adresse e-mail

Nous ne partagerons jamais votre adresse e-mail.

S'abonner

Merci pour votre inscription ! Vérifiez votre boîte de réception pour confirmer.
