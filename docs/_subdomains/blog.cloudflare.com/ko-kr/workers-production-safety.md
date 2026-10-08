---
url: https://blog.cloudflare.com/ko-kr/workers-production-safety/
title: \ud504\ub85c\ub355\uc158 \uc548\uc804\uc744 \uc704\ud55c \uc0c8\ub85c\uc6b4 \ub3c4\uad6c \u2014 \uc810\uc9c4\uc801 \ubc30\ud3ec, \uc18c\uc2a4 \uc9c0\ub3c4, \ub808\uc774\ud2b8 \ub9ac\ubbf8\ud305, \uc0c8\ub85c\uc6b4 SDK | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:27.879198+00:00
---

# 프로덕션 안전을 위한 새로운 도구 — 점진적 배포, 소스 지도, 레이트 리미팅, 새로운 SDK | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/workers-production-safety/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Observability](https://blog.cloudflare.com/ko-kr/tag/observability/)+22개의 태그 더 보기

5개 태그5개 태그 보기

  * 게시물 태그
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Observability](https://blog.cloudflare.com/ko-kr/tag/observability/)[Rate Limiting](https://blog.cloudflare.com/ko-kr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/ko-kr/tag/sdk/)
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



[Rate Limiting](https://blog.cloudflare.com/ko-kr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/ko-kr/tag/sdk/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Observability](https://blog.cloudflare.com/ko-kr/tag/observability/)[Rate Limiting](https://blog.cloudflare.com/ko-kr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/ko-kr/tag/sdk/)

2024년 4월 4일

# 프로덕션 안전을 위한 새로운 도구 — 점진적 배포, 소스 지도, 레이트 리미팅, 새로운 SDK

![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Tanushree Sharma](https://blog.cloudflare.com/ko-kr/author/tanushree/) 및 [Jacob Bednarz](https://blog.cloudflare.com/ko-kr/author/jacob-bednarz/)

13분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/workers-production-safety/), [Deutsch](https://blog.cloudflare.com/de-de/workers-production-safety/), [Español](https://blog.cloudflare.com/es-es/workers-production-safety/), [Français](https://blog.cloudflare.com/fr-fr/workers-production-safety/), [日本語](https://blog.cloudflare.com/ja-jp/workers-production-safety/), [繁體中文](https://blog.cloudflare.com/zh-tw/workers-production-safety/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/workers-production-safety/).

![New tools for production safety — Gradual deployments, Source maps, Rate Limiting, and new SDKs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FR4MNGHSCH0P7DD7P68W.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///+//769vXz8fDw8vHx9PLy8u7u6+fl/////vz98vT16+7y6+7z7u/17ezw5+Tm/////f3/8PP55u315ez36O356Orz5OPq////////8vb+5/D65e/85+/+6Oz55Obv////////+f3/7/f/7Pb/7fb/7fL/6uz2////////////+///+P7/9/7/9fr/8vT8/////////////////////////P//+Pv/////////////////////////////+/3/)

2024년의 Developer Week는 프로덕션 준비에 중점을 두고 있습니다. 4월 1일 월요일에, 저희가 [발표](https://blog.cloudflare.com/ko-kr/making-full-stack-easier-d1-ga-hyperdrive-queues-ko-kr/)한 내용은 [D1](https://developers.cloudflare.com/d1/), [Queues](https://developers.cloudflare.com/queues/) [Hyperdrive](https://developers.cloudflare.com/hyperdrive/), [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)이 프로덕션 규모에 맞게 준비되었으며 일반 사용자가 사용할 수 있게 되었다는 것이었습니다. 4월 2일 화요일에는 추론 플랫폼인 [Workers AI](https://developers.cloudflare.com/workers-ai/)에 대해서도 같은 내용을 [발표](https://blog.cloudflare.com/workers-ai-ga-huggingface-loras-python-support)했습니다. 그리고 아직 끝나지 않았습니다.

하지만 프로덕션 준비 상태는 귀사가 구축하는 서비스의 규모와 안정성 그 이상을 의미합니다. 안전하고 안정적으로 변경할 수 있는 도구도 필요합니다. 고객은 Cloudflare에서 제공하는 기능을 필요로 할 뿐만 아니라 Cloudflare 의 작동 방식을 앱의 요구 사항에 맞게 정확하게 제어하고 조정할 수 있어야 합니다.

오늘 저희는 Gradual Deployments, Tail Workers의 소스 매핑 스택 추적, 새로운 레이트 리미팅 API, 새로운 API SDK, Durable Objects 업데이트 등 필수적인 프로덕션 서비스를 염두에 두고 마련된 5가지 업데이트를 발표합니다. 당사의 제품은 [Access](https://developers.cloudflare.com/cloudflare-one/policies/access/), [R2](https://developers.cloudflare.com/r2/), [KV](https://developers.cloudflare.com/kv/), [대기실](https://developers.cloudflare.com/waiting-room/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Queues](https://developers.cloudflare.com/queues/), [Stream](https://developers.cloudflare.com/stream/)을 포함하여 Workers를 사용하여 구축합니다. 이러한 새로운 기능 하나하나를 직접 사용해 프로덕션에 적용할 수 있도록 준비했으며, 이제 모든 분께 제공할 수 있게 되어 기쁩니다.

### 변경 사항을 Workers 및 Durable Objects에 배포

Worker 배포는 몇 초 만에 거의 즉각적으로 이루어지며 변경 사항이 [모든 곳](https://www.cloudflare.com/network/)에 실시간으로 적용됩니다.

프로덕션 규모에 도달하면 변경할 때마다 규모와 기대치 측면에서 더 큰 위험이 수반됩니다. 99.99% 가용성 SLA를 충족하거나 야심찬 P90 대기 시간 SLO를 달성해야 합니다. 45초 동안 100%의 트래픽이 발생하는 잘못된 배포는 수백만 건의 요청 실패를 의미할 수 있습니다. 미묘한 코드 변경이 한꺼번에 적용되면 백엔드에 재시도가 폭주하여 과부하가 걸릴 수 있습니다. 이러한 것들은 저희가 Workers를 기반으로 구축된 자체 서비스에 대해 고려하고 자체적으로 완화하는 종류의 위험입니다.

이러한 위험을 완화하는 방법은 점진적인 변경 사항을 배포하는 것이며, 일반적으로 롤링 배포라고 합니다.

  1. 현재 버전의 앱이 프로덕션 환경에서 실행됩니다.
  2. 새 버전의 앱을 프로덕션에 배포하되 트래픽의 일부만 이 새 버전으로 라우팅하고 그 트래픽이 프로덕션에 '흡수'될 때까지 기다리면서 회귀 및 버그가 있는지 모니터링합니다. 나쁜 일이 발생하면 적은 비율로 조기에 발견하여(예: 1%) 트래픽을 빠르게 되돌릴 수 있습니다.
  3. 새 버전이 완전히 배포되는 시점인 100%가 될 때까지 트래픽 비율을 점진적으로 늘립니다.



오늘 저희는 [Cloudflare API](https://developers.cloudflare.com/api/operations/worker-deployments-list-deployments), [Wrangler CLI](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-wrangler), [Workers 대시보드](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#via-the-cloudflare-dashboard)를 통해 코드 변경 사항을 Workers 및 Durable Objects에 점진적으로 배포하는 최고의 방법을 공개합니다. Gradual Deployments가 오픈 베타 버전에 들어갑니다. [Workers Free 요금제](https://developers.cloudflare.com/workers/platform/pricing/#workers)를 사용하는 모든 Cloudflare 계정으로 Gradual Deployments를 사용할 수 있으며, 곧 [Workers 유료](https://developers.cloudflare.com/workers/platform/pricing/#workers) 및 Enterprise 요금제를 사용하는 Cloudflare 계정으로 점진적 배포를 사용할 수 있게 될 것입니다. 계정에 액세스 권한이 부여되면 Workers 대시보드에 배너가 표시됩니다.

프로덕션에서 Worker 또는 Durable Object의 두 가지 버전이 동시에 실행되는 경우 메트릭, 예외 및 로그를 버전별로 필터링할 수 있기를 원할 것입니다. 이를 통해 새 버전이 소량의 트래픽에만 배포될 때 프로덕션 문제를 조기에 발견하거나 트래픽을 50/50으로 분할할 때 성능 메트릭을 비교하는 데 도움이 될 수 있습니다. 저희는 또한 플랫폼 전반의 버전 수준에서 가시성을 추가했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Splitting traffic between different versions of a Worker.](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4792EFMEWR5SFVJAMDC49A.png&w=715&h=353&f=webp&fit=cover&position=center)

  * Workers 대시보드와 [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)를 통해 버전별로 Analytics를 필터링할 수 있습니다.
  * [Workers Trace Events](https://developers.cloudflare.com/workers/observability/logging/logpush/) 및 [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/) 이벤트에는 Worker 의 버전 ID와 함께 선택적 버전 메시지 및 버전 태그 필드가 포함됩니다.
  * [Wrangler Tail](https://developers.cloudflare.com/workers/wrangler/commands/#tail)을 사용하여 실시간 로그를 볼 때 특정 버전에 대한 로그를 볼 수 있습니다.
  * [버전 메타데이터 바인딩](https://developers.cloudflare.com/workers/runtime-apis/bindings/version-metadata/)을 구성하여 Worker의 코드 내에서 버전 ID, 메시지, 태그에 액세스할 수 있습니다.



또한 각 클라이언트 또는 사용자에게 일관된 버전의 Worker만 표시되도록 할 수도 있습니다. 특정 식별자(예: 사용자, 세션 또는 고유 ID)와 관련된 요청이 항상 일관된 버전의 Worker에서 처리되도록 [버전 선호도](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity)를 추가했습니다. [세션 선호도](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#version-keys-and-session-affinity)를 [규칙 집합 엔진](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/gradual-deployments/#setting-cloudflare-workers-version-key-using-ruleset-engine)과 함께 사용하면 "고착성"을 보장하는 데 사용되는 메커니즘과 식별자를 모두 완벽하게 제어할 수 있습니다.

Gradual Deployments가 오픈 베타 버전으로 전환됩니다. GA를 향해 진행해 나감에 따라 다음과 같은 지원을 위해 노력하고 있습니다.

  * **버전 재정의.** 프로덕션 트래픽을 제공하기 전에 테스트하기 위해 Worker의 특정 버전을 호출합니다. 이렇게 하면 블루-그린 배포를 생성할 수 있습니다.
  * **Cloudflare Pages.** Pages의 CI/CD 시스템이 사용자를 대신하여 자동으로 배포를 진행하도록 합니다.
  * **자동 롤백.** 새 버전의 Worker에서 오류율이 급증하면 배포를 자동으로 롤백합니다.



여러분의 피드백을 기다립니다! [이](https://www.cloudflare.com/lp/developer-week-deployments/) 피드백 양식을 통해 의견을 보내 주시거나 [개발자 Discord](https://discord.gg/HJvPcPcN)에서 #workers-gradual-deployments-beta 채널로 문의해 주세요.

### Tail Workers의 소스 매핑된 스택 추적

프로덕션 준비는 오류와 예외를 추적하고 오류를 0으로 낮추기 위해 노력하는 것을 의미합니다. 오류가 발생하면 일반적으로 가장 먼저 살펴보고 싶은 것은 오류의 [스택 추적](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack), 즉 어떤 순서로, 어떤 줄과 파일에서, 어떤 인수를 사용하여 특정 함수가 호출되었는지 입니다.

Workers 뿐만 아니라 여러 플랫폼에 걸쳐 대부분의 JavaScript 코드는 먼저 번들링되고, 종종 트랜스파일링된 후 프로덕션에 배포되기 전에 축소됩니다. 이는 성능을 최적화하기 위해 더 작은 번들을 생성하고 필요한 경우 Typescript에서 JavaScript 로 변환하기 위해 백그라운드에서 수행됩니다.

예외가 /src/index.js:1:342와 같은 스택 추적을 반환하는 것을 본 적이 있다면, 함수의 축소 코드의 342번째 문자에서 오류가 발생했다는 뜻입니다. 이는 디버깅에 그다지 도움이 되지 않습니다.

[소스 맵](https://web.dev/articles/source-maps)은 컴파일되고 축소된 코드를 작성한 원본 코드에 다시 매핑하여 이 문제를 해결합니다. 소스 맵은 JavaScript 런타임에서 반환한 스택 추적과 결합되어 사람이 읽을 수 있는 스택 추적을 표시합니다. 예를 들어, 다음 스택 추적은 Worker가 down.ts 파일의 30번째 줄에서 예기치 않은 null 값을 받았음을 보여 줍니다. 이는 디버깅에 유용한 시작점이며, 스택 추적을 아래로 이동하여 null 값을 발생시킨 설정된 호출된 함수를 이해할 수 있습니다.

그 작동 방식은 다음과 같습니다.
    
    
    Unexpected input value: null
      at parseBytes (src/down.ts:30:8)
      at down_default (src/down.ts:10:19)
      at Object.fetch (src/index.ts:11:12)

  1. wrangler.toml에서 upload_[source_maps = true](https://developers.cloudflare.com/workers/wrangler/configuration/)를 설정하면 Wrangler는 [Wrangler 배포](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) 또는 [Wrangler 버전 업로드](https://developers.cloudflare.com/workers/wrangler/commands/#versions)를 실행할 때 모든 소스 맵 파일을 자동으로 생성하고 업로드합니다.
  2. Worker에서 잡히지 않은 예외가 발생하면 소스 맵을 가져와서 예외의 스택 추적을 Worker의 원본 소스 코드 줄에 다시 매핑하는 데 사용합니다.
  3. 그런 다음 이 난독 해제된 스택 추적을 [실시간 로그](https://developers.cloudflare.com/workers/observability/logging/real-time-logs/) 또는 [Tail Workers](https://developers.cloudflare.com/workers/observability/logging/tail-workers/)에서 볼 수 있습니다.



오늘부터 오픈 베타 버전에서는 Worker를 배포할 때 소스 맵을 Cloudflare에 업로드할 수 있습니다. [문서를 읽어 보시고 시작하세요](https://developers.cloudflare.com/workers/observability/source-maps). 그리고 4월 15일부터 Workers 런타임에서 소스 맵을 사용하여 스택 추적을 난독 해제하기 시작할 것입니다. 소스 매핑된 스택 추적을 사용할 수 있게 되면 Cloudflare 대시보드에 알림을 게시하고 [Cloudflare 개발자 X 계정](https://twitter.com/CloudflareDev?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)에 게시할 예정입니다.

### API in Workers에서의 새 레이트 리미팅

API는 합리적인 [레이트 리미팅](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)이 있는 경우에만 프로덕션 준비가 완료된 것입니다. 비즈니스가 성장함에 따라 특정 고객의 요구와 균형을 맞추거나 서비스의 건전성을 보호하거나 특정 시나리오에서 제한을 적용하고 조정하기 위해 적용해야 하는 제한의 복잡성과 다양성도 증가하고 있습니다. Cloudflare의 자체 API도 이 문제를 안고 있습니다. 많은 API 엔드포인트가 있는 수십 개의 제품 각각에 서로 다른 레이트 리미팅을 적용해야 할 수 있습니다.

2017년부터 Cloudflare에서 [레이트 리미팅 규칙](https://developers.cloudflare.com/waf/rate-limiting-rules/)을 구성할 수 있었습니다. 하지만 지금까지는 Cloudflare 대시보드 또는 Cloudflare API를 통해서만 이를 제어할 수 있었습니다. _런타임_에 동작을 정의하거나 레이트 리미팅과 직접 상호 작용하는 Worker에서 코드를 작성하는 것은 불가능했으며, 요청이 Worker에 도달하기 전에만 요청이 레이트 리미팅 되는지 여부를 제어할 수 있었습니다.

오늘 오픈 베타 버전으로 Worker에서 레이트 리미팅에 직접 액세스할 수 있는 새로운 API를 소개합니다. 이 API는 멤캐시드의 지원으로 매우 빠르며, Worker에 추가하는 것도 아주 간단합니다. 예를 들어, 다음 구성은 60초 이내에 100건의 요청으로 레이트 리미팅을 정의합니다.

그런 다음 Worker에서 원하는 키를 제공하여 RATE_LIMITER 바인딩의 리미팅 메서드를 호출할 수 있습니다. 위의 구성에 따라 이 코드는 60초 동안 특정 경로에 대한 요청이 100회 이상 발생하면 [HTTP 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) 응답 상태 코드를 반환합니다.
    
    
    [[unsafe.bindings]]
    name = "RATE_LIMITER"
    type = "ratelimit"
    namespace_id = "1001" # An identifier unique to your Cloudflare account
    
    # Limit: the number of tokens allowed within a given period, in a single Cloudflare location
    # Period: the duration of the period, in seconds. Must be either 60 or 10
    simple = { limit = 100, period = 60 } 

이제 Workers 멤캐시드 같은 데이터 저장소에 직접 연결할 수 있게 되었으니, 저희가 또 무엇을 제공할 수 있을까요? 카운터? 잠금? [인메모리 캐시](https://github.com/cloudflare/workerd/pull/1666)? 레이트 리미팅은 많은 Worker [격리](https://developers.cloudflare.com/workers/reference/how-workers-works/#isolates)에 걸쳐 있는 임시 공유 상태가 어디에 있어야 하는지에 대해 저희가 수년 동안 받은 질문을 해결하기 위해 Workers에서 제공하는 많은 기본 기능 중 첫 번째입니다. 귀하가 현재 Worker의 글로벌 범위에 상태를 넣는 데 의존하고 있다면, 저희는 특정 사용 사례를 위해 특별히 제작된 더 나은 기본 기능을 개발 중입니다.
    
    
    export default {
      async fetch(request, env) {
        const { pathname } = new URL(request.url)
    
        const { success } = await env.RATE_LIMITER.limit({ key: pathname })
        if (!success) {
          return new Response(`429 Failure – rate limit exceeded for ${pathname}`, { status: 429 })
        }
    
        return new Response(`Success!`)
      }
    }

Workers의 레이트 리미팅 API는 오픈 베타 버전이며, [문서를 읽고서](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit) 시작할 수 있습니다.

### Cloudflare의 API를 위한 새로운 자동 생성 SDK

프로덕션 준비 상태란 대시보드의 버튼을 클릭하여 변경하는 방식에서 [Terraform](https://github.com/cloudflare/terraform-provider-cloudflare)이나 [Pulumi](https://github.com/pulumi/pulumi-cloudflare)와 같은 코드형 인프라 접근 방식을 사용하여 프로그래밍 방식으로 변경하거나 직접 또는 SDK를 통해 API를 직접 호출하는 방식으로 변경하는 것을 의미합니다.

[Cloudflare API](https://developers.cloudflare.com/api/)는 방대하고, 지속해서 새로운 기능이 추가되고 있으며, 평균적으로 [하루에 20~30회 정도 API 스키마를 업데이트](https://github.com/cloudflare/api-schemas/activity)합니다. 하지만 지금까지는 API SDK를 수동으로 구축하고 유지 관리해 왔으므로 이를 자동화해야 할 필요성이 절실했습니다.

저희는 그렇게 해왔고, 오늘 Cloudflare API를 위한 새로운 클라이언트 SDK를 [Typescript](https://github.com/cloudflare/cloudflare-typescript), [Python](https://github.com/cloudflare/cloudflare-python), [Go](https://github.com/cloudflare/cloudflare-go)의 세 가지 언어로 발표하며, 더 많은 언어를 준비 중입니다.

각 SDK는 각 API 엔드포인트의 구조와 기능을 정의하는 [OpenAPI](https://github.com/cloudflare/api-schemas) 스키마에 기반한 [Stainless API](https://www.stainlessapi.com/)를 사용하여 자동으로 생성됩니다. 즉, 모든 Cloudflare 제품에 걸쳐 Cloudflare API에 새로운 기능을 추가하면 이러한 API SDK가 자동으로 다시 생성되고 새 버전이 게시되어 올바른 최신 버전이 유지됩니다.

다음 명령 중 하나를 실행하여 SDK를 설치할 수 있습니다.

Terraform 또는 Pulumi를 사용하는 경우, 내부적으로 Cloudflare의 Terraform 공급자는 현재 자동화가 되지 않은 기존의 [Go SDK](https://github.com/cloudflare/cloudflare-go)를 사용합니다. Terraform 적용을 실행하면 Cloudflare Terraform 공급자가 어떤 순서로 어떤 API 호출을 수행할지 결정하고 Go SDK를 사용하여 이를 실행합니다.
    
    
    // Typescript
    npm install cloudflare
    
    // Python
    pip install cloudflare
    
    // Go
    go get -u github.com/cloudflare/cloudflare-go/v2

자동 생성되는 새로운 Go SDK는 모든 Cloudflare 제품에 대하여 보다 포괄적인 Terraform 지원을 위한 길을 열어주며, 최신 API 변경 사항을 정확하고 최신 상태로 유지할 수 있는 기본 도구 세트를 제공합니다. 저희는 Cloudflare의 제품팀에서 Cloudflare API를 통해 노출되는 새로운 기능을 개발할 때마다 SDK에서 자동으로 지원되는 미래를 향해 나아가고 있습니다. 2024년 내내 이와 관련된 더 많은 업데이트를 기대하세요.

### Durable Object 네임스페이스 분석 및 WebSocket Hibernation GA

[대기실](https://developers.cloudflare.com/waiting-room/) ,[R2](https://developers.cloudflare.com/r2/), [Queues](https://developers.cloudflare.com/queues/) 등 많은 저희 자체 제품과 [PartyKit](https://www.partykit.io/) 등의 플랫폼은 [Durable Objects](https://developers.cloudflare.com/durable-objects/)를 사용하여 구축됩니다. 새로 추가된 대양주 지원을 포함하여 전 세계에 배포된 Durable Objects는 단일 조정 지점을 제공하고 [상태를 유지](https://developers.cloudflare.com/durable-objects/api/transactional-storage-api/)할 수 있는 개체 Workers와 같다고 생각하면 됩니다. Durable Objects는 대화형 채팅이나 공동 편집과 같이 실시간 사용자 조정이 필요한 앱에 적합합니다. Atlassian의 말을 믿으세요.

> _새로운 기능 중 하나는_ _[Confluence 화이트보드](https://www.atlassian.com/software/confluence/whiteboards)이며, 이는 팀에서 보다 공식적으로 문서화하기 전에 브레인스토밍 및 초기 계획과 같은 비정형 작업을 캡처할 수 있는 자유로운 방법을 제공합니다. 팀에서는 실시간 협업을 위한 여러 옵션을 고려한 끝에 결국 Cloudflare의 Durable Objects를 사용하기로 결정했습니다. Durable Objects는 인프라를 크게 간소화하고 많은 사용자로 쉽게 확장할 수 있는 독특한 기능의 조합으로, 이 문제 공간에 아주 적합하다는 것이 입증되었습니다. -_ [_Atlassian_](https://www.atlassian.com/software/confluence/whiteboards)

이전에는 대시보드에 관련 분석 추세를 노출시키지 않았으므로 [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/)를 직접 사용하지 않는 한 [Durable Objects 네임스페이스](https://developers.cloudflare.com/durable-objects/configuration/access-durable-object-from-a-worker/#generate-ids-randomly) 내의 사용 패턴과 오류율을 파악하기 어려웠습니다. 이제 [Durable Objects 대시보드](https://dash.cloudflare.com/?to=/:account/workers/durable-objects)가 개선되어 메트릭을 세부 분석하고 필요한 만큼 깊이 있게 분석할 수 있습니다.

[첫날](https://blog.cloudflare.com/introducing-workers-durable-objects)부터 Durable Objects는 [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)을 지원하여 많은 클라이언트가 Durable Object에 직접 연결하여 메시지를 주고받을 수 있도록 했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2305 Embedded Image - tUWMOW](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NGJQ7SMHCNME7M5TATPN.png&w=715&h=557&f=webp&fit=cover&position=center)

하지만 클라이언트 앱이 WebSocket 연결을 열었다가 결국 아무것도 하지 않는 경우가 있습니다. 지난 5시간 동안 브라우저에 열어두었지만, 건드리지 않은 탭이 있다고 생각해 보세요. 그 탭에서 WebSocket을 사용하여 메시지를 주고받는 경우, 사실상 아무 용도로도 사용되지 않는 수명이 긴 TCP 연결을 갖게 됩니다. 이 연결이 Durable Object에 연결된 경우 해당 Durable Object가 계속 실행되어 어떤 일이 일어나기를 기다리므로 사용자는 메모리를 소모하고 비용을 지불해야 합니다.

이 문제를 해결하기 위해 저희가 처음 [도입한 것이 WebSocket Hibernation](https://blog.cloudflare.com/workers-pricing-scale-to-zero)이었으며, 오늘 이 기능이 베타 버전에서 벗어나 정식 버전으로 출시되었음을 알려드립니다. WebSocket Hibernation 모드를 사용하면 최대 절전 모드 중에 사용할 자동 응답을 설정하고 최대 절전 모드에서도 유지되도록 상태를 직렬화할 수 있습니다. 이렇게 하면 Durable Object가 활발하게 실행되지 않고 유휴 시간에 대한 요금이 청구되지 않도록 "최대 절전 모드"로 전환하는 동안 클라이언트로부터 열린 WebSocket 연결을 유지하는 데 필요한 입력이 Cloudflare에 제공됩니다. 그 결과 실제로 필요할 때는 항상 상태를 인메모리에 사용할 수 있지만, 필요하지 않을 때는 불필요하게 유지되지 않습니다. Durable Object가 최대 절전 모드에 있는 한, 웹소켓을 통해 연결된 활성 클라이언트가 있더라도 지속 시간에 대한 요금이 청구되지 않습니다.

저희는 또한 Durable Objects로 들어오는 WebSocket 메시지 비용에 대한 개발자들의 피드백을 들었습니다. 실시간 커뮤니케이션을 위해 더 작고 빈번한 메시지를 선호한다는 것이었습니다. 오늘부터, 수신되는 웹소켓 메시지는 요청의 1/20에 해당하는 금액이 청구됩니다(지금까지처럼 메시지 1개가 요청 1개에 해당하는 것과는 달리). [가격 책정 예시](https://developers.cloudflare.com/durable-objects/platform/pricing/#example-4)를 참고하세요.

.tg {border-collapse:collapse;border-color:#ccc;border-spacing:0;} .tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;} .tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:1px;color:#333; font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;} .tg .tg-0lax{text-align:left;vertical-align:top} .tg .tg-4kyp{color:#0E101A;text-align:left;vertical-align:top} .tg .tg-bhdc{color:#0E101A;font-weight:bold;text-align:left;vertical-align:top}

| WebSocket Connection Requests | Incoming WebSocket Messages | Billed Requests | Request Billing  
---|---|---|---|---  
Before | 10K | 432M | 432,010,000 | $64.65  
After | 10K | 432M | 21,610,000 | $3.09  
  
WebSocket 연결 요청

수신 WebSocket 메시지

청구된 요청

요청 청구

이전

10K

432M

432,010,000

$64.65

이후

10K

432M

21,610,000

$3.09

### 프로덕션 복잡성 없이 프로덕션 준비 완료

이전 세대의 클라우드 플랫폼에서 프로덕션을 준비한다는 것은 출시 속도가 느려진다는 것을 의미했습니다. 프로덕션을 준비한다는 것은 단절된 여러 도구를 하나로 연결하거나 내부 플랫폼에서 작업하기 위해 전체 팀을 구성하는 것을 의미했습니다. 장애물이 되는 플랫폼에 맞춰 자체 생산성 계층을 개조해야 했습니다.

Cloudflare 개발자 플랫폼은 성장하여 생산 준비가 되어 있고, 통합 플랫폼이 되기 위해 최선을 다하고 있습니다. 이 플랫폼에서는 제품이 직관적으로 함께 작동하고 동일한 작업을 수행하는 10가지 방법이 없으며, 함께 작동하는 것을 이해하는 데 도움이 되는 호환성 매트릭스가 필요 없게 됩니다. 이러한 각 업데이트는 제품 및 Cloudflare 플랫폼의 일부에 새로운 기능을 통합하여 이를 실제로 보여 줍니다.

이를 위해 여러분이 다음에 보고 싶은 기능뿐만 아니라 더 간소화할 수 있는 부분이나 더 잘 작동할 수 있다고 생각하는 제품에 대한 의견을 듣고자 합니다. 저희가 더 많은 도움을 드릴 수 있다고 생각되는 부분을 알려 주세요. [Cloudflare 개발자 Discord](https://discord.cloudflare.com/)는 항상 열려 있습니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkers-production-safety%2F&t=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98%20%EC%95%88%EC%A0%84%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EB%8F%84%EA%B5%AC%20%E2%80%94%20%EC%A0%90%EC%A7%84%EC%A0%81%20%EB%B0%B0%ED%8F%AC%2C%20%EC%86%8C%EC%8A%A4%20%EC%A7%80%EB%8F%84%2C%20%EB%A0%88%EC%9D%B4%ED%8A%B8%20%EB%A6%AC%EB%AF%B8%ED%8C%85%2C%20%EC%83%88%EB%A1%9C%EC%9A%B4%20SDK)[](https://x.com/intent/post?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98+%EC%95%88%EC%A0%84%EC%9D%84+%EC%9C%84%ED%95%9C+%EC%83%88%EB%A1%9C%EC%9A%B4+%EB%8F%84%EA%B5%AC+%E2%80%94+%EC%A0%90%EC%A7%84%EC%A0%81+%EB%B0%B0%ED%8F%AC%2C+%EC%86%8C%EC%8A%A4+%EC%A7%80%EB%8F%84%2C+%EB%A0%88%EC%9D%B4%ED%8A%B8+%EB%A6%AC%EB%AF%B8%ED%8C%85%2C+%EC%83%88%EB%A1%9C%EC%9A%B4+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkers-production-safety%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkers-production-safety%2F)[](https://bsky.app/intent/compose?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98+%EC%95%88%EC%A0%84%EC%9D%84+%EC%9C%84%ED%95%9C+%EC%83%88%EB%A1%9C%EC%9A%B4+%EB%8F%84%EA%B5%AC+%E2%80%94+%EC%A0%90%EC%A7%84%EC%A0%81+%EB%B0%B0%ED%8F%AC%2C+%EC%86%8C%EC%8A%A4+%EC%A7%80%EB%8F%84%2C+%EB%A0%88%EC%9D%B4%ED%8A%B8+%EB%A6%AC%EB%AF%B8%ED%8C%85%2C+%EC%83%88%EB%A1%9C%EC%9A%B4+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkers-production-safety%2F)[](https://mastodonshare.com/?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98+%EC%95%88%EC%A0%84%EC%9D%84+%EC%9C%84%ED%95%9C+%EC%83%88%EB%A1%9C%EC%9A%B4+%EB%8F%84%EA%B5%AC+%E2%80%94+%EC%A0%90%EC%A7%84%EC%A0%81+%EB%B0%B0%ED%8F%AC%2C+%EC%86%8C%EC%8A%A4+%EC%A7%80%EB%8F%84%2C+%EB%A0%88%EC%9D%B4%ED%8A%B8+%EB%A6%AC%EB%AF%B8%ED%8C%85%2C+%EC%83%88%EB%A1%9C%EC%9A%B4+SDK&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkers-production-safety%2F)[](https://www.threads.net/intent/post?text=%ED%94%84%EB%A1%9C%EB%8D%95%EC%85%98+%EC%95%88%EC%A0%84%EC%9D%84+%EC%9C%84%ED%95%9C+%EC%83%88%EB%A1%9C%EC%9A%B4+%EB%8F%84%EA%B5%AC+%E2%80%94+%EC%A0%90%EC%A7%84%EC%A0%81+%EB%B0%B0%ED%8F%AC%2C+%EC%86%8C%EC%8A%A4+%EC%A7%80%EB%8F%84%2C+%EB%A0%88%EC%9D%B4%ED%8A%B8+%EB%A6%AC%EB%AF%B8%ED%8C%85%2C+%EC%83%88%EB%A1%9C%EC%9A%B4+SDK+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fworkers-production-safety%2F)

## 관련 태그

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Observability](https://blog.cloudflare.com/ko-kr/tag/observability/)[Rate Limiting](https://blog.cloudflare.com/ko-kr/tag/rate-limiting/)[SDK](https://blog.cloudflare.com/ko-kr/tag/sdk/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Jacob Bednarz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49K001G8XNDQ04C9HC4S4S.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Jacob Bednarz](https://blog.cloudflare.com/ko-kr/author/jacob-bednarz/)

[](https://jacobbednarz.com)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
