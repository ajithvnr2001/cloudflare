---
url: https://blog.cloudflare.com/ko-kr/workflow-diagrams/
title: Cloudflare\uc5d0\uc11c \ucd94\uc0c1 \uad6c\ubb38 \ud2b8\ub9ac(AST)\ub97c \uc0ac\uc6a9\ud558\uc5ec Workflows \ucf54\ub4dc\ub97c \uc2dc\uac01\uc801 \ub2e4\uc774\uc5b4\uadf8\ub7a8\uc73c\ub85c \ubcc0\ud658\ud558\ub294 \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:35:38.719328+00:00
---

# Cloudflare에서 추상 구문 트리(AST)를 사용하여 Workflows 코드를 시각적 다이어그램으로 변환하는 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/workflow-diagrams/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Workflows](https://blog.cloudflare.com/ko-kr/tag/workflows/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)

3개 태그3개 태그 보기

  * 게시물 태그
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Workflows](https://blog.cloudflare.com/ko-kr/tag/workflows/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)
  * 모든 태그
  * 일치하는 태그
  * 일치하는 태그가 없습니다
  * [1.1.1.1](https://blog.cloudflare.com/ko-kr/tag/1-1-1-1/)
  * [Access](https://blog.cloudflare.com/ko-kr/tag/access/)
  * [접근성](https://blog.cloudflare.com/ko-kr/tag/accessibility/)
  * [인수](https://blog.cloudflare.com/ko-kr/tag/acquisitions/)
  * [주소 지정](https://blog.cloudflare.com/ko-kr/tag/addressing/)
  * [첨단 DDoS](https://blog.cloudflare.com/ko-kr/tag/advanced-ddos/)
  * [Aegis](https://blog.cloudflare.com/ko-kr/tag/aegis/)
  * [에이전트 준비도](https://blog.cloudflare.com/ko-kr/tag/agent-readiness/)
  * [에이전트](https://blog.cloudflare.com/ko-kr/tag/agents/)
  * [Agents Week](https://blog.cloudflare.com/ko-kr/tag/agents-week/)
  * [AI](https://blog.cloudflare.com/ko-kr/tag/ai/)
  * [AI 봇](https://blog.cloudflare.com/ko-kr/tag/ai-bots/)
  * [AI Gateway](https://blog.cloudflare.com/ko-kr/tag/ai-gateway/)
  * [AI 검색](https://blog.cloudflare.com/ko-kr/tag/ai-search/)
  * [AI Week](https://blog.cloudflare.com/ko-kr/tag/ai-week/)
  * [AI-SPM](https://blog.cloudflare.com/ko-kr/tag/ai-spm/)
  * [AMD](https://blog.cloudflare.com/ko-kr/tag/amd/)
  * [Analytics](https://blog.cloudflare.com/ko-kr/tag/analytics/)
  * [Anonymous (KO)](https://blog.cloudflare.com/ko-kr/tag/anonymous/)
  * [Anycast (KO)](https://blog.cloudflare.com/ko-kr/tag/anycast/)
  * [API](https://blog.cloudflare.com/ko-kr/tag/api/)
  * [API Gateway (KO)](https://blog.cloudflare.com/ko-kr/tag/api-gateway/)
  * [API 보안](https://blog.cloudflare.com/ko-kr/tag/api-security/)
  * [응용 프로그램 보안](https://blog.cloudflare.com/ko-kr/tag/application-security/)
  * [애플리케이션 서비스](https://blog.cloudflare.com/ko-kr/tag/application-services/)
  * [공격](https://blog.cloudflare.com/ko-kr/tag/attacks/)
  * [감사 로그](https://blog.cloudflare.com/ko-kr/tag/audit-logs/)
  * [자동화](https://blog.cloudflare.com/ko-kr/tag/automation/)
  * [AWS](https://blog.cloudflare.com/ko-kr/tag/aws/)
  * [Beta (KO)](https://blog.cloudflare.com/ko-kr/tag/beta/)
  * [더 나은 인터넷](https://blog.cloudflare.com/ko-kr/tag/better-internet/)
  * [BGP](https://blog.cloudflare.com/ko-kr/tag/bgp/)
  * [창립기념일 주간](https://blog.cloudflare.com/ko-kr/tag/birthday-week/)
  * [Black Friday (KO)](https://blog.cloudflare.com/ko-kr/tag/black-friday/)
  * [봇 관리](https://blog.cloudflare.com/ko-kr/tag/bot-management/)
  * [Botnet (KO)](https://blog.cloudflare.com/ko-kr/tag/botnet/)
  * [봇](https://blog.cloudflare.com/ko-kr/tag/bots/)
  * [BPF](https://blog.cloudflare.com/ko-kr/tag/bpf/)
  * [브라우저 렌더링](https://blog.cloudflare.com/ko-kr/tag/browser-rendering/)
  * [Browser Run](https://blog.cloudflare.com/ko-kr/tag/browser-run/)
  * [Bug Bounty (KO)](https://blog.cloudflare.com/ko-kr/tag/bug-bounty/)
  * [BYOIP](https://blog.cloudflare.com/ko-kr/tag/byoip/)
  * [캐시](https://blog.cloudflare.com/ko-kr/tag/cache/)
  * [캐시 제거](https://blog.cloudflare.com/ko-kr/tag/cache-purge/)
  * [Cache Reserve (KO)](https://blog.cloudflare.com/ko-kr/tag/cache-reserve/)
  * [Cache Rules (KO)](https://blog.cloudflare.com/ko-kr/tag/cache-rules/)
  * [CASB](https://blog.cloudflare.com/ko-kr/tag/casb/)
  * [CDN](https://blog.cloudflare.com/ko-kr/tag/cdn/)
  * [Certificate Authority (KO)](https://blog.cloudflare.com/ko-kr/tag/certificate-authority/)
  * [인증](https://blog.cloudflare.com/ko-kr/tag/certification/)
  * [인증 질문 페이지](https://blog.cloudflare.com/ko-kr/tag/challenge-page/)
  * [China (KO)](https://blog.cloudflare.com/ko-kr/tag/china/)
  * [Chrome](https://blog.cloudflare.com/ko-kr/tag/chrome/)
  * [CIO Week](https://blog.cloudflare.com/ko-kr/tag/cio-week/)
  * [CISA (KO)](https://blog.cloudflare.com/ko-kr/tag/cisa/)
  * [ClickHouse](https://blog.cloudflare.com/ko-kr/tag/clickhouse/)
  * [클라이언트리스](https://blog.cloudflare.com/ko-kr/tag/clientless/)
  * [Cloud Email Security](https://blog.cloudflare.com/ko-kr/tag/cloud-email-security/)
  * [Cloudflare Access](https://blog.cloudflare.com/ko-kr/tag/cloudflare-access/)
  * [Cloudflare Calls](https://blog.cloudflare.com/ko-kr/tag/cloudflare-calls/)
  * [스타트업을 위한 Cloudflare](https://blog.cloudflare.com/ko-kr/tag/cloudflare-for-startups/)
  * [Cloudflare Gateway](https://blog.cloudflare.com/ko-kr/tag/gateway/)
  * [Cloudflare History (KO)](https://blog.cloudflare.com/ko-kr/tag/cloudflare-history/)
  * [Cloudflare Images](https://blog.cloudflare.com/ko-kr/tag/cloudflare-images/)
  * [Cloudflare 미디어 플랫폼](https://blog.cloudflare.com/ko-kr/tag/cloudflare-media-platform/)
  * [Cloudflare One](https://blog.cloudflare.com/ko-kr/tag/cloudflare-one/)
  * [Cloudflare 페이지](https://blog.cloudflare.com/ko-kr/tag/cloudflare-pages/)
  * [Cloudflare Queues](https://blog.cloudflare.com/ko-kr/tag/cloudflare-queues/)
  * [Cloudflare Stream](https://blog.cloudflare.com/ko-kr/tag/cloudflare-stream/)
  * [Cloudflare Tunnel](https://blog.cloudflare.com/ko-kr/tag/cloudflare-tunnel/)
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/ko-kr/tag/cloudflare-zero-trust/)
  * [Cloudforce One](https://blog.cloudflare.com/ko-kr/tag/cloudforce-one/)
  * [코드 오렌지](https://blog.cloudflare.com/ko-kr/tag/code-orange/)
  * [규정 준수](https://blog.cloudflare.com/ko-kr/tag/compliance/)
  * [압축](https://blog.cloudflare.com/ko-kr/tag/compression/)
  * [구성 관리](https://blog.cloudflare.com/ko-kr/tag/configuration-management/)
  * [정체 제어](https://blog.cloudflare.com/ko-kr/tag/congestion-control/)
  * [클라우드 연결성](https://blog.cloudflare.com/ko-kr/tag/connectivity-cloud/)
  * [소비자 서비스](https://blog.cloudflare.com/ko-kr/tag/consumer-services/)
  * [컨테이너](https://blog.cloudflare.com/ko-kr/tag/containers/)
  * [콘텐츠 독립기념일](https://blog.cloudflare.com/ko-kr/tag/content-independence-day/)
  * [컨텍스트](https://blog.cloudflare.com/ko-kr/tag/context/)
  * [코어](https://blog.cloudflare.com/ko-kr/tag/core/)
  * [크롤러 힌트](https://blog.cloudflare.com/ko-kr/tag/crawler-hints/)
  * [CrowdStrike (KO)](https://blog.cloudflare.com/ko-kr/tag/crowdstrike/)
  * [암호화](https://blog.cloudflare.com/ko-kr/tag/cryptography/)
  * [Customer Zero](https://blog.cloudflare.com/ko-kr/tag/customer-zero/)
  * [CVE-2023-50387 (KO)](https://blog.cloudflare.com/ko-kr/tag/cve-2023-50387/)
  * [D1](https://blog.cloudflare.com/ko-kr/tag/d1/)
  * [대시보드](https://blog.cloudflare.com/ko-kr/tag/dashboard-tag/)
  * [데이터](https://blog.cloudflare.com/ko-kr/tag/data/)
  * [데이터 플랫폼](https://blog.cloudflare.com/ko-kr/tag/data-platform/)
  * [데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)
  * [DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)
  * [DDoS 경보](https://blog.cloudflare.com/ko-kr/tag/ddos-alerts/)
  * [DDoS 보고서](https://blog.cloudflare.com/ko-kr/tag/ddos-reports/)
  * [디버깅](https://blog.cloudflare.com/ko-kr/tag/debugging/)
  * [자세히 보기](https://blog.cloudflare.com/ko-kr/tag/deep-dive/)
  * [설계](https://blog.cloudflare.com/ko-kr/tag/design/)
  * [개발자 설명서](https://blog.cloudflare.com/ko-kr/tag/developer-documentation/)
  * [개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)
  * [Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)
  * [개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)
  * [개발자 스토리지](https://blog.cloudflare.com/ko-kr/tag/developers-storage/)
  * [DevOps (KO)](https://blog.cloudflare.com/ko-kr/tag/devops/)
  * [Digital Experience Monitoring (KO)](https://blog.cloudflare.com/ko-kr/tag/digital-experience-monitoring/)
  * [디지털 포렌식](https://blog.cloudflare.com/ko-kr/tag/digital-forensics/)
  * [Diversity (KO)](https://blog.cloudflare.com/ko-kr/tag/diversity/)
  * [DLP](https://blog.cloudflare.com/ko-kr/tag/dlp/)
  * [DNS](https://blog.cloudflare.com/ko-kr/tag/dns/)
  * [DNS Flood (KO)](https://blog.cloudflare.com/ko-kr/tag/dns-flood/)
  * [DNSSEC](https://blog.cloudflare.com/ko-kr/tag/dnssec/)
  * [Dogfood](https://blog.cloudflare.com/ko-kr/tag/dogfooding/)
  * [Durable Execution](https://blog.cloudflare.com/ko-kr/tag/durable-execution/)
  * [Durable Objects](https://blog.cloudflare.com/ko-kr/tag/durable-objects/)
  * [EC2 (KO)](https://blog.cloudflare.com/ko-kr/tag/ec2/)
  * [Edge](https://blog.cloudflare.com/ko-kr/tag/edge/)
  * [에지 컴퓨팅](https://blog.cloudflare.com/ko-kr/tag/edge-computing/)
  * [송신](https://blog.cloudflare.com/ko-kr/tag/egress/)
  * [Elastic (KO)](https://blog.cloudflare.com/ko-kr/tag/elastic/)
  * [이메일](https://blog.cloudflare.com/ko-kr/tag/email/)
  * [Email Routing (KO)](https://blog.cloudflare.com/ko-kr/tag/email-routing/)
  * [이메일 보안](https://blog.cloudflare.com/ko-kr/tag/email-security/)
  * [Emissions](https://blog.cloudflare.com/ko-kr/tag/emissions/)
  * [Encrypted SNI (KO)](https://blog.cloudflare.com/ko-kr/tag/encrypted-sni/)
  * [엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)
  * [기업](https://blog.cloudflare.com/ko-kr/tag/enterprise/)
  * [Fast Fonts (KO)](https://blog.cloudflare.com/ko-kr/tag/fast-fonts/)
  * [기능 플래그](https://blog.cloudflare.com/ko-kr/tag/feature-flags/)
  * [방화벽](https://blog.cloudflare.com/ko-kr/tag/firewall/)
  * [Forrester](https://blog.cloudflare.com/ko-kr/tag/forrester/)
  * [Foundation DNS (KO)](https://blog.cloudflare.com/ko-kr/tag/foundation-dns/)
  * [창립자 서한](https://blog.cloudflare.com/ko-kr/tag/founders-letter/)
  * [사기](https://blog.cloudflare.com/ko-kr/tag/fraud/)
  * [프런트 엔드](https://blog.cloudflare.com/ko-kr/tag/front-end/)
  * [전체 스택](https://blog.cloudflare.com/ko-kr/tag/full-stack/)
  * [Gartner (KO)](https://blog.cloudflare.com/ko-kr/tag/gartner/)
  * [Gatebot (KO)](https://blog.cloudflare.com/ko-kr/tag/gatebot/)
  * [일반 가용성](https://blog.cloudflare.com/ko-kr/tag/general-availability/)
  * [생성형 AI](https://blog.cloudflare.com/ko-kr/tag/generative-ai/)
  * [GitHub](https://blog.cloudflare.com/ko-kr/tag/github/)
  * [Google](https://blog.cloudflare.com/ko-kr/tag/google/)
  * [Google Cloud](https://blog.cloudflare.com/ko-kr/tag/google-cloud/)
  * [하드웨어](https://blog.cloudflare.com/ko-kr/tag/hardware/)
  * [HTTP2 (KO)](https://blog.cloudflare.com/ko-kr/tag/http2/)
  * [HTTP3](https://blog.cloudflare.com/ko-kr/tag/http3/)
  * [하이브리드 클라우드](https://blog.cloudflare.com/ko-kr/tag/hybrid-cloud/)
  * [Hyperdrive](https://blog.cloudflare.com/ko-kr/tag/hyperdrive/)
  * [ID](https://blog.cloudflare.com/ko-kr/tag/identity/)
  * [IETF](https://blog.cloudflare.com/ko-kr/tag/ietf/)
  * [이미지 최적화](https://blog.cloudflare.com/ko-kr/tag/image-optimization/)
  * [이미지 크기 조정](https://blog.cloudflare.com/ko-kr/tag/image-resizing/)
  * [영향](https://blog.cloudflare.com/ko-kr/tag/impact/)
  * [사고 대응](https://blog.cloudflare.com/ko-kr/tag/incident-response/)
  * [인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)
  * [코드형 인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure-as-code/)
  * [인사이트](https://blog.cloudflare.com/ko-kr/tag/insights/)
  * [Intel](https://blog.cloudflare.com/ko-kr/tag/intel/)
  * [Interconnection](https://blog.cloudflare.com/ko-kr/tag/interconnection/)
  * [Internet Performance (KO)](https://blog.cloudflare.com/ko-kr/tag/internet-performance/)
  * [인터넷 품질](https://blog.cloudflare.com/ko-kr/tag/internet-quality/)
  * [인터넷 셧다운](https://blog.cloudflare.com/ko-kr/tag/internet-shutdown/)
  * [인터넷 트래픽](https://blog.cloudflare.com/ko-kr/tag/internet-traffic/)
  * [인터넷 동향](https://blog.cloudflare.com/ko-kr/tag/internet-trends/)
  * [인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)
  * [IPv4](https://blog.cloudflare.com/ko-kr/tag/ipv4/)
  * [IPv6](https://blog.cloudflare.com/ko-kr/tag/ipv6/)
  * [IWD (KO)](https://blog.cloudflare.com/ko-kr/tag/iwd/)
  * [JavaScript](https://blog.cloudflare.com/ko-kr/tag/javascript/)
  * [Kafka](https://blog.cloudflare.com/ko-kr/tag/kafka/)
  * [KeyTrap](https://blog.cloudflare.com/ko-kr/tag/keytrap/)
  * [Killnet (KO)](https://blog.cloudflare.com/ko-kr/tag/killnet/)
  * [Korea (KO)](https://blog.cloudflare.com/ko-kr/tag/korea/)
  * [Kubernetes](https://blog.cloudflare.com/ko-kr/tag/kubernetes/)
  * [LangChain (KO)](https://blog.cloudflare.com/ko-kr/tag/langchain/)
  * [LavaRand (KO)](https://blog.cloudflare.com/ko-kr/tag/lavarand/)
  * [Cloudflare에서의 근무 환경](https://blog.cloudflare.com/ko-kr/tag/life-at-cloudflare/)
  * [Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)
  * [LLM](https://blog.cloudflare.com/ko-kr/tag/llm/)
  * [Log4J (KO)](https://blog.cloudflare.com/ko-kr/tag/log4j/)
  * [Log4Shell (KO)](https://blog.cloudflare.com/ko-kr/tag/log4shell/)
  * [로깅](https://blog.cloudflare.com/ko-kr/tag/logging/)
  * [로그](https://blog.cloudflare.com/ko-kr/tag/logs/)
  * [Magic Transit](https://blog.cloudflare.com/ko-kr/tag/magic-transit/)
  * [Magic WAN Connector (KO)](https://blog.cloudflare.com/ko-kr/tag/magic-wan-connector/)
  * [맬웨어](https://blog.cloudflare.com/ko-kr/tag/malware/)
  * [MCP](https://blog.cloudflare.com/ko-kr/tag/mcp/)
  * [Meris (KO)](https://blog.cloudflare.com/ko-kr/tag/meris/)
  * [마이크로 프런트엔드](https://blog.cloudflare.com/ko-kr/tag/micro-frontends/)
  * [Microsoft Azure](https://blog.cloudflare.com/ko-kr/tag/microsoft-azure/)
  * [Migration Hub (KO)](https://blog.cloudflare.com/ko-kr/tag/migration-hub/)
  * [Mirai](https://blog.cloudflare.com/ko-kr/tag/mirai/)
  * [MLops (KO)](https://blog.cloudflare.com/ko-kr/tag/mlops/)
  * [모델 컨텍스트 프로토콜,](https://blog.cloudflare.com/ko-kr/tag/model-context-protocol/)
  * [Multi-Cloud (KO)](https://blog.cloudflare.com/ko-kr/tag/multi-cloud/)
  * [MySQL](https://blog.cloudflare.com/ko-kr/tag/mysql/)
  * [네트워크](https://blog.cloudflare.com/ko-kr/tag/network/)
  * [Network Interconnect (KO)](https://blog.cloudflare.com/ko-kr/tag/network-interconnect/)
  * [네트워크 성능 업데이트](https://blog.cloudflare.com/ko-kr/tag/network-performance-update/)
  * [Network Protection (KO)](https://blog.cloudflare.com/ko-kr/tag/network-protection/)
  * [네트워크 서비스](https://blog.cloudflare.com/ko-kr/tag/network-services/)
  * [네트워킹](https://blog.cloudflare.com/ko-kr/tag/networking/)
  * [NGINX](https://blog.cloudflare.com/ko-kr/tag/nginx/)
  * [Node.js](https://blog.cloudflare.com/ko-kr/tag/node-js/)
  * [Notifications (KO)](https://blog.cloudflare.com/ko-kr/tag/notifications/)
  * [NSEC3 (KO)](https://blog.cloudflare.com/ko-kr/tag/nsec3/)
  * [OAuth](https://blog.cloudflare.com/ko-kr/tag/oauth/)
  * [Observability](https://blog.cloudflare.com/ko-kr/tag/observability/)
  * [Okta (KO)](https://blog.cloudflare.com/ko-kr/tag/okta/)
  * [오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)
  * [OpenTelemetry ](https://blog.cloudflare.com/ko-kr/tag/opentelemetry/)
  * [최적화](https://blog.cloudflare.com/ko-kr/tag/optimization/)
  * [중단](https://blog.cloudflare.com/ko-kr/tag/outage/)
  * [파트너](https://blog.cloudflare.com/ko-kr/tag/partners/)
  * [Peering (KO)](https://blog.cloudflare.com/ko-kr/tag/peering/)
  * [성능](https://blog.cloudflare.com/ko-kr/tag/performance/)
  * [피싱](https://blog.cloudflare.com/ko-kr/tag/phishing/)
  * [Pingora](https://blog.cloudflare.com/ko-kr/tag/pingora/)
  * [PlanetScale](https://blog.cloudflare.com/ko-kr/tag/planetscale/)
  * [플랫폼 엔지니어링](https://blog.cloudflare.com/ko-kr/tag/platform-engineering/)
  * [정책 및 법률](https://blog.cloudflare.com/ko-kr/tag/policy/)
  * [사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)
  * [포스트 퀀텀](https://blog.cloudflare.com/ko-kr/tag/post-quantum/)
  * [Postgres](https://blog.cloudflare.com/ko-kr/tag/postgres/)
  * [개인정보 보호](https://blog.cloudflare.com/ko-kr/tag/privacy/)
  * [사설 네트워크:](https://blog.cloudflare.com/ko-kr/tag/private-network/)
  * [제품 설계](https://blog.cloudflare.com/ko-kr/tag/product-design/)
  * [제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)
  * [Galileo 프로젝트](https://blog.cloudflare.com/ko-kr/tag/project-galileo/)
  * [Project Safekeeping (KO)](https://blog.cloudflare.com/ko-kr/tag/project-safekeeping/)
  * [Project Turpentine (KO)](https://blog.cloudflare.com/ko-kr/tag/project-turpentine/)
  * [Prometheus](https://blog.cloudflare.com/ko-kr/tag/prometheus/)
  * [프로토콜](https://blog.cloudflare.com/ko-kr/tag/protocols/)
  * [Python](https://blog.cloudflare.com/ko-kr/tag/python/)
  * [Queues](https://blog.cloudflare.com/ko-kr/tag/queues/)
  * [QUIC](https://blog.cloudflare.com/ko-kr/tag/quic/)
  * [QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)
  * [R2](https://blog.cloudflare.com/ko-kr/tag/r2/)
  * [R2 Super Slurper](https://blog.cloudflare.com/ko-kr/tag/r2-super-slurper/)
  * [Radar](https://blog.cloudflare.com/ko-kr/tag/cloudflare-radar/)
  * [Radar API (KO)](https://blog.cloudflare.com/ko-kr/tag/radar-api/)
  * [Randomness (KO)](https://blog.cloudflare.com/ko-kr/tag/randomness/)
  * [랜섬 공격](https://blog.cloudflare.com/ko-kr/tag/ransom-attacks/)
  * [Rapid Reset (KO)](https://blog.cloudflare.com/ko-kr/tag/rapid-reset/)
  * [Rate Limiting](https://blog.cloudflare.com/ko-kr/tag/rate-limiting/)
  * [RDDoS (KO)](https://blog.cloudflare.com/ko-kr/tag/rddos/)
  * [Reading List (KO)](https://blog.cloudflare.com/ko-kr/tag/reading-list/)
  * [실시간](https://blog.cloudflare.com/ko-kr/tag/real-time/)
  * [등록기관](https://blog.cloudflare.com/ko-kr/tag/registrar/)
  * [신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)
  * [연구](https://blog.cloudflare.com/ko-kr/tag/research/)
  * [Resolver (KO)](https://blog.cloudflare.com/ko-kr/tag/resolver/)
  * [리버스 엔지니어링](https://blog.cloudflare.com/ko-kr/tag/reverse-engineering/)
  * [위험 관리](https://blog.cloudflare.com/ko-kr/tag/risk-management/)
  * [라우팅](https://blog.cloudflare.com/ko-kr/tag/routing/)
  * [라우팅 보안](https://blog.cloudflare.com/ko-kr/tag/routing-security/)
  * [RPKI](https://blog.cloudflare.com/ko-kr/tag/rpki/)
  * [Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)
  * [Rust Workers](https://blog.cloudflare.com/ko-kr/tag/rust-workers/)
  * [SaaS 보안](https://blog.cloudflare.com/ko-kr/tag/saas-security/)
  * [Salt](https://blog.cloudflare.com/ko-kr/tag/salt/)
  * [샌드박스](https://blog.cloudflare.com/ko-kr/tag/sandbox/)
  * [SASE](https://blog.cloudflare.com/ko-kr/tag/sase/)
  * [SDK](https://blog.cloudflare.com/ko-kr/tag/sdk/)
  * [안전한 웹 게이트웨이](https://blog.cloudflare.com/ko-kr/tag/secure-web-gateway/)
  * [보안](https://blog.cloudflare.com/ko-kr/tag/security/)
  * [보안 센터](https://blog.cloudflare.com/ko-kr/tag/security-center/)
  * [보안 상태](https://blog.cloudflare.com/ko-kr/tag/security-posture/)
  * [보안 상태 관리](https://blog.cloudflare.com/ko-kr/tag/security-posture-management/)
  * [Security Service Edge (KO)](https://blog.cloudflare.com/ko-kr/tag/security-service-edge/)
  * [Security Week](https://blog.cloudflare.com/ko-kr/tag/security-week/)
  * [서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)
  * [서버](https://blog.cloudflare.com/ko-kr/tag/servers/)
  * [SIEM](https://blog.cloudflare.com/ko-kr/tag/siem/)
  * [Smart Shield](https://blog.cloudflare.com/ko-kr/tag/smart-shield/)
  * [Spectrum](https://blog.cloudflare.com/ko-kr/tag/spectrum/)
  * [속도](https://blog.cloudflare.com/ko-kr/tag/speed/)
  * [속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)
  * [SQL](https://blog.cloudflare.com/ko-kr/tag/sql/)
  * [SRE(Systems Reliability Engineer)](https://blog.cloudflare.com/ko-kr/tag/sre/)
  * [SSE (KO)](https://blog.cloudflare.com/ko-kr/tag/sse/)
  * [표준](https://blog.cloudflare.com/ko-kr/tag/standards/)
  * [스토리지](https://blog.cloudflare.com/ko-kr/tag/storage/)
  * [SYN Flood (KO)](https://blog.cloudflare.com/ko-kr/tag/syn-flood/)
  * [TCP](https://blog.cloudflare.com/ko-kr/tag/tcp/)
  * [팀](https://blog.cloudflare.com/ko-kr/tag/team/)
  * [Teams Dashboard (KO)](https://blog.cloudflare.com/ko-kr/tag/teams-dashboard/)
  * [Terraform](https://blog.cloudflare.com/ko-kr/tag/terraform/)
  * [위협 데이터](https://blog.cloudflare.com/ko-kr/tag/threat-data/)
  * [위협 인텔리전스](https://blog.cloudflare.com/ko-kr/tag/threat-intelligence/)
  * [위협 운영](https://blog.cloudflare.com/ko-kr/tag/threat-operations/)
  * [위협](https://blog.cloudflare.com/ko-kr/tag/threats/)
  * [TLS](https://blog.cloudflare.com/ko-kr/tag/tls/)
  * [추적](https://blog.cloudflare.com/ko-kr/tag/tracing/)
  * [트래픽](https://blog.cloudflare.com/ko-kr/tag/traffic/)
  * [투명성](https://blog.cloudflare.com/ko-kr/tag/transparency/)
  * [추세](https://blog.cloudflare.com/ko-kr/tag/trends/)
  * [TURN 서버](https://blog.cloudflare.com/ko-kr/tag/turn-server/)
  * [Turnstile](https://blog.cloudflare.com/ko-kr/tag/turnstile/)
  * [TypeScript](https://blog.cloudflare.com/ko-kr/tag/typescript/)
  * [사용자 연구](https://blog.cloudflare.com/ko-kr/tag/user-research/)
  * [Vectorize (KO)](https://blog.cloudflare.com/ko-kr/tag/vectorize/)
  * [VoiP (KO)](https://blog.cloudflare.com/ko-kr/tag/voip/)
  * [VPC](https://blog.cloudflare.com/ko-kr/tag/vpc/)
  * [VPN (KO)](https://blog.cloudflare.com/ko-kr/tag/vpn/)
  * [WAF](https://blog.cloudflare.com/ko-kr/tag/waf/)
  * [WARP](https://blog.cloudflare.com/ko-kr/tag/warp/)
  * [WARP Connector (KO)](https://blog.cloudflare.com/ko-kr/tag/warp-connector/)
  * [WASM](https://blog.cloudflare.com/ko-kr/tag/wasm/)
  * [웹 애플리케이션 방화벽](https://blog.cloudflare.com/ko-kr/tag/web-application-firewall/)
  * [WebAssembly](https://blog.cloudflare.com/ko-kr/tag/webassembly/)
  * [WebRTC](https://blog.cloudflare.com/ko-kr/tag/webrtc/)
  * [Workers AI](https://blog.cloudflare.com/ko-kr/tag/workers-ai/)
  * [Workers Launchpad](https://blog.cloudflare.com/ko-kr/tag/workers-launchpad/)
  * [Workers VPC](https://blog.cloudflare.com/ko-kr/tag/workers-vpc/)
  * [Workflows](https://blog.cloudflare.com/ko-kr/tag/workflows/)
  * [Wrangler](https://blog.cloudflare.com/ko-kr/tag/wrangler/)
  * [검토](https://blog.cloudflare.com/ko-kr/tag/year-in-review/)
  * [Z3](https://blog.cloudflare.com/ko-kr/tag/z3/)
  * [Zero Day Threats (KO)](https://blog.cloudflare.com/ko-kr/tag/zero-day-threats/)
  * [Zero Trust](https://blog.cloudflare.com/ko-kr/tag/zero-trust/)



[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Workflows](https://blog.cloudflare.com/ko-kr/tag/workflows/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)

2026년 3월 27일

# Cloudflare에서 추상 구문 트리(AST)를 사용하여 Workflows 코드를 시각적 다이어그램으로 변환하는 방법 

![André Venceslau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TZTSTWQ6JMKEC8GX38NE.png&w=64&h=64&f=webp&fit=cover&position=center)![Mia Malden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4559TC07A12MQHAEK8YM1R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[André Venceslau](https://blog.cloudflare.com/ko-kr/author/andre-venceslau/) 및 [Mia Malden](https://blog.cloudflare.com/ko-kr/author/mia/)

9분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/workflow-diagrams/) 및 [日本語](https://blog.cloudflare.com/ja-jp/workflow-diagrams/).

![BLOG-3163 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47AEP95R4WVM6YM3WW23XZ.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88O/y4+Xu4+jx6u/27/Hz7uzr////////6+712uLw2eX04+346/D27e3u////////6O/50uH00OP43e386fH67e7y////////6fL+0eT50Ob83/D/7PX+8PL2////////7/f/2+r+3O7/6/j/9fv/9vf7////////+f7/6fP/7fj/+v///////fz+////////////9vr//P//////////////////////////+/3/////////////////)

[_Cloudflare Workflows_](https://www.cloudflare.com/developer-platform/products/workflows/) 는 단계를 연결하고, 실패 시 재시도하며, 장기 실행 프로세스에서 상태를 유지할 수 있는 지속형 실행 엔진입니다. 개발자는 Workflows를 사용하여 백그라운드 에이전트를 구동하고, 데이터 파이프라인을 관리하며, 휴먼인더루프(human-in-the-loop) 승인 시스템을 구축하는 등의 작업을 수행할 수 있습니다.

지난 달, 저희는 Cloudflare에 배포된 모든 워크플로의 대시보드에 완전한 시각적 다이어그램이 표시된다고 [_발표했습니다_](https://developers.cloudflare.com/changelog/post/2026-02-03-workflows-visualizer/).

애플리케이션을 시각화할 수 있는 능력이 그 어느 때보다 중요한 지금 이러한 상황이 되었습니다. 코딩 에이전트는 사용자가 읽을 수도 있고 읽지 않을 수도 있는 코드를 작성합니다. 하지만 단계가 어떻게 연결되는지, 어디에서 분기되며, 실제로 어떤 일이 일어나고 있는지 구축하는 형태가 여전히 중요합니다.

이전에 비주얼 워크플로우 빌더의 다이어그램을 본 적이 있다면, 이들은 일반적으로 JSON 구성, YAML, 드래그 앤 드롭 등 선언적인 것으로 작동합니다. 하지만 Cloudflare Workflows는 코드에 불과합니다. 여기에는 [_Promises, Promise.all, 루프, 조건문_](https://developers.cloudflare.com/workflows/build/workers-api/) 이 포함되거나 함수 또는 클래스에 중첩될 수 있습니다. 이 동적 실행 모델 때문에 다이어그램 렌더링이 조금 더 복잡해집니다.

추상 구문 트리(AST)를 사용하여 그래프를 정적으로 도출하고, `Promise` 및 `await` 관계를 추적하여 무엇이 병렬로 실행되는지, 어떤 블록이 작동하는지, 조각들이 어떻게 연결되는지 이해합니다. 

계속 읽으면서 다이어그램을 구축한 방법을 알아보거나, 첫 워크플로우를 배포하고 다이어그램을 직접 확인하세요.

[![Cloudflare에 배포](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workflows-starter-template)

다음은 Cloudflare Workflows 코드에서 생성된 다이어그램의 예입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3163 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FCEK2SHE8ZKJ2DZXJ9SH.png&w=715&h=912&f=webp&fit=cover&position=center)

### 동적 워크플로우 실행

일반적으로 워크플로우 엔진은 동적 또는 순차적(정적) 실행 순서에 따라 실행될 수 있습니다. 순차적 실행이 더 직관적인 솔루션처럼 보일 수 있습니다. 워크플로 → A 단계 → B 단계 → 엔진이 A 단계를 완료한 후 즉시 B 단계의 실행이 시작되는 C 단계를 트리거합니다.

[_Cloudflare Workflows_](https://developers.cloudflare.com/workflows/) 는 동적 실행 모델을 따릅니다. 워크플로우는 코드이므로 런타임이 단계를 만나면 실행됩니다. 런타임에서 단계를 검색하면 해당 단계는 워크플로우 엔진으로 전달되며, 워크플로우 엔진에서는 실행을 관리합니다. await를 거치지 않는 한 단계는 본질적으로 순차적이지 않습니다. 엔진은 기다리지 않은 모든 단계를 병렬로 실행합니다. 이러한 방식으로 추가 래퍼나 지시문 없이 워크플로 코드를 흐름 제어로 작성할 수 있습니다. 핸드오프가 작동하는 방식은 다음과 같습니다.

  1. 해당 인스턴스의 "슈퍼바이저" Durable Object 역할을 하는 _엔진_ 이 작동합니다. 엔진은 실제 워크플로 실행 로직을 담당합니다. 
  2. 엔진은 [_사용자 Worker_](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers) 를 [_동적 디스패치_](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/)를 통해 트리거하여 Workers 런타임으로 제어권을 넘깁니다.
  3. 런타임이 `step.do`를 만나면, 실행을 엔진으로 다시 넘깁니다.
  4. 엔진이 단계를 실행하고, 결과를 유지한(또는 해당하는 경우 오류가 발생함), 사용자 Worker를 다시 트리거합니다. 



이 아키텍처에서는 엔진이 본질적으로 실행 중인 단계의 순서를 "알 수는 없지만" 다이어그램의 경우 단계 순서가 중요한 정보가 됩니다. 대부분의 워크플로를 진단에 유용한 그래프로 정확하게 변환하는 것이 과제입니다. 베타 버전의 다이어그램을 사용하여 이러한 표현을 계속 반복하고 개선할 예정입니다.

### 코드 구문 분석

런타임이 아니라 [_배포 시_](https://developers.cloudflare.com/workers/get-started/guide/#4-deploy-your-project) 스크립트를 가져오면 전체 워크플로우를 구문 분석하여 다이어그램을 정적으로 생성할 수 있습니다. 

한 걸음 물러서서, 워크플로우 배포의 수명은 다음과 같습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3163 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Z4PFGJR15RR2B45KXVTM.png&w=715&h=1033&f=webp&fit=cover&position=center)

다이어그램을 생성하기 위해 Workers를 배포하는 내부 구성 서비스에서 번들로 제공한 스크립트를 가져옵니다(Workflow 배포의 2단계). 그런 다음 파서를 사용하여 워크플로를 나타내는 추상 구문 트리(AST)를 생성하면 내부 서비스에서 모든 WorkflowEntrypoint와 워크플로 단계에 대한 호출이 있는 중간 그래프를 생성하고 순회합니다. Cloudflare에서는 API의 최종 결과에 따라 다이어그램을 렌더링합니다. 

Worker가 배포되면 [_달리_](https://developers.cloudflare.com/workers/wrangler/configuration/#inheritable-keys) 명시되지 않는 한 구성 서비스는 코드를 번들로 [_묶고(기본적으로 esbuild_](https://esbuild.github.io/) 사용) 최소화합니다. 이는 또 다른 문제를 야기합니다. TypeScript의 Workflows는 직관적인 패턴을 따르지만, 축소된 Javascript(JS)는 밀도가 높고 소화하기 어려울 수 있습니다. 번들러에 따라 코드를 최소화할 수 있는 다른 방법도 있습니다. 

다음은 **병렬로 실행되는 에이전트** 를 보여주는 Workflow 코드의 예입니다.
    
    
    const summaryPromise = step.do(
             `summary agent (loop ${loop})`,
             async () => {
               return runAgentPrompt(
                 this.env,
                 SUMMARY_SYSTEM,
                 buildReviewPrompt(
                   'Summarize this text in 5 bullet points.',
                   draft,
                   input.context
                 )
               );
             }
           );
            const correctnessPromise = step.do(
             `correctness agent (loop ${loop})`,
             async () => {
               return runAgentPrompt(
                 this.env,
                 CORRECTNESS_SYSTEM,
                 buildReviewPrompt(
                   'List correctness issues and suggested fixes.',
                   draft,
                   input.context
                 )
               );
             }
           );
            const clarityPromise = step.do(
             `clarity agent (loop ${loop})`,
             async () => {
               return runAgentPrompt(
                 this.env,
                 CLARITY_SYSTEM,
                 buildReviewPrompt(
                   'List clarity issues and suggested fixes.',
                   draft,
                   input.context
                 )
               );
             }
           );

[_rspack_](https://rspack.rs/)과 함께 번들링하면 축소된 코드의 일부는 다음과 같습니다.
    
    
    class pe extends e{async run(e,t){de("workflow.run.start",{instanceId:e.instanceId});const r=await t.do("validate payload",async()=>{if(!e.payload.r2Key)throw new Error("r2Key is required");if(!e.payload.telegramChatId)throw new Error("telegramChatId is required");return{r2Key:e.payload.r2Key,telegramChatId:e.payload.telegramChatId,context:e.payload.context?.trim()}}),s=await t.do("load source document from r2",async()=>{const e=await this.env.REVIEW_DOCUMENTS.get(r.r2Key);if(!e)throw new Error(`R2 object not found: ${r.r2Key}`);const t=(await e.text()).trim();if(!t)throw new Error("R2 object is empty");return t}),n=Number(this.env.MAX_REVIEW_LOOPS??"5"),o=this.env.RESPONSE_TIMEOUT??"7 days",a=async(s,i,c)=>{if(s>n)return le("workflow.loop.max_reached",{instanceId:e.instanceId,maxLoops:n}),await t.do("notify max loop reached",async()=>{await se(this.env,r.telegramChatId,`Review stopped after ${n} loops for ${e.instanceId}. Start again if you still need revisions.`)}),{approved:!1,loops:n,finalText:i};const h=t.do(`summary agent (loop ${s})`,async()=>te(this.env,"You summarize documents. Keep the output short, concrete, and factual.",ue("Summarize this text in 5 bullet points.",i,r.context)))...

또는, [_vite_](https://vite.dev/)와 함께 번들로 제공되는 최소화된 스니펫은 다음과 같습니다.
    
    
    class ht extends pe {
      async run(e, r) {
        b("workflow.run.start", { instanceId: e.instanceId });
        const s = await r.do("validate payload", async () => {
          if (!e.payload.r2Key)
            throw new Error("r2Key is required");
          if (!e.payload.telegramChatId)
            throw new Error("telegramChatId is required");
          return {
            r2Key: e.payload.r2Key,
            telegramChatId: e.payload.telegramChatId,
            context: e.payload.context?.trim()
          };
        }), n = await r.do(
          "load source document from r2",
          async () => {
            const i = await this.env.REVIEW_DOCUMENTS.get(s.r2Key);
            if (!i)
              throw new Error(`R2 object not found: ${s.r2Key}`);
            const c = (await i.text()).trim();
            if (!c)
              throw new Error("R2 object is empty");
            return c;
          }
        ), o = Number(this.env.MAX_REVIEW_LOOPS ?? "5"), l = this.env.RESPONSE_TIMEOUT ?? "7 days", a = async (i, c, u) => {
          if (i > o)
            return H("workflow.loop.max_reached", {
              instanceId: e.instanceId,
              maxLoops: o
            }), await r.do("notify max loop reached", async () => {
              await J(
                this.env,
                s.telegramChatId,
                `Review stopped after ${o} loops for ${e.instanceId}. Start again if you still need revisions.`
              );
            }), {
              approved: !1,
              loops: o,
              finalText: c
            };
          const h = r.do(
            `summary agent (loop ${i})`,
            async () => _(
              this.env,
              et,
              K(
                "Summarize this text in 5 bullet points.",
                c,
                s.context
              )
            )
          )...

축소된 코드는 상당히 복잡해질 수 있으며, 번들러에 따라 여러 방향으로 복잡해질 수 있습니다.

우리는 다양한 형태의 축소된 코드를 빠르고 정확하게 구문 분석할 방법이 필요했습니다. 저희는 `oxc-parser` 가 [_JavaScript Oxidation Compiler_](https://oxc.rs/) (OXC)에서 이 작업에 완벽하다고 판단했습니다. 저희는 Rust를 실행하는 컨테이너를 통해 이 아이디어를 먼저 테스트했습니다. 모든 스크립트 ID가 [_Cloudflare Queue_](https://developers.cloudflare.com/queues/)로 전송된 다음, 메시지가 팝업되어 처리할 컨테이너로 전송되었습니다. 이 접근 방식이 효과가 있음을 확인한 후, Cloudflare는 Rust로 작성된 Worker로 이전했습니다. Workers는 [_WebAssembly를 통한 Rust_](https://developers.cloudflare.com/workers/languages/rust/) 실행을 지원하며, 패키지는 이 과정이 간단할 만큼 작았습니다.

Rust Worker는 먼저 축소된 JS를 AST 노드 유형으로 변환한 다음, AST 노드 유형을 대시보드에 렌더링되는 그래픽 버전의 워크플로로 변환하는 일을 담당합니다. 이를 위해 각 워크플로우에 대해 미리 정의된 [_노드 유형_](https://developers.cloudflare.com/workflows/build/visualizer/) 의 그래프를 생성하고, 일련의 노드 매핑을 통해 그래프 표현으로 변환합니다. 

### 다이어그램 렌더링

워크플로의 다이어그램 버전을 렌더링하는 데는 두 가지 과제가 있었습니다. 단계와 기능 관계를 올바르게 추적하는 방법, 그리고 모든 표면 영역을 다루면서 워크플로 노드 유형을 최대한 간단하게 정의하는 방법이었습니다.

단계와 기능 관계를 올바르게 추적하려면 기능과 단계 이름을 모두 수집해야 했습니다. 앞서 설명한 것처럼 엔진에는 단계에 대한 정보만 있지만, 단계는 기능에 종속될 수 있으며, 그 반대의 경우도 마찬가지입니다. 예를 들어, 개발자는 함수로 단계를 래핑하거나 함수를 단계로 정의할 수 있습니다. 또한 다른 [_모듈_](https://blog.cloudflare.com/workers-javascript-modules/) 에서 온 함수 내에서 단계를 호출하거나 단계의 이름을 바꿀 수 있습니다. 

라이브러리는 AST를 제공하여 초기 장애물을 통과하지만, 우리는 여전히 라이브러리를 구문 분석하는 방법을 결정해야 합니다. 추가적인 창의성이 필요한 코드 패턴도 있습니다. 예를 들어 함수 — `WorkflowEntrypoint` 내에는 단계를 직접, 간접적으로 호출하거나, 호출하지 않는 함수가 있을 수 있습니다. 고려해 보겠습니다 `functionA`는 `console.log(await functionB(), await functionC()`)를 포함하며, 여기서 `functionB` 는 `step.do()`를 호출합니다. 이 경우 `functionA` 와 `functionB` 는 모두 워크플로우 다이어그램에 포함되어야 합니다. 하지만 `functionC` 는 포함되어서는 안 됩니다. 직접 및 간접 단계 호출이 포함된 모든 함수를 포착하기 위해 각 함수에 대한 하위 그래프를 만들고 여기에 단계 호출 자체가 포함되어 있는지 또는 그것이 있을 수 있는 다른 함수를 호출하는지 여부를 확인합니다. 이러한 하위 그래프는 모든 관련 노드를 포함하는 기능 노드로 표현됩니다. 함수 노드가 그래프의 리프이거나 직접 또는 간접적인 워크플로우 단계가 없는 경우에는 최종 출력에서 잘립니다. 

저희는 최대 10가지 방법으로 정의된 워크플로우 다이어그램 또는 변수를 추론할 수 있는 정적 단계 목록을 포함하여 다른 패턴도 확인합니다. 스크립트에 여러 워크플로우가 포함된 경우 저희는 한 수준 더 높은 수준에서 추상화된 함수에 대해 생성된 하위 그래프와 유사한 패턴을 따릅니다. 

모든 AST 노드 유형에 대해, 워크플로우 내에서 사용할 수 있는 모든 방법을 고려해야 했습니다. 루프, 분기, 프라미스, 병렬, 대기, 화살표 함수 등 목록의 계속입니다. 이러한 경로 안에도 수십 개의 가능성이 존재합니다. 루프를 실행하는 몇 가지 방법을 고려해보세요.
    
    
    // for...of
    for (const item of items) {
    	await step.do(`process ${item}`, async () => item);
    }
    // while
    while (shouldContinue) {
    	await step.do('poll', async () => getStatus());
    }
    // map
    await Promise.all(
    	items.map((item) => step.do(`map ${item}`, async () => item)),
    );
    // forEach
    await items.forEach(async (item) => {
    	await step.do(`each ${item}`, async () => item);
    });

루핑을 넘어서서 분기를 처리하는 방법은 다음과 같습니다.
    
    
    // switch / case
    switch (action.type) {
    	case 'create':
    		await step.do('handle create', async () => {});
    		break;
    	default:
    		await step.do('handle unknown', async () => {});
    		break;
    }
    
    // if / else if / else
    if (status === 'pending') {
    	await step.do('pending path', async () => {});
    } else if (status === 'active') {
    	await step.do('active path', async () => {});
    } else {
    	await step.do('fallback path', async () => {});
    }
    
    // ternary operator
    await (cond
    	? step.do('ternary true branch', async () => {})
    	: step.do('ternary false branch', async () => {}));
    
    // nullish coalescing with step on RHS
    const myStepResult =
    	variableThatCanBeNullUndefined ??
    	(await step.do('nullish fallback step', async () => 'default'));
    
    // try/catch with finally
    try {
    	await step.do('try step', async () => {});
    } catch (_e) {
    	await step.do('catch step', async () => {});
    } finally {
    	await step.do('finally step', async () => {});
    }

우리의 목표는 너무 복잡하지 않으면서 개발자가 알아야 할 것을 전달할 수 있는 간결한 API를 만드는 것이었습니다. 하지만 워크플로우를 다이어그램으로 변환하려면 가능한 모든 패턴(모범 사례 준수 여부 여부)과 에지 사례를 고려해야 했습니다. 앞서 설명한 것처럼 각 단계는 기본적으로 다른 단계로 명시적으로 순차적이지 않습니다. 워크플로가 `await` 및 `Promise.all()`을 활용하지 않으면, 단계가 발생한 순서대로 실행될 것으로 가정합니다. 하지만 워크플로에 `await`, `Promise` 또는 `Promise.all()`이 포함된 경우, 우리는 이러한 관계를 추적할 방법이 필요했습니다.

우리는 각 노드에 `starts:` 및 `resolves:` 필드가 있는 실행 순서를 추적하기로 결정했습니다. `starts` 및 `resolves` 인덱스는 프라미스가 실행을 시작한 시점과 즉각적인 후속 결론 없이 시작된 첫 번째 프라미스를 기준으로 종료되는 시점을 알려줍니다. 이는 다이어그램 UI에서의 수직적 위치 지정과 관련이 있습니다(즉, `starts:1` 인 모든 단계가 인라인입니다). 단계가 선언될 때 await가 사용되는 경우 `starts` 및 `resolves` 이 정의되지 않고 런타임에 단계가 표시된 순서대로 워크플로가 실행됩니다.

구문 분석을 하는 동안 기다리지 않은 `Promise` 또는 `Promise.all()을` 만나면 해당 노드에는 `starts` 필드에 나타난 엔트리 번호가 표시됩니다. 해당 프라미스에서 `await` 가 발생하면 엔트리 번호가 1씩 증가하고 종료 번호에 저장됩니다(`resolves`의 값입니다). 이렇게 하면 어떤 프라미스가 동시에 실행되고 언제 완료되는지 서로 연관하여 알 수 있습니다.
    
    
    export class ImplicitParallelWorkflow extends WorkflowEntrypoint<Env, Params> {
     async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
       const branchA = async () => {
         const a = step.do("task a", async () => "a"); //starts 1
         const b = step.do("task b", async () => "b"); //starts 1
         const c = await step.waitForEvent("task c", { type: "my-event", timeout: "1 hour" }); //starts 1 resolves 2
         await step.do("task d", async () => JSON.stringify(c)); //starts 2 resolves 3
         return Promise.all([a, b]); //resolves 3
       };
    
       const branchB = async () => {
         const e = step.do("task e", async () => "e"); //starts 1
         const f = step.do("task f", async () => "f"); //starts 1
         return Promise.all([e, f]); //resolves 2
       };
    
       await Promise.all([branchA(), branchB()]);
    
       await step.sleep("final sleep", 1000);
     }
    }

다이어그램에서 단계의 정렬을 볼 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3163 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW480NNEVSMK7AVV6RGRF4T0.png&w=715&h=611&f=webp&fit=cover&position=center)

이러한 패턴을 모두 고려한 후 다음과 같은 노드 유형 목록을 결정했습니다. 
    
    
    | StepSleep
    | StepDo
    | StepWaitForEvent
    | StepSleepUntil
    | LoopNode
    | ParallelNode
    | TryNode
    | BlockNode
    | IfNode
    | SwitchNode
    | StartNode
    | FunctionCall
    | FunctionDef
    | BreakNode;

다음은 다양한 동작에 대한 API 출력 샘플입니다. 

`function` 호출:
    
    
    {
      "functions": {
        "runLoop": {
          "name": "runLoop",
          "nodes": []
        }
      }
    }

`if` 조건이 `step.do`로 분기됩니다:
    
    
    {
      "type": "if",
      "branches": [
        {
          "condition": "loop > maxLoops",
          "nodes": [
            {
              "type": "step_do",
              "name": "notify max loop reached",
              "config": {
                "retries": {
                  "limit": 5,
                  "delay": 1000,
                  "backoff": "exponential"
                },
                "timeout": 10000
              },
              "nodes": []
            }
          ]
        }
      ]
    }

`step.do` 및 `waitForEvent`와 `waitForEvent`.
    
    
    {
      "type": "parallel",
      "kind": "all",
      "nodes": [
        {
          "type": "step_do",
          "name": "correctness agent (loop ${...})",
          "config": {
            "retries": {
              "limit": 5,
              "delay": 1000,
              "backoff": "exponential"
            },
            "timeout": 10000
          },
          "nodes": [],
          "starts": 1
        },
    ...
        {
          "type": "step_wait_for_event",
          "name": "wait for user response (loop ${...})",
          "options": {
            "event_type": "user-response",
            "timeout": "unknown"
          },
          "starts": 3,
          "resolves": 4
        }
      ]
    }

### 다음 단계

이 Workflow 다이어그램의 최종 목표는 풀 서비스 디버깅 도구로 기능하는 것입니다. 즉, 다음을 수행할 수 있습니다.

  * 그래프를 통해 실시간으로 실행 추적
  * 오류를 발견하고, 휴먼인더루프(human-in-the-loop) 승인을 기다리며, 테스트 단계를 건너뛰세요
  * 로컬 개발 시각화 액세스



[ _워크플로 개요 페이지_](https://dash.cloudflare.com/?to=/:account/workers/workflows)에서 다이어그램을 확인하세요. 기능 요청이나 버그를 발견하면 [_Discord의 Cloudflare 개발자 커뮤니티_](https://discord.cloudflare.com/)에 참여하여 Cloudflare 팀에 직접 피드백을 공유해 주세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkflow-diagrams%2F&t=Cloudflare%EC%97%90%EC%84%9C%20%EC%B6%94%EC%83%81%20%EA%B5%AC%EB%AC%B8%20%ED%8A%B8%EB%A6%AC%28AST%29%EB%A5%BC%20%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC%20Workflows%20%EC%BD%94%EB%93%9C%EB%A5%BC%20%EC%8B%9C%EA%B0%81%EC%A0%81%20%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8%EC%9C%BC%EB%A1%9C%20%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94%20%EB%B0%A9%EB%B2%95%20)[](https://x.com/intent/post?text=Cloudflare%EC%97%90%EC%84%9C+%EC%B6%94%EC%83%81+%EA%B5%AC%EB%AC%B8+%ED%8A%B8%EB%A6%AC%28AST%29%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+Workflows+%EC%BD%94%EB%93%9C%EB%A5%BC+%EC%8B%9C%EA%B0%81%EC%A0%81+%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8%EC%9C%BC%EB%A1%9C+%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95+&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkflow-diagrams%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkflow-diagrams%2F)[](https://bsky.app/intent/compose?text=Cloudflare%EC%97%90%EC%84%9C+%EC%B6%94%EC%83%81+%EA%B5%AC%EB%AC%B8+%ED%8A%B8%EB%A6%AC%28AST%29%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+Workflows+%EC%BD%94%EB%93%9C%EB%A5%BC+%EC%8B%9C%EA%B0%81%EC%A0%81+%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8%EC%9C%BC%EB%A1%9C+%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95++https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkflow-diagrams%2F)[](https://mastodonshare.com/?text=Cloudflare%EC%97%90%EC%84%9C+%EC%B6%94%EC%83%81+%EA%B5%AC%EB%AC%B8+%ED%8A%B8%EB%A6%AC%28AST%29%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+Workflows+%EC%BD%94%EB%93%9C%EB%A5%BC+%EC%8B%9C%EA%B0%81%EC%A0%81+%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8%EC%9C%BC%EB%A1%9C+%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95+&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkflow-diagrams%2F)[](https://www.threads.net/intent/post?text=Cloudflare%EC%97%90%EC%84%9C+%EC%B6%94%EC%83%81+%EA%B5%AC%EB%AC%B8+%ED%8A%B8%EB%A6%AC%28AST%29%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+Workflows+%EC%BD%94%EB%93%9C%EB%A5%BC+%EC%8B%9C%EA%B0%81%EC%A0%81+%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8%EC%9C%BC%EB%A1%9C+%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95++https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkflow-diagrams%2F)

## 관련 태그

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Workflows](https://blog.cloudflare.com/ko-kr/tag/workflows/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
