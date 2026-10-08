---
url: https://blog.cloudflare.com/ko-kr/async-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source/
title: \ube44\ub3d9\uae30 QUIC \ubc0f HTTP:3 \uc0ac\uc6a9\uc774 \uc26c\uc6cc\uc9d0- tokio-quiche\uac00 \uc774\uc81c \uc624\ud508 \uc18c\uc2a4\uc785\ub2c8\ub2e4 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:50.355664+00:00
---

# 비동기 QUIC 및 HTTP:3 사용이 쉬워짐- tokio-quiche가 이제 오픈 소스입니다 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/async-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source/

[블로그](https://blog.cloudflare.com/ko-kr/)

[QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)[개인정보 보호](https://blog.cloudflare.com/ko-kr/tag/privacy/)[프로토콜](https://blog.cloudflare.com/ko-kr/tag/protocols/)

3개 태그3개 태그 보기

  * 게시물 태그
  * [QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)[개인정보 보호](https://blog.cloudflare.com/ko-kr/tag/privacy/)[프로토콜](https://blog.cloudflare.com/ko-kr/tag/protocols/)
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



[QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)[개인정보 보호](https://blog.cloudflare.com/ko-kr/tag/privacy/)[프로토콜](https://blog.cloudflare.com/ko-kr/tag/protocols/)

2025년 11월 6일

# 비동기 QUIC 및 HTTP/3를 쉽게 만들 수 있습니다. tokio-quiche가 이제 오픈 소스입니다

![Pedro Mendes](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44728NW455QD7JX15VF2WS.webp&w=64&h=64&f=webp&fit=cover&position=center)![Leo Blöcher](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49579CYY7HBQE8A4NZZ9B2.webp&w=64&h=64&f=webp&fit=cover&position=center)![Evan Rittenhouse](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47GS3RW10ESS21SA5P60SX.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Fisher Darling](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463PVCFZWEEPCE2T84TW2R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Pedro Mendes](https://blog.cloudflare.com/ko-kr/author/mendes/), [Leo Blöcher](https://blog.cloudflare.com/ko-kr/author/leo-bloecher/), [Evan Rittenhouse](https://blog.cloudflare.com/ko-kr/author/evan-rittenhouse/) 및 [Fisher Darling](https://blog.cloudflare.com/ko-kr/author/fisher/)

7분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/async-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source/) 및 [日本語](https://blog.cloudflare.com/ja-jp/async-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source/).

![BLOG-2701 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48CXNHYFFSVNS19HDND8B6.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAAFyYJ2WbUHWgYn2gY3uaWnWTVHOTVniXOWeUUXWddY6vjaG+lafCkKK6gpatdYugVnGObIOfkqW/rr/YusnitMPZorDCjJqnYXWJeoufpLLHwdDly9nvws/jrLjHk56oXHGHe4ueqbbHxdHiytXnusbXoKu7iJOgSmeHcoWdpbHAvsjTuMLNnai1fouda3qRL1yIZn6bnqq4srrAoqqtd4KKSF94P1yBGleIYHqamqe0rbS4l56dYWxyFEFjGUt6)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

우리는 약 6년 전에 Rust로 작성된 오픈 소스 QUIC 구현인 [_quiche를_](https://blog.cloudflare.com/enjoy-a-slice-of-quic-and-rust/) 발표했습니다. 오늘 Cloudflare에서는 키시와 Rust **Tokio** **비동기** 런타임을 결합하여 실전에서 검증된 비동기 QUIC 라이브러리인 [**_tokio-quiche_**](https://crates.io/crates/tokio-quiche)의 오픈 소스화를 발표합니다. **tokio-quiche는** Apple iCloud 비공개 릴레이에서 Cloudflare의 프록시 B와 [_차세대 Oxy 기반_](https://blog.cloudflare.com/introducing-oxy/) 프록시를 구동하여 짧은 대기 시간과 높은 처리량으로 초당 수백만 건의 HTTP/3 요청을 처리합니다. tokio-quiche도 [_Cloudflare Warp의 MASQUE_](https://blog.cloudflare.com/zero-trust-warp-with-a-masque/) 클라이언트를 구동하여 WireGuard 터널을 QUIC 기반 터널과 [_h3i_](https://blog.cloudflare.com/h3i/)의 비동기 버전으로 대체합니다.

quiche는 [_sans-io_](https://sans-io.readthedocs.io/how-to-sans-io.html) 라이브러리로 개발되었습니다. 즉, 사용자가 IO를 수행하는 방법에 대한 가정을 하지 않고 QUIC 전송 프로토콜을 처리하는 데 필요한 상태 머신을 구현한다는 의미입니다. 즉, 그리스만 충분하다면 누구나 키시를 통한 IO 통합을 작성할 수 있습니다! 여기에는 UDP 소켓에서 연결하거나 수신하여 모든 네트워크 `정보를 quiche에` `공급하는 동안 해당`소켓에서 UDP 데이터그램 송수신을 관리하는 작업이 수반됩니다. 이 통합이 비동기적으로 이루어져야 한다는 점을 감안할 때, 비동기 Rust 런타임과 통합하면서 이 모든 작업을 수행해야 합니다. tokio-quiche를 사용하면 이러한 모든 작업이 자동으로 수행되며 그리스가 필요하지 않습니다.

### 진입 장벽 낮추기

원래 tokio-quiche는 [_Oxy의_](https://blog.cloudflare.com/introducing-oxy/) HTTP/3 _서버_ 의 코어로만 사용되었습니다. 하지만 tokio-quiche를 독립 라이브러리로 만들려면 MASQUE를 사용할 수 있는 HTTP/3 _클라이언트_ 가 필요했습니다. 우리의 Zero Trust 팀과 개인정보 보호 팀에서 WARP와 개인정보 보호 프록시를 통해 각각 데이터를 터널링하기 위해 MASQUE 클라이언트가 필요했고, 우리는 동일한 기술을 사용하여 클라이언트와 서버를 모두 구축하고 싶었습니다.

Cloudflare는 가능한 한 많은 이해관계자와 메모리 안전 QUIC 및 HTTP/3 구현을 공유하기 위해 키시를 오픈 소스로 공개했습니다. 그 당시 우리의 초점은 많은 유형의 소프트웨어에 통합되고 널리 배포될 수 있는 로우 레벨의 무작위 설계였습니다. 우리는 다양한 클라이언트와 서버에 키시를 배포하여 이러한 목표를 달성했습니다. 하지만 sans-io 라이브러리를 애플리케이션에 통합하는 과정은 오류가 발생하기 쉽고 시간이 많이 소요됩니다. tokio-quiche에서의 목표는 필요한 코드의 대부분을 직접 제공하여 진입 장벽을 낮추는 것입니다.

우리 제품과 시스템과 상호 작용하고 싶어하는 다른 사람들도 HTTP/3를 채택하지 않는다면, Cloudflare 단독으로는 HTTP/3을 수용하는 것은 무용지물입니다. tokio-quiche 오픈 소싱을 이용하면 Cloudflare 시스템과의 통합이 더욱 간단해지고 업계에서 HTTP의 새로운 표준을 도입하는 데 도움이 됩니다. 저희는 tokio-quiche를 Rust 생태계에 다시 기여함으로써 HTTP/3, QUIC, 새로운 개인 정보 보호 기술의 개발과 사용을 촉진하고자 합니다.

tokio-quiche가 내부적으로 사용된 지 수년이 지났습니다. 이를 통해 우리는 이를 개선하고 실제적인 테스트를 할 시간을 확보하여 수백만 개의 RPS를 처리할 수 있음을 입증했습니다. tokio-quiche는 독립형 HTTP/3 클라이언트나 서버가 되도록 **의도된 것이 아니지만** , 저수준 프로토콜을 구현하고 향후 더 높은 수준의 프로젝트를 허용합니다. [_readme에 서버_](https://github.com/cloudflare/quiche/tree/master/tokio-quiche#starting-an-http3-server) 및 [_클라이언트_](https://github.com/cloudflare/quiche/tree/master/tokio-quiche#sending-an-http3-request) 이벤트 루프의 예가 포함되어 있습니다.

### 바로 액터들입니다

[ _Tokio_](https://tokio.rs/) 는 가장 인기 있는 비동기식 Rust 런타임입니다. 에지에서 실행되는 수십억 개의 비동기 작업을 효율적으로 관리하고 예약하고 실행합니다. [_Cloudflare_](https://blog.cloudflare.com/20-percent-internet-upgrade/)[ _에서는_](https://blog.cloudflare.com/pingora-open-source/) Tokio를 [_광범위하게_](https://blog.cloudflare.com/introducing-oxy/) 사용하므로 키시를 키슈와 긴밀하게 통합하게 되어 tokio-quiche라는 이름이 붙었습니다. 내부적으로, tokio-quiche는 _액터_ 를 이용하여 QUIC 및 HTTP/3 상태 머신의 다양한 부분을 구동합니다. 행위자는 일반적으로 채널을 통해 전달되는 메시지를 사용하여 외부 세계와 통신하는 내부 상태를 가진 작은 작업입니다.

액터 모델은 개념적 유사성으로 인해 산-io 라이브러리를 비동기화하는 데 사용하기에 훌륭한 추상화입니다. 행위자와 sans-io 라이브러리 모두 독점적으로 액세스하려는 어떤 종류의 내부 상태를 가지고 있습니다. 두 사람 모두 일반적으로 "메시지"를 보내고 받으면서 외부 세계와 상호 작용합니다. Quiche의 "메시지"는 들어오고 나가는 네트워크 데이터를 나타내는 원시 바이트 버퍼입니다. tokio-quiche의 “메시지” 중 하나는 들어오는 UDP 패킷을 설명하는 `Incoming` 구조입니다. 이러한 유사성으로 인해 sans-io 라이브러리의 비동기화는 새 메시지 또는 IO 대기, 메시지 또는 IO를 sans-io 라이브러리가 이해할 수 있는 것으로 변환, 내부 상태 시스템 발전, 상태 시스템의 출력을 메시지로 번역 또는 마지막으로 메시지 또는 IO를 전송합니다. (Tokio의 액터에 대해 더 많은 논의가 필요하면, 해당 주제에 대한 Alice Rhyl의 [_훌륭한 블로그 게시물을_](https://ryhl.io/blog/actors-with-tokio/) 확인해보세요.)

tokio-quiche의 주요 행위자는 IO 루프 행위자로, quiche와 소켓 간에 패킷을 이동시킵니다. QUIC는 전송 프로토콜이므로 원하는 모든 애플리케이션 프로토콜을 전송할 수 있습니다. [_HTTP/3_](https://datatracker.ietf.org/doc/rfc9114/) 는 꽤 일반적이지만, [_DNS over QUIC_](https://datatracker.ietf.org/doc/rfc9250/) 와 출시될 [_Media over QUIC_](https://blog.cloudflare.com/moq/) 는 다른 예입니다. 자체 QUIC 응용 프로그램을 생성하는 데 도움이 되는 [_RFC_](https://www.rfc-editor.org/rfc/rfc9308.html) 도 있습니다! tokio-quiche는 응용 프로그램 프로토콜을 추상화하기 위해 `ApplicationOverQuic `특성을 노출합니다. 이 특성은 키시의 메서드와 기본 I/O를 추상화하여 애플리케이션 로직에 집중할 수 있도록 합니다. 예를 들어, Cloudflare의 HTTP/3 디버그 및 테스트 클라이언트인 [_h3i_](https://blog.cloudflare.com/h3i/)는 클라이언트 중심의 비 HTTP/3 `ApplicationOverQuic` 구현에 의해 구동됩니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2701 Image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47Z6TZB6KS1BV6J55G5FZS.png&w=715&h=693&f=webp&fit=cover&position=center)

서버 아키텍처 다이어그램

tokio-quiche는 `H3drive라는` HTTP/3 `중심 ApplicationOverQuic와` 함께 제공됩니다. `H3Driver` 는 quiche의 HTTP/3 모듈을 이 IO 루프에 연결하여 비동기 HTTP/3 클라이언트 또는 서버의 구성 요소를 제공합니다. 이 드라이버는 키시의 원시 HTTP/3 이벤트를 상위 수준 이벤트와 비동기 본문 데이터 스트림으로 변환하여 여러분이 여기에 현물로 응답할 수 있도록 합니다. `H3Driver` 는 그 자체로 일반적이므로, 핵심 드라이버의 이벤트에 각각 추가 동작을 쌓는 `ServerH3Driver` 및 `ClientH3Driver` 변형을 노출합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2701 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45PY9JDRC01XDGHF54GDTE.png&w=715&h=381&f=webp&fit=cover&position=center)

내부 데이터 흐름

tokio-quiche 내부에서, 우리는 소켓에서 키시로의 데이터 이동을 용이하게 하는 두 가지 중요한 작업이 생성됩니다. 첫 번째는 `InboundPacketRouter`이며, 소켓의 수신 절반을 소유하고 [_연결 ID_](https://datatracker.ietf.org/doc/html/rfc9000#name-connection-id) (DCID)별로 연결별 채널에 인바운드 데이터그램을 라우팅합니다. 두 번째 작업인 `IoWorker` 액터는 앞서 언급한 IO 루프이며 단일 키시 `연결을` 구동합니다. `ApplicationOverQuic 메서드와` 키시 호출을 산재하여 IO 상호 작용 전후의 연결을 검사할 수 있습니다.

tokio-quiche를 만드는 것에 대한 더 많은 블로그 게시물이 곧 공개될 예정입니다. 행위자 모델 및 뮤택스, UDP GRO 및 GSO, tokio Task Coop 버짓팅 등을 논의합니다.

### 다음: QUIC 및 그 이상에 대한 자세한 내용!

tokio-quick는 Tokio의 QUIC 및 HTTP/3 생태계에 Cloudflare가 투자하는 중요한 기반이지만, 여전히 자체 복잡성이 있는 빌딩 블록에 불과합니다. 앞으로는 현재의 Oxy 프록시 및 WARP 클라이언트를 구동하는 것과 동일한 사용하기 쉬운 HTTP 클라이언트 및 서버 추상화를 릴리스할 계획입니다. 개인정보 보호 [_프록시_](https://blog.cloudflare.com/privacy-edge-making-building-privacy-first-apps-easier/#privacy-preserving-proxying-built-into-applications) 고객을 위한 오픈 소스 클라이언트와 tokio-quiche를 사용하여 수백만 RPS를 처리하는 완전히 새로운 서비스를 포함하여 Cloudflare의 QUIC 및 HTTP/3에 대한 더 많은 블로그 게시물을 계속 지켜봐 주세요!

일단은 crates.io에서 [_tokio-quiche 크레이트_](https://crates.io/crates/tokio-quiche) 를 살펴보고 GitHub에서 [_소스 코드_](https://github.com/cloudflare/quiche/tree/master/tokio-quiche) 를 확인하여 여러분만의 QUIC 애플리케이션을 구축해 보세요. 단순 에코 서버, DNS-over-QUIC 클라이언트, 사용자 지정 VPN, 기능을 갖춘 HTTP 서버일 수 있습니다. 우리를 대담하게 이겨낼 수 있을까요?

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fasync-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source%2F&t=%EB%B9%84%EB%8F%99%EA%B8%B0%20QUIC%20%EB%B0%8F%20HTTP%2F3%EB%A5%BC%20%EC%89%BD%EA%B2%8C%20%EB%A7%8C%EB%93%A4%20%EC%88%98%20%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.%20tokio-quiche%EA%B0%80%20%EC%9D%B4%EC%A0%9C%20%EC%98%A4%ED%94%88%20%EC%86%8C%EC%8A%A4%EC%9E%85%EB%8B%88%EB%8B%A4)[](https://x.com/intent/post?text=%EB%B9%84%EB%8F%99%EA%B8%B0+QUIC+%EB%B0%8F+HTTP%2F3%EB%A5%BC+%EC%89%BD%EA%B2%8C+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.+tokio-quiche%EA%B0%80+%EC%9D%B4%EC%A0%9C+%EC%98%A4%ED%94%88+%EC%86%8C%EC%8A%A4%EC%9E%85%EB%8B%88%EB%8B%A4&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fasync-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fasync-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source%2F)[](https://bsky.app/intent/compose?text=%EB%B9%84%EB%8F%99%EA%B8%B0+QUIC+%EB%B0%8F+HTTP%2F3%EB%A5%BC+%EC%89%BD%EA%B2%8C+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.+tokio-quiche%EA%B0%80+%EC%9D%B4%EC%A0%9C+%EC%98%A4%ED%94%88+%EC%86%8C%EC%8A%A4%EC%9E%85%EB%8B%88%EB%8B%A4+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fasync-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source%2F)[](https://mastodonshare.com/?text=%EB%B9%84%EB%8F%99%EA%B8%B0+QUIC+%EB%B0%8F+HTTP%2F3%EB%A5%BC+%EC%89%BD%EA%B2%8C+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.+tokio-quiche%EA%B0%80+%EC%9D%B4%EC%A0%9C+%EC%98%A4%ED%94%88+%EC%86%8C%EC%8A%A4%EC%9E%85%EB%8B%88%EB%8B%A4&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fasync-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source%2F)[](https://www.threads.net/intent/post?text=%EB%B9%84%EB%8F%99%EA%B8%B0+QUIC+%EB%B0%8F+HTTP%2F3%EB%A5%BC+%EC%89%BD%EA%B2%8C+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.+tokio-quiche%EA%B0%80+%EC%9D%B4%EC%A0%9C+%EC%98%A4%ED%94%88+%EC%86%8C%EC%8A%A4%EC%9E%85%EB%8B%88%EB%8B%A4+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fasync-quic-and-http-3-made-easy-tokio-quiche-is-now-open-source%2F)

## 관련 태그

[QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)[개인정보 보호](https://blog.cloudflare.com/ko-kr/tag/privacy/)[프로토콜](https://blog.cloudflare.com/ko-kr/tag/protocols/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
