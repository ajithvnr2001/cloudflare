---
url: https://blog.cloudflare.com/ko-kr/ecdysis-rust-graceful-restarts/
title: ecdysis\ub85c \uc624\ub798\ub41c \ucf54\ub4dc \uc0ac\uc6a9\ud558\uae30: Cloudflare\uc758 Rust \uc11c\ube44\uc2a4\ub97c \uc704\ud55c \uc6b0\uc544\ud55c \uc7ac\uc2dc\uc791 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:45.503236+00:00
---

# ecdysis로 오래된 코드 사용하기: Cloudflare의 Rust 서비스를 위한 우아한 재시작 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/ecdysis-rust-graceful-restarts/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Edge](https://blog.cloudflare.com/ko-kr/tag/edge/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)+55개의 태그 더 보기

8개 태그8개 태그 보기

  * 게시물 태그
  * [Edge](https://blog.cloudflare.com/ko-kr/tag/edge/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[애플리케이션 서비스](https://blog.cloudflare.com/ko-kr/tag/application-services/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)
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



[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[애플리케이션 서비스](https://blog.cloudflare.com/ko-kr/tag/application-services/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)

[Edge](https://blog.cloudflare.com/ko-kr/tag/edge/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[애플리케이션 서비스](https://blog.cloudflare.com/ko-kr/tag/application-services/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)

2026년 2월 13일

# ecdysis로 오래된 코드 사용하기: Cloudflare의 Rust 서비스를 위한 우아한 재시작

![Manuel Olguín Muñoz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MRZQBM4H5K19ZVS98WTD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Manuel Olguín Muñoz](https://blog.cloudflare.com/ko-kr/author/manuel-olguin-munoz/)

10분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/ecdysis-rust-graceful-restarts/) 및 [日本語](https://blog.cloudflare.com/ja-jp/ecdysis-rust-graceful-restarts/).

![BLOG-3121 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47APEZTY8GYKA04QBEVEE0.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f/97fLy4uft4+jy6e/37fHz6u7p/////v//6+702t/u1t3y3uX45+v27O3s////////6uz21NjvzNP01dz75Of57u7w////////7+7419jxztP3193/5+r+8/H1////////+PX75uPz4OD75+r/8vT/+vj6///////////9+PL29/T//P3////////+//////////////73///////////////////////////////4////////////////)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

> ecdysis | _ˈekdəsəs_ |
> 
> 명사
> 
> 오래된 피부를 제거하는 과정(파충류의 경우) 또는 바깥 쪽 표피를 제거하는 과정(곤충 등의 절지동물의 경우). 

연결 하나도 중단하지 않고 어떻게 전 세계에서 초당 수백만 건의 요청을 처리하는 네트워크 서비스를 업그레이드할 수 있을까요?

Cloudflare가 이 대규모 문제에 대한 솔루션 중 하나는 오랫동안 라이브 연결이 삭제되지 않고 새로운 연결이 거부되지 않는 정상적인 프로세스 재시작을 구현하는 Rust 라이브러리인 [**_ecdysis_**](https://github.com/cloudflare/ecdysis)였습니다. 

지난 달에는 이제 누구나 사용할 수 있도록**ecdysis를 오픈 소스로** 공개했습니다. ecdysis는 Cloudflare에서 5년 동안 프로덕션 환경에서 사용한 후, 핵심 Rust 인프라 전체를 다운타임 없이 업그레이드하고 Cloudflare의 [_글로벌 네트워크_](https://www.cloudflare.com/network/)를 통해 재시작할 때마다 수백만 건의 요청을 절약하는 것으로 입증되었습니다.

이러한 업그레이드, 특히 Cloudflare 네트워크의 규모에 있어서의 중요성은 아무리 강조해도 지나치지 않습니다. Cloudflare의 서비스는 대부분 트래픽 라우팅, [_TLS 수명 주기 관리_](https://www.cloudflare.com/application-services/solutions/certificate-lifecycle-management/), 방화벽 규칙 시행 등의 중요한 작업을 수행하면서도 지속적으로 운영되어야 합니다. 이러한 서비스 중 하나가 중단되면 잠시라도 연쇄적인 영향이 미칠 수 있습니다. 연결 끊김과 실패한 요청은 고객 성능 저하와 비즈니스 영향으로 빠르게 이어집니다.

이런 서비스에 업데이트가 필요하다면 보안 패치가 기대됩니다. 버그를 수정해야 하고 새로운 기능을 배포해야 합니다. 

이 순진한 접근 방식은 이전 프로세스가 중지될 때까지 기다렸다가 새 프로세스를 시작해야 하지만, 그럴 경우 연결이 거부되고 요청이 중단되는 시간 창이 생성됩니다. 단일 위치에서 초당 수천 건의 요청을 처리하는 서비스에 수백 개의 데이터 센터를 곱하면, 잠시 재시작하면 전 세계적으로 수백만 건의 요청이 실패합니다.

이 문제와 ecdysis가 당사의 솔루션이 되었던 방법, 그리고 여러분에게도 해결책이 될 수 있는 방법을 살펴보겠습니다. 

**링크** : [GitHub](https://github.com/cloudflare/ecdysis) **|** [crates.io](https://crates.io/crates/ecdysis) **|** [docs.rs](https://docs.rs/ecdysis)

### 단계적 재시작이 어려운 이유

앞서 언급했듯이 서비스를 재시작하는 순진한 접근 방식은 기존 프로세스를 중지하고 새 프로세스를 시작하는 것입니다. 이는 실시간 요청을 처리하지 않는 단순한 서비스에서는 잘 작동하지만, 라이브 연결을 처리하는 네트워크 서비스의 경우 이 접근 방식은 심각한 한계가 있습니다.

첫째, 나이브 접근 방식은 프로세스가 들어오는 연결을 수신 대기하지 않는 기간을 만듭니다. 이전 프로세스가 중지되면 수신 대기 소켓을 닫아 OS가 `ECONNREFUSED` 상태에서 새 연결을 즉시 거부합니다. 새 프로세스가 즉시 시작되더라도 밀리초든 초 단위든 항상 연결을 수락하지 않는 공간이 있습니다. 초당 수천 개의 요청을 처리하는 서비스의 경우 100ms의 격차도 수백 개의 연결이 끊기는 것을 의미합니다.

둘째, 기존 프로세스를 중지하면 이미 설정된 모든 연결이 종료됩니다. 대용량 파일을 업로드하거나 동영상을 스트리밍하는 클라이언트의 연결이 갑자기 끊깁니다. WebSocket 또는 gRPC 스트림과 같이 수명이 긴 연결은 작동 중에 종료됩니다. 고객 입장에서는 서비스가 사라질 뿐입니다.

이전 프로세스를 종료하기 전에 새 프로세스를 바인딩하면 이 문제를 해결하는 것으로 보이지만, 추가적인 문제가 발생하기도 합니다. 커널은 일반적으로 하나의 주소:포트 조합에 하나의 프로세스만 바인딩하도록 허용하지만, [_SO_REUSEPORT 소켓 옵션_](https://man7.org/linux/man-pages/man7/socket.7.html) 은 다중 바인딩을 허용합니다. 그러나 이는 프로세스 전환 중에 단계적 재시작에 적합하지 않은 문제를 일으킵니다.

`SO_REUSEPORT` 를 사용하면 커널은 각 프로세스마다 별도의 수신 대기 소켓을 생성하고 [_이 소켓 간에 새로운 연결의 부하를 분산합니다_](https://lwn.net/Articles/542629/). 연결에 대한 초기 `SYN` 패킷이 수신되면 커널은 이 패킷을 수신 대기 프로세스 중 하나에 할당합니다. 초기 핸드셰이크가 완료되면 프로세스가 이를 수락할 때까지 프로세스의 `accept()` 대기열에 있습니다. 그런 다음 프로세스가 이 연결을 수락하기 전에 종료되면 분리되어 커널에 의해 종료됩니다. GitHub의 엔지니어링 팀에서는 [_GLB Director 부하 분산 장치를 구축할 때_](https://github.blog/2020-10-07-glb-director-zero-downtime-load-balancer-updates/) 이 문제를 광범위하게 문서화했습니다.

### ecdysis의 작동 방식

ecdysis를 설계하고 구축하면서, 라이브러리의 4가지 핵심 목표를 확인했습니다.

  1. **오래된 코드는 업그레이드 후 완전히 차단할 수 있습니다**.
  2. **새 프로세스에는 초기화 유예 기간이 있습니다.**
  3. **초기화 중 새로운 코드가 충돌해도 괜찮으며** , 실행 중인 서비스에 영향이 없어야 합니다.
  4. **연쇄적인 실패를 피하기 위해 단일 업그레이드만 동시에 실행됩니다.**



ecdysis는 초창기부터 단계적 업그레이드를 지원해 온 NGINX가 선도한 접근 방식을 통해 이러한 요건을 충족합니다. 이 접근 방식은 간단합니다. 

  1. 부모 프로세스가 새로운 자식 프로세스를 `fork()`합니다.
  2. 자식 프로세스는 `execve()`로 새 버전의 코드로 자신을 대체합니다.
  3. 자식 프로세스는 부모 프로세스와 공유되는 네임드 파이프를 통해 소켓 파일 설명자를 상속합니다.
  4. 부모 프로세스는 종료하기 전에 자식 프로세스가 준비 신호를 보낼 때까지 기다립니다.



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3121 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46QD03TCDXHTGDDCMT2B4Z.png&w=695&h=750&f=webp&fit=cover&position=center)

결정적으로, 소켓은 전환 기간 내내 열려 있습니다. 자식 프로세스는 명명된 파이프를 통해 공유되는 파일 설명자로 부모로부터 수신 대기 소켓을 상속합니다. 하위 프로세스에서는 두 프로세스 모두 동일한 기본 커널 데이터 구조를 공유하므로 상위 프로세스가 신규 연결과 기존 연결을 계속 수락하고 처리할 수 있습니다. 하위 요소가 초기화를 완료하면, 상위 요소에 알리고 연결을 수락하기 시작합니다. 이 준비 완료 알림을 받으면, 상위 요소는 즉시 수신 대기 소켓의 사본을 닫고 기존 연결만 계속 처리합니다. 

이 프로세스는 적용 범위 격차를 제거하면서 하위에 안전한 초기화 기간을 제공합니다. 상위 계층과 하위 계층이 동시에 연결을 수락할 수 있는 짧은 시간 창이 있습니다. 이는 의도적인 것입니다. 상위 항목이 수락한 모든 연결은 비우기 프로세스의 일부로 완료될 때까지 단순히 처리됩니다.

이 모델은 필수 충돌 안전도 제공합니다. 만약 구성 오류로 인해 자식 프로세스가 초기화 과정에 실패하면, 그대로 종료됩니다. 상위 서버가 수신을 멈추지 않기 때문에 연결이 끊기지 않으며 문제가 해결되면 업그레이드를 다시 시도할 수 있습니다.

ecdysis는[ _Tokio_](https://tokio.rs) 및`systemd` 통합을 통해 비동기 프로그래밍에 대한 최고 수준의 지원을 통해 분기 모델을 구현합니다.

  * **Tokio 통합** : Tokio용 네이티브 비동기 스트림 래퍼. 상속된 소켓은 추가적인 글루 코드 없이도 리스너가 됩니다. 동기 서비스의 경우 ecdysis는 비동기 런타임 없이도 작업할 수 있도록 지원합니다.
  * **systemd-notify 지원** : `systemd_notify` 기능이 활성화되면, ecdysis가 systemd의 프로세스 수명 주기 알림과 자동으로 통합됩니다. 서비스 장치 파일에 `Type=notify-reload` 를 설정하면, systemd가 업그레이드를 올바로 추적할 수 있습니다.
  * **systemd 명명된 소켓** : `systemd_sockets` 기능을 사용하면 ecdysis가 systemd 활성화 소켓을 관리할 수 있습니다. 귀사의 서비스는 소켓으로 활성화될 수 있으며 동시에 단계적 재시작을 지원할 수 있습니다.



플랫폼 정보: ecdysis는 소켓 상속 및 프로세스 관리를 위해 Unix 전용 시스템 호출에 의존합니다. Windows에서는 작동하지 않습니다. 이것이 분기 접근법의 근본적인 한계입니다.

### 보안 고려 사항

단계적으로 재시작하려면 보안 고려 사항이 필요합니다. 분기 모델은 두 가지 프로세스 세대가 공존하는 환경을 만들고, 동일한 수신 대기 소켓과 잠재적으로 중요한 파일 설명자에 접근할 수 있게 됩니다.

ecdysis는 설계를 통해 이러한 문제를 해결합니다.

**Fork-then-exec** : ecdysis는 `fork()` 다음에 `execve()`가 이어지는 전통적인 유닉스 패턴을 따릅니다. 이렇게 하면 새로운 주소 공간, 새로운 코드, 상속된 메모리가 없는 깨끗한 상태에서 자식 프로세스를 시작할 수 있습니다. 명시적으로 전달된 파일 설명자만 경계를 통과합니다.

**명시적 상속** : 수신 대기 소켓과 통신 파이프만 상속됩니다. 다른 파일 설명자는 `CLOEXEC` 플래그를 통해 닫힙니다. 따라서 민감한 핸들이 우발적으로 누출되는 것을 방지할 수 있습니다.

**seccomp 호환성** : seccomp 필터를 사용하는 서비스는 `fork()` 및 `execve()`를 허용해야 합니다. 정상 재시작에는 이러한 syscall이 필요하므로 차단할 수 없습니다.

대부분의 네트워크 서비스의 경우 이러한 절충은 받아들일 수 있습니다. fork-exec 모델의 보안은 잘 알려져 있으며 NGINX, Apache 등의 소프트웨어에서 수십 년 동안 실전에서 테스트되었습니다.

### 코드 예시

실용적인 예를 살펴보겠습니다. 다음은 단계적 재시작을 지원하는 간소화된 TCP 에코 서버입니다.
    
    
    use ecdysis::tokio_ecdysis::{SignalKind, StopOnShutdown, TokioEcdysisBuilder};
    use tokio::{net::TcpStream, task::JoinSet};
    use futures::StreamExt;
    use std::net::SocketAddr;
    
    #[tokio::main]
    async fn main() {
        // Create the ecdysis builder
        let mut ecdysis_builder = TokioEcdysisBuilder::new(
            SignalKind::hangup()  // Trigger upgrade/reload on SIGHUP
        ).unwrap();
    
        // Trigger stop on SIGUSR1
        ecdysis_builder
            .stop_on_signal(SignalKind::user_defined1())
            .unwrap();
    
        // Create listening socket - will be inherited by children
        let addr: SocketAddr = "0.0.0.0:8080".parse().unwrap();
        let stream = ecdysis_builder
            .build_listen_tcp(StopOnShutdown::Yes, addr, |builder, addr| {
                builder.set_reuse_address(true)?;
                builder.bind(&addr.into())?;
                builder.listen(128)?;
                Ok(builder.into())
            })
            .unwrap();
    
        // Spawn task to handle connections
        let server_handle = tokio::spawn(async move {
            let mut stream = stream;
            let mut set = JoinSet::new();
            while let Some(Ok(socket)) = stream.next().await {
                set.spawn(handle_connection(socket));
            }
            set.join_all().await;
        });
    
        // Signal readiness and wait for shutdown
        let (_ecdysis, shutdown_fut) = ecdysis_builder.ready().unwrap();
        let shutdown_reason = shutdown_fut.await;
    
        log::info!("Shutting down: {:?}", shutdown_reason);
    
        // Gracefully drain connections
        server_handle.await.unwrap();
    }
    
    async fn handle_connection(mut socket: TcpStream) {
        // Echo connection logic here
    }

요점:

  1. **`build_listen_tcp`** 는 자식 프로세스에 상속될 리스너를 생성합니다.
  2. **`ready()`** 메서드는 초기화가 완료되었으며 안전하게 종료될 수 있음을 부모 프로세스에 알립니다.
  3. **`shutdown_fut.await`** 는 업그레이드나 중지가 요청될 때까지 차단됩니다. 이 Future는 업그레이드/재로드가 성공적으로 실행되었거나 셧다운 신호가 수신되었기 때문에 프로세스가 종료되어야 하는 경우에만 양보합니다.



이 프로세스에 `SIGHUP` 을 보내면 ecdysis는 다음과 같이 작동합니다.

_…상위 프로세스:_

  * 바이너리의 새 인스턴스를 분기시키고 실행합니다.
  * 수신 대기 소켓을 자식에게 전달합니다.
  * 자식이 `ready()`를 호출하기를 기다립니다.
  * 기존 연결을 드레이닝한 다음 종료합니다.



_...하위 프로세스:_

  * 부모와 동일한 실행 흐름에 따라 자신을 초기화하지만, ecdysis가 소유한 소켓은 상속되며 자식에 바인딩되지 않습니다.
  * `ready()`를 호출하여 상위 요소에 준비 상태를 알립니다.
  * 셧다운 또는 업그레이드 신호를 차단합니다.



### 대규모 생산

ecdysis는 2021년부터 Cloudflare에서 프로덕션 환경에서 실행되고 있습니다. 클라우드 연결성은 120여 개 국가의 330여 개 데이터 센터에 배포된 중요한 Rust 인프라 서비스를 구동합니다. 이러한 서비스에서는 하루에 수십억 건의 요청을 처리하며 보안 패치, 기능 릴리스, 구성 변경을 위해 자주 업데이트를 요구합니다.

ecdysis를 사용해 재시작할 때마다 수십만 개의 요청이 절약됩니다. 그렇지 않았다면 순진한 중지/시작 주기 동안에 삭제되었을 것입니다. 이를 통해 글로벌 사업장에서 수백만 개의 연결이 보존되고 고객의 안정성이 향상됩니다.

### ecdysis와 대안

단계적 재시작 라이브러리는 여러 생태계에 존재합니다. 올바른 도구를 선택하려면 ecdysis와 다른 솔루션을 사용해야 하는 경우를 이해하는 것이 중요합니다.

[**_tableflip_**](https://github.com/cloudflare/tableflip) 은 ecdysis에 영감을 준 Go 라이브러리입니다. 바둑 서비스에 대해 동일한 분기 및 상속 모델을 구현합니다. 바둑이 필요하다면 tableflip이 좋은 옵션입니다!

[**_shellflip_**](https://github.com/cloudflare/shellflip) 은 Cloudflare의 또 다른 Rust Graceful 재시작 라이브러리로, Rust 기반 프록시인 Oxy를 위해 특별히 설계되었습니다. Shellflip은 더 독단적입니다. 이는 systemd 및 Tokio를 가정하고 상위와 하위 간의 임의의 애플리케이션 상태를 전송하는 데 중점을 둡니다. 따라서 복잡한 상태 저장 서비스 또는 자체 소켓을 열 수조차 없는 적극적인 샌드박싱을 적용하려는 서비스에 적합하지만 간단한 경우에는 오버헤드가 추가되는 서비스에 적합합니다.

### 구축 시작

ecdysis는 5년 간 프로덕션 환경에서 강화된 단계적 재시작 기능을 Rust 생태계에 도입합니다. 바로 이 기술이 Cloudflare의 전역 네트워크에서 수백만 개의 연결을 보호하는 기술로, 오픈 소스로 누구나 이용할 수 있습니다!

API 참조, 일반적인 사용 사례에 대한 예제,`systemd` 와 통합하는 단계를 포함한 전체 문서는 [_docs.rs/ecdysis 에서_](https://docs.rs/ecdysis) 확인할 수 있습니다.

리포지토리의 [_예제 디렉토리_](https://github.com/cloudflare/ecdysis/tree/main/examples) 에는 TCP 리스너, Unix 소켓 리스너, systemd 통합을 보여주는 작동 코드가 있습니다.

라이브러리는 Argo Smart Routing & Orpheus 팀이 Cloudflare 전반 팀의 기여로 적극적으로 유지 관리합니다. 저희는 [_GitHub_](https://github.com/cloudflare/ecdysis)를 통한 기여, 버그 보고서 및 기능 요청을 환영합니다.

고성능 프록시를 구축하든, 수명이 긴 API 서버를 구축하든, 가동 시간이 중요한 모든 네트워크 서비스를 구축하든, ecdysis는 가동 중단 시간이 없는 운영의 기반을 제공할 수 있습니다.

시작하기:[ _github.com/cloudflare/ecdysis_](https://github.com/cloudflare/ecdysis)

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fecdysis-rust-graceful-restarts%2F&t=ecdysis%EB%A1%9C%20%EC%98%A4%EB%9E%98%EB%90%9C%20%EC%BD%94%EB%93%9C%20%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0%3A%20Cloudflare%EC%9D%98%20Rust%20%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%9A%B0%EC%95%84%ED%95%9C%20%EC%9E%AC%EC%8B%9C%EC%9E%91)[](https://x.com/intent/post?text=ecdysis%EB%A1%9C+%EC%98%A4%EB%9E%98%EB%90%9C+%EC%BD%94%EB%93%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Cloudflare%EC%9D%98+Rust+%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC+%EC%9C%84%ED%95%9C+%EC%9A%B0%EC%95%84%ED%95%9C+%EC%9E%AC%EC%8B%9C%EC%9E%91&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fecdysis-rust-graceful-restarts%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fecdysis-rust-graceful-restarts%2F)[](https://bsky.app/intent/compose?text=ecdysis%EB%A1%9C+%EC%98%A4%EB%9E%98%EB%90%9C+%EC%BD%94%EB%93%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Cloudflare%EC%9D%98+Rust+%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC+%EC%9C%84%ED%95%9C+%EC%9A%B0%EC%95%84%ED%95%9C+%EC%9E%AC%EC%8B%9C%EC%9E%91+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fecdysis-rust-graceful-restarts%2F)[](https://mastodonshare.com/?text=ecdysis%EB%A1%9C+%EC%98%A4%EB%9E%98%EB%90%9C+%EC%BD%94%EB%93%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Cloudflare%EC%9D%98+Rust+%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC+%EC%9C%84%ED%95%9C+%EC%9A%B0%EC%95%84%ED%95%9C+%EC%9E%AC%EC%8B%9C%EC%9E%91&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fecdysis-rust-graceful-restarts%2F)[](https://www.threads.net/intent/post?text=ecdysis%EB%A1%9C+%EC%98%A4%EB%9E%98%EB%90%9C+%EC%BD%94%EB%93%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Cloudflare%EC%9D%98+Rust+%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC+%EC%9C%84%ED%95%9C+%EC%9A%B0%EC%95%84%ED%95%9C+%EC%9E%AC%EC%8B%9C%EC%9E%91+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fecdysis-rust-graceful-restarts%2F)

## 관련 태그

[Edge](https://blog.cloudflare.com/ko-kr/tag/edge/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[애플리케이션 서비스](https://blog.cloudflare.com/ko-kr/tag/application-services/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
