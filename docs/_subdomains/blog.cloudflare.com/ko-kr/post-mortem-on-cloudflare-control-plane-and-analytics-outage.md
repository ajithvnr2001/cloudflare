---
url: https://blog.cloudflare.com/ko-kr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/
title: Cloudflare \uc81c\uc5b4\ud310 \ubc0f \ubd84\uc11d \uc11c\ube44\uc2a4 \uc911\ub2e8 \uc0ac\ud6c4 \ubd84\uc11d | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:39:47.134903+00:00
---

# Cloudflare 제어판 및 분석 서비스 중단 사후 분석 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/

[블로그](https://blog.cloudflare.com/ko-kr/)

[사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)

2개 태그2개 태그 보기

  * 게시물 태그
  * [사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)
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



[사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)

2023년 11월 4일

# Cloudflare 제어판 및 분석 서비스 중단 사후 분석

![Matthew Prince](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KQ4Z9PY1TR0ERGW96HZR.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matthew Prince](https://blog.cloudflare.com/ko-kr/author/matthew-prince/)

16분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/), [Deutsch](https://blog.cloudflare.com/de-de/post-mortem-on-cloudflare-control-plane-and-analytics-outage/), [Español](https://blog.cloudflare.com/es-es/post-mortem-on-cloudflare-control-plane-and-analytics-outage/), [Français](https://blog.cloudflare.com/fr-fr/post-mortem-on-cloudflare-control-plane-and-analytics-outage/), [日本語](https://blog.cloudflare.com/ja-jp/post-mortem-on-cloudflare-control-plane-and-analytics-outage/), [繁體中文](https://blog.cloudflare.com/zh-tw/post-mortem-on-cloudflare-control-plane-and-analytics-outage/), [简体中文](https://blog.cloudflare.com/zh-cn/post-mortem-on-cloudflare-control-plane-and-analytics-outage/) 및 [Português](https://blog.cloudflare.com/pt-br/post-mortem-on-cloudflare-control-plane-and-analytics-outage/).

![Post mortem on the Cloudflare Control Plane and Analytics Outage](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FSBWC0D25T68JD98V477.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////+vz/8e/v7Obi7ujj8u3q8O7u6ent/////f7/8+7q7eLa7+Ta9Ozk8u/s7Ozt////////9u7n8ODT8uPT9+3h9vLs8fDv////////+/Lq9OPU9+bV/PLk/Pfw9vXz//////////ny++zf/e/h//rv//74/Pr5///////////+//fv//vy///9///////////////////////9////////////////////////////////////////////////)

2023년 11월 2일 목요일 오전 11:43(UTC)부터 Cloudflare의 제어판 및 분석 서비스가 일시적으로 중단되었습니다. Cloudflare의 제어판은 주로 웹 사이트, API 등 모든 서비스에 대한 고객 대면 인터페이스로 구성됩니다. Cloudflare의 분석 서비스에는 로깅 및 분석 보고가 포함됩니다.

이 사고는 11월 2일 11:44(UTC)부터 11월 4일 04:25(UTC)까지 지속되었습니다. 11월 2일 17:57(UTC)을 기준으로 재해 복구 시설에서 대부분의 제어판을 복구할 수 있었습니다. 재해 복구 시설이 온라인 상태가 된 후에는 많은 고객이 대부분의 제품에서 문제를 경험하지 않았을 것으로 예상됩니다. 그러나 다른 서비스는 복구하는 데 시간이 더 오래 걸렸으며, 해당 서비스를 사용하던 고객들은 Cloudflare에서 사고를 완전히 해결할 때까지 문제를 겪었을 가능성이 있습니다. 사고 발생 기간 동안 대부분의 고객은 원시 로그 서비스를 사용할 수 없었습니다.

이제 모든 고객에 대한 서비스가 복구되었습니다. 사고 기간 내내 Cloudflare의 네트워크 및 보안 서비스는 예상대로 계속 작동했습니다. 고객이 해당 서비스를 변경할 수 없는 기간이 있었지만, Cloudflare 네트워크를 통한 트래픽에는 영향이 미치지 않았습니다.

이 게시물에서는 해당 사고의 발생 원인, 기존의 대응 방안과 아키텍쳐의 한계점, 그리고 지난 36시간동안 Cloudflare에서 경험을 바탕으로 향상된 대응 방안에 대해 핵심적으로 안내해드림으로써 저희 서비스 사용에 투명성을 제고하고자 합니다.

우선, 이번 사고는 절대 일어나서는 안 되는 일이었습니다. Cloudflare에서는 이와 같은 서비스 중단을 막을 수 있는 높은 가용성 시스템을 갖추고 있었다고 믿었습니다. 핵심 데이터 센터 공급자 중 하나가 치명적인 장애를 일으켰을 때에도 말입니다. 또한, 많은 시스템은 설계된 대로 온라인 상태를 유지했지만, 일부 중요 시스템에는 확연히 드러나지 않은 종속성이 있어 사용할 수 없게 되었습니다. 이번 사고를 통해 Cloudflare을 사용해주시는 고객분들이 겪었을 어려움에 다시 한 번 사과의 말씀을 전합니다.

### 의도된 설계

Cloudflare의 제어판 및 분석 시스템은 주로 오리건주 힐스버러 주변에 위치한 데이터 센터 세 곳에 있는 서버에서 실행됩니다. 세 데이터 센터는 서로 독립적이고, 각기 여러 유틸리티 전원 공급 장치를 갖추고 있으며, 각각 독자적인 이중화 네트워크 연결 장치를 여럿 보유하고 있습니다.

이들 시설은 자연재해로 인해 세 곳 모두 영향을 받을 가능성을 최소화하도록 의도적으로 멀리 떨어져 있으면서도 액티브-액티브 이중화 데이터 클러스터를 모두 실행할 수 있을 만큼 충분히 가까운 곳에 위치하도록 선택되었습니다. 이는 세 시설 간에 데이터가 지속해서 동기화된다는 의미입니다. 설계상 시설 중 하나가 오프라인 상태가 되더라도 나머지 시설은 계속 운영될 수 있습니다.

이는 Cloudflare가 4년 전부터 구현하기 시작한 시스템 설계입니다. Cloudflare의 중요 제어판 시스템이 대부분 고가용성 클러스터로 마이그레이션되었지만, 일부 서비스, 특히 일부 최신 제품의 경우 아직 고가용성 클러스터에 추가되지 않았습니다.

또한 로깅 시스템은 의도적으로 고가용성 클러스터에 포함시키지 않았습니다. 이러한 결정의 배경이 된 논리는 로깅이 이미 네트워크의 에지에서 대기열에서 대기한 다음 오리건주의 코어(또는 로깅을 위해 지역 서비스를 사용하는 고객의 경우 다른 지역 시설)로 다시 전송되는 분산된 문제라는 것이었습니다. 로깅 시설이 오프라인 상태라면 분석 로그는 다시 온라인 상태가 될 때까지 네트워크 에지에서 대기열에서 대기하게 됩니다. Cloudflare에서는 분석이 지연되는 것은 허용할 수 있다고 판단했습니다.

### Flexential 데이터 센터 정전

오리건 주에 있는 세 곳의 시설 중 가장 큰 시설은 Flexential에서 운영합니다. Cloudflare에서는 이 시설을 "PDX-DC04"라고 부릅니다. Cloudflare에서는 PDX-04의 공간을 임대하여 가장 큰 분석 클러스터 및 고가용성 클러스터를 위한 장비의 3분의 1 이상을 수용합니다. 이 시설은 또한 아직 고가용성 클러스터에 온보딩되지 않은 서비스의 기본 위치이기도 합니다. 당사는 이 시설의 비교적 큰 고객으로, 시설 전체 용량의 약 10%를 이용합니다.

11월 2일 08시 50분(UTC)에 PDX-04를 서비스하는 유틸리티 회사인 포틀랜드 제너럴 일렉트릭(PGE)에서는 건물로 공급되는 독립 전력 공급 장치 중 하나에 영향을 미치는 예기치 않은 유지보수 이벤트를 겪었습니다. 이 이벤트 때문에 PDX-04에 대한 피드 하나가 중단되었습니다. 데이터 센터에는 시설에 전력을 공급할 수 있는, 어느 정도의 독립성을 갖춘 피드가 여러 개 있습니다. 하지만 Flexential에서는 다운된 피드를 효과적으로 보충하기 위해 발전기를 가동했습니다.

모범 사례와는 달리 Flexential에서는 장애가 발생하여 발전기 전원으로 대체되었다는 사실을 Cloudflare에 알리지 않았습니다. Cloudflare의 어떤 가시성 도구에서도 전원 공급원이 변경된 것을 감지하지 못했습니다. 미리 알려주었다면 시설을 면밀히 모니터링하고 해당 시설에 의존하는 제어판 서비스를 중단된 기간 동안 다른 곳으로 옮길 팀을 구성했을 것입니다.

Flexential에서 남아 있던 하나의 유틸리티 피드와 발전기를 동시에 가동한 것도 이례적인 일입니다. 전력 수요가 많을 때 유틸리티 측에서 데이터 센터에 전력망에서 분리하고 발전기로만 운영하도록 요청하는 것은 드문 일이 아닙니다. Flexential에서는 최대 부하에서 시설을 지원할 수 있는 예비 장치를 포함하여 10개의 발전기를 운영합니다. Flexential에서 남은 유틸리티 피드로만 시설을 가동하는 것도 가능했을 것입니다. Cloudflare에서는 왜 유틸리티 전력과 발전기 전력을 사용했는지에 대한 명확한 답변을 얻지 못했습니다.

### 데이터 기반의 추후 사건 예측

이 결정 이후, 아직까지 Flexential 측으로부터 근본 원인이나 그들이 내린 결정이나 이벤트에 대한 명확한 답변을 듣지 못했습니다. 플렉센셜과 PGE로부터 무슨 일이 있었는지 더 많은 정보를 입수하는 대로 이 게시물을 업데이트할 예정입니다. 다음 내용 중 일부는 가장 가능성이 높은 일련의 사고와 개별 Flexential 직원이 비공식적으로 당사에 공유한 내용을 바탕으로 한 정보에 근거한 추측입니다.

유틸리티 라인을 가동 상태로 두었을 수 있는 한 가지 가능한 이유는 Flexential이 DSG라고 불리는 PGE 프로그램의 일부였기 때문입니다. DSG를 사용하면 지역 유틸리티에서 데이터 센터의 발전기를 가동하여 전력망에 추가 전력을 공급할 수 있습니다. 그 대가로 전력 회사에서는 발전기의 유지보수를 돕고 연료를 공급합니다. Flexential에서 Cloudflare에게 DSG 프로그램에 대해 알려준 기록은 찾을 수 없습니다. 그 당시 DSG가 활성화되어 있었는지 문의했지만, 답변을 받지 못했습니다. 그것이 Flexential의 결정에 영향을 미쳤는지는 알 수 없지만, 그것으로 발전기가 가동된 후에도 유틸리티 라인이 계속 온라인 상태를 유지한 이유를 설명할 수 있습니다.

약 11:40(UTC)에 PDX-04의 PGE 변압기에 접지 오류가 발생했습니다. 데이터 센터에 들어올 때 여전히 가동 중이던 두 번째 피드에 대하여 전력망으로부터의 전력을 차단한 변압기가 이 변압기인 것으로 Cloudflare에서는 믿지만, Flexential이나 PGE로부터 확인을 받지는 못했습니다. Flexential이나 PGE로부터 확인을 받지는 못했지만, PGE에서 수행하고 있었던 계획되지 않은 유지보수 작업으로 인해 접지 오류가 발생하여 첫 번째 피드에 영향을 준 것으로 보입니다. 아니면 아주 불운한 우연의 일치였을 수도 있습니다.

고전압(12,470볼트) 전력선의 접지 오류는 매우 위험합니다. 전기 시스템은 접지 오류가 발생하면 신속하게 차단되어 손상을 방지하도록 설계되어 있습니다. 안타깝게도 이 경우 보호 조치로 인해 PDX-04의 모든 발전기도 정지되었습니다. 이는 해당 시설의 두 가지 전력 공급원(이중화 유틸리티 라인과 발전기 10대)이 모두 오프라인 상태라는 것을 의미했습니다.

다행히도 PDX-04에는 발전기 외에도 UPS 배터리 뱅크가 포함되어 있습니다. 이 배터리는 약 10분 동안 해당 시설에 전원을 공급하기에 충분한 것으로 알려져 있습니다. 이 시간은 정전과 발전기 자동 가동 사이의 간극을 메우기에 충분한 시간입니다. Flexential에서 10분 이내에 발전기나 유틸리티 피드를 복구할 수 있다면 서비스 중단이 발생하지 않을 것입니다. 실제로는, Cloudflare 자체 장비에서 가동이 중단된 것을 관찰한 결과, 배터리는 단 4분 만에 가동이 중단되기 시작했습니다. 그리고 Flexential에서 발전기를 복구하는 데는 10분이 훨씬 넘게 걸렸습니다.

### 전원 복구 시도

공식적인 확인을 받지는 못했지만, 직원들로부터 해당 발전기를 다시 가동하는 데 방해가 된 세 가지 요인이 있었다고 들었습니다. 첫째, 접지 오류로 인해 회로가 트립되었기 때문에 물리적으로 발전기에 접근하여 수동으로 재시작해야 했습니다. 둘째, Flexential의 접근 제어 시스템이 배터리 백업으로 전원이 공급되지 않아 오프라인 상태였습니다. 셋째, 현장의 야간 근무 인력에는 숙련된 운영 전문가나 전기 전문가가 포함되지 않았으며, 야간 근무조는 보안 요원과 근무를 시작한 지 일주일 밖에 되지 않은 기술자 한 명으로 구성되었습니다.

UTC 11:44~12:01 사이에 발전기가 완전히 재가동되지 않은 상태에서 UPS 배터리가 방전되어 데이터 센터의 모든 고객에 대한 전원이 끊겼습니다. 이 과정 내내 Flexential에서는 시설에 문제가 있다는 사실을 Cloudflare에 전혀 알리지 않았습니다. Cloudflare에서는 데이터 센터를 전 세계와 연결하는 라우터 두 대가 11:44(UTC)에 오프라인 상태가 되었을 때 데이터 센터에 문제가 있다는 사실을 처음 통지받았습니다. 라우터에 직접 연결하거나 대역 외 관리를 통해 연결할 수 없게 되자, Cloudflare에서는 Flexential에 연락을 시도하고 현지 팀을 파견하여 해당 시설로 직접 이동했습니다. Flexential에서 문제가 발생했다고 보낸 첫 번째 메시지는 12: 28(UTC)에 Cloudflare에 전달되었습니다.

> _당사에서는 현재 오전 0500시(태평양 표준시 기준)[12:00 UTC]에 시작된 당사 [PDX-04]에서의 전원 문제를 겪고 있습니다. 엔지니어들이 해당 문제를 해결하고 서비스를 복구하기 위해 적극 노력하고 있습니다. 30분마다 또는 복구 예상 시간에 대한 추가 정보가 입수되는 대로 진행 상황을 알려드리겠습니다. 기다려 주시고 이해해 주셔서 감사합니다._

### 데이터 센터 수준의 장애에 대비한 설계

PDX-04의 설계는 구축 전에 Tier III 인증을 받았으며 고가용성 SLA를 제공할 것으로 예상되지만, Cloudflare에서는 오프라인 상태가 될 가능성에 대비하여 계획을 수립했습니다. 잘 운영되는 시설도 안 좋은 때가 있을 수 있습니다. 그리고 Cloudflare에서는 그에 대비한 계획을 세웠던 것입니다. Cloudflare에서 예상했던 상황은 다음과 같습니다. 분석이 오프라인 상태가 되고, 로그가 에지에서 대기 상태가 되어 지연되며, 고가용성 클러스터에 통합되지 않은 우선순위가 낮은 일부 서비스가 다른 시설에서 복원될 때까지 일시적으로 오프라인 상태가 되는 경우입니다.

이 지역에서 운영되는 다른 두 개의 데이터 센터에서 고가용성 클러스터를 책임지고 중요한 서비스를 온라인 상태로 유지합니다. 대체로 이 계획은 효과가 있었습니다. 안타깝게도, Cloudflare에서는 고가용성 클러스터에 있도록 되어 있는 서비스의 하위 집합이 PDX-04에서 독점적으로 실행되는 서비스에 종속되어 있다는 사실을 발견했습니다.

특히 로그를 처리하고 분석을 강화하는 두 가지 중요한 서비스인 Kafka와 ClickHouse는 PDX-04에서만 사용할 수 있었지만, 고가용성 클러스터에서 실행되는 서비스에 의존하는 서비스도 있었습니다. 이러한 종속성은 너무 엄격하지 않았어야 했고, 좀 더 예측 가능하게 중지되어야 했으며, Cloudflare에서 이를 포착했어야 했습니다.

Cloudflare에서는 다른 두 데이터 센터 시설 각각(그리고 둘 다)을 완전히 오프라인 상태로 전환하여 고가용성 클러스터를 테스트했습니다. 또한 PDX-04의 고가용성 부분을 오프라인으로 전환하는 테스트도 진행했습니다. 하지만 PDX-04 시설 전체를 완전히 오프라인으로 전환하는 테스트는 한 번도 해본 적이 없었습니다. 그 결과 데이터 영역에서의 이러한 종속성 중 일부의 중요성을 놓치고 있었습니다.

또한 새로운 제품 및 관련 데이터베이스가 고가용성 클러스터와 통합되도록 요구하는 것에 대해서도 너무 느슨하게 대처했습니다. Cloudflare를 이용하면 여러 팀에서 빠르게 혁신할 수 있습니다. 따라서 제품은 초기 알파를 달성하기까지 각기 다른 경로를 거치는 경우가 많습니다. 시간이 지남에 따라 이러한 서비스의 백엔드를 모범 사례에 따라 마이그레이션하는 것이 관행이지만, Cloudflare에서는 제품이 일반 사용 가능(GA)으로 선언되기 전에는 공식적으로 이를 요구하지 않았습니다. 이는 제품에 따라 Cloudflare에서 마련한 이중화 보호 기능이 일관성 없이 작동한다는 것을 의미했기 때문에 실수였습니다.

또한, Cloudflare의 너무 많은 서비스가 핵심 시설의 가용성에 의존하고 있습니다. 많은 소프트웨어 서비스가 이러한 방식으로 제공되기는 하지만, 이는 Cloudflare의 강점으로 작용하지는 않습니다. Cloudflare는 분산 시스템에 능숙합니다. 이 사고 기간 동안 Cloudflare의 전역 네트워크는 예상대로 계속 작동했습니다. Cloudflare의 일부 제품 및 기능은 코어 없이도 네트워크 에지를 통해 구성하고 서비스할 수 있지만, 요즘에는 코어를 사용할 수 없는 경우 너무 많은 제품이 기능을 발휘하지 못합니다. Cloudflare에서는 모든 고객에게 제공하는 분산 시스템 제품을 모든 서비스에 사용해야 합니다. 그래야 핵심 시설에 장애가 발생하더라도 대부분 정상적으로 작동합니다.

### 재해 복구

12:48(UTC)에 Flexential에서는 발전기를 재가동할 수 있었습니다. 해당 시설 일부에 전기 공급이 재개되었습니다. 데이터센터의 전원을 복구할 때는 시스템에 과부하가 걸리지 않도록 일반적으로 한 번에 한 회로씩 전원을 다시 켜는 방식으로 점진적으로 진행됩니다. 주거용 주택의 회로 차단기와 마찬가지로 각 고객은 이중화 차단기를 통해 서비스를 받습니다. Flexential에서 Cloudflare의 회로에 전원을 다시 공급하려고 시도했을 때 회로 차단기에 결함이 있는 것으로 밝혀졌습니다. 사고로 인해 접지 결함이나 다른 서지로 인해 차단기가 고장 났는지, 아니면 이전부터 문제가 있었는데 전원이 꺼진 후에야 발견되었는지는 알 수 없습니다.

Flexential에서는 고장 난 차단기를 교체하는 프로세스를 시작했습니다. 시설에서 보유하고 있는 차단기보다 고장 난 차단기가 더 많았으므로 새로운 차단기를 조달해야 했습니다. 예상보다 더 많은 서비스가 오프라인 상태였고 Flexential에서 서비스 복구 시간을 알려주지 않았으므로 Cloudflare에서는 13:40(UTC)에 유럽에 위치한 Cloudflare의 재해 복구 사이트에 장애 조치를 요청했습니다. 다행히도 Cloudflare의 전체 제어판 중 일부만 장애 조치하면 되었습니다. 대부분의 서비스는 두 개의 활성 코어 데이터 센터에 걸쳐 있는 고가용성 시스템에서 계속 실행되었습니다.

Cloudflare에서는 재해 복구 사이트에서 13:43(UTC)에 첫 서비스를 개시했습니다. Cloudflare의 재해 복구 사이트에서는 재해 발생 시 중요한 제어판 서비스를 제공합니다. 재해 복구 사이트에서는 일부 로그 처리 서비스를 지원하지 않지만, 제어판의 다른 부분을 지원하도록 설계되었습니다.

서비스를 시작했을 때, 실패한 API 호출이 서비스를 압도하는 이벤트 처리 충돌 문제를 경험했습니다. Cloudflare에서는 요청량을 제어하기 위해 레이트 리미팅을 구현했습니다. 이 기간에 대부분의 제품을 사용하는 고객은 대시보드 또는 API를 통해 수정할 때 간헐적으로 오류를 경험했을 것입니다. 17:57(UTC)까지 재해 복구 사이트로 성공적으로 이전된 서비스는 안정적이었으며 대부분의 고객은 더 이상 직접적인 영향을 받지 않았습니다. 그러나 일부 시스템에서는 여전히 수동 구성이 필요했으며(예: Magic WAN), 주로 로그 처리 및 일부 맞춤형 API와 관련된 일부 다른 서비스는 Cloudflare에서 PDX-04를 복원할 때까지 계속 사용할 수 없었습니다.

### 일부 제품 및 기능 재시작 지연

일부 제품은 Cloudflare의 재해 복구 사이트에서 제대로 작동하지 않았습니다. 이들 제품은 재해 복구 절차를 완전히 구현하고 테스트하지 않은 더 새로운 제품인 경우가 많았습니다. 여기에는 새 동영상 업로드를 위한 Stream 서비스 및 기타 서비스가 포함되었습니다. Cloudflare 팀은 이러한 서비스를 복구하기 위해 다음의 두 가지 트랙을 동시에 진행했습니다. 1) 재해 복구 사이트에서 다시 구현하고, 2) 고가용성 클러스터로 마이그레이션했습니다.

Flexential에서는 고장난 회로 차단기를 교체하고 두 유틸리티 피드를 모두 복구했으며 22:48(UTC)에 전원의 전압이 안정된 것을 확인했습니다. Cloudflare 팀은 하루 종일 모두 모여 일하고 있었으므로 대부분 휴식을 취하고 아침에 PDX-04로 다시 이동하는 것이 좋겠다는 결정을 내렸습니다. 이 결정으로 인해 완전한 복구가 지연되기는 했지만, 추가적인 실수로 인해 상황이 악화될 가능성은 줄어들었다고 생각합니다.

11월 3일부터 Cloudflare 팀은 PDX-04에서 서비스를 복구하기 시작했습니다. 이 작업은 네트워크 장비를 물리적으로 부팅한 다음 수천 대의 서버에 전원을 공급하고 서비스를 복구하는 것으로 시작되었습니다. 사고 당시 여러 번의 정전이 발생했을 가능성이 높다고 판단했기 때문에 데이터 센터의 서비스 상태는 알 수 없었습니다. 안전하게 복구할 수 있는 유일한 프로세스는 전체 시설의 완전한 부트스트랩을 따르는 것이었습니다.

여기에는 구성 관리 서버를 온라인 상태로 전환하여 시설 복구를 시작하는 수동 프로세스가 포함되었습니다. 재구축하는 데는 3시간이 걸렸습니다. 이를 통해 Cloudflare 팀에서는 서비스를 구동하는 나머지 서버를 부트스트랩으로 재구축할 수 있었습니다. 각 서버를 재구축하는 데는 10분~2시간이 걸렸습니다. 여러 서버에 걸쳐 병렬로 실행할 수는 있었지만, 서비스 간에 내재된 종속성이 있어 일부 서비스를 순차적으로 다시 온라인 상태로 전환해야 했습니다.

2023년 11월 4일 04:25(UTC)을 기준으로 서비스가 완전히 복구되었습니다. 대부분의 고객의 경우, Cloudflare에서 유럽의 핵심 데이터 센터에도 분석을 저장하므로 대시보드와 API에 걸쳐 대부분의 분석에서 데이터가 손실될 수 없습니다. 그러나 EU에서 복제되지 않는 일부 데이터 세트에는 지속해서 격차가 발생합니다. 로그 푸시 기능을 사용하는 고객의 경우, 대부분의 이벤트에서 로그가 처리되지 않으므로 수신되지 않은 항목은 복구되지 않습니다.

### 교훈 및 복원

Flexential 측에서 답변할 필요가 있는 질문이 몇 가지 있습니다. 그러나 Cloudflare에서는 전체 데이터 센터가 장애를 일으킬 수도 있다는 점도 예상해야 합니다. Google에는 중대한 사건이나 위기가 발생하면 코드 옐로우 또는 코드 레드를 선언하는 프로세스가 있습니다. 이러한 경우 엔지니어링 리소스의 대부분 또는 전부가 당면 문제를 해결하는 데 투입됩니다.

Cloudflare에서는 과거에는 이러한 프로세스가 없었지만, 이제는 이러한 프로세스의 Cloudflare만의 버전을 구현해야 한다는 것이 분명해졌습니다. 바로 코드 오렌지입니다. Cloudflare에서는 핵심적이지 않은 모든 엔지니어링 기능을 제어판의 높은 신뢰성을 보장하는 데 집중하도록 전환하고 있습니다. 그 일환으로 다음과 같은 변화가 있을 것으로 예상합니다.

  * 모든 서비스의 제어판 구성에 대하여 핵심 데이터 센터에 대한 종속성을 제거하고 가능한 경우 분산 네트워크에 의해 우선적으로 구동되도록 이동시킴
  * 모든 핵심 데이터 센터가 오프라인 상태인 경우에도 네트워크에서 실행 중인 제어판이 계속 작동하도록 보장함
  * 일반 사용 가능으로 지정된 모든 제품 및 기능은 특정 시설에 대한 소프트웨어 종속성 없이 고가용성 클러스터(핵심 데이터 센터에 의존하는 경우)에 의존해야 할 것을 요구함
  * 일반 사용 가능으로 지정된 모든 제품 및 기능에는 테스트를 거친 안정적인 재해 복구 계획이 마련되어 있도록 요구함
  * 시스템 장애에 따라 영향이 미치는 범위를 테스트하고 장애로 인해 영향을 받는 서비스 수를 최소화함
  * 각 핵심 데이터 센터 시설의 완전한 제거를 포함하여 모든 데이터 센터 기능에 대하여 보다 엄격한 카오스 테스트를 실행함
  * 모든 핵심 데이터 센터에 대한 철저한 감사와 재감사 계획을 통해 당사의 기준을 준수하는지 확인함
  * 모든 핵심 시설에 장애가 발생하더라도 로그가 손실되지 않도록 보장하는 로깅 및 분석 재해 계획을 마련함



앞서 말씀드린 것처럼, 이번 사고를 통해 Cloudflare를 **이** 용해주시는 고객분들이 겪었을 어려움에 다시 한 번 사과의 말씀을 전합니다. Cloudflare에서는 데이터 센터 제공자가 겪은 일련의 연쇄적인 장애에도 견딜 수 있는 적절한 시스템과 절차를 마련해놓고 있지만, 이를 준수하고 알려지지 않은 종속성에 대해 테스트하도록 더욱 엄격하게 시행할 필요가 있습니다. 올해 남은 기간 동안 저와 대다수의 팀원들은 이 문제에 집중적으로 관심을 쏟을 것입니다. 그리고 지난 며칠간의 고통에서 얻은 교훈으로 Cloudflare는 더욱 발전할 것입니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F&t=Cloudflare%20%EC%A0%9C%EC%96%B4%ED%8C%90%20%EB%B0%8F%20%EB%B6%84%EC%84%9D%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%A4%91%EB%8B%A8%20%EC%82%AC%ED%9B%84%20%EB%B6%84%EC%84%9D)[](https://x.com/intent/post?text=Cloudflare+%EC%A0%9C%EC%96%B4%ED%8C%90+%EB%B0%8F+%EB%B6%84%EC%84%9D+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8+%EC%82%AC%ED%9B%84+%EB%B6%84%EC%84%9D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://bsky.app/intent/compose?text=Cloudflare+%EC%A0%9C%EC%96%B4%ED%8C%90+%EB%B0%8F+%EB%B6%84%EC%84%9D+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8+%EC%82%AC%ED%9B%84+%EB%B6%84%EC%84%9D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://mastodonshare.com/?text=Cloudflare+%EC%A0%9C%EC%96%B4%ED%8C%90+%EB%B0%8F+%EB%B6%84%EC%84%9D+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8+%EC%82%AC%ED%9B%84+%EB%B6%84%EC%84%9D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)[](https://www.threads.net/intent/post?text=Cloudflare+%EC%A0%9C%EC%96%B4%ED%8C%90+%EB%B0%8F+%EB%B6%84%EC%84%9D+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8+%EC%82%AC%ED%9B%84+%EB%B6%84%EC%84%9D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fpost-mortem-on-cloudflare-control-plane-and-analytics-outage%2F)

## 관련 태그

[사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
