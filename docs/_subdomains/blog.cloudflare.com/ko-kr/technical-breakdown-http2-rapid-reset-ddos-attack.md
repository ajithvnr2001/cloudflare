---
url: https://blog.cloudflare.com/ko-kr/technical-breakdown-http2-rapid-reset-ddos-attack/
title: HTTP/2 Rapid Reset: \uae30\ub85d\uc801\uc778 \uacf5\uaca9\uc758 \ubd84\uc11d | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:18.450783+00:00
---

# HTTP/2 Rapid Reset: 기록적인 공격의 분석 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/technical-breakdown-http2-rapid-reset-ddos-attack/

[블로그](https://blog.cloudflare.com/ko-kr/)

[DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[Vulnerabilities](https://blog.cloudflare.com/ko-kr/tag/vulnerabilities/)[공격](https://blog.cloudflare.com/ko-kr/tag/attacks/)+22개의 태그 더 보기

5개 태그5개 태그 보기

  * 게시물 태그
  * [DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[공격](https://blog.cloudflare.com/ko-kr/tag/attacks/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[추세](https://blog.cloudflare.com/ko-kr/tag/trends/)
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



[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[추세](https://blog.cloudflare.com/ko-kr/tag/trends/)

[DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[Vulnerabilities](https://blog.cloudflare.com/ko-kr/tag/vulnerabilities/)[공격](https://blog.cloudflare.com/ko-kr/tag/attacks/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[추세](https://blog.cloudflare.com/ko-kr/tag/trends/)

2023년 10월 10일

# HTTP/2 Rapid Reset: 기록적인 공격의 분석

![Lucas Pardue](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44S1ZEGFAAY82ZM1A53KHB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Julien Desgats](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490NXEPS0Y3GYM6MEBDP98.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Lucas Pardue](https://blog.cloudflare.com/ko-kr/author/lucas/) 및 [Julien Desgats](https://blog.cloudflare.com/ko-kr/author/julien-desgats/)

20분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/), [Deutsch](https://blog.cloudflare.com/de-de/technical-breakdown-http2-rapid-reset-ddos-attack/), [Español](https://blog.cloudflare.com/es-es/technical-breakdown-http2-rapid-reset-ddos-attack/), [Français](https://blog.cloudflare.com/fr-fr/technical-breakdown-http2-rapid-reset-ddos-attack/), [日本語](https://blog.cloudflare.com/ja-jp/technical-breakdown-http2-rapid-reset-ddos-attack/), [繁體中文](https://blog.cloudflare.com/zh-tw/technical-breakdown-http2-rapid-reset-ddos-attack/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/technical-breakdown-http2-rapid-reset-ddos-attack/).

![BLOG-2023 Embedded Image - mLN7qf](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48WDXXVR9MBXJX2BC6M78M.png&w=1600&h=901&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////9PLz5+br4uPt5Ofz6O3z6+/v////////7Orx19bm0NHn2Nvu5Ojx6+/w////////5OPxxsXivsDiztHq4eTx7fDy////////4+P0wcHkurzjztDs5Of08fT2////////7Oz6z9Dty8zt29307fD69/r7////////+vr/5uf65OX67/D/+fz//v//////////////+vv/+fr/////////////////////////////////////////////)

Cloudfare에서는 2023년 8월 25일부터 다수의 고객을 향한 일반적이지 않은 일부 대규모 HTTP 공격을 발견했습니다. 이 공격은 우리의 자동 DDos 시스템에서 탐지하여 완화되었습니다. 하지만 얼마 지나지 않아 기록적인 규모의 공격이 시작되어, 나중에 최고조에 이르러서는 초당 2억 1백만 요청이 넘었습니다. 이는 우리 [기록상 가장 대규모 공격이었던 이전의 공격](https://blog.cloudflare.com/ko-kr/cloudflare-mitigates-record-breaking-71-million-request-per-second-ddos-attack-ko-kr/)의 거의 3배에 달하는 크기입니다.

_공격을 받고 있거나 추가 보호가 필요하신가요?[여기를 클릭하여 도움을 받으세요](https://www.cloudflare.com/h2/)._  


우려되는 부분은 공격자가 머신 20,000개로 이루어진 봇넷만으로 그러한 공격을 퍼부을 수 있었다는 사실입니다. 오늘날의 봇넷은 수십만 혹은 수백만 개의 머신으로 이루어져 있습니다. 웹 전체에서 일반적으로 초당 10억~30억 개의 요청이 목격된다는 점을 생각하면, 이 방법을 사용했을 때 웹 전체 요청에 달하는 규모를 소수의 대상에 집중시킬 수 있다는 가능성도 완전히 배제할 수는 없습니다.

## 감지 및 완화

이는 전례 없는 규모의 새로운 공격 벡터였으나, Cloudflare는 기존 보호 기능을 통해 치명적인 공격을 대부분 흡수할 수 있었습니다. 처음에 목격된 충격은 초기 공격 웨이브 동안 고객 트래픽 요청의 약 1%에 영향을 주었으나, 현재는 완화 방법을 개선하여 시스템에 영향을 주지 않고 Cloudflare 고객을 향한 공격을 차단할 수 있습니다.

우리는 업계의 다른 주요 대기업인 Google과 AWS에서도 같은 시기에 이러한 공격이 있었음을 알게 되었습니다. 이에 따라 지금은 우리의 모든 고객을 이 새로운 DDoS 공격 방법으로부터 어떤 영향도 받지 않도록 보호하기 위하여 Cloudflare의 시스템을 강화했습니다. 또한 Google 및 AWS와 협력하여 영향을 받은 업체와 주요 인프라 제공 업체에 해당 공격을 알렸습니다.

이 공격은 HTTP/2 프로토콜과 서버 구현 세부 사항의 일부 주요 기능을 악용했기에 가능했습니다(자세한 내용은 [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487) 참조). HTTP/2 프로토콜의 숨어 있는 약점을 파고들었던 공격이었기 때문에, HTTP/2을 구현한 업체라면 해당 공격의 대상이 될 것이라 판단하고 있습니다. 여기에는 요즘의 모든 웹 서버가 포함됩니다. 우리는 Google 및 AWS와 더불어 패치를 구현할 것이라 예상하고 있는 웹 서버 업체를 향한 해당 공격 방법을 공개해왔습니다. 그 동안 최고의 방어는 웹을 대면하는 웹과 API 서버의 프론트에 Cloudflare와 같이 DDoS 완화 서비스를 적용하는 것입니다.

이 포스팅에서는 HTTP/2 프로토콜의 세부 사항, 즉 공격자가 대규모 공격을 만들어내는 데 악용한 주요 기능과 모든 고객을 보호하기 위해 Couldfare가 채택한 완화 전략을 상세히 살펴봅니다. 우리의 희망은 이러한 세부 사항을 공개해 영향을 받는 다른 웹 서버와 서비스에서 완화 전략 구현에 필요한 정보를 갖추는 것입니다. 또한 이에 그치지 않고, HTTP/2 프로토콜 표준 팀과 미래의 웹 표준을 수립하는 팀에서 더 나은 설계를 내놓아 이와 같은 공격을 예방하는 것입니다.

## RST 공격 세부 내용

HTTP는 웹을 구동하는 애플리케이션 프로토콜입니다. [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)는 HTTP의 모든 버전, 즉 전반적 아키텍처, 용어, 프로토콜 측면(예: 요청 및 응답 메시지, 메서드, 상태 코드, 헤더 및 트레일러 필드, 메시지 내용 등)에서 공통입니다. 각 HTTP 버전은 인터넷에서 상호작용을 위해 "와이어 포맷"으로 시맨틱을 변환하는 방법을 정의합니다. 예를 들어 클라이언트가 요청 메시지를 바이너리 데이터로 직렬화한 후 전송하면, 서버는 이를 다시 처리할 수 있는 메시지로 다시 구문 분석합니다.

[HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html)은 직렬화된 텍스트 형식을 사용합니다. 요청과 응답 메시지는 ASCII 문자의 스트림으로 교환되고, TCP처럼 안정적인 전송 계층을 통해 다음 [형식](https://www.rfc-editor.org/rfc/rfc9112.html#section-2.1)(CRLF는 캐리지 리턴 및 줄바꿈을 의미)으로 전송됩니다.
    
    
     HTTP-message   = start-line CRLF
                       *( field-line CRLF )
                       CRLF
                       [ message-body ]

예를 들어, `https://blog.cloudflare.com/` 에 대한 매우 간단한 GET 요청은 와이어에서 다음과 같이 표시됩니다:

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

그리고 응답은 다음과 같습니다:

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

이 형식은 와이어에서 메시지의 형식을 정의하는데, 이는 단일 TCP 연결을 사용하여 다수의 요청과 응답을 주고받을 수 있다는 의미입니다. 그러나 이 형식은 각 메시지를 전체로 보내야 합니다. 추가로 요청과 응답을 정확하게 상호 연결하려면 순서를 엄격하게 지켜야 합니다. 즉, 메시지는 직렬로 교환되고, 다중화될 수 없습니다. `https://blog.cloudflare.com/`과 `https://blog.cloudflare.com/page/2/`에 대한 두 개의 GET 요청은 다음과 같이 표시됩니다:

`GET / HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLFGET /page/2/ HTTP/1.1 CRLFHost: blog.cloudflare.comCRLFCRLF`

응답은 다음과 같습니다.

`HTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>CRLFHTTP/1.1 200 OK CRLFServer: cloudflareCRLFContent-Length: 100CRLFtext/html; charset=UTF-8CRLFCRLF<100 bytes of data>`

웹 페이지에는 예시보다 더 복잡한 HTTP 상호작용이 필요합니다. Cloudflare 블로그를 방문할 때 브라우저는 여러 스크립트, 스타일, 미디어 에셋을 로드합니다. HTTP/1.1로 해당 페이지를 방문하고, 빠르게 다음 페이지로 넘어가고자 할 때, 브라우저는 2가지 선택지 중 하나를 고를 수 있습니다. 페이지가 시작하기도 전에 이제는 원하지 않는 다음 페이지에 대해 대기 중인 모든 응답을 기다리거나, TCP 연결을 닫고 새로운 연결을 열어 전송 중인 요청을 취소할 수 있습니다. 2가지 선택지 모두 그다지 실용적이지는 않습니다. 브라우저는 TCP 연결 풀(호스트당 최대 6개)을 관리하고 풀에서 복잡한 요청 전송 로직을 구현하며 이러한 제한을 준수합니다.

[HTTP/2](https://www.rfc-editor.org/rfc/rfc9113)에서는 HTTP/1.1에서 발생한 문제 대부분이 해결됩니다. 각 HTTP 메시지는 유형, 길이, 플래그, 스트림 식별자(ID), 페이로드가 있는 **HTTP/2 프레임** 조합으로 직렬화됩니다. 스트림 ID는 와이어의 어떤 바이트가 어떤 메시지에 적용되는지 분명히 하는 동시에 안전하게 다중화하고 동시성을 부여합니다. 스트림은 양방향입니다. 클라이언트가 프레임을 전송하면, 서버는 같은 ID를 사용하는 프레임으로 응답합니다.

HTTP/2에서 `https://blog.cloudflare.com`에 대한 GET 요청은 스트림 ID 1을 통해 교환됩니다. 클라이언트가 1개의 [HEADERS](https://www.rfc-editor.org/rfc/rfc9113#name-headers) 프레임을 보내면 서버는 1개의 HEADERS 프레임과 뒤이어 1개 이상의 [DATA](https://www.rfc-editor.org/rfc/rfc9113#name-data) 프레임으로 응답합니다. 클라이언트가 요청하는 스트림 ID는 항상 홀수이므로, 후속 요청은 스트림 ID 3, 5 등이 됩니다. 응답은 순서와 관계없이 전달되고, 다른 스트림의 프레임이 인터리빙될 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - x9QxRg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49B9T4FFZW2YJF9EFMJGRE.png&w=715&h=221&f=webp&fit=cover&position=center)

스트림 다중화와 동시성은 HTTP/2의 강력한 주요 특징입니다. 두 이점은 단일 TCP 연결의 더욱 더 효율적인 사용을 지원합니다. HTTP/2는 [우선순위 지정](https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/)과 짝을 이룰 때 특히나 리소스 가져오기를 최적화합니다. 반대로 생각해보면, 클라이언트의 대규모 병렬 작업을 수월하게 시행할 수 있게 만들어 줌으로써 HTTP/1.1과 비교했을 때, 서버 리소스에 대한 피크 수요가 높아집니다. 이는 서비스 거부에 대한 분명한 벡터입니다.

HTTP/2는 약간의 방어 수단을 제공하기 위해 최대 활성 [동시 스트림](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2)의 개념을 제시합니다. [SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_FRAME_SIZE) 매개변수는 서버가 자신의 동시성 제한을 알릴 수 있도록 합니다. 예를 들어, 서버에 100개로 제한을 둔다면, 어느 시점에서도 100개의 요청만이 활성화될 수 있습니다. 클라이언트가 제한을 초과하는 스트림을 열고자 한다면, 이 시도는 [RST_STREAM](https://www.rfc-editor.org/rfc/rfc9113#section-6.4) 을 사용하는 서버에서 거부되어야 합니다. 스트림 거부는 연결 상의 이동 중인 다른 스트림에 영향을 주지 않습니다.

실제 이야기는 조금 더 복잡합니다. 스트림에는 [수명 주기](https://www.rfc-editor.org/rfc/rfc9113#section-5.1)가 있습니다. 아래 HTTP/2 스트림 상태인 기기의 도표가 나와있습니다. 클라이언트와 서버는 스트림 상태인 자신의 뷰를 관리합니다. HEADERS, DATA, RST_STREAM 프레임은 전송되거나 수신될 때, 전환을 유발합니다. 스트림 상태의 뷰는 독립적이기는 하지만, 동기화됩니다.

HEADERS와 DATA 프레임에는 값이 1(true)로 설정되었을 때, 상태 전환을 일으킬 수 있는 END_STREAM이 포함되어 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - dgpLal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45G749M08PSFAAXZRQE5DQ.png&w=715&h=515&f=webp&fit=cover&position=center)

메시지 내용이 없는 GET 요청의 예시를 자세히 살펴보겠습니다. 클라이언트는 END_STREAM 플래그 조합을 1로 설정한 HEADERS 프레임으로 요청을 전송합니다. 클라이언트는 먼저 스트림 상태를 유휴에서 열림 상태로 전환한 다음, 곧바로 **반 닫힘** 상태로 전환합니다. 클라이언트의 반 닫힘 상태란 더 이상 HEADERS 또는 DATA를 보낼 수 없고, [WINDOW_UPDATE](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.9), [PRIORITY](https://www.rfc-editor.org/rfc/rfc9113.html#section-6.3) 또는 RST_STREAM 프레임만을 보낼 수 있는 상태를 말합니다. 하지만 클라이언트가 받는 프레임의 종류에는 제한이 없습니다.

서버가 HEADERS 프레임을 받아 구문 분석하고 나면 스트림 상태를 유휴에서 열림, 그리고 반 닫힘 상태로 전환해 클라이언트와 상태를 일치시킵니다. 서버가 반 닫힘 상태라는 의미는 어떤 프레임이든지 보낼 수 있지만, WINDOW_UPDATE, PRIORITY, RST_STREAM만 받을 수 있는 상태를 말합니다.

GET에 대한 응답에는 메시지 내용이 포함되므로 서버에서는 0으로 설정된 END_STREAM 플래그가 포함된 HEADERS를 보내고 난 다음, 1로 설정한 END_STREAM 플래그가 포함된 HEADERS를 보냅니다. DATA 프레임은 서버에서 스트림이 **반 닫힘** 상태에서 닫힘 상태로 전환되게 합니다. 클라이언트가 DATA 프레임을 받으면, 클라이언트 또한 닫힘 상태로 전환됩니다. 스트림이 닫히고 나면 어떤 프레임도 보내거나 받을 수 없습니다.

수명 주기를 동시성 컨텍스트에 다시 적용하면 HTTP/2는 [다음과 같이 나타납니다](https://www.rfc-editor.org/rfc/rfc9113#section-5.1.2-2):

_"열림" 상태이거나 "반 닫힘" 상태인 스트림은 엔드포인트가 열 수 있도록 허용된 최대 스트림 수에 포함됩니다. 이 세 가지 상태 중 하나에 있는 스트림은_ [_SETTINGS_MAX_CONCURRENT_STREAMS_](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS) _설정에서 통지된 한도에 포함됩니다._

이론상, 동시성 제한은 유용합니다. 그렇지만, 그 효과를 방해하는 실용적인 요소가 있으며, 이는 블로그 뒷 부분에서 다룰 예정입니다.

### HTTP/2 요청 취소

앞서 전송 중인 요청의 클라이언트 취소에 관해 설명했습니다. HTTP/2에서는 이를 HTTP/1.1보다 더 효율적인 방식으로 지원합니다. 클라이언트는 전체 연결을 끊지 않고도 단일 스트림에 대한 RST_STREAM 프레임을 보낼 수 있습니다. 이로 인해 서버는 요청 처리를 멈추고, 응답을 중단함으로써, 서버 리소스를 확보하고 대역폭 낭비를 방지할 수 있습니다.

앞선 예시인 3개의 요청을 살펴보겠습니다. 이번에는 클라이언트가 모든 HEADERS를 보내고 난 후에 스트림 1의 요청을 취소하는 경우를 가정해 보겠습니다. 서버는 응답을 보낼 준비를 하기 전에 이 RST_STREAM 프레임을 구문 분석하고 그 대신 스트림 3과 5에 대해서만 응답합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - alylDM](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48VGZF708M4TQDMQVJN3F2.png&w=715&h=225&f=webp&fit=cover&position=center)

요청 취소는 유용한 기능입니다. 예를 들어, 여러 이미지가 있는 웹 페이지를 스크롤할 때, 웹 브라우저는 뷰포트에서 벗어난 이미지를 취소할 수 있는데, 다시 말해 뷰포트로 들어오는 이미지는 더 빨리 로드된다는 의미입니다. HTTP/1.1과 비교했을 때 HTTP/2가 이러한 행위를 훨씬 더 효율적으로 수행합니다.

취소된 요청 스트림은 스트림 수명주기를 통해 빠르게 전환됩니다. END_STREAM 플래그가 1로 설정된 HEADERS는 클라이언트를 유휴 상태에서 열림, **반 닫힘** 상태로 전환시키고, 이어서 RST_STREAM이 곧바로 **반 닫힘** 상태에서 **닫힘** 상태로 전환시킵니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - FOxdTz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SPXM07R6QG2B8FEXJCHJ.png&w=715&h=515&f=webp&fit=cover&position=center)

열림 또는 반 닫힘 상태의 스트림만이 스트림 동시성 제한에 영향을 미친다는 점을 상기해 보세요. 클라이언트가 스트림을 취소하면 즉시 그 자리에 다른 스트림을 열 수 있고 바로 다른 요청을 보낼 수도 있습니다. 이는 [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)을 작동시키는 핵심입니다.

### 서비스 거부로 이어지는 Rapid Reset

HTTP/2 요청 취소는 무한한 스트림을 빠르게 초기화하는 데 악용될 수 있습니다. HTTP/2 서버가 클라이언트가 보낸 RST_STREAM 프레임을 처리할 수 있고, 충분히 빠르게 상태를 분해할 수 있다면, Rapid Reset은 문제가 되지 않습니다. 정리 과정에서 지연이나 처짐이 발생할 때 문제가 발생하기 시작합니다. 이때 클라이언트는 작업 백로그를 누적시키는 많은 요청으로 인해 이탈될 수 있으며, 이는 서버 리소스의 과도한 소모로 이어집니다.

일반적인 HTTP 배포 아키텍처는 다른 구성 요소보다 앞서서 HTTP/2 프록시 또는 부하 분산 장치를 실행할 수 있습니다. 클라이언트 요청이 도착하면 빠르게 전송되고, 실제 작업은 다른 곳에서 비동기 활동으로 이루어집니다. 이로 인해 프록시는 클라이언트 트래픽을 매우 효율적으로 처리할 수 있습니다. 그러나 이러한 분리로 인해 프록시가 처리 중인 작업은 정리하는 것이 어려워질 수 있습니다. 따라서 이러한 배포는 Rapid Reset로 인한 문제를 만날 가능성이 더 높습니다.

Cloudflare의 [역프록시](https://www.rfc-editor.org/rfc/rfc9110#section-3.7-6)가 수신되는 HTTP/2 클라이언트 트래픽을 처리할 때, 연결의 소켓에서 버퍼로 데이터를 복사한 다음 버퍼에 있는 데이터를 순서대로 처리합니다. 각 요청을 읽으면(HEADER와 DATA 프레임) 이는 업스트림 서비스로 전송됩니다. RST_STREAM 프레임을 읽으면, 해당 요청에 대한 로컬 상태는 해체되고, 업스트림에서는 요청이 취소되었다는 알림을 받습니다. 버퍼를 비우고 버퍼 전체가 사용될 때까지 이를 반복합니다. 하지만 이 로직은 악용될 수 있습니다. 그 이유는 악의적 클라이언트가 연결을 시작할 때 엄청난 양의 요청과 초기화 체인을 보내기 시작하면, 우리의 서버는 의욕이 넘쳐서 체인을 모두 읽고, 업스트림 서버에 새롭게 수신되는 요청을 처리할 수 없는 시점까지 압력을 만들어내기 때문입니다.

짚고 넘어가야 하는 중요한 점은 그 자체의 스트림 동시성이 Rapid Reset를 완화시켜줄 수 없다는 것입니다. 클라이언트는 요청이 서버의 [SETTINGS_MAX_CONCURRENT_STREAMS](https://www.rfc-editor.org/rfc/rfc9113#SETTINGS_MAX_CONCURRENT_STREAMS) 설정 값과 관계 없이 높은 요청 속도를 만들어낼 수 있습니다.

### Rapid Reset 분석

여기 총 1,000건의 요청을 생산하려는 개념 증명 클라이언트로 재생산된 Rapid Reset의 예가 있습니다. 여기서는 어떤 완화도 없는 상용 서버를 사용했으며, 테스트 환경에서는 443 포트가 수신 대기 중입니다. 트래픽은 Wireshark로 분석되며, 명확성을 위해 HTTP/2 트래픽만을 표시하도록 필터링됩니다. [pcap을 다운로드](http://staging.blog.mrk.cfdata.org/content/images/rapidreset.pcapng)하여 다음을 확인하세요.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - WbJayy](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46CJJHBWXXWMSQCY94SYWG.png&w=715&h=35&f=webp&fit=cover&position=center)

프레임이 많으므로 트래픽을 확인하는 데 조금 어려울 수 있습니다. Wireshark 통계 > HTTP2 툴을 통한 빠른 요악을 받아볼 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - hiRPjv](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44JCSEZW1GJBEZC3CJVBK1.png&w=715&h=219&f=webp&fit=cover&position=center)

패킷 14에서 이 트레이스의 첫 번째 프레임은 서버의 SETTINGS 프레임으로, 최대 100개의 스트림 동시성을 알립니다. 패킷 15에서 클라이언트는 몇몇 제어 프레임을 보낸 다음 Rapid Reset이 되는 요청을 시작합니다. 첫 번째 HEADERS 프레임은 26바이트이고, 모든 후속 HEADERS는 9바이트에 불과합니다. 이 크기 차이는 [HPACK](https://blog.cloudflare.com/hpack-the-silent-killer-feature-of-http-2/)이라는 압축 기술 덕분입니다. 패킷 15에는 총 525개의 요청이 포함되어 있으며, 스트림 1051까지 올라갑니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - 4zuXCV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497JBM72881G9RYDWRT2C6.png&w=619&h=593&f=webp&fit=cover&position=center)

흥미롭게도 스트림 1051에 대한 RST_STREAM은 패킷 15에 맞지 않아 패킷 16에서 서버가 404로 응답하는 것을 볼 수 있습니다. 그 후에 클라이언트는 패킷 17에서 나머지 475개의 요청을 전송하기 전에 RST_STREAM을 전송합니다.

서버에서는 동시 스트림이 100개라고 알렸으나, 클라이언트에서 보낸 2개의 패킷 모두 그보다 훨씬 더 많은 HEADERS 프레임을 보냈습니다. 클라이언트는 서버로부터의 응답 트래픽을 기다릴 필요가 없었고, 보낼 수 있는 패킷의 크기에 따른 제한만을 받았습니다. 이 트레이스에서 서버의 RST_STREAM 프레임이 전혀 보이지 않는 것은 서버가 동시 스트림 위반을 관찰하지 못했음을 말해줍니다.

## 고객에게 미치는 영향

위에서 언급한 것과 같이 요청이 취소되면 업스트림 서비스는 알림을 전달받고, 너무 많은 리소스를 낭비하기 전에 요청을 중단할 수 있습니다. 이번 공격 케이스에서도 마찬가지였고, 대부분의 악의적 요청은 원본 서버로 전혀 포워딩되지 않았습니다. 그렇지만, 그 공격의 규모만으로도 일부 영향이 있었습니다.

첫째, 들어오는 요청의 속도가 이전에는 볼 수 없었던 최고치에 도달함에 따라, 고객의 502 오류 보고 횟수가 늘었다는 보고가 있었습니다. 이는 가장 지대한 영향을 받은 데이터 센터에서 모든 요청을 처리하기 위해 분투하는 과정에서 발생했습니다. 우리의 네트워크는 대규모 공격에 대응할 수 있도록 설계되었음에도, 이 특정한 취약점으로 인해 인프라의 약점이 노출되었습니다. 이제 더 세부 사항으로 들어가서, 데이터센터 중 한 곳에 공격이 발생했을 때, 들어오는 요청이 어떻게 처리되는지에 초점을 맞추어 보겠습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - ZsURSu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45571VPJA9ST5WBRH9KPG8.png&w=715&h=269&f=webp&fit=cover&position=center)

Cloudflare 인프라는 각각 다른 책임을 맡은 여러 프록시 서버 체인으로 구성되어 있음을 확인할 수 있습니다. 특히 클라이언트가 HTTPS 트래픽을 전송하기 위해 Cloudflare에 연결하면 먼저 TLS 복호화 프록시에 연결됩니다. 프록시는 TLS 트래픽을 복호화하고 HTTP 1, 2 또는 3 트래픽을 처리한 다음, 이를 "비즈니스 로직" 프록시로 포워딩합니다. 이 프록시는 각 고객에 대한 모든 설정을 로드하고, 요청을 다른 업스트림 서비스로 정확하게 라우팅하는데, **이 케이스에서는 그보다 더 중요한 보안 기능도 담당합니다**. L7 공격 완화도 이 프록시에서 처리됩니다.

이번 공격 벡터의 문제점은 모든 연결에서 매우 빠르게 다량의 요청을 보낼 수 있다는 사실입니다. 우리가 공격 벡터를 차단할 기회를 갖기도 전에 각 요청이 비즈니스 로직 프록시로 포워딩되어야 했습니다. 요청 처리량이 프록시 용량을 앞지르면서 이 두 서비스를 연결하는 채널이 우리의 일부 서버에서는 포화 상태에 도달했습니다.

이렇게 되면 TLS 프록시가 업스트림 프록시에 더 이상 연결될 수 없으며, 이것이 몇몇 클라이언트에서 가장 심각한 공격 중 소량의 "502 Bad Gateway" 오류가 발생했던 원인입니다. 주목해야 할 점은 오늘 현재 HTTP 분석을 생성하기 위해 사용하는 로그 또한 비즈니스 로직 프록시에서 전송된다는 사실입니다. 그 결과, 이러한 오류는 Cloudflare 대시보드에서 보이지 않습니다. 내부 대시보드에서는 초기 공격 웨이브(완화 조치를 구현하기 전) 중 약 1%의 요청이 영향을 받았으며, 가장 심각한 공격이 발생했던 8월 29일에는 수 초 동안 약 12%를 기록하며, 최고치를 달성했습니다. 다음 그래프에는 공격이 발생한 2시간 동안 오류의 비율이 나와있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - cDLXgV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H86FX527NRYXEFG5HNZH.png&w=715&h=442&f=webp&fit=cover&position=center)

이 글 아래에서 설명될 내용과 같이 그다음 날에는 이 숫자를 극적으로 낮추는 작업이 진행되었습니다. 스택의 변화와 이러한 공격 규모를 상당히 감소시킨 완화 조치 덕분에 현재 이 수치는 사실상 0입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - AfViXl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW484F1GN0TB062910TF1AD8.png&w=715&h=442&f=webp&fit=cover&position=center)

### 499 오류 및 HTTP/2 스트림 동시성의 문제

일부 고객이 알려온 또 다른 증상은 499 오류의 증가입니다. 그 이유는 조금 다른데, 이는 앞서 설명한 HTTP/2 연결의 최대 스트림 동시성 수와 관련이 있습니다.

HTTP/2 설정은 SETTINGS 프레임을 사용해 연결이 시작될 때 교환됩니다. 명시적 매개변수를 받지 않은 경우에는 기본값이 적용됩니다. 클라이언트가 HTTP/2 연결을 설정하고 나면, 서버의 SETTINGS(느림)를 기다리거나, 기본값을 가정하고 요청(빠름)을 시작할 수 있습니다. SETTINGS_MAX_CONCURRENT_STREAMS의 기본값은 사실상 무제한입니다(스트림 ID는 31비트 숫자 공간을 사용, 요청은 홀수를 사용하므로 실제 제한은 1073741824). 사양에서는 서버에서 100개 이상의 스트림을 제공하기를 권장합니다. 클라이언트는 일반적으로 속도에 편향되어 있으므로 서버 설정을 기다리지 않는 경향이 있으며, 이로 인해 약간의 경쟁 조건이 만들어집니다. 클라이언트는 서버에서 어떤 제한을 선택할지 도박을 하는 것과 같습니다. 잘못 선택한다면, 요청은 거부되고, 다시 시도해야 하기 때문입니다. 1073741824 스트림에 대한 도박은 다소 어리석은 일입니다. 그 대신 다수의 클라이언트는 서버가 사양 권장 사항을 따르기를 바라면서, 100개의 동시 스트림으로 제한할 것을 결정합니다. 서버가 100개 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - VLKjcD](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46456QGGZGE6J54D0S0W49.png&w=715&h=246&f=webp&fit=cover&position=center)

미만을 선택한다면, 클라이언트의 도박은 실패하고 스트림은 초기화됩니다.

서버가 동시성 제한을 초과한 스트림을 초기화하는 데는 여러가지 이유가 있습니다. HTTP/2는 프로토콜이 엄격하고, 구문 분석이 있거나 로직 오류가 있을 때 스트림을 닫아야 합니다. 2019년, Cloudflare에서는 [HTTP/2 DoS 취약점](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/)에 대응해 몇 가지 완화 조치를 개발했습니다. 몇몇 취약점은 클라이언트의 올바르지 않은 행동, 서버에서 스트림을 초기화하도록 이끄는 클라이언트가 그 원인이었습니다. 이러한 클라이언트를 단속하는 매우 효과적인 방법은 연결 중 서버 초기화 횟수를 세고, 몇몇 임계값을 넘을 때 [GOAWAY](https://www.rfc-editor.org/rfc/rfc9113#section-6.8) 프레임으로 연결을 끊는 것입니다. 합법적인 클라이언트라면 연결 시 한두 가지 정도의 실수는 할 수 있습니다. 클라이언트에서 너무 많은 실수를 범한다면, 문제가 있거나 악의를 가진 경우이며, 연결을 끊으면 두 가지 케이스가 모두 해결됩니다.

Cloudflare에서는 [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)으로 활성화된 DoS 공격에 대응하는 동안, 최대 스트림 동시성을 64개로 줄였습니다. 이러한 변화를 주기 전에는 클라이언트에서 SETTINGS를 기다리지 않고 100개의 동시성을 가정한다는 사실을 알지 못했습니다. 이미지 갤러리와 같은 일부 웹 페이지는 연결 시작 시에 곧바로 브라우저가 100개의 요청을 보내도록 하기도 합니다. 하지만, 우리의 제한을 초과한 36개의 스트림은 모두 초기화되어야 했으며, 이는 카운팅 완화 조치의 시행 조건으로 작용했습니다. 이는 합법적인 클라이언트와의 연결을 끊게 만들어 페이지 가져오기의 완전한 실패로 이어졌습니다. 따라서 이 상호운용성 문제를 인지하자마자 최대 스트림 동시성 수를 100개로 변경했습니다.

## Cloudflare 측의 조치

2019년, HTTP/2 구현과 관련한 몇 가지 [DoS 취약점](https://blog.cloudflare.com/on-the-recent-http-2-dos-attacks/)이 발견되었습니다. Cloudflare에서는 이에 대한 대응으로 일련의 감지 및 완화 조치를 개발하고 배포했습니다. [CVE-2023-44487](https://www.cve.org/CVERecord?id=CVE-2023-44487)은 HTTP/2 취약점의 다른 표현입니다. 하지만, 이를 완화하기 위해 기존의 보호 기능을 확장하여 클라이언트가 전송한 RST_STREAM 프레임을 모니터링하고, 악용되는 경우 연결을 닫을 수 있었습니다. 합법적인 클라이언트의 RST_STREAM 사용은 영향을 받지 않습니다.

우리는 직접적인 수정에 그치치 않고, 서버의 HTTP/2 프레임 처리 및 요청 전송 코드에도 몇 가지 개선점을 구현했습니다. 추가로, 비즈니스 로직 서버의 대기열 및 스케줄링 또한 개선해서, 불필요한 작업을 줄이고 취소 응답성을 높일 수 있었습니다. 이러한 개선 모두에 힘입어 다양한 잠재적 남용 패턴의 영향이 줄어들고 서버가 포화 상태에 이르기 전에 요청을 처리할 수 있는 공간이 더 확보됩니다.

### 공격의 조기 완화

Cloudflare에서는 더욱 저렴한 방식으로 대규모 공격을 효율적으로 완화할 수 있는 시스템을 이미 갖추고 있습니다. 그중 하나가 "IP Jail"입니다. IP Jail은 대규모 볼류메트릭 공격 시 공격에 참여하는 클라이언트 IP를 수집하고, 해당 IP 레벨이나 TLS 프록시에서 공격받은 위치와의 연결을 끊습니다. 하지만 이 시스템이 온전히 효과를 발휘하기 위해서는 몇 초가 필요합니다. 이 귀중한 시간에 원본은 보호받지만, 인프라는 여전히 모든 HTTP 요청을 받아들여야 합니다. 이 새로운 봇넷은 사실상 램프업 기간이 없으므로 우리는 문제가 되기 전에 공격을 무력화할 수 있는 능력을 갖추어야 합니다.

우리는 이를 구현하기 위해 전체 인프라를 보호하는 IP Jail 시스템을 확장했습니다. 일단 IP가 "구속되면", 공격받은 위치로의 연결이 차단될 뿐만 아니라, 해당 IP는 일정 시간 Cloudflare의 다른 도메인에 HTTP/2를 사용하는 것도 금지됩니다. 이러한 프로토콜의 악용은 HTTP/1.x로는 불가능하므로, 공격자는 대규모 공격을 퍼부을 수 있는 능력이 제한되는 반면, 동일한 IP를 공유하는 합법적인 클라이언트는 해당 시간 아주 미세한 성능 저하만을 겪습니다. IP 기반의 완화 조치는 매우 무딘 도구이며, 그렇기 때문에 해당 규모로 사용할 때는 극도로 신중을 기해야 하며, 가능한 한 긍정 오류를 피해야 합니다. 또한 봇넷에서 특정 IP의 수명은 일반적으로 짧으므로, 장기간의 완화 조치는 장점보다 단점이 더 많을 수도 있습니다. 다음 그래프에는 우리가 목격한 공격 중 급격한 변화가 나와있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2023 Embedded Image - zEcUBs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BMWNAXCMETHFB5FB79WB.png&w=715&h=348&f=webp&fit=cover&position=center)

그래프에서 확인할 수 있듯이, 다수의 새로운 IP가 특정한 날 이후 매우 빠르게 사라집니다.

이 모든 조치는 HTTPS 파이프라인의 시작 부분에 있는 TLS 프록시에서 이루어지므로 우리의 일반 L7 완화 시스템과 비교했을 때 상당한 리소스를 절약할 수 있습니다. 이로 인해 훨씬 더 원활하게 공격에 대응할 수 있었고, 이제 봇넷으로 인한 무작위 502 오류 수는 0개가 되었습니다.

### 관찰 가능성 개선

Cloudflare에서 변화를 만들어 가고 있는 영역은 관찰 가능성입니다. 고객 분석에서 보이지 않고, 고객에게 오류를 돌려주는 상황은 만족할 수 없는 부분입니다. 다행스럽게도 최근 공격이 발생하기 훨씬 이전부터 해당 시스템을 정비하는 프로젝트가 진행 중이었습니다. 프로젝트의 궁극적인 방향은 비즈니스 로직 프록시에 의존하여 로그 데이터를 통합하고 방출하는 것이 아닌, 인프라 내의 각 서비스가 자체 데이터를 로깅할 수 있는 것입니다. 이번 사고로 인해 해당 작업의 중요성이 대두되었기에, 노력을 배가하고 있습니다.

또한 이러한 프로토콜 악용을 훨씬 더 빠르게 발견해 DDoS 완화 기능을 개선할 수 있는 연결 수준의 로깅 개선 업무도 작업 중입니다.

## 결론

이 사고는 가장 최근의 기록적인 공격이었지만, 이번이 마지막은 아닐 것이라는 사실은 잘 알고 있습니다. 공격이 점점 더 정교해짐에 따라 Cloudflare에서는 새로운 위협을 적극적으로 식별해서 수백만 고객이 즉각적이고 자동적으로 보호받을 수 있도록 전역 네트워크에 대응책을 배포하는 등 끊임없는 노력을 기울이고 있습니다.

Cloudflare는 2017년부터 고객에게 무료로 무제한 DDoS 방어를 제공해 왔습니다. 이와 더불어, 모든 규모의 조직 니즈에 맞는 광범위한 부가 보안 기능 또한 제공합니다. 보호받고 있는지 확신할 수 없거나 어떻게 보호받을 수 있는지 알고 싶다면 [이곳으로 문의하세요](https://www.cloudflare.com/ko-kr/h2/).

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F&t=HTTP%2F2%20Rapid%20Reset%3A%20%EA%B8%B0%EB%A1%9D%EC%A0%81%EC%9D%B8%20%EA%B3%B5%EA%B2%A9%EC%9D%98%20%EB%B6%84%EC%84%9D)[](https://x.com/intent/post?text=HTTP%2F2+Rapid+Reset%3A+%EA%B8%B0%EB%A1%9D%EC%A0%81%EC%9D%B8+%EA%B3%B5%EA%B2%A9%EC%9D%98+%EB%B6%84%EC%84%9D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://bsky.app/intent/compose?text=HTTP%2F2+Rapid+Reset%3A+%EA%B8%B0%EB%A1%9D%EC%A0%81%EC%9D%B8+%EA%B3%B5%EA%B2%A9%EC%9D%98+%EB%B6%84%EC%84%9D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://mastodonshare.com/?text=HTTP%2F2+Rapid+Reset%3A+%EA%B8%B0%EB%A1%9D%EC%A0%81%EC%9D%B8+%EA%B3%B5%EA%B2%A9%EC%9D%98+%EB%B6%84%EC%84%9D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)[](https://www.threads.net/intent/post?text=HTTP%2F2+Rapid+Reset%3A+%EA%B8%B0%EB%A1%9D%EC%A0%81%EC%9D%B8+%EA%B3%B5%EA%B2%A9%EC%9D%98+%EB%B6%84%EC%84%9D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftechnical-breakdown-http2-rapid-reset-ddos-attack%2F)

## 관련 태그

[DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[Vulnerabilities](https://blog.cloudflare.com/ko-kr/tag/vulnerabilities/)[공격](https://blog.cloudflare.com/ko-kr/tag/attacks/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[추세](https://blog.cloudflare.com/ko-kr/tag/trends/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
