---
url: https://blog.cloudflare.com/ko-kr/making-super-slurper-five-times-faster/
title: Workers, Durable Objects, Queues\ub85c Super Slurper\ub97c 5\ubc30 \ub354 \ube60\ub974\uac8c \ub9cc\ub4e4\uae30 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:01.197553+00:00
---

# Workers, Durable Objects, Queues로 Super Slurper를 5배 더 빠르게 만들기 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/making-super-slurper-five-times-faster/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Queues](https://blog.cloudflare.com/ko-kr/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)+44개의 태그 더 보기

7개 태그7개 태그 보기

  * 게시물 태그
  * [Cloudflare Queues](https://blog.cloudflare.com/ko-kr/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/ko-kr/tag/durable-objects/)[Queues](https://blog.cloudflare.com/ko-kr/tag/queues/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ko-kr/tag/r2-super-slurper/)
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



[Durable Objects](https://blog.cloudflare.com/ko-kr/tag/durable-objects/)[Queues](https://blog.cloudflare.com/ko-kr/tag/queues/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ko-kr/tag/r2-super-slurper/)

[Cloudflare Queues](https://blog.cloudflare.com/ko-kr/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/ko-kr/tag/durable-objects/)[Queues](https://blog.cloudflare.com/ko-kr/tag/queues/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ko-kr/tag/r2-super-slurper/)

2025년 4월 10일

# Workers, Durable Objects, Queues로 Super Slurper를 5배 더 빠르게 만들기

![Connor Maddox](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GJCDNCNMKRFZB06B4MZ6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Siddhant Sinha](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XJ1R2S5DZS8B6TDZBZ25.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Prasanna Sai Puvvada](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SJHBSH635BDQ2W9VQA8G.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Connor Maddox](https://blog.cloudflare.com/ko-kr/author/connor-maddox/), [Siddhant Sinha](https://blog.cloudflare.com/ko-kr/author/siddhant/) 및 [Prasanna Sai Puvvada](https://blog.cloudflare.com/ko-kr/author/prasanna-sai-puvvada/)

11분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/making-super-slurper-five-times-faster/), [Deutsch](https://blog.cloudflare.com/de-de/making-super-slurper-five-times-faster/), [Español](https://blog.cloudflare.com/es-es/making-super-slurper-five-times-faster/), [Français](https://blog.cloudflare.com/fr-fr/making-super-slurper-five-times-faster/), [日本語](https://blog.cloudflare.com/ja-jp/making-super-slurper-five-times-faster/), [繁體中文](https://blog.cloudflare.com/zh-tw/making-super-slurper-five-times-faster/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/making-super-slurper-five-times-faster/).

![BLOG-2731 Feature Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49756SEE9TPQPR5FT8SAFG.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////85OjwydfryNrx2eb36u308ezr///////+3+byvtHtu9Pz0eL65u338e7t////////3OX2tM7xr8/3yuD+5e378/Hx////////3+n7ttH2sdL8y+P/5/H/9vX2////////6fH/xtz7wt3/1+v/7vf/+/r7////////9fv/3Ov/2ev/6Pb/+P7/////////////////7vf/6/f/9f7/////////////////////9Pv/8vv/+///////////)

[_Super Slurper_](https://developers.cloudflare.com/r2/data-migration/super-slurper/)는 Cloudflare의 데이터 마이그레이션 도구로, 클라우드 개체 스토리지 공급자와 [_Cloudflare R2_](https://developers.cloudflare.com/r2/) 간의 대규모 데이터 전송을 쉽게 처리할 수 있도록 설계되었습니다. 출시 이후 수천 명의 개발자가 Super Slurper를 사용하여 AWS S3, Google Cloud Storage, [_기타 S3 호환 서비스_](https://developers.cloudflare.com/r2/data-migration/super-slurper/#supported-cloud-storage-providers) 에서 페타바이트 규모의 데이터를 R2로 이동했습니다.

하지만 Cloudflare는 그 속도를 훨씬 더 높일 수 있는 기회를 발견했습니다. [_Cloudflare Workers_](https://developers.cloudflare.com/workers/), [_Durable Objects_](https://developers.cloudflare.com/durable-objects/), [_Queues_](https://developers.cloudflare.com/queues/) 등을 기반으로 Cloudflare 개발자 플랫폼을 활용하여 Super Slurper를 처음부터 다시 설계하고, 전송 속도를 최대 5배 개선했습니다. 이 게시물에서는 초기 아키텍처, Cloudflare가 파악한 성능 병목 현상, 이를 해결한 방법, 이러한 개선 사항이 실제 환경에 미치는 효과에 대해 자세히 살펴보겠습니다.

## 초기 아키텍처 및 성능 병목 현상

Super Slurper는 원래 AWS S3에서 [_Cloudflare Images_](https://developers.cloudflare.com/images/)로 이미지를 대량으로 가져오기 위해 구축된 도구인 [_SourcingKit_](https://developers.cloudflare.com/images/upload-images/sourcing-kit/)와 아키텍처를 공유했습니다. SourcingKit은 Kubernetes에 배포되어 [_Images_](https://developers.cloudflare.com/images/) 서비스와 함께 실행되었습니다. Super Slurper 구축을 시작했을 때 Cloudflare는 이를 자체 Kubernetes 네임스페이스로 분리하고, 개체 스토리지 사용 사례에 더 쉽게 사용할 수 있도록 몇 가지 새로운 API를 도입했습니다. 이 설정은 잘 작동했으며 수천 명의 개발자가 데이터를 R2로 이동하는 데 도움이 되었습니다.

하지만 어려움이 없었던 것은 아닙니다. SourcingKit은 페타바이트급 대규모 전송에 필요한 규모를 처리하도록 설계되지 않았습니다. SourcingKit, 더 나아가 Super Slurper는 핵심 데이터 센터 중 한 곳에 위치한 Kubernetes 클러스터에서 운영되었으므로 Cloudflare의 제어판, 분석 및 기타 서비스와 컴퓨팅 리소스 및 대역폭을 공유해야 했습니다. 마이그레이션 수가 증가함에 따라 이러한 리소스 제약은 명백한 병목 현상이 되었습니다.

개체 스토리지 공급자 간에 데이터를 전송하는 서비스의 경우 작업은 간단합니다. 소스에서 개체를 나열하고, 대상으로 복사하는 작업을 반복하는 것입니다. 이것이 원래 Super Slurper가 작동한 방식이었습니다. 소스 버킷에서 개체를 나열하고, 해당 목록을 Postgres 기반 대기열(`pg_queue`)에 푸시한 다음, 일정한 속도로 이 대기열에서 가져와 개체를 복사했습니다. 개체 스토리지 마이그레이션의 규모를 고려할 때 대역폭 사용량은 필연적으로 높을 수밖에 없었습니다. 이로 인해 확장하기가 어려웠습니다.

핵심 데이터 센터에서만 작동하는 대역폭 제약을 해결하기 위해, Cloudflare는 추가로 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/)를 도입했습니다. 데이터 복사를 핵심 데이터 센터에서 처리하는 대신, Worker가 실제 복사를 수행하도록 호출하기 시작한 것입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44D530YYFHF6VPDT2G2NT5.png&w=715&h=498&f=webp&fit=cover&position=center)

Super Slurper의 사용량이 증가함에 따라 Kubernetes 리소스 사용량도 함께 증가했습니다. 데이터 전송 중 상당한 시간이 네트워크 I/O 또는 스토리지 대기 시간에 소요되었으며, 실제로 컴퓨팅 집약적인 작업을 수행하는 데는 사용되지 않았습니다. 따라서 더 많은 메모리나 더 많은 CPU가 필요한 것이 아니라 더 높은 동시성이 필요했습니다.

수요를 따라잡기 위해 Cloudflare는 복제본 수를 계속 증가시켰습니다. 하지만 결국 한계에 부딪혔습니다. Cloudflare는 수십 개의 포드 규모로 실행할 때 확장성 문제에 직면했으며, 수십 배 더 큰 규모를 원했습니다.

Cloudflare는 지금까지 이어온 아키텍처에 의존하는 대신 처음부터 전체 접근 방식을 재고하기로 결정했습니다. 약 일주일 만에 [_Cloudflare Workers_](https://developers.cloudflare.com/workers/), [_Durable Objects_](https://developers.cloudflare.com/durable-objects/), [_Queues_](https://developers.cloudflare.com/queues/)를 사용하여 대략적인 개념 증명을 구축했습니다. Cloudflare는 소스 버킷에서 개체를 나열하고, 대기열에 푸시한 다음, 대기열의 메시지를 사용하여 전송을 시작했습니다. 이는 원래 구현 방식과 매우 유사해 보일 수 있지만, Cloudflare 개발자 플랫폼을 기반으로 구축함으로써 이전보다 수십 배 더 높은 규모를 자동으로 달성할 수 있었습니다.

  * **Cloudflare Queues** : 비동기식 개체 전송을 가능하게 하고, 마이그레이션되는 개체 수에 맞게 자동으로 확장됩니다.
  * **Cloudflare Workers** : Kubernetes의 오버헤드 없이 간단한 컴퓨팅 작업을 실행하며, 프로세스의 각 부분이 실행되는 위치를 최적화하여 대기 시간을 줄이고 성능을 개선합니다.
  * **SQLite 기반 Durable Objects(DO)** : 완전히 분산된 데이터베이스 역할을 하여 단일 PostgreSQL 인스턴스의 한계를 제거합니다.
  * **Hyperdrive** : 원래 PostgreSQL 데이터베이스에서 이전 작업 데이터에 빠르게 액세스할 수 있도록 하여 이를 아카이브 저장소로 유지합니다.



몇 가지 테스트를 진행한 결과, 수백 개 개체 수준의 소규모 전송에서는 개념 증명 구현이 기존 구현 방식보다 느렸지만, 전송 규모가 수백만 개의 개체로 확장됨에 따라 기존 성능과 맞먹거나 이를 초과하는 결과를 달성했습니다. 이는 Cloudflare가 개념 증명을 프로덕션으로 전환하기 위해 시간을 투자할 필요가 있다는 신호였습니다.

Cloudflare는 개념 증명 해킹을 제거하고 안정성을 개선했으며, 전송을 훨씬 더 높은 동시성으로 확장할 수 있는 새로운 방법을 찾아냈습니다. 몇 차례의 반복 작업 끝에, 만족할 만한 결과물을 얻을 수 있었습니다.

## 새로운 아키텍처: Workers, Queues, Durable Objects

#### 처리 계층: 마이그레이션 흐름 관리

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GAXDNPXMT21H1Q8CNN7M.png&w=715&h=251&f=webp&fit=cover&position=center)

처리 계층의 중심에는 **대기열, 소비자 작업자** 가 있습니다. 이 과정은 다음과 같이 진행됩니다.

#### 마이그레이션 시작

클라이언트가 마이그레이션을 트리거하면 **API Worker** 로 전송된 요청으로 마이그레이션이 시작됩니다. 이 작업자는 마이그레이션에 대한 세부 정보를 가져와 데이터베이스에 저장하고, **List Queue** 에 메시지를 추가하여 프로세스를 시작합니다.

#### 소스 버킷 개체 나열

**List Queue Consumer** 는 본격적인 작업이 시작되는 지점입니다. 대기열에서 메시지를 가져오고, 소스 버킷 에서 개체 목록을 검색하며, 필요한 필터를 적용하고, 중요한 메타데이터를 데이터베이스에 저장합니다. 그런 다음 개체 전송 메시지를 **Transfer Queue** 에 추가하여 새로운 작업을 생성합니다.

Cloudflare는 즉시 새로운 작업 배치를 대기열에 추가하여 동시성을 극대화합니다. 내장된 제한 메커니즘은 종속 시스템 다운과 같은 예기치 않은 장애가 발생했을 때 Cloudflare 대기열에 메시지를 더 추가하지 않도록 합니다. 이를 통해 안정성을 유지하고 중단 시 과부하를 방지할 수 있습니다.

#### 효율적인 개체 전송

**Transfer Queue Consumer** Workers는 대기열에서 개체 전송 메시지를 가져와 각 개체가 한 번만 처리되도록 데이터베이스에서 개체 키를 잠급니다. 전송이 완료되면 개체의 잠금이 해제됩니다. 더 큰 개체의 경우, 이를 적절한 크기로 분할하여 멀티파트 업로드 방식으로 전송합니다.

#### 원활한 오류 처리

분산 시스템에서는 오류가 불가피하기 때문에, Cloudflare는 이에 대한 대비를 마련해야 했습니다. 일시적인 오류에 대해서는 자동 재시도 메커니즘을 구현하여, 마이그레이션 흐름이 중단되지 않도록 했습니다. 그러나 재시도로 해결할 수 없는 문제는 **Dead Letter Queue (DLQ)** 로 메시지를 이동시켜 추후 검토 및 해결을 위해 로그에 기록합니다.

#### 작업 완료 및 수명 주기 관리

모든 개체가 나열되고 전송이 진행되면 **Lifecycle Queue Consumer** 가 전체 프로세스를 주시합니다. 이 Consumer는 진행 중인 전송을 모니터링하여 누락된 개체가 없도록 보장합니다. 모든 전송이 완료되면 작업이 완료된 것으로 표시되고, 마이그레이션 프로세스가 마무리됩니다.

### 데이터베이스 계층: 내구성 있는 스토리지 및 레거시 데이터 검색

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46PPCT7KRZD27PS744HKQT.png&w=715&h=479&f=webp&fit=cover&position=center)

새로운 아키텍처를 구축할 때, Cloudflare는 대규모 데이터 세트를 처리할 수 있으면서도 과거 작업 데이터의 검색을 보장할 수 있는 강력한 솔루션이 필요하다는 것을 알고 있었습니다. **Durable Objects(DO)** 와 **Hyperdrive** 의 조합이 바로 그 역할을 했습니다.

#### Durable Objects

Cloudflare는 각 계정에 마이그레이션 작업을 추적할 수 있도록 전용 Durable Object를 할당했습니다. 각 **작업의 DO** 에는 버킷 이름, 사용자 옵션, 작업 상태 등의 중요한 세부 정보가 저장됩니다. 이를 통해 모든 것이 체계적이고 관리하기 쉽게 유지될 수 있었습니다. Cloudflare는 대규모 마이그레이션을 지원하기 위해 전송 대기 중인 모든 개체를 관리하는 **Batch DO** 를 추가했으며, 여기에는 전송 상태, 개체 키, 추가 메타데이터가 저장됩니다.

마이그레이션이 **수십억 개의 개체** 로 확장됨에 따라 Cloudflare는 스토리지에 보다 창의적으로 접근해야 했습니다. Cloudflare는 요청 부하를 분산하기 위해 샤딩 전략을 구현하여 병목 현상을 방지하고, **SQLite DO의 10GB** 스토리지 한계를 극복했습니다. 개체가 전송됨에 따라, Cloudflare는 해당 세부 정보를 정리하여 스토리지 공간을 최적화했습니다. 십억 개의 개체 키가 얼마나 많은 스토리지를 필요로 하는지는 놀라울 정도입니다!

#### Hyperdrive

Cloudflare는 수년간의 마이그레이션 기록이 있는 시스템을 재구축하고 있었으므로 과거의 모든 마이그레이션 세부 정보를 보존하고 액세스할 수 있는 방법이 필요했습니다. Hyperdrive는 레거시 시스템과의 연결고리 역할을 하며, 핵심 **PostgreSQL** 데이터베이스에서 과거 작업 데이터를 원활하게 검색할 수 있도록 지원합니다. 이 기능은 단순한 데이터 검색 메커니즘이 아니라, 복잡한 마이그레이션 시나리오를 위한 아카이브 역할도 수행합니다.

## 결과: Super Slurper, 이제 R2로 최대 5배 빠르게 데이터 전송

그렇다면, 이 모든 작업 끝에 전송 속도를 높이려는 목표를 실제로 달성했을까요?

Cloudflare는 AWS S3에서 R2로 75,000개의 개체를 마이그레이션하는 테스트를 진행했습니다. 기존 구현으로는 전송에 15분 30초가 소요되었습니다. 그러나 성능 개선 이후에는 동일한 마이그레이션이 단 3분 25초 만에 완료되었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477CPDAB1K3Y0SNDE0Z0SJ.png&w=715&h=360&f=webp&fit=cover&position=center)

올해 2월부터 프로덕션 환경에서 새로운 서비스를 사용한 마이그레이션이 시작되면서, 개체 크기 분포에 따라 일부 사례에서는 훨씬 더 큰 성능 개선이 확인되었습니다. Super Slurper는 출시된 지 [_약 2년_](https://blog.cloudflare.com/r2-super-slurper-ga/)이 되었지만, 성능 개선 덕분에 훨씬 더 많은 데이터를 이동할 수 있게 되었습니다. Super Slurper를 통해 복사된 전체 개체 중 무려 35%가 지난 두 달 동안 전송된 것입니다.

## 한계 및 이슈

새로운 아키텍처를 구축하며 Cloudflare가 직면한 가장 큰 과제 중 하나는 중복 메시지를 처리하는 것이었습니다. 중복이 발생할 수 있는 경우는 몇 가지가 있었습니다.

  * Queues는 최소 한 번 전송하므로, 전송을 확실히 보장하기 위해 소비자는 동일한 메시지를 두 번 이상 받을 수 있습니다.
  * 오류와 재시도 또한 명백한 중복을 만들어낼 수 있습니다. 예를 들어, 개체가 이미 전송된 후 Durable Object에 대한 요청이 실패하면, 재시도를 통해 동일한 개체를 다시 처리할 수 있습니다.



올바르게 처리되지 않으면 동일한 개체가 여러 번 전송될 수 있습니다. Cloudflare는 이 문제를 해결하기 위해 각 개체가 정확하게 처리되고 한 번만 전송되도록 몇 가지 전략을 구현했습니다.

  1. 개체 목록 작성은 순차적으로 진행되기 때문에(예: 개체 2를 얻으려면 개체 1 목록에서 얻은 연속 토큰이 필요함), Cloudflare는 각 목록 작성 작업에 고유한 시퀀스 ID를 할당합니다. 이를 통해 중복 목록을 감지하고 여러 프로세스가 동시에 시작되는 것을 방지할 수 있습니다. 이 방법은 데이터베이스와 대기열 작업이 완료될 때까지 기다리지 않고 다음 배치를 나열하기 때문에 특히 유용합니다. 목록 2가 실패하면 다시 시도할 수 있으며, 목록 3이 이미 시작된 경우 불필요한 재시도를 건너뛸 수 있습니다.
  2. 각 개체는 전송이 시작될 때 잠금이 설정되어 동일한 개체가 병렬로 전송되는 것을 방지합니다. 전송이 성공적으로 완료되면 개체 키를 데이터베이스에서 삭제하여 잠금을 해제합니다. 추후에 해당 개체에 대한 메시지가 다시 나타나더라도 데이터베이스에 키가 더 이상 존재하지 않으면, 메시지가 이미 전송된 것으로 안전하게 간주할 수 있습니다.
  3. Cloudflare는 카운트를 정확히 유지하기 위해 데이터베이스 트랜잭션에 의존합니다. 개체가 잠금 해제에 실패하면 카운트는 변경되지 않습니다. 마찬가지로, 데이터베이스에 개체 키 추가가 실패하면 카운트가 업데이트되지 않고, 이후 작업이 다시 시도됩니다.
  4. 마지막 안전 장치로, 대상 버킷에 개체가 이미 존재하며, 그 개체가 Cloudflare가 마이그레이션을 시작한 후에 게시되었는지 확인합니다. 만약 개체가 마이그레이션 시작 이후에 업로드된 경우, 해당 개체는 Cloudflare 프로세스(또는 다른 프로세스)에 의해 이미 전송된 것으로 간주하고 건너뛰어도 안전합니다.



![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2731 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44AHGCDWRPKVF577ESK4QA.png&w=715&h=228&f=webp&fit=cover&position=center)

## Super Slurper의 다음 계획은?

Cloudflare는 항상 Super Slurper를 더 빠르고, 확장 가능하며, 훨씬 더 사용하기 쉽게 만들기 위한 방법을 항상 모색하고 있습니다. 그리고 이는 시작에 불과합니다.

  * 최근에는 모든 [_S3 호환 스토리지 공급자_](https://developers.cloudflare.com/changelog/2025-02-24-r2-super-slurper-s3-compatible-support/)에서 마이그레이션할 수 있는 기능을 출시했습니다!
  * 현재 데이터 마이그레이션은 계정당 3개의 동시 마이그레이션으로 제한되어 있지만, Cloudflare는 이 제한을 늘리고자 합니다. 이를 통해 개체 접두사를 별도의 마이그레이션으로 나누어 병렬로 실행할 수 있게 되어, 버킷 마이그레이션 속도가 획기적으로 향상될 것입니다. Super Slurper 및 기존 개체 스토리지에서 R2로 데이터를 마이그레이션하는 방법에 대한 자세한 내용은 Cloudflare [_문서_](https://developers.cloudflare.com/r2/data-migration/super-slurper/)를 참조하세요.



추신 이번 업데이트를 통해 API 사용 방법도 훨씬 간단해져, 이제 마이그레이션을 [_프로그래밍 방식으로 관리_](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/)할 수 있습니다!

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-super-slurper-five-times-faster%2F&t=Workers%2C%20Durable%20Objects%2C%20Queues%EB%A1%9C%20Super%20Slurper%EB%A5%BC%205%EB%B0%B0%20%EB%8D%94%20%EB%B9%A0%EB%A5%B4%EA%B2%8C%20%EB%A7%8C%EB%93%A4%EA%B8%B0)[](https://x.com/intent/post?text=Workers%2C+Durable+Objects%2C+Queues%EB%A1%9C+Super+Slurper%EB%A5%BC+5%EB%B0%B0+%EB%8D%94+%EB%B9%A0%EB%A5%B4%EA%B2%8C+%EB%A7%8C%EB%93%A4%EA%B8%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-super-slurper-five-times-faster%2F)[](https://bsky.app/intent/compose?text=Workers%2C+Durable+Objects%2C+Queues%EB%A1%9C+Super+Slurper%EB%A5%BC+5%EB%B0%B0+%EB%8D%94+%EB%B9%A0%EB%A5%B4%EA%B2%8C+%EB%A7%8C%EB%93%A4%EA%B8%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-super-slurper-five-times-faster%2F)[](https://mastodonshare.com/?text=Workers%2C+Durable+Objects%2C+Queues%EB%A1%9C+Super+Slurper%EB%A5%BC+5%EB%B0%B0+%EB%8D%94+%EB%B9%A0%EB%A5%B4%EA%B2%8C+%EB%A7%8C%EB%93%A4%EA%B8%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-super-slurper-five-times-faster%2F)[](https://www.threads.net/intent/post?text=Workers%2C+Durable+Objects%2C+Queues%EB%A1%9C+Super+Slurper%EB%A5%BC+5%EB%B0%B0+%EB%8D%94+%EB%B9%A0%EB%A5%B4%EA%B2%8C+%EB%A7%8C%EB%93%A4%EA%B8%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmaking-super-slurper-five-times-faster%2F)

## 관련 태그

[Cloudflare Queues](https://blog.cloudflare.com/ko-kr/tag/cloudflare-queues/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Durable Objects](https://blog.cloudflare.com/ko-kr/tag/durable-objects/)[Queues](https://blog.cloudflare.com/ko-kr/tag/queues/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[R2 Super Slurper](https://blog.cloudflare.com/ko-kr/tag/r2-super-slurper/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
