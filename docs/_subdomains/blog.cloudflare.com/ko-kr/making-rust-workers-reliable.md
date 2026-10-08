---
url: https://blog.cloudflare.com/ko-kr/making-rust-workers-reliable/
title: Rust Workers\ub97c \uc548\uc815\uc801\uc73c\ub85c \ub9cc\ub4e4\uae30: wasm-bindgen\uc5d0\uc11c\uc758 \ud328\ub2c9 \ubc0f \uc911\ub2e8 \ubcf5\uad6c | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:34:40.068684+00:00
---

# Rust Workers를 안정적으로 만들기: wasm-bindgen에서의 패닉 및 중단 복구 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/making-rust-workers-reliable/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ko-kr/tag/rust-workers/)+88개의 태그 더 보기

11개 태그11개 태그 보기

  * 게시물 태그
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ko-kr/tag/rust-workers/)[WASM](https://blog.cloudflare.com/ko-kr/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ko-kr/tag/webassembly/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)
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



[WASM](https://blog.cloudflare.com/ko-kr/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ko-kr/tag/webassembly/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ko-kr/tag/rust-workers/)[WASM](https://blog.cloudflare.com/ko-kr/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ko-kr/tag/webassembly/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)

2026년 4월 22일

# Rust Workers를 안정적으로 만들기: wasm-bindgen에서의 패닉 및 중단 복구

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/ko-kr/author/guy-bedford/), [Hood Chatham](https://blog.cloudflare.com/ko-kr/author/hood/) 및 [Logan Gatlin](https://blog.cloudflare.com/ko-kr/author/logan-gatlin/)

11분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/making-rust-workers-reliable/), [日本語](https://blog.cloudflare.com/ja-jp/making-rust-workers-reliable/), [繁體中文](https://blog.cloudflare.com/zh-tw/making-rust-workers-reliable/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/making-rust-workers-reliable/).

![BLOG-3145 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HQEZP84STFXFD0H3EBY7.png&w=2048&h=1152&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////88O7x3uLt3eXz6e758/L19u/r//////7+5Ofzx9XuxNb01uP66ez38u7t//////7/2OH2rsjwqMj2w9j93+f77+3x////////1eL6psf0nsX6vdf/3uj/8PD2////////4Oz/t9T6sdT/y+P/5/H/9/f7////////8fr/1en/0ur/5Pb/9v7/////////////////7fr/7Pz/+P//////////////////////9///9v//////////////)

[_Rust Workers_](https://developers.cloudflare.com/workers/languages/rust/)는 Cloudflare Workers 플랫폼에서 Rust를 WebAssembly로 컴파일하여 실행되지만, 저희가 파악한 것처럼 WebAssembly에는 어려운 점이 있습니다. 패닉이나 예기치 않은 중단으로 인해 문제가 발생하면 런타임이 정의되지 않은 상태로 남을 수 있습니다. Rust Workers 사용자의 경우, 패닉이 인스턴스를 중독시키고 일정 기간 동안 Worker를 브릭으로 만들기도 하면 역사적으로 치명적이었습니다.

이러한 문제를 감지하고 완화할 수는 있었지만, Rust Worker가 예기치 않게 실패하고 다른 요청도 함께 실패할 가능성은 조금 있었습니다. 하나의 요청에 영향을 미치는 Worker에서 처리되지 않은 Rust 중단은 형제 요청에 영향을 미치는 더 광범위한 실패로 확대되거나 새로운 수신 요청에 계속 영향을 미칠 수 있습니다. 이 문제의 근본 원인은 Rust Workers가 의존하는 Rust와 JavaScript의 바인딩을 생성하는 핵심 프로젝트인 wasm-bindgen과 내장 복구 시맨틱의 부재에 있었습니다.

이 게시물에서는 중단으로 인해 발생하는 이 샌드박스 포이즈닝을 해결하는 Rust Workers의 최신 버전에서 포괄적인 Wasm 오류 복구를 처리하는 방법을 공유합니다. 이 작업은 wasm-bindgen 조직 내의 협업의 일환으로 [_wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen) 에 다시 기여되었으며, 이는 [_작년에 결성된_](https://blog.rust-lang.org/inside-rust/2025/07/21/sunsetting-the-rustwasm-github-org/) 것입니다. 첫 번째로 `패닉 해제` 지원이 있습니다. 이는 실패한 단일 요청이 다른 요청을 방해하지 못하도록 보장합니다. 두 번째는 Wasm의 Rust 코드가 중단 후 다시 실행되지 않도록 보장하는 중단 복구 메커니즘입니다. 

## 초기 복구 완화

이 영역에서 안정성을 해결하기 위한 초기 시도는 프로덕션 Rust Workers에서의 Rust 패닉 및 중단으로 발생하는 장애를 이해하고 억제하는 데 중점을 두었습니다. 저희는 Worker 내에서 실패 상태를 추적하고 후속 요청을 처리하기 전에 전체 애플리케이션 재초기화를 트리거하는 사용자 지정 Rust 패닉 핸들러를 도입했습니다. JavaScript 측에서 이를 위해서는 모든 진입점이 일관되게 캡슐화되도록 프록시 기반 간접 참조를 사용하여 Rust-JavaScript 호출 경계를 래핑해야 했습니다. 또한 장애가 발생한 후 WebAssembly 모듈을 올바르게 다시 초기화할 수 있도록 생성된 바인딩을 대상에 맞게 수정했습니다.

이 접근 방식은 맞춤형 JavaScript 로직에 의존했지만, 안정적인 복구를 달성할 수 있고 실제로 나타나는 지속적인 장애 모드를 제거할 수 있음을 입증했습니다. 이 솔루션은 버전 0.6부터 모든 작업자 사용자에게 기본적으로 제공되었으며, 이후 섹션에서 설명할 보다 일반적이고 업스트림된 중단 복구 메커니즘의 기반을 마련했습니다.

## WebAssembly 예외 처리로 `panic=unwind` 구현

위에서 설명한 중단 복구 메커니즘은 Worker가 장애에서 생존할 수 있도록 하지만, 전체 애플리케이션을 다시 초기화하여 이를 수행합니다. 상태 비저장 요청 처리기의 경우 이는 괜찮습니다. 그러나 Durable Objects와 같이 메모리에 의미 있는 상태를 유지하는 워크로드의 경우 재초기화는 해당 상태를 완전히 삭제하는 것을 의미합니다. 하나의 요청에서 하나의 패닉이 발생해도 동시에 발생하는 다른 요청에서 사용 중인 인메모리 상태가 지워질 수 있습니다.

대부분의 네이티브 Rust 환경에서는 패닉 상태를 해결하여 소멸자가 실행되고 프로그램이 상태를 잃지 않고 복구할 수 있도록 합니다. WebAssembly의 경우 기존 방식과 매우 달랐습니다. `wasm32-unknown-unknown`을 통해 Wasm으로 컴파일된 Rust는 기본적으로 `panic=abort`로 설정되어 있으므로, Rust Worker 내부에서 패닉이 발생하면 `unreachable` 명령과 함께 갑자 트랩되어 Wasm이 `WebAssembly.RuntimeError`와 함께 JS로 종료됩니다.

인스턴스 상태를 삭제하지 않고 패닉 상태에서 복구하려면, wasm-bindgen에서 `panic=unwind` 지원이 `wasm32-unknown-unknown`에 필요했으며, 이는 2023년에 광범위한 엔진 지원을 얻은 WebAssembly 예외 처리 제안으로 인해 가능해졌습니다.

`RUSTFLAGS='-Cpanic=unwind' cargo build -Zbuild-std`로 컴파일하는 것으로 시작합니다. 이는 해제 지원으로 표준 라이브러리를 다시 빌드하고 적절하게 패닉을 해제하는 코드를 생성합니다. 예:
    
    
    struct HasDropA;
    struct HasDropB;
    extern "C" {
        fn imported_func();
    }
    
    fn some_func() {
        let a = HasDropA;
        let b = HasDropB;
        imported_func();
    }

다음과 같이 WebAssembly로 컴파일합니다.
    
    
    try
      call <imported_func>
    catch_all
      call <drop_b>
      call <drop_a>
      rethrow
    end
    call <drop_b>
    call <drop_a>

이렇게 하면 `imported_func()` 가 패닉 상태에 빠지더라도 소멸자가 계속 실행됩니다. 마찬가지로, `std::panic::catch_unwind(|| some_func())은` 다음과 같이 컴파일됩니다.
    
    
    try
      call <some_func>
      ;; set result to Ok(return value)
    catch
      try
        call <std::panicking::catch_unwind::cleanup>
        ;; set result to Err(panic payload)
      catch_all
        call <core::panicking::cannot_unwind>
        unreachable
      end
    end

이를 처음부터 작동하게 하려면 Wasm-bindgen 툴체인을 몇 가지 변경해야 했습니다. WebAssembly 파서 Walrus가 시도/캐치 명령을 처리하는 방법을 모르므로 우리가 해당 명령에 대한 지원을 추가했습니다. 설명자 인터프리터는 예외 처리 블록이 포함된 코드를 평가하는 방법도 알려야 했습니다. 이 시점에서 `Panic=unwind 명령으로 전체` 애플리케이션을 빌드할 수 있습니다.

마지막 단계에서는 Rust-JavaScript 경계에서 패닉을 포착하고 JavaScript `PanicError` 예외로 표시하도록 wasm-bindgen으로 생성된 내보내기를 수정했습니다. 한 가지 미묘하게도, Rust는 `extern "C"` 함수를 통해 해제할 때 외부 예외를 포착하고 중단하므로 경계를 넘어 명시적으로 해제를 허용하려면 익스포트에 `extern "C-unwind"`를 표시해야 했습니다. 퓨처의 경우 패닉은 `PanicError와` 함께 JavaScript `Promise를` 거부합니다.

클로저는 `panic=unwind`로 구축했을 때만 `UnwindSafe`를 확인하는 새로운 `MaybeUnwindSafe` 트레이트를 통해 해제 안전성이 제대로 확인되었는지 확인하기 위해 특별한 주의가 필요했습니다. 하지만 이로 인해 문제가 빠르게 노출되었습니다. 많은 클로저가 언와인드 후에도 남아 있는 참조를 캡처하므로 본질적으로 언와인드-안전하지 않습니다. 컴파일러를 만족시키기 위해 사용자가 `AssertUnwindSafe` 내에서 클로저를 잘못 래핑하도록 유도하는 상황을 피하고자, 언와인드 안전성을 보장할 수 없는 경우 언와인딩 대신 패닉으로 종료되는 `Closure::new_aborting` 변형을 추가했습니다.

패닉 해제 활성화 시:

  * 내보낸 Rust 함수에서 패닉 상태가 wasm-bindgen에 포착됨
  * JavaScript에 PanicError 예외로 패닉이 표면화됨
  * 비동기 내보내기는 PanicError와 함께 반환된 프라미스를 거부합니다
  * Rust 소멸자가 올바르게 실행됨
  * WebAssembly 인스턴스는 여전히 유효하고 재사용 가능합니다.



이러한 접근법에 대한 자세한 내용과 wasm-bindgen에서 사용하는 방법은 [_Wasm Bindgen: 캐칭 패닉_](https://wasm-bindgen.github.io/wasm-bindgen/reference/catch-unwind.html)의 최신 가이드 페이지에서 다룹니다.

## 복구 중단

`panic=unwind` 지원에도 불구하고 중단은 여전히 발생하며, 메모리 부족 오류가 일반적인 원인 중 하나입니다. 중단으로는 해제할 수 없으므로 상태가 복구될 가능성은 전혀 없지만, 최소한 후속 요청에 대한 잘못된 상태 오류를 방지하기 위해 향후 작업을 위한 중단을 감지하고 복구할 수는 있습니다.

긴급 상황 해제 지원으로 인해 중단 복구에 대한 새로운 문제가 생겼습니다. Wasm으로부터 오류를 수신하면 외부 오류 `'C-unwind' 외부에서` 발생한 오류인지, 아니면 진짜 중단 오류인지 알 수 없습니다. 중단은 WebAssembly에서 다양한 형태를 취할 수 있습니다.

우리는 이 문제를 기술적으로 해결하기 위해 모든 오류를 확실히 중단되도록 표시하거나 확실히 해제할 수 있는 모든 오류로 표시하는 두 가지 옵션이 있었습니다. 둘 다 가능했지만 우리는 후자를 선택했습니다. 외부 예외 처리는 이미 원시 WAT 수준(WebAssembly 텍스트 형식) 예외 처리 지침을 직접 사용하고 있었으므로, 외부 예외에 대한 예외 태그를 구현하여 해제 안전하지 않은 예외를 중단시키는 것과 구분하는 것이 더 쉽다는 것을 발견했습니다.

WebAssembly 예외 처리의 이 `Exception.Tag` 기능 덕분에 복구 가능한 오류와 복구 불가능한 오류를 명확하게 구분할 수 있는 기능을 통해 새로운 중단 핸들러와 중단 재진입 보호 기능을 모두 통합할 수 있었습니다.  
  
새로운 중단 후크인 `set_on_abort`는 초기화 시 플랫폼 임베딩의 필요에 따라 복구되는 핸들러를 연결하는 데 사용할 수 있습니다.

유효하지 않은 실행 상태를 피하려면 패닉 및 중단 처리를 강화하는 것이 중요합니다. WebAssembly는 딥 인터리브 처리된 콜 스택을 허용하며, Wasm은 JavaScript를 호출하고, JavaScript는 임의의 깊이에서 Wasm에 다시 들어갈 수 있으며, 이와 함께 동일한 인스턴스에서 여러 작업이 작동할 수 있습니다. 이전에는 하나의 작업이나 중첩 스택에서 중단이 발생해도 JS를 통한 상위 스택이 무효화되도록 보장되지 않아 정의되지 않은 동작을 초래했습니다. 실행 모델을 보장할 수 있으려면 주의가 필요했으며, 이 분야에서의 기여는 계속되고 있습니다.

중단은 절대 이상적이지 않고 실패 시 재초기화는 절대적으로 최악의 시나리오이지만, 마지막 방어선으로 중요 오류 복구를 구현하면 실행의 정확성이 보장되고 향후 작업이 성공할 수 있습니다. 유효하지 않은 상태는 지속되지 않으므로 단일 오류가 여러 번의 오류로 이어지지 않습니다.

## 확장: abort Reinitialization for Wasm-bindgen 라이브러리

이 작업을 진행하는 동안, 저희는 이것이 wasm-bindgen으로 구축된 JS에서 사용하는 라이브러리에 대해 일반적인 문제이며 복구를 수행할 수 있도록 중단 핸들러를 연결하면 라이브러리에서도 이점을 얻을 수 있다는 것을 깨달았습니다.

하지만 Wasm을 ES 모듈로 빌드하고 직접 가져오는 경우(예: ``import { func } from ‘wasm-dep’`) 사용자 JS 애플리케이션에 이미 링크되고 초기화된 라이브러리에 대해 ``func()``를 호출하는 동안 Wasm이 중단될 경우 복구 메커니즘이 무엇인지 명확하지 않습니다.

엄밀히 말하면 Rust Workers 사용 사례는 아니지만, 저희 팀에서는 Rust 지원 Wasm 라이브러리 종속성을 실행하는 JS 기반 Workers 사용자도 지원합니다. 이 문제를 동시에 해결할 수 있다면, Cloudflare Workers 플랫폼에서의 Wasm 사용에 간접적인 도움이 될 수 있습니다.

Wasm 라이브러리 사용 사례에서 자동 중단 복구를 지원하기 위해 저희는 실험적인 재초기화 메커니즘에 대한 지원을 wasm-bindgen, `--reset-state-function`에 추가했습니다. 그러면 Rust 애플리케이션에서, 생성된 바인딩의 소비자에게 바인딩을 다시 가져오거나 다시 만들 것을 요구하지 않고도 다음 호출을 위해 내부 Wasm 인스턴스를 초기 상태로 재설정하도록 효과적으로 요청할 수 있는 함수가 노출됩니다. 핸들이 분리되면 이전 인스턴스의 클래스 인스턴스가 발생하지만, 그러면 새 클래스를 생성할 수 있습니다. Wasm 라이브러리를 사용하는 JS 애플리케이션에 오류가 발생했지만, 브릭으로 처리되지는 않았습니다.

이 기능의 전체적인 기술적 세부 사항과 이를 wasm-bindgen에서 사용하는 방법은 새로운 wasm-bindgen 가이드 섹션 [_Wasm Bindgen: 중단 처리하기_](https://wasm-bindgen.github.io/wasm-bindgen/reference/handling-aborts.html)에서 다룹니다.

## Wasm 예외 처리 생태계의 성숙

이 작업을 위한 업스트림 기여는 wasm-bindgen 프로젝트에서 멈추지 않았습니다. `panic=unwind` 상태에서 Wasm을 위해 빌드하는 것은 여전히 실험적인 나이틀리 Rust 타겟이 필요하므로, 저희는 이를 안정적인 Rust로 가져오는 데 도움이 되도록 WebAssembly 예외 처리에 대한 Rust의 Wasm 지원을 발전시키는 작업을 해왔습니다.

WebAssembly 예외 처리를 개발하는 과정 중 마지막 단계의 사양 변경으로 인해[ _레거시 예외_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/legacy/Exceptions.md) [_처리와 "exnref 사용"_](https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md) 마지막 최신 예외 처리라는 두 가지 변형이 생겼습니다. 오늘날에도 Rust의 WebAssembly 대상은 여전히 레거시 변형에 대한 코드를 기본적으로 내보내고 있습니다. 레거시 예외 처리는 널리 지원되기는 하지만, 현재는 더 이상 사용되지 않습니다.

최신 WebAssembly 예외 처리는 다음 JS 플랫폼 릴리스를 통해 지원됩니다.

런타임| 버전| 출시일  
---|---|---  
v8| 13.8.1| 2025년 4월 28일  
workerd| v1.20250620.0| 2025년 6월 19일  
Chrome| 138| 2025년 6월 28일  
Firefox| 131| 2024년 10월 1일  
Safari| 18.4| 2025년 3월 31일  
Node.js| 25.0.0| 2025년 10월 15일  
  
지원 매트릭스를 조사하던 중 가장 큰 문제는 결국 Node.js 24 LTS 릴리스 일정이 되어 2028년 4월까지 전체 생태계가 레거시 WebAssembly 예외 처리에 묶여 있게 되었습니다.

이러한 불일치를 발견한 후, 저희는 최신 예외 처리를 Node.js 24 릴리스로 백포팅하고, 해당 대상을 확실히 지원하기 위해 Node.js 22 릴리스 라인에서 예외 처리를 작동시키는 데 필요한 수정도 백포팅할 수 있었습니다. 이를 통해 내년에 최신 예외 처리 제안을 기본 대상이 될 수 있습니다.

앞으로 몇 달간 최종 사용자가 최대한 눈에 띄지 않도록 안정적인 `panic=unwind` 및 최신 예외 처리로 전환할 예정입니다.

이처럼 장기적인 생태계에 대한 투자에는 시간이 걸리지만, Rust WebAssembly 커뮤니티 전체의 강력한 기반을 구축하는 데 도움이 되고, Cloudflare는 이러한 개선에 기여할 수 있어 기쁩니다.

## Rust Workers에서 패닉 해제 사용

Rust Workers 버전 0.8.0부터는 새로운 `--panic-unwind` 플래그가 추가되었으며, [_여기 지침_](https://github.com/cloudflare/workers-rs?tab=readme-ov-file#panic-recovery-with---panic-unwind)에 따라 빌드 명령에 추가할 수 있습니다.

이 플래그를 사용하면 패닉을 완전히 복구할 수 있으며, 중단 복구는 새로운 중단 분류 및 복구 후크 메커니즘을 사용합니다. 저희는 더욱 안정적인 Rust Workers 경험을 위해 업그레이드하고 사용해 볼 것을 강력히 권장하며, 후속 릴리스에서는 `panic=unwind` 를 기본으로 설정할 계획입니다. `panic=abort` 상태인 사용자는 0.6.0부터의 이전 사용자 지정 복구 래퍼 처리 기능을 계속 활용할 수 있습니다.

## Rust Workers 안정성에 전념

이 작업은 Rust Workers의 안정적인 릴리스를 위한 지속적인 노력의 일환입니다. Wasm 플랫폼의 이러한 첨예한 가장자리를 근원에서 해결하고 생태계에 다시 기여함으로써 우리는 플랫폼뿐만 아니라 전체 Rust, JS, Wasm 생태계를 위한 더 강력한 기반을 구축할 수 있습니다.

Cloudflare는 Rust Workers에 대한 향후 개선 계획이 다수 있습니다. Cloudflare 팀의 Guy Bedford가 다음 강연에서 미리 설명한 Wasm-bindgen 제네릭 및 자동화된 바인딩젠을 포함한 이 추가 작업의 업데이트를 곧 공유하겠습니다 [_Wasm.io의 데이터입니다_](https://www.youtube.com/watch?v=zlSJY8Qv5XI).

**#rust‑on‑workers** 에서 [_Cloudflare Discord_](https://discord.com/invite/cloudflaredev)에서 저희를 찾아보세요. 저희는 피드백과 토론, 특히 [_workers-rs_](https://github.com/cloudflare/workers-rs) 및 [_wasm-bindgen_](https://github.com/wasm-bindgen/wasm-bindgen) GitHub 프로젝트에 새로 참여하는 모든 기여자들을 환영합니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-rust-workers-reliable%2F&t=Rust%20Workers%EB%A5%BC%20%EC%95%88%EC%A0%95%EC%A0%81%EC%9C%BC%EB%A1%9C%20%EB%A7%8C%EB%93%A4%EA%B8%B0%3A%20wasm-bindgen%EC%97%90%EC%84%9C%EC%9D%98%20%ED%8C%A8%EB%8B%89%20%EB%B0%8F%20%EC%A4%91%EB%8B%A8%20%EB%B3%B5%EA%B5%AC)[](https://x.com/intent/post?text=Rust+Workers%EB%A5%BC+%EC%95%88%EC%A0%95%EC%A0%81%EC%9C%BC%EB%A1%9C+%EB%A7%8C%EB%93%A4%EA%B8%B0%3A+wasm-bindgen%EC%97%90%EC%84%9C%EC%9D%98+%ED%8C%A8%EB%8B%89+%EB%B0%8F+%EC%A4%91%EB%8B%A8+%EB%B3%B5%EA%B5%AC&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-rust-workers-reliable%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-rust-workers-reliable%2F)[](https://bsky.app/intent/compose?text=Rust+Workers%EB%A5%BC+%EC%95%88%EC%A0%95%EC%A0%81%EC%9C%BC%EB%A1%9C+%EB%A7%8C%EB%93%A4%EA%B8%B0%3A+wasm-bindgen%EC%97%90%EC%84%9C%EC%9D%98+%ED%8C%A8%EB%8B%89+%EB%B0%8F+%EC%A4%91%EB%8B%A8+%EB%B3%B5%EA%B5%AC+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-rust-workers-reliable%2F)[](https://mastodonshare.com/?text=Rust+Workers%EB%A5%BC+%EC%95%88%EC%A0%95%EC%A0%81%EC%9C%BC%EB%A1%9C+%EB%A7%8C%EB%93%A4%EA%B8%B0%3A+wasm-bindgen%EC%97%90%EC%84%9C%EC%9D%98+%ED%8C%A8%EB%8B%89+%EB%B0%8F+%EC%A4%91%EB%8B%A8+%EB%B3%B5%EA%B5%AC&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-rust-workers-reliable%2F)[](https://www.threads.net/intent/post?text=Rust+Workers%EB%A5%BC+%EC%95%88%EC%A0%95%EC%A0%81%EC%9C%BC%EB%A1%9C+%EB%A7%8C%EB%93%A4%EA%B8%B0%3A+wasm-bindgen%EC%97%90%EC%84%9C%EC%9D%98+%ED%8C%A8%EB%8B%89+%EB%B0%8F+%EC%A4%91%EB%8B%A8+%EB%B3%B5%EA%B5%AC+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-rust-workers-reliable%2F)

## 관련 태그

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[Rust Workers](https://blog.cloudflare.com/ko-kr/tag/rust-workers/)[WASM](https://blog.cloudflare.com/ko-kr/tag/wasm/)[WebAssembly](https://blog.cloudflare.com/ko-kr/tag/webassembly/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
