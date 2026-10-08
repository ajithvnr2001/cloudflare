---
url: https://blog.cloudflare.com/ko-kr/r2-sql-aggregations/
title: R2 SQL\uc5d0\uc11c GROUP BY, SUM \ubc0f \uae30\ud0c0 \uc9d1\uacc4 \ucffc\ub9ac \uc9c0\uc6d0 \ubc1c\ud45c | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:46.635886+00:00
---

# R2 SQL에서 GROUP BY, SUM 및 기타 집계 쿼리 지원 발표 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/r2-sql-aggregations/

[블로그](https://blog.cloudflare.com/ko-kr/)

[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[SQL](https://blog.cloudflare.com/ko-kr/tag/sql/)+33개의 태그 더 보기

6개 태그6개 태그 보기

  * 게시물 태그
  * [R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[SQL](https://blog.cloudflare.com/ko-kr/tag/sql/)[데이터](https://blog.cloudflare.com/ko-kr/tag/data/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)[에지 컴퓨팅](https://blog.cloudflare.com/ko-kr/tag/edge-computing/)
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



[데이터](https://blog.cloudflare.com/ko-kr/tag/data/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)[에지 컴퓨팅](https://blog.cloudflare.com/ko-kr/tag/edge-computing/)

[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[SQL](https://blog.cloudflare.com/ko-kr/tag/sql/)[데이터](https://blog.cloudflare.com/ko-kr/tag/data/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)[에지 컴퓨팅](https://blog.cloudflare.com/ko-kr/tag/edge-computing/)

2025년 12월 18일

# R2 SQL에서 GROUP BY, SUM 및 기타 집계 쿼리 지원 발표

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marc Selwan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455H274J0ZYJ6K4KHKJT25.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/ko-kr/author/jerome/), [Nikita Lapkov](https://blog.cloudflare.com/ko-kr/author/nikita-lapkov/) 및 [Marc Selwan](https://blog.cloudflare.com/ko-kr/author/marc-selwan/)

10분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/r2-sql-aggregations/), [日本語](https://blog.cloudflare.com/ja-jp/r2-sql-aggregations/), [繁體中文](https://blog.cloudflare.com/zh-tw/r2-sql-aggregations/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/r2-sql-aggregations/).

![BLOG-3082 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45417DV5EYZK6BB5T2Z60B.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f395OPwzs7ry9Dx2N745uj17urq////////5+bz0dLuztT02uH66Ov37+zs////////6+z31tny0tr43uf+6/D78vHw////////8PL83OH32OL94+7/8Pb/9/b1////////9vn/4un83+r/6fX/9fz/+/z6////////+///6PD/5fL/7/z/+f/////+/////////v//7PX/6ff/8////f//////////////////7ff/6/n/9P///v//////)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

대량의 데이터를 처리할 때는 빠른 개요를 얻는 것이 도움이 되며, 이는 집계에서 SQL에서 제공하는 기능입니다. "GROUP BY 쿼리"로 알려진 집계는 조감도를 제공하므로 방대한 양의 데이터로부터 빠르게 인사이트를 얻을 수 있습니다.

이러한 이유로, Cloudflare에서는 [_R2 Data Catalog_](https://developers.cloudflare.com/r2/data-catalog/) 에 저장된 데이터에 대해 SQL 쿼리를 실행할 수 있는 Cloudflare의 서버리스 분산 분석 쿼리 엔진인 [_R2 SQL_](https://blog.cloudflare.com/r2-sql-deep-dive/) 에서의 집계 지원을 발표하게 되어 기쁘게 생각합니다. [_R2 SQL_](https://developers.cloudflare.com/r2-sql/) 사용자는 집계를 통해 데이터의 중요한 동향과 변화를 파악하고, 보고서를 생성하며, 로그에서 이상 징후를 찾아낼 수 있습니다.

이번 릴리스에서는 분석 워크로드의 기반인 이미 지원되는 필터 쿼리를 기반으로 하며 사용자는 [_Apache Parquet_](https://parquet.apache.org/) 파일의 건초더미에서 바늘을 찾을 수 있습니다.

이 게시물에서는 집계의 유틸리티와 특징을 살펴보고 R2 데이터 카탈로그에 저장된 방대한 양의 데이터에 대해 이러한 쿼리를 실행할 수 있도록 R2 SQL을 확장한 방법을 자세히 알아봅니다.

## 분석에서 집계의 중요성

집계 또는 “GROUP BY 쿼리”는 기본 데이터의 간단한 요약을 생성합니다.

일반적인 집계의 사용 사례는 보고서를 생성할 때입니다. 여러 국가와 일부 조직의 부서에 걸친 모든 매출에 대한 과거 데이터가 포함되어 있는 "매출"이라는 테이블을 생각해 보겠습니다. 이 집계 쿼리를 사용하면 부서별 매출액에 대한 보고서를 쉽게 생성할 수 있습니다.
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department

  
"GROUP BY" 문을 사용하면 테이블 행을 버킷으로 분할할 수 있습니다. 각 버킷에는 특정 부서에 해당하는 레이블이 있습니다. 버킷이 가득 차면 각 버킷의 모든 행에 대한 "합(값)"을 계산하여 해당 부서에서 수행한 총 매출을 알 수 있습니다.

일부 보고서의 경우 가장 많은 볼륨을 가진 부서에만 관심이 있을 수 있습니다. 이런 경우에 “ORDER BY” 문이 유용합니다.
    
    
    SELECT department, sum(value)
    FROM sales
    GROUP BY department
    ORDER BY sum(value) DESC
    LIMIT 10

여기에서는 쿼리 엔진에 모든 부서 버킷의 총량을 기준으로 내림차순으로 정렬하고 가장 큰 상위 10개만 반환하도록 지시합니다.

마지막으로, 이상을 필터링하는 데 관심이 있을 수 있습니다. 예를 들어, 보고서에 매출 합계가 5개보다 큰 부서만 포함시키고 싶을 수 있습니다. "HAVING" 문으로 이를 쉽게 수행할 수 있습니다.
    
    
    SELECT department, sum(value), count(*)
    FROM sales
    GROUP BY department
    HAVING count(*) > 5
    ORDER BY sum(value) DESC
    LIMIT 10

여기에서는 각 버킷에서 끝난 행 수를 계산하는 "count(*)"라는 새로운 집계 함수를 쿼리에 추가했습니다. 이는 각 부서의 매출 수와 직접적으로 일치하므로, 5개 이상의 행이 포함된 버킷만 남겨두도록 “HAVING” 문에 조건자를 추가했습니다.

## 집계에 대한 두 가지 접근 방식: 조만간 컴퓨팅

집계 쿼리에는 어디에도 저장되지 않은 열을 참조할 수 있다는 흥미로운 속성이 있습니다. "합(값)"을 고려해보세요. 이 열은 R2에 저장된 Parquet 파일에서 가져오는 "부서" 열과 달리 쿼리 엔진이 즉석에서 계산합니다. 이 미묘한 차이는 '합', '개수' 등의 집계를 참조하는 모든 쿼리를 두 단계로 분할해야 함을 의미합니다.

첫 번째 단계는 새 열을 계산하는 것입니다. "ORDER BY" 문을 사용하여 "count(*)" 열 기준으로 데이터를 정렬하거나 "HAVING" 문을 사용하여 데이터를 기준으로 행을 필터링하려면 이 열의 값을 알아야 합니다. "count(*)"와 같은 열의 값을 알면 나머지 쿼리 실행을 진행할 수 있습니다.

쿼리가 "HAVING" 또는 "ORDER BY"로 집계 함수를 참조하지 않지만 "SELECT"에서는 계속 사용하는 경우 트릭을 이용할 수 있습니다. 마지막까지 집계 함수의 값이 필요하지 않으므로 사용자에게 반환하기 직전에 부분적으로 집계 함수의 값을 계산하고 결과를 병합할 수 있습니다.

두 접근 방식의 주요 차이점은 집계 함수를 계산할 때입니다. 사용자가 필요로 하는 결과를 반복해서 구축합니다.

먼저, 저희가 "산란-수집 집계"라고 부르는 기술인 즉석 결과 작성에 대해 자세히 알아보겠습니다. 그런 다음 해당 기능을 기반으로 "HAVING" 및 "ORDER BY"와 같은 추가 계산을 집계 함수 위에서 실행할 수 있는 "집계 셔플링"을 도입합니다.

## 스캐터-게더 집계

'HAVING' 및 'ORDER BY'가 없는 집계 쿼리도 필터링 쿼리와 유사한 방식으로 실행할 수 있습니다. 필터 쿼리의 경우 R2 SQL은 쿼리 실행에서 하나의 노드를 코디네이터로 선택합니다. 이 노드가 쿼리를 분석하고 R2 데이터 카탈로그를 참조하여 어떤 Parquet 행 그룹에 쿼리와 관련된 데이터가 포함될 수 있는지 파악합니다. 각 Parquet 행 그룹은 단일 컴퓨팅 노드가 처리할 수 있는 비교적 작은 작업을 나타냅니다. 코디네이터 노드는 작업을 여러 worker 노드에 분산하고 결과를 수집하여 사용자에게 반환합니다.

집계 쿼리를 실행하기 위해 동일한 단계를 수행하고 worker 노드 간에 작은 작업을 분산합니다. 그러나 이번에는 "WHERE" 문의 조건자를 기반으로 행을 필터링하는 대신 작업자 **노드가 사전 집계도** 계산합니다.

사전 집계는 집계의 중간 상태를 나타냅니다. 이는 데이터의 하위 집합에 대해 부분적으로 계산된 집계 함수를 나타내는 불완전한 데이터 조각입니다. 여러 사전 집계를 병합하여 집계 함수의 최종 값을 계산할 수 있습니다. 집계 함수를 사전 집계로 나누면 집계 계산을 수평적으로 확장할 수 있으므로 Cloudflare 네트워크에서 사용할 수 있는 방대한 계산 리소스를 사용할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BPPXJKC47WPRR8TQZR5H.png&w=715&h=674&f=webp&fit=cover&position=center)

예를 들어 'count(*)'의 사전 집계는 단순히 데이터 하위 집합의 행 수를 나타내는 숫자입니다. 최종 '개수(*)'를 계산하는 것은 이들 숫자를 더하는 것만큼 쉽습니다. 'avg(value)'의 사전 집계는 'sum(value)'와 'count(*)'라는 두 숫자로 구성됩니다. "avg(value)"의 값은 모든 "sum(value)" 값을 더하고, 모든 "count(*)" 값을 더한 다음, 마지막으로 한 숫자를 다른 숫자로 나누어 계산할 수 있습니다.

작업자 노드가 사전 집계 컴퓨팅을 완료하면, 결과를 코디네이터 노드로 스트리밍합니다. 코디네이터 노드는 모든 결과를 수집하고 사전 집계에서 집계 함수의 최종 값을 계산하여 그 결과를 사용자에게 반환합니다.

## 셔플링, 분산-수집의 한계를 뛰어넘음

분산-수집은 코디네이터가 Workers의 작은 부분 상태를 병합하여 최종 결과를 계산할 수 있을 때 매우 효율적입니다. `SELECT sum(sales) FROM orders`와 같은 쿼리를 실행하면 코디네이터는 각 worker로부터 단일 숫자를 수신하여 합산합니다. 코디네이터의 메모리 풋프린트는 R2에 있는 데이터의 양과 관계없이 무시할 수 있습니다.

그러나 이 접근 방식은 쿼리가 집계 _결과_ 를 기반으로 정렬하거나 필터링해야 하는 경우 비효율적입니다. 판매량 기준 상위 2개 부서를 찾는 다음 쿼리를 고려해보세요.
    
    
    SELECT department, sum(sales)
    FROM sales
    GROUP BY department
    ORDER BY sum(sales) DESC
    LIMIT 2

글로벌 상위 2위를 올바르게 결정하려면 전체 데이터 세트에 걸쳐 모든 부서의 총 매출을 알아야 합니다. 데이터가 기본 Parquet 파일 간에 효과적으로 무작위로 분산되어 있으므로 특정 부서의 영업이 여러 직원에게 분산될 가능성이 높습니다. 부서에서 현지 상위 2개 목록에서 제외하면 모든 개별 worker의 매출이 낮지만, 총 매출을 보면 전 세계적으로 가장 높은 매출을 기록할 수 있습니다.

아래 다이어그램에는 이 쿼리에 대해 분산-수집 접근 방식이 작동하지 않는 이유가 나와 있습니다. "A 부서"는 글로벌 영업 리더이지만, 직원들에게 매출이 고르게 분포되어 있으므로 일부 현지 상위 2개 목록에 들지 못하며, 코디네이터가 폐기하게 됩니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463ZP69R3N5R25QG4E9T0V.png&w=715&h=674&f=webp&fit=cover&position=center)

따라서 글로벌 집계 기준으로 쿼리 결과를 정렬하는 경우, 코디네이터가 사전에 필터링된 Workers의 결과를 신뢰할 수 없습니다. 전역 합계를 계산하려면 _먼저_ _모든_ 작업자에게 모든 부서에 대한 합계 개수를 요청해야 합니다. IP 주소나 사용자 ID와 같이 카디널리티가 높은 열을 기준으로 그룹화하면 코디네이터가 강제로 수백만 개의 행을 수집하고 병합해야 하므로 단일 노드에서 리소스 병목 현상이 발생합니다.

이를 해결하려면 최종 집계가 수행되기 전에 특정 그룹에 대한 데이터를 같은 위치에 배치하는 방법인 **셔플링** 이 필요합니다.

### 집계 데이터 셔플링

무작위 데이터 분포 문제를 해결하기 위해 **셔플링 단계** 를 도입합니다. 작업자들은 결과를 코디네이터에게 전송하는 대신 서로 직접 데이터를 교환하여 그룹화 키를 기반으로 행을 배치합니다.

이 라우팅은 **결정론적 해시 파티셔닝** 에 의존합니다. 작업자가 행을 처리할 때 `GROUP BY` 열을 해시 처리하여 대상 작업자를 식별합니다. 이 해시는 결정론적이므로 클러스터의 모든 작업자는 특정 데이터를 보낼 위치에 독립적으로 합의합니다. "엔지니어링"이 Worker 5로 해시되면 모든 worker는 "엔지니어링" 행을 Worker 5로 라우팅한다는 것을 알게 됩니다. 중앙 레지스트리가 필요하지 않습니다.

아래 그림에 이러한 흐름이 나와 있습니다. Workers 1, 2, 3에서 "부서 A"가 어떻게 시작되는지 주목하세요. 해시 함수는 "부서 A"를 Worker 1에 매핑하므로 모든 Workers는 이러한 행을 동일한 대상으로 라우팅합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3082 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45ZD7B5A4ZRR0NG4HHEKV4.png&w=715&h=622&f=webp&fit=cover&position=center)

집계를 무작위로 섞으면 올바른 결과가 생성됩니다. 그러나 이러한 포괄적인 교환으로 인해 타이밍 종속성이 발생합니다. 작업자 3이 데이터 점유율 전송을 완료하기 전에 작업자 1에서 "부서 A"의 최종 합계 계산을 시작하면 결과가 완전하지 않게 됩니다.

이 문제를 해결하기 위해 Cloudflare는 **엄격한 동기화 장벽을** 적용합니다. 작업자가 나가는 데이터를 버퍼링하고 [_gRPC_](https://grpc.io/) 스트림을 통해 피어로 플러시하는 동안 코디네이터가 전체 클러스터의 진행 상황을 추적합니다. 모든 worker가 입력 파일 처리 및 셔플 버퍼 플러시가 완료되었음을 확인한 경우에만 코디네이터가 작업을 진행하라는 명령을 내립니다. 이 장벽은 다음 단계가 시작될 때 각 worker의 데이터 세트가 완전하고 정확함을 보장합니다.

### 로컬 마무리

동기화 장벽이 제거되면 모든 worker는 할당된 그룹에 대한 전체 데이터 세트를 보유하게 됩니다. 이제 Worker 1은 "부서 A"에 대한 100% 판매 레코드를 가지고 있으며 최종 합계를 확실하게 계산할 수 있습니다.

이를 통해 필터링 및 정렬과 같은 계산 논리를 코디네이터에게 부담을 주지 않고 worker에게 맡길 수 있습니다. 예를 들어, 쿼리에 `HAVING count(*) > 5`가 포함된 경우, 작업자는 집계 직후 이 기준을 충족하지 않는 그룹을 필터링할 수 있습니다.

이 단계가 끝나면 각 worker는 자신이 소유한 그룹에 대해 정렬되고 마무리된 결과 스트림을 생성합니다.

### 스트리밍 병합

퍼즐의 마지막 조각은 코디네이터입니다. 분산-수집 모델에서는 코디네이터가 전체 데이터 세트를 집계하고 정렬하는 값비싼 작업을 담당했습니다. 셔플링 모델에서는 역할이 바뀝니다.

Workers는 이미 최종 집계를 계산하고 로컬에서 정렬했으므로, 코디네이터는 **k-way 병합** 만 수행하면 됩니다. 모든 작업자에게 스트림을 열어주고 결과를 한 행씩 읽습니다. 각 worker에서 현재 행을 비교하고 정렬 순서에 따라 "승자"를 선택하고 사용자에게 전송되는 쿼리 결과에 추가합니다.

이 접근 방식은 특히 `LIMIT` 쿼리에 대해 강력합니다. 사용자가 상위 10개 부서를 요청하면 코디네이터는 상위 10개 항목을 찾을 때까지 스트림을 병합한 다음 즉시 처리를 중단합니다. 남은 수백만 개의 행을 로드하거나 병합할 필요가 없으므로 컴퓨팅 리소스를 과도하게 소비하지 않고도 작업 규모를 확장할 수 있습니다.

## 방대한 데이터세트를 처리할 수 있는 강력한 엔진

집계 기능이 추가된 [_R2 SQL_](https://developers.cloudflare.com/r2-sql/?cf_target_id=84F4CFDF79EFE12291D34EF36907F300) 은 데이터 필터링에 적합한 도구에서 벗어나 대규모 데이터세트의 데이터를 처리할 수 있는 강력한 엔진으로 탈바꿈합니다. 이는 스캐터-게더링 및 셔플링과 같은 분산 실행 전략을 구현하여 가능하며, Cloudflare의 대규모 컴퓨팅 및 네트워크의 규모를 사용하여 데이터가 있는 곳으로 컴퓨팅을 푸시할 수 있습니다. 

보고서를 생성하든, 대량의 로그에서 이상 징후를 모니터링하든, 단순히 데이터에서 트렌드를 파악하든, 복잡한 OLAP 인프라를 관리하거나 R2 외부로 데이터를 이동시키는 오버헤드 없이 Cloudflare의 개발자 플랫폼 내에서 모든 작업을 쉽게 수행할 수 있습니다.

## 지금 사용해 보세요

R2 SQL에서 집계 지원은 오늘부터 제공됩니다. 여러분은 R2 Data Catalog의 데이터로 이러한 새로운 함수를 어떻게 사용할지 기대됩니다.

  * **시작하기:** Cloudflare [_문서에서_](https://developers.cloudflare.com/r2-sql/sql-reference/) 집계 쿼리 실행에 대한 예제와 구문 가이드를 확인하세요.
  * **대화에 참여하기:** 질문이나 피드백이 있거나 만들고 있는 것을 공유하고 싶다면 Cloudflare [_개발자 Discord_](https://discord.com/invite/cloudflaredev)에 참여하세요.



이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fr2-sql-aggregations%2F&t=R2%20SQL%EC%97%90%EC%84%9C%20GROUP%20BY%2C%20SUM%20%EB%B0%8F%20%EA%B8%B0%ED%83%80%20%EC%A7%91%EA%B3%84%20%EC%BF%BC%EB%A6%AC%20%EC%A7%80%EC%9B%90%20%EB%B0%9C%ED%91%9C)[](https://x.com/intent/post?text=R2+SQL%EC%97%90%EC%84%9C+GROUP+BY%2C+SUM+%EB%B0%8F+%EA%B8%B0%ED%83%80+%EC%A7%91%EA%B3%84+%EC%BF%BC%EB%A6%AC+%EC%A7%80%EC%9B%90+%EB%B0%9C%ED%91%9C&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fr2-sql-aggregations%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fr2-sql-aggregations%2F)[](https://bsky.app/intent/compose?text=R2+SQL%EC%97%90%EC%84%9C+GROUP+BY%2C+SUM+%EB%B0%8F+%EA%B8%B0%ED%83%80+%EC%A7%91%EA%B3%84+%EC%BF%BC%EB%A6%AC+%EC%A7%80%EC%9B%90+%EB%B0%9C%ED%91%9C+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fr2-sql-aggregations%2F)[](https://mastodonshare.com/?text=R2+SQL%EC%97%90%EC%84%9C+GROUP+BY%2C+SUM+%EB%B0%8F+%EA%B8%B0%ED%83%80+%EC%A7%91%EA%B3%84+%EC%BF%BC%EB%A6%AC+%EC%A7%80%EC%9B%90+%EB%B0%9C%ED%91%9C&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fr2-sql-aggregations%2F)[](https://www.threads.net/intent/post?text=R2+SQL%EC%97%90%EC%84%9C+GROUP+BY%2C+SUM+%EB%B0%8F+%EA%B8%B0%ED%83%80+%EC%A7%91%EA%B3%84+%EC%BF%BC%EB%A6%AC+%EC%A7%80%EC%9B%90+%EB%B0%9C%ED%91%9C+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fr2-sql-aggregations%2F)

## 관련 태그

[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[SQL](https://blog.cloudflare.com/ko-kr/tag/sql/)[데이터](https://blog.cloudflare.com/ko-kr/tag/data/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)[에지 컴퓨팅](https://blog.cloudflare.com/ko-kr/tag/edge-computing/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
