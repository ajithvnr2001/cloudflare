---
url: https://blog.cloudflare.com/ko-kr/connecting-to-production-the-architecture-of-remote-bindings/
title: \ud504\ub85c\ub355\uc158\uc5d0 \uc5f0\uacb0: \uc6d0\uaca9 \ubc14\uc778\ub529\uc758 \uc544\ud0a4\ud14d\ucc98 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:39.463064+00:00
---

# 프로덕션에 연결: 원격 바인딩의 아키텍처 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/connecting-to-production-the-architecture-of-remote-bindings/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[D1](https://blog.cloudflare.com/ko-kr/tag/d1/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)

3개 태그3개 태그 보기

  * 게시물 태그
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[D1](https://blog.cloudflare.com/ko-kr/tag/d1/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)
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



[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[D1](https://blog.cloudflare.com/ko-kr/tag/d1/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)

2025년 11월 12일

# 프로덕션에 연결: 원격 바인딩의 아키텍처

![Samuel Macleod](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498X1ZVM0N111DBDKB3MM1.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Dario Piotrowicz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW450K2XVXFFD2EJ6JZZ2SDE.png&w=64&h=64&f=webp&fit=cover&position=center)

[Samuel Macleod](https://blog.cloudflare.com/ko-kr/author/samuel/) 및 [Dario Piotrowicz](https://blog.cloudflare.com/ko-kr/author/dario/)

8분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/connecting-to-production-the-architecture-of-remote-bindings/) 및 [日本語](https://blog.cloudflare.com/ja-jp/connecting-to-production-the-architecture-of-remote-bindings/).

![BLOG 2840 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48XZE1XZ7YJGDM6ZHMR24M.png&w=1201&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA9/j96+z20dHnvL3fvsHlztLu2dvu29rm+vv/7vD51NTpv7/fwsPl0dPu293v3d3p////9Pb/29ztyMfiysrm2Nnw4eLz4ePt/////f//5ujz1tbo2Nfs5OT26+z46uzz////////9fb85+jy6ur29PP++Pn/9ff5////////////+Pr9+/z/////////////////////////////////////////////////////////////////////////////)

원격 바인딩은 로컬에서 시뮬레이션된 리소스 _대신_ Cloudflare 계정에 배포된 리소스에 연결하는 바인딩입니다.[_그리고 최근에는 원격 바인딩을 일반 사용자도 모두 사용할 수 있다고 발표했습니다._](https://blog.cloudflare.com/cloudflare-developer-platform-keeps-getting-better-faster-and-more-powerful/#connect-to-production-services-and-resources-from-local-development-with-remote-bindings-now-ga)

이번 출시를 통해 이제 로컬 컴퓨터에서 Worker 코드를 실행하면서 [_R2 버킷_](https://developers.cloudflare.com/r2/) 및 [_D1 데이터베이스_](https://www.cloudflare.com/developer-platform/products/d1/) 와 같은 배포된 리소스에 연결할 수 있습니다. 즉, 반복할 때마다 배포하는 오버헤드 없이 실제 데이터 및 서비스에 대해 로컬 코드 변경 사항을 테스트할 수 있습니다. 

이 블로그 게시물에서는 Cloudflare가 이를 어떻게 구축하여 원활한 로컬 개발 경험을 만들었는지에 대한 기술적 세부 사항을 살펴봅니다.

### Workers 플랫폼에서 개발

[ _Cloudflare Workers 플랫폼_](https://www.cloudflare.com/developer-platform/products/workers/) 의 핵심은 무언가를 테스트할 때마다 코드를 배포하지 않고도 로컬에서 코드를 개발할 수 있는 기능이었습니다. 지원 방식은 수년에 걸쳐 크게 바뀌었습니다. 

먼저 `wrangler` dev를 원격 모드로 실행했습니다. 이는 코드를 변경할 때마다 Cloudflare의 네트워크에서 실행되는 Worker의 미리 보기 버전을 배포하고 연결하여 작동하므로 개발하면서 테스트할 수 있습니다. 그러나 원격 모드는 복잡하고 유지 관리하기 어려우므로 완벽하지는 않습니다. 또한 개발자 경험은 느린 반복 속도, 불안정한 디버깅 연결, 다중 작업자 시나리오에 대한 지원 부족 등 아쉬운 점이 많습니다. 

이러한 문제 등은 2023년 중반에 출시되어 [_wrangler dev의 기본 경험_](https://blog.cloudflare.com/wrangler3/)이 된 Workers의 완전한 로컬 개발 환경에 상당한 투자를 하게 된 동기가 되었습니다. [_그 이후로 저희는 Wrangler,_](https://developers.cloudflare.com/workers/wrangler/) [_Cloudflare Vite_](https://developers.cloudflare.com/workers/vite-plugin/) 플러그인([_@cloudflare/vitest-풀-workers와_](https://developers.cloudflare.com/workers/testing/vitest-integration/) 함께), [_Miniflare_](https://developers.cloudflare.com/workers/testing/miniflare/) 등을 포함한 로컬 개발 경험에 많은 노력을 기울였습니다.

그래도 원래 원격 모드는 `wrangler dev --remote` 플래그를 통해 계속 액세스할 수 있었습니다. 원격 모드를 사용하면 완전한 로컬 경험의 모든 DX 이점과 지난 몇 년 동안 이룬 개선 사항이 무시됩니다. 그렇다면 사람들이 여전히 Cloudflare를 이용하는 이유는 무엇일까요? 이를 통해 로컬 개발 중에 원격 리소스에 바인딩하는 고유한 핵심 기능이 가능해집니다. 로컬 모드를 사용하여 로컬에서 Worker를 개발하면 모든 [_바인딩_](https://developers.cloudflare.com/workers/runtime-apis/bindings/) 이 로컬(초기에는 비어 있음) 데이터를 사용하여 로컬에서 시뮬레이션됩니다. 이는 테스트 데이터로 앱의 로직을 반복할 때 환상적입니다. 하지만 팀과 리소스를 공유하고자 하는 경우, 실제 데이터와 연계된 버그를 복제하려는 경우, 앱이 실제 리소스로 프로덕션 환경에서 작동한다는 확신을 갖고자 할 때 그것만으로는 충분하지 않을 때가 있습니다. .

이러한 점을 고려하면, 다음과 같은 기회를 포착했습니다. 원격 모드의 가장 좋은 부분(즉, 원격 리소스 액세스)을 `Wrangler` 개발자에게 제공하는 경우 Workers 개발에 단일 단일 흐름이 있으므로 많은 사용 사례를 가능하게 하면서도 로컬 개발에서 수행한 발전에서 사람들을 가로막지 못할 것입니다. 그렇게 했죠! 

Wrangler v4.37.0부터는 단순히 `remote` 옵션을 지정하는 것만으로 바인딩별로 원격 또는 로컬 리소스를 사용할지 여부를 선택할 수 있습니다. 이 점을 다시 강조하는 것이 중요합니다.`remote: true만` 추가하면 됩니다! API 키와 자격 증명을 복잡하게 관리할 필요 없이 Wrangler와 Cloudflare API 사이의 기존 Oauth 연결을 사용하기만 하면 됩니다.
    
    
    {
      "name": "my-worker",
      "compatibility_date": "2025-01-01",
      "kv_namespaces": [{
        "binding": "KV",
        "id": "my-kv-id",
      },{
        "binding": "KV_2",
        "id": "other-kv-id",
        "remote": true
      }],
      "r2_buckets": [{
        "bucket_name": "my-r2-name",
        "binding": "R2"
      }]
    }

매의 눈을 가진 사람들은 일부 바인딩이 이미 이러한 방식으로 로컬 개발자의 원격 리소스에 액세스하는 방식으로 작동한다는 사실을 깨달았을 것입니다. 가장 두드러진 점은 [_AI 바인딩_](https://developers.cloudflare.com/workers-ai/configuration/bindings/) 이 일반 원격 바인딩 솔루션의 미래를 개척했다는 점입니다. Workers AI와 함께 사용할 수 있는 다양한 모델을 모두 지원하는 진정한 로컬 환경은 실용적이지 않고 AI 모델을 대량으로 미리 다운로드해야 하므로 도입부터 AI 바인딩은 항상 원격 리소스에 연결되었습니다. 

Workers 내의 서로 다른 제품(예: Images 및 Hyperdrive)에는 원격 바인딩과 유사한 것이 필요하다는 것을 깨닫고 서로 다른 솔루션을 약간의 패치워크로 만들었습니다. Cloudflare는 모든 바인딩 유형에서 작동하는 단일 원격 바인딩 솔루션으로 통합했습니다.

### 구축 방법

저희는 개발자가 프로덕션 Workers 코드를 변경하지 않고도 원격 리소스에 정말 쉽게 액세스할 수 있도록 하기 위해 Worker의 사용 지점에서 원격 리소스에서 데이터를 가져와야 하는 솔루션을 찾았습니다.
    
    
    const value = await env.KV.get("some-key")

_위의 코드는 env.KV[ _KV 네임스페이스의_](https://developers.cloudflare.com/kv/api/read-key-value-pairs/) "some-key" 값에 액세스하는 것을 보여줍니다. 이 값은 로컬에서 사용할 수 없으며 네트워크를 통해 가져와야 합니다._

이것이 우리의 요구 사항이라면 어떻게 달성할 수 있을까요? 예를 들어 사용자가 Worker에서 `env.KV.put("key","value")를` 호출했다면 실제로 이를 원격 KV 저장소에 저장하려면 어떻게 해야 할까요? 가장 확실한 해결책은 [_Cloudflare API_](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/update/)를 사용하는 것이었습니다. 우리는 로컬에서 전체 env를 API 호출을 하는 스텁 객체로 대체하고 `env.KV.put()` 을 PUT `http:///accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}`으로 변환할 수도 있었습니다. 

이 방식은 KV, R2, D1 등 성숙한 HTTP APIs를 포함한 바인딩에 유용했을 것입니다. 하지만 구현하고 유지 관리하기가 상당히 복잡한 솔루션이었을 것입니다. 우리는 전체 바인딩 API 표면을 복제하고 바인딩에서 가능한 모든 작업을 동등한 API 호출로 변환해야 했습니다. 또한 일부 바인딩 작업에는 이에 해당하는 API 호출이 없으므로 이 전략을 사용하면 지원할 수 없습니다.

대신 우리는 이미 프로덕션에서 사용하는 API가 기성품으로 우리를 기다리고 있다는 것을 깨달았습니다! 

### 프로덕션의 내부에서 바인딩이 작동하는 방식

Workers 플랫폼의 대부분의 바인딩은 본질적으로 [_서비스 바인딩_](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)으로 귀결됩니다. 서비스 바인딩은 두 Workers 사이의 링크를 통해 HTTP나 [_JSRPC_](https://blog.cloudflare.com/javascript-native-rpc/) (JSRPC에 대해서는 나중에 설명하겠습니다)를 통해 통신할 수 있도록 합니다. 

예를 들어, KV 바인딩은 작성된 Worker와 HTTP Worker 간의 서비스 바인딩으로 구현됩니다. KV 바인딩용 JS API는 Workers 런타임에서 구현되며, `env.KV.get()` 과 같은 호출을 KV 서비스를 구현하는 Worker에 대한 HTTP 호출로 변환합니다. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG 2840 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46Q87QEAZ2T40R2PF2VVMK.png&w=715&h=299&f=webp&fit=cover&position=center)

 _프로덕션 환경에서 KV 바인딩이 작동하는 방식을 단순화한 모델을 보여주는 다이어그램_

여기에는 `env.KV.get()` 호출을 변환하는 런타임과 KV 서비스를 구현하는 Worker 사이에 자연스러운 비동기 네트워크 경계가 있음을 알 수 있습니다. 그래서 자연스러운 네트워크 경계를 사용하여 원격 바인딩을 구현할 수 있다는 것을 깨달았습니다. _프로덕션_ `런타임이 env.KV.get()` 을 HTTP 호출로 변환하는 대신,_로컬_ 런타임([_workerd)이_](https://github.com/cloudflare/workerd) `env.KV.get()` 을 HTTP 호출로 변환한 다음, KV 서비스로 직접 보내도록 할 수 있습니다. 프로덕션 런타임을 우회하는 것입니다. 그렇게 했죠!

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG 2840 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RHXWQ74T21SNQVVKFPQQ.png&w=715&h=295&f=webp&fit=cover&position=center)

_원격 프록시 서버와 통신하는 단일 원격 프록시 클라이언트, 차례로 원격 KV와 통신하는 단일 KV 바인딩을 사용하여 로컬로 실행되는 worker를 보여주는 다이어그램_

위 다이어그램은 원격 KV 바인딩과 함께 실행되는 로컬 Worker를 보여줍니다. 이제 로컬 KV 시뮬레이션이 처리하는 대신 원격 프록시 클라이언트가 처리합니다. 그런 다음 이 Worker는 실제 원격 KV 리소스에 연결된 원격 프록시 서버와 통신하여 궁극적으로 로컬 Worker가 원격 KV 데이터와 원활하게 통신할 수 있도록 합니다.

각 바인딩은 원격 프록시 클라이언트(모두 동일한 원격 프록시 서버에 연결된) 또는 로컬 시뮬레이션에서 독립적으로 처리될 수 있으므로, 일부 바인딩은 로컬에서 시뮬레이션되고 다른 바인딩은 실제 원격 리소스에 연결되는 매우 동적인 워크플로우가 가능합니다. 아래 예시에서 설명하겠습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG 2840 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GXD2S8761JB6KWM17YM6.png&w=707&h=360&f=webp&fit=cover&position=center)

_위 다이어그램과 구성은 서로 다른 3개의 리소스에 바인딩된 Worker(컴퓨터에서 실행)를 보여줍니다. 2개는 로컬(KV 및 R2), 다른 1개는 원격(KV_2)_

### JSRPC의 적합성

위 섹션에서는 HTTP 연결(예: KV 및 R2)로 지원되는 바인딩을 다루었지만, 최신 바인딩은 [_JSRPC_](https://blog.cloudflare.com/javascript-native-rpc/)를 사용합니다. 즉, 로컬에서 실행되는 `workerd `가 JSRPC를 프로덕션 런타임 인스턴스와 대화할 수 있는 방법이 필요했습니다. 

[ _Cap'n Web 블로그에서_](https://blog.cloudflare.com/capnweb-javascript-rpc-library/) 자세히 설명한 바와 같이, 다행히도 이를 가능하게 하는 병행 프로젝트가 진행되고 있었습니다. `로컬 workerd` 인스턴스와 원격 런타임 인스턴스 간의 연결이 [_Cap'n Web을 사용하여 WebSocket을 통해_](https://github.com/cloudflare/capnweb) 통신하도록 하고, JSRPC로 지원되는 바인딩이 작동하도록 했습니다. 여기에는 [_Images_](https://developers.cloudflare.com/images/transform-images/transform-via-workers/)와 같은 최신 바인딩과 자체 Workers에 대한 JSRPC 서비스 바인딩이 포함됩니다.

### Vite, Vitest, JavaScript 생태계와의 원격 바인딩

이 흥미로운 새 기능을 `wrangler dev` 전용으로 제한하고 싶지 않았습니다. 저희는 Cloudflare Vite 플러그인 및 바이테스트-풀-작업자 패키지에서 이를 지원하고, JavaScript 생태계의 다른 잠재적 도구와 사용 사례에서도 이점을 누릴 수 있도록 하고 싶었습니다.

이 목적을 달성하기 위해, wrangler 패키지는 이제 `wrangler dev를` 활용하지 않는 도구도 원격 바인딩을 지원할 수 있도록 해주는`startRemoteProxySession` 등의 유틸리티를 내보냅니다. 자세한 내용은 [_공식 원격 바인딩 문서_](https://developers.cloudflare.com/workers/development-testing/#remote-bindings)에서 확인할 수 있습니다.

### 어떻게 시험해 볼 수 있나요?

그냥 `wrangler dev`를 사용하세요! Wranglerv4.37.0(`@cloudflare/vite-plugin` v1.13.0, `@cloudflare/vitest-pool-workers` v0.9.0) 기준으로, 원격 바인딩은 모든 프로젝트에서 사용할 수 있으며, 다음을 추가하여 바인딩별로 설정할 수 있습니다 `remote:` [_Wrangler 구성 파일의 바인딩_](https://developers.cloudflare.com/workers/wrangler/configuration/) 정의와 일치해야 합니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F&t=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98%EC%97%90%20%EC%97%B0%EA%B2%B0%3A%20%EC%9B%90%EA%B2%A9%20%EB%B0%94%EC%9D%B8%EB%94%A9%EC%9D%98%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98)[](https://x.com/intent/post?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98%EC%97%90+%EC%97%B0%EA%B2%B0%3A+%EC%9B%90%EA%B2%A9+%EB%B0%94%EC%9D%B8%EB%94%A9%EC%9D%98+%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://bsky.app/intent/compose?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98%EC%97%90+%EC%97%B0%EA%B2%B0%3A+%EC%9B%90%EA%B2%A9+%EB%B0%94%EC%9D%B8%EB%94%A9%EC%9D%98+%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://mastodonshare.com/?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98%EC%97%90+%EC%97%B0%EA%B2%B0%3A+%EC%9B%90%EA%B2%A9+%EB%B0%94%EC%9D%B8%EB%94%A9%EC%9D%98+%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)[](https://www.threads.net/intent/post?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98%EC%97%90+%EC%97%B0%EA%B2%B0%3A+%EC%9B%90%EA%B2%A9+%EB%B0%94%EC%9D%B8%EB%94%A9%EC%9D%98+%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnecting-to-production-the-architecture-of-remote-bindings%2F)

## 관련 태그

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[D1](https://blog.cloudflare.com/ko-kr/tag/d1/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
