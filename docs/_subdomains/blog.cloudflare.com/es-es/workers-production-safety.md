---
url: https://blog.cloudflare.com/es-es/workers-production-safety/
title: Nuevas herramientas para la seguridad de la producci\u00f3n: implementaciones graduales, correlaciones de c\u00f3digo fuente, limitaci\u00f3n de velocidad y nuevos SDK | Blog de Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:28.460584+00:00
---

# Nuevas herramientas para la seguridad de la producción: implementaciones graduales, correlaciones de código fuente, limitación de velocidad y nuevos SDK | Blog de Cloudflare

> Source: https://blog.cloudflare.com/es-es/workers-production-safety/

[Blog](https://blog.cloudflare.com/es-es/)

[Cloudflare Workers](https://blog.cloudflare.com/es-es/tag/workers/)[Developer Week](https://blog.cloudflare.com/es-es/tag/developer-week/)[Observability](https://blog.cloudflare.com/es-es/tag/observability/)+2Mostrar 2 etiquetas más

5 etiquetasMostrar 5 etiquetas

  * Etiquetas de la publicación
  * [Cloudflare Workers](https://blog.cloudflare.com/es-es/tag/workers/)[Developer Week](https://blog.cloudflare.com/es-es/tag/developer-week/)[Rate Limiting (ES)](https://blog.cloudflare.com/es-es/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/es-es/tag/sdk/)
  * Todas las etiquetas
  * Etiquetas coincidentes
  * No se han encontrado etiquetas
  * [1.1.1.1](https://blog.cloudflare.com/es-es/tag/1-1-1-1/)
  * [Protección avanzada contra DDoS](https://blog.cloudflare.com/es-es/tag/advanced-ddos/)
  * [Preparación para agentes](https://blog.cloudflare.com/es-es/tag/agent-readiness/)
  * [Agentes](https://blog.cloudflare.com/es-es/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/es-es/tag/agents-week/)
  * [AI](https://blog.cloudflare.com/es-es/tag/ai/)
  * [AI Bots (ES)](https://blog.cloudflare.com/es-es/tag/ai-bots/)
  * [AI Gateway (ES)](https://blog.cloudflare.com/es-es/tag/ai-gateway/)
  * [AI Week](https://blog.cloudflare.com/es-es/tag/ai-week/)
  * [IA-SPM](https://blog.cloudflare.com/es-es/tag/ai-spm/)
  * [Always Online (ES)](https://blog.cloudflare.com/es-es/tag/always-online/)
  * [AMD (ES)](https://blog.cloudflare.com/es-es/tag/amd/)
  * [Analytics (ES)](https://blog.cloudflare.com/es-es/tag/analytics/)
  * [Anonymous (ES)](https://blog.cloudflare.com/es-es/tag/anonymous/)
  * [Anycast (ES)](https://blog.cloudflare.com/es-es/tag/anycast/)
  * [API](https://blog.cloudflare.com/es-es/tag/api/)
  * [Seguridad de la API](https://blog.cloudflare.com/es-es/tag/api-security/)
  * [Seguridad de aplicaciones](https://blog.cloudflare.com/es-es/tag/application-security/)
  * [Servicios de aplicación](https://blog.cloudflare.com/es-es/tag/application-services/)
  * [Athenian Project (ES)](https://blog.cloudflare.com/es-es/tag/athenian-project/)
  * [Ataques](https://blog.cloudflare.com/es-es/tag/attacks/)
  * [Automatización](https://blog.cloudflare.com/es-es/tag/automation/)
  * [AWS](https://blog.cloudflare.com/es-es/tag/aws/)
  * [Beta](https://blog.cloudflare.com/es-es/tag/beta/)
  * [Semana aniversario](https://blog.cloudflare.com/es-es/tag/birthday-week/)
  * [Black Friday (ES)](https://blog.cloudflare.com/es-es/tag/black-friday/)
  * [Gestión de bots](https://blog.cloudflare.com/es-es/tag/bot-management/)
  * [Botnet (ES)](https://blog.cloudflare.com/es-es/tag/botnet/)
  * [Bots](https://blog.cloudflare.com/es-es/tag/bots/)
  * [Representación del navegador](https://blog.cloudflare.com/es-es/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/es-es/tag/browser-run/)
  * [Bug Bounty (ES)](https://blog.cloudflare.com/es-es/tag/bug-bounty/)
  * [Caché](https://blog.cloudflare.com/es-es/tag/cache/)
  * [CASB](https://blog.cloudflare.com/es-es/tag/casb/)
  * [CDN](https://blog.cloudflare.com/es-es/tag/cdn/)
  * [Certificate Authority (ES)](https://blog.cloudflare.com/es-es/tag/certificate-authority/)
  * [Certificación](https://blog.cloudflare.com/es-es/tag/certification/)
  * [China (ES)](https://blog.cloudflare.com/es-es/tag/china/)
  * [CIO Week](https://blog.cloudflare.com/es-es/tag/cio-week/)
  * [CISA (ES)](https://blog.cloudflare.com/es-es/tag/cisa/)
  * [Cloud Email Security](https://blog.cloudflare.com/es-es/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/es-es/tag/cloudflare-access/)
  * [Cloudflare Calls](https://blog.cloudflare.com/es-es/tag/cloudflare-calls/)
  * [Cloudflare para startups](https://blog.cloudflare.com/es-es/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/es-es/tag/gateway/)
  * [Cloudflare One](https://blog.cloudflare.com/es-es/tag/cloudflare-one/)
  * [Cloudflare Pages](https://blog.cloudflare.com/es-es/tag/cloudflare-pages/)
  * [Cloudflare Queues](https://blog.cloudflare.com/es-es/tag/cloudflare-queues/)
  * [Cloudflare Workers](https://blog.cloudflare.com/es-es/tag/workers/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/es-es/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/es-es/tag/cloudforce-one/)
  * [Coinbase](https://blog.cloudflare.com/es-es/tag/coinbase/)
  * [Conformidad](https://blog.cloudflare.com/es-es/tag/compliance/)
  * [Compression (ES)](https://blog.cloudflare.com/es-es/tag/compression/)
  * [Connectivity (ES)](https://blog.cloudflare.com/es-es/tag/connectivity/)
  * [Conectividad cloud](https://blog.cloudflare.com/es-es/tag/connectivity-cloud/)
  * [Servicios al consumidor](https://blog.cloudflare.com/es-es/tag/consumer-services/)
  * [Contenedores](https://blog.cloudflare.com/es-es/tag/containers/)
  * [Contexto](https://blog.cloudflare.com/es-es/tag/context/)
  * [CrowdStrike (ES)](https://blog.cloudflare.com/es-es/tag/crowdstrike/)
  * [Crypto Week (ES)](https://blog.cloudflare.com/es-es/tag/crypto-week/)
  * [D1 (ES)](https://blog.cloudflare.com/es-es/tag/d1/)
  * [Data Localization (ES)](https://blog.cloudflare.com/es-es/tag/data-localization/)
  * [Data Transfer Bucket (ES)](https://blog.cloudflare.com/es-es/tag/data-transfer-bucket/)
  * [Base de datos](https://blog.cloudflare.com/es-es/tag/database/)
  * [DDoS](https://blog.cloudflare.com/es-es/tag/ddos/)
  * [Alertas DDoS](https://blog.cloudflare.com/es-es/tag/ddos-alerts/)
  * [Informes DDoS](https://blog.cloudflare.com/es-es/tag/ddos-reports/)
  * [Deep Dive (ES)](https://blog.cloudflare.com/es-es/tag/deep-dive/)
  * [Documentación para desarrolladores](https://blog.cloudflare.com/es-es/tag/developer-documentation/)
  * [Plataforma para desarrolladores](https://blog.cloudflare.com/es-es/tag/developer-platform/)
  * [Developer Week](https://blog.cloudflare.com/es-es/tag/developer-week/)
  * [Desarrolladores](https://blog.cloudflare.com/es-es/tag/developers/)
  * [DevOps (ES)](https://blog.cloudflare.com/es-es/tag/devops/)
  * [Digital Experience Monitoring (ES)](https://blog.cloudflare.com/es-es/tag/digital-experience-monitoring/)
  * [Diversity (ES)](https://blog.cloudflare.com/es-es/tag/diversity/)
  * [DLP](https://blog.cloudflare.com/es-es/tag/dlp/)
  * [DMARC (ES)](https://blog.cloudflare.com/es-es/tag/dmarc/)
  * [DNS](https://blog.cloudflare.com/es-es/tag/dns/)
  * [DNS Flood (ES)](https://blog.cloudflare.com/es-es/tag/dns-flood/)
  * [Dogfooding (ES)](https://blog.cloudflare.com/es-es/tag/dogfooding/)
  * [DoH (ES)](https://blog.cloudflare.com/es-es/tag/doh/)
  * [Durable Objects](https://blog.cloudflare.com/es-es/tag/durable-objects/)
  * [Early Hints (ES)](https://blog.cloudflare.com/es-es/tag/early-hints/)
  * [EC2 (ES)](https://blog.cloudflare.com/es-es/tag/ec2/)
  * [Seguridad del correo electrónico](https://blog.cloudflare.com/es-es/tag/email-security/)
  * [Emissions (ES)](https://blog.cloudflare.com/es-es/tag/emissions/)
  * [Ingeniería](https://blog.cloudflare.com/es-es/tag/engineering/)
  * [Entropy (ES)](https://blog.cloudflare.com/es-es/tag/entropy/)
  * [Firewall (ES)](https://blog.cloudflare.com/es-es/tag/firewall/)
  * [Football (ES)](https://blog.cloudflare.com/es-es/tag/football/)
  * [Forrester](https://blog.cloudflare.com/es-es/tag/forrester/)
  * [Foundation DNS (ES)](https://blog.cloudflare.com/es-es/tag/foundation-dns/)
  * [Carta de los fundadores](https://blog.cloudflare.com/es-es/tag/founders-letter/)
  * [Fraude](https://blog.cloudflare.com/es-es/tag/fraud/)
  * [Freedom of Speech (ES)](https://blog.cloudflare.com/es-es/tag/freedom-of-speech/)
  * [Frontend](https://blog.cloudflare.com/es-es/tag/front-end/)
  * [integral](https://blog.cloudflare.com/es-es/tag/full-stack/)
  * [GA Week (ES)](https://blog.cloudflare.com/es-es/tag/ga-week/)
  * [Gartner (ES)](https://blog.cloudflare.com/es-es/tag/gartner/)
  * [Gatebot (ES)](https://blog.cloudflare.com/es-es/tag/gatebot/)
  * [Disponibilidad general](https://blog.cloudflare.com/es-es/tag/general-availability/)
  * [Generative AI (ES)](https://blog.cloudflare.com/es-es/tag/generative-ai/)
  * [GitHub](https://blog.cloudflare.com/es-es/tag/github/)
  * [Google Cloud](https://blog.cloudflare.com/es-es/tag/google-cloud/)
  * [HTTP2 (ES)](https://blog.cloudflare.com/es-es/tag/http2/)
  * [Hyperdrive](https://blog.cloudflare.com/es-es/tag/hyperdrive/)
  * [Impacto](https://blog.cloudflare.com/es-es/tag/impact/)
  * [Impact Week (ES)](https://blog.cloudflare.com/es-es/tag/impact-week/)
  * [Intel](https://blog.cloudflare.com/es-es/tag/intel/)
  * [Interconnection](https://blog.cloudflare.com/es-es/tag/interconnection/)
  * [Rendimiento de Internet](https://blog.cloudflare.com/es-es/tag/internet-performance/)
  * [Calidad de Internet](https://blog.cloudflare.com/es-es/tag/internet-quality/)
  * [Desconexión de Internet](https://blog.cloudflare.com/es-es/tag/internet-shutdown/)
  * [Tráfico de Internet](https://blog.cloudflare.com/es-es/tag/internet-traffic/)
  * [Tendencias de Internet](https://blog.cloudflare.com/es-es/tag/internet-trends/)
  * [JAMstack (ES)](https://blog.cloudflare.com/es-es/tag/jamstack/)
  * [Jengo (ES)](https://blog.cloudflare.com/es-es/tag/jengo/)
  * [Killnet (ES)](https://blog.cloudflare.com/es-es/tag/killnet/)
  * [Latinoamérica](https://blog.cloudflare.com/es-es/tag/latin-america/)
  * [LavaRand (ES)](https://blog.cloudflare.com/es-es/tag/lavarand/)
  * [El día a día en Cloudflare](https://blog.cloudflare.com/es-es/tag/life-at-cloudflare/)
  * [LLM](https://blog.cloudflare.com/es-es/tag/llm/)
  * [Logs (ES)](https://blog.cloudflare.com/es-es/tag/logs/)
  * [Managed Rules (ES)](https://blog.cloudflare.com/es-es/tag/managed-rules/)
  * [MCP](https://blog.cloudflare.com/es-es/tag/mcp/)
  * [Meris (ES)](https://blog.cloudflare.com/es-es/tag/meris/)
  * [Microsoft Azure (ES)](https://blog.cloudflare.com/es-es/tag/microsoft-azure/)
  * [Mirai](https://blog.cloudflare.com/es-es/tag/mirai/)
  * [Mobile (ES)](https://blog.cloudflare.com/es-es/tag/mobile/)
  * [Multi-Cloud (ES)](https://blog.cloudflare.com/es-es/tag/multi-cloud/)
  * [MySQL](https://blog.cloudflare.com/es-es/tag/mysql/)
  * [NaaS (ES)](https://blog.cloudflare.com/es-es/tag/naas/)
  * [Network Interconnect (ES)](https://blog.cloudflare.com/es-es/tag/network-interconnect/)
  * [Network Protection (ES)](https://blog.cloudflare.com/es-es/tag/network-protection/)
  * [Servicios de red](https://blog.cloudflare.com/es-es/tag/network-services/)
  * [Notifications (ES)](https://blog.cloudflare.com/es-es/tag/notifications/)
  * [Olympics (ES)](https://blog.cloudflare.com/es-es/tag/olympics/)
  * [Interrupción](https://blog.cloudflare.com/es-es/tag/outage/)
  * [Page Rules (ES)](https://blog.cloudflare.com/es-es/tag/page-rules/)
  * [Socios](https://blog.cloudflare.com/es-es/tag/partners/)
  * [Rendimiento](https://blog.cloudflare.com/es-es/tag/performance/)
  * [Phishing](https://blog.cloudflare.com/es-es/tag/phishing/)
  * [Política y legal](https://blog.cloudflare.com/es-es/tag/policy/)
  * [Post mortem](https://blog.cloudflare.com/es-es/tag/post-mortem/)
  * [Privacidad](https://blog.cloudflare.com/es-es/tag/privacy/)
  * [Noticias de productos](https://blog.cloudflare.com/es-es/tag/product-news/)
  * [Proyecto Galileo](https://blog.cloudflare.com/es-es/tag/project-galileo/)
  * [Project Safekeeping (ES)](https://blog.cloudflare.com/es-es/tag/project-safekeeping/)
  * [Python (ES)](https://blog.cloudflare.com/es-es/tag/python/)
  * [Queues](https://blog.cloudflare.com/es-es/tag/queues/)
  * [R2 Super Slurper](https://blog.cloudflare.com/es-es/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/es-es/tag/cloudflare-radar/)
  * [Radar API (ES)](https://blog.cloudflare.com/es-es/tag/radar-api/)
  * [Randomness (ES)](https://blog.cloudflare.com/es-es/tag/randomness/)
  * [Ataques de rescate](https://blog.cloudflare.com/es-es/tag/ransom-attacks/)
  * [Rapid Reset (ES)](https://blog.cloudflare.com/es-es/tag/rapid-reset/)
  * [Rate Limiting (ES)](https://blog.cloudflare.com/es-es/tag/rate-limiting/)
  * [En tiempo real](https://blog.cloudflare.com/es-es/tag/real-time/)
  * [Regional Services (ES)](https://blog.cloudflare.com/es-es/tag/regional-services/)
  * [Gestión de riesgos](https://blog.cloudflare.com/es-es/tag/risk-management/)
  * [Routing (ES)](https://blog.cloudflare.com/es-es/tag/routing/)
  * [SaaS (ES)](https://blog.cloudflare.com/es-es/tag/saas/)
  * [Seguridad SaaS](https://blog.cloudflare.com/es-es/tag/saas-security/)
  * [Sable (ES)](https://blog.cloudflare.com/es-es/tag/sable/)
  * [de espacios aislados](https://blog.cloudflare.com/es-es/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/es-es/tag/sase/)
  * [SDK](https://blog.cloudflare.com/es-es/tag/sdk/)
  * [Puerta de enlace web segura](https://blog.cloudflare.com/es-es/tag/secure-web-gateway/)
  * [Seguridad](https://blog.cloudflare.com/es-es/tag/security/)
  * [Centro de seguridad](https://blog.cloudflare.com/es-es/tag/security-center/)
  * [Security Posture (ES)](https://blog.cloudflare.com/es-es/tag/security-posture/)
  * [Gestión de la postura de seguridad](https://blog.cloudflare.com/es-es/tag/security-posture-management/)
  * [Security Service Edge (ES)](https://blog.cloudflare.com/es-es/tag/security-service-edge/)
  * [Security Week](https://blog.cloudflare.com/es-es/tag/security-week/)
  * [Sin servidor](https://blog.cloudflare.com/es-es/tag/serverless/)
  * [SIEM (ES)](https://blog.cloudflare.com/es-es/tag/siem/)
  * [SIM (ES)](https://blog.cloudflare.com/es-es/tag/sim/)
  * [Snippets (ES)](https://blog.cloudflare.com/es-es/tag/snippets/)
  * [South America (ES)](https://blog.cloudflare.com/es-es/tag/south-america/)
  * [Velocidad](https://blog.cloudflare.com/es-es/tag/speed/)
  * [Velocidad/fiabilidad](https://blog.cloudflare.com/es-es/tag/speed-and-reliability/)
  * [Speed Week (ES)](https://blog.cloudflare.com/es-es/tag/speed-week/)
  * [Sports (ES)](https://blog.cloudflare.com/es-es/tag/sports/)
  * [SSE (ES)](https://blog.cloudflare.com/es-es/tag/sse/)
  * [Almacenamiento](https://blog.cloudflare.com/es-es/tag/storage/)
  * [Sumo Logic (ES)](https://blog.cloudflare.com/es-es/tag/sumo-logic/)
  * [Supercloud (ES)](https://blog.cloudflare.com/es-es/tag/supercloud/)
  * [Sustainability (ES)](https://blog.cloudflare.com/es-es/tag/sustainability/)
  * [SYN Flood (ES)](https://blog.cloudflare.com/es-es/tag/syn-flood/)
  * [Equipo](https://blog.cloudflare.com/es-es/tag/team/)
  * [Teams Dashboard (ES)](https://blog.cloudflare.com/es-es/tag/teams-dashboard/)
  * [Testing (ES)](https://blog.cloudflare.com/es-es/tag/testing/)
  * [Información sobre amenazas](https://blog.cloudflare.com/es-es/tag/threat-intelligence/)
  * [Operaciones de amenazas](https://blog.cloudflare.com/es-es/tag/threat-operations/)
  * [Amenazas](https://blog.cloudflare.com/es-es/tag/threats/)
  * [Tor (ES)](https://blog.cloudflare.com/es-es/tag/tor/)
  * [Orígenes ](https://blog.cloudflare.com/es-es/tag/traffic/)
  * [Transparencia](https://blog.cloudflare.com/es-es/tag/transparency/)
  * [Tendencias](https://blog.cloudflare.com/es-es/tag/trends/)
  * [Servidor TURN](https://blog.cloudflare.com/es-es/tag/turn-server/)
  * [Vectorize (ES)](https://blog.cloudflare.com/es-es/tag/vectorize/)
  * [VoIP (ES)](https://blog.cloudflare.com/es-es/tag/voip/)
  * [WAF](https://blog.cloudflare.com/es-es/tag/waf/)
  * [Waiting Room (ES)](https://blog.cloudflare.com/es-es/tag/waiting-room/)
  * [WARP Connector (ES)](https://blog.cloudflare.com/es-es/tag/warp-connector/)
  * [WASM (ES)](https://blog.cloudflare.com/es-es/tag/wasm/)
  * [Firewall de aplicaciones web](https://blog.cloudflare.com/es-es/tag/web-application-firewall/)
  * [WebAssembly (ES)](https://blog.cloudflare.com/es-es/tag/webassembly/)
  * [WebRTC](https://blog.cloudflare.com/es-es/tag/webrtc/)
  * [Workers AI](https://blog.cloudflare.com/es-es/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/es-es/tag/workers-launchpad/)
  * [x402](https://blog.cloudflare.com/es-es/tag/x402/)
  * [Resumen del año](https://blog.cloudflare.com/es-es/tag/year-in-review/)
  * [Zero Day Threats (ES)](https://blog.cloudflare.com/es-es/tag/zero-day-threats/)
  * [Zero Trust](https://blog.cloudflare.com/es-es/tag/zero-trust/)



[Rate Limiting (ES)](https://blog.cloudflare.com/es-es/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/es-es/tag/sdk/)

[Cloudflare Workers](https://blog.cloudflare.com/es-es/tag/workers/)[Developer Week](https://blog.cloudflare.com/es-es/tag/developer-week/)[Observability](https://blog.cloudflare.com/es-es/tag/observability/)[Rate Limiting (ES)](https://blog.cloudflare.com/es-es/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/es-es/tag/sdk/)

4 de abril de 2024

# Nuevas herramientas para la seguridad de la producción: implementaciones graduales, correlaciones de código fuente, limitación de velocidad y nuevos SDK

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/es-es/author/tanushree/) y [Jacob Bednarz](https://blog.cloudflare.com/es-es/author/jacob-bednarz/)

15 min de lectura

COPIAR URL

Esta publicación también está disponible en [English](https://blog.cloudflare.com/workers-production-safety/), [Deutsch](https://blog.cloudflare.com/de-de/workers-production-safety/), [Français](https://blog.cloudflare.com/fr-fr/workers-production-safety/), [日本語](https://blog.cloudflare.com/ja-jp/workers-production-safety/), [한국어](https://blog.cloudflare.com/ko-kr/workers-production-safety/), [繁體中文](https://blog.cloudflare.com/zh-tw/workers-production-safety/) y [简体中文](https://blog.cloudflare.com/zh-cn/workers-production-safety/).

![New tools for production safety — Gradual deployments, Source maps, Rate Limiting, and new SDKs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FR4MNGHSCH0P7DD7P68W.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+//769vXz8fDw8vHx9PLy8u7u6+fl/////vz98vT16+7y6+7z7u/17ezw5+Tm/////f3/8PP55u315ez36O356Orz5OPq////////8vb+5/D65e/85+/+6Oz55Obv////////+f3/7/f/7Pb/7fb/7fL/6uz2////////////+///+P7/9/7/9fr/8vT8/////////////////////////P//+Pv/////////////////////////////+/3/)

Developer Week 2024 está dedicada a la puesta en producción. El lunes 1 de abril, [anunciamos](https://blog.cloudflare.com/es-es/making-full-stack-easier-d1-ga-hyperdrive-queues-es-es/) que [D1](https://developers.cloudflare.com/d1/), [Queues](https://developers.cloudflare.com/queues/), [Hyperdrive](https://developers.cloudflare.com/hyperdrive/) y [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) están listos para pasar a la escala de producción y disponibles de forma general. El martes 2 de abril, [anunciamos](https://blog.cloudflare.com/es-es/workers-ai-ga-huggingface-loras-python-support-es-es/) lo mismo sobre nuestra plataforma de inferencia, [Workers AI](https://developers.cloudflare.com/workers-ai/). Y aún no hemos terminado.

Sin embargo, la puesta en producción no depende únicamente de la escala y la fiabilidad de los servicios con los que desarrollas. También necesitas herramientas para realizar cambios de forma segura y fiable. Dependes no solo de lo que proporciona Cloudflare, sino de poder controlar y adaptar con precisión el comportamiento de Cloudflare según las necesidades de tu aplicación.

Hoy anunciamos cinco novedades que te darán más poder: implementaciones graduales, stack traces con correlaciones de código fuente en Tail Workers, una nueva API de limitación de velocidad, nuevos SDK de API y actualizaciones de Durable Objects, cada una de ellas creadas específicamente para los servicios esenciales de producción. Nosotros desarrollamos nuestros propios productos utilizando Workers, como [Access](https://developers.cloudflare.com/cloudflare-one/policies/access/), [R2](https://developers.cloudflare.com/r2/), [KV](https://developers.cloudflare.com/kv/), [Waiting Room](https://developers.cloudflare.com/waiting-room/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Queues](https://developers.cloudflare.com/queues/) [Stream](https://developers.cloudflare.com/stream/) y muchos otros. Confiamos en cada una de estas nuevas funciones para garantizar que estamos preparados para la producción, y ahora estamos encantados de ponerlas a disponibilidad de todos.

### Implementa gradualmente los cambios en Workers y Durable Objects

La implementación de un Worker es casi instantánea: unos segundos y tu cambio se habrá aplicado [en todas partes](https://www.cloudflare.com/network/).

A escala de producción, cualquier cambio que realizas conlleva un mayor riesgo, tanto en términos de volumen como de expectativas. Necesitas cumplir tu SLA de disponibilidad del 99,99 %, o tienes un ambicioso SLO de latencia P90. Una implementación errónea que esté activa para la totalidad del tráfico durante apenas 45 segundos podría significar que millones de solicitudes recibieran un error. Un pequeño cambio en el código podría causar un ingente aluvión de reintentos a un backend desbordado, si toda la implementación se realiza de una sola vez. Estos son los tipos de riesgos que tenemos en cuenta y mitigamos nosotros mismos para nuestros propios servicios basados en Workers.

La forma de mitigar estos riesgos es implementar los cambios gradualmente (lo que se denomina habitualmente como implementaciones progresivas):

  1. La versión actual de tu aplicación se ejecuta en el entorno de producción.
  2. Implementas la nueva versión de tu aplicación en el entorno de producción, pero solo direccionas un pequeño porcentaje del tráfico a esta nueva versión, y esperas a que se "empape" en producción, controlando si hay regresiones y errores. Si algo falla, lo habrás detectado a tiempo en un pequeño porcentaje del tráfico (p. ej. el 1 %) y puede revertirse rápidamente.
  3. Incrementa gradualmente el porcentaje hasta que la nueva versión reciba la totalidad del tráfico, momento en el que esta se habrá implementado por completo.



Hoy presentamos un método de primera clase para implementar cambios de código de forma gradual en Workers y Durable Objects a través de la [API de Cloudflare](https://developers.cloudflare.com/api/operations/worker-deployments-list-deployments), la [CLI de Wrangler](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-wrangler) o el [panel de control de Workers](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-the-cloudflare-dashboard). Las implementaciones graduales están disponibles en la versión beta abierta. Puedes utilizar esta función con cualquier cuenta de Cloudflare del [plan gratuito de Workers](https://developers.cloudflare.com/workers/platform/pricing/#workers), y en breve podrás empezar a utilizarla con cuentas de Cloudflare de los [planes de pago de Workers](https://developers.cloudflare.com/workers/platform/pricing/#workers) y Enterprise. Cuando esté disponible el acceso para tu cuenta, verás un banner en el panel de Workers.

Si tienes dos versiones de tu Worker o Durable Object ejecutándose simultáneamente en producción, probablemente querrás poder filtrar tus métricas, excepciones y registros según la versión. Esto te permitirá detectar los problemas de producción en una fase temprana, con la nueva versión solo implementada en un pequeño porcentaje del tráfico, o comparar las métricas de rendimiento al dividir el tráfico en dos mitades. También hemos añadido observabilidad a nivel de versión en toda nuestra plataforma:

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Splitting traffic between different versions of a Worker.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4792EFMEWR5SFVJAMDC49A.png&w=715&h=353&f=webp&fit=cover&position=center)

  * Puedes filtrar por versión los análisis en el panel de control de Workers y a través de [la API de GraphQL Analytics](https://developers.cloudflare.com/analytics/graphql-api/).
  * [Workers Trace Events](https://developers.cloudflare.com/workers/observability/logging/logpush/) y [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) incluyen el ID de versión de tu Worker, junto con los campos opcionales de mensaje de versión y etiqueta de versión.
  * Si utilizas [wrangler tail](https://developers.cloudflare.com/workers/wrangler/commands/#tail) para visualizar los registros en directo, puedes ver los registros de una versión concreta.
  * Puedes acceder al ID, al mensaje y a la etiqueta de versión desde el código de tu Worker, configurando el [enlace Metadatos de versión](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/).



Es posible que también quieras asegurarte de que cada cliente o usuario vea solo una versión coherente de tu Worker. Hemos añadido la [Afinidad de versión](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity) para que las solicitudes asociadas a un identificador específico (p. ej., usuario, sesión o cualquier identificador único) siempre las gestione una versión coherente de tu Worker. La [Afinidad de sesión](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity), cuando se utiliza con el [motor de conjunto de reglas](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#setting-cloudflare-workers-version-key-using-ruleset-engine), te proporciona un control total tanto sobre el mecanismo como sobre el identificador que se utilizan para garantizar esta persistencia.

Las implementaciones granulares ya están disponibles en la versión beta abierta. Conforme avanzamos hacia su disponibilidad general, estamos trabajando para ofrecer:

  * **Anulaciones de versión.** Invoca una versión específica de tu Worker para probarla antes de que sirva tráfico de producción. Esto te permitirá crear implementaciones azul-verde.
  * **Cloudflare Pages.** Deja que el sistema de integración y distribución continuas (CI/CD) de Cloudflare Pages avance automáticamente las implementaciones en tu nombre.
  * **Reversiones automáticas.** Revierte automáticamente las implementaciones cuando aumente la tasa de errores para una nueva versión de tu Worker.



¡Esperamos recibir tus comentarios! Dinos qué te parece mediante [este formulario](https://www.cloudflare.com/lp/developer-week-deployments/) de comentarios o ponte en contacto con nosotros en nuestro [Discord para desarrolladores](https://discord.gg/HJvPcPcN) en el canal #workers-gradual-deployments-beta.

### Stack traces con correlaciones de código fuente en Tail Workers

La puesta en producción requiere un seguimiento de los errores y las excepciones, e intentar reducirlos a cero. Cuando se produce un error, normalmente lo primero que compruebas es el [stack trace](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack) del error: las funciones concretas que se han invocado, en qué orden, desde qué línea y archivo, y con qué argumentos.

La mayor parte del código JavaScript (no solo en Workers, sino en todas las plataformas) primero se empaqueta, a menudo se transpila y luego se minifica antes de su implementación en producción. Estas tareas se realizan en segundo plano para crear paquetes más pequeños a fin de optimizar el rendimiento y realizar la conversión de Typescript a Javascript si es necesario.

Si te has encontrado alguna vez que una excepción devuelve un stack trace como: /src/index.js:1:342, significa que el error se produjo en el carácter 342 del código minificado de tu función. Evidentemente, esto no es muy útil para fines de depuración.

Las [source-maps](https://web.dev/articles/source-maps) correlaciones de código fuente resuelven este problema: vuelven a asignar el código compilado y minificado al código original que escribiste. Las correlaciones de código fuente se combinan con el stack trace que ha devuelto el tiempo de ejecución de JavaScript para presentarte un stack trace que puedas leer. Por ejemplo, el siguiente stack trace muestra que el Worker ha recibido un valor nulo inesperado en la línea 30 del archivo down.ts. Este es un punto de partida útil para la depuración, y puedes desplazarte hacia abajo por el stack trace para ver las funciones que se han invocado y que han generado el valor nulo.

Así es como funciona:
    
    
    Unexpected input value: null
      at parseBytes (src/down.ts:30:8)
      at down_default (src/down.ts:10:19)
      at Object.fetch (src/index.ts:11:12)

  1. Si estableces upload_source_maps = true en tu [wrangler.toml](https://developers.cloudflare.com/workers/wrangler/configuration/), Wrangler generará y cargará automáticamente los archivos de correlación de código fuente cuando ejecutes [wrangler deploy](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) o [wrangler versions upload](https://developers.cloudflare.com/workers/wrangler/commands/#versions).
  2. Cuando tu Worker emite una excepción no detectada, recuperamos la correlación de código fuente y la utilizamos para correlacionar el stack trace de la excepción con las líneas del código fuente original de tu Worker.
  3. A continuación, puedes ver este stack trace sin ofuscación en los [registros en tiempo real](https://developers.cloudflare.com/workers/observability/logging/real-time-logs/) o en [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/).



A partir de hoy, en la versión beta abierta, puedes cargar correlaciones de código fuente a Cloudflare al implementar tu Worker. [Para empezar, consulta la documentación](https://developers.cloudflare.com/workers/observability/source-maps). A partir del 15 de abril, el tiempo de ejecución de Workers empezará a utilizar correlaciones de código fuente para desofuscar los stack traces. Cuando los stack traces con correlaciones de código fuente estén disponibles, publicaremos una notificación en el panel de control de Cloudflare y en nuestra [cuenta de X para desarrolladores de Cloudflare](https://twitter.com/CloudflareDev?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor).

### Nueva API de limitación de velocidad en Workers

Una API solo está lista para la producción si tiene un [límite de velocidad](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/) adecuado. A medida que crece tu negocio, también lo hacen la complejidad y la diversidad de los límites que necesitas aplicar para equilibrar las necesidades de clientes específicos, proteger el estado de tu servicio o aplicar y ajustar límites en escenarios concretos. La propia API de Cloudflare afronta este desafío: cada una de nuestras docenas de productos, cada uno con muchos puntos finales de la API, puede necesitar aplicar distintos límites de velocidad.

Desde 2017 puedes configurar [reglas de limitación de velocidad](https://developers.cloudflare.com/waf/rate-limiting-rules/) en Cloudflare. No obstante, hasta hoy la única forma de controlar esto era mediante el panel de control o la API de Cloudflare. No había sido posible definir el comportamiento en _tiempo de ejecución_ , o escribir código en Worker que interactuara directamente con los límites de velocidad. Solo podías controlar si una solicitud tenía o no limitación de velocidad antes de que llegara a tu Worker.

Hoy presentamos una nueva API, en versión beta abierta, que te permite acceder directamente a los límites de velocidad desde tu Worker. Es muy rápida, está basada en memcached y es muy fácil de añadir a tu Worker. Por ejemplo, la siguiente configuración define un límite de velocidad de 100 solicitudes en un periodo de 60 segundos:

A continuación, en tu Worker, puedes invocar el método limit en el enlace RATE_LIMITER, proporcionando la clave que prefieras. Con la configuración anterior, este código devolverá un código de estado de respuesta [HTTP 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) cuando se realicen más de 100 solicitudes a una ruta específica en un periodo de 60 segundos:
    
    
    [[unsafe.bindings]]
    name = "RATE_LIMITER"
    type = "ratelimit"
    namespace_id = "1001" # An identifier unique to your Cloudflare account
    
    # Limit: the number of tokens allowed within a given period, in a single Cloudflare location
    # Period: the duration of the period, in seconds. Must be either 60 or 10
    simple = { limit = 100, period = 60 } 

Ahora que Workers puede conectarse directamente a un almacén de datos como memcached, ¿qué más podríamos proporcionar? ¿Contadores? ¿Bloqueos? ¿Una [caché en memoria](https://github.com/cloudflare/workerd/pull/1666)? La limitación de velocidad es la primera de muchas primitivas que estamos estudiando ofrecer en Workers y que responden a las preguntas que llevamos años escuchando acerca de dónde se debería encontrar un estado compartido temporal que abarque muchos [aislamientos](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates) de Worker. Si actualmente dependes de poner el estado en el ámbito global de tu Worker, estamos trabajando en mejores primitivas creadas específicamente para casos de uso concretos.
    
    
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

La API de limitación de velocidad en Workers está en la versión beta abierta. Para empezar a utilizarla, [lee la documentación](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit).

### Nuevos SDK generados automáticamente para la API de Cloudflare

La puesta en producción implica pasar de realizar cambios mediante clics en un panel de control a hacerlos mediante programación, utilizando un enfoque de infraestructura como código, como [Terraform](https://github.com/cloudflare/terraform-provider-cloudflare) o [Pulumi](https://github.com/pulumi/pulumi-cloudflare), o haciendo llamadas API directamente, ya sea por tu cuenta o mediante un SDK.

La [API de Cloudflare](https://developers.cloudflare.com/api/) es masiva e incorpora continuamente nuevas capacidades: de media, [actualizamos nuestros esquemas de API entre 20 y 30 veces al día](https://github.com/cloudflare/api-schemas/activity). Sin embargo, hasta la fecha hemos estado desarrollando y manteniendo nuestros SDK de API manualmente, por lo que nos urgía automatizar estas tareas.

Eso es lo que hemos hecho, y hoy anunciamos nuevos SDK de cliente para la API de Cloudflare en tres lenguajes: [Typescript](https://github.com/cloudflare/cloudflare-typescript), [Python](https://github.com/cloudflare/cloudflare-python) y [Go](https://github.com/cloudflare/cloudflare-go), y próximamente en otros.

Cada SDK se genera automáticamente mediante la [API de Stainless](https://www.stainlessapi.com/), basada en los [esquemas OpenAPI](https://github.com/cloudflare/api-schemas) que definen la estructura y las capacidades de cada uno de nuestros puntos finales de la API. Esto significa que cuando añadimos cualquier nueva funcionalidad a la API de Cloudflare, en cualquier producto de Cloudflare, estos SDK de API se vuelven a generar automáticamente y se publican nuevas versiones, lo que garantiza que son correctos y están actualizados.

Puedes instalar los SDK ejecutando uno de estos comandos:

Si utilizas Terraform o Pulumi, a nivel interno el proveedor Terraform de Cloudflare utiliza actualmente el [SDK de Go](https://github.com/cloudflare/cloudflare-go) existente no automatizado. Cuando ejecutas terraform apply, el proveedor Terraform de Cloudflare determina qué solicitudes de API realizar y en qué orden, y las ejecuta utilizando el SDK de Go.
    
    
    // Typescript
    npm install cloudflare
    
    // Python
    pip install cloudflare
    
    // Go
    go get -u github.com/cloudflare/cloudflare-go/v2

El nuevo SDK de Go generado automáticamente abre el camino para una compatibilidad más completa con Terraform en todos los productos de Cloudflare, ya que ofrece un conjunto básico de herramientas que te garantizan que son correctos y que están actualizados con los últimos cambios de la API. Estamos trabajando para que, en el futuro, cada vez que un equipo de producto de Cloudflare desarrolle una nueva función que esté disponible mediante la API de Cloudflare, esta función sea automáticamente compatible con los SDK. Verás más novedades sobre esto a lo largo de 2024.

### Disponibilidad general del análisis del espacio de nombres de Durable Objetcs y WebSocket Hibernation

Muchos de nuestros propios productos, como [Waiting Room](https://developers.cloudflare.com/waiting-room/), [R2](https://developers.cloudflare.com/r2/) y [Queues](https://developers.cloudflare.com/queues/), y plataformas como [PartyKit](https://www.partykit.io/), se desarrollan utilizando [Durable Objects](https://developers.cloudflare.com/durable-objects/). Puedes considerar Durable Objects (implementados en todo el mundo, incluido el nuevo soporte para Oceanía) como Workers singleton que pueden proporcionar un único punto de coordinación y [persistencia de estado](https://developers.cloudflare.com/durable-objects/api/transactional-storage-api/). Son perfectos para las aplicaciones que necesitan coordinación de usuarios en tiempo real, como el chat interactivo o la edición colaborativa. Según Atlassian:

> _Una de nuestras nuevas capacidades son_ _[las pizarras de Confluence](https://www.atlassian.com/software/confluence/whiteboards), con las que podemos capturar con libertad el trabajo no estructurado, como la lluvia de ideas y la planificación inicial, antes de que los equipos lo documenten de manera más formal. El equipo consideró muchas opciones para la colaboración en tiempo real y finalmente decidió utilizar Durable Objects de Cloudflare. Durable Objects ha demostrado ser la solución perfecta a este problema, con una combinación única de funcionalidades que nos ha permitido simplificar enormemente nuestra infraestructura y escalar fácilmente a un gran número de usuarios. -_ [_Atlassian_](https://www.atlassian.com/software/confluence/whiteboards)

Antes no mostrábamos las tendencias analíticas asociadas en el panel de control, lo que hacía difícil comprender los patrones de uso y las tasas de error en un [espacio de nombres de Durable Objects](https://developers.cloudflare.com/durable-objects/configuration/access-durable-object-from-a-worker/#generate-ids-randomly), a menos que utilizaras directamente la [API de GraphQL Analytics](https://developers.cloudflare.com/analytics/graphql-api/). Hemos renovado el [panel de control de Durable Objects](https://dash.cloudflare.com/?to=/:account/workers/durable-objects), que ahora te permite detallar en las métricas tanto como necesites.

Desde el [primer día](https://blog.cloudflare.com/introducing-workers-durable-objects), Durable Objects ha ofrecido compatibilidad con [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), por lo que muchos clientes pueden conectarse directamente a un Durable Object para enviar y recibir mensajes.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2305 Embedded Image - tUWMOW](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NGJQ7SMHCNME7M5TATPN.png&w=715&h=557&f=webp&fit=cover&position=center)

Sin embargo, a veces las aplicaciones cliente abren una conexión WebSocket y luego no hacen... nada. Piensa en esa pestaña que tienes abierta en el navegador desde hace 5 horas y que aún no has tocado. Si utiliza WebSockets para enviar y recibir mensajes, en realidad tiene una conexión TCP de larga duración que no se utiliza para nada. Si esta conexión es a un Durable Object, este debe permanecer en ejecución, a la espera de que ocurra algo, consumiendo memoria y costándote dinero.

Inicialmente [presentamos WebSocket Hibernation](https://blog.cloudflare.com/workers-pricing-scale-to-zero) para resolver este problema. Hoy anunciamos que esta función pasa de su versión beta abierta a la disponibilidad general. Con WebSocket Hibernation, estableces una respuesta automática que se utilizará durante la hibernación y serializas el estado de modo que persiste tras la hibernación. Esto proporciona a Cloudflare la información que necesitamos para mantener abiertas las conexiones WebSocket de los clientes durante la "hibernación" del Durable Object, de manera que no se ejecuta activamente, ni se te factura por el tiempo de inactividad. Como resultado, tu estado siempre está disponible en memoria cuando realmente lo necesitas, pero no se mantiene innecesariamente cuando no es así. Mientras tu Durable Object esté hibernando, aunque haya clientes activos todavía conectados a través de un WebSocket, no se te facturará por esa duración.

Además, hemos respondido a los comentarios de los desarrolladores sobre los costes de los mensajes WebSocket entrantes a Durable Objects, que favorecen los mensajes más pequeños y frecuentes para la comunicación en tiempo real. A partir de hoy, los mensajes WebSocket entrantes se facturarán al equivalente de una veinteava parte de una solicitud (en lugar de que 1 mensaje equivalga a 1 solicitud, como hasta ahora). A continuación se mostramos un [ejemplo de precios](https://developers.cloudflare.com/durable-objects/platform/pricing/#example-4):

.tg {border-collapse:collapse;border-color:#ccc;border-spacing:0;} .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top} .tg .tg-4kyp{color:#0E101A;text-align:left;vertical-align:top} .tg .tg-bhdc{color:#0E101A;font-weight:bold;text-align:left;vertical-align:top}

| WebSocket Connection Requests | Incoming WebSocket Messages | Billed Requests | Request Billing  
---|---|---|---|---  
Before | 10K | 432M | 432,010,000 | $64.65  
After | 10K | 432M | 21,610,000 | $3.09  
  
Solicitudes de conexión WebSocket

Mensajes WebSocket entrantes

Solicitudes facturadas

Facturación de solicitudes

Antes

10K

432M

432 010 000

64,65 USD

Después

10K

432M

21 610 000

3,09 USD

### Listo para entornos de producción, sin la complejidad del entorno de producción

En la última generación de plataformas en la nube, prepararse para la puesta en producción significaba ralentizar el lanzamiento. Significaba combinar muchas herramientas desconectadas o crear equipos enteros dedicados a trabajar en las plataformas internas. Tenías que adaptar tus propias capas de productividad a plataformas que ponían obstáculos.

La plataforma para desarrolladores de Cloudflare ha crecido y está lista para la puesta en producción, con el compromiso de ser una plataforma integrada en la que los productos funcionen juntos de forma intuitiva y donde no haya 10 formas de hacer lo mismo, sin necesidad de una matriz de compatibilidad que ayude a entender qué elementos funcionan juntos. Cada una de estas actualizaciones muestra esto en la práctica, integrando nuevas funcionalidades en todos los productos y componentes de la plataforma de Cloudflare.

Con ese objetivo, queremos que nos digas no solo lo que quieres ver a continuación, sino también dónde crees que podríamos simplificar aún más, o dónde crees que nuestros productos podrían funcionar mejor juntos. Cuéntanos dónde crees que podríamos hacer más: nuestro [Discord para desarrolladores de Cloudflare](https://discord.cloudflare.com/) está siempre abierto.

En esta página

Debatir en línea

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fworkers-production-safety%2F&t=Nuevas%20herramientas%20para%20la%20seguridad%20de%20la%20producci%C3%B3n%3A%20implementaciones%20graduales%2C%20correlaciones%20de%20c%C3%B3digo%20fuente%2C%20limitaci%C3%B3n%20de%20velocidad%20y%20nuevos%20SDK)[](https://x.com/intent/post?text=Nuevas+herramientas+para+la+seguridad+de+la+producci%C3%B3n%3A+implementaciones+graduales%2C+correlaciones+de+c%C3%B3digo+fuente%2C+limitaci%C3%B3n+de+velocidad+y+nuevos+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fworkers-production-safety%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fworkers-production-safety%2F)[](https://bsky.app/intent/compose?text=Nuevas+herramientas+para+la+seguridad+de+la+producci%C3%B3n%3A+implementaciones+graduales%2C+correlaciones+de+c%C3%B3digo+fuente%2C+limitaci%C3%B3n+de+velocidad+y+nuevos+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fworkers-production-safety%2F)[](https://mastodonshare.com/?text=Nuevas+herramientas+para+la+seguridad+de+la+producci%C3%B3n%3A+implementaciones+graduales%2C+correlaciones+de+c%C3%B3digo+fuente%2C+limitaci%C3%B3n+de+velocidad+y+nuevos+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fworkers-production-safety%2F)[](https://www.threads.net/intent/post?text=Nuevas+herramientas+para+la+seguridad+de+la+producci%C3%B3n%3A+implementaciones+graduales%2C+correlaciones+de+c%C3%B3digo+fuente%2C+limitaci%C3%B3n+de+velocidad+y+nuevos+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fworkers-production-safety%2F)

## Etiquetas relacionadas

[Cloudflare Workers](https://blog.cloudflare.com/es-es/tag/workers/)[Developer Week](https://blog.cloudflare.com/es-es/tag/developer-week/)[Observability](https://blog.cloudflare.com/es-es/tag/observability/)[Rate Limiting (ES)](https://blog.cloudflare.com/es-es/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/es-es/tag/sdk/)

Síguenos en redes sociales

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Jacob Bednarz](https://blog.cloudflare.com/es-es/author/jacob-bednarz/)

[](https://jacobbednarz.com)




## Suscríbete para recibir notificaciones de nuevas publicaciones

Correo electrónico

Nunca compartiremos tu dirección de correo electrónico.

Suscribirse

¡Gracias por suscribirte! Revisa tu bandeja de entrada para confirmar.
