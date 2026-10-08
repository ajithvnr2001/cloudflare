---
url: https://blog.cloudflare.com/ko-kr/waf-payload-logging/
title: \uc545\uc758\uc801\uc778 \ud398\uc774\ub85c\ub4dc \ub85c\uae45\uc73c\ub85c WAF\uc758 \uac00\uc2dc\uc131 \uac1c\uc120 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:48.012418+00:00
---

# 악의적인 페이로드 로깅으로 WAF의 가시성 개선 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/waf-payload-logging/

[블로그](https://blog.cloudflare.com/ko-kr/)

[WAF](https://blog.cloudflare.com/ko-kr/tag/waf/)[로깅](https://blog.cloudflare.com/ko-kr/tag/logging/)[방화벽](https://blog.cloudflare.com/ko-kr/tag/firewall/)

3개 태그3개 태그 보기

  * 게시물 태그
  * [WAF](https://blog.cloudflare.com/ko-kr/tag/waf/)[로깅](https://blog.cloudflare.com/ko-kr/tag/logging/)[방화벽](https://blog.cloudflare.com/ko-kr/tag/firewall/)
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



[WAF](https://blog.cloudflare.com/ko-kr/tag/waf/)[로깅](https://blog.cloudflare.com/ko-kr/tag/logging/)[방화벽](https://blog.cloudflare.com/ko-kr/tag/firewall/)

2025년 11월 24일

# 악의적인 페이로드 로깅으로 WAF의 가시성 개선

![Paschal Obba](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48YJYHP0864S3RA6Z3GTZE.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Paschal Obba](https://blog.cloudflare.com/ko-kr/author/paschal/)

9분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/waf-payload-logging/) 및 [日本語](https://blog.cloudflare.com/ja-jp/waf-payload-logging/).

![BLOG-2824 Hero Image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW450A990GQDCP1NNP086BTB.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v398vLz6+vt7e3v8/Lz9PDw7+np/f//9/r/6+/25Onw5ury7O717Ozz5+bs9/7/8fn/5u763+j04en25uz65ur34OTw+P//8/z/6PL/4ev54+z85+//5+384ef0/////P//8vr/7PP/7vX/8vf/8fX/6+/6////////////+v7//P//////////+vn+////////////////////////////////////////////////////////////////)

웹에서 공격이 발생할 수 있는 표면 영역이 증가함에 따라, Cloudflare의 [_웹 애플리케이션 방화벽(WAF)_](https://www.cloudflare.com/application-services/products/waf/) 은 이러한 공격을 완화하기 위한 수많은 솔루션을 제공합니다. 이는 Cloudflare 고객에게는 유용하지만, Cloudflare에서 서비스하는 수백만 건의 요청 워크로드에 있어 카디널리티로 인해 긍정 오류가 불가피합니다. 즉, 고객을 위한 기본 구성은 미세 조정되어야 합니다. 

미세 조정은 어려운 프로세스가 아닙니다. 고객은 일부 데이터 포인트를 얻은 다음 자신에게 적합한 것을 결정해야 합니다. 이 게시물에서는 WAF가 특정 작업을 수행하는 이유를 고객들이 확인할 수 있도록 Cloudflare가 제공하는 기술들과, 노이즈를 줄이고 신호를 늘리기 위한 개선 사항들을 설명합니다.

## 로그 작업은 훌륭합니다. 더 많은 작업을 수행할 수 있을까요?

Cloudflare의 [_WAF_](https://www.cloudflare.com/application-services/products/waf/) 는 [_애플리케이션 계층_](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/)을 대상으로 하는 공격인 다양한 종류의 애플리케이션 계층 공격으로부터 원본 서버를 보호합니다. 다음과 같은 다양한 도구로 보호할 수 있습니다.

  * Cloudflare의 보안 분석가가 _[일반적인 취약점 및 노출(CVE),](https://www.cve.org/)[OWASP 보안](https://www.cloudflare.com/learning/security/threats/owasp-top-10/)_ 위험, Log4Shell과 같은 취약점을 해결하기 위해[ _작성하는 관리형 규칙._](https://developers.cloudflare.com/waf/managed-rules/)
  * [_사용자 지정_](https://developers.cloudflare.com/waf/custom-rules/) 규칙. 고객이 표현형 Rules [_언어로 규칙을 작성할 수 있습니다._](https://developers.cloudflare.com/ruleset-engine/rules-language/)
  * [_레이트 리미팅_](https://developers.cloudflare.com/waf/rate-limiting-rules/) 규칙, [_악의적 업로드_](https://developers.cloudflare.com/waf/detections/malicious-uploads/) 감지, [_자격 증명 유출_](https://developers.cloudflare.com/waf/detections/leaked-credentials/) 감지 등



이러한 도구는 [_Rulesets 엔진_](https://developers.cloudflare.com/ruleset-engine/)을 기반으로 합니다. [_규칙 표현식_](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/)과 일치하는 항목이 있으면 엔진이 [_작업_](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/)을 실행합니다.

로그 작업은 규칙의 동작을 시뮬레이션하는 데 사용됩니다. 이렇게 하면 엔진이 규칙 표현식과 일치하는지 확인하고 [_보안 분석_](https://developers.cloudflare.com/waf/analytics/security-analytics/), [_보안 이벤트_](https://developers.cloudflare.com/waf/analytics/security-events/), [_Logpush_](https://developers.cloudflare.com/logs/logpush/) 또는 [_Edge Log Delivery_](https://developers.cloudflare.com/logs/logpush/logpush-job/edge-log-delivery/)를 통해 액세스할 수 있는 로그 이벤트를 방출합니다.

로그는 규칙이 일치할 것으로 예상된 트래픽에서 예상대로 작동하는지 확인하는 데는 훌륭하지만, 특히 규칙 표현식에 여러 코드 경로가 있을 수 있는 경우 규칙 일치를 보여주는 것으로는 충분하지 않습니다.  
  
의사 코드에서 식은 다음과 같을 수 있습니다.

`http 요청 헤더에 '인증' 키가 포함되어 있거나 http 호스트 헤더의 소문자 표현이 "cloudflare"로 시작하는 경우 theN log`  
  
규칙 언어 구문은 다음과 같습니다.
    
    
    any(http.request.headers[*] contains "authorization") or starts_with(lower(http.host), "cloudflare")

이 표현식을 디버깅하면 몇 가지 문제가 발생합니다. 위 OR 표현식의 왼쪽(LHS) 아니면 오른쪽(RHS)이 일치하는 것은? [_Base64_](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#decode_base64) 디코딩, [_URL 디코딩,_](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#url_decode) 이 경우 [_소문자_](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#lower) 등의 기능은 이러한 필드의 원래 표현에 변환을 적용할 수 있으며, 이로 인해 요청의 어떤 특성이 일치하는지에 대한 모호성이 더욱 커집니다.

[_규칙_](https://developers.cloudflare.com/ruleset-engine/about/rules/) [_집합의_](https://developers.cloudflare.com/ruleset-engine/about/rulesets/) 많은 규칙이 일치 항목을 등록할 수 있으므로 상황이 더욱 복잡해집니다. [_Cloudflare OWASP_](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/) 와 같은 규칙 집합은 다양한 규칙의 누적 점수를 사용하여 점수가 [_설정된 임계값_](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/#score-threshold)을 초과할 때 작업을 트리거합니다. 

또한 Cloudflare Managed 및 OWASP 규칙의 표현은 비공개입니다. 이는 Cloudflare의 보안 상태를 강화하지만, 고객은 이러한 규칙이 제목, 태그 및 설명을 통해서만 무엇을 하는지 추측할 수 밖에 없습니다. 예를 들어, 레이블이 “SonicWall DMA - 원격 코드 실행 - CVE:CVE-2025-32819”일 수 있습니다.

다음과 같은 질문을 제기합니다. 요청의 어떤 부분이 규칙 집합 엔진의 일치로 이어졌습니까? 긍정 오류일까요? 

바로 이 부분에서 악의적인 페이로드 로깅이 빛을 발합니다. 변환 후 일치를 가져온 규칙에서 특정 필드와 해당 값으로 자세히 분석하는 데 도움이 될 수 있습니다. 

## 페이로드 로깅

악의적인 페이로드 로깅은 WAF가 조치를 취하게 한 규칙과 연결된 요청의 필드를 기록하는 기능입니다. 이는 모호성을 줄이고, 오탐을 검사하고, 정확성을 보장하며, 더 나은 성능을 위해 이러한 규칙을 미세 조정하는 데 도움이 되는 유용한 정보를 제공합니다.

위 예에서 악의적인 페이로드 로그 항목은 표현식의 왼쪽 또는 오른쪽 중 하나를 포함하지만, 둘 모두를 포함하지는 않습니다. 

### 악의적인 페이로드 로깅은 어떻게 작동할까요?

악의적인 페이로드 로깅 및 규칙 집합 엔진은 Wirefilter에 구축되었으며, 이는 이미 자세히 [_설명되어_](https://blog.cloudflare.com/building-fast-interpreters-in-rust/) 있습니다.

기본적으로 이러한 엔진은 Rust로 작성된 객체로서 [_컴파일러_](https://github.com/cloudflare/wirefilter/blob/72e3954622ff7f30c4171f45461c2274656ee1e3/engine/src/compiler.rs#L7) 특성을 구현합니다. 이러한 특성에 따라 이러한 표현식에서 파생된 추상 구문 트리(AST)가 컴파일됩니다.
    
    
    struct PayloadLoggingCompiler {
         regex_cache HashMap<String, Arc<Regex>>
    }
    
    impl wirefilter::Compiler for PayloadLoggingCompiler {
    	type U = PayloadLoggingUserData
    	
    	fn compile_logical_expr(&mut self, node: LogicalExpr) -> CompiledExpr<Self::U> {
    		// ...
    		let regex = self.regex_cache.entry(regex_pattern)
    		.or_insert_with(|| Arc::new(regex))
    		// ...
    	}
    
    }

규칙 세트 엔진은 표현식을 실행하며, 평가가 참이면 재평가를 위해 표현식과 [_실행 컨텍스트_](https://github.com/cloudflare/wirefilter/blob/72e3954622ff7f30c4171f45461c2274656ee1e3/engine/src/execution_context.rs#L38) 가 악의적인 페이로드 로깅 컴파일러로 전송됩니다. 실행 컨텍스트는 표현식을 평가하는 데 필요한 모든 런타임 값을 제공합니다.

재평가가 완료된 후 true로 평가된 표현식 분기에 관련된 필드가 기록됩니다.

로그의 구조는 wirefilter 필드와 해당 값의 맵입니다 `Map<Field, Value>`
    
    
    {
    
    	“http.host”: “cloudflare.com”,
    	“http.method”: “get”,
    	“http.user_agent”: “mozilla”
    
    }

참고: [_이러한 로그는 고객이 제공한 공개 키로 암호화됩니다._](https://blog.cloudflare.com/encrypt-waf-payloads-hpke/)

이러한 로그는 로깅 파이프라인을 거치며 다양한 방식으로 읽을 수 있습니다. 고객은 Logpush 작업을 구성하여 당사가 구축한 사용자 지정 Worker에 작성하며, 이 Worker는 고객의 개인 키를 사용하여 이러한 로그를 자동으로 해독할 수 있습니다. 악의적인 페이로드 로깅 [_CLI 도구_](https://github.com/cloudflare/matched-data-cli), [_Worker_](https://github.com/cloudflare/matched-data-worker) 또는 Cloudflare 대시보드를 사용해도 복호화할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![ALT description goes here](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HRS75MW92YDSCY8NRK05.png&w=715&h=264&f=webp&fit=cover&position=center)

### 어떤 개선 사항이 제공되었나요?

wirefilter에서 일부 필드는 배열 유형입니다. [_http.request.headers.names_](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.names/) 필드는 요청에 포함된 모든 헤더 이름의 배열입니다. 예:
    
    
    [“content-type”, “content-length”, “authorization”, "host"]

헤더 중 하나 이상에 문자 "c"가 포함되어 있으므로 `any(http.request.headers.names[*] contains “c”)`라고 읽는 식은 true로 평가됩니다. 이전 버전의 악의적인 페이로드 로깅 컴파일러에서는 "http.request.headers.names" 필드는 true로 평가되는 표현식의 일부이므로 기록됩니다. 

**악의적인 페이로드 로그(이전)**
    
    
     http.request.headers.names[*] = [“content-type”, “content-length”, “authorization”, "host"]

이제 배열 필드를 부분적으로 평가하고 표현식 제약 조건과 일치하는 인덱스를 기록합니다. 이 경우 헤더에만 "c"가 포함됩니다!

**악의적인 페이로드 로그(신규)**
    
    
     http.request.headers.names[0,1] = [“content-type”, “content-length”]

### 연산자

이제 wirefilter 연산자로 이동합니다. "eq"와 같은 일부 연산자는 정확히 일치합니다. `http.host eq “a.com”`. "in", "contains", "matches"와 같이 "부분적" 일치 결과를 초래하는 연산자가 정규 표현식과 함께 작동합니다.   
  
예시에서의 표현식 ``any(http.request.headers[*] contains “c”)`는` 부분 일치를 생성하는 "contains" 연산자를 사용합니다. 또한 부분적으로 일치한다고 말할 수 있는 "`any` " 함수를 사용합니다. 헤더 중 적어도 하나에 "c"가 포함된 경우 _모든_ 헤더를 기록해야 _하는_ 것은 아닙니다(이전 버전에서처럼).

악의적인 페이로드 로깅 컴파일러가 개선되어 이러한 표현식을 평가할 때는 부분적으로 일치하는 부분만 기록합니다. 이 경우 새로운 악의적인 페이로드 로깅 컴파일러는 [_Rust 표준 라이브러리에서 바이트에 대한 "find" 메서드와 유사하게 "contains" 연산자를_](https://doc.rust-lang.org/std/string/struct.String.html#method.find) 처리합니다. 따라서 악의적인 페이로드 로그가 다음과 같이 개선됩니다.
    
    
    http.request.headers.names[0,1] = [“c”, “c”]

따라서 상황이 훨씬 명확해집니다. 또한 로깅 파이프라인이 수백만 바이트를 처리하는 과정을 절약할 수 있습니다. 예를 들어, 많이 분석되는 필드는 요청 본문 — [_http.request.body.raw_](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.raw/)— 이며 그 크기가 수십 KB에 달할 수 있습니다. 때때로 표현식에서는 세 문자와 일치하는 정규식 패턴이 확인됩니다. 이 경우 킬로바이트 대신 3 바이트를 기록합니다!

### 컨텍스트

저도 알아요, `[“c”, “c”]` 는 사실 큰 의미가 없습니다. 우리가 일치의 정확한 이유를 제공했고 고객의 스토리지 대상에 기록되는 바이트 양을 상당히 줄이고 있더라도 고객에게 유용한 디버깅 정보를 제공하는 것이 핵심 목표입니다. 페이로드 로깅 개선의 일환으로, 컴파일러는 이제 부분 일치에 대해 "이전" 및 "이후"(해당되는 경우)도 기록합니다. 이들 버퍼의 크기는 현재 각각 15바이트입니다. 즉, 악의적인 페이로드 로그는 다음과 같습니다.
    
    
    http.request.headers[0,1] = [
        {
            before: null, // isnt included in the final log
            content: “c”, 
            after: “ontent-length”
        },
        {
            before: null, // isnt included in the final log
            content: “c”, 
            after:”ontent-type”
        }
    ]

**악의적인 페이로드 로그 예시(이전)**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2824 Image 2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4748NX8WS1HGMYVGJVX515.png&w=715&h=87&f=webp&fit=cover&position=center)

**악의적인 페이로드 로그 예시(신규)**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2824 Image 3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW483F5T65F4C7D3QV5A9YKG.png&w=715&h=194&f=webp&fit=cover&position=center)

이전 로그에는 모든 헤더 값이 있습니다. 새 로그에서 확인할 수 있는 것은 HTTP 헤더의 악의적 스크립트인 8번째 인덱스입니다. “<script>” 태그에서 일치하고 나머지는 회색 텍스트인 컨텍스트입니다. 

### 최적화

관리형 규칙은 악의적 요청을 감지하기 위해 정규 표현식에 크게 의존합니다. 이러한 표현식을 구문 분석하고 컴파일하는 것은 CPU를 많이 사용하는 작업입니다. 관리 규칙은 한 번 작성되어 수백만 개의 영역에 배포되므로 이러한 정규식을 컴파일하고 메모리에 캐싱하면 이점이 있습니다. 이렇게 하면 프로세스가 다시 시작될 때까지 다시 컴파일할 필요가 없으므로 CPU 사이클이 절약됩니다.

악의적인 페이로드 로깅 컴파일러는 동적 크기의 배열 또는 벡터를 많이 사용하여 이러한 로그의 중간 상태를 저장합니다. [_smallvec_](https://docs.rs/smallvec/latest/smallvec/) 과 같은 크레이트는 힙 할당을 줄이는 데 사용되기도 합니다. 

### 악명 높은 “TRACKATED” 값

고객의 악의적인 페이로드 로그에 [_"잘린"_](https://github.com/cloudflare/matched-data-cli/blob/master/src/main.rs#L124-L129) 오류가 나타나는 경우가 있습니다. 모든 방화벽 이벤트에는 바이트 단위의 크기 제한이 있기 때문입니다. 이 제한을 초과하면 악의적인 페이로드 로그가 잘립니다. 

**악의적인 페이로드 로그(이전)**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2824 Image 4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48J7MQGP7PCNMTP177031B.png&w=715&h=263&f=webp&fit=cover&position=center)

**악의적인 페이로드 로그(신규)**

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2824 Image 5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4691SKC78119QZPYV3AP2N.png&w=715&h=298&f=webp&fit=cover&position=center)

저희는 악의적인 페이로드 로그의 p50바이트 크기가 1.5KB에서 500바이트로 67% 감소한 것을 확인했습니다! 즉, 잘린 악의적인 페이로드 로그가 줄어듭니다.

### 다음은?

저희는 현재 값을 표현하기 [_위해 utf-8 문자열의 손실 표현을 사용하고 있습니다._](https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8_lossy) 이는 멀티미디어와 같이 유효하지 않은 utf-8 문자열이 [_U+FFFD 유니코드 대체 문자_](https://doc.rust-lang.org/std/char/constant.REPLACEMENT_CHARACTER.html)로 표시됨을 의미합니다. 이진 데이터에 대해 작동하는 규칙의 경우 이러한 값의 무결성은 바이트 배열 또는 다른 직렬화 형식으로 유지되어야 합니다.

악의적인 페이로드 로깅의 스토리지 형식은 JSON입니다. [_CBOR_](https://cbor.io/), [_Cap'n Proto_](https://capnproto.org/), [_Protobuf_](https://protobuf.dev/) 등의 다른 바이너리 형식과 함께 이를 벤치마킹하여 처리 시간을 얼마나 많이 절약하는지 파이프라인을 절약할 예정입니다. 이는 바이너리 형식이 이전 버전과 호환되도록 정의된 스키마를 유지하는 데 도움이 될 수 있다는 추가적인 이점과 함께 로그를 고객에게 더 빠르게 전달하는 데 도움이 될 것입니다. 

마지막으로, 악의적인 페이로드 로깅은 관리형 규칙에서만 작동합니다. 이는 사용자 지정 규칙, WAF attack score, 콘텐츠 스캐닝, [_Firewall for AI_](https://developers.cloudflare.com/waf/detections/firewall-for-ai/) 등과 같은 다른 Cloudflare WAF 제품에도 적용될 것입니다.   
  
_AI용 방화벽에서 감지한, PII가 포함된 프롬프트를 보여주는 페이로드 로깅의 예:_

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2824 Image 6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZZPWYSTQ64D6QH4CYR90.png&w=715&h=162&f=webp&fit=cover&position=center)

## 흥분해야 하는 이유는 무엇일까요?

WAF가 취한 조치를 볼 수 있게 되므로 고객은 규칙이나 구성이 정확히 예상대로 작동하는지 확인할 수 있습니다. 악의적인 페이로드 로깅의 특이성을 개선하는 것은 이러한 방향으로 한 걸음 더 나아가고 있으며, 안정성, 대기 시간 및 더 많은 WAF 제품으로의 확장을 위해 추가로 개선할 계획입니다.

이는 JSON 스키마의 주요 변경 사항이므로 [_적절한 문서_](https://developers.cloudflare.com/changelog/2025-05-08-improved-payload-logging/)와 함께 고객에게 천천히 배포했습니다.

페이로드 로깅을 시작하고 활성화하려면 [_개발자 문서를 방문하세요_](https://developers.cloudflare.com/waf/managed-rules/payload-logging/#turn-on-payload-logging). 

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwaf-payload-logging%2F&t=%EC%95%85%EC%9D%98%EC%A0%81%EC%9D%B8%20%ED%8E%98%EC%9D%B4%EB%A1%9C%EB%93%9C%20%EB%A1%9C%EA%B9%85%EC%9C%BC%EB%A1%9C%20WAF%EC%9D%98%20%EA%B0%80%EC%8B%9C%EC%84%B1%20%EA%B0%9C%EC%84%A0)[](https://x.com/intent/post?text=%EC%95%85%EC%9D%98%EC%A0%81%EC%9D%B8+%ED%8E%98%EC%9D%B4%EB%A1%9C%EB%93%9C+%EB%A1%9C%EA%B9%85%EC%9C%BC%EB%A1%9C+WAF%EC%9D%98+%EA%B0%80%EC%8B%9C%EC%84%B1+%EA%B0%9C%EC%84%A0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwaf-payload-logging%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwaf-payload-logging%2F)[](https://bsky.app/intent/compose?text=%EC%95%85%EC%9D%98%EC%A0%81%EC%9D%B8+%ED%8E%98%EC%9D%B4%EB%A1%9C%EB%93%9C+%EB%A1%9C%EA%B9%85%EC%9C%BC%EB%A1%9C+WAF%EC%9D%98+%EA%B0%80%EC%8B%9C%EC%84%B1+%EA%B0%9C%EC%84%A0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwaf-payload-logging%2F)[](https://mastodonshare.com/?text=%EC%95%85%EC%9D%98%EC%A0%81%EC%9D%B8+%ED%8E%98%EC%9D%B4%EB%A1%9C%EB%93%9C+%EB%A1%9C%EA%B9%85%EC%9C%BC%EB%A1%9C+WAF%EC%9D%98+%EA%B0%80%EC%8B%9C%EC%84%B1+%EA%B0%9C%EC%84%A0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwaf-payload-logging%2F)[](https://www.threads.net/intent/post?text=%EC%95%85%EC%9D%98%EC%A0%81%EC%9D%B8+%ED%8E%98%EC%9D%B4%EB%A1%9C%EB%93%9C+%EB%A1%9C%EA%B9%85%EC%9C%BC%EB%A1%9C+WAF%EC%9D%98+%EA%B0%80%EC%8B%9C%EC%84%B1+%EA%B0%9C%EC%84%A0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fwaf-payload-logging%2F)

## 관련 태그

[WAF](https://blog.cloudflare.com/ko-kr/tag/waf/)[로깅](https://blog.cloudflare.com/ko-kr/tag/logging/)[방화벽](https://blog.cloudflare.com/ko-kr/tag/firewall/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)

  * ![Paschal Obba](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48YJYHP0864S3RA6Z3GTZE.jpeg&w=64&h=64&f=webp&fit=cover&position=center)[Paschal Obba](https://blog.cloudflare.com/ko-kr/author/paschal/)

[](https://paschal.dev)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
