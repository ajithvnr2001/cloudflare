---
url: https://blog.cloudflare.com/ko-kr/fail-small-resilience-plan/
title: \ucf54\ub4dc \uc624\ub80c\uc9c0: \uc2e4\ud328\ub97c \ud1b5\ud55c \uc131\uc7a5 \u2014 \ucd5c\uadfc \uc0ac\uace0 \ubc1c\uc0dd\uc5d0 \ub530\ub978 Cloudflare\uc758 \ubcf5\uc6d0\ub825 \uacc4\ud68d | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:38:41.080782+00:00
---

# 코드 오렌지: 실패를 통한 성장 — 최근 사고 발생에 따른 Cloudflare의 복원력 계획 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/fail-small-resilience-plan/

[블로그](https://blog.cloudflare.com/ko-kr/)

[사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)[코드 오렌지](https://blog.cloudflare.com/ko-kr/tag/code-orange/)

3개 태그3개 태그 보기

  * 게시물 태그
  * [사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)[코드 오렌지](https://blog.cloudflare.com/ko-kr/tag/code-orange/)
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



[사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)[코드 오렌지](https://blog.cloudflare.com/ko-kr/tag/code-orange/)

2025년 12월 19일

# 코드 오렌지: 실패를 통한 성장 — 최근 사고 발생에 따른 Cloudflare의 복원력 계획

![Dane Knecht](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45BN3R68K90TS6F0H9P7YQ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Dane Knecht](https://blog.cloudflare.com/ko-kr/author/dane-knecht/)

10분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/fail-small-resilience-plan/), [Deutsch](https://blog.cloudflare.com/de-de/fail-small-resilience-plan/), [Español (Latinoamérica)](https://blog.cloudflare.com/es-la/fail-small-resilience-plan/), [Français](https://blog.cloudflare.com/fr-fr/fail-small-resilience-plan/), [日本語](https://blog.cloudflare.com/ja-jp/fail-small-resilience-plan/), [繁體中文](https://blog.cloudflare.com/zh-tw/fail-small-resilience-plan/), [简体中文](https://blog.cloudflare.com/zh-cn/fail-small-resilience-plan/) 및 [Português](https://blog.cloudflare.com/pt-br/fail-small-resilience-plan/).

![BLOG-3079 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GNZJ7D2BGC4T3BKJ7HHJ.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////97/Hz4+nu5ezy7fL28fLz7uvp////////6+713OPv3Obz5u346+706unr////////6e341uDy1eH13+n65+346Onv////////6/D92OL21uP64Ov/6e/86+30////////8/j/4uv84ez/6/T/8vf/8/T5/////////v//8Pf/8fn/+f///v///fz+/////////////P///v//////////////////////////////////////////////)

[_2025년 11월 18일_](https://blog.cloudflare.com/18-november-2025-outage/)에 Cloudflare 네트워크에서 약 2시간 10분 동안 네트워크 트래픽 전송에 심각한 오류가 발생했습니다. 거의 3주 후인 [_2025년 12월 5일_](https://blog.cloudflare.com/5-december-2025-outage/), Cloudflare 네트워크 뒤에 있는 애플리케이션의 28%에서 약 25분 동안 트래픽이 처리되지 못했습니다.

두 사고 이후 자세한 사후 분석 블로그 게시물을 게시했지만, 저희는 여러분의 신뢰를 회복하기 위해 해야 할 일이 더 많다는 것을 알고 있습니다. 오늘 저희는 이와 같은 장애가 재발하지 않도록 Cloudflare에서 진행하고 있는 노력에 관한 세부 정보를 공유하고자 합니다.

저희는 이 계획을 '**코드 오렌지: 실패를 통한 성장** '이라고 부르기로 했습니다. 이는 대규모 장애를 초래할 수 있는 오류나 실수에 대한 저희 네트워크의 복원력을 강화하려는 목표를 반영합니다. '코드 오렌지'는 이 프로젝트 작업이 다른 모든 작업보다 우선해서 처리됨을 의미합니다. 참고로, 저희 Cloudflare에서는 [_또 한 번_](https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/)의 대형 사고 후에 회사 전체 직원의 최우선 작업이 필요하게 되어 '코드 오렌지'를 선언한 적이 있습니다. 저희는 최근 발생한 사고에도 동일한 집중적인 노력이 필요하다고 생각합니다. 코드 오렌지는 그러한 노력을 가능하게 하는 저희 방식으로, 여러 팀에서 필요에 따라 협업하여 작업을 완료할 수 있게 됩니다.

코드 오렌지 작업은 세 가지 주요 영역으로 구성됩니다.

  * 네트워크에 전파되는 모든 구성 변경 사항에 대해 제어된 롤아웃 적용. 이는 현재 소프트웨어 바이너리 릴리스와 동일하게 적용됩니다.
  * 네트워크 트래픽을 처리하는 모든 시스템의 장애 모드를 검토, 개선, 테스트. 이는 예기치 않은 오류 상태를 포함한 모든 조건에서 명확하게 정의된 동작이 보이는지 확인하기 위한 것입니다.
  * 내부 '브레이크 글래스'* 절차를 변경하고 모든 순환 종속성을 제거. 이는 당사와 고객이 사고 발생 시 신속하게 조치를 취하고 문제 없이 모든 시스템에 액세스할 수 있도록 하기 위한 것입니다.



이러한 프로젝트는 마무리될 때 하나의 '빅뱅' 변화가 일어나는 것이 아니라, 진행 과정에서 반복적으로 개선이 이루어집니다. 각각의 업데이트에 따라 Cloudflare의 복원력이 향상되는 것입니다. 최종적으로, 지난 두 달간 저희가 경험한 글로벌 장애를 유발한 문제들을 포함해 Cloudflare 네트워크의 복원력이 크게 향상될 것으로 예상합니다.

저희는 이러한 사고가 고객 여러분과 인터넷 전체에 고통스러운 일임을 잘 알고 있습니다. 이러한 문제로 인해 정말 당혹스럽습니다. 이 문제를 해결하는 것은 Cloudflare 전 직원의 최우선 과제입니다.

_***** Cloudflare에서는 브레이크 클래스 절차를 통해 특정 상황에서 특정 개인의 권한 등급을 올려 시급한 조치를 수행하고 심각한 시나리오를 해결할 수 있도록 합니다._

## 문제가 있습니까?

첫 번째 사고 시, Cloudflare의 고객 사이트를 방문한 사용자들은 Cloudflare에서 요청에 대한 응답을 제공할 수 없음을 나타내는 오류 페이지를 보았습니다. 두 번째에서는 빈 페이지가 보였습니다.

두 서비스 중단 모두 유사한 패턴을 따랐습니다. 각 사고가 발생하기 직전에 저희는 전 세계 수백 개 도시에 있는 데이터 센터에 구성 변경 사항을 즉각 배포했습니다.

11월 변경 사항은 Bot Management 분류기에 대한 자동 업데이트였습니다. 저희는 봇을 식별하는 감지 기능을 구축하기 위해 저희 네트워크를 오가는 트래픽을 통해 학습하는 다양한 인공 지능 모델을 실행합니다. 저희는 이러한 시스템을 지속해서 업데이트하여 당사의 보안 보호를 회피하여 고객 사이트에 접속하려는 악의적인 행위자보다 앞서 나가려고 합니다.

12월에 발생한 사고 당시, 널리 사용되는 오픈 소스 프레임워크 React의 취약점으로부터 고객을 보호하기 위해 저희는 보안 분석가가 사용하는 보안 도구에 변경 사항을 배포하여 서명을 개선했습니다. 새로운 봇 관리 업데이트의 시급성과 마찬가지로, 저희는 취약점을 악용하려는 공격자보다 먼저 앞서나가야 했습니다. 해당 변경으로 인해 사고가 촉발되었습니다.

이 패턴은 Cloudflare가 구성 변경 사항을 배포하는 방식과 소프트웨어 업데이트를 릴리스하는 방식 간에 심각한 격차를 드러냈습니다. 소프트웨어 버전 업데이트를 릴리스할 때, 저희는 제어되고 모니터링되는 방식으로 진행합니다. 전 세계에 걸쳐 트래픽을 처리하려면 먼저 새로운 바이너리 릴리스가 나올 때마다 여러 게이트의 배포를 성공적으로 완료해야 합니다. 저희는 먼저 직원 트래픽에 배포한 후 무료 사용자를 시작으로 전 세계 고객에게 점진적으로 변경 사항을 신중하게 배포합니다. 어느 단계에서든 이상 징후가 감지되면, 인적 개입 없이 릴리스를 되돌릴 수 있습니다

당사는 해당 방법을 구성 변경 사항에 적용하지 않았습니다. 네트워크를 구동하는 핵심 소프트웨어를 출시하는 것과는 달리, 구성을 변경할 때는 소프트웨어의 작동 방식을 수정하게 되므로 즉시 변경할 수 있습니다. 저희는 고객에게도 이러한 강력한 기능을 제공합니다. 사용자가 Cloudflare에서 설정을 변경하면 그 변경 사항이 몇 초 이내에 전 세계에 걸쳐 즉시 반영됩니다

그러한 속도에는 장점이 있지만, 해결해야 할 위험도 수반됩니다. 지난 두 번의 사고를 통해, 네트워크 트래픽 처리 방식에 적용되는 모든 변경 사항에 소프트웨어 자체 변경에 적용하는 수준의 검증된 주의를 기울여야 한다는 점이 드러났습니다.

## Cloudflare에서는 구성 업데이트 배포 방식을 변경할 예정입니다

구성 변경 사항을 전 세계에 몇 초 이내에 배포할 수 있다는 점이 두 사고의 핵심적인 공통점이었습니다. 두 경우 모두 잘못된 구성으로 인하여 몇 초 만에 네트워크가 다운되었습니다.

소프트웨어 릴리스에서 **_이미 수행_** 하고 있는 것처럼, 구성에 대한 제어된 롤아웃을 도입하는 것은 코드 오렌지 계획의 가장 중요한 작업 흐름입니다.

Cloudflare에서의 구성 변경 사항은 네트워크에 매우 빠르게 전파됩니다. 사용자가 새 DNS 레코드를 생성하거나 새로운 보안 규칙을 생성하면 몇 초 이내에 네트워크상의 서버 90%에 도달합니다. 이는 내부적으로 Quicksilver라고 하는 소프트웨어 구성 요소에 의해 작동됩니다.

Quicksilver는 저희 자체 팀에서 필요한 구성 변경 사항에도 사용됩니다. 속도가 특징임: Cloudflare에서는 네트워크 동작에 매우 빠르게 대응하고 전 그 동작을 전 세계에 걸쳐 업데이트할 수 있습니다. 그러나 두 사고 모두에서, 이로 인해 게이트를 거쳐 테스트되지 않은 채로 몇 초 이내에 전체 네트워크로 전파되는 중대한 변경 사항이 발생했습니다.

네트워크 변경 사항을 거의 즉시 배포하는 기능은 대부분의 경우에 유용하지만, 필수는 아닙니다. Quicksilver 내에서 제어된 배포를 도입하여 구성 변경 사항을 코드와 동일한 방식으로 처리하는 작업을 진행하고 있습니다.

저희는 상태 기반 배포(Health Mediated Deployment, HMD) 시스템을 통해 하루에 여러 번 네트워크에 소프트웨어 업데이트를 출시합니다. 이 프레임워크에서 Cloudflare의 서비스(네트워크에 배포된 소프트웨어)를 소유한 모든 팀에서는 배포 성공 또는 실패를 나타내는 메트릭, 롤아웃 계획, 실패 시 취할 조치를 정의해야 합니다.

여러 다른 서비스마다 변수가 조금씩 다를 수 있습니다. 일부는 더 많은 데이터 센터로 진행하기 전에 더 오래 기다려야 할 수 있지만, 긍정 오류 신호가 발생하더라도 오류율에 대한 허용 오차가 더 낮은 경우도 있습니다.

배포 후, 저희 HMD 툴킷은 각 단계를 모니터링하면서 계획에 따라 신중하게 진행되기 시작합니다. 어떤 단계에서라도 실패하면 롤백이 자동으로 시작되고 필요한 경우 팀에 연락할 수 있습니다.

코드 오렌지 종료 시 구성 업데이트는 이와 동일한 프로세스를 따릅니다. 저희는 이를 통해 과거 두 차례의 사고에서 발생했던 종류의 문제가 광범위한 문제로 확산되기 훨씬 전에 신속하게 포착할 수 있을 것으로 기대합니다.

## Cloudflard에서는 서비스 간 오류 모드를 어떻게 해결할까요?

저희는 구성 변경을 더 잘 제어하여 사고가 발생하기 전에 더 많은 문제를 발견할 수 있으리라고 낙관하지만, 실수가 발생할 수 있고 또 발생하리라는 것을 알고 있습니다. 두 사고 모두에서, 고객이 Cloudflare 사용 방법을 구성하기 위해 의존하는 제어판을 포함하여 Cloudflare 네트워크 한 부분의 오류가 대부분의 기술 스택에서 문제가 되었습니다.

저희는 지리적 확장(더 많은 데이터 센터로 확산) 또는 인구 확장(직원 및 고객 유형으로 확산) 측면뿐만 아니라 신중하고 단계적인 롤아웃에 대해서도 고려해야 합니다. 또한 서비스 진행 실패(봇 관리 서비스와 같은 하나의 제품에서 대시보드와 같은 관련 없는 제품으로 확산되는)를 포함하는 더 안전한 배포를 계획해야 합니다.

이를 위해 저희는 네트워크를 구성하는 모든 핵심 제품 및 서비스 간의 인터페이스 계약을 검토하여 a) 각 인터페이스 간에 **장애가 발생할 수 있음** 을 가정하고 b) 해당 장애를 가능한 한 **가장 합리적인 방식으로** 처리합니다. 

봇 관리 서비스 장애 시로 돌아가 보면, 장애가 발생하리라고 미리 예상했더라면 어떤 고객에게도 영향이 미칠 가능성이 없도록 처리할 수 있었을 핵심 인터페이스가 최소 두 곳 있었습니다. 첫 번째 인터페이스는 손상된 구성 파일을 읽는 인터페이스였습니다. 패닉에 빠지는 대신, 트래픽이 네트워크를 통과하도록 허용하는 검증된 기본 설정이 있어야 했고, 최악의 경우 봇 감지 머신러닝 모델에 제공되는 실시간 미세 조정 기능만 잃었을 것입니다.  
  
두 번째 인터페이스는 네트워크를 운영하는 핵심 소프트웨어와 봇 관리 모듈 간의 인터페이스였습니다. 봇 관리 모듈이 실패한 경우(실제로 발생했지만) 기본적으로 트래픽을 삭제해서는 안 되었습니다. 대신, 트래픽이 적절한 분류로 통과하도록 허용한다는 더 합리적인 기본 설정을 다시 생각해 낼 수도 있었습니다.

## 향후 긴급 상황을 어떻게 더 신속하게 해결할 수 있을까요?

해당 사고들이 발생하는 동안 문제를 해결하는 데 너무 오랜 시간이 걸렸습니다. 두 경우 모두, 보안 시스템으로 인해 팀원들이 문제 해결에 필요한 도구에 접근하지 못하게 되어 상황이 악화되었고, 일부 경우에는 순환 의존성으로 인해 일부 내부 시스템을 사용할 수 없게 되면서 지체되었습니다.

보안 기업인 당사의 모든 도구는 고객 데이터 보호 및 무단 접근 방지를 위해 세분화된 액세스 제어 기능이 적용된 인증 계층 뒤에 있습니다. 이는 올바른 결정이지만, 동시에 속도가 최우선순위인 현재 프로세스와 시스템으로 인해 지체되었던 것입니다.

순환 의존성 때문에 고객 경험에도 영향이 미쳤습니다. 예를 들어, 11월 18일 사고 중에는 CAPTCHA 없는 저희 봇 솔루션 Turnstile을 사용할 수 없게 되었습니다. Cloudflare 대시보드 로그인 과정에 Turnstile이 사용됨에 따라, 활성 세션 또는 API 서비스 토큰이 없는 고객은 중요한 변경이 가장 필요한 순간에 Cloudflare에 로그인할 수 없었습니다.

저희 팀에서는 필요한 경우 보안 요구 사항을 준수하면서 올바른 도구에 최대한 신속하게 액세스할 수 있도록 모든 '브레이크 글래스' 절차와 기술을 검토하여 개선할 예정입니다. 여기에는 순환 종속성을 검토하여 제거하거나, 사고 발생 시 신속하게 이를 '우회'할 수 있는 기능이 포함됩니다. 또한 향후 발생할 수 있는 재난 상황에 대비하여 모든 팀에서 프로세스를 충분히 이해하도록 교육 훈련 빈도를 늘릴 예정입니다. 

## 언제 완료될까요?

이 게시물에서 내부적으로 진행하고 있는 작업을 모두 언급하지는 못했지만, 앞에서 자세히 설명한 작업 흐름은 팀에서 집중해야 할 최우선 과제입니다. 이러한 각 작업 흐름은 Cloudflare의 거의 모든 제품팀과 엔지니어링팀에 영향을 미치는 상세 계획과 연결됩니다. 향후 해야 할 일이 많습니다.

1분기가 말이면, 대체로 그 이전에 끝나겠지만, 다음과 같은 목표를 달성하겠습니다.

  * 구성 관리를 위해 모든 프로덕션 시스템이 상태 기반 배포(Health Mediated Deployments, HMD)로 관리되도록 합니다.
  * 각 제품군에 적합한 장애 모드를 준수하도록 시스템을 업데이트합니다.
  * 적절한 인원이 긴급 상황 발생 시 적절히 복구할 수 있도록 적절한 액세스 권한을 가질 수 있는 프로세스를 마련합니다.



이들 목표 중 일부는 앞으로도 바뀌지 않을 것입니다. 새로운 소프트웨어를 출시할 때마다 순환 종속성을 더 잘 처리해야 할 필요성이 항상 존재하며, 보안 기술이 시간이 지남에 따라 변화하는 것을 반영하여 브레이크 글래스 절차를 업데이트해야 합니다.

지난 두 번의 사고에서 Cloudflare는 사용자와 인터넷 전체에 실망을 안겨 드렸습니다. 저희는 이를 바로잡기 위해 해야 할 일이 있습니다. 이 작업이 진행되는 대로 업데이트를 공유할 예정입니다. 고객 및 파트너께서 보내주신 질문과 의견에 감사드립니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffail-small-resilience-plan%2F&t=%EC%BD%94%EB%93%9C%20%EC%98%A4%EB%A0%8C%EC%A7%80%3A%20%EC%8B%A4%ED%8C%A8%EB%A5%BC%20%ED%86%B5%ED%95%9C%20%EC%84%B1%EC%9E%A5%20%E2%80%94%20%EC%B5%9C%EA%B7%BC%20%EC%82%AC%EA%B3%A0%20%EB%B0%9C%EC%83%9D%EC%97%90%20%EB%94%B0%EB%A5%B8%20Cloudflare%EC%9D%98%20%EB%B3%B5%EC%9B%90%EB%A0%A5%20%EA%B3%84%ED%9A%8D)[](https://x.com/intent/post?text=%EC%BD%94%EB%93%9C+%EC%98%A4%EB%A0%8C%EC%A7%80%3A+%EC%8B%A4%ED%8C%A8%EB%A5%BC+%ED%86%B5%ED%95%9C+%EC%84%B1%EC%9E%A5+%E2%80%94+%EC%B5%9C%EA%B7%BC+%EC%82%AC%EA%B3%A0+%EB%B0%9C%EC%83%9D%EC%97%90+%EB%94%B0%EB%A5%B8+Cloudflare%EC%9D%98+%EB%B3%B5%EC%9B%90%EB%A0%A5+%EA%B3%84%ED%9A%8D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffail-small-resilience-plan%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffail-small-resilience-plan%2F)[](https://bsky.app/intent/compose?text=%EC%BD%94%EB%93%9C+%EC%98%A4%EB%A0%8C%EC%A7%80%3A+%EC%8B%A4%ED%8C%A8%EB%A5%BC+%ED%86%B5%ED%95%9C+%EC%84%B1%EC%9E%A5+%E2%80%94+%EC%B5%9C%EA%B7%BC+%EC%82%AC%EA%B3%A0+%EB%B0%9C%EC%83%9D%EC%97%90+%EB%94%B0%EB%A5%B8+Cloudflare%EC%9D%98+%EB%B3%B5%EC%9B%90%EB%A0%A5+%EA%B3%84%ED%9A%8D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffail-small-resilience-plan%2F)[](https://mastodonshare.com/?text=%EC%BD%94%EB%93%9C+%EC%98%A4%EB%A0%8C%EC%A7%80%3A+%EC%8B%A4%ED%8C%A8%EB%A5%BC+%ED%86%B5%ED%95%9C+%EC%84%B1%EC%9E%A5+%E2%80%94+%EC%B5%9C%EA%B7%BC+%EC%82%AC%EA%B3%A0+%EB%B0%9C%EC%83%9D%EC%97%90+%EB%94%B0%EB%A5%B8+Cloudflare%EC%9D%98+%EB%B3%B5%EC%9B%90%EB%A0%A5+%EA%B3%84%ED%9A%8D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffail-small-resilience-plan%2F)[](https://www.threads.net/intent/post?text=%EC%BD%94%EB%93%9C+%EC%98%A4%EB%A0%8C%EC%A7%80%3A+%EC%8B%A4%ED%8C%A8%EB%A5%BC+%ED%86%B5%ED%95%9C+%EC%84%B1%EC%9E%A5+%E2%80%94+%EC%B5%9C%EA%B7%BC+%EC%82%AC%EA%B3%A0+%EB%B0%9C%EC%83%9D%EC%97%90+%EB%94%B0%EB%A5%B8+Cloudflare%EC%9D%98+%EB%B3%B5%EC%9B%90%EB%A0%A5+%EA%B3%84%ED%9A%8D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffail-small-resilience-plan%2F)

## 관련 태그

[사후](https://blog.cloudflare.com/ko-kr/tag/post-mortem/)[중단](https://blog.cloudflare.com/ko-kr/tag/outage/)[코드 오렌지](https://blog.cloudflare.com/ko-kr/tag/code-orange/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
