---
url: https://blog.cloudflare.com/ko-kr/python-workers-advancements/
title: Python Workers Redux: \ube60\ub978 \ucf5c\ub4dc \uc2a4\ud0c0\ud2b8, \ud328\ud0a4\uc9c0, uv \uc6b0\uc120 \uc6cc\ud06c\ud50c\ub85c\uc6b0 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:47.519414+00:00
---

# Python Workers Redux: 빠른 콜드 스타트, 패키지, uv 우선 워크플로우 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/python-workers-advancements/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Python](https://blog.cloudflare.com/ko-kr/tag/python/)

2개 태그2개 태그 보기

  * 게시물 태그
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Python](https://blog.cloudflare.com/ko-kr/tag/python/)
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



[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Python](https://blog.cloudflare.com/ko-kr/tag/python/)

2025년 12월 8일

# Python Workers Redux: 빠른 콜드 스타트, 패키지, uv 우선 워크플로우

![Dominik Picheta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P5G8RRA9GKFZA6BYERZ1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Mike Nomitch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462B7XNRB3FQ030XK95Y0H.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dominik Picheta](https://blog.cloudflare.com/ko-kr/author/dominik/), [Hood Chatham](https://blog.cloudflare.com/ko-kr/author/hood/) 및 [Mike Nomitch](https://blog.cloudflare.com/ko-kr/author/mike-nomitch/)

12분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/python-workers-advancements/), [日本語](https://blog.cloudflare.com/ja-jp/python-workers-advancements/), [繁體中文](https://blog.cloudflare.com/zh-tw/python-workers-advancements/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/python-workers-advancements/).

![BLOG-2925 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SJ3N46YQKDZYJ6Q7M0S4.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////97e/z3eLu2+Lx4+n26+3y7uvp////////6u3119/w1eD04Oj56e317evs////////6O3509710eD53un96e/67e3w////////6/D+1eL61OT+4e7/7fP/8fH1////////8/j/3+v/3u3/6/b/9fn/9/b7/////////f//7fb/7fj/9/7//v////3/////////////+P//+P///////////////////////////P///P//////////////)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

_참고: 이 게시물은 AWS Lambda에 대한 추가 세부 정보와 함께 업데이트되었습니다._

작년에 저희는 Python 개발자가 단일 명령으로 Python을 지구상 모든 지역으로 배송하고 Workers 플랫폼을 활용할 수 [_있도록 Python Workers에_](https://blog.cloudflare.com/python-workers/) [_대한 기본_](https://workers.cloudflare.com/) 지원을 발표했습니다.

그 이후로 저희는 [_Workers에서의 Python 환경_](https://developers.cloudflare.com/workers/languages/python/) 을 훌륭하게 만들기 위해 열심히 노력해 왔습니다. Cloudflare는 플랫폼에 패키지 지원을 제공하는 데 집중해왔으며, 이는 이제 실현 가능하며 예외적으로 빠른 콜드 스타트와 Python 네이티브 개발자 경험을 통해 실현되었습니다.

이는 패키지가 Python Worker에 통합되는 방식이 변경되었음을 의미합니다. 저희는 제한된 기본 제공 패키지 세트를 제공하는 대신 이제 Python Workers를 지원하는 WebAssembly 런타임인 Pyodide에서 지원하는 모든 [_패키지_](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)를 지원합니다. 여기에는 모든 순수 Python 패키지뿐만 아니라 동적 라이브러리에 의존하는 많은 패키지가 포함됩니다. 또한 패키지를 쉽게 설치할 수 있도록 [_uv_](https://docs.astral.sh/uv/) 와 관련된 도구를 구축했습니다.

저희는 또한 전용 메모리 스냅샷을 구현하여 콜드 스타트 시간을 줄였습니다. 이 스냅샷을 사용하면 다른 서버리스 Python 벤더에 비해 속도가 크게 향상됩니다. 공통 패키지를 사용하는 콜드 스타트 테스트에서, Cloudflare Workers는 **SnapStart를 사용하지 않는** **AWS Lambda보다 2.4배** , **Google Cloud Run보다는 3배 더** 빠르게 시작합니다.

이 블로그 게시물에서는 Python Workers의 고유한 점을 설명하고 위에서 설명한 성공을 달성한 방법에 대한 몇 가지 기술적 세부 사항을 공유합니다. 하지만 먼저, Workers나 서버리스 플랫폼에 익숙하지 않으실 수 있는 분들, 특히 Python 배경을 이용하시는 분들을 위해 Workers를 사용하고 싶은 이유를 공유해 드리겠습니다.

### 2분 만에 전 세계에 Python 배포

Workers가 마법 같은 것을 느끼는 이유는 간단한 코드와 간편한 글로벌 배포입니다. 2분도 안 되는 빠른 콜드 스타트 기능으로 전 세계에 FastAPI 앱을 배포할 수 있는 방법을 보여드리는 것으로 시작하겠습니다.

FastAPI를 사용하는 간단한 Worker는 다음과 같이 몇 줄만으로 구현할 수 있습니다.
    
    
    from fastapi import FastAPI
    from workers import WorkerEntrypoint
    import asgi
    
    app = FastAPI()
    
    @app.get("/")
    async def root():
       return {"message": "This is FastAPI on Workers"}
    
    class Default(WorkerEntrypoint):
       async def fetch(self, request):
           return await asgi.fetch(app, request.js_object, self.env)

비슷한 것을 배포하려면 `uv` 와 `npm` 이 설치되어 있는지 확인한 후 다음을 실행하면 됩니다:
    
    
    $ uv tool install workers-py
    $ pywrangler init --template \
        https://github.com/cloudflare/python-workers-examples/03-fastapi
    $ pywrangler deploy

약간의 코드와 `pywrangler 배포`만으로도 [_125개국 330개 지역_](https://www.cloudflare.com/network/)으로 확장되는 Cloudflare의 에지 네트워크에 애플리케이션을 배포할 수 있습니다. 인프라나 확장을 걱정할 필요가 없습니다.

그리고 많은 사용 사례에서 Python Workers는 완전히 무료입니다. 무료 등급은 하루에 100,000건의 요청 및 호출당 10ms의 CPU 시간을 제공합니다. 자세한 내용은 [_문서의 가격 페이지_](https://developers.cloudflare.com/workers/platform/pricing/)를 확인하세요.

더 많은 예시를 확인하려면 [_GitHub에서 리포지터리를 확인하세요_](https://github.com/cloudflare/python-workers-examples). 계속 읽으면서 Python Workers에 대해 자세히 알아보세요.

### 그렇다면 Python Workers로 무엇을 할 수 있을까요?

이제 Worker가 있으므로 거의 모든 작업이 가능합니다. 코드를 작성하면 스스로 결정할 수 있습니다. Python Worker는 HTTP 요청을 수신하고 공용 인터넷의 모든 서버에 요청할 수 있습니다.

Cron 트리거를 설정하여 Worker가 정기적으로 실행되도록 할 수 있습니다. 또한, 더 복잡한 요구 사항이 있는 경우 [_Workflows for Python Workers_](https://blog.cloudflare.com/python-workflows/)를 사용하거나 [_Durable Objects_](https://developers.cloudflare.com/durable-objects/get-started/)를 사용하는 장기 WebSocket 서버 및 클라이언트를 사용할 수 있습니다.

다음은 Python Workers로 수행할 수 있는 작업의 예입니다.

  * [_Jinja와 같은 라이브러리를 사용하여 에지에서 HTML 템플릿을 렌더링하면서 서버에서 직접 동적 콘텐츠를 가져오세요_](https://github.com/cloudflare/python-workers-examples/tree/main/03-fastapi)
  * [ _서버의 응답을 수정합니다. 예를 들어, 요청된 콘텐츠에 따라 HTML에 opengraph 태그를 동적으로 삽입할 수 있습니다_](https://github.com/cloudflare/python-workers-examples/tree/main/11-opengraph)
  * [ _Durable Objects와 WebSocket을 사용하여 채팅방 구축하기_](https://github.com/cloudflare/python-workers-examples/tree/main/15-chatroom)
  * [ _WebSocket 연결의 데이터를 소비합니다._](https://github.com/cloudflare/python-workers-examples/tree/main/14-websocket-stream-consumer)
  * [_Pillow Python 패키지를 사용하여 이미지 생성_](https://github.com/cloudflare/python-workers-examples/tree/main/12-image-gen)
  * [ _Python 패키지의 API를 노출하는 작은 Python Worker를 작성한 다음, RPC를 사용하여 JavaScript Worker에서 액세스합니다_](https://github.com/cloudflare/python-workers-examples/tree/main/13-js-api-pygments)



### 더 빠른 패키지 콜드 스타트

Workers와 같은 서버리스 플랫폼은 필요할 때만 코드를 실행하므로 비용을 절감할 수 있습니다. 즉, Worker가 요청을 수신하지 않는 경우 Worker가 종료될 수 있으며 새 요청이 들어오면 다시 시작해야 합니다. 이로 인해 일반적으로 "콜드 스타트"라고 부르는 리소스 오버헤드가 발생합니다. 최종 사용자의 대기 시간을 최소화하려면 이러한 코드를 최대한 짧게 유지하는 것이 중요합니다.

표준 Python에서는 런타임을 부팅하는 데 비용이 많이 들고 저희가 Python Workers를 처음 구현할 때는 _런타임_ 이 빠르게 부팅되도록 하는 데 초점을 맞췄습니다. 하지만 이것으로는 충분하지 않다는 것을 곧 깨달았습니다. Python 런타임이 빠르게 부팅되더라도, 실제 시나리오에서 초기 시작에는 일반적으로 패키지에서 모듈을 로드하는 것이 포함되며, 불행히도 Python에서는 많은 인기 있는 패키지가 로드되는 데 몇 초가 걸릴 수 있습니다.

우리는 패키지의 로드 여부와 관계없이 빠르게 콜드 스타트를 시작했습니다.

현실적인 콜드 스타트 성능을 측정하기 위해 공통 패키지를 가져오는 벤치마크와 베어 Python 런타임을 사용하여 "hello world"를 실행하는 벤치마크를 설정했습니다. Standard Lambda는 [_런타임만 빠르게 시작할 수 있지만_](https://cold.picheta.me/#bare), 패키지를 가져오게 되면 콜드 스타트 시간이 늘어납니다. 패키지의 더 빠른 콜드 스타트를 위해 최적화하기 위해 Lambda에서 SnapStart를 사용할 수 있습니다(이 기능도 곧 링크된 벤치마크에 추가될 예정). 그러면 스냅샷 저장 비용과 복원 시마다 추가 비용이 발생합니다. Python Workers는 모든 Python Worker에 대해 메모리 스냅샷을 무료로 자동 적용합니다.

다음은 일반적인 세 가지 패키지([_httpx,_](https://www.python-httpx.org/) [_fastapi_](https://fastapi.tiangolo.com/) 및 [_pydatic_](https://docs.pydantic.dev/latest/))를 로드할 때의 평균 콜드 스타트 시간입니다.

플랫폼| 평균 콜드 스타트(초)  
---|---  
Cloudflare Python Workers| 1.027  
AWS Lambda(SnapStart 미사용)| 2.502  
Google 클라우드 Run| 3.069  
  
이 경우, **Cloudflare Python Workers는 SnapStart가 없는 AWS Lambda보다 2.4배, Google 클라우드 Run보다 3배 더 빠른 콜드 스타트가 가능합니다**. 우리는 메모리 스냅샷을 사용하여 이러한 낮은 콜드 스타트 수치를 달성했으며, 그 방법은 이후 섹션에서 설명할 것입니다.

Cloudflare에서는 이러한 벤치마크를 정기적으로 실행하고 있습니다. [_여기_](https://cold.picheta.me/#bare)에서 Cloudflare의 테스트 방법에 대한 최신 데이터와 자세한 정보를 확인하세요.

Cloudflare는 이러한 다른 플랫폼과 구조적으로 다릅니다. 즉, [_Workers는 격리 기반입니다_](https://developers.cloudflare.com/workers/reference/how-workers-works/). 따라서 우리의 목표는 높고, 제로 콜드 스타트의 미래를 계획하고 있습니다.

### uv와 통합된 패키지 도구

다양한 패키지 생태계는 Python을 놀랍게 만드는 큰 부분입니다. 그래서 Cloudflare는 Workers에서 최대한 쉽게 패키지를 사용하도록 노력했습니다.

탁월한 개발 경험을 얻기 위해서는 기존의 Python 툴링으로 작업하는 것이 최선의 방법이라는 것을 알게 되었습니다. 그래서 우리는 빠르고 성숙하며 Python 생태계에서 추진력을 얻고 있는 `uv` 패키지 및 프로젝트 관리자를 선택했습니다.

우리는 [_pywrangler_](https://github.com/cloudflare/workers-py#pywrangler)라고 하는 `uv를` 중심으로 한 자체 도구를 구축했습니다. 이 도구는 기본적으로 다음과 같은 작업을 수행합니다.

  * Worker의 pyproject.toml 파일을 읽어 파일에 지정된 종속성을 확인합니다
  * Worker 경로에 있는 `python_modules` 폴더에 종속성을 포함합니다.



Pywrangler는 `uv` 를 사용하여 Python Workers와 호환되는 방식으로 종속성을 설치하며, 로컬로 개발하거나 Workers를 배포할 때는 `wrangler` 를 사용합니다. 

사실상 이는 `pywrangler dev` 와 `pywrangler` `deploy` 를 실행하여 로컬에서 Worker를 테스트하고 배포하기만 하면 된다는 것을 의미합니다. 

### 유형 힌트

`pywrangler` 유형을 사용하여 Wrangler 구성에 정의된 모든 [_바인딩_](https://developers.cloudflare.com/workers/runtime-apis/bindings/)의 유형 힌트를 생성할 수 있습니다. 이러한 타입 힌트는 [_Pylance_](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 또는 최신 버전의 [_mypy_](https://mypy-lang.org/)에서 작동합니다.

타입을 생성하기 위해 [_wrangler types_](https://developers.cloudflare.com/workers/wrangler/commands/#types) 를 사용하여 타입스크립트 타입 힌트를 생성한 다음 타입스크립트 컴파일러를 사용하여 타입에 대한 추상 구문 트리를 생성합니다. 마지막으로, JS 개체의 반복자 필드 여부와 같은 TypeScript 힌트를 사용하여 Pyodide 외부 함수 인터페이스와 함께 작동하는 `mypy` 유형 힌트를 생성합니다.

### 스냅샷을 이용한 콜드 스타트 기간 단축

Python을 시작하는 것은 일반적으로 매우 느리고 Python 모듈을 가져오는 데 많은 양의 작업이 필요할 수 있습니다. 저희는 메모리 스냅샷을 사용하여 콜드 스타트 중에 Python 시작을 실행하지 않습니다.

Worker가 배포되면 Worker의 최상위 범위를 실행한 다음 메모리 스냅샷을 만들어 Worker와 함께 저장합니다. Worker를 위한 새로운 격리를 시작할 때마다 메모리 스냅샷이 복원되고 Worker는 요청을 처리할 준비가 되므로 준비로 Python 코드를 실행할 필요가 없습니다. 따라서 콜드 스타트 시간이 상당히 개선됩니다. 예를 들어, `fastapi`, `httpx` 및 `pydantic` 을 가져오는 Worker를 스냅샷 없이 시작하는 데 약 10초가 걸립니다. 스냅샷으로는 1초면 충분합니다.

Pyodide가 WebAssembly를 기반으로 구축되어 이를 가능하게 합니다. 런타임의 전체 선형 메모리를 쉽게 캡처하고 복원할 수 있습니다. 

#### 메모리 스냅샷과 엔트로피

WebAssembly 런타임은 보안을 위해 주소 공간 레이아웃 무작위화와 같은 기능을 필요로 하지 않으므로, 최신 운영 체제에서 메모리 스냅샷이 갖는 문제가 대부분 발생하지 않습니다. 네이티브 메모리 스냅샷과 마찬가지로 [_XKCD 난수 생성기를 사용하지 않으려면 시작 시 엔트로피를_](https://xkcd.com/221/) 신중하게 처리해야 합니다(Cloudflare는 [_실제 난수를 잘 처리하고_](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/) 있습니다).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2925 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW459DS22T0KYDPDJGGEAW3H.png&w=400&h=144&f=webp&fit=cover&position=center)

메모리를 스냅샷으로 생성하면, 의도치 않게 난수 시드 값을 고정할 수 있습니다. 이 경우 향후 '랜덤' 숫자에 대한 호출이 여러 요청에 걸쳐 동일한 값의 시퀀스를 일관되게 반환하게 됩니다.

파이썬은 시작 시 많은 엔트로피를 사용하므로 이를 피하는 것은 특히 어렵습니다. 여기에는 libc 함수 `getentropy()` 및 `getrandom()` 과 `/dev/random` 및 `/dev/urandom`에서 읽기가 포함됩니다. 이 모든 함수는 JavaScript의 관점에서 동일한 구현을 `공유합니다.` 기능을 제공합니다.

Cloudflare Workers에서 `crypto.getRandomValues()` 나중에 메모리 스냅샷 사용으로 전환할 수 있도록 시작 시에는 항상 비활성화되어 있었습니다. 안타깝게도 Python 인터프리터는 이 함수를 호출하지 않고는 부트스트랩할 수 없습니다. 또한 많은 패키지가 시작 시 엔트로피를 필요로 합니다. 이 엔트로피에는 기본적으로 두 가지 목적이 있습니다.

  * 해시 무작위화를 위한 해시 시드
  * 의사 난수 생성기용 시드



시작할 때 해시 무작위화를 수행하고, 특정 Worker마다 고정된 해시 시드를 보유하므로 비용을 감수합니다. Python에는 시작 후 해시 시드를 대체할 수 있는 메커니즘이 없습니다.

의사 난수 생성기(PRNG)의 경우 다음과 같은 접근 방식을 취합니다.

배포 시:

  1. 고정된 "포이즌 시드"를 PRNG에 시드한 다음 PRNG 상태를 기록합니다.
  2. 사용자 오류로 인해 배포가 실패하는 오버레이가 있는 PRNG를 호출하는 모든 API를 교체하세요.
  3. 사용자 코드의 최상위 범위를 실행합니다.
  4. 스냅샷을 캡처합니다.



런타임 시:

  1. PRNG 상태가 변경되지 않았음을 어설션합니다. 변경되었다면, 일부 메서드에 대한 오버레이를 잊어버린 것입니다. 내부 오류와 함께 배포가 실패합니다.
  2. 스냅샷을 복원한 후 핸들러를 실행하기 전에 난수 생성기를 다시 시드하세요.



이를 통해 Worker가 실행되는 동안에는 PRNG를 사용할 수 있지만, 초기화 및 사전 스냅샷 중에는 Workers에서 PRNG를 사용하지 못하도록 할 수 있습니다.

#### 메모리 스냅샷 및 WebAssembly 상태

WebAssembly에서 메모리 스냅샷을 생성할 때 추가적인 어려움이 발생합니다. 저장하는 메모리 스냅샷은 WebAssembly의 선형 메모리만으로 구성되지만, Pyodide WebAssembly 인스턴스의 전체 상태는 선형 메모리에 포함되어 있지 않습니다. 

이 메모리 외부에 두 개의 테이블이 있습니다.

하나의 테이블에 함수 포인터의 값이 저장됩니다. 기존 컴퓨터는 "본 노이만" 아키텍처를 사용하는데, 이는 코드가 데이터와 동일한 메모리 공간에 존재하므로 함수 포인터를 호출하는 것은 일부 메모리 주소로 점프하는 것을 의미합니다. WebAssembly는 코드가 별도의 주소 공간에 있는 'Harvard 아키텍처'입니다. 이는 WebAssembly에서 보장되는 대부분의 보안, 특히 WebAssembly에 주소 공간 레이아웃 무작위화가 필요하지 않은 이유 대부분의 핵심입니다. WebAssembly의 함수 포인터는 함수 포인터 테이블에 대한 색인입니다.

두 번째 테이블에는 Python에서 참조한 모든 JavaScript 개체가 보관됩니다. JavaScript 가상 머신이 JavaScript 개체에 대한 포인터를 직접 얻는 것을 금지하므로 JavaScript 개체는 메모리에 직접 저장할 수 없습니다. 대신 테이블에 저장되고 WebAssembly에서 테이블에 대한 인덱스로 표시됩니다.

스냅샷을 복원한 후에는 이 두 테이블이 모두 스냅샷을 캡처했을 때와 정확히 동일한 상태로 유지해야 합니다.

함수 포인터 테이블은 WebAssembly 인스턴스가 초기화될 때 항상 동일한 상태에 있으며, 우리가 동적 라이브러리, 즉 numpy와 같은 네이티브 파이썬 패키지를 불러올 때 동적 로더에 의해 업데이트됩니다. 

동적 로딩 처리 방법:

  1. 스냅샷을 생성하면, 로더를 패치해 동적 라이브러리의 로드 순서, 각 라이브러리에 대한 메타데이터가 할당된 메모리 주소, 재배치를 위한 함수 포인터 테이블 기본 주소를 기록합니다. 
  2. 스냅샷을 복원할 때는 동적 라이브러리를 같은 순서로 다시 로드하고 패치된 메모리 할당자를 사용하여 메타데이터를 같은 위치에 배치합니다. 우리는 함수 포인터 테이블의 현재 크기가 우리가 동적 라이브러리에 대해 기록한 함수 포인터 테이블의 기본과 일치하는지 확인합니다.



이 모든 것은 스냅샷을 복원한 후에도 각 함수 포인터가 스냅샷을 만들 때와 동일한 의미를 갖도록 보장합니다.

JavaScript 참조를 처리하기 위해 구현한 시스템은 상당히 제한적이었습니다. JavaScript 개체가 일련의 속성 액세스를 통해 globalThis에서 액세스할 수 있는 경우, Cloudflare는 해당 속성 액세스를 기록하고 스냅샷을 복원할 때 재생합니다. 이러한 방식으로 액세스할 수 없는 JavaScript 개체에 대한 참조가 있는 경우 Worker를 배포할 수 없습니다. 이는 Pyodide를 지원하는 기존의 모든 Python 패키지를 처리하기에 충분하며, 다음과 같은 최상위 수준의 가져오기를 수행합니다.
    
    
    from js import fetch

### 샤딩을 이용한 콜드 스타트 빈도 줄이기

Python Workers에 대한 성능 전략의 또 다른 중요한 특징은 샤딩입니다. [_여기_](https://blog.cloudflare.com/eliminating-cold-starts-2-shard-and-conquer/)에서 이를 구현하는 과정에 대한 자세한 설명을 확인할 수 있습니다. 간단히 말해, 이전에는 새 인스턴스를 시작하는 것을 선택했다면, 지금은 요청을 기존 Worker 인스턴스로 라우팅했습니다.

실제로 Python Workers에는 Sharding이 먼저 활성화되었고 이를 위한 훌륭한 테스트베드임이 입증되었습니다. 콜드 스타트는 JavaScript보다 Python에서 훨씬 더 비싸므로 요청이 이미 실행 중인 격리로 라우팅되는지 확인하는 것이 특히 중요합니다.

### 이제부터 어디로 가야 할까요?

이것은 시작에 불과합니다. Cloudflare는 Python Workers를 개선하기 위해 다양한 계획을 갖고 있습니다.

  * 더 개발자 친화적인 도구
  * Cloudflare의 격리 아키텍처를 활용하여 훨씬 더 빠른 콜드 스타트
  * 더 많은 패키지 지원
  * 네이티브 TCP 소켓, 네이티브 WebSockets 등의 바인딩 지원



Python Workers에 대해 자세히 알아보려면 [_여기_](https://developers.cloudflare.com/workers/languages/python/)에서 제공되는 문서를 확인하세요. 도움을 받으려면 [_Discord_](https://discord.cloudflare.com/)에 꼭 가입하세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpython-workers-advancements%2F&t=Python%20Workers%20Redux%3A%20%EB%B9%A0%EB%A5%B8%20%EC%BD%9C%EB%93%9C%20%EC%8A%A4%ED%83%80%ED%8A%B8%2C%20%ED%8C%A8%ED%82%A4%EC%A7%80%2C%20uv%20%EC%9A%B0%EC%84%A0%20%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C%EC%9A%B0)[](https://x.com/intent/post?text=Python+Workers+Redux%3A+%EB%B9%A0%EB%A5%B8+%EC%BD%9C%EB%93%9C+%EC%8A%A4%ED%83%80%ED%8A%B8%2C+%ED%8C%A8%ED%82%A4%EC%A7%80%2C+uv+%EC%9A%B0%EC%84%A0+%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C%EC%9A%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpython-workers-advancements%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpython-workers-advancements%2F)[](https://bsky.app/intent/compose?text=Python+Workers+Redux%3A+%EB%B9%A0%EB%A5%B8+%EC%BD%9C%EB%93%9C+%EC%8A%A4%ED%83%80%ED%8A%B8%2C+%ED%8C%A8%ED%82%A4%EC%A7%80%2C+uv+%EC%9A%B0%EC%84%A0+%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C%EC%9A%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpython-workers-advancements%2F)[](https://mastodonshare.com/?text=Python+Workers+Redux%3A+%EB%B9%A0%EB%A5%B8+%EC%BD%9C%EB%93%9C+%EC%8A%A4%ED%83%80%ED%8A%B8%2C+%ED%8C%A8%ED%82%A4%EC%A7%80%2C+uv+%EC%9A%B0%EC%84%A0+%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C%EC%9A%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpython-workers-advancements%2F)[](https://www.threads.net/intent/post?text=Python+Workers+Redux%3A+%EB%B9%A0%EB%A5%B8+%EC%BD%9C%EB%93%9C+%EC%8A%A4%ED%83%80%ED%8A%B8%2C+%ED%8C%A8%ED%82%A4%EC%A7%80%2C+uv+%EC%9A%B0%EC%84%A0+%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C%EC%9A%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpython-workers-advancements%2F)

## 관련 태그

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Python](https://blog.cloudflare.com/ko-kr/tag/python/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
