---
url: https://blog.cloudflare.com/ko-kr/hyper-bug/
title: Hyper HTTP \ub77c\uc774\ube0c\ub7ec\ub9ac\uc5d0\uc11c \ubc84\uadf8\ub97c \ubc1c\uacac\ud55c \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:41.421539+00:00
---

# Hyper HTTP 라이브러리에서 버그를 발견한 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/hyper-bug/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Images](https://blog.cloudflare.com/ko-kr/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)+33개의 태그 더 보기

6개 태그6개 태그 보기

  * 게시물 태그
  * [Cloudflare Images](https://blog.cloudflare.com/ko-kr/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[이미지 최적화](https://blog.cloudflare.com/ko-kr/tag/image-optimization/)
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



[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[이미지 최적화](https://blog.cloudflare.com/ko-kr/tag/image-optimization/)

[Cloudflare Images](https://blog.cloudflare.com/ko-kr/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[이미지 최적화](https://blog.cloudflare.com/ko-kr/tag/image-optimization/)

2026년 6월 22일

# Hyper HTTP 라이브러리에서 버그를 발견한 방법

![Deanna Lam](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47KFXCHBMAHQ4B20STFNCC.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Diretnan Domnan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47Q4B9ZYMXFBZ5X354KFW2.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Matt Lewis](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMRANK371K7W3Y3CXQT0M.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Deanna Lam](https://blog.cloudflare.com/ko-kr/author/deanna/), [Diretnan Domnan](https://blog.cloudflare.com/ko-kr/author/diretnan-domnan/) 및 [Matt Lewis](https://blog.cloudflare.com/ko-kr/author/matt-lewis-2/)

16분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/hyper-bug/) 및 [日本語](https://blog.cloudflare.com/ja-jp/hyper-bug/).

![BLOG-3318 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WKWXBGMT7K0V773578D1B.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAQAAaRgAeUBQtVyxBWDVRVDJVUCBKTQAyQQAbUAsmajQ7ekdPfE5bc0dbYjROUxQ3QwAaWiErfkZGlFtal2BjiVdgcUJRWCU5RQAUXygrhk5JnmJdoWdlkl1gd0dOWio3RwABXiQkgUpEll5YmWJfildYcUFGWCUuSQAAWBUScT04gU9LgVNRdEhKYjM4UhIdSgAAUQAAXSooZDw8YT5BWDQ7UBwnTAAASgAATgAAUx8eVDE0TzM6SCgzRgseSgAA)

[_Images_](https://developers.cloudflare.com/images/) 서비스는 [_Workers_](https://developers.cloudflare.com/workers/) 기반으로 Rust로 구축되었으며 Cloudflare 에지 네트워크 내 모든 머신에서 실행됩니다. 클라이언트 연결을 처리하기 위해 Rust용 오픈 소스 HTTP 라이브러리인 [_hyper_](https://github.com/hyperium/hyper)를 사용합니다.

작년에 저희는 Workers에서 원격 이미지를 처리하기 위한 사용자 지정 프로그래밍 방식 워크플로우를 가능하게 하는 [_Images 바인딩을 도입했습니다_](https://blog.cloudflare.com/improve-your-media-pipelines-with-the-images-binding-for-cloudflare-workers/). 2025년 말에 저희는 Workers 런타임과 Images 서비스 간의 보다 직접적인 로컬 연결을 제공하도록 바인딩을 다시 설계했습니다.

롤아웃 직후, 우리는 바인딩의 변환 요청이 실패한다는 보고를 받았습니다. 하지만 이는 더 큰 이미지에서만 간헐적으로 발생했습니다. 더 이상하게도, 이러한 요청에 대한 응답은 오류가 기록되지 않은 채 `200` 상태를 반환했습니다. 2MB쯤 도착해야 하는 응답이 수백 킬로바이트 크기로 도착할 수도 있었습니다.

우리는 6주 동안 Images 바인딩이 처리된 이미지 데이터를 클라이언트에 반환하는 방식에 영향을 미치는 하이퍼 라이브러리의 거의 보이지 않는 버그(특정 조건에서만 발생하는 경쟁 조건)를 추적하는 데 보냈습니다. 결국, 이 문제를 해결하는 데 4줄의 코드가 필요했습니다.

### 호핑, 핸드오프, 하이퍼

개발자가 Cloudflare에서 구축하는 경우, 바인딩을 통해 Workers가 액세스할 수 있는 플랫폼 서비스 세트에서 전체 스택 애플리케이션을 구성하게 됩니다. [_바인딩_](https://developers.cloudflare.com/workers/runtime-apis/bindings/) 은 [_컴퓨팅_](https://www.cloudflare.com/products/#compute), [_스토리지_](https://www.cloudflare.com/products/#storage), [_AI 추론_](https://www.cloudflare.com/products/#ai) 및 [_미디어 처리_](https://www.cloudflare.com/products/#media)와 같은 개발자 플랫폼의 리소스에 대한 직접 API를 제공합니다.

Images 바인딩은 이미지 최적화와 전달을 분리합니다. 출력을 HTTP 응답으로 반환하지 않고도 이미지를 트랜스코딩, 합성, 조작할 수 있습니다. 또한 [_최적화 매개변수_](https://developers.cloudflare.com/images/optimization/features/) 를 [_URL 인터페이스_](https://developers.cloudflare.com/images/optimization/features/#url-interface)에서 부과하는 고정된 순서를 따르지 않고 임의의 순서로 적용할 수 있습니다. 여기에서 Worker는 이미지 데이터를 Images APIs에 직접 전달하고, 작업을 체인화하고, 처리된 결과를 스트림으로 다시 가져올 수 있습니다.
    
    
    const result = await env.IMAGES
      .input(image)
      .transform({ width: 800, rotate: 90 })
      .output({ format: "image/avif" });
    return result.response();

높은 수준에서 이미지 데이터는 다양한 서비스를 통해 이동합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3318 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WM1JKG14FT6JFWG5YX2QK.png&w=715&h=400&f=webp&fit=cover&position=center)

_파이프는 중개자와 Images 사이의 소켓 연결을 나타내며, 커널의 버퍼를 통해 한 프로세스에서 다음 프로세스로 데이터가 전달됩니다._

이 바인딩은 Workers 런타임에서 관리하는 소켓 연결을 통해 Images와 통신합니다. 소켓 연결은 두 프로세스 간의 통신 채널입니다. 소켓의 양쪽 끝에는 운영 체제의 커널이 관리하는 버퍼가 있습니다. 이 버퍼는 한 쪽에서 쓴 후 다른 쪽에서 읽기 전에 데이터가 앉는 임시 보관 영역입니다.

Hyper는 Images 서비스 측의 연결을 관리하여 소켓에서 들어오는 요청을 읽고 응답을 다시 작성합니다.

요청이 Images 바인딩을 사용하는 경우 Images 서비스는 입력을 읽고, 요청된 최적화 작업을 수행하고, 결과를 인코딩합니다. 그런 다음 전체 인코딩된 이미지를 단일 인메모리 블록으로 하이퍼에 전달합니다. 

Hyper는 이 응답 데이터를 자체 내부 버퍼에 씁니다. 이 시점에서 Hyper는 전송에 필요한 모든 바이트를 가지고 있으므로 인코딩 작업이 완료된 것으로 간주합니다. 다음 단계는 내부 버퍼를 소켓의 아웃바운드 버퍼로 플러시하여 데이터를 Images 서비스에서 다른 쪽 끝에 있는 중개자에게 이동하는 것입니다.

다른 쪽 끝의 리더가 빠른 경우 Hyper는 한 번에 모든 것을 플러시할 수 있습니다. 리더는 데이터가 도착하는 대로 빠르게 소비하므로 아웃바운드 버퍼에는 공간이 있습니다. 모든 데이터가 전송되면 하이퍼가 소켓에 `shutdown` 을 실행하여 연결이 완료되고 더 이상 데이터를 작성하지 않음을 알립니다. 그러나 리더가 느려지면(몇 밀리초라도) 아웃바운드 버퍼가 가득 차서 Hyper는 계속해서 기록할 공간이 생길 때까지 기다려야 합니다.

### 로컬 데이터 센터에서

Cloudflare 네트워크로 들어오는 모든 트래픽은 보안 및 성능 기능을 실행하고 요청을 적절한 백엔드로 라우팅하는 내부 중개 서비스인 FL을 통과합니다. 바인딩을 처음 출시했을 때 이미지 데이터는 Workers 런타임에서 FL을 통해 Images 서비스로 이동했습니다.

이 경로는 당사의 초기 릴리스에 자연스럽게 적합했으며 URL 인터페이스와 동일한 아키텍처를 따릅니다. 하지만 시간이 지나면서 FL과의 이러한 결합 때문에 제약이 되었습니다. 바인딩을 변경할 때는 모두 FL의 릴리스 주기를 따라야 했습니다.

2025년 12월, Images 팀은 동일한 머신에서 실행되는 내부 Worker 바인딩인 새로운 중개 서비스로 FL을 대체했습니다. 원래 아키텍처에서 데이터는 네트워크 소켓을 통해 FL을 통해 이동했습니다. 이 경로는 DNS 조회 및 라우팅과 같은 플로리다의 전체 처리 파이프라인 간접비를 전달했습니다.

내부 바인딩은 이를 Unix 소켓으로 대체하여 동일한 시스템에서 서비스를 직접 연결하여 FL과 네트워크 스택의 오버헤드를 우회하는 것입니다. 이를 통해 Images에 대한 요청 경로가 더 빨라지고 구속력이 있는 릴리스에 대해 팀에서 독립적으로 제어할 수 있게 되었습니다.

출시 후 며칠 만에 우리는 첫 번째 고객 보고서를 받았습니다.

### 200 OK(Not OK)

첫 번째 문제 징후는 고객이 비표준 설정에서 나타났습니다. 두 이미지 처리 계층으로 한 파이프라인이 다른 파이프라인 안에 중첩된 것입니다.

먼저, 작업자가 Images 바인딩을 사용하여 JPEG 배경 및 PNG 오버레이 레이어와 같은 R2에서 여러 개의 큰 소스 이미지를 결합된 하나의 JPEG로 합성했습니다. 둘째, URL 인터페이스를 통해 결과를 추가로 압축하고, 트랜스코딩하고, 크기를 조정했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3318 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WM3D5WAMWP2BB8FW0YNMW.png&w=715&h=400&f=webp&fit=cover&position=center)

_이 버그는 내부 파이프라인의 반환 경로에서 시작되어, 외부 파이프라인에 도달하기 전에 응답이 잘렸습니다._

내부 파이프라인(변환 바인딩)이 합성을 처리했습니다. 외부 파이프라인(변환 URL)은 확장 및 형식 변환과 같은 전송 최적화를 처리했습니다. 이 계층화된 접근 방식은 내부 파이프라인이 잘린 응답을 반환할 때 유일하게 한 수준 위에 나타납니다.
    
    
    error reading a body from connection: end of file before message length reached

외부 파이프라인은 수 메가바이트를 약속하는 `Content-Length` 헤더가 있는 내부 파이프라인으로부터 HTTP `200을 수신했습니다.` 실제 본문은 이 중 일부에 불과했습니다. 한 요청에서는 예상된 3.3MB 중 약 200KB만이 도착했습니다. 이 오류는 외부 파이프라인에서 발생한 것이지만, 잘림은 바인딩, 중개 서비스, Images 서비스 또는 그 사이의 어딘가에서 발생할 수 있습니다.

브라우저가 잘린 이미지를 수신하면 그 결과가 표시됩니다. 형식에 따라 이미지가 부분적으로 렌더링되거나(예: 하단이 누락되거나 회색으로 표시됨) 완전히 디코딩되지 않고 손상된 이미지가 표시될 수 있습니다.

### 어두운 환경에서의 디버깅

여기에서 우리는 요청 경로의 내부에서 작업하면서, 각 계층을 테스트하면서 잘림이 발생한 위치를 격리했습니다. 이러한 노력 중 일부는 막다른 길에 도달했습니다. 검색 범위를 좁힐 수 있도록 이동 경로를 제공한 사용자:

  * **재생산 구축.** 고객의 중첩 설정을 모방한 Worker를 구축한 다음 바인딩만으로 버그를 트리거할 수 있을 때까지 계층을 제거했습니다. 작은 스크립트를 통해 요청을 일괄적으로 실행할 수 있습니다. 초기 실행에서는 25개 요청 중 19개가 실패했습니다. 도착한 데이터의 양(약 200KB)은 프로덕션 환경의 소켓 버퍼 크기에 의심스러울 정도로 가까이 있었습니다. 이를 통해 문제가 고객의 구성과 관련이 없음을 확인하고 필요 시 버그를 트리거할 수 있는 안정적인 방법을 확보할 수 있게 되었습니다.
  * **제한 시간 초과 조사.** 초기에 Cloudflare는 제한 시간 초과 동작(즉, 시간 제한 후 연결이 닫힘)과 관련이 있다고 의심했습니다. 잘리는 것은 요청 지속 시간과 상관관계가 없었으므로 이 이론은 유효하지 않았습니다.
  * **하이퍼 버전 업데이트.** 버그가 처음 보고되었을 때 0.14.x를 실행하고 있었으며 최신 하이퍼 버전은 1.8.x 정도였습니다. 가장 확실한 답이 정확하고 쉬운 경우를 대비하여 하이퍼 버전 0.14, 1.7, 1.8에 걸쳐 테스트했습니다. 그러나 버그는 각 버전에서 나타났고, 이는 업스트림 수정이 없었다는 것을 의미했습니다.
  * **국지적으로 복제.** 우리는 macOS와 Debian VM에서 로컬 통합 테스트를 실행했습니다. 상당한 부하 상황에서도 로컬 요청으로 인해 실패가 트리거되지 않았습니다. 바인딩 소켓에 직접 curl 요청을 수행하고 캡처된 요청을 재생하는 것이 항상 효과가 있는 것 같았습니다. 이 버그는 실제 동시성이 소켓의 다른 쪽 끝에 있는 실제 Workers 런타임 클라이언트가 있을 때 전체 프로덕션 경로에서 나타났습니다. 그래서 런타임 자체를 의심하기 시작했습니다.
  * **Workers 런타임 배제.** 우리는 Workers 런타임이 바인딩 소켓을 통해 Images와 통신하는 데 사용하는 HTTP 클라이언트를 조사했습니다. 연결 양쪽의 추적에서는 예기치 않은 종료 또는 조기 종료를 나타내는 시스템 콜이 없었습니다. 클라이언트가 올바르게 작동했으며 다른 여러 서비스에서는 동일한 클라이언트를 문제 없이 사용했음을 확인했습니다.
  * **분산 추적.** 엔드투엔드 요청 추적을 검사해, 고객 설정의 외부 변환 계층에 도달하기 전에 잘린 본문이 이미 존재했음을 확인했습니다. 따라서 문제가 내부 파이프라인, 즉 Images 서비스를 통한 바인딩 경로로 좁혀졌습니다.
  * **중개 서비스 계측.** 우리는 응답 데이터를 전달하기 전에 신체 크기를 측정하는 계측을 중개 서비스에 추가했습니다. Images 서비스를 중단할 때 이미 본문이 잘려져 있었기 때문에 중개자는 배제되었습니다.
  * **Images 서비스 내에서의 심층 추적.** 서비스 수준에서, 요청이 처리되고 이미지가 올바르게 인코딩되었으며 응답은 HTTP `200`으로 전송되었습니다.



유일하게 일관된 신호는 버그가 타이밍에 의존적이었다는 것입니다. 프로덕션 경로에서만 실제 동시 발생하며 더 큰 이미지에서 나타납니다.

### 한 알의 진실

응용 프로그램 수준 디버깅을 위한 도구는 시스템에서 자신이 하고 있다고 생각하는 작업만을 보여주었습니다. 그러나 시스템에 따르면 모든 것은 정상이었습니다. Tracing은 응답을 보냈고, logging에서는 오류가 보고되지 않았고 Images 서비스는 모든 요청에서 `200` 을 반환했습니다.

시스템에서 실제로 무엇을 하는지 확인하기 위해 Images 서비스에 `strace` 를 연결했습니다. `strace` 는 프로세스가 커널에 수행하는 시스템 호출을 기록하여 정확히 작성된 바이트, 셧다운이 호출된 시점, 클라이언트가 종료 신호를 보냈는지 여부 등을 정확하게 나타낼 수 있습니다.

추적 설정은 복잡했습니다. `Strace` 는 시스템 콜이 발생할 때 이를 인터셉트하여 작동하므로 각각에 약간의 타이밍 오버헤드가 추가됩니다. 시스템콜을 소수로 필터링하여 이 오버헤드를 최소화했습니다. 하지만 필터를 넓히면 플러시와 셧다운 검사 사이의 타이밍을 바꾸어 버그가 완전히 사라질 수 있을 만큼 프로세스가 느려졌습니다. 이것만으로도 이 사안은 타이밍에 민감하다는 Cloudflare의 이론을 뒷받침해 주었습니다.

저희는 재생산 Worker를 사용하여 버그를 트리거하고 성공적인 요청과 실패한 요청의 syscall 출력을 비교했습니다.

요청이 성공하면 소켓 버퍼가 허용하는 만큼 응답이 청크에 기록되며, 모든 데이터를 전송한 후에만 셧다운이 호출됩니다. 예를 들면 다음과 같습니다.
    
    
    sendto(42, "HTTP/1.1 200 OK\r\nContent-Length: 14991808\r\n...", ...) = 219264
    sendto(42, "\xff\xd8\xff\xe0...", 292352) = 292352
    // ... keeps writing until buffer drains ...
    sendto(42, "...", 292352) = 292352
    shutdown(42, SHUT_WR) = 0

버그를 재현했을 때, 실패한 요청은 다음과 같았습니다.
    
    
    sendto(42, "HTTP/1.1 200 OK\r\nContent-Length: 14991808\r\n...", ...) = 219264
    shutdown(42, SHUT_WR) = 0

여기에서는 셧다운이 즉시 호출되기 전에 헤더와 본문의 일부에 대해 한 번만 쓰기가 이루어집니다. 14.9MB 응답 중 약 219KB만 전송되었습니다. 나머지 약 14.8MB의 이미지 데이터는 Hyper의 내부 버퍼를 떠나지 않았으며, 쓰기와 셧다운 사이에 클라이언트가 종료 신호를 보내지 않았습니다. 대신, Images 서비스는 진정으로 연결이 완료되었다고 생각하고 조기에 연결을 종료했습니다.

실패한 요청을 통해, 버그가 간헐적으로 트리거된 경쟁 조건이었음이 확인되었습니다. 요청 성공 또는 실패 여부는 플러시와 셧다운 작업이 겹치는지 여부에 따라 달라지며, 이는 요청마다 다릅니다. Hyper가 연결이 종료되었다고 판단한 바로 그 순간에 버퍼가 여전히 가득 차 있으면 데이터가 손실됩니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3318 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW9WMQYFZ5QYQVP0826XYCS2.png&w=715&h=400&f=webp&fit=cover&position=center)

_리더가 하이퍼 쓰기보다 느리게 소비하면 아웃바운드 버퍼가 가득 차게 됩니다. 버퍼가 고갈되기 전에 Hyper가 연결을 셧다운하면, 응답의 일부만이 중개자에게 전달됩니다. 이 불완전한 데이터는 Workers 런타임과 클라이언트로 다시 전달됩니다._

12월 아키텍처에는 이 버그가 도입되지 않았으며, 이는 수년간 여러 주요 버전에서 하이퍼 상태로 존재해 왔습니다. 그러나 새로운 중개자가 소켓의 응답 측에서 판독하는 주체를 변화시켰습니다. 우리의 실제 이론에 따르면 이전 중개자 인 FL이 응답 중에 소켓 버퍼가 거의 채워지지 않을 만큼 빠르게 데이터를 소비했습니다. 새로운 리더는 대규모 응답 중에 때때로 버퍼가 채워지는 속도로 읽습니다.

이 몇 밀리초의 배압 덕분에 다른 모든 것을 더 빠르게 만들 수 있는 개선이 도입되어 잘 드러나지 않는 곳에 숨어 있던 결함이 드러났습니다.

### Dispatch 루프의 내부

Hyper의 HTTP/1 연결 수명 주기는 `dispatch.rs`라는 파일의 상태 시스템에 의해 구동됩니다. 요청을 읽고, 응답을 쓰고, 쓰기 버퍼를 소켓에 플러시하고, 종료 시기를 결정하는 루프를 실행합니다. 간략한 형태:
    
    
    fn poll_loop(&mut self, cx: &mut Context<'_>) -> Poll<Result<(), Error>> {
        loop {
            let _ = self.poll_read(cx)?;
            let _ = self.poll_write(cx)?;
            let _ = self.poll_flush(cx)?;
    
            if !self.conn.wants_read_again() {
                return Poll::Ready(Ok(()));
            }
        }
    }

더 정확하게 말하자면, `let _` 이전의 `poll_flush` 는 버그가 있는 곳입니다.

Rust에서 `let _ = expr` 는 플러시가 아직 완료되지 않았다는 신호인 `Poll::Pending`을 포함하여 표현식의 결과를 무시합니다. 플러시 버퍼에 메가바이트가 남아 있을 수 있지만, 루프에서 찾을 수 없습니다.

요청이 실패했을 때의 정확한 이벤트 순서는 다음과 같습니다.

  1. Images 서비스는 이미지 인코딩을 완료하고 전체 응답을 단일 인메모리 블록으로 전달합니다.
  2. Hyper가 블록을 내부 버퍼에 쓰고 쓰기 상태를 `쓰기::닫힘`으로 표시합니다. 인코딩의 관점에서는 인코딩할 것이 아무것도 남지 않고 작업이 완료된 것입니다.
  3. Hyper가 `poll_flush` 를 호출하여 버퍼링된 데이터를 소켓으로 옮깁니다. 이전 예에서 소켓은 약 219KB를 허용했습니다. 나머지 ~14.8MB는 Hyper의 버퍼에 유지됩니다. 소켓이 가득 차서 커널이 `Poll::Pending`을 반환합니다.
  4. `poll_loop` 는 `Poll::Pending` 을 `let _`과 함께 버립니다.
  5. `wants_read_again()`을(를) 검사합니다. 전체 요청이 이미 수신되었으므로 `false`를 반환합니다.
  6. `poll_loop` 는 `Poll::Ready(Ok(()))`를 반환하여 루프가 완료되었음을 알리지만, 플러시가 완료되지 않았습니다.
  7. `poll_shutdown()` 이 실행됩니다. `SHUT_WR` 시스템 호출이 발행됩니다.
  8. 클라이언트는 14.9MB를 예상하지만, 219KB와 연결이 닫혔음을 나타내는 EOF(파일 끝)를 수신합니다.



두 번째 단계에서 하이퍼는 실제로 플러시되었을 때가 아니라 응답 본문이 버퍼링되는 즉시(즉, 인코딩이 완료될 때) 쓰기 작업을 완료로 표시합니다. 대부분의 경우 플러시는 단일 패스로 완료되며 이러한 구분은 보이지 않습니다. 소켓 버퍼가 차서 플러시를 기다려야 하는 경우도 있지만, Hyper는 그렇지 않습니다. 바이트는 여전히 하이퍼의 버퍼에 있으면서 소켓으로 플러시되기를 기다리고 있습니다. Hyper가 이 데이터가 여전히 버퍼에 있는 상태에서 연결을 종료합니다.

이로 인해 curl이 버그를 트리거하지 않은 이유도 설명됩니다. Curl은 데이터가 도착하는 즉시 읽습니다. 소켓 버퍼가 채워지지 않고 플러시가 항상 즉시 완료되며 삭제된 반환 값은 무해합니다. 때때로 몇 밀리초 동안 멈추는 리더를 포함한 프로덕션 경로는 정확히 잘못된 순간에 버퍼가 채워지는 유일한 구성이었습니다.

### 플러시하는 것을 잊지 마세요.

몇 주에 걸친 조사 끝에 해결 방법은 개념적으로 간단했습니다. Hyper는 계속 진행하기 전에 플러시가 실제로 수행되었는지 확인해야 했습니다.

Cloudflare의 복제 근무자가 버그가 존재하는 것을 확인했지만, 요청이 실패한 이유는 알 수 없었습니다. 수정 사항을 작성하기 전에 하이퍼 내부의 정확한 소켓 조건을 트리거할 수 있는 테스트가 필요했습니다.

우리는 버그를 유발하는 조건을 알고 있었습니다. 바로 한 가지 데이터 청크를 받아들여 차단하는 소켓이었습니다. 제어된 시나리오로 테스트하기 위해 우리는 전체 소켓 버퍼를 시뮬레이션하는 TCP 스트림 주위에 사용자 지정 래퍼를 구축했습니다. 이 래퍼는 첫 번째 쓰기에서 8KB를 허용한 다음 이후 쓰기마다 `Poll::Pending` 을 반환했으며, 이는 버퍼 배출을 중단한 리더와 유사합니다.

테스트에서는 이 제한된 소켓을 통해 500KB 응답을 전송하고 492KB가 아직 버퍼링된 상태에서 셧다운을 호출했는지 확인했습니다. 해결책이 없었습니다. 문제가 생기면서 기다렸습니다.

처음에 우리는 하이퍼의 디스패치 루프에 수정 사항을 적용했습니다. `poll_flush`의 결과를 삭제하는 대신 플러시가 실제로 완료되었는지 확인했습니다.
    
    
    let flush_result = self.poll_flush(cx)?;
    
    if flush_result.is_pending() {
        return Poll::Pending;
    }
    
    if !self.conn.wants_read_again() {
        return Poll::Ready(Ok(()));
    }

플러시가 완료되지 않았으면, 루프가 비동기 런타임에 `Poll::Pending` 을 반환합니다. 런타임은 소켓이 쓰기 가능 상태가 될 때까지 기다린 다음 작업을 다시 활성화하여 플러시를 계속합니다. 모든 데이터가 전송된 후에만 연결이 종료됩니다.

이 수정 프로그램을 배포한 결과, 버퍼가 실제로 빈 후에야 모든 바이트가 기록되고 셧다운이 호출되었습니다. 첫 번째 신고를 한 고객도 문제가 사라졌다고 확인했습니다.

초기 솔루션은 효과가 있었지만, 디스패치 루프가 문제를 해결하기에 적합한 위치가 아니었습니다. `Poll::Pending` 를 일찍 반환하면 읽기 폴링 빈도가 줄어 동일한 연결에서 다른 작업의 속도가 느려져 의도하지 않은 백프레셔가 발생할 수 있습니다. 이는 또한 단일 연결이 여러 요청을 순차적으로 처리하는 Keepalive 연결을 올바르게 처리하지 못하므로 이전 응답이 여전히 플러시되는 동안에도 재사용 가능한 상태로 유지되어야 합니다. 두 문제 모두 Keepalive가 비활성화된 특정 서비스에는 영향을 미치지 않았지만, 수정 사항이 업스트림에 기여한다면 다른 하이퍼 사용자에게 영향을 미칠 수 있습니다.

우리는 Hyper의 연결 수명 주기를 추적한 결과 보다 표적화된 접근 방식을 발견했습니다. 디스패치 루프의 작동 방식을 변경하는 대신 셧다운이 실제로 호출되는 지점에서 수정 사항을 적용했습니다. 소켓을 종료하기 전에, 하이퍼는 먼저 버퍼에 남아있는 데이터를 플러시해야 합니다.
    
    
    pub(crate) fn poll_shutdown(
        &mut self,
        cx: &mut Context<'_>,
    ) -> Poll<io::Result<()>> {
        ready!(self.poll_flush(cx)?);
        Pin::new(&mut self.io).poll_shutdown(cx)
    }

이렇게 하면 Dispatch 루프가 변경되지 않습니다. 데이터 손실이 발생할 정확한 시점, 즉 셧다운 직전에만 플러시를 추가합니다.

### 무엇을 할 수 있었는가

애플리케이션 수준의 어떤 도구에서도 유용한 단서를 제공할 오류, 충돌, 로그 항목을 나타내지 않았습니다. 애플리케이션 수준의 관찰 가능성은 인식 아래에 있는 버그에 대한 사각지대가 있을 수 있습니다.

장애는 간헐적으로 발생했으며 응답 크기에 따라 확장되고 curl과 같은 간단한 도구로 재현할 수 없었으며 시스템을 더 면밀히 관찰한 결과 사라졌습니다. 이 신호는 애플리케이션 로직이 아닌 연결 계층에 있는 타이밍 종속 버그를 가리킵니다.

저희가 달성한 혁신은 소켓에서 실제로 발생한 일을 기록하는 계층인 `Strace`와 커널 수준의 도구를 함께 사용하면서 이루어졌습니다. 기본 버그는 부분 플러시와 시스템을 더 빠르게 만든 후에만 열리는 너무 이른 셧다운 사이의 몇 밀리초 사이의 시간 동안 존재했습니다.

[_PR #4018을_](https://github.com/hyperium/hyper/pull/4018) 통해 수정과 결정론적 테스트를 `Hyperium/hyper에` 병합했습니다. 향후 Hyper 릴리스에서 사용할 수 있게 되어, Hyper의 HTTP/1 구현을 사용하는 모든 서비스에서 동일한 경쟁 조건에 대한 응답 데이터가 손실되지 않습니다.

한편, 패치를 적용한 내부 포크를 진행하고 있습니다. 이 수정으로 바인딩의 아키텍처가 안정화되어 기능을 확장할 수 있는 안정적인 기반이 마련되었습니다.

Images 바인딩은 처음에는 원격 이미지의 변환만 다뤘습니다. 이번 달 초, 저희는 [_Images 바인딩이 호스팅된 이미지 작업을 지원하여 개발자들이 Cloudflare에서 미디어가 풍부한 애플리케이션을 구축할 수 있는 통합된 방법을 제공한다_](https://developers.cloudflare.com/changelog/post/2026-06-10-hosted-images-binding/)고 발표했습니다.

바인딩이 작동하는 방식은 [_Cloudflare 문서에서 자세히 알아보세요._](https://developers.cloudflare.com/images/storage/binding/)

  


이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhyper-bug%2F&t=Hyper%20HTTP%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EC%97%90%EC%84%9C%20%EB%B2%84%EA%B7%B8%EB%A5%BC%20%EB%B0%9C%EA%B2%AC%ED%95%9C%20%EB%B0%A9%EB%B2%95)[](https://x.com/intent/post?text=Hyper+HTTP+%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EC%97%90%EC%84%9C+%EB%B2%84%EA%B7%B8%EB%A5%BC+%EB%B0%9C%EA%B2%AC%ED%95%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhyper-bug%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhyper-bug%2F)[](https://bsky.app/intent/compose?text=Hyper+HTTP+%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EC%97%90%EC%84%9C+%EB%B2%84%EA%B7%B8%EB%A5%BC+%EB%B0%9C%EA%B2%AC%ED%95%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhyper-bug%2F)[](https://mastodonshare.com/?text=Hyper+HTTP+%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EC%97%90%EC%84%9C+%EB%B2%84%EA%B7%B8%EB%A5%BC+%EB%B0%9C%EA%B2%AC%ED%95%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhyper-bug%2F)[](https://www.threads.net/intent/post?text=Hyper+HTTP+%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%EC%97%90%EC%84%9C+%EB%B2%84%EA%B7%B8%EB%A5%BC+%EB%B0%9C%EA%B2%AC%ED%95%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhyper-bug%2F)

## 관련 태그

[Cloudflare Images](https://blog.cloudflare.com/ko-kr/tag/cloudflare-images/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)[이미지 최적화](https://blog.cloudflare.com/ko-kr/tag/image-optimization/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
