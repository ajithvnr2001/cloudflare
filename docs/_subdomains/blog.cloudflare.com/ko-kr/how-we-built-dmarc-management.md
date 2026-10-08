---
url: https://blog.cloudflare.com/ko-kr/how-we-built-dmarc-management/
title: \uc6b0\ub9ac\uac00 Cloudflare Workers\ub97c \uc774\uc6a9\ud574 DMARC \uad00\ub9ac\ub97c \uad6c\ucd95\ud55c \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:42:19.116166+00:00
---

# 우리가 Cloudflare Workers를 이용해 DMARC 관리를 구축한 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/how-we-built-dmarc-management/

[블로그](https://blog.cloudflare.com/ko-kr/)

[DMARC](https://blog.cloudflare.com/ko-kr/tag/dmarc/)[Security Week](https://blog.cloudflare.com/ko-kr/tag/security-week/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)+11개의 태그 더 보기

4개 태그4개 태그 보기

  * 게시물 태그
  * [Security Week](https://blog.cloudflare.com/ko-kr/tag/security-week/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[이메일 보안](https://blog.cloudflare.com/ko-kr/tag/email-security/)
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



[이메일 보안](https://blog.cloudflare.com/ko-kr/tag/email-security/)

[DMARC](https://blog.cloudflare.com/ko-kr/tag/dmarc/)[Security Week](https://blog.cloudflare.com/ko-kr/tag/security-week/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[이메일 보안](https://blog.cloudflare.com/ko-kr/tag/email-security/)

2023년 3월 17일

# 우리가 Cloudflare Workers를 이용해 DMARC 관리를 구축한 방법

![André Cruz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FAFHK5DDQ0GQPPQ92C3B.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nelson Duarte](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49P72CGQX08FQC903Q0E4F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[André Cruz](https://blog.cloudflare.com/ko-kr/author/andre-cruz/) 및 [Nelson Duarte](https://blog.cloudflare.com/ko-kr/author/nelson-duarte/)

9분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/how-we-built-dmarc-management/), [Deutsch](https://blog.cloudflare.com/de-de/how-we-built-dmarc-management/), [Español](https://blog.cloudflare.com/es-es/how-we-built-dmarc-management/), [Français](https://blog.cloudflare.com/fr-fr/how-we-built-dmarc-management/), [日本語](https://blog.cloudflare.com/ja-jp/how-we-built-dmarc-management/), [繁體中文](https://blog.cloudflare.com/zh-tw/how-we-built-dmarc-management/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/how-we-built-dmarc-management/).

![How we built DMARC Management using Cloudflare Workers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VEZPBHGFF89NHRCXR27K.png&w=1201&h=676&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/vvo+fbi7uvV6ObO6ujQ7+3W7+zW6ebQ//vp+vXj7ujW5uDO6OPR7ujX7+nW6uTQ//3r/fbl7+bX5tzP6N3S7uXY8OfY7OTR///v//jo8+ja6dzS6t3V8OXb8+jb8ObU///z//3s+O7f7uPX7+TZ9evf+O7f9evZ///3///x/vXk9ezc9u7e/PPj/fXj+vHe///6///0//zo+vXg/Pbh//vm//vn/ffi///7///2//7p/fjh/vrj//3o//3o//jj)

### DMARC 보고서란

[DMARC](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/)는 도메인 기반 메시지 인증, 보고, 적합성을 의미합니다. 이는 이메일 [피싱](https://www.cloudflare.com/en-gb/learning/access-management/phishing-attack/) 및 [스푸핑](https://www.cloudflare.com/en-gb/learning/email-security/what-is-email-spoofing/) 방어에 도움이 되는 이메일 인증 프로토콜입니다.

DMARC를 사용하면 이메일을 전송할 때 [SPF](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/)(발신자 정책 프레임워크), [DKIM](https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/)(도메인키 식별 메일) 등 인증 방법을 지정하는 DNS 레코드를 설정하여 이메일의 진위 여부를 확인할 수 있습니다. 이메일이 이러한 인증 검사에 실패하면 DMARC는 수신자의 이메일 공급자가 메시지를 격리하거나 완전히 거부하여 메시지를 처리하는 방법을 알려줍니다.

이메일 피싱과 스푸핑 공격이 점점 더 정교해지며 널리 퍼지고 있는 오늘날의 인터넷 환경에서 DMARC의 중요성은 점점 더 커지고 있습니다. 도메인 소유자는 DMARC를 구현하면 이러한 공격으로 인해 발생하는 신뢰 상실, 평판 손상, 재정 손실 등의 부정적인 영향으로부터 브랜드와 고객을 보호할 수 있습니다.

DMARC는 피싱 및 스푸핑 공격으로부터의 방어하는 기능 외에도 [보고](https://www.rfc-editor.org/rfc/rfc7489) 기능도 제공합니다. 도메인 소유자는 어떤 메시지가 DMARC 검사를 통과했고 통과하지 못했는지, 메시지의 출처가 어디인지 등 이메일 인증 활동에 대한 보고서를 받을 수 있습니다.

DMARC 관리에는 도메인에 DMARC 정책을 구성하고 유지 관리하는 활동이 포함됩니다. DMARC를 효과적으로 관리하려면 이메일 인증 활동을 모니터링하고 분석하며 필요 시 DMARC 정책을 조정하거나 업데이트해야 합니다.

효과적인 DMARC 관리에 필요한 몇 가지 주요 구성 요소는 다음과 같습니다.

  * DMARC 정책 설정: 도메인의 DMARC 레코드를 구성하여 인증 검사에 실패한 메시지를 처리하기 위한 적절한 인증 방법과 정책을 지정합니다. DMARC DNS 레코드의 모습은 다음과 같습니다.



`v=DMARC1; p=reject; rua=mailto:dmarc@example.com`

이는 우리가 DMARC 버전 1을 사용하도록 지정합니다. 우리의 정책은 DMARC 확인에 실패한 경우 이메일을 거부하고 공급자가 DMARC 보고서를 보내야 하는 이메일 주소를 거부하는 것입니다.

  * 이메일 인증 활동 모니터링: DMARC 보고서는 도메인 소유자가 이메일 보안과 전달 가능성을 보장하고 업계 표준과 규정을 준수하는 데 중요한 도구입니다. 도메인 소유자는 DMARC 보고서를 정기적으로 모니터링하고 분석하면 이메일 위협을 식별하고 이메일 캠페인을 최적화하며 이메일 인증을 전반적으로 개선할 수 있습니다.
  * 필요 시 조정 수행: 도메인 소유자는 DMARC 보고서 분석을 기반으로 이메일 메시지를 적절하게 인증하고 피싱과 스푸핑 공격으로부터 보호하는 데 DMARC 정책 조정이나 인증 방법이 필요할 수 있습니다.
  * 이메일 공급자 및 타사 벤더와의 협업: 효과적으로 DMARC를 관리하려면 이메일 공급자 및 타사 벤더와 협업하여 DMARC 정책을 제대로 구현하고 적용하고 있는지 확인해야 합니다.



오늘 Cloudflare에서는 [DMARC 관리](https://blog.cloudflare.com/dmarc-management)를 출시했습니다. 구축 방법은 다음과 같습니다.

### 구축 방법

Cloudflare에서는 클라우드 기반 보안과 성능 솔루션의 선두 공급업체로서 특별한 접근 방식으로 제품을 테스트합니다. 자사 도구와 서비스를 "시험적으로 사용"합니다. 즉, 우리 사업을 운영하는 데 사용합니다. 이를 통해 어떠한 문제나 버그가 발생하여 고객에게 영향을 미치기 전에 이를 파악할 수 있습니다.

Cloudflare에서는 개발자가 전역 네트워크에서 코드를 실행할 수 있는 서버리스 플랫폼인 [Cloudflare Workers](https://workers.cloudflare.com/) 등 자사 제품을 내부적으로 사용하고 있습니다. 2017년 플랫폼 출시 이후 Workers 생태계는 크게 성장했습니다. 현재 수천 명의 개발자가 이 플랫폼에서 애플리케이션을 구축하고 배포하고 있습니다. Workers 생태계의 힘은 개발자가 이전에는 불가능했거나 비현실적이었던 정교한 애플리케이션을 구축하여 클라이언트와 가까운 곳에서 실행할 수 있다는 점입니다. Workers를 사용하면 API를 구축하고 동적 콘텐츠를 생성하고 실시간 처리를 수행할 수 있습니다. 가능성은 사실상 무한합니다. Cloudflare에서는 Workers를 사용하여 [Radar 2.0](https://blog.cloudflare.com/technology-behind-radar2/)과 같은 서비스나 [Wildebeest](https://blog.cloudflare.com/welcome-to-wildebeest-the-fediverse-on-cloudflare/)와 같은 소프트웨어 패키지를 구동했습니다.

최근 Cloudflare의 [이메일 라우팅](https://developers.cloudflare.com/email-routing/) 제품이 Workers와 통합되어 Workers 스크립트를 통해 [수신 이메일 처리](https://blog.cloudflare.com/announcing-route-to-workers/)가 가능합니다. [문서](https://developers.cloudflare.com/email-routing/email-workers/) 내용: “Email Workers를 사용하면 Cloudflare Workers의 강력한 기능을 활용하여 이메일을 처리하고 복잡한 규칙을 생성하는 데 필요한 로직을 구현할 수 있습니다. 이러한 규칙에 따라 이메일을 수신했을 때 어떤 일이 발생하는지가 결정됩니다.” 규칙과 확인된 주소는 모두 Cloudflare [API](https://developers.cloudflare.com/api/operations/email-routing-destination-addresses-list-destination-addresses)를 통해 구성할 수 있습니다.

간단한 Email Worker의 모습은 다음과 같습니다.

아주 간단하지요?
    
    
    export default {
      async email(message, env, ctx) {
        const allowList = ["friend@example.com", "coworker@example.com"];
        if (allowList.indexOf(message.headers.get("from")) == -1) {
          message.setReject("Address not allowed");
        } else {
          await message.forward("inbox@corp");
        }
      }
    }

수신 이메일을 프로그래밍 방식으로 처리할 수 있는 기능이 있는 이 플랫폼은 확장 가능하고 효율적인 방식으로 수신 DMARC 보고서 이메일을 처리할 수 있는 완벽한 방법인 것 같습니다. 또한 이메일 라우팅과 Workers는 전 세계에서 오는 수 많은 이메일을 수신하는 어려운 작업도 처리합니다. 필요했던 기능을 대략적으로 설명하면 다음과 같습니다.

  1. 이메일 수신 및 보고서 추출
  2. 분석 관련 플랫폼에 관련 세부 정보 게시
  3. 원시 보고서 저장



Email Workers를 사용하면 첫 번째 기능은 쉽게 수행할 수 있습니다. email() 핸들러가 있는 worker를 생성하기만 하면 됩니다. 이 핸들러는 [SMTP](https://www.rfc-editor.org/rfc/rfc5321) 봉투 요소, 사전 구문 분석된 버전의 이메일 헤더, 전체 원시 이메일을 읽을 수 있는 스트림을 수신합니다.

두 번째 기능의 경우에도 Workers 플랫폼을 살펴보면 [Workers Analytics 엔진](https://developers.cloudflare.com/analytics/analytics-engine/)을 확인할 수 있습니다. 보고서의 내용과 이후에 수행하려는 쿼리에 따라 적절한 스키마를 정의하기만 하면 됩니다. 그런 다음 [GraphQL](https://developers.cloudflare.com/analytics/graphql-api/) 또는 [SQL](https://developers.cloudflare.com/analytics/analytics-engine/sql-api/) API를 사용하여 데이터를 쿼리할 수 있습니다.

세 번째 기능의 경우 [R2](https://www.cloudflare.com/en-gb/products/r2/) 개체 스토리지만 살펴보면 됩니다. Worker에서 R2를 액세스하는 것은 [단순](https://developers.cloudflare.com/r2/examples/demo-worker/)합니다. 이메일에서 보고서를 추출한 후 나중을 위해 R2에 저장합니다.

이 기능을 영역에서 사용할 수 있는 관리형 서비스로 구축했고 편의성을 위해 대시보드 인터페이스에 추가했지만, 실제로는 서버, 확장성 성능을 걱정할 필요 없이 자신의 계정에서 Cloudflare Workers상에 나만의 DMARC 보고서 프로세서를 배포할 수 있습니다.

### 아키텍처

[Email Workers](https://developers.cloudflare.com/email-routing/email-workers/)는 이메일 라우팅 제품의 주요 기능입니다. 이메일 라우팅 구성 요소는 모든 노드에서 실행되므로 어떤 노드에서도 수신 이메일을 처리할 수 있으며, 이는 모든 Cloudflare 데이터 센터의 Email 수신 BGP 접두사를 알려주므로 중요합니다. Email Worker에 이메일을 보내는 것은 이메일 라우팅 대시보드에서 규칙을 설정하는 것만큼 쉽습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1751 Embedded Image - qUt3Zo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW465JK1BXGCB56J3DVNFMVG.png&w=715&h=410&f=webp&fit=cover&position=center)

이메일 라우팅 구성 요소가 Worker에 전달할 규칙과 일치하는 이메일을 수신하면, 최근에 오픈 소스로 지원하고 모든 노드에서도 실행되는 자사 버전의 [workerd](https://github.com/cloudflare/workerd) 런타임에 연결됩니다. 이 상호 작용을 관장하는 RPC 스키마는 [Capnproto](https://github.com/capnproto/capnproto) 스키마에 정의되어 있으며, 이메일 본문을 읽을 때 Edgeworker로 스트리밍될 수 있습니다. Worker 스크립트가 이 이메일로 전달하기로 결정한 경우 Edgeworker는 원본 요청에서 전송된 기능을 사용하여 이메일 라우팅에 연결합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1751 Embedded Image - xo7GIP](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW472EZF80K47ZMXFN76TXDC.png&w=715&h=139&f=webp&fit=cover&position=center)

DMARC 보고서의 맥락에서 수신 이메일을 처리하는 방식은 다음과 같습니다.
    
    
    jsg::Promise<void> ForwardableEmailMessage::forward(kj::String rcptTo, jsg::Optional<jsg::Ref<Headers>> maybeHeaders) {
      auto req = emailFwdr->forwardEmailRequest();
      req.setRcptTo(rcptTo);
    
      auto sendP = req.send().then(
          [](capnp::Response<rpc::EmailMetadata::EmailFwdr::ForwardEmailResults> res) mutable {
        auto result = res.getResponse().getResult();
        JSG_REQUIRE(result.isOk(), Error, result.getError());
      });
      auto& context = IoContext::current();
      return context.awaitIo(kj::mv(sendP));
    }
    

  1. 처리 중인 이메일의 수신자를 가져옵니다. 이것은 사용된 RUA입니다. RUA는 특정 도메인과 관련한 집계 DMARC 처리 피드백을 보고해야 할 위치를 나타내는 DMARC 구성 매개변수입니다. 이 수신자는 메시지의 “to” 속성에서 찾을 수 있습니다.
  2. const ruaID = message.to
  3. 도메인에서 무제한으로 DMARC 보고서를 처리할 수 있으므로 Workers KV를 사용하여 각 도메인의 일부 정보를 저장하고 이 정보를 RUA의 키로 저장합니다. 이는 또한 이러한 보고서를 수신해야 하는지 여부도 알려줍니다.
  4. const accountInfoRaw = await env.KV_DMARC_REPORTS.get(dmarc:${ruaID})
  5. 이 시점에서 전체 이메일을 구문 분석하기 위해 arrayBuffer로 읽어야 합니다. 보고서의 크기에 따라 무료 Workers 요금제의 한도에 도달할 수 있습니다. 이 경우 문제가 없는 [Workers Unbound](https://www.cloudflare.com/en-gb/workers-unbound-beta/) 리소스 모델로 전환하는 것이 좋습니다.
  6. const rawEmail = new Response(message.raw)  
const arrayBuffer = await rawEmail.arrayBuffer()
  7. 원시 이메일 구문 분석에는 무엇보다도 MIME 부분의 구문 분석이 포함됩니다. 구문 분석 수행에 사용할 수 있는 여러 라이브러리가 있습니다. 예를 들어, [postal-mime](https://www.npmjs.com/package/postal-mime)을 사용할 수 있습니다.
  8. const parser = new PostalMime.default()  
const email = await parser.parse(arrayBuffer)
  9. 이메일을 구문 분석했으므로 이제 첨부 파일에 액세스할 수 있습니다. 이 첨부 파일은 DMARC 보고서 자체이며 압축할 수 있습니다. 장기 보관을 위해 가장 먼저 압축된 형태로 [R2](https://developers.cloudflare.com/r2/data-access/workers-api/workers-api-usage/)에 저장합니다. 이들 에메일은 이후 관심이 있는 보고서를 재처리하거나 조사할 때 유용하게 사용할 수 있습니다. 이 작업은 R2 바인딩에서 put()을 호출하는 것만큼 간단합니다. 이후 쉽게 검색할 수 있도록 현재 시간을 기준으로 보고서 파일을 여러 디렉터리에 분산하는 것을 권장합니다.
  10. await env.R2_DMARC_REPORTS.put(  
`${date.getUTCFullYear()}/${date.getUTCMonth() + 1}/${attachment.filename}`,  
attachment.content  
)
  11. 이제 첨부 파일 mime 유형을 살펴볼 필요가 있습니다. DMARC 보고서의 원시 형식은 XML이지만, 압축할 수 있습니다. 이 경우 먼저 보고서의 압축을 풀어야 합니다. DMARC 리포터 파일은 여러 압축 알고리즘을 사용할 수 있습니다. 어떤 알고리즘을 사용하는지 MIME 유형으로 확인합니다.[Zlib](https://en.wikipedia.org/wiki/Zlib)로 압축된 보고서의 경우 [pako](https://www.npmjs.com/package/pako)를 사용할 수 있고 ZIP으로 압축된 보고서의 경우 [unzipit](https://www.npmjs.com/package/unzipit)를 선택하는 것이 좋습니다.
  12. 보고서의 원시 XML 형식을 확보했다면 구문 분석할 때 [fast-xml-parser](https://www.npmjs.com/package/fast-xml-parser)가 잘 작동한 것입니다. DMARC 보고서 XML의 모습은 다음과 같습니다.
  13. 이제 보고서의 데이터를 모두 손에 넣었습니다. 지금부터는 데이터를 표시하려는 방법에 따라 많이 달라집니다. Cloudflare의 목표는 보고서에서 추출한 의미 있는 데이터를 대시보드에 표시하는 것이었습니다. 그래서 풍부한 데이터를 푸시할 수 있는 분석 플랫폼이 필요했습니다. 그것이 바로 [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/)입니다. 이 분석 엔진을 사용하면 worker에서 데이터를 엔진으로 [전송](https://developers.cloudflare.com/analytics/analytics-engine/get-started/#3-write-data-from-your-worker)할 수 있고, [GraphQL API](https://developers.cloudflare.com/analytics/graphql-api/)를 노출하여 이후 데이터와 상호 작용할 수 있으므로 이 작업에 완벽합니다. 여기까지가 바로 대시보드에 표시할 데이터를 얻는 방법입니다.



향후에는 보고서를 비동기적으로 처리하고 클라이언트가 처리를 완료할 때까지 기다리지 않도록 워크플로우에서 [Queues](https://developers.cloudflare.com/queues/)를 통합하는 방안도 고려하고 있습니다.
    
    
    const ruaID = message.to

Workers 인프라에만 의존하여 엔드투엔드 방식으로 이 프로젝트를 구현했으므로 확장성, 성능, 스토리지, 보안 문제를 걱정하지 않고 단순하지 않은 앱을 구축하는 것이 가능하며 유리하다는 점을 증명했습니다.
    
    
    const accountInfoRaw = await env.KV_DMARC_REPORTS.get(dmarc:${ruaID})

### 오픈 소스
    
    
    const rawEmail = new Response(message.raw)
    const arrayBuffer = await rawEmail.arrayBuffer()

앞서 언급했듯이 Cloudflaredptj는 활성화하여 사용할 수 있는 관리형 서비스를 구축했으므로 대신 관리해 드리겠습니다. 하지만 계정에서 직접 배포하신 후 자체 DMARC 보고서를 관리할 수도 있습니다. 쉽고 무료입니다. 이를 지원하기 위해 위에서 설명한 방식대로 DMARC 보고서를 처리하는 오픈 소스 버전의 Worker를 출시합니다. <https://github.com/cloudflare/dmarc-email-worker>
    
    
    const parser = new PostalMime.default()
    const email = await parser.parse(arrayBuffer)

데이터를 표시할 대시보드가 없는 경우에도 Worker에서 분석 엔진을 [쿼리](https://developers.cloudflare.com/analytics/analytics-engine/worker-querying/)할 수 있습니다. 또는 관계형 데이터베이스에 저장하려는 경우 [D1](https://developers.cloudflare.com/d1/platform/client-api/)을 사용할 수 있습니다. 가능성은 무궁무진하며 이러한 도구로 무엇을 구축하실지 기대가 됩니다.
    
    
    await env.R2_DMARC_REPORTS.put(
        `${date.getUTCFullYear()}/${date.getUTCMonth() + 1}/${attachment.filename}`,
        attachment.content
      )

기여해 주시고 직접 만들어시면 귀 기울여 듣겠습니다.
    
    
    <feedback>
      <report_metadata>
        <org_name>example.com</org_name>
        <emaildmarc-reports@example.com</email>
       <extra_contact_info>http://example.com/dmarc/support</extra_contact_info>
        <report_id>9391651994964116463</report_id>
        <date_range>
          <begin>1335521200</begin>
          <end>1335652599</end>
        </date_range>
      </report_metadata>
      <policy_published>
        <domain>business.example</domain>
        <adkim>r</adkim>
        <aspf>r</aspf>
        <p>none</p>
        <sp>none</sp>
        <pct>100</pct>
      </policy_published>
      <record>
        <row>
          <source_ip>192.0.2.1</source_ip>
          <count>2</count>
          <policy_evaluated>
            <disposition>none</disposition>
            <dkim>fail</dkim>
            <spf>pass</spf>
          </policy_evaluated>
        </row>
        <identifiers>
          <header_from>business.example</header_from>
        </identifiers>
        <auth_results>
          <dkim>
            <domain>business.example</domain>
            <result>fail</result>
            <human_result></human_result>
          </dkim>
          <spf>
            <domain>business.example</domain>
            <result>pass</result>
          </spf>
        </auth_results>
      </record>
    </feedback>

### 마지막 한마디

이 게시물을 통해 Workers 플랫폼에 대한 이해가 한층 더 깊어졌기를 바랍니다. 현재 Cloudflare는 이 플랫폼을 활용하여 당사 서비스 대부분을 구축하고 있으며 귀사에서도 가능하다고 생각합니다.

오픈 소스 버전에 자유롭게 기여하시고 무엇을 할 수 있는지 보여 주세요.

또한 이메일 라우팅에서는 Email Workers API의 기능적 측면을 더 확장하고 있지만, 그 내용은 곧 다른 블로그에서 다룰 예정입니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-dmarc-management%2F&t=%EC%9A%B0%EB%A6%AC%EA%B0%80%20Cloudflare%20Workers%EB%A5%BC%20%EC%9D%B4%EC%9A%A9%ED%95%B4%20DMARC%20%EA%B4%80%EB%A6%AC%EB%A5%BC%20%EA%B5%AC%EC%B6%95%ED%95%9C%20%EB%B0%A9%EB%B2%95)[](https://x.com/intent/post?text=%EC%9A%B0%EB%A6%AC%EA%B0%80+Cloudflare+Workers%EB%A5%BC+%EC%9D%B4%EC%9A%A9%ED%95%B4+DMARC+%EA%B4%80%EB%A6%AC%EB%A5%BC+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-dmarc-management%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-dmarc-management%2F)[](https://bsky.app/intent/compose?text=%EC%9A%B0%EB%A6%AC%EA%B0%80+Cloudflare+Workers%EB%A5%BC+%EC%9D%B4%EC%9A%A9%ED%95%B4+DMARC+%EA%B4%80%EB%A6%AC%EB%A5%BC+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-dmarc-management%2F)[](https://mastodonshare.com/?text=%EC%9A%B0%EB%A6%AC%EA%B0%80+Cloudflare+Workers%EB%A5%BC+%EC%9D%B4%EC%9A%A9%ED%95%B4+DMARC+%EA%B4%80%EB%A6%AC%EB%A5%BC+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-dmarc-management%2F)[](https://www.threads.net/intent/post?text=%EC%9A%B0%EB%A6%AC%EA%B0%80+Cloudflare+Workers%EB%A5%BC+%EC%9D%B4%EC%9A%A9%ED%95%B4+DMARC+%EA%B4%80%EB%A6%AC%EB%A5%BC+%EA%B5%AC%EC%B6%95%ED%95%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-dmarc-management%2F)

## 관련 태그

[DMARC](https://blog.cloudflare.com/ko-kr/tag/dmarc/)[Security Week](https://blog.cloudflare.com/ko-kr/tag/security-week/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[이메일 보안](https://blog.cloudflare.com/ko-kr/tag/email-security/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
