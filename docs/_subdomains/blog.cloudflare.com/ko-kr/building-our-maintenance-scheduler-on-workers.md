---
url: https://blog.cloudflare.com/ko-kr/building-our-maintenance-scheduler-on-workers/
title: Workers\uac00 \ub0b4\ubd80 \uc720\uc9c0 \uad00\ub9ac \uc77c\uc815 \ud30c\uc774\ud504\ub77c\uc778\uc744 \uac15\ud654\ud558\ub294 \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:45:14.603594+00:00
---

# Workers가 내부 유지 관리 일정 파이프라인을 강화하는 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/building-our-maintenance-scheduler-on-workers/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Prometheus](https://blog.cloudflare.com/ko-kr/tag/prometheus/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)+11개의 태그 더 보기

4개 태그4개 태그 보기

  * 게시물 태그
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Prometheus](https://blog.cloudflare.com/ko-kr/tag/prometheus/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)
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



[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Prometheus](https://blog.cloudflare.com/ko-kr/tag/prometheus/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)

2025년 12월 22일

# Workers가 내부 유지 관리 일정 파이프라인을 강화하는 방법

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/ko-kr/author/kevin-deems/) 및 [Michael Hoffmann](https://blog.cloudflare.com/ko-kr/author/michael-hoffmann/)

12분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/building-our-maintenance-scheduler-on-workers/), [日本語](https://blog.cloudflare.com/ja-jp/building-our-maintenance-scheduler-on-workers/), [繁體中文](https://blog.cloudflare.com/zh-tw/building-our-maintenance-scheduler-on-workers/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/building-our-maintenance-scheduler-on-workers/).

![BLOG-3017 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MH5G11Z4TPXRMZT8FJXD.png&w=1016&h=635&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAO1yFQGCLTWmWWXWgX36jXH2gT3OaPWWUQ2mQU3OWbIakeZSydpe5aJC3WIOrT3eeS3acYoSjhJ6zk67Ei63OdKHLYZK8XoepT3+nao+tkKq9oLvOl7nYfqvVaZrGZpCxUIOuapGzj6rAobnNmrjVhKrTbpvFZZG0TYKyY4y1hKC9l63Flq3JhqPGcJW9XYy0Sn+zWYa1dZO5ip27kJ+6hpm3cI60U4SySH6zVYO1boy3g5W2jJmzhpWwcIuvT4Cx)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

Cloudflare는 전 세계 [_330여 개 도시에 데이터 센터를 보유하고 있으므로_](https://www.cloudflare.com/network/), 데이터 센터 운영을 계획할 때 사용자들이 알지 못하는 사이에 데이터 센터가 쉽게 중단될 수 있다고 생각할 수도 있습니다. 하지만 서비스 [_중단을 지원하려면 신중한 계획이 필요한 것이 현실이 되었고_](https://developers.cloudflare.com/support/disruptive-maintenance/), Cloudflare가 성장하면서 인프라와 네트워크 운영 전문가 간의 수동 조정으로 이러한 복잡성을 관리하는 것이 거의 불가능해졌습니다.

사람이 중복되는 모든 유지보수 요청을 추적하거나 모든 고객별 라우팅 규칙을 실시간으로 고려하는 것은 이제 불가능합니다. 우리는 수동 감독만으로는 어느 지역에서 일상적인 하드웨어 업데이트가 다른 지역의 중요 경로와 의도치 않게 충돌하지 않는다는 것을 보장할 수 없는 지경에 이르렀습니다.

저희는 보호 장치 역할을 할 중앙 집중식 자동화된 '두 뇌', 즉 전체 네트워크 상태를 한 번에 볼 수 있는 시스템이 필요하다는 것을 깨달았습니다. [_Cloudflare Workers_](https://workers.cloudflare.com/)에서 이 스케줄러를 구축함으로써 저희는 안전 제약 조건을 프로그래밍 방식으로 적용할 수 있는 방법을 마련했으며, 이를 통해 고객이 의존하는 서비스의 안정성을 결코 희생시키지 않는다는 것을 보장했습니다.

이 블로그 게시물에서는 Cloudflare에서 이를 어떻게 구축했는지 설명하고 현재 확인 중인 결과를 공유해 보겠습니다.

## 중요한 유지 관리 작업의 위험을 줄이기 위한 시스템 구축

대도시 지역에서 운영되는 많은 Cloudflare 데이터 센터에 공용 인터넷을 공동으로 연결하는 소규모의 이중화 게이트웨이 그룹 중 하나의 역할을 하는 에지 라우터를 상상해 보세요. 인구가 많은 도시에서는 라우터가 모두 동시에 오프라인 상태가 되어 이 작은 라우터 클러스터 뒤에 있는 여러 데이터 센터가 중단되지 않도록 해야 합니다. 

유지보수 문제는 Cloudflare의 Zero Trust 제품인 전용 CDN 송신 IP에서 비롯됩니다. 이를 이용하는 고객은 짧은 대기 시간을 위해 사용자 트래픽을 Cloudflare에서 나가서 지리적으로 가까운 원본 서버로 전송할 특정 데이터 센터를 선택할 수 있습니다. (이 게시물은 간략함을 위해 Dedicated CDN 송신 IP 제품을 이전 이름에서였던 "Aegis"라고 부르겠습니다.) 고객이 선택한 모든 데이터 센터가 한 번에 오프라인 상태인 경우 대기 시간이 더 길어지고 5XX 오류가 발생할 수 있으며, Cloudflare는 이를 피해야 합니다. 

Cloudflare 유지 관리 스케줄러는 이와 같은 문제를 해결합니다. 특정 영역에서 항상 하나 이상의 에지 라우터를 활성화할 수 있도록 할 수 있습니다. 또한 유지 관리를 예약할 때, 여러 예약된 이벤트가 결합되어 고객의 Aegis 풀의 모든 데이터 센터가 동시에 오프라인 상태가 되는지 확인할 수 있습니다.

스케줄러를 만들기 전에는 이러한 파괴적인 이벤트가 동시에 발생하면 고객에게 가동 중지 시간이 발생할 수 있습니다. 이제 스케줄러를 통해 내부 운영자에게 잠재적인 충돌 가능성을 알려 다른 관련 데이터 센터 유지 관리 이벤트와 겹치지 않도록 새로운 시간을 제안할 수 있습니다.

저희는 에지 라우터 가용성 및 고객 규칙과 같은 이러한 운영 시나리오를 더 예측 가능하고 안전한 유지 관리 계획을 수립할 수 있는 유지 관리 제약 조건으로 정의합니다.

## 유지 관리 제약

모든 제약 조건은 네트워크 라우터 또는 서버 목록과 같은 일련의 제안된 유지 관리 항목에서 시작됩니다. 그런 다음 캘린더에서 제안된 유지 관리 기간과 겹치는 모든 유지 관리 이벤트를 찾습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N24BK9S5N2GJ6VGMRCGQ.png&w=715&h=385&f=webp&fit=cover&position=center)

다음으로, Aegis 고객 IP 풀 목록과 같은 제품 APIs를 집계합니다. Aegis는 아래와 같이 고객이 특정 데이터 센터 ID에서 송신을 요청한 IP 범위 세트를 반환합니다.
    
    
    [
        {
          "cidr": "104.28.0.32/32",
          "pool_name": "customer-9876",
          "port_slots": [
            {
              "dc_id": 21,
              "other_colos_enabled": true,
            },
            {
              "dc_id": 45,
              "other_colos_enabled": true,
            }
          ],
          "modified_at": "2023-10-22T13:32:47.213767Z"
        },
    ]

이 시나리오에서는 Aegis 고객 9876이 Cloudflare의 송신 트래픽을 수신하기 위한 데이터 센터가 하나 이상 필요하므로 데이터 센터 21과 데이터 센터 45가 서로 연관되어 있습니다. 21번 데이터 센터와 45번 데이터 센터를 동시에 가동 중지시키려고 하면, 코디네이터가 해당 고객의 워크로드에 의도하지 않은 결과가 발생할 수 있다고 경고합니다.

처음에는 모든 데이터를 단일 Worker에 로드하는 순진한 솔루션을 가지고 있었습니다. 여기에는 모든 서버 관계, 제품 구성, 제품 및 인프라 상태에서 제약 조건을 계산하는 메트릭이 포함되었습니다. 개념 증명 단계에서도 '메모리 부족' 오류 문제가 발생했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44X5J4KQRSH4Q5YRX5JNQC.png&w=715&h=226&f=webp&fit=cover&position=center)

Workers의 [_플랫폼 제한_](https://developers.cloudflare.com/workers/platform/limits/)을 더 잘 인식할 필요가 있었습니다. 이를 위해서는 제약 조건의 비즈니스 로직을 처리하는 데 절대적으로 필요한 만큼의 데이터만 로드하면 되었습니다. 독일 프랑크푸르트에 있는 라우터 유지보수 요청이 들어올 경우, 이 요청은 지역 간에 중복되는 일이 없기 때문에 호주에서 무슨 일이 일어나든 전혀 신경 쓰지 않습니다. 따라서 독일의 인접한 데이터 센터에 대한 데이터만 로드해야 합니다. 데이터세트의 관계를 처리할 수 있는 보다 효율적인 방법이 필요했습니다.

## Workers에서의 그래프 처리

제약 조건을 살펴보면 각 제약 조건이 개체 및 연결이라는 두 가지 개념으로 귀결되는 패턴이 나타났습니다. 그래프 이론에서는 이러한 구성 요소를 각각 꼭짓점과 간선이라고 합니다. 개체는 네트워크 라우터가 될 수 있고, 연결은 라우터를 온라인 상태로 만들기 위해 필요한 데이터 센터의 Aegis 풀 목록이 될 수 있습니다. Cloudflare는 Facebook의 [_TAO_](https://research.facebook.com/publications/tao-facebooks-distributed-data-store-for-the-social-graph/) 연구 논문에서 영감을 받아 제품 및 인프라 데이터 위에 그래프 인터페이스를 구축했습니다. API는 다음과 같은 모습입니다.
    
    
    type ObjectID = string
    
    interface MainTAOInterface<TObject, TAssoc, TAssocType> {
      object_get(id: ObjectID): Promise<TObject | undefined>
    
      assoc_get(id1: ObjectID, atype: TAssocType): AsyncIterable<TAssoc>
    }

핵심 인사이트는 연결이 입력된다는 것입니다. 예를 들어, 제약 조건은 Aegis 제품 데이터를 검색하기 위해 그래프 인터페이스를 호출합니다.
    
    
    async function constraint(c: AppContext, aegis: TAOAegisClient, datacenters: string[]): Promise<Record<string, PoolAnalysis>> {
      const datacenterEntries = await Promise.all(
        datacenters.map(async (dcID) => {
          const iter = aegis.assoc_get(c, dcID, AegisAssocType.DATACENTER_INSIDE_AEGIS_POOL)
          const pools: string[] = []
          for await (const assoc of iter) {
            pools.push(assoc.id2)
          }
          return [dcID, pools] as const
        }),
      )
    
      const datacenterToPools = new Map<string, string[]>(datacenterEntries)
      const uniquePools = new Set<string>()
      for (const pools of datacenterToPools.values()) {
        for (const pool of pools) uniquePools.add(pool)
      }
    
      const poolTotalsEntries = await Promise.all(
        [...uniquePools].map(async (pool) => {
          const total = aegis.assoc_count(c, pool, AegisAssocType.AEGIS_POOL_CONTAINS_DATACENTER)
          return [pool, total] as const
        }),
      )
    
      const poolTotals = new Map<string, number>(poolTotalsEntries)
      const poolAnalysis: Record<string, PoolAnalysis> = {}
      for (const [dcID, pools] of datacenterToPools.entries()) {
        for (const pool of pools) {
          poolAnalysis[pool] = {
            affectedDatacenters: new Set([dcID]),
            totalDatacenters: poolTotals.get(pool),
          }
        }
      }
    
      return poolAnalysis
    }

위의 코드에서는 두 가지 연결 유형을 사용합니다.

  1. DATACENTER_INSIDE_AEGIS_POL - 데이터 센터가 있는 Aegis 고객 풀을 검색합니다.
  2. AEGIS_POL_CONTAINS_DATACENTER는 Aegis 풀이 트래픽을 처리하는 데 필요한 데이터 센터를 검색합니다.



이러한 연관성은 서로 역전된 지표입니다. 액세스 패턴은 이전과 완전히 동일하지만, 이제 그래프 구현에서 쿼리하는 데이터의 양을 훨씬 더 잘 제어할 수 있습니다. 이전에는 모든 Aegis 풀을 메모리에 로드하고 비즈니스 로직을 필터링해야 했습니다. 이제 애플리케이션에 중요한 데이터만 직접 가져올 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46V747SXCQBJ3NZGGBWH72.png&w=715&h=313&f=webp&fit=cover&position=center)

이 인터페이스는 그래프 구현이 비즈니스 로직을 복잡하게 만들지 않고도 백그라운드에서 성능을 개선할 수 있기 때문에 강력합니다. 따라서 Workers의 확장성과 Cloudflare CDN을 사용하여 내부 시스템에서 데이터를 매우 빠르게 가져올 수 있습니다.

## 가져오기 파이프라인

저희는 새로운 그래프 구현을 사용하도록 전환하여 더 대상이 지정된 API 호출을 보냈습니다. 하룻밤 사이에 응답 크기가 100배까지 감소했고, 로딩이 적은 요청에서 작은 요청 다수로 전환되었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48J28W9JDW5V667ENB9QRH.png&w=715&h=344&f=webp&fit=cover&position=center)

이렇게 하면 메모리에 과도하게 많은 것을 로드하는 문제가 해결되지만, 몇 가지 큰 HTTP 요청 대신 작은 요청을 훨씬 더 많이 수행하기 때문에 하위 요청 문제가 발생합니다. Cloudflare는 하루아침에 하위 요청 제한을 지속해서 위반하기 시작했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3017 image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45SB0HD85RBHA7KBXDD3TD.png&w=715&h=346&f=webp&fit=cover&position=center)

이 문제를 해결하기 위해 Cloudflare에서는 그래프 구현과 `fetch` API 사이에 스마트 미들웨어 계층을 구축했습니다.
    
    
    export const fetchPipeline = new FetchPipeline()
      .use(requestDeduplicator())
      .use(lruCacher({
        maxItems: 100,
      }))
      .use(cdnCacher())
      .use(backoffRetryer({
        retries: 3,
        baseMs: 100,
        jitter: true,
      }))
      .handler(terminalFetch);

바둑에 익숙하신 분이라면 [_singleflight_](https://pkg.go.dev/golang.org/x/sync/singleflight) 패키지를 본 적이 있을 것입니다. 저희는 이 아이디어에서 영감을 얻었고 가져오기 파이프라인의 첫 번째 미들웨어 구성 요소가 전송 중인 HTTP 요청의 중복을 제거하여 동일한 Worker에서 중복 요청을 생성하는 대신 데이터에 대해 모두 동일한 프라미스를 기다립니다. 다음으로, 경량 LRU(최소 최근 사용) 캐시를 사용하여 이전에 이미 본 요청을 내부적으로 캐시합니다.

이 두 가지를 모두 완료하면 Cloudflare의 `caches.default.match` 함수를 사용하여 Worker가 실행 중인 지역에서 모든 GET 요청을 캐시합니다. 성능 특성이 서로 다른 데이터 소스가 여러 개 있으므로 Time To Live(TTL) 값을 신중하게 선택합니다. 예를 들어, 실시간 데이터는 1분 동안만 캐시됩니다. 비교적 정적인 인프라 데이터는 데이터 유형에 따라 1~24시간 동안 캐시될 수 있었습니다. 전원 관리 데이터는 에지에서 더 오래 캐시할 수 있도록 수동으로 그리고 자주 변경될 수 있습니다.

이러한 계층 외에도 표준 지수 백오프, 재시도, 지터가 있습니다. `이렇게 하면 다운스트림 리소스를` 일시적으로 사용할 수 없게 되는 가져오기 호출을 줄이는 데 도움이 됩니다. 뒤로 물러서면 다음 요청을 성공적으로 가져올 확률이 높아집니다. 반대로, Worker가 백오프 없이 지속해서 요청을 보내는 경우 원본이 5xx 오류를 반환하기 시작할 때 하위 요청 제한을 쉽게 위반하게 됩니다.

이 모든 것을 종합해보면 캐시 적중률은 약 99%에 달합니다. [_캐시_](https://www.cloudflare.com/learning/cdn/what-is-a-cache-hit-ratio/) 적중률은 Cloudflare의 빠른 캐시 메모리에서 처리된 HTTP 요청의 비율('적중')과 Cloudflare의 제어판에서 실행 중인 데이터 소스에 대한 느린 요청('실패')의 비율로, (적중 / (적중 + 누락))으로 계산합니다 . Worker의 캐시에서 데이터를 쿼리하는 것은 다른 지역에 있는 원본 서버에서 데이터를 가져오는 것보다 훨씬 빠르므로 속도가 높으면 HTTP 요청 성능이 개선되고 비용이 절감됩니다. 설정을 조정한 후 인메모리 및 CDN 캐시의 캐시 적중률이 극적으로 증가했습니다. 워크로드의 대부분이 실시간이므로 분당 한 번 이상 새 데이터를 요청해야 하므로 적중률 100%는 불가능합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44RXG38NESXHB4QMTCNP2J.png&w=715&h=691&f=webp&fit=cover&position=center)

가져오기 계층의 개선에 대해서는 이야기했지만, 원본 HTTP 요청의 속도를 개선하는 방법에 대해서는 이야기하지 않았습니다. 유지보수 담당자는 데이터 센터 내 네트워크 성능 저하 및 장비 장애에 실시간으로 대응해야 합니다. Cloudflare는 분산형 [_Prometheus_](https://blog.cloudflare.com/how-cloudflare-runs-prometheus-at-scale/) 쿼리 엔진인 Thanos를 사용하여 에지에서 코디네이터로 고성능 메트릭을 제공합니다.

## 실시간으로 제공하는 타노스

그래프 처리 인터페이스 사용 선택이 실시간 쿼리에 어떤 영향을 미쳤는지 설명하기 위해 예를 들어 보겠습니다. 에지 라우터의 상태를 분석하기 위해 다음 쿼리를 보낼 수 있습니다.
    
    
    sum by (instance) (network_snmp_interface_admin_status{instance=~"edge.*"})

원래 Cloudflare는 각 에지 라우터의 현재 상태 목록을 요청하고 Worker 내부 유지 관리와 관련된 라우터를 수동으로 필터링했습니다. 이는 여러 가지 이유로 최적이 아닙니다. 예를 들어, 타노스는 디코딩과 인코딩에 필요한 멀티 MB 응답을 반환했습니다. 또한 Worker는 특정 유지 관리 요청을 처리하는 동안 대부분의 데이터를 필터링하기 위해 이러한 대규모 HTTP 응답을 캐시하고 디코딩하면 되었습니다. TypeScript는 단일 스레드이고 JSON 데이터 구문 분석은 CPU에 의존하므로 두 개의 큰 HTTP 요청을 전송하면 하나는 차단되어 다른 요청이 구문 분석을 마칠 때까지 기다리게 됩니다.

대신 그래프를 사용하여 `EDGE_ROUTER_NETWORK_CONNECTS_TO_SPINE`으로 표시되는 에지와 스파인 라우터 간의 인터페이스 링크와 같은 표적 관계를 찾기만 하면 됩니다.
    
    
    sum by (lldp_name) (network_snmp_interface_admin_status{instance=~"edge01.fra03", lldp_name=~"spine.*"})

그 결과 여러 MB가 나타나는 대신 평균 1Kb이거나 약 1,000배 더 작습니다. 우리는 대부분의 역직렬화를 타사로 오프로드하므로 Worker 내부에 필요한 CPU 양도 크게 줄어듭니다. 앞서 설명한 것처럼 이는 더 많은 수의 작은 가져오기 요청을 수행해야 하지만, Tanos 앞에 있는 로드 밸런서를 통해 요청을 균등하게 분산하여 이 사용 사례의 처리량을 늘릴 수 있습니다. 

그래프 구현 및 가져오기 파이프라인은 수천 건의 작은 실시간 요청이라는 '끔찍한 무리'를 성공적으로 처리했습니다. 하지만 이력 분석은 I/O와는 다른 문제를 제시합니다. 작고 구체적인 관계를 가져오는 대신 몇 달치의 데이터를 스캔하여 충돌하는 유지 관리 기간을 찾아야 합니다. 과거에는 Thanos가 개체 저장소인 [R2](https://www.cloudflare.com/developer-platform/products/r2/)에 대량의 무작위 읽기를 발행했습니다. 성능을 그대로 유지하면서 이 막대한 대역폭 저하를 해결하기 위해 저희는 올해 내부적으로 Observability 팀에서 개발한 새로운 접근 방식을 채택했습니다.

## 과거 데이터 분석

당사의 솔루션이 정확하고 Cloudflare 네트워크의 성장에 따라 확장될지 여부를 판단하려면 과거 데이터에 의존해야 할 정도로 유지 관리 사용 사례가 많습니다. Cloudflare는 사고를 일으키고 싶지 않으며, 제안된 물리적 유지 보수가 불필요하게 차단되지 않도록 방지하고자 합니다. 이 두 가지 우선순위의 균형을 유지하기 위해, 2개월 전이나 1년 전에 발생한 유지 관리 이벤트에 대한 시계열 데이터를 사용하여 유지 관리 이벤트가 제약 조건 중 하나를 위반하는 빈도를 알 수 있습니다. 에지 라우터 가용성 또는 Aegis입니다. 저희는 올해 초에 타노스를 사용하여 [_자동으로 소프트웨어를 출시하고 에지로 되돌리는 것에_](https://blog.cloudflare.com/safe-change-at-any-scale/) 대해 블로그에 게시한 적이 있습니다.

Tanos는 주로 Prometheus를 사용하지만, Prometheus의 유지가 쿼리에 응답하기에 충분하지 않은 경우 개체 스토리지(이 경우 R2)에서 데이터를 다운로드해야 합니다. Prometheus TSDB 블록은 원래 로컬 SSD용으로 설계되었으며, 개체 스토리지로 이동할 때 병목 현상이 발생하는 무작위 액세스 패턴에 의존합니다. 스케줄러가 충돌하는 제약 조건을 식별하기 위해 몇 달 동안의 유지 관리 데이터를 분석해야 할 때 개체 스토리지에서 무작위 읽기는 막대한 I/O 페널티를 초래합니다. 이 문제를 해결하기 위해 Cloudflare는 이러한 블록을 [_Apache Parquet_](https://parquet.apache.org/) 파일로 변환하는 변환 계층을 구현했습니다. Parquet은 행이 아닌 열별로 데이터를 구성하는 빅데이터 분석에 기본인 열 형식으로, 풍부한 통계와 함께 필요한 항목만 가져올 수 있습니다.

또한 TSDB 블록을 Parquet 파일로 다시 작성하므로 데이터를 순차적으로 큰 청크로 읽을 수 있는 방식으로 저장할 수도 있습니다.
    
    
    sum by (instance) (hmd:release_scopes:enabled{dc_id="45"})

위의 예에서는 "(__name__, dc_id)" 튜플을 기본 정렬 키로 선택하여 이름이 "hmd:release_scopes:활성화"이고 "dc_id"에 동일한 값을 가진 메트릭이 가깝게 정렬되도록 했습니다.

이제 Parquet 게이트웨이는 쿼리와 관련된 특정 열만 가져오기 위해 정확한 R2 범위 요청을 발행합니다. 따라서 악의적인 페이로드가 메가바이트에서 킬로바이트로 줄어듭니다. 또한 이러한 파일 세그먼트는 변경할 수 없으므로 Cloudflare CDN에 적극적으로 캐시할 수 있습니다.

이렇게 하면 R2가 대기 시간이 짧은 쿼리 엔진으로 전환되므로 복잡한 유지 관리 시나리오를 장기 추세에 대해 즉시 백테스트할 수 있어 원래 TSDB 형식에서 발생했던 제한 시간 초과 및 긴 대기 시간을 피할 수 있습니다. 아래 그래프는 최근의 부하 테스트로, 동일한 쿼리 패턴에서 이전 시스템에 비해 Parquet의 P90 성능이 최대 15배에 달한 것을 보여줍니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BX8FVSJG36HNQHC5YCNS.png&w=715&h=222&f=webp&fit=cover&position=center)

Parquet 구현이 작동하는 방식을 더 심층적으로 이해하려면 PromCon EU 2025에서 개최되는[ _'TSDB를 넘어서: 최신 규모를 위한 Parquet를 통해 Prometheus 활용하기'를 시청할_](https://www.youtube.com/watch?v=wDN2w2xN6bA&list=PLoz-W_CUquUlHOg314_YttjHL0iGTdE3O&index=16) 수 있습니다.

## 확장성을 위한 구축

저희는 Cloudflare Workers를 활용하여 메모리가 부족한 시스템에서 데이터를 지능적으로 캐시하고 효율적인 관찰 가능성 도구를 사용하여 제품 및 인프라 데이터를 실시간으로 분석하는 시스템으로 전환했습니다. 우리는 네트워크 성장과 제품 성능 사이의 균형을 유지하는 유지 관리 스케줄러를 구축했습니다.

하지만 '균형'은 움직이는 목표입니다.

매일 우리는 전 세계에 걸쳐 더 많은 하드웨어를 추가하고 있으며, 고객 트래픽을 방해하지 않고 하드웨어를 유지하는 데 필요한 로직은 제품 및 유지 관리 작업의 유형이 많아질수록 기하급수적으로 어려워지고 있습니다. Cloudflare는 첫 번째 일련의 문제를 해결했지만, 이제 이렇게 방대한 규모에서만 나타나는 보다 미묘하고 복잡한 문제를 자세히 살펴보고 있습니다.

우리에게는 어려운 문제를 두려워하지 않는 엔지니어가 필요합니다. [_Cloudflare 인프라 팀에_](https://www.cloudflare.com/careers/jobs/?department=Infrastructure) 합류하여 함께 구축해 보세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fbuilding-our-maintenance-scheduler-on-workers%2F&t=Workers%EA%B0%80%20%EB%82%B4%EB%B6%80%20%EC%9C%A0%EC%A7%80%20%EA%B4%80%EB%A6%AC%20%EC%9D%BC%EC%A0%95%20%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%84%20%EA%B0%95%ED%99%94%ED%95%98%EB%8A%94%20%EB%B0%A9%EB%B2%95)[](https://x.com/intent/post?text=Workers%EA%B0%80+%EB%82%B4%EB%B6%80+%EC%9C%A0%EC%A7%80+%EA%B4%80%EB%A6%AC+%EC%9D%BC%EC%A0%95+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%84+%EA%B0%95%ED%99%94%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://bsky.app/intent/compose?text=Workers%EA%B0%80+%EB%82%B4%EB%B6%80+%EC%9C%A0%EC%A7%80+%EA%B4%80%EB%A6%AC+%EC%9D%BC%EC%A0%95+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%84+%EA%B0%95%ED%99%94%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://mastodonshare.com/?text=Workers%EA%B0%80+%EB%82%B4%EB%B6%80+%EC%9C%A0%EC%A7%80+%EA%B4%80%EB%A6%AC+%EC%9D%BC%EC%A0%95+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%84+%EA%B0%95%ED%99%94%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fbuilding-our-maintenance-scheduler-on-workers%2F)[](https://www.threads.net/intent/post?text=Workers%EA%B0%80+%EB%82%B4%EB%B6%80+%EC%9C%A0%EC%A7%80+%EA%B4%80%EB%A6%AC+%EC%9D%BC%EC%A0%95+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%84+%EA%B0%95%ED%99%94%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fbuilding-our-maintenance-scheduler-on-workers%2F)

## 관련 태그

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Prometheus](https://blog.cloudflare.com/ko-kr/tag/prometheus/)[신뢰성](https://blog.cloudflare.com/ko-kr/tag/reliability/)[인프라](https://blog.cloudflare.com/ko-kr/tag/infrastructure/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
