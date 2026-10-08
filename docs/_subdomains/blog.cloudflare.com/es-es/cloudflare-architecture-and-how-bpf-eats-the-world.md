---
url: https://blog.cloudflare.com/es-es/cloudflare-architecture-and-how-bpf-eats-the-world/
title: Estructura de Cloudflare y c\u00f3mo el filtro de paquetes Berkeley (BPF) se come el mundo | Blog de Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:22.927638+00:00
---

# Estructura de Cloudflare y cómo el filtro de paquetes Berkeley (BPF) se come el mundo | Blog de Cloudflare

> Source: https://blog.cloudflare.com/es-es/cloudflare-architecture-and-how-bpf-eats-the-world/

[Blog](https://blog.cloudflare.com/es-es/)

[Anycast (ES)](https://blog.cloudflare.com/es-es/tag/anycast/)[Desarrolladores](https://blog.cloudflare.com/es-es/tag/developers/)[eBPF](https://blog.cloudflare.com/es-es/tag/ebpf/)+3Mostrar 3 etiquetas más

6 etiquetasMostrar 6 etiquetas

  * Etiquetas de la publicación
  * [Anycast (ES)](https://blog.cloudflare.com/es-es/tag/anycast/)[Desarrolladores](https://blog.cloudflare.com/es-es/tag/developers/)
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



[Linux](https://blog.cloudflare.com/es-es/tag/linux/)[Programming](https://blog.cloudflare.com/es-es/tag/programming/)[TCP](https://blog.cloudflare.com/es-es/tag/tcp/)

[Anycast (ES)](https://blog.cloudflare.com/es-es/tag/anycast/)[Desarrolladores](https://blog.cloudflare.com/es-es/tag/developers/)[eBPF](https://blog.cloudflare.com/es-es/tag/ebpf/)[Linux](https://blog.cloudflare.com/es-es/tag/linux/)[Programming](https://blog.cloudflare.com/es-es/tag/programming/)[TCP](https://blog.cloudflare.com/es-es/tag/tcp/)

18 de mayo de 2019

# Estructura de Cloudflare y cómo el filtro de paquetes Berkeley (BPF) se come el mundo

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/es-es/author/marek-majkowski/)

11 min de lectura

COPIAR URL

Esta publicación también está disponible en [English](https://blog.cloudflare.com/cloudflare-architecture-and-how-bpf-eats-the-world/), [Deutsch](https://blog.cloudflare.com/de-de/cloudflare-architecture-and-how-bpf-eats-the-world/), [Français](https://blog.cloudflare.com/fr-fr/cloudflare-architecture-and-how-bpf-eats-the-world/) y [简体中文](https://blog.cloudflare.com/zh-cn/cloudflare-architecture-and-how-bpf-eats-the-world/).

![Cloudflare architecture and how BPF eats the world](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4625EY4M7N1KRERTHTYMFT.jpg&w=950&h=512&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////8/Lr2cu3zrig3tHI8fDz9Pb96Ofs////8u/n1MSqyLCM282+8u/v9vb66Obn////8u7l0cCfxKp52sy29PDt+Pj56ebk////9/Pq1cWmx7GA3tG6+PXw/Pz87erm//////324NW908Oh5t7L/f34////8vLu////////7una4trF8O7h////////9/v6////////+fjw7+vg+frz/////////P///////////v748/Hp/P75/////////f//)

Recientemente, en [Netdev 0x13](https://www.netdevconf.org/0x13/schedule.html), la conferencia sobre Redes en Linux en Praga, di [una breve charla titulada “Linux en Cloudflare”](https://netdevconf.org/0x13/session.html?panel-industry-perspectives). La [charla](https://speakerdeck.com/majek04/linux-at-cloudflare) terminó siendo casi en su totalidad sobre el BPF. Parece que independientemente de la pregunta, el BPF es la respuesta.

Aquí presentamos una transcripción de una versión ligeramente adaptada de esa charla.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - 8PjjfZ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S032Z8BX2FVSVHN1SG1E.jpg&w=715&h=458&f=webp&fit=cover&position=center)

En Cloudflare, ejecutamos Linux en nuestros servidores. Operamos dos categorías de centros de datos: los centros de datos “básicos” grandes, donde procesamos registros, analizamos ataques y hacemos cálculos analíticos, y la flota de servidores “perimetrales”, que envían contenido de clientes desde 180 ubicaciones en todo el mundo.

En esta charla, nos concentraremos en los servidores “perimetrales”. Es aquí donde utilizamos las características más recientes de Linux, optimizamos el rendimiento y nos ocupamos en gran medida de la resiliencia del DoS.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - yMZ8oK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457DSJSJ59D0H3MJMH3XD1.png&w=715&h=458&f=webp&fit=cover&position=center)

Nuestro servicio perimetral es especial debido a nuestra configuración de red, estamos utilizando ampliamente el enrutamiento _anycast._ _Anycast_ significa que todos nuestros centros de datos anuncian la misma serie de direcciones IP.

Este diseño tiene enormes ventajas. En primer lugar, garantiza la velocidad óptima para los usuarios finales. Independientemente del lugar en que usted se encuentre, siempre llegará al centro de datos más cercano. Luego, _anycast_ nos ayuda a extender el tráfico de DoS. Durante los ataques, cada una de las ubicaciones recibe una pequeña fracción del tráfico total, lo que facilita la asimilación y el filtrado del tráfico no deseado.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - UmJ9T6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473V4QZBVPZJYMTAATAPT0.jpg&w=715&h=291&f=webp&fit=cover&position=center)

_Anycast_ nos permite mantener la uniformidad de la configuración de red en todos los centros de datos perimetrales. Aplicamos el mismo diseño en nuestros centros de datos: nuestra pila de software es uniforme en todos los servidores perimetrales. Todas las piezas de software se ejecutan en todos los servidores.

En principio, cada equipo puede gestionar cada tarea, y nosotros ejecutamos una cantidad de tareas diversas y exigentes. Tenemos una pila HTTP completa, el mágico Cloudflare Workers, dos series de servidores DNS - autorización y resolución, y muchas otras aplicaciones públicas como Spectrum y Warp.

Si bien en cada servidor se está ejecutando todo el software, las solicitudes suelen pasar por muchas máquinas en su trayecto hacia la pila. Por ejemplo, una máquina diferente puede gestionar una solicitud HTTP durante cada una de las 5 etapas del procesamiento.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - Nx55Rn](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW451J7QR62Z3DR15BGJ56NW.png&w=715&h=371&f=webp&fit=cover&position=center)

Permítanme guiarlos en las primeras etapas del procesamiento de paquetes entrantes:

(1) En primer lugar, los paquetes llegan a nuestro enrutador. El enrutador genera una multirruta de igual costo (ECMP) y reenvía los paquetes a nuestros servidores Linux. Utilizamos ECMP para distribuir cada IP de destino entre muchas máquinas, al menos 16. Esto se utiliza como una técnica rudimentaria de equilibrio de carga.

(2) En los servidores tomamos paquetes con eBPF de XDP. En XDP ejecutamos dos etapas. En primer lugar, ejecutamos mitigaciones de DoS volumétricas y eliminamos los paquetes que pertenecen a ataques muy grandes de la capa 3.

(3) Luego, aún en XDP, llevamos a cabo el equilibrio de carga de la capa 4. Todos los paquetes que no son de ataque se redirigen a través de los equipos. Esto se utiliza para solucionar los problemas de ECMP, nos da un equilibrio de carga de granularidad fina y nos permite sacar correctamente de servicio a los servidores.

(4) Después de la redirección, los paquetes llegan a un equipo designado. En este punto, la pila de redes de Linux normal los toma, pasan por el firewall de iptables habitual y se envían a un socket de red adecuado.

(5) Por último, una aplicación recibe los paquetes. Por ejemplo, las conexiones HTTP son manejadas por un servidor de “protocolo” encargado del cifrado TLS y el procesamiento de los protocolos HTTP, HTTP/2 y QUIC.

Es en estas primeras fases de procesamiento de solicitudes donde utilizamos las características nuevas más interesantes de Linux. Podemos agrupar las funciones modernas útiles en tres categorías:

  * Control de DoS
  * Equilibrio de carga
  * Envío de sockets



* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - LhKOKN](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45XXKSKV58CVZ3KRAQ9HS5.png&w=715&h=255&f=webp&fit=cover&position=center)

Analicemos el control de DoS en más detalle. Como se mencionó anteriormente, el primer paso después del enrutamiento ECMP es la pila XDP de Linux donde, entre otras cosas, ejecutamos mitigaciones de DoS.

Históricamente, nuestras mitigaciones de ataques volumétricos se expresaban en la gramática clásica de estilo de iptables y BPF. Recientemente, hicimos una adaptación para ejecutar en el contexto de eBPF de XDP, lo que resultó ser increíblemente difícil. Siga leyendo sobre nuestras experiencias:

  * [L4Drop: Mitigaciones de DDoS XDP](https://blog.cloudflare.com/l4drop-xdp-ebpf-based-ddos-mitigations/)
  * [xdpcap: Captura de paquetes XDP](https://blog.cloudflare.com/xdpcap/)
  * Charla de [mitigación de DoS en función de XDP](https://netdevconf.org/0x13/session.html?talk-XDP-based-DDoS-mitigation) de Arthur Fabre
  * [XDP en la práctica: integración de XDP en nuestra canalización de mitigación de DDoS](https://netdevconf.org/2.1/papers/Gilberto_Bertin_XDP_in_practice.pdf)(PDF)



Durante este proyecto nos encontramos con una serie de limitaciones de eBPF/XDP. Una de ellas fue la falta de primitivas de concurrencia. Resultó muy difícil implementar cosas como algoritmos _token buckets_ sin competencia. Más tarde, descubrimos que la [ingeniera de Facebook Julia Kartseva](http://vger.kernel.org/lpc-bpf2018.html#session-9) tenía los mismos problemas. En febrero, este problema se solucionó con la introducción de la aplicación auxiliar bpf_spin_lock.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - WuSEbO](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW457FM8E07AEFEMGNVWSCNK.png&w=715&h=251&f=webp&fit=cover&position=center)

Si bien nuestros modernos sistemas de defensa de ataques DoS volumétricos se hacen en la capa XDP, aún contamos con iptables para aplicar las mitigaciones de la capa 7. Aquí, resultan útiles las características de un firewall de nivel superior: connlimit, hashlimits e ipsets. También utilizamos el módulo de iptables xt_bpf para ejecutar cBPF en iptables que coincidan con las cargas útiles del paquete. Ya hablamos de esto antes:

  * [Lecciones de defensa de lo indefendible](https://speakerdeck.com/majek04/lessons-from-defending-the-indefensible) (PPT)
  * [Presentación de herramientas del BPF](https://blog.cloudflare.com/introducing-the-bpf-tools/)



* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - mLDecw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48SS2ZE7FC30R5AKRSDFV9.png&w=715&h=370&f=webp&fit=cover&position=center)

Después de XDP e iptables, tenemos una última capa de defensa DoS del lado del núcleo.

Considere una situación en la que fallan nuestras mitigaciones del protocolo de datagramas de usuarios (UDP). En tal caso, podríamos recibir una avalancha de paquetes que llegan a al socket de UDP de nuestra aplicación. Esto podría desbordar el socket y generar la pérdida de paquetes. Esto es un problema, ya que se eliminarán indiscriminadamente tanto los paquetes buenos como los malos. Para aplicaciones como DNS esto resulta catastrófico. En el pasado, para reducir el daño ejecutamos un socket de UDP por dirección IP. Una inundación sin mitigar era algo malo, pero al menos no afectaba el tráfico a otras direcciones IP del servidor.

En la actualidad, esa estructura ya no resulta adecuada. Estamos ejecutando más de 30 000 IP DNS, y la ejecución de esa cantidad de sockets UDP no es una situación óptima. Nuestra solución actual es la ejecución de un único socket UDP con un filtro de socket eBPF complejo - utilizando la opción de socket SO_ATTACH_BPF. En publicaciones anteriores, hablamos sobre la ejecución de eBPF en sockets de red:

  * [eBPF, sockets, distancia de salto y escritura manual de ensamblado de eBPF](https://blog.cloudflare.com/epbf_sockets_hop_distance/)
  * [SOCKMAP - Empalme de TCP del futuro](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/)



El tipo de eBPF mencionado limita los paquetes. Mantiene el estado - recuento de paquetes - en un mapa de eBPF. Estamos seguros de que una sola IP inundada no afectará al resto del tráfico. Esto funciona bien, sin embargo, mientras trabajábamos en este proyecto encontramos un error bastante preocupante en el verificador de eBPF:

  * [¡¿eBPF no puede contar?!](https://blog.cloudflare.com/ebpf-cant-count/)



Supongo que ejecutar eBPF en un socket UDP no es una tarea común.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - qUqTiR](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48N4A8AJ8A882QX9ZJW00H.png&w=715&h=224&f=webp&fit=cover&position=center)

Aparte del DoS, en XDP también ejecutamos un equilibrador de carga de capa 4. Este es un proyecto nuevo, y aún no hemos hablado mucho de este. Sin entrar en tantos detalles: en ciertas ocasiones, necesitamos hacer una búsqueda de socket desde XDP.

El problema es relativamente simple - nuestro código necesita buscar la estructura del núcleo del “socket” para una tupla-5 extraída de un paquete. Por lo general, esto es fácil - hay una asistencia bpf_sk_lookup disponible para esto. Como era de esperar, hubo algunas complicaciones. Un problema fue la incapacidad de verificar si un paquete ACK recibido era una parte válida del protocolo de enlace de tres vías cuando se activan las cookies SYN. Mi colega Lorenz Bauer está trabajando para lograr más apoyo para este caso fuera de lo habitual.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - Z5AQj3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AZSQVK6GMC8GCG3QWTPE.png&w=715&h=232&f=webp&fit=cover&position=center)

Después de la denegación de servicio (DoS) y las capas de equilibrio de carga, los paquetes pasan a la pila de TCP / UDP de Linux habitual. Aquí hacemos un envío de socket - por ejemplo, los paquetes que van al puerto 53 pasan a un socket que pertenece a nuestro servidor DNS.

Hacemos todo lo posible por utilizar características estándar de Linux, pero las cosas se vuelven complejas cuando se usan miles de direcciones IP en los servidores.

Convencer a Linux para enrutar paquetes correctamente es bastante fácil con [el truco “AnyIP](https://blog.cloudflare.com/how-we-built-spectrum). Verificar que los paquetes se envían a la aplicación correcta es otra cuestión. Lamentablemente, la lógica de envío de sockets Linux estándar no es lo suficientemente flexible para nuestras necesidades. Para puertos populares como TCP/80 queremos compartir el puerto entre varias aplicaciones, cada una de las cuales lo maneja en un rango de IP diferente. Linux no es compatible de manera directa. Usted puede llamar enlazar() a una dirección IP específica o a todas las IP (con 0.0.0.0).

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - UyelYs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW454X48JSVW3F7W532P8XA0.png&w=715&h=260&f=webp&fit=cover&position=center)

Para solucionar este inconveniente, desarrollamos un parche de núcleo personalizado que agrega [una opción de socket SO_BINDTOPREFIX](http://patchwork.ozlabs.org/patch/602916/). Como su nombre lo indica, nos permite llamar enlazar() un prefijo de IP seleccionado. Esto resuelve el problema de aplicaciones múltiples que comparten puertos populares como 53 u 80.

Luego nos encontramos con otro problema. Para nuestro producto Spectrum, necesitamos escuchar en los 65535 puertos. Ejecutar tantos sockets de escucha no es una buena idea (ver [nuestro viejo blog con historias de guerras](https://blog.cloudflare.com/revenge-listening-sockets/)), por lo tanto, tuvimos que encontrar otra manera. Después de algunos experimentos, aprendimos a utilizar un módulo de iptables no muy conocido - TPROXY - para este propósito. Leer sobre este aquí:

  * [Abuso del _firewall_ de Linux: el _hack_ que nos permitió crear Spectrum](https://blog.cloudflare.com/how-we-built-spectrum/)



Esta configuración está funcionando, pero no nos gustan las reglas de firewall adicionales. Estamos trabajando para resolver correctamente este problema, en realidad estamos ampliando la lógica de envío de socket. Adivinó, queremos extender la lógica de envío de socket mediante la utilización de eBPF. Estamos desarrollando algunos parches.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - ii0Zd0](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KF3RTD2RE4TT91W3GYVE.png&w=715&h=370&f=webp&fit=cover&position=center)

Luego, hay una manera de utilizar eBPF para optimizar las aplicaciones. Recientemente, nos interesamos en el empalme de TCP con SOCKMAP:

  * [SOCKMAP - Empalme de TCP del futuro](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/)



Esta técnica ofrece un gran potencial para mejorar la latencia de cola en muchas piezas de nuestra pila de software. La implementación de SOCKMAP actual aún no está lista para el horario de mayor tráfico, pero el potencial es enorme.

Del mismo modo, los nuevos enlaces [TCP-BPF también conocidos como BPF_SOCK_OPS](https://netdevconf.org/2.2/papers/brakmo-tcpbpf-talk.pdf) ofrecen una excelente manera de inspeccionar los parámetros de rendimiento de los flujos de TCP. Esta funcionalidad resulta muy útil para nuestro equipo de rendimiento.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - uXroGK](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FV0YJYWWZR3691CB3DMV.jpg&w=715&h=458&f=webp&fit=cover&position=center)

Algunas características de Linux no soportaron bien el paso del tiempo y tenemos que trabajar en esto. Por ejemplo, estamos llegando a los límites de las métricas de red. No quiero que me malinterprete: las métricas de red son increíbles, pero lamentablemente no tienen la granularidad suficiente. Cosas como TcpExtListenDrops y TcpExtListenOverflows se informan como contadores globales, y nosotros necesitamos la información de cada aplicación.

Nuestra solución es utilizar un sondeo de eBPF para extraer los números directamente del núcleo. Mi colega Ivan Babrou desarrolló un exportador de métricas Prometheus que se llama “ebpf_exporter” para facilitar esto. Seguir leyendo:

  * [Presentación de ebpf_exporter](https://blog.cloudflare.com/introducing-ebpf_exporter/)
  * <https://github.com/cloudflare/ebpf_exporter>



Con “ebpf_exporter”, podemos generar todo tipo de métricas detalladas. Es muy potente y nos salvó en muchas ocasiones.

* * *

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare architecture and how BPF eats the world Embedded Image - iWWQYL](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TQR7YWXSSVZCMA3HPKBA.png&w=715&h=280&f=webp&fit=cover&position=center)

En esta charla analizamos las 6 capas del BPF que se ejecutan en nuestros servidores perimetrales:

  * Las mitigaciones de DoS volumétricas se ejecutan en eBPF de XDP
  * Iptables xt_bpf cBPF para ataques de capas de aplicaciones
  * SO_ATTACH_BPF para límites de velocidad en sockets UDP
  * Equilibrador de carga, que se ejecuta en XDP
  * Auxiliares de aplicaciones que se ejecutan en eBPF como SOCKMAP para el empalme de socket TCP y TCP-BPF para mediciones de TCP
  * “ebpf_exporter” para métricas granulares



¡Y eso es solo el comienzo! Pronto haremos más con el envío de socket basado en eBPF, eBPF que se ejecuta en la capa [Linux TC (Control de tráfico)](https://linux.die.net/man/8/tc) y más integración con enlaces eBPF para cgroup. Además, nuestro equipo de ingeniería de confiabilidad del sitio (SRE) lleva una lista cada vez más extensa de [scripts BCC](https://github.com/iovisor/bcc)qué resulta útil para la depuración.

Parece que Linux dejó de desarrollar nuevas API y todas las características nuevas se implementan como auxiliares y enlaces eBPF. Esto está bien y presenta muchas ventajas. Es más fácil y seguro actualizar el programa de eBPF que tener que volver a compilar un módulo del núcleo. Algunas cosas como TCP-BPF, que exponen un gran volumen de datos de seguimiento del rendimiento, probablemente serían imposibles sin eBPF.

Algunos afirman que “el software se está comiendo el mundo”, yo diría que: “el BPF se está comiendo el software”.

En esta página

Debatir en línea

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F&t=Estructura%20de%20Cloudflare%20y%20c%C3%B3mo%20el%20filtro%20de%20paquetes%20Berkeley%20%28BPF%29%20se%20come%20el%20mundo)[](https://x.com/intent/post?text=Estructura+de+Cloudflare+y+c%C3%B3mo+el+filtro+de+paquetes+Berkeley+%28BPF%29+se+come+el+mundo&url=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://bsky.app/intent/compose?text=Estructura+de+Cloudflare+y+c%C3%B3mo+el+filtro+de+paquetes+Berkeley+%28BPF%29+se+come+el+mundo+https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://mastodonshare.com/?text=Estructura+de+Cloudflare+y+c%C3%B3mo+el+filtro+de+paquetes+Berkeley+%28BPF%29+se+come+el+mundo&url=https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)[](https://www.threads.net/intent/post?text=Estructura+de+Cloudflare+y+c%C3%B3mo+el+filtro+de+paquetes+Berkeley+%28BPF%29+se+come+el+mundo+https%3A%2F%2Fblog.cloudflare.com%2Fes-es%2Fcloudflare-architecture-and-how-bpf-eats-the-world%2F)

## Etiquetas relacionadas

[Anycast (ES)](https://blog.cloudflare.com/es-es/tag/anycast/)[Desarrolladores](https://blog.cloudflare.com/es-es/tag/developers/)[eBPF](https://blog.cloudflare.com/es-es/tag/ebpf/)[Linux](https://blog.cloudflare.com/es-es/tag/linux/)[Programming](https://blog.cloudflare.com/es-es/tag/programming/)[TCP](https://blog.cloudflare.com/es-es/tag/tcp/)

Síguenos en redes sociales

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## Suscríbete para recibir notificaciones de nuevas publicaciones

Correo electrónico

Nunca compartiremos tu dirección de correo electrónico.

Suscribirse

¡Gracias por suscribirte! Revisa tu bandeja de entrada para confirmar.
