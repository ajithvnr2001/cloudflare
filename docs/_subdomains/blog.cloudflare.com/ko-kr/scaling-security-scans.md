---
url: https://blog.cloudflare.com/ko-kr/scaling-security-scans/
title: \ubcf4\uc548 \uc778\uc0ac\uc774\ud2b8 \ud655\uc7a5: \uae00\ub85c\ubc8c \uc2a4\uce90\ub2dd \uc6a9\ub7c9\uc744 10\ubc30 \ub298\ub9ac\ub294 \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:35:20.872005+00:00
---

# 보안 인사이트 확장: 글로벌 스캐닝 용량을 10배 늘리는 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/scaling-security-scans/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Kafka](https://blog.cloudflare.com/ko-kr/tag/kafka/)[Postgres](https://blog.cloudflare.com/ko-kr/tag/postgres/)[보안 상태 관리](https://blog.cloudflare.com/ko-kr/tag/security-posture-management/)+22개의 태그 더 보기

5개 태그5개 태그 보기

  * 게시물 태그
  * [Kafka](https://blog.cloudflare.com/ko-kr/tag/kafka/)[Postgres](https://blog.cloudflare.com/ko-kr/tag/postgres/)[보안 상태 관리](https://blog.cloudflare.com/ko-kr/tag/security-posture-management/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[응용 프로그램 보안](https://blog.cloudflare.com/ko-kr/tag/application-security/)
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



[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[응용 프로그램 보안](https://blog.cloudflare.com/ko-kr/tag/application-security/)

[Kafka](https://blog.cloudflare.com/ko-kr/tag/kafka/)[Postgres](https://blog.cloudflare.com/ko-kr/tag/postgres/)[보안 상태 관리](https://blog.cloudflare.com/ko-kr/tag/security-posture-management/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[응용 프로그램 보안](https://blog.cloudflare.com/ko-kr/tag/application-security/)

2026년 6월 12일

# 보안 인사이트 확장: 글로벌 스캐닝 용량을 10배 늘리는 방법

![Dave Baxter](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GGX3X5MXWP1Q0BBVAMCR.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Dave Baxter](https://blog.cloudflare.com/ko-kr/author/dave-baxter/)

11분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/scaling-security-scans/) 및 [日本語](https://blog.cloudflare.com/ja-jp/scaling-security-scans/).

![BLOG-3307 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455GF2NCFC9V7H6F5JSR8H.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////vz78u7w6Obq6ers7fHx7fHx6err////+/v97Orx4ODq4OXs5u3y6e7y5ujt////+vr/5+j02Nzs2OHu4Ov05e315ejw/////f7/6ev52t/x2uTz4u756PH56Ov1////////8/T/5ur45u767ff/8fn/8PP7////////////9/j/9/v//P///f//+vz/////////////////////////////////////////////////////////////////)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

[_보안 인사이트_](https://developers.cloudflare.com/security/security-insights/) 는 모든 Cloudflare 계정에 대해 실행 가능한 보안 권장 사항을 제공합니다. 이러한 인사이트를 찾기 위해 모든 계정, 영역, DNS 레코드를 정기적으로 스캔하여 잠재적인 보안 위험과 잘못된 구성이 있는지 찾습니다.  


하지만 두 가지 중요한 문제가 발생했습니다. 첫째, 스캔 빈도가 너무 낮았습니다. 검사는 한두 주에 한두 번만 수행되었으므로 새로 도입된 보안 위험은 최대 2주 동안 감지되지 않은 채로 남아 있을 수 있었습니다. 둘째, 많은 무료 요금제 계정이 자동 검사를 선택했는데, 이는 많은 계정이 전혀 검사되지 않는다는 것을 의미했습니다.

자동화된 공격이 가속화되면서 보안 구성 오류를 감지할 수 있는 윈도우는 줄어들고 있습니다. Cloudflare는 _모든_ 고객을 위해 이러한 문제가 발생하도록 하는 것은 모두를 위해 더 나은 인터넷을 구축하려는 Cloudflare의 목표에 매우 중요합니다.

스캔 빈도를 높이고 모든 계정에 대한 자동 스캔을 활성화하려면 스캔 처리량을 평균 약 10배, 즉 초당 10회 스캔에서 초당 100회 스캔으로 늘려야 한다는 계산이 나왔습니다. 하지만 저희 시스템은 이미 로드로 인해 어려움을 겪고 있었습니다. 수백만 개의 이벤트가 처리를 기다리는 백로그를 가득 채우고 있었습니다. API가 자주 시간 초과되었습니다. 프로세스가 충돌했습니다. 시스템을 수리해야 했고 _확장할_ 수 있어야 했습니다.

Cloudflare가 Security Insights의 스캔 처리량을 10배 이상 늘리고 수백만 고객에게 보안 인사이트를 제공하며 모든 고객을 대상으로 스캔 빈도를 두 배로 늘린 방법에 대한 이야기입니다. Cloudflare가 이러한 개선을 달성한 방법을 알아보려면 계속 읽어보세요.

## Cloudflare가 보안 인사이트를 스캔하는 방법

높은 수준에서 자동 보안 검사는 스케줄러에 의해 트리거됩니다. 계정 또는 영역을 스캔해야 하는 경우 스케줄러는 오픈 소스 분산 이벤트 스트리밍 플랫폼인 [_Apache Kafka_](https://blog.cloudflare.com/using-apache-kafka-to-process-1-trillion-messages/)에 메시지(또는 메시지)를 게시합니다. 이러한 메시지는 특정 자산 또는 구성을 스캔하는 전문화된 Go 마이크로서비스인 여러 체커에 전달됩니다.

각 검사기는 모든 메시지에 대해 결과(발견한 보안 인사이트)를 내부 API로 전송하고, 내부 API는 이를 Postgres 데이터베이스에 저장합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XA08C1D2X1ERGR4EQW9X.jpg&w=715&h=1163&f=webp&fit=cover&position=center)

## 확장 가능하게 만들기

### Kafka 확장

Apache Kafka는 엄밀히 말하면 _큐_ 가 아닙니다. 분할된 이벤트 스트림입니다(최근에 [_대기열 시맨틱_](https://www.confluent.io/blog/kafka-queue-semantics-share-consumer-ga/)을 갖게 되었지만). 파티션 내에서 메시지는 순서대로 소비되고 _처리_ 되어야 합니다. 이는 메시지가 순서대로 사용될 수 있지만 순서대로 처리되지 않는 일반적인 대기열과 다릅니다. 따라서 _소비자 그룹_ 내에서는 파티션당 하나의 소비자만 활성화될 수 있습니다.

이로 인해 다음과 같은 두 가지 결과가 초래됩니다.

  * 처리 속도가 느린 메시지 때문에 소비자가 다음 메시지로 넘어갈 수 없음
  * 각 검사기에 대해 파티션 개수만큼 소비자를 가질 수 있습니다(각 검사기마다 자체 소비자 그룹이 있음)



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44G4BXDMSJ2RQWZAXHMFVV.jpg&w=715&h=585&f=webp&fit=cover&position=center)

파티션을 더 추가하여 확장을 시도할 수도 있었습니다. 그러나 이렇게 하면 다른 많은 서비스에서 공유하는 Kafka 브로커 자체의 리소스 사용량이 증가합니다. 우리는 코드와 아키텍처를 우선적으로 개선하기 위해 마지막 수단으로 이 옵션을 예약했습니다.

### 병렬 처리 소개

메시지를 순서대로 소비할 수는 있지만, 한 번에 여러 메시지를 사용하는 것을 막을 수는 없습니다.

우리는 검사기가 _일괄적으로_ 메시지를 소비하여 별도의 고루틴에서 각 메시지를 처리하도록 변경했습니다. 단점은 배치 중간에 프로세스가 중단되면 다시 수행해야 하는 작업이 더 많고 메모리 사용량이 약간 증가한다는 것입니다. 우리의 경우, 이 두 가지는 모두 수용 가능했습니다.

### head-of-line 차단 방지

일부 검사기에서 처리되는 일부 메시지는 다른 메시지보다 처리 시간이 훨씬 깁니다. 예를 들어, 한 계정/영역에는 다른 계정/영역보다 자산이 훨씬 더 많을 수 있습니다. 최악의 경우 이러한 메시지를 처리하는 데 평균 몇 초 또는 밀리초가 소요될 수 있습니다.

우리는 소비자 그룹과 체커를 '저속 차선'과 '빠른 차선'으로 분리하는 아주 간단한 접근 방식을 선택했습니다. Cloudflare에서는 메시지를 느리게 처리할지 빠르게 처리할지 빠르게 결정할 수 있었습니다. '고속 차선' 검사기는 느린 메시지를 발견하면 건너뛰게 됩니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4681CBHS27WJTHBKZAKJSS.jpg&w=715&h=318&f=webp&fit=cover&position=center)

이를 통해 문제가 해결되었습니다. 느린 메시지는 최소한의 지연으로 처리할 수 있는 전용 리소스와 시간이 확보되었고, 빠른 메시지는 평소의 빠른 속도로 진행될 수 있었습니다.

## 데이터베이스 쿼리 최적화

Cloudflare가 찾은 모든 인사이트는 Postgres 데이터베이스에 기록됩니다. 이는 Cloudflare의 체커가 인사이트 목록과 함께 호출하는 단일 API 엔드포인트에서 처리합니다. 구현 과정은 다음과 같습니다.
    
    
    for _, issue := range issues {
    	_, err = tx.Exec(ctx, `INSERT INTO table ... VALUES ($1, $2, ...) ON CONFLICT DO UPDATE ...`, ...)
    	if err != nil {
    		return err
    	}
    }

예리한 독자는 인사이트가 많은 경우, 이 코드가 인사이트마다 데이터베이스를 왕복한다는 것을 알 수 있습니다. 최대 500,000개의 관찰된 크기를 보면, 단일 API 호출로 인한 왕복, 쿼리, 트랜잭션은 50만 건에 달했습니다.

우리는 처음에 Postgres: COPY 임시 테이블에 대량 삽입을 위한 최적의 표준을 시도했습니다. 그러나 우리는 이러한 접근 방식으로 인해 Postgres 시스템 테이블이 비대해지는 것을 발견했습니다.

Cloudflare는 하이브리드 접근 방식으로 결정했습니다.

  * 이슈 수가 임계값 미만일 때 UNNEST 사용
  * 발행 수가 이 임계값을 초과하면 COPY 사용



이렇게 하면 엄청난 인사이트 세트를 위한 합리적으로 빠른 삽입(초)과 작은 인사이트 세트를 위한 더 빠른 삽입(밀리초)의 두 가지 장점이 제공되었습니다.

## API 제한 시간 초과 조사

규모를 조정하려고 시도하는 동안 내부 API에서 몇 가지 이상한 동작을 발견했습니다.

  * 많은 요청으로 인해 클라이언트 측 제한 시간 초과가 트리거되었습니다
  * 많은 검사기가 처리 시간의 20~90%를 단일 API 호출에 소비하고 있었습니다
  * 많은 양의 스캔을 트리거하면 처리량이 높게 시작하여 저하됩니다



이 모든 문제의 근본 원인은 **대기 시간** 이었습니다.

Cloudflare의 기본 데이터베이스는 오리건주 포틀랜드에 있습니다. 하지만 우리 API는 포틀랜드와 암스테르담 모두에서 액티브-액티브로 실행되고 있었습니다. 빛의 속도라고 해도 포틀랜드와 암스테르담 간의 왕복 대기 시간은 50밀리초입니다.

이 대기 시간으로 인해 암스테르담 API 인스턴스의 데이터베이스 쿼리는 훨씬 더 오래 걸렸고, 클라이언트 측 연결 풀의 연결은 열린 상태로 유지되었습니다. API에 대한 대량의 요청으로 연결 풀이 빠르게 소진되어 무료 연결을 기다리는 동안 제한 시간 초과가 발생했습니다. Cloudflare의 API 호출은 포틀랜드에서는 평균 10ms 이내에 완료되지만, 암스테르담에서는 거의 3초 내에 완료됩니다!

그런데 왜 메시지 처리량이 감소할까요? 각 검사기 프로세스에는 사용할 Kafka 스트림의 파티션 세트가 할당됩니다. Cloudflare의 API는 부하가 분산되었습니다. 우리는 프로세스의 수명 주기 내내 연결을 유지해 놓았으므로 일부 프로세스는 암스테르담 API에 연결되어 있고 다른 프로세스는 포틀랜드 API에 연결되어 있습니다. 포틀랜드와 링크된 파티션은 빠르게 처리되었지만, 암스테르담으로 향하는 프로세스에서 사용된 파티션은 그보다 뒤처져 있었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HWWDWTHZ7T3R6W61H15N.png&w=715&h=327&f=webp&fit=cover&position=center)

_Cloudflare 검사기 중 하나의 파티션별 카프카 지연(단일 소비자 그룹 내에서 처리를 기다리는 메시지 수)입니다. 이 경우에는 30개의 파티션이 있습니다. 정확히 15개의 파티션이 뒤처져 있는 것을 볼 수 있습니다(03/10 03:00경보다 0에 도달하거나 가까워지는 선). 이는 부하 분산 장치가 API 엔드포인트 간에 트래픽을 균등하게 분할하기 때문입니다._

이것은 간단한 수정이었습니다. 우리는 API를 [_활성-수동_](https://developers.cloudflare.com/load-balancing/load-balancers/common-configurations/#active---passive-failover)으로 전환하여 활성 API가 기본 데이터베이스를 따르도록 했습니다. 대기 시간 문제는 하룻밤 사이에 사라졌습니다.

## 스케줄러 재고하기

우리는 Kafka를 확장했습니다. 데이터베이스 쿼리를 최적화했습니다. API를 수정했습니다. 하지만 여전히 문제가 발생했습니다. 스캔 시간을 대략적으로 균일하게 분산시켜야 했습니다. Kafka 주제가 시간 기반 보존 정책을 사용하기 때문에 모든 스캔을 동시에 대기열에 넣는 것은 가능하지 않았습니다.

스케줄러는 스캔을 균일하게 분산하지 못했습니다. 주어진 시간에 트리거되는 스캔 수는 급증했고 예측할 수 없었습니다. 일주일 내내 특정 시점에서 수십만 건의 검사가 몇 분 이내에 서로 트리거되기도 합니다. 무슨 일이죠?

스케줄러는 고정된 반복 기간에 스캔을 트리거합니다. 의사 코드에서 스케줄러는 다음과 같은 모습입니다.
    
    
    Loop forever:
        Find accounts where last_scheduled_at + scanning frequency <= now
        For each account:
            Trigger scan for account
            Trigger scan for all zones in the account
            Update last_scheduled_at = now

Cloudflare는 데이터베이스의 다수의 계정에서 last_scheduled_at이 유사하다는 것을 빠르게 발견했으며, 이는 이러한 불균등의 원인이 되었습니다.

그러나 완벽하게 고른 분포라 하더라도 스캔 빈도를 늘리면 이 문제가 더욱 악화될 수 있습니다. 예를 들어, 스캔 빈도를 15일마다에서 7일마다로 변경하면 계정의 53%가 갑자기 스캔해야 합니다.

이 논리에는 또 다른 문제가 있었습니다. 일부 계정에는 매우 많은 수의 영역이 있습니다. 이러한 계정을 예약한 시점에는 모든 영역에 대한 스캔이 연쇄적으로 이루어졌습니다. 이로 인해 Kafka 파티션이 포화되어 훨씬 더 작은 계정을 검사하는 데 지연이 발생했습니다.

이 문제를 해결하기 위해 세 가지 주요 변경 사항을 적용했습니다.

  * 계정과 관계없이 구간을 예약합니다. 각 구간에는 고유한 last_scheduled_at 필드가 있습니다.
  * 기존 계정과 구간의 last_scheduled_at 시간을 무작위로 설정합니다.
  * 스캔 예약을 위한 적응형 속도 제한을 도입합니다.



영역을 독립적으로 예약하는 것은 대규모 계정의 문제를 해결하는 확실한 방법이었습니다. last_scheduled_at 시간을 무작위로 지정(그리고 이 프로세스 중에 스캔이 지연되지 않도록)하여 데이터베이스에 기존의 불균등성을 수정할 수 있었습니다.

적응형 레이트 리미팅은 약간 더 흥미롭습니다. 레이트 리미팅을 사용하면 스캔 주파수를 변경할 때 스캔 급증 문제를 해결할 수 있습니다. 예를 들어, 스캔 빈도를 7일마다로 늘리고자 하는데 계정이 5천만 개일 때, 레이트 리미팅을 83회/초로 설정하면 7일 동안 고르게 스캔할 수 있습니다.

하지만 계정이 천만 개 더 추가된다면 어떨까요? 이 경우 이 속도 제한으로 인해 모든 계정을 스캔하는 데 _8일_ 이 소요됩니다. 여기에서 _적응형_ 부분이 등장합니다. 전체 계정 및 영역 수와 스캔 빈도에 따라 30분마다 레이트 리미팅을 비동기식으로 재계산하는 것입니다. 이렇게 하면 수천 또는 수백만 개의 계정과 영역을 더 온보딩하는 경우에도 스캔을 정시에 계속할 수 있습니다.
    
    
    func computeRate(free, pro, biz, ent int64) rate.Limit {
       r := float64(free)/freeScanInterval.Seconds() +
          float64(pro)/proScanInterval.Seconds() +
          float64(biz)/bizScanInterval.Seconds() +
          float64(ent)/entScanInterval.Seconds()
    
    
       // Guard against zero counts. We always want to schedule at least one scan per second.
       if r < 1 {
          r = 1
       }
    
    
       // Increase rate limit beyond the 'perfect' value, to have a buffer in case of any downtime
       // or spikes in load.
       r *= rateLimitBufferFactor
    
    
       return rate.Limit(r)
    }

## 현재 Cloudflare의 위치

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW469VYB4FFXZ8WJTD15TBTZ.png&w=715&h=324&f=webp&fit=cover&position=center)

 _이러한 수정으로 시간 경과에 따른 검사기당 7일 이동 평균 처리량은 10배 이상 증가했습니다._

이러한 개선 이전에는 초당 약 10개의 스캔을 실행했습니다. 이 속도와 초당 100회의 스캔 처리량이라는 우리 목표의 차이는 큰 것 같았습니다. 우리는 Kafka 주제에 더 많은 리소스를 투입하고, Kafka 주제에 대해 더 많은 파티션을 추가하는 것에 대해 논의했으며, 심지어 전체 아키텍처를 폐기할 수도 있었습니다.

하지만 Cloudflare의 수정 사항으로 모든 것이 달라졌습니다. 현재, Security Insights는 피크 예약 시간에도 초당 120개 이상의 검사를 수행하며, 개선 목표의 10배를 초과하고 있습니다. 내부 API 시간이 더 이상 초과되지 않으며 Kafka 지연 메트릭이 훨씬 더 건강해 보입니다. 이러한 확장성 개선을 통해 _모든_ 무료 계정 및 영역에 대해 자동 스캔을 설정하고 모든 고객에 대해 스캔 빈도를 늘릴 수 있었습니다.

  * 무료: 7일마다
  * 프로 및 비즈니스 요금제: 3일마다
  * Enterprise: 매일



시스템 안정성이 향상되어 이전에는 생성하기 어려웠던 새로운 기능을 구축할 수 있다는 자신감이 생겼습니다. 세분화된 주문형 검색을 수행하는 기능을 추가했습니다. 이제 Cloudflare 계정, 영역, 인사이트 또는 인사이트 유형을 수동으로 다시 스캔할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3307 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487T27G7ZW0EH3AM50T7R5.png&w=715&h=477&f=webp&fit=cover&position=center)

_Cloudflare 대시보드의[ _보안 개요 페이지_](https://blog.cloudflare.com/security-overview-dashboard/) 에서 세분화된 주문형 스캔 시작_

우리는 아무것도 버리기 전에 기존 시스템을 깊이 이해하는 것이 중요하다는 교훈을 얻었습니다. 코드, SQL 쿼리, 로그, 메트릭(_특히_ 메트릭!)을 면밀히 살펴보면서 단순히 포드나 파티션을 추가하지 않고도 용량을 늘릴 수 있었습니다. 우리의 가정에 의문을 제기하고, 이상하게 보이는 메트릭을 파헤친 다음, 쉬운 방법(예: API 클라이언트 측 제한 시간 초과 증가)을 거부함으로써 우리는 더 안정적이고 탄력적인 시스템을 구축했습니다.

문제에 더 많은 리소스를 투입하는 것이 _때로는_ 해결책이 될 수도 있지만, Cloudflare에서는 문제를 해결하기 위해 엔지니어링하는 것이 중요하다고 믿습니다.

Security Insights 스캔은 모든 Cloudflare 요금제에서 기본적으로 활성화되어 있습니다. 지금 바로 [_Cloudflare 대시보드_](https://dash.cloudflare.com/?to=/:account/security-center) 에 로그인하여 보안 인사이트를 검토하고 관리하세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fscaling-security-scans%2F&t=%EB%B3%B4%EC%95%88%20%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8%20%ED%99%95%EC%9E%A5%3A%20%EA%B8%80%EB%A1%9C%EB%B2%8C%20%EC%8A%A4%EC%BA%90%EB%8B%9D%20%EC%9A%A9%EB%9F%89%EC%9D%84%2010%EB%B0%B0%20%EB%8A%98%EB%A6%AC%EB%8A%94%20%EB%B0%A9%EB%B2%95)[](https://x.com/intent/post?text=%EB%B3%B4%EC%95%88+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8+%ED%99%95%EC%9E%A5%3A+%EA%B8%80%EB%A1%9C%EB%B2%8C+%EC%8A%A4%EC%BA%90%EB%8B%9D+%EC%9A%A9%EB%9F%89%EC%9D%84+10%EB%B0%B0+%EB%8A%98%EB%A6%AC%EB%8A%94+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fscaling-security-scans%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fscaling-security-scans%2F)[](https://bsky.app/intent/compose?text=%EB%B3%B4%EC%95%88+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8+%ED%99%95%EC%9E%A5%3A+%EA%B8%80%EB%A1%9C%EB%B2%8C+%EC%8A%A4%EC%BA%90%EB%8B%9D+%EC%9A%A9%EB%9F%89%EC%9D%84+10%EB%B0%B0+%EB%8A%98%EB%A6%AC%EB%8A%94+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fscaling-security-scans%2F)[](https://mastodonshare.com/?text=%EB%B3%B4%EC%95%88+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8+%ED%99%95%EC%9E%A5%3A+%EA%B8%80%EB%A1%9C%EB%B2%8C+%EC%8A%A4%EC%BA%90%EB%8B%9D+%EC%9A%A9%EB%9F%89%EC%9D%84+10%EB%B0%B0+%EB%8A%98%EB%A6%AC%EB%8A%94+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fscaling-security-scans%2F)[](https://www.threads.net/intent/post?text=%EB%B3%B4%EC%95%88+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8+%ED%99%95%EC%9E%A5%3A+%EA%B8%80%EB%A1%9C%EB%B2%8C+%EC%8A%A4%EC%BA%90%EB%8B%9D+%EC%9A%A9%EB%9F%89%EC%9D%84+10%EB%B0%B0+%EB%8A%98%EB%A6%AC%EB%8A%94+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fscaling-security-scans%2F)

## 관련 태그

[Kafka](https://blog.cloudflare.com/ko-kr/tag/kafka/)[Postgres](https://blog.cloudflare.com/ko-kr/tag/postgres/)[보안 상태 관리](https://blog.cloudflare.com/ko-kr/tag/security-posture-management/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[응용 프로그램 보안](https://blog.cloudflare.com/ko-kr/tag/application-security/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
