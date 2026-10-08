---
url: https://blog.cloudflare.com/ko-kr/tcp-resets-timeouts/
title: Cloudflare Radar\uc758 TCP \uc7ac\uc124\uc815 \ubc0f \uc81c\ud55c \uc2dc\uac04 \ucd08\uacfc\uc5d0 \ub300\ud55c \uc778\uc0ac\uc774\ud2b8 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:36:17.057362+00:00
---

# Cloudflare Radar의 TCP 재설정 및 제한 시간 초과에 대한 인사이트 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/tcp-resets-timeouts/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Radar](https://blog.cloudflare.com/ko-kr/tag/cloudflare-radar/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인터넷 트래픽](https://blog.cloudflare.com/ko-kr/tag/internet-traffic/)+11개의 태그 더 보기

4개 태그4개 태그 보기

  * 게시물 태그
  * [Radar](https://blog.cloudflare.com/ko-kr/tag/cloudflare-radar/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인터넷 트래픽](https://blog.cloudflare.com/ko-kr/tag/internet-traffic/)[인터넷 품질](https://blog.cloudflare.com/ko-kr/tag/internet-quality/)
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



[인터넷 품질](https://blog.cloudflare.com/ko-kr/tag/internet-quality/)

[Radar](https://blog.cloudflare.com/ko-kr/tag/cloudflare-radar/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인터넷 트래픽](https://blog.cloudflare.com/ko-kr/tag/internet-traffic/)[인터넷 품질](https://blog.cloudflare.com/ko-kr/tag/internet-quality/)

2024년 9월 5일

# Cloudflare Radar의 TCP 재설정 및 제한 시간 초과에 대한 인사이트

![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Luke Valenta](https://blog.cloudflare.com/ko-kr/author/luke/)

24분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/tcp-resets-timeouts/), [日本語](https://blog.cloudflare.com/ja-jp/tcp-resets-timeouts/), [繁體中文](https://blog.cloudflare.com/zh-tw/tcp-resets-timeouts/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/tcp-resets-timeouts/).

![1622-1-Hero](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW486Q2JXV8WYJ701EQQ3RW0.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////78e/v5OTn5ufo7u/s8fHt7+zp///////+7Orx3Nzp3N/r5unw7e7x7evs/////v7/6Ob11dXt09jv3+T26ez27evx////////6ej61Nbz0tj23ub86u788O73////////8PD/3eD52uL95e//8Pb/9fT8////////+vz/6u//6PH/8fv/+f///Pz/////////////9vv/9f7/+///////////////////////+v//+f//////////////)

Cloudflare에서는 전 세계에 걸쳐 초당 6천만 건 이상의 HTTP 요청을 처리하며, 그중 [약 70%](https://radar.cloudflare.com/adoption-and-usage)는 [TCP](https://datatracker.ietf.org/doc/html/rfc9293) 연결을 통해 수신됩니다(나머지는 [QUIC](https://datatracker.ietf.org/doc/html/rfc9000)/[UDP](https://datatracker.ietf.org/doc/html/rfc768) 요청). 이상적으로는, Cloudflare에 대한 모든 새 TCP 연결마다 성공적인 데이터 교환을 가져오는 하나 이상의 요청이 전달되지만, 이는 진실과는 거리가 멉니다. 실제로는 전 세계적으로 요청을 완료하기 전이나 초기 요청 직후에, Cloudflare 서버에 대한 새로운 TCP 연결 중 [20% 가량](https://radar.cloudflare.com/security-and-attacks/#tcp-resets-and-timeouts)이 제한 시간 초과되거나 TCP '중단' 메시지와 함께 연결이 끊깁니다.

이 게시물에서는 유용한 데이터 교환이 발생하기 전에 여러 가지 이유로 서버에 대하여 예기치 않게 중단된 것으로 보이는 연결을 살펴봅니다. Cloudflare의 작업에 따르면 일반적으로 연결은 클라이언트에서 종료되지만, 타사 간섭으로 인해 연결이 닫힐 수도 있습니다. 오늘 Cloudflare Radar에서 새로운 [대시보드](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)와 [API 엔드포인트](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary)를 출시하게 되어 기쁩니다. 이 엔드포인트는 재설정이나 시간 초과로 인해 처음 10개의 유입 패킷 내에서 종료되는 Cloudflare 네트워크에 대한 TCP 연결을 거의 실시간으로 보여줍니다. 이 게시물에서는 이를 _비정상_ TCP 연결이라고 합니다. 이 비정상적인 동작을 분석하면 스캐닝, 연결 변조, DoS 공격, 연결 문제, 기타 동작에 대한 인사이트를 얻을 수 있습니다.

Radar를 통해 이 데이터를 생성하고 공유하는 Cloudflare의 능력은 [연결 변조](https://blog.cloudflare.com/connection-tampering)에 대한 글로벌 조사를 통해 이루어집니다. 독자 여러분께서는 상호 검토(peer review) [연구](https://research.cloudflare.com/publications/SundaraRaman2023/)의 기술적 세부 사항을 읽거나 [해당 프레젠테이션](https://youtu.be/RD73IgzQMFo?si=OWvNnlNNLalbhygV&t=2984)을 참조하시기 바랍니다. 계속 읽어보시면서 데이터를 사용하고 해석하는 방법, 다른 사람들이 우리의 접근 방식을 따라할 수 있도록 Cloudflare에서 감지 메커니즘을 설계하고 배포한 방법을 알아보세요.

시작하면서 먼저 정상 TCP 연결과 비정상 TCP 연결의 분류를 살펴보겠습니다.

## **설정에서 종료까지의 TCP 연결**

전송 제어 프로토콜(TCP)은 인터넷의 두 호스트 간에 데이터를 안정적으로 전송하기 위한 프로토콜([RFC 9293](https://datatracker.ietf.org/doc/rfc9293/))입니다. TCP 연결은 연결 설정에서 데이터 전송 및 연결 종료까지 여러 단계를 거칩니다.

TCP 연결은 3방향 핸드셰이크로 설정됩니다. 클라이언트라고 불리는 한 당사자가 'SYN' 플래그가 표시된 패킷을 전송하여 연결 프로세스를 초기화하면서 핸드셰이크가 시작됩니다. 서버에서는 'ACK' 플래그가 클라이언트의 초기화 'SYN'을 승인하는 'SYN+ACK' 패킷으로 응답합니다. 추가 동기화 정보는 초기화 패킷과 패킷의 응답 모두에 포함되어 있습니다. 마지막으로 클라이언트가 서버의 SYN+ACK 패킷을 최종 ACK 패킷에 대하여 확인하여 핸드셰이크를 완료합니다.

그러면 데이터 전송을 위한 연결 준비가 완료됩니다. 일반적으로 클라이언트는 첫 번째 데이터 포함 패킷에 PSH 플래그를 설정하여 서버의 TCP 스택에 데이터를 애플리케이션에 즉시 전달하라는 신호를 보냅니다. 양쪽 당사자는 연결이 더 이상 필요하지 않을 때까지 계속 데이터를 전송하고 수신된 데이터를 확인하고, 그 시점에 연결이 닫힙니다.

[RFC 9293](https://datatracker.ietf.org/doc/html/rfc9293#section-3.6)은 TCP 연결이 닫힐 수 있는 두 가지 방식을 설명합니다.

  * 정상적이고 단계적인 TCP 종료 시퀀스는 FIN 교환을 이용합니다. 어느 쪽 당사자든 더 이상 전송할 데이터가 없음을 나타내기 위해 FIN 플래그가 설정된 패킷을 보낼 수 있습니다. 상대방이 해당 FIN 패킷을 확인하면 그 방향의 연결이 닫힙니다. 승인하는 당사자가 데이터 전송을 마치면 연결의 각 방향을 독립적으로 닫아야 하므로 자체 FIN 패킷을 전송하여 닫습니다.
  * 한 당사자가 RST 패킷을 전송하여 다른 당사자에게 즉시 모든 연결 상태를 닫고 삭제하도록 지시하는 중단 또는 '재설정' 신호. 재설정은 일반적으로 복구할 수 없는 오류가 발생했을 때 전송됩니다.



다음 시퀀스 다이어그램에는 FIN으로 정상적으로 닫히는 연결의 전체 수명이 나와있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EYYYZCT4S29FV5WY9DFT.png&w=715&h=718&f=webp&fit=cover&position=center)

_정상적인 TCP 연결은 3방향 핸드셰이크로 시작하여 FIN 핸드셰이크로 끝납니다_

또한 TCP 연결은 데이터 수신 또는 승인 없이 연결이 활성화될 수 있는 최대 기간을 지정하는 [_제한 시간 초과_](https://blog.cloudflare.com/ko-kr/when-tcp-sockets-refuse-to-die/)에 의해 종료될 수 있습니다. 예를 들어 비활성 연결은 [_Keepalive_](https://blog.cloudflare.com/ko-kr/when-tcp-sockets-refuse-to-die/) 메시지로 열린 상태로 유지할 수 있습니다. 재정의하지 않는 한 RFC 9293에 지정된 글로벌 기본 기간은 5분입니다.

저희는 TCP 연결이 클라이언트 측에서 재설정이나 제한 시간 초과로 인해 닫히는 경우를 _비정상적인 상황_ 으로 간주합니다.

## **비정상적인 연결의 출처**

비정상적인 TCP 연결은 그 자체로는 문제가 없을 수 있지만, 특히 TCP 연결의 초기(데이터 이전) 단계에서 발생하는 경우 더 큰 문제의 증상일 수 있습니다. 다음은 재설정 또는 제한 시간 초과가 관찰될 수 있는 잠재적 원인의 목록이지만, 전체 목록은 아닙니다.

  * **스캐너** : 인터넷 스캐너는 서버가 주어진 포트에서 응답하는 경우 프로브에 SYN 패킷을 보낼 수 있지만, 그렇지 않은 경우 프로브가 서버로부터 응답을 이끌어낸 후에는 연결을 정리하지 못합니다.
  * **갑작스러운 애플리케이션 종료** : 열려 있는 연결이 더 이상 필요하지 않은 경우 애플리케이션에서 해당 연결을 갑자기 닫을 수 있습니다. 예를 들어, 웹 브라우저에서 탭을 닫은 후 연결을 종료하기 위해 RST를 보내거나, 장치에 전원이 들어오거나 연결이 끊긴 경우 연결 시간이 초과될 수 있습니다.
  * **네트워크 오류** : 불안정한 네트워크 상태(예: 끊어진 케이블 연결로 인해 연결 제한 시간 초과가 발생할 수 있음)
  * **공격** : 악의적인 클라이언트가 비정상적인 연결로 보이는 공격 트래픽을 보낼 수 있습니다. 예를 들어 [SYN 폭주](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)(반쯤 개방) 공격에서 공격자는 이러한 반쯤 개방된 연결을 유지하고 있는 리소스를 압도하기 위해 대상 서버에 SYN 패킷을 반복해서 전송합니다.
  * **변조** : 클라이언트와 서버 간의 패킷을 가로챌 수 있는 방화벽이나 다른 미들 장비는 패킷을 삭제하여 통신 당사자에게 제한 시간 초과를 일으킬 수 있습니다. 심층 패킷 검사(DPI)가 가능한 미들 장비는 TCP 프로토콜이 인증되지 않고 암호화되지 않았다는 사실을 활용하여 [_패킷_](https://en.wikipedia.org/wiki/Packet_injection)을 [주입](https://en.wikipedia.org/wiki/Packet_injection)하여 연결 상태를 방해할 수도 있습니다. 연결 변조에 대한 자세한 내용은 [동반된 블로그 게시물](https://blog.cloudflare.com/connection-tampering)을 참조하세요.



비정상적인 연결의 규모와 근본적인 이유를 이해하면 장애를 완화하고 보다 강력하고 안정적인 네트워크를 구축하는 데 도움이 될 수 있습니다. 저희가 이러한 인사이트를 공개적으로 공유하는 것이 전 세계 네트워크의 투명성과 책임성을 개선하는 데 도움이 되기를 바랍니다.

## データセットの使用方法

이 섹션에서는 이전에 알려진 행동 확인, 후속 연구를 위한 새로운 대상 탐색, 시간에 따른 네트워크 행동의 변화를 포착하기 위한 종단 연구 등 세 가지 사용 사례를 크게 설명하여 TCP 재설정 및 제한 시간 초과 데이터 집합을 해석하는 방법에 대한 지침과 예를 제공합니다.

각 예에서 그래프는 비정상적인 연결이 닫힌 연결의 단계에 해당하며, 이는 이상 현상의 원인이 무엇인지에 대한 중요한 단서를 제공합니다. 들어오는 각각의 연결을 다음 단계 중 하나에 배치합니다.

**포스트-SYN(핸드셰이크 중간)** : 서버가 클라이언트의 SYN 패킷을 수신한 후 연결이 재설정되거나 제한 시간 초과됩니다. 당사 서버는 응답했지만 재설정 또는 제한 시간 초과 전에 클라이언트로부터 확인 ACK 패킷이 돌아오지 않았습니다. [패킷 스푸핑](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/)은 이 연결 단계에서 흔하므로 지리적 위치 정보는 특히 신뢰할 수 없습니다.

**포스트 ACK(핸드셰이크 바로 후)** : 핸드셰이크가 완료되고 연결이 성공적으로 설정된 후 연결이 재설정되거나 제한 시간 초과가 발생합니다. 이후 전송되었을 수 있는 데이터는 저희 서버에 도달하지 않았습니다.

**포스트 PSH(첫 번째 데이터 패킷 이후)** : 서버가 PSH 플래그가 설정된 패킷을 수신한 후 연결이 재설정되거나 제한 시간 초과됩니다. PSH 플래그는 TCP 패킷에 애플리케이션에 전달할 준비가 된 데이터(예: [TLS 클라이언트 Hello](https://www.cloudflare.com/en-gb/learning/ssl/what-happens-in-a-tls-handshake/#:~:text=The%20%27client%20hello%27%20message%3A) 메시지)가 포함되어 있음을 나타냅니다.

**이후(다중 데이터 패킷 후)** : 클라이언트로부터 첫 10개 패킷 내에 연결이 재설정되지만, 서버가 여러 데이터 패킷을 수신한 후.

**없음** : 다른 모든 연결.

합법적인 연결에 초점을 맞추기 위해, Cloudflare의 공격 완화 시스템에서 연결을 처리하고 필터링한 후 데이터 세트를 구성합니다. 데이터 세트를 구성하는 방법에 대한 자세한 내용은 [아래](https://blog.cloudflare.com/tcp-resets-timeouts/#anomalousTCP)를 참조하세요.

### **자제 평가로 시작하기**

시작하려면 독자 여러분께서 [Radar 대시보드](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)를 방문하여 전 세계 및 자국과 ISP에 대한 결과를 확인해 보는 것을 권장합니다.

아래와 같이 전 세계에 걸쳐 Cloudflare 네트워크에 대한 새로운 TCP 연결의 약 20%가 클라이언트로부터 첫 10패킷 이내에 재설정 또는 제한 시간 초과에 따라 닫힙니다. 이 수치는 놀라울 정도로 높은 것으로 보이지만, 이전 연구와 일치합니다. 앞으로 살펴보겠지만, 재설정 및 제한 시간 초과 비율은 국가와 네트워크에 따라 크게 다르며, 이러한 차이는 글로벌 평균에서는 사라집니다.  


![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![2544-2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44T7FYEJ2F73EQD8Q5FAY7.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

[미국](https://radar.cloudflare.com/us)은 제 모국으로, 전 세계 평균보다 약간 낮은 비정상적인 연결률을 보이는데, 이는 주로 포스트 ACK 및 포스트 PSH 단계에서 닫히는 연결률이 낮기 때문입니다(이 단계는 미들 장비 [변조](https://blog.cloudflare.com/connection-tampering) 동작을 더 잘 반영합니다). 포스트 SYN의 높은 비율은 스캐닝으로 인해 대부분 네트워크에서 일반적이지만, 실제 클라이언트의 IP 주소를 스푸핑하는 패킷이 포함될 수 있습니다. 마찬가지로, 후기 연결 단계(초기 데이터 교환 후이지만 여전히 처음 10개 패킷 내)에서 높은 비율의 연결 재설정은 탭을 닫은 후 원치 않는 TCP 연결을 닫는 RST를 사용하는 브라우저와 같이 인간의 행동에 응답하는 애플리케이션일 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FTFP85N1QR5NH9WAPRTA.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/us?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

제 집의 ISP[AS22773(Cox Communications)](https://radar.cloudflare.com/as22773)에는 미국 전체와 비슷한 요금이 부과됩니다. 이는 미국에서 운영되는 대부분의 가정용 ISP에서 보편적입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49AMA9PHB1QR5D34EVKF39.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS22773?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

이를 [AS15169(Google LLC)](https://radar.cloudflare.com/as15169)와 비교해 보세요. 이는 Google의 [크롤러와 페처](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)의 대부분에서 유래합니다. 이 네트워크는 '나중의' 연결 단계에서 재설정 비율이 상당히 낮은데, 이는 인간 사용자 동작(예: 브라우저 탭 닫기)이 아닌 자동화된 트래픽의 비중이 더 크기 때문일 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW495FNQV343X710FCAEFTSX.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS15169?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

실제로 당사의 [봇 감지 시스템](https://radar.cloudflare.com/traffic)은 AS15169의 HTTP 요청 중 99% 이상을 자동화된 요청으로 분류합니다. 이것은 Radar에서 다양한 유형의 데이터를 대조하는 것이 가치가 있음을 보여줍니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49E8JSW82C0SBNAPXY2VX6.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/traffic/AS15169?dateStart=2024-07-28&dateEnd=2024-08-26#bot-vs-human) 를 통해_

Radar에 표시되는 새로운 비정상적인 연결 데이터세트는 대부분 수동적이고, 관찰 가능한 이벤트만 보고하며 원인은 보고하지 않습니다. 이러한 맥락에서 위의 Google 네트워크 그래프는 관찰 결과를 뒷받침하는 근거를 제시하며, 이는 다음에서 설명합니다.

## **신호에 대한 하나의 보기, 검증을 위한 더 많은 보기**

Cloudflare의 수동적 측정 접근 방식은 Cloudflare 규모에서 작동합니다. 하지만, 근본 원인이나 실측을 자체적으로 식별하지는 못합니다. 특정 단계에서, 특히 재설정 패킷 및 제한 시간 초과로 인한 연결의 경우 연결이 닫히는 이유에 대한 그럴듯한 설명이 많이 있습니다. 이 데이터 출처에만 의존하여 설명하려고 하면 추측으로 이어질 수 밖에 없습니다. 

그러나 이러한 제한은 활성 측정과 같은 다른 데이터 소스와 결합하면 극복할 수 있습니다. 예를 들어, [OONI](https://ooni.org/) 또는 [Censored Planet](https://censoredplanet.org/)의 보고서나 현장 보고서와 함께 확인하면 더 완전한 스토리가 제공될 수 있습니다. 따라서 TCP 재설정 및 시간 초과 데이터 세트의 주요 사용 사례 중 하나는 이전에 문서화된 현상의 규모와 영향을 이해하는 것입니다.

### **인터넷 규모의 측정 프로젝트 검증**

[AS398324](https://radar.cloudflare.com/as398324)를 보면, 절반 이상의 연결이 포스트 SYN 단계에서 비정상으로 나타나서 무언가 심각하게 잘못된 것이 있는 것 같습니다. 하지만 이 네트워크는 인터넷 스캐닝 회사 [Censys](https://censys.com/)의 CENSYS-ARIN-01로 밝혀졌습니다. 포스트 SYN 비정상은 네트워크 계층 스캐닝의 결과일 수 있습니다. 여기서 스캐너는 서버를 조사하기 위해 단일 SYN 패킷을 보내지만, TCP 핸드셰이크를 완료하지 않습니다. 또한, 거의 100%의 연결이 자동화로 분류되는 것으로 나타나 애플리케이션 계층 스캐닝을 나타낼 수 있는 이후(Later) 비정상의 비율도 높습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW454E412TEX10NE8ZM0ZMNH.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS398324?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts) 를 통해_

실제로 AS15169와 유사하게, Cloudflare에서는 AS398324의 요청 중 99% 이상을 자동화된 요청으로 분류합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48X1S84WNVWZ2SS95Q1E4K.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/traffic/AS398324?dateStart=2024-07-28&dateEnd=2024-08-26#bot-vs-human)_ _를 통해_

지금까지 스크립팅되거나 자동화된 트래픽을 대량으로 생성하는 네트워크에 대해 살펴보았습니다. 이제 더 깊이 살펴보겠습니다.

### **연결 변조 검증**

이 데이터 세트의 시작점은 [HTTPS 가로채기](https://blog.cloudflare.com/monsters-in-the-middleboxes)에 대한 작업과 비슷한 정신으로 활성 연결 변조를 이해하고 감지하는 연구 프로젝트였습니다. 우리가 이를 시작한 이유는 [동반된 블로그 게시물](https://blog.cloudflare.com/connection-tampering)에서 자세히 설명합니다.

[외부 환경에서 연결을 강제로 닫는 데 사용되는 ](https://go.gale.com/ps/anonymous?id=GALE%7CA175630128&it=r&linkaccess=abs&issn=10727825)잘 문서화된 기술은 [재설정 주입](https://www.ndss-symposium.org/wp-content/uploads/2017/09/weav.pdf)입니다. 재설정 주입을 사용하면 목적지로 가는 경로에 있는 미들 장비가 패킷의 데이터 부분을 검사합니다. 미들 장비가 금지된 도메인 이름으로 가는 패킷을 보면 위조된 TCP 재설정(RST) 패킷을 통신 당사자 중 하나 또는 둘 다에 주입하여 연결을 중단시킵니다. 미들 장비가 금지된 패킷을 먼저 삭제하지 않았다면 서버는 미들 장비 변조를 유발한 클라이언트 패킷(아마도 [서버 이름 표시(SNI)](https://www.cloudflare.com/en-gb/learning/ssl/what-is-sni/) 필드가 있는 TLS 클라이언트 Hello 메시지를 포함)과 곧이어 위조된 RST 패킷을 받게 됩니다.

TCP 재설정 및 제한 시간 초과 데이터세트에서 재설정 삽입을 통해 중단된 연결은 일반적으로 포스트 ACK, 포스트 PSH 또는 이후(Later) 이상으로 나타납니다(그러나 모든 이상이 재설정 주입으로 인한 것은 아님).

예를 들어, 재설정 주입 기술은 [알려져 있고](https://go.gale.com/ps/anonymous?id=GALE%7CA175630128&it=r&linkaccess=abs&issn=10727825) 일반적으로 중국의 만리방화벽(GFW)과 관련이 있습니다. 실제로 [중국](https://radar.cloudflare.com/cn)에 지리적으로 위치한 IP에서 시작된 연결의 포스트 PSH 이상 징후를 살펴보면 전 세계 평균보다 높은 비율을 확인할 수 있습니다. 그러나 중국의 개별 네트워크를 살펴보면 포스트 PSH 비율이 크게 다르며, 아마도 전송되는 트래픽 유형이나 기술의 구현 방식 때문일 수 있습니다. 반면, 포스트 SYN 이상 징후 비율은 대부분의 주요 중국 AS에서 일관되게 높습니다. 이는 스캐너, 스푸핑된 SYN 폭주 공격 또는 [잔차(residual)](https://www.usenix.org/conference/usenixsecurity23/presentation/wu-mingshi) [차단](https://gfw.report/publications/usenixsecurity23/en/)일 수 있으며, 이는 [_부수적 영향_](https://blog.cloudflare.com/ko-kr/consequences-of-ip-blocking)을 초래할 수 있습니다. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49730V4M2PPXSP0EYNK96R.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/cn?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

[AS4134(CHANANET-ACKBONE)](https://radar.cloudflare.com/as4134)는 다른 중국 AS보다 낮은 포스트 PSH 이상 징후의 비율을 보여 주지만, 여전히 전 세계 평균보다 훨씬 높습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-11](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46P53Z8K61Z4ZGWZNEGWVA.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS4134?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

네트워크 [AS9808(CHNAMOBILE-CN)](https://radar.cloudflare.com/as9808)과 [AS56046(CMNET-Jiangsu-AP)](https://radar.cloudflare.com/as56046)에서는 모두 포스트 PSH 이상 징후와 일치하는 연결의 비율이 두 자릿수를 나타냅니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-12](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45GQC61V9XX64FNPMXWEMZ.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS9808?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-13](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45F5HKG96EF4RWBKSG5QW4.png&w=715&h=402&f=webp&fit=cover&position=center)

 _[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS56046?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

연결 변조에 대한 자세한 내용은 [심층 블로그 게시물](https://blog.cloudflare.com/connection-tampering)을 참조하세요.

## **후속 연구를 위한 새로운 인사이트 및 목표 파악하기**

TCP 재설정 및 제한 시간 초과 데이터세트는 '눈에 띄고' 추가 조사가 필요한 네트워크를 찾는 데 도움이 되므로 새롭거나 이전에 제대로 연구되지 않은 네트워크 동작을 식별하는 데 도움이 될 수도 있습니다.

### **귀속 불가능한 ZMap 스캐닝**

여기에 설명할 수 없는 문제가 있습니다. 매일 동일한 18시간 간격 동안 영국 클라이언트의 연결 중 10% 이상이 초기 SYN 패킷을 넘어 진행되지 않고 시간 초과로 끝납니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-14](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW470YR5X0B25MKBQB5B8JDN.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/gb?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

내부 검사 결과, 거의 모든 포스트 이상 징후는 [AS396982(GOOGLE-CLOUD-PLATFORM)](https://radar.cloudflare.com/as396982)에서 [ZMap](https://zmap.io/)을 사용하는 스캐너에서 비롯된 것으로 나타났으며, 이는 모든 IP 주소 범위에 걸친 전체 포트 스캔인 것으로 보입니다. (ZMap 클라이언트는 나중에 논의할 ZMap의 책임 있는 자체 식별을 기반으로 책임 있게 자체 식별합니다.) 저희는 지리적으로 미국에 위치한 AS396982의 IP 접두사에서 유사한 수준의 스캔 트래픽을 확인합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-15](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KBSPA7F7F18Q1AB9BA2P.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS396982?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

### **모바일 네트워크에서의 제로 레이팅**

국가 수준에서 이상 징후 비율을 잠깐 살펴보면 몇 가지 흥미로운 결과가 드러납니다. 예를 들어, [멕시코](https://radar.cloudflare.com/mx)의 연결을 살펴보면 연결 변조와 관련된 포스트 ACK 및 포스트 PSH 이상 징후 비율이 글로벌 평균보다 높습니다. 멕시코 연결의 프로필도 이 지역의 다른 프로필과 비슷합니다. 그러나 멕시코는 “[정부나 다른 행위자가 인터넷 콘텐츠를 차단하거나 필터링한다는 문서화된 증거가 없습니다.](https://freedomhouse.org/country/mexico/freedom-net/2023)”

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-16](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JFJXK571V3YA12NDZ0K7.png&w=715&h=402&f=webp&fit=cover&position=center)

 _[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/mx?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

멕시코에서 HTTP 트래픽 볼륨에 따른 상위 AS를 살펴보면, [AS28403(RadioMovil Dipsa, S.A. de C.V., Telcel로 운영)](https://radar.cloudflare.com/as28403)에서 온 연결의 약 50%가 TCP 핸드셰이크(포스트 ACK 연결 단계)가 완료된 직후 재설정 또는 제한 시간 초과를 통해 종료됩니다. 이 단계에서는 미들 장비에서 Cloudflare에 도달하기 전에 데이터 패킷을 보고 삭제했을 가능성이 있습니다.

이러한 동작에 대한 한 가지 설명은 [제로 등급](https://en.wikipedia.org/wiki/Zero-rating)일 수 있습니다. 셀룰러 네트워크 제공자가 특정 리소스(예: 메시징 또는 소셜 미디어 앱)에 대한 액세스를 무료로 허용하는 것입니다. 사용자가 계정의 데이터 전송 한도를 초과하면 제공자는 다른 리소스에 대한 연결을 차단하는 동안에도 제로 등급 대상에 대한 트래픽을 허용할 수 있습니다.

제로 등급 정책을 시행하기 위해 ISP에서는 [TLS 서버 이름 표시(SNI)](https://www.cloudflare.com/en-gb/learning/ssl/what-is-sni/)를 사용하여 연결을 차단할지 허용할지 결정할 수 있습니다. SNI는 TCP 핸드셰이크 직후에 데이터가 포함된 패킷으로 전송됩니다. 따라서 ISP에서 SNI가 포함된 패킷을 삭제해도 서버에는 여전히 클라이언트의 SYN 및 ACK 패킷이 표시되지만, 후속 패킷은 표시되지 않으며 이는 포스트 ACK 연결 이상과 일치합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-17](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48RXXVA7FGYBQDQNT95W7X.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS28403?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

데이터 세트에서 유사한 프로필을 가진 또 다른 국가인 [페루](https://radar.cloudflare.com/pe)를 살펴보면, 멕시코에 비해 포스트 ACK 및 포스트 PSH 이상 징후 비율이 더 높습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-18](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44XAPAT3MHKFBKXAZYVE6Q.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/pe?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

특정 AS에 초점을 맞추면, [AS12252(Claro Peru)](https://radar.cloudflare.com/as12252)는 멕시코의 AS28403과 유사한 높은 비율의 Post-ACK 이상 징후를 보입니다. 두 네트워크는 같은 모회사인 [América Móvil](https://www.americamovil.com/English/overview/default.aspx)에서 운영하므로 유사한 네트워크 정책과 네트워크 관리 기술이 사용될 것으로 예상할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-19](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PXYS28W740SNP0SVACTR.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/AS12252?dateStart=2024-07-28&dateEnd=2024-08-26#tcp-resets-and-timeouts)_ _를 통해_

흥미롭게도 [AS6147(Telefónica Del Perú)](https://radar.cloudflare.com/as6147)에서는 PSH 이후 연결 이상 징후에서 높은 비율을 보였습니다. 이는 이 네트워크가 네트워크 계층에서 다른 기술을 사용하여 정책을 시행함을 의미할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-20](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FGDYC7PKDTFQ0NBA3E77.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/dz?dateStart=2024-06-06&dateEnd=2024-06-19#tcp-resets-and-attacks)_ _를 통해_

## **시간에 따른 변화, 종단적 관점**

Cloudflare의 지속적 수동적 측정의 가장 강력한 측면 중 하나는 더 긴 기간에 걸쳐 네트워크를 측정할 수 있는 기능입니다.

### **인터넷 셧다운**

2024년 6월 블로그 게시물 '[시리아, 이라크, 알제리의 인터넷 셧다운 조사](https://blog.cloudflare.com/syria-iraq-algeria-exam-internet-shutdown)'에서 Cloudflare에서는 시험과 관련된 전국적인 인터넷 셧다운을 Cloudflare 네트워크의 관점에서 공유했습니다. 그 당시 TCP 재설정 및 제한 시간 초과 데이터 세트를 준비하고 있었으므로 외부 보고서를 확인하고 셧다운에 사용된 특정 기술에 대한 인사이트를 얻는 데 도움이 되었습니다.

행동이 변화하는 사례로 '시간을 되돌려' 시험 관련 차단이 발생한 모습을 관찰할 수 있습니다. [시리아](https://radar.cloudflare.com/sy)의 경우, 시험으로 인한 셧다운 기간 동안 SYN 이후의 이상 징후 비율이 급증하는 것을 볼 수 있습니다. 실제로 이 기간에는 트래픽(SYN 패킷 포함)이 [거의 완전히 감소](https://radar.cloudflare.com/traffic/sy?dateStart=2024-05-20&dateEnd=2024-06-19)했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-21](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45Y7W4YDCBVDE364FQK8XZ.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/sy?dateStart=2024-05-20&dateEnd=2024-06-19#tcp-resets-and-timeouts)_ _를 통해_

  
7월 마지막 주에 시작되는 두 [번째](https://x.com/CloudflareRadar/status/1816438072768078078) 셧다운도 상당히 눈에 띕니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-21](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463MDS7KG8T04VHR716TTD.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/sy?dateStart=2024-07-20&dateEnd=2024-08-19#tcp-resets-and-timeouts)_ _를 통해_

[이라크](https://radar.cloudflare.com/iq)에서의 연결을 살펴보면, Cloudflare의 시험 관련 셧다운에 대한 견해는 시리아의 경우와 유사해 보이며, SYN 이후 급증이 여러 번 발생했지만, 훨씬 덜 두드러졌습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-23](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4578CQXW66V0AFRGRAZ4XG.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/iq?dateStart=2024-05-17&dateEnd=2024-06-10#tcp-resets-and-timeouts)_ _를 통해_

[시험 셧다운 블로그](https://blog.cloudflare.com/syria-iraq-algeria-exam-internet-shutdown)에서는 또한 [알제리](https://radar.cloudflare.com/dz)에서 시험 기간에 콘텐츠에 대한 액세스를 제한하기 위해 보다 미묘한 접근 방식을 취한 방법을 설명합니다. 증거에 따르면 알제리에서는 인터넷을 완전히 중단하는 대신 특정 연결을 대상으로 했습니다. 실제로 시험 기간에 포스트 ACK 연결 이상이 증가합니다. 이러한 동작은 미들 장비가 금지된 콘텐츠가 포함된 패킷을 선택적으로 삭제하고 다른 패킷(예: 초기 SYN 및 ACK)은 그대로 두는 경우 예상할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![1622-24](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47XSQF8ZNS4HV9G3RH6WFW.png&w=715&h=402&f=webp&fit=cover&position=center)

_[Cloudflare Radar](https://radar.cloudflare.com/security-and-attacks/dz?dateStart=2024-06-06&dateEnd=2024-06-19#tcp-resets-and-attacks)_ _를 통해_

위의 예는 이 데이터가 다른 신호와 상관관계가 있을 때 가장 유용하다는 것을 강조합니다. 이 데이터는 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary)를 통해서도 사용할 수 있으므로 다른 사람들이 더 깊이 알아볼 수 있습니다. 다음에 설명하는 것처럼 당사의 탐지 기술은 다른 서버와 운영자에게도 이전할 수 있습니다.

## How to detect anomalous TCP connections at scale

이 섹션에서는 TCP 재설정 및 제한 시간 초과 데이터세트를 구성한 방법을 설명합니다. Cloudflare 전역 네트워크의 규모는 데이터 처리 및 분석에 있어 독특한 과제를 안겨 줍니다. Cloudflare에서는 독자가 Cloudflare의 방법론을 이해하고, 데이터세트를 해석하며, 다른 네트워크나 서버에 메커니즘을 복제하는 데 도움이 되는 Cloudflare의 기술을 공유합니다.

Cloudflare의 방법론은 다음과 같이 요약할 수 있습니다.

  * Cloudflare의 클라이언트 대면 서버에 도착하는 연결 샘플을 기록합니다. 이 샘플링 시스템은 완전히 수동적이므로 트래픽을 해독하는 기능이 없으며 네트워크를 통해 전송된 기존 패킷에만 액세스할 수 있습니다.
  * 캡처한 패킷에서 연결을 재구성합니다. Cloudflare 설계의 새로운 측면은 클라이언트에서 서버로 한 방향만 관찰하면 된다는 것입니다.
  * 재설정 또는 제한 시간 초과로 인해 종료된 비정상적인 연결에 대해 복원된 연결을 시그니처 세트와 비교합니다. 이 서명은 _연결 단계_ 와 조사 및 Cloudflare 자체의 관찰에 따른 특정 행동을 나타내는 _태그_ 의 두 부분으로 구성됩니다.



이러한 설계 옵션을 통해 암호화된 패킷을 안전하게 유지하고 대상 서버에 액세스하지 않고도 어디에서나 복제할 수 있습니다.

## First, sample connections

Our main goal was to design a mechanism that scales, and gives us broad visibility into all connections arriving at Cloudflare’s network. Running traffic captures on each client-facing server works, but does not scale. We would also need to know exactly where and when to look, making continuous insights hard to capture. Instead, we sample connections from all of Cloudflare’s servers and log them to a central location where we could perform offline analysis.

## **첫째, 샘플 연결**

저희 주요 목표는 Cloudflare의 네트워크에 도달하는 모든 연결을 확장할 수 있고 폭넓은 가시성을 제공하는 메커니즘을 설계하는 것이었습니다. 클라이언트 대면 서버마다 트래픽 캡처를 실행하면 되지만, 확장되지는 않습니다. 또한 언제 어디에서 살펴봐야 하는지 정확히 알아야 하므로 지속적인 인사이트를 포착하기가 어려웠습니다. 그 대신, Cloudflare의 모든 서버에서 연결을 샘플링하여 오프라인 분석을 수행할 수 있는 중앙 위치에 기록합니다.

여기서 우리는 첫 번째 난관에 봉착했습니다. Cloudflare의 분석 시스템에서 사용하는 기존 패킷 로깅 파이프라인은 개별 패킷을 로깅하지만 연결은 여러 패킷으로 구성됩니다. 연결 이상을 감지하려면 주어진 연결에서 모든 패킷 또는 적어도 충분한 패킷을 확인해야 했습니다. 다행히도 Cloudflare의 DoS 팀에서 구축한 유연한 로깅 시스템을 활용하여 [DDoS 공격에 관련된 패킷을 분석](https://developers.cloudflare.com/ddos-protection/about/how-ddos-protection-works/)할 수 있었고, 두 개의 [`iptables`](https://manpages.debian.org/bookworm/iptables/iptables.8.en.html) 규칙을 신중하게 호출하여 목표를 달성할 수 있었습니다.

첫 번째 `iptables` 규칙은 샘플링을 위해 새 연결을 무작위로 선택하여 표시합니다. 저희 경우, 10,000개의 유입 TCP 연결당 하나를 샘플링하기로 했습니다. 이 숫자에는 마법 같은 것은 없지만, Cloudflare의 규모에서는 데이터 처리 및 분석 파이프라인에 부담을 주지 않으면서 충분히 캡처하는 균형을 이룹니다. `iptables` 규칙은 DDoS 완화 시스템을 통과한 패킷에만 적용됩니다. TCP 연결은 오래 지속될 수 있으므로 새 TCP 연결만 샘플링합니다. 샘플링할 연결을 표시하기 위한 `iptables` 규칙은 다음과 같습니다.
    
    
    -t mangle -A PREROUTING -p tcp --syn -m state 
    --state NEW -m statistic --mode random 
    --probability 0.0001 -m connlabel --label <label> 
    --set -m comment --comment "Label a sample of ingress TCP connections"
    

이를 세분화하면, 규칙은 들어오는 패킷을 처리하는 체인의 `mangle`테이블(패킷 수정용)에 설치됩니다(`-A PREROUTING`). SYN 플래그가 설정된 TCP 패킷만 고려됩니다(`-p tcp --syn`). 여기에는 연결에 대한 이전 상태가 없습니다(`--state NEW`). 필터는 10,000개의 SYN 패킷마다 하나를 선택하고(`-m statistic –mode random --probability 0.0001`) 연결에 레이블을 적용합니다(`-m connlabel --label --set`).

두 번째 iptables 규칙은 연결의 후속 패킷을 최대 10패킷까지 기록합니다. 다시 말하지만, 숫자 10이 일반적으로 연결 설정, 후속 요청 패킷, 예상 전에 종료되는 연결의 재설정을 캡처하기에 충분하다는 것 외에는 마법 같은 것은 없습니다.
    
    
    -t mangle -A PREROUTING -m connlabel --label 
    <label> -m connbytes ! --connbytes 11 
    --connbytes-dir original --connbytes-mode packets 
    -j NFLOG --nflog-prefix "<logging flags>" -m 
    comment --comment "Log the first 10 incoming packets of each sampled ingress connection"
    

이 규칙은 이전 규칙과 동일한 체인에 설치됩니다. 샘플링된 연결의 패킷만 일치합니다(`-m connlabel --label` )). 그리고 각 연결의 처음 10개 패킷만 일치합니다(`-m connbytes ! --connbytes 11 --connbytes-dir original --connbytes-mode packets`). 일치하는 패킷은 NFLOG로 전송됩니다(`-j NFLOG --nflog-prefix """`). 여기서 로깅 시스템에서 수집하여 오프라인 분석을 위해 중앙 위치에 저장합니다.

## **샘플링된 패킷으로부터 연결 재구성**

서버에 기록된 패킷은 분석 파이프라인의 일부로 [ClickHouse](https://blog.cloudflare.com/tag/clickhouse/) 테이블에 삽입됩니다. 기록된 각 패킷은 데이터베이스의 개별 행에 저장됩니다. 그 다음 과제는 추가 분석을 위해 패킷을 해당 연결로 다시 조립하는 것입니다. 더 진행하기 전에 이 분석의 목적을 위해 '연결'이 무엇인지 정의해야 합니다.

다음과 같은 조정을 통해 네트워크 5-투플인 `프로토콜, 소스 IP 주소, 소스 포트, 대상 IP 주소`, `대상 포트`에 의해 정의된 연결의 표준 정의를 사용합니다.

  * 저희는 연결의 _수신_(클라이언트-서버) 절반에서만 패킷을 샘플링하므로 서버에서 클라이언트로의 해당 응답 패킷을 볼 수 없습니다. 대부분의 경우, 서버가 어떻게 구성되어 있는지에 대한 지식을 바탕으로 서버 응답이 무엇인지 유추할 수 있습니다. 궁극적으로 수신 패킷은 비정상적인 TCP 연결 동작을 학습하기에 충분합니다.
  * ClickHouse 데이터세트를 15분 간격으로 쿼리하고 해당 간격 내에서 동일한 네트워크 5-투플을 공유하는 패킷을 그룹화합니다. 즉, 쿼리 간격이 끝나갈수록 연결이 잘릴 수 있습니다. 연결 제한 시간 초과를 분석할 때, 최신 패킷 타임스탬프가 쿼리 종료 후 10초 이내에 발생한 불완전한 흐름은 제외했습니다.
  * 재설정 및 제한 시간 초과는 _새_ 연결에 영향을 미칠 가능성이 가장 높으므로 새로운 TCP 핸드셰이크의 시작을 표시하는 SYN 패킷으로 시작하는 패킷 시퀀스만 고려합니다. 따라서 기존의 수명이 긴 연결은 제외됩니다.
  * 로깅 시스템은 정확한 패킷 도착 간 타임스탬프를 보장하지 않으므로 도착 시간을 기준으로 정렬하지 않고 도착하는 패킷 집합만 고려합니다. 경우에 따라 TCP 시퀀스 번호에 따라 패킷 순서를 결정할 수 있지만, 그렇게 해도 결과에 큰 영향이 없는 것으로 밝혀졌습니다.
  * 분석 시 노이즈를 줄이기 위해 여러 SYN 패킷이 포함된 연결의 일부를 필터링했습니다.



위의 연결 정의 방법 조건을 확인했으므로 이제 분석 파이프라인을 더 자세히 설명할 수 있습니다.

## **단계에 연결 종료 이벤트 매핑**

TCP 연결은 연결 설정에서 최종 연결 종료까지의 일련의 단계를 통해 전환됩니다. 비정상적인 연결이 닫히는 단계는 이상이 발생한 _이유_ 에 대한 단서를 제공합니다. Cloudflare에서는 서버에서 수신하는 패킷에 따라 각 연결을 네 가지 단계(포스트 SYN, 포스트 ACK, 포스트 PSH, 이후(Later)) 중 하나로 분류하며, 이는 [앞서](https://blog.cloudflare.com/tcp-resets-timeouts/#dataset) 자세히 설명했습니다.

연결 종료 단계만으로도 다양한 네트워크의 비정상적인 TCP 연결에 대한 유용한 인사이트가 제공되며, 현재 Cloudflare Radar에서 이러한 정보를 확인할 수 있습니다. 하지만 경우에 따라 더 특정한 시그니처와 연결을 매칭하면 더 심층적인 인사이트가 제공될 수 있습니다.

## **보다 구체적인 연결 동작을 설명하는 태그 적용**

위에서 설명한 대로 연결을 단계로 그룹화하는 것은 해당 연결에 있는 패킷의 TCP 플래그만을 기준으로 해서 이루어집니다. 패킷 간 도착 타이밍, TCP 플래그의 정확한 조합, 기타 패킷 필드(IP 식별, IP TTL, TCP 시퀀스 및 승인 번호, TCP 윈도우 크기 등)와 같은 다른 요소를 고려하면 특정 동작에 대해 보다 세밀하게 매칭할 수 있습니다.

예를 들어, 인기 있는 [ZMap](http://zmap.io/) 스캐너 소프트웨어는 생성하는 SYN 패킷에서 IP 식별 필드를 54321로, TCP 창 크기를 65535로 수정합니다([소스 코드](https://github.com/zmap/zmap/blob/c88db2917612328c843561101495e5263ef7ac5b/src/probe_modules/packet.c)). 이러한 정확한 필드가 설정된 패킷이 네트워크에 도착하는 것이 관찰되면, 패킷이 ZMap을 사용하는 스캐너에서 생성되었을 가능성이 큽니다.

태그는 변조 미들 장비의 알려진 시그니처에 대한 연결을 일치시키는 데에도 사용할 수 있습니다. 많은 활성 측정 작업(예: [Weaver, Sommer, Paxson](https://www.ndss-symposium.org/wp-content/uploads/2017/09/weav.pdf))에서 일부 미들 장비 배포가 클라이언트가 보낸 다른 패킷과 다른 IP TTL 필드를 설정하거나 RST 패킷과 RST+ACK 패킷을 모두 보내는 것과 같이 재설정 주입을 통해 연결을 중단할 때 일관된 동작을 보인다는 것이 발견되었습니다. 특정 연결 변조 시그니처에 대한 자세한 내용은 [블로그 게시물](https://blog.cloudflare.com/connection-tampering)과 [상호 검토 논문](https://research.cloudflare.com/publications/SundaraRaman2023/)을 참조하세요.

현재 저희는 다음 태그를 정의하고 있으며, 시간이 지남에 따라 이를 개선하고 확장할 예정입니다. 일부 태그는 아래 계층적 표현에서 알 수 있듯이 다른 태그도 설정된 경우에만 적용됩니다(예: `fin` 태그는 재설정 태그도 설정된 경우에만 적용할 수 있음).

  * `제한 시간 초과`: 제한 시간 초과로 종료됨
  * `재설정`: 재설정으로 인해 종료됨(RST 플래그가 설정된 패킷)
    * fin: 하나 이상의 RST 패킷과 함께 하나 이상의 FIN 패킷이 수신되었음
    * `single_rst`: 하나의 RST 패킷으로 종료됨
    * `multiple_rsts`: 다수의 RST 패킷으로 종료됨
      * `acknumsame`: RST 패킷의 승인 번호가 모두 동일하고 0이 아니었음
      * `acknumsame0`: RST 패킷의 승인 번호가 모두 0이었음
      * `acknumdif`f: RST 패킷의 승인 번호가 다르고 모두 0이 아니었음
      * `acknumdiff0`: RST 패킷의 승인 번호가 다르고 하나가 0이었음
    * `single_rstack`: 하나의 RST+ACK 패킷으로 종료됨(RST와 ACK 플래그 모두 설정됨)
    * `multiple_rstacks`: 다수의 RST+ACK 패킷으로 종료됨
    * `rst_and_rstacks`: RST와 RST+ACK 패킷의 조합으로 종료됨
  * `zmap`: SYN 패킷이 ZMap 스캐너로 생성된 패킷과 일치함



연결 태그는 현재 Radar [대시보드](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)와 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary)에 표시되지 않지만, 향후 이 추가 기능을 출시할 계획입니다.

## **다음은?**

Cloudflare의 사명은 더 나은 인터넷을 구축하는 것이며, 저희는 투명성과 책임성이 그 사명의 중요한 부분이라고 생각합니다. 저희가 공유하는 인사이트와 도구가 전 세계의 비정상적인 네트워크 동작을 밝히는 데 도움이 되기를 바랍니다.

현재의 TCP 재설정 및 제한 시간 초과 데이터 세트는 네트워크 운영자, 연구원, 인터넷 시민 모두에게 즉시 유용하지만, 저희 여기서 멈추지 않을 계획입니다. 향후 추가하려는 개선 사항이 몇 가지 있습니다.

  * 특정 네트워크 동작을 포착하기 위한 태그 세트를 확장하고 이 세트를 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary) 및 [대시보드](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)에 노출.
  * Cloudflare에서 고객 원본 서버로 연결하여 인사이트를 확장.
  * 현재 전 세계 Cloudflare에 대한 HTTP 요청의 [30% 이상](https://radar.cloudflare.com/adoption-and-usage)에 사용되는 QUIC에 대한 지원을 추가.



이 블로그가 흥미로웠다면, 첨부된 [블로그 게시물](https://blog.cloudflare.com/connection-tampering)과 [논문](https://research.cloudflare.com/publications/SundaraRaman2023/)을 읽으면서 연결 변조에 대해 자세히 알아보고, Cloudflare Radar에서 TCP 재설정 및 제한 시간 초과 [대시보드](https://radar.cloudflare.com/security-and-attacks#tcp-resets-and-timeouts)와 [API](https://developers.cloudflare.com/api/operations/radar-get-tcp-resets-timeouts-summary)를 살펴보세요. 질문이나 의견은 radar@cloudflare.com으로 보내주시기 바랍니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftcp-resets-timeouts%2F&t=Cloudflare%20Radar%EC%9D%98%20TCP%20%EC%9E%AC%EC%84%A4%EC%A0%95%20%EB%B0%8F%20%EC%A0%9C%ED%95%9C%20%EC%8B%9C%EA%B0%84%20%EC%B4%88%EA%B3%BC%EC%97%90%20%EB%8C%80%ED%95%9C%20%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8)[](https://x.com/intent/post?text=Cloudflare+Radar%EC%9D%98+TCP+%EC%9E%AC%EC%84%A4%EC%A0%95+%EB%B0%8F+%EC%A0%9C%ED%95%9C+%EC%8B%9C%EA%B0%84+%EC%B4%88%EA%B3%BC%EC%97%90+%EB%8C%80%ED%95%9C+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftcp-resets-timeouts%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftcp-resets-timeouts%2F)[](https://bsky.app/intent/compose?text=Cloudflare+Radar%EC%9D%98+TCP+%EC%9E%AC%EC%84%A4%EC%A0%95+%EB%B0%8F+%EC%A0%9C%ED%95%9C+%EC%8B%9C%EA%B0%84+%EC%B4%88%EA%B3%BC%EC%97%90+%EB%8C%80%ED%95%9C+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftcp-resets-timeouts%2F)[](https://mastodonshare.com/?text=Cloudflare+Radar%EC%9D%98+TCP+%EC%9E%AC%EC%84%A4%EC%A0%95+%EB%B0%8F+%EC%A0%9C%ED%95%9C+%EC%8B%9C%EA%B0%84+%EC%B4%88%EA%B3%BC%EC%97%90+%EB%8C%80%ED%95%9C+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftcp-resets-timeouts%2F)[](https://www.threads.net/intent/post?text=Cloudflare+Radar%EC%9D%98+TCP+%EC%9E%AC%EC%84%A4%EC%A0%95+%EB%B0%8F+%EC%A0%9C%ED%95%9C+%EC%8B%9C%EA%B0%84+%EC%B4%88%EA%B3%BC%EC%97%90+%EB%8C%80%ED%95%9C+%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ftcp-resets-timeouts%2F)

## 관련 태그

[Radar](https://blog.cloudflare.com/ko-kr/tag/cloudflare-radar/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인터넷 트래픽](https://blog.cloudflare.com/ko-kr/tag/internet-traffic/)[인터넷 품질](https://blog.cloudflare.com/ko-kr/tag/internet-quality/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Luke Valenta](https://blog.cloudflare.com/ko-kr/author/luke/)

[](https://lukevalenta.com/)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
