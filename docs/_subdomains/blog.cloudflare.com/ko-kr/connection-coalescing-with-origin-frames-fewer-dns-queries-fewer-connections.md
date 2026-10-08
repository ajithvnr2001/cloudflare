---
url: https://blog.cloudflare.com/ko-kr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/
title: ORIGIN Frames\uc640\uc758 \uc5f0\uacb0 \ud1b5\ud569: DNS \ucffc\ub9ac \uac10\uc18c, \uc5f0\uacb0 \uc218 \uac10\uc18c | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:03.129306+00:00
---

# ORIGIN Frames와의 연결 통합: DNS 쿼리 감소, 연결 수 감소 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/

[블로그](https://blog.cloudflare.com/ko-kr/)

[DNS](https://blog.cloudflare.com/ko-kr/tag/dns/)[HTTP2 (KO)](https://blog.cloudflare.com/ko-kr/tag/http2/)[TLS](https://blog.cloudflare.com/ko-kr/tag/tls/)+33개의 태그 더 보기

6개 태그6개 태그 보기

  * 게시물 태그
  * [DNS](https://blog.cloudflare.com/ko-kr/tag/dns/)[HTTP2 (KO)](https://blog.cloudflare.com/ko-kr/tag/http2/)[TLS](https://blog.cloudflare.com/ko-kr/tag/tls/)[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)
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



[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)

[DNS](https://blog.cloudflare.com/ko-kr/tag/dns/)[HTTP2 (KO)](https://blog.cloudflare.com/ko-kr/tag/http2/)[TLS](https://blog.cloudflare.com/ko-kr/tag/tls/)[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)

2023년 9월 4일

# ORIGIN Frames와의 연결 통합: DNS 쿼리 감소, 연결 수 감소

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Jonathan Hoyland](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WSR1Z35ZHN4AZE03JA0Z.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/ko-kr/author/suleman/), [Jonathan Hoyland](https://blog.cloudflare.com/ko-kr/author/jonathan-hoyland/) 및 [Sudheesh Singanamalla](https://blog.cloudflare.com/ko-kr/author/sudheesh/)

16분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/), [Deutsch](https://blog.cloudflare.com/de-de/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/), [Français](https://blog.cloudflare.com/fr-fr/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/), [日本語](https://blog.cloudflare.com/ja-jp/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/), [繁體中文](https://blog.cloudflare.com/zh-tw/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/connection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections/).

![Connection coalescing with ORIGIN Frames: fewer DNS queries, fewer connections](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HDJ2ZAZ6FJXTRPX0N4CN.png&w=1600&h=889&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vfi+fHe7eTV593R6+LU8OrZ7unW5eHN//vn+/Xi8Oja6uHW7eXZ8uzc8OvZ6OTS///s//ro9O3h7ubd8enf9e/i8+/f7OnX///y///u+fPn8+zj9e7l+vTo+PTl8e7d///2///z/vfr+PHn+vTq//nt/fnq9fLi///5///1//vt/PTq//ju//7x//3u+fbl///7///3//3v//fs//vw///0///w/Pnn///8///3//3v//js//zx///1///x/fno)

_이 블로그는 ACM_ _[인터넷 측정 컨퍼런스](https://research.cloudflare.com/publications/Singanamalla2022/)에서 발표된 Cloudflare_ _[연구 논문](https://conferences.sigcomm.org/imc/2022/program/)의 내용을 보고하고 요약한 것으로, ORIGIN Frames와의 연결 통합을 측정하고 프로토타입을 제작하는 내용이 담겨 있습니다._

한 번의 웹 페이지 방문으로 브라우저에서 수십, 때로는 수백 번의 웹 연결이 이루어질 수 있다는 사실에 놀랄 독자도 있을 것입니다. 바로 이 블로그를 예로 들어보겠습니다. Cloudflare 블로그를 처음 방문하거나 마지막으로 방문한 후 오랜 시간이 지난 경우 브라우저는 페이지를 렌더링하기 위해 여러 번 연결합니다. 브라우저는 DNS 쿼리를 수행하여 blog.cloudflare.com에 해당하는 IP 주소를 찾은 다음 전체 페이지를 성공적으로 렌더링하는 데 필요한 웹 페이지에서 필요한 하위 리소스를 검색하기 위해 후속 요청을 수행합니다. 얼마나 될까요? 아래를 보면, 작성 시점에 Cloudflare 블로그를 로드하는 데 32개의 서로 다른 호스트 이름이 사용됩니다. 이는 클라이언트가 이러한 연결 중 일부를 재사용(또는 병합)할 수 있는 경우를 제외하고 32개의 DNS 쿼리와 _최소_ 32개의 TCP(또는 QUIC) 연결을 의미합니다.

새로운 웹 연결은 서버의 처리 능력에 추가적인 부하를 유발하여 사용량이 많은 시간대에 확장성 문제가 발생할 수 있을 뿐만 아니라 개인이 액세스하는 일반 텍스트 호스트 이름과 같은 클라이언트 메타데이터가 네트워크에 노출됩니다. 이러한 메타 정보 때문에 사용자의 온라인 활동과 브라우징 행동이 경로상의 네트워크 공격자 및 도청자에게 노출될 가능성이 있습니다!

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - ckxTYV](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47N3FXQ0TE0F5BAWC0YQTS.png&w=715&h=409&f=webp&fit=cover&position=center)

이 블로그에서는 "연결 병합"에 대해 자세히 살펴보겠습니다. [2021년에 IP 기반 병합](https://blog.cloudflare.com/connection-coalescing-experiments/)에 대해 처음 살펴본 이후, 저희는 인터넷 전반에 걸쳐 대규모 측정과 모델링을 추가로 수행하여 병합이 가장 잘 작동하는 위치와 방법을 이해하고 예측했습니다. IP 병합은 대규모로 관리하기 어려우므로 작년에 저희는 IP 주소 관리에 대한 걱정 없이 에지 연결을 병합하기 위해 [HTTP/2 ORIGIN Frame 확장](https://datatracker.ietf.org/doc/rfc8336/)이라는 유망한 표준을 구현하고 실험을 진행했습니다.

많은 대형 공급자들이 놓치고 있는 기회가 있습니다. 이 블로그(그리고 자세한 내용이 담긴 ACM IMC 2022에서의 저희 [발표물](https://research.cloudflare.com/publications/Singanamalla2022/))가 서버와 클라이언트에서 ORIGIN Frame 표준을 활용하는 데 도움이 되는 첫걸음이 되기를 바랍니다.

### 무대 설정

높은 수준에서 보면, 사용자가 웹을 탐색할 때 브라우저는 종속 하위 리소스를 검색하여 전체 웹 페이지를 구성함으로써 웹 페이지를 렌더링합니다. 이 프로세스는 공장에서 실제 제품을 조립하는 방식과 매우 유사합니다. 이런 의미에서 최신 웹 페이지는 조립 공장과 같다고 볼 수 있습니다. 최신 웹 페이지는 최종 제품을 생산하는 데 필요한 리소스의 "공급망"에 의존합니다.

물리적 세계의 조립 공장에서는 여러 부품을 한 번에 주문하고 공급업체로부터 한 번에 배송받을 수 있으며(가치를 극대화하고 응답 시간을 최소화하는[키팅 프로세스와](https://www.sciencedirect.com/science/article/abs/pii/092552739290109K)유사함), 부품의 제조업체나 생산지와 관계없이 공급업체와의 '연결' 하나만 있으면 됩니다. 공급업체에서 조립 공장으로 이동하는 하나의 트럭에 여러 제조업체의 부품을 실을 수 있습니다.

웹의 설계로 인해 브라우저는 일반적으로 본질적으로 그 반대의 일을 하게 됩니다. 웹 페이지의 이미지, JavaScript, 기타 리소스(부품)를 검색하려면 웹 클라이언트(조립 공장)는 서버(공급업체)가 반환하는 HTML에 정의된 모든 호스트 이름(제조업체)에 _최소한_ 하나의 연결을 생성해야 합니다. 이러한 호스트 이름에 대한 연결이 동일한 서버로 연결되든 그렇지 않든, 예를 들어 Cloudflare와 같은 [리버스 프록시](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/)로 연결되든 상관없습니다. 각 제조업체마다 동일한 공급업체에서 조립 공장으로 자재를 전송하려면 "새로운" 트럭이 필요하거나, 보다 공식적으로는 동일한 웹 페이지의 호스트 이름에서 하위 리소스를 요청하려면 새로운 연결을 생성해야 합니다.

연결 병합 없음

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Without connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46818DS1DBPGY0C4DKT15E.png&w=715&h=305&f=webp&fit=cover&position=center)

웹 페이지를 로드하는 데 사용되는 연결 수는 의외로 많을 수 있습니다. 또한 하위 리소스에 또 다른 하위 리소스가 필요한 경우가 많으므로 이전 연결의 결과로 새로운 연결이 생겨나는 경우도 흔합니다. 호스트 이름에 대한 HTTP 연결은 종종 DNS 쿼리가 앞에 온다는 사실도 기억하세요! 연결 통합을 통해 더 적은 수의 연결을 사용하거나 _동일한 일련의 트럭들을 "재사용"하여 단일 공급업체에서 여러 제조업체의 부품을 운반할 수 있습니다._

연결 병합 적용

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![With connection coalescing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GJXTQ9MV673E7RD0JDJG.png&w=715&h=305&f=webp&fit=cover&position=center)

### 원칙적인 연결 통합

연결 병합은 [HTTP/2에서 도입되어](https://datatracker.ietf.org/doc/html/rfc7540) [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html#name-connection-reuse)으로 이어졌습니다. [이전에](https://blog.cloudflare.com/connection-coalescing-experiments/) 연결 병합에 대해 블로그에 게시한 적이 있습니다(자세한 내용은 해당 블로그를 참조하시기 바랍니다). 아이디어는 간단하지만, 이를 구현하는 데는 여러 가지 엔지니어링 과제가 있을 수 있습니다. 예를 들어, 지금 읽고 있는 웹 페이지를 로드하기 위해 32개의 호스트 이름(이 글을 쓰는 시점 기준)이 있다는 점을 상기해 보시기 바랍니다. 32개의 호스트 이름 중에는 16개의 고유 도메인("유효 [TLD+1](https://www.cloudflare.com/learning/dns/top-level-domain/)"로 정의됨 )이 있습니다. 각 고유 도메인에 대해 더 적은 수의 연결을 만들거나 기존 연결을 "통합"할 수 있을까요? 대답은 '_예, 하지만 상황에 따라 다릅니다_ '입니다.

블로그 페이지를 로드하는 데 필요한 정확한 연결 수는 전혀 명확하지 않으며 알기도 어렵습니다. 16개의 도메인에 32개의 호스트 이름이 연결되어 있을 수 있지만, "고유 연결 수는 몇 개입니까?"라는 질문에 대한 답이 16개라는 뜻은 아닙니다. 모든 호스트 이름이 단일 서버에서 연결 가능한 경우 정답은 _하나_의 연결일 수도 있고, 각 개별 호스트 이름에 액세스하기 위해 서로 다른 별개의 서버가 필요한 경우 최대 32개의 독립적인 연결일 수도 있습니다.

연결 재사용은 다양한 형태로 제공되므로 HTTP 공간에서 "연결 병합"을 정의하는 것이 중요합니다. 예를 들어, 호스트 이름에 대한 기존의 [TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) 또는 TLS 연결을 재사용하여 **_동일한_** 호스트 이름에서 하위 리소스에 대한 여러 요청을 하는 것은 연결 재사용에 해당되지만, 병합에는 해당되지 않습니다.

병합은 일부 호스트 이름에 대한 기존 TLS 채널의 용도를 변경하거나 **_다른_** 호스트 이름에 연결하는 데 사용할 수 있을 때 발생합니다. 예를 들어, blog.cloudflare.com을 방문하면 HTML은 하위 리소스 cdnjs.cloudflare.com을 가리킵니다. 하위 리소스에 대해 동일한 TLS 연결을 재사용하려면 TLS 인증서의 ["서버 대체 이름(SAN)](https://en.wikipedia.org/wiki/Subject_Alternative_Name)" 목록에 두 호스트 이름이 함께 표시되어야 합니다. 하지만 이 단계만으로는 브라우저들이 통합되도록 설득하기에 충분하지 않습니다.결국, 같은 인증서를 사용하더라도 cdnjs.Cloudflare.com 서비스는 blog.cloudflare.com과 같은 서버에서 연결될 수도 있고 연결되지 않을 수도 있습니다. 그렇다면 브라우저에서는 어떻게 알 수 있을까요? 병합은 서버에서 올바른 조건이 설정된 경우에만 작동하지만, 클라이언트에서 병합 여부를 결정해야 하므로 브라우저에서는 인증서 목록의 SAN을 넘어 병합을 위한 신호를 필요로 합니다. 다시 비유로 돌아가 본다면, 조립 공장에서는 공급업체에서 이미 창고에 동일한 부품을 가지고 있다는 것을 모르고 제조업체에 직접 부품을 주문할 수 있습니다.

브라우저가 연결 병합 여부를 결정하는 데 사용할 수 있는 두 가지 명시적 신호가 있습니다. 하나는 IP 기반이고 다른 하나는 ORIGIN Frame 기반입니다. 전자는 서버 운영자가 DNS 레코드를 서버에서 사용 가능한 HTTP 리소스에 엄격하게 바인딩해야 합니다. 이는 관리 및 배포가 어렵고 실제로 모든 리소스를 특정 집합 또는 단일 IP 주소 뒤에 배치해야 하므로 위험한 종속성이 초래됩니다. IP 주소가 병합 결정에 영향을 미치는 방식은 [브라우저마다 다르며](https://daniel.haxx.se/blog/2016/08/18/http2-connection-coalescing/), 일부 브라우저는 더 보수적인 방식을, 다른 브라우저는 더 허용하는 방식을 선택합니다. 그 대신에, HTTP ORIGIN Frame은 서버가 오케스트레이션하기 쉬운 신호이며, 유연하고 서비스 중단 없이 정상적으로 실패할 수 있습니다(사양을 준수하는 구현의 경우).

이 두 가지 병합 신호의 근본적인 차이점은 다음과 같습니다. IP 기반 합산 신호는 암시적이며, 심지어 우발적으로 발생하므로 존재할 수도 있고 존재하지 않을 수도 있는 병합 가능성을 클라이언트가 추론해야 한다는 것입니다. IP 주소는 [이름과 실제 관계가 없도록](https://blog.cloudflare.com/ko-kr/addressing-agility-ko-kr/) 설계되었기 때문에 이 모든 것이 놀라운 일이 아닙니다! 이와는 대조적으로 ORIGIN Frame은 특정 호스트 이름에 대해 DNS가 무엇을 말하든 병합이 가능하다는 것을 서버에서 클라이언트로 보내는 명시적인 신호입니다.

[이전에도 IP 기반 병합](https://blog.cloudflare.com/connection-coalescing-experiments/)을 실험한 적이 있지만, 이번 블로그에서는 ORIGIN Frame 기반 병합에 대해 자세히 살펴보겠습니다.

### ORIGIN Frame 표준이란?

ORIGIN Frame은 각각 스트림 0 또는 연결의 제어 스트림에서 전송되는 특수 Frame으로, [HTTP/2](https://www.rfc-editor.org/rfc/rfc8336) 및 [HTTP/3](https://www.rfc-editor.org/rfc/rfc9412) 사양의 확장입니다. 이 Frame을 사용하면 서버는 _기존_에 설정된 TLS 연결에서 클라이언트에 '오리진 세트'를 보낼 수 있으며, 여기에는 권한이 부여된 호스트 이름이 포함되어 있고 [HTTP 421 오류](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421)가 발생하지 않습니다. 오리진 세트의 호스트 이름은 DNS를 통해 다른 IP 주소에서 호스트 이름을 알린 경우에도 서버의 인증서 SAN 목록에 나타나야 합니다.

구체적으로, 두 가지 단계가 필요합니다.

  1. 웹 서버는 오리진 세트(지정된 연결에 사용될 수 있는 호스트 이름)를 열거하는 목록을 ORIGIN Frame 확장으로 전송해야 합니다.
  2. 웹 서버에서 반환하는 TLS 인증서는 DNS 이름 SAN 항목의 ORIGIN Frame에서 반환되는 추가 호스트 이름을 포함해야 합니다.



높은 수준에서 ORIGIN Frame은 운영자가 첨부할 수 있는 TLS 인증서를 보완하는 것으로, "이것 봐! 헤이, 클라이언트, 여기 이 연결에서 사용할 수 있는 SAN의 이름이 있어. 병합할 수 있어!"라고 이야기할 수 있습니다. ORIGIN Frame은 인증서 자체의 일부가 아니므로 그 내용을 독립적으로 변경할 수 있습니다. 새 인증서가 필요하지 않습니다. 또한 IP 주소에 대한 종속성도 없습니다. 병합 가능한 호스트 이름의 경우, 새로운 연결이나 DNS 쿼리 없이 기존 TCP/QUIC+TLS 연결을 재사용할 수 있습니다.

[오늘날 많은 웹 사이트에서는](https://w3techs.com/technologies/overview/proxy) Cloudflare CDN 서비스와 같은 CDN에서 제공하는 콘텐츠에 의존하고 있습니다. 외부 CDN 서비스를 사용하면 웹 사이트에 속도와 안정성이라는 이점이 제공되고 [원본 서버](https://www.cloudflare.com/learning/cdn/glossary/origin-server/)에서 제공하는 콘텐츠의 부하가 줄어들 수 있습니다. 웹 사이트와 리소스가 서로 다른 호스트 이름과 다른 주체가 소유하고 있음에도 불구하고 동일한 CDN에서 서비스되는 경우, CDN 사업자는 실제 원본 서버를 대신하여 ORIGIN 프레임을 전송하기 위한 인증서 관리 및 연결 요청을 모두 제어할 수 있으므로 연결을 재사용하고 통합할 수 있는 매우 흥미로운 기회가 생깁니다.

안타깝게도 지금까지는 ORIGIN Frame이 제공하는 가능성을 실제로 구현할 방법이 없었습니다. 저희가 아는 한, 현재까지 ORIGIN Frame을 지원하는 서버는 구현된 적이 없습니다. 브라우저 중에서는 Firefox만 ORIGIN Frame을 지원합니다. IP 병합이 어렵고 ORIGIN Frame은 배포된 지원이 없는데, 병합을 더 잘 지원하기 위해 엔지니어링 시간과 에너지를 투자할 가치가 있을까요? 저희는 인터넷 전반에 걸친 대규모 측정을 통해 기회를 파악하고 가능성을 예측하기로 결정한 후 ORIGIN Frame을 구현하여 프로덕션 트래픽에 대한 실험을 진행했습니다.

### 실험 #1: 필요한 변경의 규모는 어느 정도일까요?

2021년 2월, 저희는 100대의 가상 머신에서 수정된 [웹 페이지 테스트](https://blog.cloudflare.com/connection-coalescing-experiments/)를 사용하여 인터넷에서 [가장 인기 있는 웹 사이트](https://radar.cloudflare.com/domains) 50만 개에 대한 [데이터를 수집](https://github.com/WPO-Foundation/webpagetest)했습니다. 캐싱 효과를 제거하기 위해 웹 페이지를 방문할 때마다 자동화된 Chrome(v88) 브라우저 인스턴스가 실행되었습니다(캐싱이 아닌 병합을 이해하고자 했기 때문입니다). 각 세션이 성공적으로 완료되면 Chrome 개발자 도구를 사용하여 페이지 로드 데이터를 검색하고 전체 이벤트 타임 라인과 인증서 및 유효성 검사에 대한 추가 정보가 포함된 HTTP 아카이브 형식(HAR) 파일로 작성했습니다. 또한 루트 웹 페이지의 인증서 체인과 하위 리소스 요청에 의해 트리거된 새로운 TLS 연결을 구문 분석하여 (i) 호스트 이름에 대한 인증서 발급자를 식별하고 (ii) 주체 대체 이름(SAN) 확장자의 존재 여부를 검사하며 (iii) DNS 이름이 사용된 IP 주소로 확인되는지 검증했습니다. 방법론 및 결과에 대한 자세한 내용은 기술 [문서](https://research.cloudflare.com/publications/Singanamalla2022/)에서 확인할 수 있습니다.

첫 번째 단계는 웹 페이지에서 페이지 콘텐츠를 성공적으로 렌더링하기 위해 요청하는 리소스와 이러한 리소스가 인터넷에서 어디에 존재하는지 파악하는 것이었습니다. 연결 통합은 하위 리소스 도메인이 이상적으로 함께 위치할 때 가능해집니다. 저희는 해당 자율 시스템(AS)을 찾아 도메인의 위치를 어림잡았습니다. 예를 들어, [cdnjs](https://cdnjs.cloudflare.com/https://cdnjs.cloudflare.com/)에 연결된 도메인은 BGP 라우팅 테이블에서 AS 13335를 통해 연결할 수 있으며, 이 AS 번호는 Cloudflare에 속합니다. 아래 그림에는 웹 페이지의 비율과 웹 페이지를 완전히 로드하는 데 필요한 고유 AS의 수가 설명되어 있습니다.

웹 페이지의 약 14%는 완전히 로드하려면 2개의 AS가 필요합니다. 즉, 하위 리소스에 대해 하나의 추가 AS에 종속되어 있는 페이지입니다. 웹 페이지의 50% 이상은 필요한 모든 하위 리소스를 얻으려면 6개 이하의 AS에 연결해야 합니다. 위의 도표에서 볼 수 있는 이 결과는 상대적으로 적은 수의 운영자가 웹 사이트의 대부분(~50%)에 필요한 하위 리소스 콘텐츠를 제공하며, ORIGIN Frame의 사용은 의도한 영향을 미치기 위해 몇 가지 변경만 하면 된다는 것을 의미합니다. 따라서 연결 병합의 가능성은 웹 페이지의 모든 하위 리소스를 검색하는 데 필요한 고유 AS의 수로 낙관적으로 어림잡을 수 있습니다. 그러나 실제로는 SLA와 같은 운영 요인에 의해 대체되거나 [이전에 Cloudflare에서](https://research.cloudflare.com/publications/Fayed2021/) 작업한 소켓, 이름, IP 주소 간의 유연한 매핑의 도움을 받을 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Dlhpw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45X8GDMJVMT39D8F70E2T1.png&w=715&h=349&f=webp&fit=cover&position=center)

저희는 그런 다음 병합이 연결 메트릭에 미치는 영향을 이해하려고 했습니다. 웹 페이지를 로드하는 데 필요한, 측정되고 이상적인 DNS 쿼리 및 TLS 연결 수는 아래 그림에 해당 CDF별로 요약되어 있습니다.

모델링과 광범위한 분석을 통해 ORIGIN Frame을 통한 연결 통합이 브라우저의 DNS 및 TLS 연결 수를 중앙값에서 60% 이상 줄일 수 있음을 확인했습니다. 이 모델링은 클라이언트가 DNS 레코드를 요청한 횟수를 파악하여 수행했고, 이를 서비스할 이상적인 ORIGIN Frame과 결합했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - DZcmqU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48T1Y598J42C2CVMPC1M33.png&w=715&h=394&f=webp&fit=cover&position=center)

[CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)에서 운영하는 서버와 같은 많은 멀티 원본 서버는 인증서를 재사용하고 여러 DNS SAN 항목에 동일한 인증서를 제공하는 경향이 있습니다. 이를 통해 운영자는 생성 및 갱신 주기를 통해 더 적은 수의 인증서를 관리할 수 있습니다. 이론적으로는 인증서에 수백만 개의 이름을 넣을 수 있지만, 이러한 인증서를 만드는 것은 비합리적이며 효과적으로 관리하기 어렵습니다. 저희 모델링 측정은 아래 그림에서 강조된 것처럼 기존 인증서를 계속 사용함으로써 완벽한 통합을 가능하게 하는 데 필요한 변경의 규모에 대한 정보를 제시합니다.

웹 사이트에서 제공하는 인증서의 60% 이상은 수정할 필요가 없으며 ORIGIN Frame의 이점을 누릴 수 있으며, 인증서의 DNS SAN 이름을 10개 이하로 추가하면 측정 대상 웹 사이트의 92% 이상에 성공적으로 연결을 통합할 수 있는 것으로 확인했습니다. CDN 공급자는 가장 많이 요청되는 호스트 이름 중 서너 개를 각 인증서에 추가하여 가장 효과적으로 변경할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - 3Eev4N](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47R6AZHNG2GYF9CH2S97M9.png&w=715&h=398&f=webp&fit=cover&position=center)

### 실험 #2: ORIGIN Frame의 실제 작동

모델링의 기대치를 검증하기 위해 2022년 초에 보다 적극적인 접근 방식을 취했습니다. 다음 실험에서는 하위 리소스로 _cdnjs.cloudflare.com_을 광범위하게 사용하는 5,000개의 웹 사이트를 대상으로 했습니다. 실험적인 TLS 종료 엔드포인트를 수정하여 [RFC 표준](https://datatracker.ietf.org/doc/rfc8336/)에 정의된 대로 HTTP/2 ORIGIN Frame 지원을 배포했습니다. 여기에는 우리가 오픈 소스로 제공한 Golang의 _net_ 및 _http_ 종속 모듈의 내부 포크를 변경하는 작업이 포함되었습니다("[여기](https://github.com/cloudflare/go-originframe) 및 [여기](https://github.com/cloudflare/net-originframe) 참조).

실험 중에 실험 세트의 웹 사이트에 연결하면 ORIGIN frame에 _cdnjs.cloudflare.com_이 반환되는 반면, 대조 세트는 임의의(사용되지 않은) 호스트 이름을 반환했습니다. 5,000개의 웹 사이트에 대한 모든 기존 에지 인증서도 수정되었습니다. 실험 그룹의 경우, 해당 인증서를 _cdnjs.Cloudflare.com_으로 갱신하여 SAN에 추가했습니다. 대조 그룹과 실험 그룹 간의 무결성을 보장하기 위해 대조 그룹 도메인 인증서도 대조 도메인에서 사용하지 않는 유효하고 동일한 크기의 타사 도메인으로 갱신했습니다. 이는 인증서의 상대적인 크기 변경이 일정하게 유지되어 인증서 크기에 따른 잠재적인 편향이 발생하지 않도록 하기 위한 것입니다. 결과는 놀라웠습니다!

실험에서 Firefox에서 웹 사이트로 전송된 요청 중 1%를 샘플링한 결과, **초당 새로운 TLS 연결이 50%** 이상 감소하여 클라이언트가 수행하는 암호화 확인 작업의 수가 줄어들고 서버 컴퓨팅 오버헤드가 감소한 것으로 나타났습니다. 예상대로 CDN 또는 서버 운영자가 볼 때 연결 재사용의 효과를 나타내는 대조 세트에는 차이가 없었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1422 Embedded Image - q0fWGU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45GKTR9B46ZHYNCDK42GGC.png&w=715&h=399&f=webp&fit=cover&position=center)

### 논의 및 인사이트

모델링 측정 결과 약간의 성능 향상을 기대할 수 있었지만, 실제로는 크게 개선되지는 않았으며, '더 나빠지지 않는 것'이 성능에 대한 적절한 멘탈 모델임을 시사했습니다. 리소스 개체 크기, 경쟁적인 연결, 혼잡 제어 간의 미묘한 상호 작용은 네트워크 조건에 따라 달라집니다. 예를 들어, 네트워크 링크의 병목 리소스를 놓고 경쟁하는 연결 수가 줄어들면 병목을 공유하는 용량이 감소합니다. 더 많은 운영자가 서버에 ORIGIN Frame에 대한 지원을 배포함에 따라 이러한 측정치를 다시 살펴보면 흥미로울 것 같습니다.

성능 외에도 ORIGIN Frame의 주요 이점 중 하나는 개인정보 보호 측면입니다. 어떻게 이점이 되느냐고요? 병합된 각 연결은 병합되지 않은 연결에서 유출되는 클라이언트 메타데이터를 숨깁니다. 웹 페이지의 특정 리소스는 웹 사이트와 상호 작용하는 방식에 따라 로드됩니다. 이는 서버에서 일부 리소스를 검색하기 위한 모든 새 연결에 대해 [SNI](https://www.cloudflare.com/learning/ssl/what-is-sni/)([암호화된 Client Hello](https://blog.cloudflare.com/encrypted-client-hello/)가 없는 경우)와 같은 TLS 일반 텍스트 메타데이터와 포트 53에서 UDP 또는 TCP를 통해 전송되는 경우 하나 이상의 일반 텍스트 DNS 쿼리가 네트워크에 노출됨을 의미합니다. 연결을 통합하면 브라우저에서 새 TLS 연결을 열 필요가 없으며 추가 DNS 쿼리를 수행할 필요도 없습니다. 이렇게 하면 네트워크에서 수신 중인 모든 사용자로부터 메타데이터가 유출되는 것을 방지할 수 있습니다. ORIGIN Frame은 네트워크 경로에서 이러한 신호를 최소화하여 네트워크 도청자에게 유출되는 일반 텍스트 정보의 양을 줄임으로써 개인정보 보호를 개선합니다.

브라우저는 여러 인증서를 확인하는 데 필요한 암호화 계산이 줄어든다는 이점이 있습니다. 하지만 [우선순위 지정](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/)과 같은 엔드포인트(브라우저 및 원본 서버)에서의 리소스 스케줄링 또는 [HTTP 조기 힌트](https://blog.cloudflare.com/early-hints/)와 같은 최근 제안으로 연결에 과부하가 걸리지 않거나 해당 리소스를 두고 경쟁하지 않는 클라이언트 경험을 제공하는 매우 흥미로운 미래의 기회가 생긴다는 점에서 큰 이점을 얻을 수 있습니다. [CERTIFICATE Frame](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-http2-secondary-certs-06#section-3.4) IETF 초안과 함께 사용하면, 서버가 연결 설정 후 웹 사이트의 TLS 인증서에 추가 SAN 항목 없이 호스트 이름의 권한을 증명할 수 있으므로 수동 인증서 수정의 필요성을 더욱 없앨 수 있습니다.

### 결론 및 행동 개시 요구

요약하자면, 현재 인터넷 생태계에는 인증서와 서버 인프라를 몇 가지 변경하는 것만으로 연결을 병합할 많은 기회가 있습니다. 서버는 TLS 핸드셰이크 횟수를 약 50%까지 크게 줄이는 동시에 렌더링 차단 DNS 쿼리 횟수를 60% 이상 줄일 수 있습니다. 클라이언트는 네트워크 방관자에 대한 일반 텍스트 DNS 노출을 줄임으로써 프라이버시 측면에서 이러한 이점을 추가로 누릴 수 있습니다.

이를 실현하기 위해 저희는 현재 고객을 위해 HTTP/2 및 HTTP/3 ORIGIN Frame 모두에 대한 지원을 추가할 계획입니다. 또한 타사 리소스를 관리하는 다른 사업자들도 인터넷 생태계를 개선하기 위해 ORIGIN Frame 지원을 도입할 것을 권장합니다.저희가 제출한 논문이 ACM 인터넷 측정 컨퍼런스 2022에서 승인되었으며 [다운로드할 수 있습니다](https://research.cloudflare.com/publications/Singanamalla2022/). 새로운 표준이 실제로 적용되는 것을 볼 수 있는 이와 같은 프로젝트에 참여하고 싶다면 [채용 정보 페이지](https://www.cloudflare.com/careers/)를 방문하세요!

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F&t=ORIGIN%20Frames%EC%99%80%EC%9D%98%20%EC%97%B0%EA%B2%B0%20%ED%86%B5%ED%95%A9%3A%20DNS%20%EC%BF%BC%EB%A6%AC%20%EA%B0%90%EC%86%8C%2C%20%EC%97%B0%EA%B2%B0%20%EC%88%98%20%EA%B0%90%EC%86%8C)[](https://x.com/intent/post?text=ORIGIN+Frames%EC%99%80%EC%9D%98+%EC%97%B0%EA%B2%B0+%ED%86%B5%ED%95%A9%3A+DNS+%EC%BF%BC%EB%A6%AC+%EA%B0%90%EC%86%8C%2C+%EC%97%B0%EA%B2%B0+%EC%88%98+%EA%B0%90%EC%86%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://bsky.app/intent/compose?text=ORIGIN+Frames%EC%99%80%EC%9D%98+%EC%97%B0%EA%B2%B0+%ED%86%B5%ED%95%A9%3A+DNS+%EC%BF%BC%EB%A6%AC+%EA%B0%90%EC%86%8C%2C+%EC%97%B0%EA%B2%B0+%EC%88%98+%EA%B0%90%EC%86%8C+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://mastodonshare.com/?text=ORIGIN+Frames%EC%99%80%EC%9D%98+%EC%97%B0%EA%B2%B0+%ED%86%B5%ED%95%A9%3A+DNS+%EC%BF%BC%EB%A6%AC+%EA%B0%90%EC%86%8C%2C+%EC%97%B0%EA%B2%B0+%EC%88%98+%EA%B0%90%EC%86%8C&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)[](https://www.threads.net/intent/post?text=ORIGIN+Frames%EC%99%80%EC%9D%98+%EC%97%B0%EA%B2%B0+%ED%86%B5%ED%95%A9%3A+DNS+%EC%BF%BC%EB%A6%AC+%EA%B0%90%EC%86%8C%2C+%EC%97%B0%EA%B2%B0+%EC%88%98+%EA%B0%90%EC%86%8C+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fconnection-coalescing-with-origin-frames-fewer-dns-queries-fewer-connections%2F)

## 관련 태그

[DNS](https://blog.cloudflare.com/ko-kr/tag/dns/)[HTTP2 (KO)](https://blog.cloudflare.com/ko-kr/tag/http2/)[TLS](https://blog.cloudflare.com/ko-kr/tag/tls/)[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인턴십 경험](https://blog.cloudflare.com/ko-kr/tag/internship-experience/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Sudheesh Singanamalla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44QXR5DHNZQWQ7DTBSWGM7.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Sudheesh Singanamalla](https://blog.cloudflare.com/ko-kr/author/sudheesh/)

[](https://sudheesh.info/)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
