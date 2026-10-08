---
url: https://blog.cloudflare.com/ko-kr/cloudflare-outage-on-july-17-2020/
title: 2020\ub144 7\uc6d4 17\uc77c\uc758 Cloudflare \uc11c\ube44\uc2a4 \uc911\ub2e8\uc5d0 \uad00\ud55c \ubd84\uc11d | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:47:59.107709+00:00
---

# 2020년 7월 17일의 Cloudflare 서비스 중단에 관한 분석 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/cloudflare-outage-on-july-17-2020/

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

2020년 7월 18일

# 2020년 7월 17일의 Cloudflare 서비스 중단에 관한 분석

![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[John Graham-Cumming](https://blog.cloudflare.com/ko-kr/author/john-graham-cumming/)

5분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/cloudflare-outage-on-july-17-2020/), [日本語](https://blog.cloudflare.com/ja-jp/cloudflare-outage-on-july-17-2020/), [繁體中文](https://blog.cloudflare.com/zh-tw/cloudflare-outage-on-july-17-2020/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/cloudflare-outage-on-july-17-2020/).

![Cloudflare outage on July 17, 2020](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45E37ZBEMQMP4DVWPE8YRK.png&w=1043&h=749&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////8ezr5NnY6uDf8+zr7+rp4NrX////////7+vp4NfX5tze7ubn5t7c0cS/////////6ufl2tHT4Nfb6ODi3NDOvqif////////5eDe08fK29HW5d3f18nHspOH////////39XTyrm72MvP597g2s3KspKI///////+2cnHw6ip1sXH6+Pk4tjWvaKc///////91MC9vpqY1cHA8Onn6uPhyLOw//////7907y5vJSR1cC98uvp7eflzLq3)

오늘 백본 네트워크의 구성 오류로 인해 Cloudflare 서비스의 가동이 27분 동안 중단됐습니다. Cloudflare 네트워크 전반에서 트래픽이 약 50% 감소했습니다. Cloudflare 백본 네트워크의 구조 상 이러한 가동 중단은 Cloudflare의 전 네트워크에 영향을 주지 않았고 특정 지역에 한정됐습니다.

이러한 가동 중단은, 엔지니어링팀이 백본 중 뉴어크에서 시카고 구간에서 작업 중에, 트래픽 정체를 완화하기 위해 애틀랜타에 있는 라우터의 구성을 업데이트하는 중 발생했습니다. 이 구성에 포함되어 있는 오류로 인해 백본의 모든 트래픽이 애틀랜타로 보내졌습니다. 그 결과, 애틀랜타 라우터에 과다 트래픽이 발생하여 백본에 연결된 Cloudflare 네트워크 센터들이 모두 정지했습니다.

영향을 받은 네트워크 센터는 새너제이, 댈러스, 시애틀, 로스앤젤레스, 시카고, 워싱턴 DC, 리치몬드, 뉴어크, 애틀랜타, 런던, 암스테르담, 프랑크푸르트, 파리, 스톡홀름, 모스크바, 상트페테르부르크, 상파울루, 쿠리치바, 포르투알레그리입니다. 다른 곳은 정상적으로 작동했습니다.

확실한 것은, 이번 사고는 어떠한 유형의 공격이나 보안 사고에 의해 발생한 것이 아닙니다.

이번 가동 중단에 대해 사과드리며, 이러한 사고가 재발하지 않도록 이미 백본 구성을 대폭 변경했다는 것을 알려드립니다.

### Cloudflare 백본

Cloudflare는 전 세계 많은 데이터 센터 사이에 _백본_을 운영하고 있습니다. 백본은 데이터 센터 사이에 있는 일련의 프라이빗 라인으로서 Cloudflare는 이를 사용하여 데이터 센터 사이에 더 빠르고 더 신뢰할 수 있는 경로를 구축합니다. Cloudflare는 이러한 경로를 통해 퍼블릭 인터넷을 사용하지 않고 다양한 데이터 센터 사이에 트래픽을 전달할 수 있습니다.

예를 들어, 뉴욕에 있는 웹사이트 원본 서버에 접촉하여 프라이빗 백본을 통해 캘리포니아주 새너제이는 물론 프랑크푸르트나 상파울루까지 요청을 전달합니다. 퍼블릭 인터넷을 피하기 위한 이러한 추가 옵션으로 고품질 서비스가 가능합니다. 프라이빗 네트워크를 사용하여 인터넷 정체 구간을 피할 수 있기 때문입니다. Cloudflare는 백본을 이용함으로써 인터넷 요청과 트래픽을 라우팅하는 장소와 방법에 대해 퍼블릭 인터넷보다 훨씬 강력하게 제어할 수 있습니다.

### 사고 경과

모든 시간은 UTC입니다.

먼저, 뉴어크와 시카고 사이의 백본 링크에서 문제가 발생하여 애틀랜타와 워싱턴 DC 사이의 백본 트래픽 정체가 발생했습니다.

이 문제에 대응하여 애틀랜타에서 구성을 변경했습니다. 이 변경으로 21시 12분에 가동 중단이 발생했습니다. 가동 중단이 파악된 후, 애틀랜타 라우터를 정지하였으며, 21시 39분에 트래픽이 다시 정상적으로 이동하기 시작했습니다.

얼마 지나지 않아 로그와 메트릭을 처리하는 코어 데이터 센터에서 정체가 발생하여 일부 로그가 손실되었습니다. 이 시간 동안 에지 네트워크는 정상적으로 작동했습니다.

  * 20시 25분: EWR과 ORD 사이의 백본 링크 정지
  * 20시 25분: ATL와 IAD 사이의 백본 속도 저하
  * 21시 12분 ~ 21시 39분: ATL이 백본 트래픽이 집중
  * 21시 39분 ~ 21시 47분: 백본에서 ATL 제거, 서비스 복구됨
  * 21시 47분 ~ 22시 10분: 코어 데이터 센터 정체로 일부 로그 손실, 에지 계속 작동
  * 22시 10분: 로그와 메트릭을 포함한 완전 복구



Cloudflare의 내부 트래픽 관리자 도구가 파악한 영향은 다음과 같습니다. 상단의 빨간색과 주황색 영역은 CPU 사용이 과부하에 이른 애틀랜타를 표시하며, 흰색 영역은 영향을 받은 데이터 센터가 트래픽을 더 이상 처리할 수 없어서 CPU가 거의 0에 이른 곳입니다. 이 부분이 가동 중단 구간 입니다.

영향을 받지 않은 데이터 센터에서는 사고 시간 중 CPU 사용에 변화가 없었습니다. 해당 데이터 센터는 사고 시간 중 그대로 녹색이었다는 사실에서 이를 알 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Cloudflare outage on July 17, 2020 Embedded Image - QqRlsw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46RPX0MBM7GFZT4N2SRS36.png&w=715&h=709&f=webp&fit=cover&position=center)

### 사고 내용 및 조치

애틀랜타에 백본 정체가 발생하자 저희 팀은 애틀랜타의 백본 트래픽 일부를 제거하기로 결정했습니다. 하지만 백본에서 애틀랜타 경로를 제거하는 대신, 라우터 설정의 한 줄 변경으로 인해 BGP 경로가 백본으로 누출기 시작했습니다.
    
    
    {master}[edit]
    atl01# show | compare 
    [edit policy-options policy-statement 6-BBONE-OUT term 6-SITE-LOCAL from]
    !       inactive: prefix-list 6-SITE-LOCAL { ... }

전체 코드는 다음과 같습니다.
    
    
    from {
        prefix-list 6-SITE-LOCAL;
    }
    then {
        local-preference 200;
        community add SITE-LOCAL-ROUTE;
        community add ATL01;
        community add NORTH-AMERICA;
        accept;
    }

이 코드는 local-preference를 설정하고, 일부 커뮤니티를 추가하고, prefix-list와 일치하는 경로를 수락합니다. local preference는 iBGP 세션 상의 전이 자산입니다(다음 BGP 피어로 전송됨).

올바르게 변경하였다면, prefix-list 대신 이 코드가 비활성화됐을 것입니다.

prefix-list 조건이 제거되자 라우터는 모든 BGP 경로를 다른 모든 백본 라우터로 보내라는 명령을 받았고, 이에 따라 local-preference 값이 200 증가했습니다. 유감스럽게도 당시 에지 라우터가 컴퓨팅 노드에서 받은 로컬 경로는 local-preference 값이 100이었습니다. 높은 local-preference 값이 우선하므로 로컬 컴퓨팅 노드로 향해야 할 모든 트래픽이 애틀랜타 컴퓨팅 노드로 이동했습니다.

경로가 전송되자 애틀랜타는 전 백본에서 트래픽을 끌어들이기 시작했습니다.

Cloudflare는 다음과 같이 변경을 진행하고 있습니다.

  * 백본 BGP 세션에 maximum-prefix 제한을 도입할 것입니다. 이렇게 하면 애틀랜타의 백본이 멈추겠지만, Cloudflare 네트워크는 백본 없이 올바로 작동하도록 구축되어 있습니다. 이 변경 사항은 7월 20일 월요일에 배포될 것입니다.
  * 로컬 서버 경로용 BGP local-preference 설정을 변경할 것입니다. 이러한 변경으로 한 위치가 다른 위치의 트래픽을 비슷한 방식으로 끌어들이지 못할 것입니다. 이 변경 사항은 사고 후 배포됐습니다.



### 결론

지금까지 백본 가동이 중단된 적은 없었기 때문에, 저희 팀은 신속히 대응하여 영향 받은 데이터 센터의 서비스를 복구했지만, 이는 관련된 모든 분에게 매우 고통스러운 시간이었습니다. 가동 중단으로 곤란을 겪은 고객과 Cloudflare 서비스들을 사용할 수 없었던 모든 사용자에게 사과 드립니다.

Cloudflare는 이미 백본 구성을 변경하여 이러한 사고가 재발하지 않게 하였으며 추가 변경은 월요일에 시작될 것입니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fcloudflare-outage-on-july-17-2020%2F&t=2020%EB%85%84%207%EC%9B%94%2017%EC%9D%BC%EC%9D%98%20Cloudflare%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%A4%91%EB%8B%A8%EC%97%90%20%EA%B4%80%ED%95%9C%20%EB%B6%84%EC%84%9D)[](https://x.com/intent/post?text=2020%EB%85%84+7%EC%9B%94+17%EC%9D%BC%EC%9D%98+Cloudflare+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8%EC%97%90+%EA%B4%80%ED%95%9C+%EB%B6%84%EC%84%9D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fcloudflare-outage-on-july-17-2020%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fcloudflare-outage-on-july-17-2020%2F)[](https://bsky.app/intent/compose?text=2020%EB%85%84+7%EC%9B%94+17%EC%9D%BC%EC%9D%98+Cloudflare+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8%EC%97%90+%EA%B4%80%ED%95%9C+%EB%B6%84%EC%84%9D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fcloudflare-outage-on-july-17-2020%2F)[](https://mastodonshare.com/?text=2020%EB%85%84+7%EC%9B%94+17%EC%9D%BC%EC%9D%98+Cloudflare+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8%EC%97%90+%EA%B4%80%ED%95%9C+%EB%B6%84%EC%84%9D&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fcloudflare-outage-on-july-17-2020%2F)[](https://www.threads.net/intent/post?text=2020%EB%85%84+7%EC%9B%94+17%EC%9D%BC%EC%9D%98+Cloudflare+%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A4%91%EB%8B%A8%EC%97%90+%EA%B4%80%ED%95%9C+%EB%B6%84%EC%84%9D+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fcloudflare-outage-on-july-17-2020%2F)

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
