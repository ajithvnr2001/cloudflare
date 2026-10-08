---
url: https://blog.cloudflare.com/ko-kr/rollbacks-for-workflows/
title: Cloudflare Workflows\ub97c \uc704\ud55c saga \ub864\ubc31\uc744 \uad6c\ucd95\ud55c \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:40.827488+00:00
---

# Cloudflare Workflows를 위한 saga 롤백을 구축한 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/rollbacks-for-workflows/

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

2026년 6월 25일

# Cloudflare Workflows를 위한 saga 롤백을 구축한 방법

![Vaishnav Kavitha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMMZ8JJQ1SE783SASV4PJ.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Mia Malden](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4559TC07A12MQHAEK8YM1R.jpg&w=64&h=64&f=webp&fit=cover&position=center)![André Venceslau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TZTSTWQ6JMKEC8GX38NE.png&w=64&h=64&f=webp&fit=cover&position=center)

[Vaishnav Kavitha](https://blog.cloudflare.com/ko-kr/author/vaishnav-kavitha/), [Mia Malden](https://blog.cloudflare.com/ko-kr/author/mia/) 및 [André Venceslau](https://blog.cloudflare.com/ko-kr/author/andre-venceslau/)

12분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/rollbacks-for-workflows/), [日本語](https://blog.cloudflare.com/ja-jp/rollbacks-for-workflows/), [繁體中文](https://blog.cloudflare.com/zh-tw/rollbacks-for-workflows/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/rollbacks-for-workflows/).

![BLOG-3317 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMM3AX6SCQ1TVSR6M8NMX.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+P/84u3z1uPw4Onz8PP39fX07u3s////+v/+4+320+Dy1+L15ez57fD27O3u/////f//5+/509/1z9742uX85uz57O3x////////7vT+2eP50d/82OX/5ez97/D1////////+Pz/5ez+3ef/4uv/7fL/9fb6////////////9Pf/7/P/8vf/+fv//fz+/////////////////f3/////////////////////////////////////////////)

Cloudflare Workflows를 사용하면 내장된 재시도 및 장기 실행 프로세스에서의 상태 지속성을 갖춘 내구성 있는 다단계 애플리케이션을 구축할 수 있습니다. [_Workflow_](https://developers.cloudflare.com/workflows/) 가 실행되면 각 단계에서 외부 시스템을 호출하고, 실패를 재시도하며, 다시 시작할 때 상태를 유지할 수 있습니다. 그러나 한 단계가 실패하면 완료된 단계의 이전 작업이 일관성이 없거나 부분적인 상태로 남을 수 있습니다.

오늘 Workflows를 위한 saga 롤백을 출시하여, 실패할 경우 단계 자체 내에서 롤백 로직을 선언할 수 있습니다.

예를 들어, 서로 다른 두 은행의 계좌로 자금을 이체하는 워크플로우가 있다고 가정해 보겠습니다.

  1. 은행 A 계좌에서 인출
  2. 은행 B 계좌로의 입금
  3. 두 계정 소유자 모두에게 확인 이메일 전송



은행 B에 입금하는 2단계에 실패하면 어떻게 될까요? 은행 A에서 인출이 성공하면 거래가 확정되고 금액이 시스템에서 떠나게 됩니다. 트랜잭션의 조율자는 A 은행의 시스템에서 작업을 단순히 "실행 취소"할 수 없습니다. 대신 첫 번째 작업을 의미론적으로 전환하는 새로운 작업을 통해 돈을 은행 A의 계좌로 다시 입금해야 합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WKYMHAWC2FCMBSGG1XMKT.png&w=715&h=681&f=webp&fit=cover&position=center)

  
작업과 보상 로직을 이렇게 조합하는 것을 [_사가 패턴_](https://www.youtube.com/watch?v=xDuwrtwYHu8)이라고 합니다.

이전에는 개발자가 단계의 직접적인 정의를 벗어나 성공, 실패, 실패 시 수행해야 하는 조치를 추적하기 위해 자체적인 보상 로직을 구현해야 했습니다. 이제 각 단계에 대한 보상 로직을 정의할 수 있습니다. `step.do()` 롤백에 대한 워크플로의 내구성도 유지합니다.
    
    
    // track what completed so we know what to undo
    let debitA;
    let creditB;
    try {
      debitA = await step.do("debit-bank-a", () => bankA.debit(from, amount));
      creditB = await step.do("credit-bank-b", () => bankB.credit(to, amount));
      await step.do("notify", () => notifyBoth(from, to, amount));
    } catch (error) {
      // unwind in reverse. each undo is its own durable step,
      // must be idempotent, and must keep going if one fails.
      if (creditB) {
        try {
          await step.do("reverse-credit-b", () => bankB.debit(to, amount, creditB.id));
        } catch (e) {
          await alertOnCall("reverse-credit-b failed", e);
        }
      }
      if (debitA) {
        try {
          await step.do("refund-debit-a", () => bankA.credit(from, amount, debitA.id));
        } catch (e) {
          await alertOnCall("refund-debit-a failed", e);
        }
      }
      throw error;
    }

_롤백 없음_
    
    
     // each step ships with its own undo. add a step,
    // add its rollback right here. no growing catch
    // block, no manual ordering, no replay logic.
    await step.do("debit-bank-a", () => bankA.debit(from, amount), {
      rollback: async ({ output }) => bankA.credit(from, amount, output.id),
    });
    await step.do("credit-bank-b", () => bankB.credit(to, amount), {
      rollback: async ({ output }) => bankB.debit(to, amount, output.id),
    });
    await step.do("notify", () => notifyBoth(from, to, amount));

_롤백 포함_

## 사용해 보기

롤백을 사용하려면 `롤백` 함수가 포함된 옵션 객체를 `step.do()`의 마지막 인수로 전달하면 됩니다.
    
    
    const debit = await step.do(
      "debit-account-a",
      async () => {
        return await bankA.debit({
          accountId: fromAccountId,
          amount,
          idempotencyKey: `${transferId}:debit-account-a`,
        });
      },
      {
        rollback: async () => {
          await bankA.credit({
            accountId: fromAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-debit-account-a`,
          });
        },
      }
    );
    
    // The idempotency keys make both the forward operations and rollback operations safe to retry without duplicating the transfer
    
    const credit = await step.do(
      "credit-account-b",
      async () => {
        return await bankB.credit({
          accountId: toAccountId,
          amount,
          idempotencyKey: `${transferId}:credit-account-b`,
        });
      },
      {
        rollback: async ({ output }) => {
          if (output === undefined) {
            return;
          }
    
          await bankB.debit({
            accountId: toAccountId,
            amount,
            idempotencyKey: `${transferId}:rollback-credit-account-b`,
          });
        },
      }
    );
    
    
    // If we fail here, we may want to revert all previous payments. Users should not have to wrap their code in complex try-catch logic just to revert two small payments (see below)
    
    await step.do("send-confirmation", async () => {
      await sendTransferConfirmation({ ... });
    });

롤백 함수는 일반 Workflow 단계와 마찬가지로 멱등해야 합니다. 요금을 환불하는 경우에는 결제 공급자의 멱등 키를 사용하세요. 인벤토리를 릴리스하는 경우 안전한 상태로 두 번 이상 호출하도록 합니다.

단계가 실패하면 롤백 처리기가 역방향 `단계 시작` 순서로 실행됩니다. 간단히 말해서 문제가 발생하면 실행 취소 단계를 실행하면 됩니다. 실제로 APIs와 실행 모델을 중요하게 만드는 몇 가지 세부 사항이 있습니다.

1\. **실패한 단계는 여전히 롤백이 필요할 수 있습니다.** 실패한 `step.do()` 롤백 처리기를 등록한 경우에도 롤백 자격이 있을 수 있습니다.

사용자 코드에 오류가 발생하고 Workflow가 계속 진행되는 경우 롤백이 시작되지 않지만, 단계 오류가 발생하고 Workflow가 나중에 다른 이유로 실패하는 경우, 롤백은 여전히 이전에 등록된 핸들러에 대해 실행될 수 있으며, 이 핸들러는 역방향 `step-start` 순서로 실행됩니다.

그 이유는 무엇일까요? 단계가 실패하기 전에 외부 시스템과 부분적으로 상호 작용했을 수 있습니다. 예를 들어 결제 공급자가 요금을 캡처하더라도 `ChargeId` 를 Workflows에 반환하기 전에 단계가 실패할 수 있습니다. 이것이 롤백 핸들러가 `출력을` 수신하지만 출력을 처리해야 하는 `이유입니다 === undefined.`

2\. **롤백은 Workflow가 실패할 때만 시작됩니다.** 롤백 처리기를 추가해도 단계 오류가 있을 때마다 롤백이 트리거되는 것은 아닙니다. 사용자 코드에서 오류를 포착하고 계속하면 Workflow가 계속 진행됩니다. 롤백은 Workflow 자체가 최종적으로 실패하게 될 때 시작됩니다.

롤백이 시작되면 Workflows는 적합한 `step.do()` 를 찾습니다. 롤백 핸들러를 실행한 다음, 최종 Workflow 실패를 기록합니다.

3\. **순서를 예측할 수 있어야 합니다.** 순차적 Workflows의 경우 롤백 순서는 다음과 같이 명확합니다.

  1. 인벤토리를 예약합니다.
  2. 차지 카드.
  3. 선적을 생성합니다.
  4. 배송이 실패하면 카드를 환불하고 재고를 반출합니다.



병행 단계들은 이를 더욱 미묘하게 만듭니다. 완료 순서는 시작 순서와 다를 수 있으므로 Workflows는 완료 순서를 반대로 바꾸는 대신 단계 시작 시작 순서를 반대로 사용합니다.

실제 규칙은 다음과 같습니다.

  1. 롤백 핸들러로 시작되거나 완료된 모든 단계가 적합합니다.
  2. 실패한 `step.do()` 도 롤백 핸들러를 등록했다면 자격이 있습니다.
  3. 처리기는 완료 순서가 아닌 단계-시작 순서의 역순으로 실행됩니다.



## Cloudflare에서 API를 설계한 방법

예상되는 행동을 염두에 두고 나면 이 새로운 패턴을 Workflows API에 추가해야 했습니다. 롤백은 `롤백 옵션`을 결정하기 전에 몇 번의 반복을 거쳤습니다. 

### 유창한 API나 빌더 API가 안 되는 이유는 무엇일까요?

첫 번째 접근 방식은 유창한 형식이었습니다. `step.do(...).rollback(...)` 읽기 쉽습니다. 포워드 액션과 보상은 나란히 배치되어 있고, 호출 사이트는 일반적인 JavaScript 체인처럼 보입니다.

문제는 `step.do()` 입니다. 이미 중요한 의미가 있습니다. 즉, 지속형 단계를 시작하고 단계 출력에 대한 약속을 반환합니다. Workers에서 프라미스류 값은 특히 의미가 있습니다. Workers RPC는 [_프라미스 파이프라인_](https://blog.cloudflare.com/capnweb-javascript-rpc-library/#chained-calls-promise-pipelining)(이는 [_Cap'n Proto_](https://capnproto.org/rpc.html#time-travel-promise-pipelining)와 같은 시스템에서 상속된 패턴)을 지원하기 때문입니다.

프라미스 파이프라인을 사용하면 코드에서 미래 값이 호출자에게 완전히 반환되기 전에 해당 값에서 메서드를 호출할 수 있습니다. 예:
    
    
    const session = api.authenticate(apiKey);
    const name = await session.whoami();

여기에서 `session` 은 아직 실제 세션 객체가 아닙니다. 이는 곧 존재하게 될 세션에 대한 핸들과도 같습니다. `session.whoami()`를 호출하면 Workers는 조기에 원격 측에 해당 호출을 보내고 "인증이 세션을 생성하면 `whoami()` 를 호출하라"고 말할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMVWKS68D8HCFGVRZQ2RA.png&w=715&h=476&f=webp&fit=cover&position=center)

왕복 시간이 절약됩니다. 호출자는 `authenticate()` 가 완전히 완료될 때까지 기다렸다가 `whoami()`를 요청할 필요가 없습니다.

저희는 유창한 API로 간주했습니다.
    
    
    step.do("charge-card", chargeCard).rollback(refundCharge);

  
독자에게 이는 `"요금 카드` 결과에 대한 ` call.rollback()"처럼 보일` 수 있습니다. 하지만 롤백은 단계 출력에 포함되지 않습니다. 이는 `step.do()` 의 일부입니다. 옵션이 포함되어 있으므로 Workflows는 이후 단계가 실패할 경우 해당 단계를 보상하는 방법을 알고 있습니다.

또한 API가 유창하면 단계 타이밍을 추론하기가 더 어려워집니다. 오늘, `step.do()` 단계가 호출될 때 단계를 시작하므로 개발자가 단계를 시작하고 다른 작업을 수행하며 나중에 첫 번째 단계를 기다릴 수 있습니다.
    
    
    const first = step.do("first", () => serviceA.call());
    
    await step.do("second", () => serviceB.call());
    
    await first;

현재의 실행 모델에서는`1순위가` 즉시 시작되고 `2순위가 그 뒤를` 잇습니다. 유창한 API라면 상황은 복잡해집니다. Workflows가 대기 상태인지 확인해야 ` 합니다.rollback()` 전체 단계 정의를 알기도 전에 연결되기 때문입니다. 이로 인해 단계가 엔진으로 전송되는 시점이 지연될 수 있습니다.

앞의 예시에서`first` `는 second` 가 이미 완료된 후 `step.do("first", ...)` 대신 `await first` 에서 시작할 수 있습니다.

따라서 동시성 Workflows를 추론하기가 더 어려워집니다. 단계 타이밍은 반환된 `Promise` 가 소비되는 시점뿐만 아니라 `step.do()` 가 호출된 위치에 따라 달라집니다.

빌더 스타일 APIs도 고려했습니다.
    
    
    const charge = await step
    	.saga("charge")
    	.do(() => chargeCard())
    	.rollback(() => refundCharge())
    	.run();

빌더 API는 `프라미스` 모호성을 방지합니다. 또한 향후 단계 수준 옵션에 대한 명확한 위치를 제공하고, 앞으로 작업과 롤백 작업이 동일한 사가 단계에 속해 있음을 명확하게 보여줍니다.

하지만 여기에는 예의가 추가됩니다. 모든 단계에는 final `.run()`이 필요합니다. forgetting `.run()` 도구가 없으면 찾기 쉽고 찾기 어려우며 간단한 원스텝 케이스는 구성 체인처럼 보이기 시작합니다. 또한 새로운 `step.saga()` 를 소개합니다. 빌더가 기존 단계에서 `벗어납니다.<action>` 패턴입니다. 가장 중요한 것은 `step.do()` 기본 Workflows 기본 요소가 아니라 이전 API처럼 느껴집니다. 롤백의 목표는 `step.do()`를 확장하는 것이었습니다. 대체하지 마세요.

### 단계 메타데이터로서의 롤백
    
    
    step.do(..., { rollback })

궁극적으로 롤백이 단계에서의 메타데이터인 명시적 형식을 선택했습니다.

이렇게 하면 각 롤백이 포워드 단계 자체 내에서 정의됩니다. 각 핸들러는 롤백 시작의 원인이 된 오류, [_단계 컨텍스트_](https://developers.cloudflare.com/workflows/build/step-context/), 그리고 포워드 단계에서 반환된 지속된 값(정의되지 않을 수 있음)이거나 단계가 값을 유지하기 전에 실패한 경우 undefined인 출력 값을 받습니다.

롤백은 수명 주기 이벤트를 생성하므로 보상이 시작되었는지, 어떤 롤백 핸들러가 실패했는지, 롤백이 성공적으로 완료되었는지 여부를 알 수 있습니다.

결정적으로, 원래의 Workflow 오류는 별개로 유지됩니다. 롤백은 Workflow가 실패한 이유가 아니라 실패 후 Workflows에서 수행하는 것입니다.

`WorkflowStepConfig`를 통해[ _단계 구성_](https://developers.cloudflare.com/workflows/build/workers-api/#workflowstepconfig) 에서 사용자 지정 재시도 및 제한 시간 초과 동작을 정의할 수 있는 것처럼,`rollbackConfig 에 롤백` 관련 값을 추가합니다.
    
    
    {
      rollback: async ({ output }) => {
        await bankA.credit({ accountId: fromAccountId, amount, transferId: `${transferId}-reversal` });
      },
      rollbackConfig: {
        retries: { limit: 10, delay: '30 seconds', backoff: 'exponential' },
        timeout: '2 minutes',
      },
    }

이는 우리가 원했던 수명주기 이벤트 멘탈 모델과 일치합니다. `step.do()` 는 이미 Workflows에서 기록하고 재시도하며 나중에 로그에 표시하는 지속형 작업 단위를 설명합니다. 롤백은 동일한 작업 단위에 대한 또 다른 수명 주기 동작입니다. API는 별도의 래퍼 또는 빌더가 아니라 단계 정의와 함께 이동해야 합니다.

  * 이 단계는 `step.do()` 가 정상적으로 시작될 때 여전히 시작됩니다.
  * 반환된 프라미스는 여전히 단계 출력을 나타냅니다.
  * Concurrent Workflow 코드는 동일한 실행 모델을 유지합니다.
  * 롤백 처리기 옆에 라이브 롤백 재시도 및 제한 시간 초과 옵션이 있습니다.
  * 기존 `step.do()` 오늘날과 똑같이 작동합니다.



이 형태는 유창한 API보다 약간 더 명시적이지만, 해당 명시성은 유용합니다. 작업과 보상이 여전히 한 곳에 있으며, APIs가 새로운 단계 빌더나 새로운 종류의 프라미스를 도입하지 않습니다. `step.do()` 를 이미 이해하고 있는 개발자 하나의 추가 `옵션` 개체만 학습하면 됩니다.

마법 같은 것은 아니지만, 더 쉽게 채택할 수 있고 더 명확하게 이해할 수 있습니다.

## 내부 작동 방식

롤백은 API가 약간 추가된 것처럼 느껴지지만, 이에 따라 Workflows가 각 단계에 대해 기록해야 하는 내용이 변경됩니다.

일반적인 `step.do()` 이미 영구 기록이 있습니다. Workflows는 단계의 시작, 완료 여부, 반환된 내용, Workflow가 나중에 다시 시작될 경우 단계를 반복하는 대신 건너뛰어야 하는지 여부를 기록합니다.

롤백은 해당 레코드에 한 가지 더 추가됩니다. 단계가 보상 로직을 등록했는지 여부.

이는 Workflow가 실패할 때 통합할 수 있는 두 가지 정보가 Workflows에 있음을 의미합니다.

첫 번째는 **지속성 단계 기록** 입니다. Workflow 엔진은 데이터를 저장하여 실행된 내용, 완료된 내용, 저장된 출력, 롤백이 등록되었는지 여부를 알 수 있습니다.

두 번째는 해당 단계를 보상하기 위해 작성된 함수인 **롤백 핸들러** 자체입니다. Workflows는 해당 함수의 텍스트를 데이터로 저장하지 않습니다. 대신 Workflow가 실행되는 동안 핸들러에 대한 호출 가능 참조를 유지합니다.

Workers RPC에서는 이러한 종류의 호출 가능 참조를 [**_스텁_**](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle)이라고 합니다. 스텁을 사용하면 시스템의 한 부분이 다른 곳에서 실행 중인 코드를 호출할 수 있습니다. 또한 스텁에는 호출 또는 실행 컨텍스트가 끝날 때 삭제될 수 있는 수명이 있습니다. 이 시점이 지나도 스텁을 유지해야 하는 경우, Workers RPC는 동일한 대상에 대한 다른 핸들을 생성하는 [`_dup()_`](https://developers.cloudflare.com/workers/runtime-apis/rpc/lifecycle/#the-dup-method) 메서드를 제공합니다.

롤백의 경우 이 모델은 유용합니다. 영구 걸음 수 이력에는 보상이 필요한 구간이 기록됩니다. 롤백 스텁은 Workflows에서 보상 코드를 호출하는 방법을 제공합니다. 그리고 롤백 핸들러가 즉각적인 `step.do()` 단계보다 오래 지속되어야 할 수도 있기 때문에 호출을 하더라도 Workflows는 롤백 단계 동안 핸들러에 대한 자체 호출 가능 참조를 유지합니다.

일반적인 경우 동일한 엔진 수명 내에 Workflow가 롤백 상태가 되면 Workflows에는 이미 필요한 롤백 스텁이 있는 것입니다. 이는 지속형 단계 기록을 사용해 대상 단계를 찾은 다음 포워드 실행 중에 등록된 롤백 스텁을 호출할 수 있습니다.

이는 Workflows를 다시 시작한 후 **복구** 해야 하는 경우 더 미묘해집니다.

롤백이 필요한 동안 엔진이 퇴출되거나 충돌하거나 재시작하는 경우, Workflows에는 여전히 지속 단계 이력이 있지만, 더 이상 인메모리 롤백 스텁이 없을 수 있습니다. 복구를 위해 Workflows는 **재생** 을 사용합니다. 재생은 완료된 정방향 단계 본문을 다시 실행하지 않고 Workflow 코드를 다시 실행할 수 있는 복구 모드입니다.

재생이 완료된 `step.do()`에 도달하면, Workflows는 단계 본문을 다시 실행하는 대신 지속된 결과를 읽습니다. 롤백 복구의 경우, Workflows는 롤백이 연결되어 롤백에 적합한 단계에 대한 핸들러만 재구축하면 됩니다. 해당 `step.do() `롤백 옵션을 통해 호출 가능한 스텁이 다시 등록될 수 있습니다.

이를 통해 Workflows는 원래 외부 부작용을 복제하지 않고도 필요한 롤백 핸들러를 복구할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3317 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMK8HE1XEHVNX1B4RNK9W.png&w=715&h=699&f=webp&fit=cover&position=center)

이러한 부분들이 준비되면 핸들러가 메모리에서 여전히 사용 가능하든, 복구 중에 핸들러를 다시 빌드해야 하든 관계없이 롤백이 작동할 수 있습니다.

Workflows가 실패하려고 할 때 Workflows는 애플리케이션에 무슨 일이 일어났는지 재구성하도록 요청하지 않습니다. 이미 걸음 수 기록이 있습니다. DLP는 지속된 레코드를 살펴보고 다음과 같은 중요한 질문에 답할 수 있습니다.

  * 어떤 단계가 시작되었나요?
  * 어떤 단계가 완료되었나요?
  * 어떤 실패한 단계가 여전히 정리가 필요할까요?
  * 어떤 단계에서 롤백 처리기를 등록할까요?
  * 각 롤백 처리기는 어떤 출력을 받아야 할까요?
  * 어떤 순서로 보상을 실행해야 할까요?



그런 다음 Workflows는 롤백 컨텍스트(원래 오류, 단계 컨텍스트, 단계 출력(하나가 지속된 경우))를 사용하여 각 롤백 스텁을 호출합니다.

주문 세부 정보는 중요합니다. 일반 JavaScript, 특히 `Promise.all()`에서 완료 순서가 시작 순서와 항상 같지는 않습니다. A 단계가 먼저 시작되고 B 단계가 두 번째로 시작되면 B 단계가 먼저 완료될 수 있습니다. 롤백의 경우, Workflows는 지속된 시작 순서를 안정적인 소스로 사용한 다음, 역순으로 해제합니다.

롤백 처리기는 Workflows의 일반 단계적 기계를 통해서도 실행됩니다. 즉, 재시도, 제한 시간 초과, 수명 주기 이벤트, 로그, 최종 기록 결과 등 여러분이 Workflows에서 기대하는 것과 동일한 운영 속성이 보상으로 주어집니다. 구성된 재시도 후에도 롤백 핸들러가 계속 실패하는 경우, Workflows는 롤백 결과를 실패로 기록하고 나머지 롤백 핸들러 실행을 중지하며, Workflow 인스턴스는 궁극적으로 `오류` 상태가 됩니다.

이것이 saga 롤백과 `catch` 블록의 주요 차이점입니다. `catch` 블록은 JavaScript가 실행된 정확한 시점에 메모리에 무엇이 남아 있는지만 알 수 있습니다. Workflows 롤백은 지속되는 단계 기록을 사용하여 이미 발생한 상황을 결정하고, 일반적인 사례에서 이미 보유한 스텁을 호출하고, 복구 중 필요 시 필요할 때 복구 중 누락된 스텁을 안전하게 재구축합니다.

그래서 API가 `step.do()` 살펴봅니다. 롤백은 별도의 전역 오류 핸들러가 아니라 Workflows에서 이미 이해하고 있는 지속성 있는 작업 단위에 연결된 메타데이터입니다.

## 다음 단계

Cloudflare의 첫 번째 롤백에는 다음이 포함됩니다. 

  * `step.do()`를 위한 명시적 단계별 롤백 핸들러
  * 순차적 롤백 실행
  * 보상을 위한 재시도 및 제한 시간 초과 구성



다음으로 살펴볼 내용은 다음과 같습니다.

  * [`_waitForEvent_`](https://developers.cloudflare.com/workflows/build/events-and-parameters/#wait-for-events)에 대한 롤백 지원
  * 병렬 롤백 실행 지원
  * [ _Python Workflows_](https://developers.cloudflare.com/workflows/python/)에 대한 롤백 지원



여러 단계로 구성된 애플리케이션이 중간에 실패할 때 가장 힘든 순간은 _실패했다는_ 사실을 모르는 것입니다. 이미 일어난 일과 다음에 _무엇이_ 일어나야 하는지 아는 것입니다.

Saga 롤백을 사용하면 각 단계 옆에 해당 답변을 배치할 수 있습니다. Workflows로 다단계 애플리케이션을 구축하는 경우, saga 롤백을 시도하고 다음에 원하는 보상 패턴을 알려주세요. [_Workflows 문서_](https://developers.cloudflare.com/workflows/) 를 시작하고 [_Cloudflare 커뮤니티_](https://community.cloudflare.com/)에서 피드백을 공유하세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Frollbacks-for-workflows%2F&t=Cloudflare%20Workflows%EB%A5%BC%20%EC%9C%84%ED%95%9C%20saga%20%EB%A1%A4%EB%B0%B1%EC%9D%84%20%EA%B5%AC%EC%B6%95%ED%95%9C%20%EB%B0%A9%EB%B2%95)[](https://x.com/intent/post?text=Cloudflare+Workflows%EB%A5%BC+%EC%9C%84%ED%95%9C+saga+%EB%A1%A4%EB%B0%B1%EC%9D%84+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Frollbacks-for-workflows%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Frollbacks-for-workflows%2F)[](https://bsky.app/intent/compose?text=Cloudflare+Workflows%EB%A5%BC+%EC%9C%84%ED%95%9C+saga+%EB%A1%A4%EB%B0%B1%EC%9D%84+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Frollbacks-for-workflows%2F)[](https://mastodonshare.com/?text=Cloudflare+Workflows%EB%A5%BC+%EC%9C%84%ED%95%9C+saga+%EB%A1%A4%EB%B0%B1%EC%9D%84+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Frollbacks-for-workflows%2F)[](https://www.threads.net/intent/post?text=Cloudflare+Workflows%EB%A5%BC+%EC%9C%84%ED%95%9C+saga+%EB%A1%A4%EB%B0%B1%EC%9D%84+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Frollbacks-for-workflows%2F)

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
