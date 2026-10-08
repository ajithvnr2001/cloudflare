---
url: https://blog.cloudflare.com/ko-kr/writing-complex-macros-in-rust-reverse-polish-notation/
title: Rust \ub85c \ubcf5\uc7a1\ud55c \ub9e4\ud06c\ub85c\ub97c \uc791\uc131\ud558\uae30: \uc5ed\ud3f4\ub780\ub4dc \ud45c\uae30\ubc95\u200b | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:21.532878+00:00
---

# Rust 로 복잡한 매크로를 작성하기: 역폴란드 표기법​ | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/writing-complex-macros-in-rust-reverse-polish-notation/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Polish](https://blog.cloudflare.com/ko-kr/tag/cloudflare-polish/)[Programming](https://blog.cloudflare.com/ko-kr/tag/programming/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)+11개의 태그 더 보기

4개 태그4개 태그 보기

  * 게시물 태그
  * [Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)
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



[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)

[Cloudflare Polish](https://blog.cloudflare.com/ko-kr/tag/cloudflare-polish/)[Programming](https://blog.cloudflare.com/ko-kr/tag/programming/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)

2018년 1월 31일

# Rust 로 복잡한 매크로를 작성하기: 역폴란드 표기법​

![Ingvar Stepanyan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HXZCX2W0E3TV8QJY1YTY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ingvar Stepanyan](https://blog.cloudflare.com/ko-kr/author/ingvar-stepanyan/)

8분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/writing-complex-macros-in-rust-reverse-polish-notation/), [Deutsch](https://blog.cloudflare.com/de-de/writing-complex-macros-in-rust-reverse-polish-notation/), [Español](https://blog.cloudflare.com/es-es/writing-complex-macros-in-rust-reverse-polish-notation/), [Français](https://blog.cloudflare.com/fr-fr/writing-complex-macros-in-rust-reverse-polish-notation/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/writing-complex-macros-in-rust-reverse-polish-notation/).

![Writing complex macros in Rust: Reverse Polish Notation](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49FSNFEYMC4YKNMQ9ZPHFY.jpg&w=640&h=427&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAVmVuTmBtO1drNFRtQ1xzU2Z4V2p4UWl2anV+YW96TmN1Rl91VGd7ZHKCZ3aDYHN/eoSNcX2JXnCBVWp/Y3OGcn6OdoKPb3+KgYuWeIWSZnmKXnSJbHyRe4eZfouad4iVfIiZdISWZXuQYHqSboKafIyhfo+id42dbX+WaH2UXXqUXXyYaoWgd42meJCmcY6iXHORWHSRU3eVWH2bZYWjcIupcI6oaY6lU26OUXCQT3WVVn2cY4WlbYupbI2pZo6m)

* * *

(이 글은 제 [개인 블로그에 게시된 튜토리얼](https://rreverser.com/writing-complex-macros-in-rust/)을 다시 올린 것입니다)

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Rust with a macro lens](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47AZAKFG11R2WFAJH521KV.jpg&w=640&h=427&f=webp&fit=cover&position=center)

Rust에는 흥미로운 기능이 많지만 그중에도 강력한 매크로 시스템이 있습니다. 불행히도 The Book[1]과 여러가지 튜토리얼을 읽고 나서도 서로 다른 요소의 복잡한 리스트를 처리하는 매크로를 구현하려고 하면 저는 여전히 어떻게 만들어야 하는지를 이해하는데 힘들어 하며, 좀 시간이 지나서 머리속에 불이 켜지는 듯한 느낌이 들면 그제서야 이것저것 매크로를 마구 사용하기 시작 합니다. :) _(맞아요, 난-매크로를-써요-왜냐하면-함수나-타입-지정이나-생명주기를-쓰고-싶어하지-않아서 처럼과 같은 이유는 아니지만 다른 사람들이 쓰는걸 봤었고 실제로 유용한 곳이라면 말이죠)_

[CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) [image](https://www.flickr.com/photos/conchur/25057125240/in/photolist-EbdjmG-8NSN1q-qXhueG-YTYnm3-odaneQ-DxCKQA-228jg4t-DU8Axz-XTQfdD-4p6nJk-UKVzbn-YFeKcW-osZ2XM-e6qefx-Tb3a6Q-dCw1zk-Et3kKh-dbAR9x-zHP8TR-a9cqw4-9JQHRy-Et1Ag5-PqFtx1-7x3Ukq-67VJc6-cvoKSo-qH2S9L-zHJAr9-XmCLsL-8AMWXX-ZV2hHh-XGPiHq-ZKpFSB-yqd2P1-23hMiaC-zETYYa-Wj7BVi-PNP4YA-LCNm6c-8AnkrZ-KA7qmt-KjYPxC-SzQsZD-Cxwvqg-GuZ3nn-J4jBaA-TzyjpB-DcYJA1-YQYNA3-My1uu8) by [Conor Lawless](https://www.flickr.com/photos/conchur/)

그래서 이 글에서는 제가 생각하는 그런 매크로를 쓰는 데 필요한 원칙을 설명하고자 합니다. 이 글에서는 The Book의 [매크로](https://doc.rust-lang.org/book/first-edition/macros.html) 섹션을 읽어 보았고 기본적인 매크로 정의와 토큰 타입에 대해 익숙하다고 가정하겠습니다.

이 튜토리얼에서는 [역폴란드 표기법 (Reverse Polish Notation, RPN)](https://en.wikipedia.org/wiki/Reverse_Polish_notation)을 예제로 사용합니다. 충분히 간단하기 때문에 흥미롭기도 하고, 학교에서 이미 배워서 익숙할 지도 모르고요. 하지만 컴파일 시간에 정적으로 구현하기 위해서는 재귀적인 매크로를 사용해야 할 것입니다.
    
    
    2 3 + 4 *

역폴란드 표기법(후위 또는 후치 표기법으로 불리기도 합니다)은 모든 연산에 스택을 사용하므로 연산 대상을 스택에 넣고 _[이진]_ 연산자는 연산 대상 두개를 스택에서 가져와서 결과를 평가하고 다시 스택에 넣습니다. 따라서 다음과 같은 식을 생각해 보면:

이 식은 다음과 같이 해석됩니다:

  1. `2`를 스택에 넣음
  2. `3`을 스택에 넣음
  3. 스택에서 두 값을 가져옴 (`3`과 `2`), 연산자 `+`를 적용하고 결과 (`5`)를 스택에 다시 넣음
  4. `4`를 스택에 넣음
  5. 스택에서 마지막 두 값을 가져옴 (`4`와 `5`), 연산자 `*` 를 적용하고 (`4 * 5`) 결과 (`20`)을 스택에 다시 넣음
  6. 식의 끝. 스택에 들어 있는 결과값은 `20` 한가지.



수학에서 사용되고 대부분의 현대적인 프로그래밍 언어에서 사용되는 일반적인 중위 표기법에서는 `(2 + 3) * 4` 로 표현이 됩니다.
    
    
    macro_rules! rpn {
      // TODO
    }
    
    println!("{}", rpn!(2 3 + 4 *)); // 20

이제 역폴란드 표기법을 컴파일 시간에 평가하여 Rust가 이해할 수 있는 중위 표기법으로 변환해 주는 매크로를 작성해 보도록 합시다.

스택에 숫자를 넣는 것 부터 시작해 봅시다.
    
    
    macro_rules! rpn {
      ($num:tt) => {
        // TODO
      };
    }

매크로는 현재 문자에 매칭하는 것을 허용하지 않으므로 `expr`은 사용할 수 없는데 숫자 하나를 읽어들이기 보다는 `2 + 3 ...`와 같은 문자열과 매칭할 수 있기 때문입니다. 따라서 (문자/식별자/유효기간 등과 같은 기본 토큰 또는 더 많은 토큰을 포함하고 있는 `()`/`[]`/`{}` 스타일의 괄호식) 토큰 트리를 하나만 읽어들일 수 있는 일반적인 토큰 매칭 기능인 `tt`를 사용하도록 하겠습니다.

이제 스택을 위한 변수가 필요 합니다.

우리는 이 스택이 컴파일 시에만 존재하기를 원하므로 매크로는 실제 변수를 사용할 수 없습니다. 따라서 그 대신에 전달 가능한 별도의 토큰 열을 갖고 축적자 같이 사용되게 하는 트릭을 쓰도록 합니다.
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt) => {
        // TODO
      };
    }

이 경우, (간단한 숫자 뿐 아니라 중간 형태의 중위 표현식을 위해서도 사용할 것이므로) 스택을 쉼표로 분리된 `expr` 의 열로 표현하고 다른 입력에서 분리하기 위해 각괄호로 둘러싸도록 합시다:

여기서 토큰 열은 실제 변수는 아닙니다 - 내용을 바꾸거나 나중에 다른 일을 시킬 수는 없습니다. 대신에 이 토큰 열에 필요한 변경을 해서 새 복사본을 만들 수 있고 재귀적으로 같은 매크로를 다시 부를 수 있습니다.
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt) => {
        rpn!([ $num $(, $stack)* ])
      };
    }

함수형 언어의 기본 지식이 있거나 불변 데이터를 제공하는 라이브러리를 이용해 본 적이 있다면, 이런 접근 방법 - 변경된 복사본을 만드는 것으로 데이터를 변경하거나 재귀를 통해 리스트를 처리하는 - 은 이미 익숙할 것입니다:
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
          rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

이제 분명한 것은 간단한 숫자만의 경우라면 별로 있을것 같지 않고 크게 흥미롭지도 않을 것이므로 그 숫자 이후의 0개나 그 이상의 `tt` 토큰을 찾도록 합니다. 이것은 추가적인 매칭과 처리를 위해 이 매크로의 다음번 호출에 전달될 수 있습니다:

이 시점에서는 아직 연산자를 지원하지 않습니다. 연산자는 어떻게 매칭해야 할까요?

우리의 RPN이 완전히 동일한 방법으로 처리하기를 원하는 토큰 열이라 한다면, 단순히 `$($token:tt)*` 처럼 리스트를 사용할 수 있습니다. 불행히도 이렇게 하면 리스트를 돌아보거나 연산 대상을 집어 넣거나 각 토큰에 따라 연산자를 적용하는 기능을 만들 수 없습니다.

The Book은 "매크로 시스템의 파싱은 명확해야 한다"라고 하고 있으며 이는 단일 매크로 가지에 있어서는 사실입니다 - `+`는 유효한 토큰이며 `tt` 그룹에 매칭이 될 수도 있으므로 `$($num:tt)* +` 와 같은 연산자 뒤에 오는 숫자의 열은 매칭할 수 없는데, 여기서 재귀적 매크로의 도움을 받을 수 있습니다.
    
    
    macro_rules! rpn {
      ([ $($stack:expr),* ] + $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] - $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] * $($rest:tt)*) => {
        // TODO
      };
      
      ([ $($stack:expr),* ] / $($rest:tt)*) => {
        // TODO
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

여러분의 매크로 정의에 복수의 가지가 있다면 Rust는 이것들을 하나씩 시도하므로 숫자 처리 이전에 연산자 가지를 놓는 방식으로 충돌을 방지할 수 있습니다:
    
    
    macro_rules! rpn {
      ([ $b:expr, $a:expr $(, $stack:expr)* ] + $($rest:tt)*) => {
        rpn!([ $a + $b $(, $stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] - $($rest:tt)*) => {
        rpn!([ $a - $b $(, $stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] * $($rest:tt)*) => {
        rpn!([ $a * $b $(,$stack)* ] $($rest)*)
      };
    
      ([ $b:expr, $a:expr $(, $stack:expr)* ] / $($rest:tt)*) => {
        rpn!([ $a / $b $(,$stack)* ] $($rest)*)
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

앞에서 이야기 했듯이 연산자는 스택의 마지막 두 숫자에 적용되므로 이것들은 별도로 매칭해서 그 결과를 "평가" 하고 (일반적인 중위 표현식을 구성) 다시 집어 넣습니다:

저는 이렇게 대놓고 반복하는 것을 그리 좋아하지 않습니다만 문자와 같이 연산자에 매칭하는 토큰 타입은 따로 없습니다.

하지만 할 수 있는 일은 평가를 담당하는 도우미를 추가 하고 명시적인 연산자 가지를 그쪽으로 위임하는 일입니다.

매크로에서는 외부 도우미를 사용할 수는 없지만 확실한 것은 여러분의 매크로가 이미 존재 한다는 것이므로, 사용할 수 있는 트릭은 유일한 토큰 열로 "표식"이 되어 있는 동일 매크로에 가지를 만들고 일반 가지에서 했던 것 처럼 재귀적으로 호출하는 것입니다.

`@op`를 그런 표식으로 사용하고 그 안에서 `tt`를 통한 어떤 연산자라도 받아들이도록 합니다(우리는 연산자만을 이 도우미에게 전달하므로 이러한 문맥에서는 `tt`는 애매한 점이 없습니다).
    
    
    macro_rules! rpn {
      (@op [ $b:expr, $a:expr $(, $stack:expr)* ] $op:tt $($rest:tt)*) => {
        rpn!([ $a $op $b $(, $stack)* ] $($rest)*)
      };
    
      ($stack:tt + $($rest:tt)*) => {
        rpn!(@op $stack + $($rest)*)
      };
      
      ($stack:tt - $($rest:tt)*) => {
        rpn!(@op $stack - $($rest)*)
      };
    
      ($stack:tt * $($rest:tt)*) => {
        rpn!(@op $stack * $($rest)*)
      };
      
      ($stack:tt / $($rest:tt)*) => {
        rpn!(@op $stack / $($rest)*)
      };
    
      ([ $($stack:expr),* ] $num:tt $($rest:tt)*) => {
        rpn!([ $num $(, $stack)* ] $($rest)*)
      };
    }

그리고 스택은 더 이상 각각의 개별 가지에서 확장될 필요가 없습니다 - 앞에서 `[]` 으로 둘러 쌓았기 때문에 또 다른 토큰 나무(`tt`)로서 매칭될 수 있고 이후에 도우미에게 전달이 됩니다:
    
    
    macro_rules! rpn {
      // ...
      
      ([ $result:expr ]) => {
        $result
      };
    }

이제 어떤 토큰이라도 해당하는 가지에서 처리가 되므로 스택에 하나의 아이템만 있고 다른 토큰이 없는 마지막 경우만 처리하면 됩니다:

이 시점에서 빈 스택과 RPN 표현식으로 이 매크로를 실행 하면 이미 제대로 된 결과를 만들어 냅니다:
    
    
    println!("{}", rpn!([] 2 3 + 4 *)); // 20

[운동장](https://play.rust-lang.org/?gist=cd56f6d7335e2d27c05e7fa89545b2cd&version=stable)

하지만 이 스택은 내부적인 구현 사항이라 사용자가 매번 빈 스택을 전달하도록 하기를 바라지는 않으므로, 시작 지점으로 사용될 수 있고 `[]`을 자동적으로 추가해 주는 가지를 하나 더 추가합니다:
    
    
    macro_rules! rpn {
      // ...
    
      ($($tokens:tt)*) => {
        rpn!([] $($tokens)*)
      };
    }
    
    println!("{}", rpn!(2 3 + 4 *)); // 20

[운동장](https://play.rust-lang.org/?gist=d94abc0e20aa5c7f689706af06fd1923&version=stable)
    
    
    println!("{}", rpn!(15 7 1 1 + - / 3 * 2 1 1 + + -)); // 5

이제 우리의 매크로는 [위키피디아의 RPN페이지](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Example)에 있는 복잡한 표현식 예제도 잘 처리 합니다!

### 오류 처리

이제 올바른 RPN 표현식에 대해서는 모든것이 잘 되는 것 같습니다만, 실제 사용 가능한 매크로가 되려면 잘못된 입력도 잘 처리해서 적절한 오류 메시지를 표시하도록 해야 합니다.
    
    
    println!("{}", rpn!(2 3 7 + 4 *));

일단 중간에 숫자 하나를 넣어서 어떻게 되는지 보도록 하면:
    
    
    error[E0277]: the trait bound `[{integer}; 2]: std::fmt::Display` is not satisfied
      --> src/main.rs:36:20
       |
    36 |     println!("{}", rpn!(2 3 7 + 4 *));
       |                    ^^^^^^^^^^^^^^^^^ `[{integer}; 2]` cannot be formatted with the default formatter; try using `:?` instead if you are using a format string
       |
       = help: the trait `std::fmt::Display` is not implemented for `[{integer}; 2]`
       = note: required by `std::fmt::Display::fmt`

출력:

괜찮은 것 같지만 표현식 내의 실제 오류에 대한 정보는 제공하지 않으므로 유용해 보이지는 않습니다.

어떤 일이 일어나는지 알기 위해서는 매크로를 디버깅해야 합니다. 이를 위해서 `trace_macros` 기능을 사용하도록 합니다(다른 부가적인 컴파일러 기능처럼 Rust의 일일 빌드가 필요할 것입니다). `println!` 을 추적하고 싶은 건 아니므로 RPN 표현식을 변수로 분리 합니다:
    
    
    #![feature(trace_macros)]
    
    macro_rules! rpn { /* ... */ }
    
    fn main() {
      trace_macros!(true);
      let e = rpn!(2 3 7 + 4 *);
      trace_macros!(false);
      println!("{}", e);
    }

[운동장](https://play.rust-lang.org/?gist=610bc0c241aacda3d30a916f89b244cd&version=nightly)
    
    
    note: trace_macro
      --> src/main.rs:39:13
       |
    39 |     let e = rpn!(2 3 7 + 4 *);
       |             ^^^^^^^^^^^^^^^^^
       |
       = note: expanding `rpn! { 2 3 7 + 4 * }`
       = note: to `rpn ! ( [  ] 2 3 7 + 4 * )`
       = note: expanding `rpn! { [  ] 2 3 7 + 4 * }`
       = note: to `rpn ! ( [ 2 ] 3 7 + 4 * )`
       = note: expanding `rpn! { [ 2 ] 3 7 + 4 * }`
       = note: to `rpn ! ( [ 3 , 2 ] 7 + 4 * )`
       = note: expanding `rpn! { [ 3 , 2 ] 7 + 4 * }`
       = note: to `rpn ! ( [ 7 , 3 , 2 ] + 4 * )`
       = note: expanding `rpn! { [ 7 , 3 , 2 ] + 4 * }`
       = note: to `rpn ! ( @ op [ 7 , 3 , 2 ] + 4 * )`
       = note: expanding `rpn! { @ op [ 7 , 3 , 2 ] + 4 * }`
       = note: to `rpn ! ( [ 3 + 7 , 2 ] 4 * )`
       = note: expanding `rpn! { [ 3 + 7 , 2 ] 4 * }`
       = note: to `rpn ! ( [ 4 , 3 + 7 , 2 ] * )`
       = note: expanding `rpn! { [ 4 , 3 + 7 , 2 ] * }`
       = note: to `rpn ! ( @ op [ 4 , 3 + 7 , 2 ] * )`
       = note: expanding `rpn! { @ op [ 4 , 3 + 7 , 2 ] * }`
       = note: to `rpn ! ( [ 3 + 7 * 4 , 2 ] )`
       = note: expanding `rpn! { [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [  ] [ 3 + 7 * 4 , 2 ] )`
       = note: expanding `rpn! { [  ] [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [ [ 3 + 7 * 4 , 2 ] ] )`
       = note: expanding `rpn! { [ [ 3 + 7 * 4 , 2 ] ] }`
       = note: to `[(3 + 7) * 4, 2]`

이제 출력을 보면 이 매크로가 단계별로 어떻게 재귀적으로 평가되는지 알 수 있습니다:
    
    
       = note: expanding `rpn! { [ 3 + 7 * 4 , 2 ] }`
       = note: to `rpn ! ( [  ] [ 3 + 7 * 4 , 2 ] )`

잘 따라가 보면 다음 단계가 문제라는 것을 알 수 있습니다:

`[ 3 + 7 * 4 , 2 ]`는 `([$result:expr]) => ...` 가지에 최종 표현식으로 매칭되지 않으므로 그 대신 마지막 가지인 `($($tokens:tt)*) => ...` 에 매칭이 되므로 빈 스택 `[]`이 앞에 추가 되고서 원래의 `[ 3 + 7 * 4 , 2 ]`는 일반적인 `$num:tt`에 매칭되어 단일 최종 값으로 스택에 들어가게 됩니다.

이런 일을 방지하기 위해서 어떤 스택과도 매칭이 되는 마지막 두 가지 시이에 가지를 하나 더 추가하도록 합니다.

이것은 토큰이 다 떨어졌을 때만 해당할 것이지만 스택에는 최종값 하나만 들어있지 않을 것이므로 이를 컴파일 오류로 취급하고 내장된 `compile_error!` 매크로를 사용해서 적절한 오류 메시지를 출력 하도록 합니다.

주의할 것은 이 문맥에서는 메시지 문자열을 만들기 위해서 런타임 API를 사용하는 `format!`을 사용할 수 없으므로 그 대신에 메시지를 만들어 내기 위해서 내장된 `concat!`과 `stringify!` 매크로를 사용 합니다.
    
    
    macro_rules! rpn {
      // ...
    
      ([ $result:expr ]) => {
        $result
      };
    
      ([ $($stack:expr),* ]) => {
        compile_error!(concat!(
          "Could not find final value for the expression, perhaps you missed an operator? Final stack: ",
          stringify!([ $($stack),* ])
        ))
      };
    
      ($($tokens:tt)*) => {
        rpn!([] $($tokens)*)
      };
    }

[운동장](https://play.rust-lang.org/?gist=e56be9422387bcae54aab3b8405a11e7&version=stable)
    
    
    error: Could not find final value for the expression, perhaps you missed an operator? Final stack: [ (3 + 7) * 4 , 2 ]
      --> src/main.rs:31:9
       |
    31 |         compile_error!(concat!("Could not find final value for the expression, perhaps you missed an operator? Final stack: ", stringify!([$($stack),*])))
       |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...
    40 |     println!("{}", rpn!(2 3 7 + 4 *));
       |                    ----------------- in this macro invocation

이제 좀 더 의미 있는 오류 메시지가 되었고 적어도 현재의 평가 상태에 대해 약간의 상세한 정보를 제공 합니다:

하지만 숫자가 없다면 어떻게 될까요?
    
    
    println!("{}", rpn!(2 3 + *));

[운동장](https://play.rust-lang.org/?gist=ce40630b8c1aa610c46b94557fdc9905&version=stable)
    
    
    error: expected expression, found `@`
      --> src/main.rs:15:14
       |
    15 |         rpn!(@op $stack * $($rest)*)
       |              ^
    ...
    40 |     println!("{}", rpn!(2 3 + *));
       |                    ------------- in this macro invocation

불행히도 이건 큰 도움이 되지는 않습니다:

만약 `trace_macros`를 사용하려 하는데 이유가 있어 스택을 보여주지 않는다고 해도, 어떻게 되고 있는지는 비교적 명확합니다 - `@op`는 매칭되는 조건이 매우 구체적입니다(스택에서 최소 두개의 값이 있어야 합니다). 그렇지 않을 경우 `@`는 더 탐욕적인 `$num:tt`에 매칭이 되어 스택에 들어 갑니다.

이걸 피하기 위해서는 아직 매칭되지 않은 `@op`로 시작하는 모든 것에 매칭하는 가지를 하나 더 추가 하고 컴파일 오류를 만들어 냅니다:
    
    
    macro_rules! rpn {
      (@op [ $b:expr, $a:expr $(, $stack:expr)* ] $op:tt $($rest:tt)*) => {
        rpn!([ $a $op $b $(, $stack)* ] $($rest)*)
      };
    
      (@op $stack:tt $op:tt $($rest:tt)*) => {
        compile_error!(concat!(
          "Could not apply operator `",
          stringify!($op),
          "` to the current stack: ",
          stringify!($stack)
        ))
      };
    
      // ...
    }

[운동장](https://play.rust-lang.org/?gist=8729a8f3c96fa58ed62d35804c48782d&version=stable)
    
    
    error: Could not apply operator `*` to the current stack: [ 2 + 3 ]
      --> src/main.rs:9:9
       |
    9  |         compile_error!(concat!("Could not apply operator ", stringify!($op), " to current stack: ", stringify!($stack)))
       |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...
    46 |     println!("{}", rpn!(2 3 + *));
       |                    ------------- in this macro invocation

다시한번 해 봅시다:

훨씬 낫네요! 이제 우리의 매크로는 컴파일 시간에 어떤 RPN도 평가할 수 있고 대부분의 흔한 실수를 잘 처리할 수 있습니다. 이제 여기까지 하도록 하고 실제 사용 가능하다고 해 두지요. :)

추가할 작은 기능은 더 많지만, 이 데모 튜토리얼의 범위를 넘어서는 것으로 하겠습니다.

이 글이 유용했는지, 또는 알고 싶은 주제가 있다면 [트위터](https://twitter.com/RReverser)로 알려 주세요!

* * *

  1. (역주) [The Rust Programming Language](https://doc.rust-lang.org/book/)를 가리키는 말입니다 ↩︎



 _This is a Korean translation of a[existing post](https://blog.cloudflare.com/writing-complex-macros-in-rust-reverse-polish-notation/) by [Ingvar Stepanyan](https://blog.cloudflare.com/author/ingvar-stepanyan/), translated by [Junho Choi](https://blog.cloudflare.com/author/junho/)._

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F&t=Rust%20%EB%A1%9C%20%EB%B3%B5%EC%9E%A1%ED%95%9C%20%EB%A7%A4%ED%81%AC%EB%A1%9C%EB%A5%BC%20%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0%3A%20%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C%20%ED%91%9C%EA%B8%B0%EB%B2%95%E2%80%8B)[](https://x.com/intent/post?text=Rust+%EB%A1%9C+%EB%B3%B5%EC%9E%A1%ED%95%9C+%EB%A7%A4%ED%81%AC%EB%A1%9C%EB%A5%BC+%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0%3A+%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C+%ED%91%9C%EA%B8%B0%EB%B2%95%E2%80%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://bsky.app/intent/compose?text=Rust+%EB%A1%9C+%EB%B3%B5%EC%9E%A1%ED%95%9C+%EB%A7%A4%ED%81%AC%EB%A1%9C%EB%A5%BC+%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0%3A+%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C+%ED%91%9C%EA%B8%B0%EB%B2%95%E2%80%8B+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://mastodonshare.com/?text=Rust+%EB%A1%9C+%EB%B3%B5%EC%9E%A1%ED%95%9C+%EB%A7%A4%ED%81%AC%EB%A1%9C%EB%A5%BC+%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0%3A+%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C+%ED%91%9C%EA%B8%B0%EB%B2%95%E2%80%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)[](https://www.threads.net/intent/post?text=Rust+%EB%A1%9C+%EB%B3%B5%EC%9E%A1%ED%95%9C+%EB%A7%A4%ED%81%AC%EB%A1%9C%EB%A5%BC+%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0%3A+%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C+%ED%91%9C%EA%B8%B0%EB%B2%95%E2%80%8B+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwriting-complex-macros-in-rust-reverse-polish-notation%2F)

## 관련 태그

[Cloudflare Polish](https://blog.cloudflare.com/ko-kr/tag/cloudflare-polish/)[Programming](https://blog.cloudflare.com/ko-kr/tag/programming/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
