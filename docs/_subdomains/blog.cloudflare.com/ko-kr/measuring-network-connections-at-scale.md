---
url: https://blog.cloudflare.com/ko-kr/measuring-network-connections-at-scale/
title: \uc778\ud130\ub137 \uaddc\ubaa8\uc5d0\uc11c TCP \uc5f0\uacb0\uc758 \ud2b9\uc131 \uce21\uc815 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:53.318180+00:00
---

# 인터넷 규모에서 TCP 연결의 특성 측정 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/measuring-network-connections-at-scale/

[블로그](https://blog.cloudflare.com/ko-kr/)

[TCP](https://blog.cloudflare.com/ko-kr/tag/tcp/)[더 나은 인터넷](https://blog.cloudflare.com/ko-kr/tag/better-internet/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)+11개의 태그 더 보기

4개 태그4개 태그 보기

  * 게시물 태그
  * [TCP](https://blog.cloudflare.com/ko-kr/tag/tcp/)[더 나은 인터넷](https://blog.cloudflare.com/ko-kr/tag/better-internet/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인사이트](https://blog.cloudflare.com/ko-kr/tag/insights/)
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



[인사이트](https://blog.cloudflare.com/ko-kr/tag/insights/)

[TCP](https://blog.cloudflare.com/ko-kr/tag/tcp/)[더 나은 인터넷](https://blog.cloudflare.com/ko-kr/tag/better-internet/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인사이트](https://blog.cloudflare.com/ko-kr/tag/insights/)

2025년 10월 29일

# 인터넷 규모에서 TCP 연결의 특성 측정

![Suleman Ahmad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44MCC5WJ427B6XCV7Z59EV.png&w=64&h=64&f=webp&fit=cover&position=center)![Peter Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4945P7JZ17N06Z9Q2E2GNT.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Suleman Ahmad](https://blog.cloudflare.com/ko-kr/author/suleman/) 및 [Peter Wu](https://blog.cloudflare.com/ko-kr/author/peter-wu/)

17분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/measuring-network-connections-at-scale/) 및 [日本語](https://blog.cloudflare.com/ja-jp/measuring-network-connections-at-scale/).

![BLOG-3048 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46M20ECBMKJ9B8MPGVMY7P.png&w=1201&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////f3+7e704OPu3uTy5Or26e306+rt//////3+6+zz2t/u19/x3+b26Ovz7evs///////+6uz01d3v0dzz3eX36ez08O3s////////7vD42OHz1eH34en67vD39fHv////////9fj94uv64ez97PT/9/j9+/f0////////////8fn/8vv/+/////////77/////////////P//////////////////////////////////////////////////)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

웹 페이지 로드, 동영상 스트리밍, API 호출 등 인터넷에서의 모든 상호 작용은 연결로 시작됩니다. 이러한 기본적인 논리적 연결은 장치 간에 오가는 패킷 스트림으로 구성됩니다.

인터넷이 존재하는 이래로 네트워크 연결의 다양한 측면은 연구자와 실무자의 관심을 불러왔습니다. 심지어 연결에 대한 관심은 1991년의 획기적인 논문[ _"광역 TCP/IP 대화의 특성"에서 볼 수 있듯이 그_](https://dl.acm.org/doi/10.1145/115994.116003) 이전부터 등장했습니다. 어쨌든 인터넷 측정 커뮤니티는 _수십 년 동안_ 인터넷 통신의 특성을 파악하는 데 전념해 왔으며, "얼마나 오래 지속됩니까?"부터 "얼마나 큰가요?" "얼마나 자주?" 그리고 이는 이제 시작일 뿐입니다.

놀랍게도 광범위한 인터넷에서의 연결 특성을 대부분 사용할 수 없는 경우가 많습니다. 누구나 도구(예: [_Wireshark_](https://www.wireshark.org/))를 사용하여 로컬에서 데이터를 캡처할 수 있지만, 액세스 및 규모로 인해 연결을 전 세계적으로 측정하는 것은 사실상 불가능합니다. 또한 네트워크 운영자는 일반적으로 자신이 관찰하는 특성을 공유하지 않습니다. 네트워크 운영자는 이러한 특성을 관찰하는 데 상당한 시간과 노력을 들인다고 가정합니다.

이 블로그 게시물에서는 다른 방향으로 이동하여 Cloudflare의 글로벌 CDN을 통해 설정된 연결에 대한 집계 인사이트를 공유합니다. [_Cloudflare에 대한 HTTP 요청의_](https://radar.cloudflare.com/adoption-and-usage) 약 70%를 차지하는 [_TCP_](https://developers.cloudflare.com/fundamentals/reference/tcp-connections/) 연결의 특성을 제시하며, 클라이언트 측 측정만으로는 얻기 어려운 경험적 인사이트를 제공합니다.

## 연결 특성이 중요한 이유

시스템 동작을 특성화하면 변경의 영향을 예측하는 데 도움이 됩니다. 네트워크 측면에서는 새로운 라우팅 알고리즘 또는 전송 프로토콜을 고려해보세요. 그 효과를 어떻게 측정할 수 있을까요? 한 가지 옵션은 변경 사항을 라이브 네트워크에 직접 배포하는 것이지만, 이는 위험합니다. 예상치 못한 결과가 발생하면 사용자나 네트워크의 다른 부분에 지장을 초래할 수 있어 '배포 우선' 접근 방식이 안전하지 않거나 윤리적으로 의심스러울 수 있습니다.

첫 번째 단계로 라이브 배포보다 안전한 대안은 시뮬레이션입니다. 설계자는 시뮬레이션을 사용하여 전체 버전을 구축하지 않고도 스키마에 대한 중요한 인사이트를 얻을 수 있습니다. 그러나 인터넷 전체를 시뮬레이션하는 것은 어려운 일입니다.[_매우 유명한 저서인 " 인터넷을 어떻게 시뮬레이션해야 할지 모르는 이유 "에서 설명한 것처럼요._](https://dl.acm.org/doi/10.1145/268437.268737)

유용한 시뮬레이션을 실행하려면 우리가 연구 중인 실제 시스템처럼 작동해야 합니다. 이는 실제 행동을 모방한 가상 데이터를 생성하는 것을 의미합니다. 이는 실제 데이터가 어떻게 작동하는지에 대한 수학적 설명인 통계 분포를 사용하는 경우가 많습니다. 그러나 이러한 분포를 만들려면 먼저 데이터를 특성화하여 주요 속성을 측정하고 이해해야 합니다. 그래야만 시뮬레이션을 통해 사실적인 결과를 얻을 수 있습니다.

## 데이터세트 풀기

모든 데이터의 가치는 수집 메커니즘에 따라 달라집니다. 모든 데이터 세트에는 사각 지대, 편향성, 한계가 있으며, 이를 무시하면 잘못된 결론에 도달할 수 있습니다. 데이터가 어떻게 수집되었는지, 데이터가 표현하는 내용, 제외되는 내용 등 더 자세한 정보를 조사함으로써 우리는 데이터의 신뢰성을 더 잘 이해하고 데이터 사용 방법에 대해 정보에 입각한 결정을 내릴 수 있습니다. 수집된 원격 측정 결과를 자세히 살펴보겠습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47P235Z3EX28MAQXDF4W28.png&w=715&h=138&f=webp&fit=cover&position=center)

**데이터세트** 개요. 이 데이터는 위 다이어그램에서 _Cloudflare 방문자_ 로 표시된 TCP 연결을 설명하며, 이 연결은 HTTP 1.0, 1.1, 2.0을 통해 글로벌 CDN 서버에서 수신되는 초당 평균 8,400만 건의 HTTP 요청 중 [약 70%](https://radar.cloudflare.com/adoption-and-usage) 를 처리합니다.

**샘플링.** 수동적으로 수집된 데이터의 스냅샷은 2025년 10월 7일부터 10월 15일 사이에 Cloudflare에 대한 균일하게 샘플링된 모든 TCP 연결 1%에서 가져온 것입니다. 클라이언트 대면 서버 각각에서 샘플링을 수행하여 데이터 센터 수준에서 샘플링하여 나타날 수 있는 편향성을 완화합니다.

**다양성.** 주로 트래픽을 자체 소유하고 검색, 소셜 미디어 또는 스트리밍 비디오와 같은 소수의 서비스에 의해 지배되는 많은 대형 사업자와는 달리, Cloudflare의 워크로드의 대다수는 고객으로부터 발생합니다. 고객은 웹 사이트 앞에 Cloudflare를 두어 보호를 제공하고, 성능을 개선하고, 비용을 절감하도록 지원합니다. 이러한 고객의 다양성으로 인해 전 세계에 걸쳐 수많은 웹 애플리케이션, 서비스, 사용자가 찾아옵니다. 그 결과로 우리가 관찰하는 연결은 끊임없이 진화하는 광범위한 클라이언트 장치와 애플리케이션별 동작에 의해 형성됩니다.

**Cloudflare가 기록합니다.** 로그의 각 항목은 SNI 및 연결 중 요청 수와 함께 Linux 커널의 [_TCP_INFO_](https://man7.org/linux/man-pages/man7/tcp.7.html) 구조를 통해 캡처된 소켓 레벨 메타데이터로 구성됩니다. 로그에서 개별 HTTP 요청, 트랜잭션, 세부 정보는 제외됩니다. 전송된 패킷의 지속 시간과 수, HTTP 요청 처리 건수 등의 연결 메타데이터 통계에 대한 로그 사용을 제한합니다.

**데이터 캡처.** [_우리는 FIN 패킷으로_](https://blog.cloudflare.com/tcp-resets-timeouts/#tcp-connections-from-establishment-to-close) 정상적으로 닫히는 연결만 특성화하여 완전히 처리된 '유용한' 연결을 데이터 세트에 나타내기로 선택했습니다. 공격 완화로 가로채기 되었거나, 제한 시간 초과가 되었거나, RST 패킷 때문에 중단된 연결은 제외됩니다.

단계적 종료 자체가 '유용한' 연결을 의미하는 것은 아니므로, 이 분석에서 유휴 또는 비 HTTP 연결을 필터링하기 위해서는 추가로 이 분석에서 유휴 연결이나 비 HTTP**연결을 제외하기 위해서는 연결 중 최소 한 번의 성공적인 HTTP 요청이 필요합니다. FIN 패킷으로 닫히는 Cloudflare로의 연결을**

[ _자세한 내용은 이전에 블로그에 Cloudflare의 전체 로깅 메커니즘_](https://blog.cloudflare.com/how-we-make-sense-of-too-much-data/) 및 [_후처리 파이프라인에_](https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/) 대한 자세한 내용을 다룬 내용을 참고하시기 바랍니다. 

## 연결 특성 시각화

네트워크는 본질적으로 동적이며 시간이 지남에 따라 추세가 변할 수 있지만, 전역 인프라에서 관찰되는 대규모 패턴은 시간이 지나도 놀라울 정도로 일관되게 유지됩니다. 저희 데이터는 연결 특성에 대한 글로벌 보기를 제공하지만, 그 분포는 지역 트래픽 패턴에 따라 여전히 다를 수 있습니다.

시각화에서 특성은 [_누적 분포 함수(CDF)_](https://en.wikipedia.org/wiki/Cumulative_distribution_function) 그래프로 표현되며, 특히 [_경험에 따르면_](https://en.wikipedia.org/wiki/Empirical_distribution_function) 그렇습니다. CDF는 분포를 거시적으로 파악하는 데 특히 유용합니다. 이를 통해 일반적인 사례와 극단적인 사례를 모두 하나의 보기에서 명확하게 파악할 수 있습니다. 아래 그림에서는 이들 변수를 사용하여 대규모 패턴을 이해합니다. 분포를 더 잘 해석하기 위해 로그 스케일링된 축을 사용하여 네트워킹 데이터에 일반적인 극단 값의 존재를 설명했습니다.

인터넷 연결에 대한 오래된 질문은[ _'코끼리와 쥐'와_](https://en.wikipedia.org/wiki/Elephant_flow) 관련이 있습니다. 실무자와 연구자들은 대부분의 흐름이 소규모이고 일부는 대규모라는 사실을 완전히 알고 있지만, 이를 구분할 수 있는 데이터가 거의 없습니다. 여기에서 프레젠테이션이 시작됩니다.

### 패킷 수

먼저 Cloudflare 서버에서 클라이언트로 연결에 전송된 응답 패킷의 수 _분포_ 를 살펴보겠습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47QYXXY4HF6QRRZ15FH75Q.png&w=715&h=283&f=webp&fit=cover&position=center)

그래프에서 x축은 전송된 응답 패킷 수를 로그 스케일로 나타내고 y축은 각 패킷 수 아래의 누적 연결 비율을 나타냅니다. 평균 응답은 약 240개의 패킷으로 구성되어 있지만, 그 분포는 매우 왜곡되어 있습니다. 중앙값은 12 패킷으로, 인터넷 연결의 50%가 _매우 적은 패킷_ 으로 구성되어 있음을 나타냅니다. 90번째 백분위까지 확장하면, 연결은 107개의 패킷만 전달합니다.

이러한 대조는 인터넷 트래픽의 헤비 테일 특성을 극명하게 보여줍니다. 소수의 연결은 비디오 스트림 또는 대규모 파일 전송과 같은 대량의 데이터를 전송하지만, 대부분의 상호 작용은 아주 작아서 작은 웹 개체, 마이크로서비스 트래픽 또는 API 응답을 전달합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45Z9TFYWAAPF7EFSYJCSCC.png&w=715&h=434&f=webp&fit=cover&position=center)

위 도표는 패킷 카운트 분포를 HTTP 프로토콜 버전별로 보여줍니다. HTTP/1.X(HTTP 1.0 및 1.1 결합) 연결의 경우 응답 중앙값이 10패킷으로 구성되며, 전체 연결의 90%는 63개 미만의 응답 패킷을 전달합니다. 이와는 대조적으로 HTTP/2 연결은 중앙값 16패킷과 170패킷의 90번째 백분위수에서 더 큰 응답을 보입니다. 이러한 차이는 HTTP/2가 단일 연결을 통해 여러 스트림을 다중화하는 방식을 반영하는 것으로 보이며, 더 많은 요청과 응답을 더 적은 수의 연결로 통합하는 경우가 많으므로 연결당 교환되는 총 패킷 수가 증가하는 경우가 많습니다. 또한 HTTP/2 연결에는 응답 패킷 수를 늘리는 제어 평면 프레임과 흐름 제어 메시지가 추가로 있습니다.

이러한 차이점에도 불구하고 결합된 보기는 동일한 헤비 테일 패턴을 표시합니다.[_작은 부분의 연결이_](https://en.wikipedia.org/wiki/Mouse_flow)[ _엄청난 양의 데이터를 전달하여(코끼리_](https://en.wikipedia.org/wiki/Elephant_flow) 플로우) 수백만 개의 패킷으로 확장되는 반면, 대부분은 대부분 가벼운 상태로 유지됩니다(마우스 플로우).

지금까지는 서버에서 클라이언트로 전송된 패킷의 총 수에 초점을 맞추었지만, 연결 동작의 또 다른 중요한 차원은 아래 그림과 같이 전송 및 수신된 패킷 간의 균형입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47GFZ4V1R0M1Y4V7PV92DP.png&w=715&h=285&f=webp&fit=cover&position=center)

x축은 클라이언트로부터 수신한 패킷에 대한 Cloudflare의 서버에서 전송한 패킷의 비율을 나타내며, CDF로 시각화됩니다. 모든 연결에서 비율의 중앙값은 0.91로, 전체 연결의 절반에서 클라이언트가 서버가 응답하는 것보다 약간 더 많은 패킷을 전송한다는 것을 의미합니다. 이러한 과도한 클라이언트 측 패킷은 주로 [_TLS_](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) 핸드셰이크 시작(ClientHello), HTTP 제어 요청 헤더, 데이터 승인(ACK)을 반영하며, 일반적으로 클라이언트는 서버가 콘텐츠 악의적인 페이로드와 함께 반환하는 것보다 더 많은 패킷을 전송하게 됩니다. 배포에 영향을 미쳤습니다.

이는 CDN 워크로드의 전형적인 대량 다운로드와 같이 클라이언트 사용량이 많은 연결의 롱테일로 인해 1.28로 더 높습니다. 대부분의 연결은 상대적으로 좁은 범위에 속합니다. 전체 연결 중 10%의 비율은 0.67 미만이고 90%는 1.85 미만입니다. 그러나 롱테일 동작은 인터넷 트래픽의 다양성을 강조합니다. 업로드와 다운로드가 많은 연결에서 모두 극단적인 값이 발생합니다. 분산 3.71은 이러한 비대칭적인 흐름을 반영하는 반면, 연결 대량의 업로드-다운로드 교환은 대략적으로 균형을 유지하고 있습니다.

### 전송된 바이트

데이터를 살펴봐야 할 또 다른 측면은 서버에서 클라이언트로 전송하는 바이트를 사용하는 것입니다. 이는 각 연결을 통해 전달되는 실제 데이터 양을 포착합니다. 이 메트릭은 tcpi_bytes_sent에서 파생되었으며, [_linux/tcp.h_](https://github.com/torvalds/linux/blob/v6.14/include/uapi/linux/tcp.h#L222-L312)에 정의된 대로 TCP 헤더를 제외하면서 (재)전송된 세그먼트 페이로드도 포함합니다.[_RFC 4898_](https://www.rfc-editor.org/rfc/rfc4898.html)(TCP 확장 통계 MIB)을 준수합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44KWGERA5BCRTGWV167YSA.png&w=715&h=435&f=webp&fit=cover&position=center)

위 그래프는 HTTP 프로토콜 버전에서 전송한 바이트를 분석한 것입니다. x축은 각 연결을 통해 서버에서 전송한 총 바이트를 나타냅니다. 이러한 패턴은 패킷 카운트에서 관찰한 결과와 일반적으로 일치합니다.

HTTP/1.X의 경우, 응답 중앙값은 4.8KB이며, 연결의 90%는 51KB 미만을 전송합니다. 반면 HTTP/2 연결은 중앙값이 6KB이고 90번째 백분위수는 146KB로 약간 더 큰 응답을 보여줍니다. 평균은 HTTP/1.x의 경우 224KB로 훨씬 높습니다. HTTP/2의 경우 390KB로, 소수의 초대형 전송을 반영합니다. 이처럼 긴 종단이 있는 극단적인 흐름은 연결당 수십 기가바이트에 도달할 수 있으며, 일부 매우 가벼운 연결은 최소 페이로드(HTTP/1.X의 최소값은 115바이트, HTTP/2의 경우 202바이트)를 전달합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45NYVFVA7EPGHVE2Y56FMP.png&w=715&h=284&f=webp&fit=cover&position=center)

이제 tcpi_bytes_received 지표를 사용하여 전송한 바이트 수 대 수신한 바이트 수의 비율을 연결별로 살펴보면 데이터 교환의 균형을 더 잘 이해할 수 있습니다. 이 비율은 각 연결이 얼마나 비대칭적인지, 기본적으로는 클라이언트로부터 수신하는 데이터와 비교하여 서버를 전송하는 데이터의 양을 표시합니다. 모든 연결에서 중앙값 비율은 3.78로, 전체의 절반에서 서버가 수신하는 데이터보다 4배 가까이 더 많은 데이터를 전송한다는 의미입니다. 평균은 81.06으로 훨씬 높으며, 이는 다운로드가 많은 플로우로 인한 강력한 롱테일을 보여줍니다. 여기서도 롱테일 분포가 무거운 것을 볼 수 있습니다. 극단적인 사례 중 일부는 그 비율이 수백만 달러에 달하며, 클라이언트에게 전송되는 데이터의 경우에는 더 극단적인 값을 가집니다.

### 연결 지속 시간

패킷 및 바이트 카운트는 교환되는 데이터의 양을 포착하는 반면, 연결 지속 시간은 시간이 지남에 따라 교환이 어떻게 진행되는지에 대한 인사이트를 제공합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47PXY3XQP68A117HA5DKNF.png&w=715&h=284&f=webp&fit=cover&position=center)

위의 CDF에는 연결 지속 시간(수명)의 분포가 초 단위로 나와있습니다. x축은 로그 척도라는 것을 상기시킵니다. 모든 연결에서 지속 시간 중앙값은 4.7초로, 전체 연결의 절반이 5초 이내에 완료됨을 의미합니다. 평균은 96초로 훨씬 높으며, 이는 수명이 긴 연결이 소수로 평균이 왜곡된 것을 반영합니다. 대부분의 연결은 0.1초(10번째 백분위수)~300초(90번째 백분위수)의 범위에 속합니다. 또한 일부 연결은 며칠 동안 지속되며, 이러한 연결은 [_기본 유휴_](https://developers.cloudflare.com/fundamentals/reference/connection-limits/) [_제한_](https://developers.cloudflare.com/fundamentals/reference/tcp-connections/#tcp-connections-and-keep-alives) 시간 초과 제한에 도달하지 않고 연결 재사용을 위해 유지를 통해 유지 관리될 수 있습니다. 이러한 수명이 긴 연결은 일반적으로 영구 세션 또는 멀티미디어 트래픽을 나타내는 반면, 웹 트래픽의 대부분은 짧고 버스트이며 일시적입니다.

### 요청 수

단일 연결은 웹 트래픽에 대한 여러 HTTP 요청을 전달할 수 있습니다. 이렇게 하면 연결 멀티플렉싱에 대한 패턴이 드러납니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46XWSECRSDT0MKBF9XV7JY.png&w=715&h=284&f=webp&fit=cover&position=center)

위의 표에는 단일 연결에서 확인되는 HTTP 요청 수(로그 척도)가 HTTP 프로토콜 버전별로 분류되어 있습니다. HTTP/1.X(평균 3개 요청) 연결과 HTTP/2(평균 8개 요청) 연결 모두 요청의 중앙값이 1개에 불과하므로, 연결 재사용이 제한적으로 만연해 있음을 확인할 수 있습니다. 그러나 HTTP/2는 단일 연결을 통해 여러 스트림 멀티플렉싱을 지원하므로 90번째 백분위수는 10개의 요청으로 증가하며, 때로는 수천 개의 요청을 처리하는 극단적인 경우도 있으며, 이는 [_연결 병합_](https://blog.cloudflare.com/connection-coalescing-experiments/)으로 인해 증폭될 수 있습니다. 이와는 대조적으로, HTTP/1.X 연결은 요청 수가 훨씬 적습니다. 이는 프로토콜 설계와도 일맥상통합니다. HTTP/1.0은 "연결당 하나의 요청" 철학을 따르는 반면, HTTP/1.1은 지속적인 연결을 도입했습니다. 백분위수.

이러한 연결의 단기적인 만연은 부분적으로는 수명이 긴 세션을 유지하기보다는 새로운 연결을 여는 경향이 있는 자동화된 클라이언트나 스크립트 때문일 수 있습니다. 이러한 직관을 넓히기 위해 클라이언트 ASN을 프록시로 사용하여 데이터 센터에서 발생한 트래픽(자동화되었을 가능성이 높음)과 일반적인 사용자 트래픽(사용자 기반)으로 데이터를 분할했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44CSDBJTBW8CCP07JWENBR.png&w=715&h=284&f=webp&fit=cover&position=center)

위의 그래프를 보면 비 DC(사용자 주도) 트래픽은 연결당 요청 수가 약간 더 많으며, 평균은 5개, 요청당 5개의 요청의 90 백분위수는 단일 영구 연결을 통해 여러 리소스를 가져오는 브라우저나 앱과 일치합니다 연결합니다. 이와는 대조적으로 DC에서 시작된 트래픽은 평균이 약 3개 요청과 90번째 백분위수가 2개이므로 저희 예상이 맞았습니다. 이러한 차이에도 불구하고 요청의 중앙값 수는 두 그룹 모두에서 1로 유지되어 있으며, 이를 통해 연결 원본에 관계없이 대부분 진정으로 짧다는 점을 강조할 수 있습니다.

## 연결 수준 데이터에서 경로 특성 추론

연결 수준 측정을 통해 기본 경로 특성에 대한 인사이트도 제공할 수 있습니다. 이제 더 자세히 살펴보겠습니다.

### 경로 최대 전송 단위

네트워크 경로를 따른 최대 전송 단위([_MTU_](https://www.cloudflare.com/learning/network-layer/what-is-mtu/))는 경로 MTU(PMTU)라고 부르는 경우가 많습니다. PMTU는 처리량, 효율성, 대기 시간에 영향을 미치는 조각화나 패킷 끊김 없이 연결을 통과할 수 있는 가장 큰 패킷 크기를 결정합니다. Cloudflare 서버의 Linux TCP 스택은 경로 최대 전송 단위 [_발견의 일환으로, 연결 경로를 따라 분할 없이 전송할 수 있는 가장 큰 세그먼트 크기를 추적합니다._](https://blog.cloudflare.com/path-mtu-discovery-in-practice/)

해당 데이터에서 PMTU의 중앙값(그리고 90번째 백분위수!)이 1500바이트임을 확인했는데, 이는 일반적인 이더넷 최대 전송 단위와 일치하며 대부분의 인터넷 경로의 [_표준으로 간주됩니다_](https://en.wikipedia.org/wiki/Maximum_transmission_unit). 흥미롭게도 10번째 백분위수는 1,420바이트로, 일부 [_VPN_](https://blog.cloudflare.com/migrating-from-vpn-to-access/), [_IPv6tov4 터널_](https://blog.cloudflare.com/increasing-ipv6-mtu/) 또는 분할을 피하기 위해 더 엄격한 제한을 적용하는 구형 네트워킹 장비에서 흔히 볼 수 있는 약간 더 작은 MTU를 가진 네트워크 링크가 경로에 포함되는 경우를 반영합니다. 극단적으로 말하면 IPv4 연결의 경우 [_Linux 커널에서_](https://www.kernel.org/doc/html/v6.5/networking/ip-sysctl.html#:~:text=Default%3A%20FALSE-,min_pmtu,-%2D%20INTEGER) 허용하는 최소 PMTU 값에 해당하는 552바이트만큼 작은 최대 전송 단위도 발견되었습니다.

### 초기 정체 기간

전송 프로토콜의 핵심 매개변수는 수신자의 승인을 기다리지 않고 전송될 수 있는 패킷의 수인 혼잡 윈도우(CWND)입니다. 이러한 패킷 또는 바이트를 "전송 중"이라고 부릅니다. 연결 중 정체 기간은 연결 전체에서 동적으로 변화합니다.

그러나 데이터 전송이 시작될 때의 초기 정체 윈도우(ICWND)는 위에서 본 인터넷 트래픽을 지배하는 수명이 짧은 연결의 경우 특히 큰 영향을 미칠 수 있습니다. ICWND가 너무 낮게 설정되면 중소 규모 전송 시 병목 대역폭에 도달하는 데 왕복 시간이 더 걸리므로 전송이 느려집니다. 반대로 값이 너무 높으면 발신자가 네트워크를 압도하여 불필요한 패킷 손실과 재전송을 초래할 위험이 있으며, 잠재적으로 병목 링크를 공유하는 모든 연결에서 발생합니다.

ICWND의 합리적인 추정치는 TCP 발신자가 [_느린 시작_](https://www.rfc-editor.org/rfc/rfc5681#section-3.1)에서 벗어나는 순간의 정체 창 크기로 취할 수 있습니다. 이 전환은 발신자가 더 이상 성장하면 혼잡의 위험이 있을 수 있다고 추론한 후 기하급수적인 증가에서 혼잡 회피로 전환하는 지점입니다. 아래 그림에는 BBR에서 계산한 시점에 느린 시작이 종료되는 시점의 [_정체 창 크기_](https://blog.cloudflare.com/http-2-prioritization-with-nginx/#bbr-congestion-control) 분포가 나와 있습니다. 중앙값은 약 464KB로, 일반적인 1,500바이트 최대 전송 단위의 경우 연결당 약 310패킷에 해당하며, 극단적인 흐름은 수십 메가바이트를 전송합니다. 이러한 차이는 다양한 TCP 연결과 동적으로 진화하는 트래픽을 전달하는 네트워크의 특성을 반영하는 것입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48P2FEV66Z1CA6ZS429EJW.png&w=715&h=508&f=webp&fit=cover&position=center)

이러한 값은 Cloudflare와 최종 사용자 간의 경로뿐만 아니라 일반적으로 잘 프로비저닝되고 더 높은 대역폭을 제공하는 Cloudflare와 인접 데이터 센터 사이의 경로를 포함하는 다양한 네트워크 경로를 반영한다는 점을 강조하는 것이 중요합니다.

위의 분포를 처음 검사했을 때 값이 매우 높은 것 같아 의심스러웠습니다. 그제서야 이 수치는 BBR 특유의 행동에서 기인한 결과라는 것을 알게 됐습니다. 경로의 가용 용량 추정치인 [_대역폭 지연 곱(BDP)_](https://en.wikipedia.org/wiki/Bandwidth-delay_product)보다 혼잡 윈도우를 높게 설정하는 것입니다. [_의도적으로_](https://www.ietf.org/archive/id/draft-cardwell-iccrg-bbr-congestion-control-01.html#name-state-machine-operation) 값이 부풀려진 것입니다. 이 가설을 증명하기 위해 BBR의 추정 BDP와 함께 아래 그림의 분포를 다시 그래프로 표시합니다. BBR의 확인되지 않은 패킷의 정체 기간과 BDP 추정치 사이에는 차이가 명확합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3048 image 9](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RQYJGE165ZK072Q4297Y.png&w=715&h=508&f=webp&fit=cover&position=center)

위 그래프는 연결 원격 측정과 관련하여 계산된 BDP 값을 더합니다. BDP의 중앙값은 약 77KB로, 약 50패킷입니다. 이를 위에서 사용한 혼잡 기간 분포와 비교하면 최근에 닫은 연결의 BDP 추정치가 훨씬 더 안정적임을 알 수 있습니다.

Cloudflare에서는 이러한 인사이트를 사용하여 합리적인 초기 정체 창 크기와 해당 상황을 파악하고 있습니다. 내부적으로 Cloudflare의 자체 실험 결과, ICWND 크기가 더 작은 연결의 경우에 30~40%까지 성능에 영향을 미치는 것으로 나타났습니다. 이러한 통찰력은 10여 년 동안 10 [_패킷_](https://datatracker.ietf.org/doc/html/rfc6928) 의 기본값이었던 더 나은 초기 정체 창 값을 찾기 위한 노력을 다시 살펴보는 데 잠재적으로 도움이 될 것입니다.

### 더 깊은 이해, 더 나은 성능

우리는 인터넷 연결이 매우 이질적인 것을 관찰했으며,[_'코끼리와 쥐'_](https://en.wikipedia.org/wiki/Elephant_flow) 현상과 일치하는 강한 헤비 테일 특성이 수십 년 동안 관찰되었음을 확인했습니다. 업로드 바이트 대 다운로드 바이트의 비율은 큰 흐름에서는 놀랍지 않지만 짧은 흐름에서는 놀라울 정도로 작아 인터넷 트래픽의 비대칭 특성을 강조합니다. 이러한 연결 특성을 이해하면 연결 성능, 안정성 및 사용자 경험을 계속 개선할 수 있습니다.

저희는 이 작업을 계속해서 발전시켜 다른 사람들도 비슷한 혜택을 누릴 수 있도록 [_Cloudflare Radar_](https://radar.cloudflare.com/) 에 연결 수준 통계를 게시할 계획입니다.

네트워크를 개선하기 위한 작업은 현재 진행 중이며, 연구자, 학계, [_인턴_](https://blog.cloudflare.com/cloudflare-1111-intern-program/) 등 이 분야에 관심이 있는 모든 분은 [_ask-research@cloudflare.com_](mailto:ask-research@cloudflare.com)으로 연락 주시기 바랍니다. 지식을 공유하고 협력함으로써 우리 모두는 모두를 위해 인터넷을 더 빠르고, 안전하고, 더 신뢰할 수 있도록 계속 만들 수 있습니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmeasuring-network-connections-at-scale%2F&t=%EC%9D%B8%ED%84%B0%EB%84%B7%20%EA%B7%9C%EB%AA%A8%EC%97%90%EC%84%9C%20TCP%20%EC%97%B0%EA%B2%B0%EC%9D%98%20%ED%8A%B9%EC%84%B1%20%EC%B8%A1%EC%A0%95)[](https://x.com/intent/post?text=%EC%9D%B8%ED%84%B0%EB%84%B7+%EA%B7%9C%EB%AA%A8%EC%97%90%EC%84%9C+TCP+%EC%97%B0%EA%B2%B0%EC%9D%98+%ED%8A%B9%EC%84%B1+%EC%B8%A1%EC%A0%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmeasuring-network-connections-at-scale%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmeasuring-network-connections-at-scale%2F)[](https://bsky.app/intent/compose?text=%EC%9D%B8%ED%84%B0%EB%84%B7+%EA%B7%9C%EB%AA%A8%EC%97%90%EC%84%9C+TCP+%EC%97%B0%EA%B2%B0%EC%9D%98+%ED%8A%B9%EC%84%B1+%EC%B8%A1%EC%A0%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmeasuring-network-connections-at-scale%2F)[](https://mastodonshare.com/?text=%EC%9D%B8%ED%84%B0%EB%84%B7+%EA%B7%9C%EB%AA%A8%EC%97%90%EC%84%9C+TCP+%EC%97%B0%EA%B2%B0%EC%9D%98+%ED%8A%B9%EC%84%B1+%EC%B8%A1%EC%A0%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmeasuring-network-connections-at-scale%2F)[](https://www.threads.net/intent/post?text=%EC%9D%B8%ED%84%B0%EB%84%B7+%EA%B7%9C%EB%AA%A8%EC%97%90%EC%84%9C+TCP+%EC%97%B0%EA%B2%B0%EC%9D%98+%ED%8A%B9%EC%84%B1+%EC%B8%A1%EC%A0%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fmeasuring-network-connections-at-scale%2F)

## 관련 태그

[TCP](https://blog.cloudflare.com/ko-kr/tag/tcp/)[더 나은 인터넷](https://blog.cloudflare.com/ko-kr/tag/better-internet/)[연구](https://blog.cloudflare.com/ko-kr/tag/research/)[인사이트](https://blog.cloudflare.com/ko-kr/tag/insights/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Peter Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4945P7JZ17N06Z9Q2E2GNT.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Peter Wu](https://blog.cloudflare.com/ko-kr/author/peter-wu/)

[](https://lekensteyn.nl/)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
