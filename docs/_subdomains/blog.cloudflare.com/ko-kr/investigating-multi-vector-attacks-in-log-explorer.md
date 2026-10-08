---
url: https://blog.cloudflare.com/ko-kr/investigating-multi-vector-attacks-in-log-explorer/
title: Log Explorer\uc758 \uba40\ud2f0 \ubca1\ud130 \uacf5\uaca9 \uc870\uc0ac | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:51:35.978573+00:00
---

# Log Explorer의 멀티 벡터 공격 조사 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/investigating-multi-vector-attacks-in-log-explorer/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Analytics](https://blog.cloudflare.com/ko-kr/tag/analytics/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[SIEM](https://blog.cloudflare.com/ko-kr/tag/siem/)+55개의 태그 더 보기

8개 태그8개 태그 보기

  * 게시물 태그
  * [Analytics](https://blog.cloudflare.com/ko-kr/tag/analytics/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[SIEM](https://blog.cloudflare.com/ko-kr/tag/siem/)[로그](https://blog.cloudflare.com/ko-kr/tag/logs/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[스토리지](https://blog.cloudflare.com/ko-kr/tag/storage/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)[클라우드 연결성](https://blog.cloudflare.com/ko-kr/tag/connectivity-cloud/)
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



[로그](https://blog.cloudflare.com/ko-kr/tag/logs/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[스토리지](https://blog.cloudflare.com/ko-kr/tag/storage/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)[클라우드 연결성](https://blog.cloudflare.com/ko-kr/tag/connectivity-cloud/)

[Analytics](https://blog.cloudflare.com/ko-kr/tag/analytics/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[SIEM](https://blog.cloudflare.com/ko-kr/tag/siem/)[로그](https://blog.cloudflare.com/ko-kr/tag/logs/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[스토리지](https://blog.cloudflare.com/ko-kr/tag/storage/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)[클라우드 연결성](https://blog.cloudflare.com/ko-kr/tag/connectivity-cloud/)

2026년 3월 10일

# Log Explorer의 멀티 벡터 공격 조사

![Jen Sells](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49JMAH0P8SVDYZSBSAS4EK.JPG&w=64&h=64&f=webp&fit=cover&position=center)![Claudio Jolowicz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456R2CFXKBCA2T8XEE5FMB.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nico Gutierrez](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HB96WV2J3TRWVDQY4X8E.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jen Sells](https://blog.cloudflare.com/ko-kr/author/jen-sells/), [Claudio Jolowicz](https://blog.cloudflare.com/ko-kr/author/claudio/) 및 [Nico Gutierrez](https://blog.cloudflare.com/ko-kr/author/nico-gutierrez/)

9분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/investigating-multi-vector-attacks-in-log-explorer/) 및 [日本語](https://blog.cloudflare.com/ja-jp/investigating-multi-vector-attacks-in-log-explorer/).

![BLOG-3164 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44T2Y7DY06GACRR2JF6RQM.png&w=1999&h=1126&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////798PHz5uru5+3x7/P28vPy7+3p/////vv96+zz3OLt3uXx5+z27u/z7erp/////vr/5+j01Nvu1d7z4ej36+z07enq//////3/6en41dzy1d/24+n77e/48O3u////////8fL+4Ob44en97fP/9vf+9/T1/////////v//8PX/8vj/+/////////37/////////////v//////////////////////////////////////////////////)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

사이버 보안의 세계에서 단일 데이터 포인트가 전부인 경우는 드뭅니다. 최신 공격자는 단순히 현관문을 두드리는 것이 아닙니다. 이들은 API를 탐색하고, "잡음"으로 네트워크를 집중시켜 팀의 주의를 분산시키고, 훔친 자격 증명을 사용하여 응용 프로그램과 서버를 탐색합니다.

이러한 멀티 벡터 공격을 차단하려면 전체적인 그림이 필요합니다. Cloudflare Log Explorer를 사용하여 보안 포렌식을 수행하면 14개의 새로운 데이터 세트 통합을 통해 360도 가시성을 얻을 수 있으며 이 데이터 세트는 Cloudflare의 애플리케이션 서비스 및 Cloudflare One 제품 포트폴리오의 전체 표면을 포괄합니다. 애플리케이션 계층 HTTP 요청, 네트워크 계층 DDoS 및 방화벽 로그, Zero Trust 액세스 이벤트의 원격 측정 결과를 상호 연관시킴으로써 보안 분석가는 평균 감지 시간(MTTD)을 크게 줄이고 정교한 다중 계층 공격을 효과적으로 파악할 수 있습니다.

Log Explorer가 신속하고 심층적인 포렌식을 위한 최고의 환경을 보안 팀에 제공하는 방법에 대해 자세히 알아보려면 계속 읽어보세요.

## 전체 스택을 위한 Flight Recorder

현대의 디지털 환경에서는 여러 공격 벡터를 사용하여 공격자를 방어하기 위해 상호 연관되어 있는 심층적 원격 측정이 필요합니다. 원시 로그는 애플리케이션의 '플라이트 기록 장치' 역할을 하여 모든 단일 상호작용, 공격 시도, 성능 병목 현상을 캡처합니다. 그리고 Cloudflare는 귀사의 사용자와 서버 사이의 에지에 위치하므로, 이러한 모든 이벤트는 요청이 귀사의 인프라에 도달하기도 전에 기록됩니다. 

Cloudflare Log Explorer는 이러한 로그를 통합 인터페이스로 중앙 집중화하여 신속하게 조사할 수 있습니다.

### 지원되는 로그 유형

#### 영역 범위 로그

 _초점: 웹 사이트 트래픽, 보안 이벤트, 에지 성능._

HTTP 요청| 가장 포괄적인 데이터 세트로서 모든 애플리케이션 계층 트래픽의 "기본 레코드" 역할을 하여 세션 활동, 악용 시도, 봇 패턴을 재구성할 수 있습니다.  
---|---  
Firewall Events| 차단되거나 인증된 위협에 대한 중요한 증거를 제공하여 분석가가 공격을 차단한 특정 WAF 규칙, IP 평판 또는 사용자 지정 필터를 식별할 수 있도록 합니다.  
DNS 로그| 권한 있는 에지에서 해결된 모든 쿼리를 추적하여 캐시 포이즈닝 시도, 도메인 하이재킹, 인프라 수준 정찰을 식별합니다.  
NEL(Network Error Logging) 보고서| 클라이언트 측 브라우저 오류를 추적하여 애플리케이션 계층 DDoS 공격과 합법적 네트워크 연결 문제를 구분합니다.  
Spectrum Events| 비 웹 앱의 경우, 이러한 로그는 L4 트래픽(TCP/UDP)에 대한 가시성을 제공하여 SSH, RDP 또는 사용자 지정 게임 트래픽과 같은 프로토콜에 대한 이상 징후나 무차별 대입 공격을 식별하는 데 도움이 됩니다.  
Page Shield| JavaScript, 아웃바운드 연결 등 사이트의 클라이언트 측 환경에 대한 무단 변경을 추적하고 감사합니다.  
Zaraz 이벤트| 개인정보 보호 규정 준수를 감사하고 승인되지 않은 스크립트 동작을 감지하는 데 필수적인 타사 도구와 트래커가 사용자 데이터와 상호 작용하는 방식을 살펴보세요.  
  
#### 계정 범위 로그

 _초점: 내부 보안, Zero Trust, 관리 변경, 네트워크 활동._

액세스 요청| ID 기반 인증 이벤트를 추적하여 특정 내부 애플리케이션에 액세스한 사용자와 이러한 시도가 승인되었는지 여부를 확인합니다.  
---|---  
감사 로그| Cloudflare 대시보드 내에서 구성 변경 추적을 제공하여 승인되지 않은 관리 작업 또는 수정을 식별할 수 있습니다.  
CASB 결과| SaaS 애플리케이션(Google Drive 또는 Microsoft 365 등) 내에서 잘못된 보안 구성 및 데이터 위험을 식별하여 무단 데이터 노출을 방지합니다.  
Magic Transit / IPSec 로그| 네트워크 엔지니어가 터널 상태 검토 및 BGP 라우팅 변경 사항 확인 등 네트워크 수준(L3) 모니터링을 수행할 수 있도록 지원합니다.  
브라우저 격리 로그| 격리된 브라우저 세션 내 사용자 작업(예: 복사-붙여넣기, 인쇄, 파일 업로드)을 추적하여 신뢰할 수 없는 사이트로의 데이터 유출 방지   
장치 상태 결과 | 네트워크에 연결하는 장치의 보안 상태 및 규제 준수 상태에 대해 자세히 설명하여 손상되거나 규제를 준수하지 않는 엔드포인트를 파악하는 데 도움이 됩니다.  
DEX 애플리케이션 테스트 | 사용자 관점에서 애플리케이션 성능을 모니터링하여 보안 관련 중단과 표준 성능 저하를 구분하는 데 도움을 줍니다.  
DEX 장치 상태 이벤트| 사용자 장치의 물리적 상태에 대한 원격 측정을 제공하여 하드웨어 또는 OS 수준의 이상 징후를 잠재적인 보안 사고와 연관시키는 데 유용합니다.  
DNS 방화벽 로그| DNS 방화벽을 통해 필터링된 DNS 쿼리를 추적하여 알려진 악의적 도메인 또는 명령 및 제어(C2) 서버와의 통신을 식별합니다.  
Email Security 경고| 게이트웨이에서 감지된 악의적 이메일 활동과 피싱 시도를 기록하여 이메일 기반 항목 벡터의 출처를 추적합니다.  
Gateway DNS| 네트워크에서 사용자가 수행하는 모든 DNS 쿼리를 모니터링하여 섀도우 IT, 맬웨어 콜백, 도메인 생성 알고리즘(DGA)을 식별합니다.  
게이트웨이 HTTP| 암호화 및 암호화되지 않은 웹 트래픽에 대한 완전한 가시성을 제공하여 숨겨진 악의적인 페이로드, 악의적인 파일 다운로드, 승인되지 않은 SaaS 사용을 감지합니다.  
Gateway 네트워크| L3/L4 네트워크 트래픽(비 HTTP)을 추적하여 무단 포트 사용, 프로토콜 이상, 네트워크 내 내부망 이동을 식별합니다.  
IPSec 로그| 암호화된 사이트 간 터널의 상태 및 트래픽을 모니터링하여 보안 네트워크 연결의 무결성과 가용성을 보장합니다.  
Magic IDS 감지| 침입 감지 시그니처와 일치하는 항목을 검사하여 네트워크를 통과하는 알려진 익스플로잇 패턴 또는 맬웨어 동작을 조사자에게 경고합니다.  
네트워크 Analytics 로그| 패킷 수준 데이터에 대한 높은 수준의 가시성을 제공하여 특정 인프라를 겨냥한 볼류메트릭 DDoS 공격 또는 비정상적인 트래픽 급증을 식별합니다.  
싱크홀 HTTP 로그| "싱크홀된" IP 주소로 향하는 트래픽을 캡처하여 어떤 내부 장치가 알려진 봇넷 인프라와 통신을 시도하는지 확인합니다.  
WARP 구성 변경 사항| 최종 사용자 장치에서 WARP 클라이언트 설정에 대한 수정 사항을 추적하여 보안 에이전트가 변조되거나 비활성화되지 않았는지 확인합니다.  
WARP 토글 변경 사항| 사용자가 언제 보안 연결을 활성화 또는 비활성화할지 구체적으로 기록하여, 장치가 보호되지 않았을 수 있는 기간을 파악하는 데 도움이 됩니다.  
Zero Trust 네트워크 세션 로그| 인증된 사용자 세션의 지속 시간과 상태를 기록하여 보호된 경계 내에서 사용자 액세스의 전체 수명 주기를 파악합니다.  
  
## 모든 단계에서 악의적인 활동을 식별할 수 있는 Log Explorer

**HTTP 요청** , **방화벽 이벤트** , **DNS 로그** 를 통해 세밀한 애플리케이션 계층 가시성을 확보하여 공개 자산에 트래픽이 어떻게 전달되는지 정확히 확인하세요. Track internal movement with **Access Requests** , **Gateway logs** , and **감사 로그**. 자격 증명이 훼손되면 어디로 갔는지 확인할 수 있습니다. **Magic IDS** 및 **Network Analytics 로그** 를 사용하여 사설 네트워크 내의 볼류메트릭 공격 및 "동-서" 내부망 이동을 발견합니다.

### 정찰 활동 식별

공격자는 스캐너 등의 도구를 사용하여 진입점, 숨겨진 디렉터리, 소프트웨어 취약점을 찾습니다. 이를 식별하려면 Log Explorer를 사용하여 단일 IP에서 발생하는 401, 403,404의 `EdgeResponseStatus` 코드 또는 중요한 경로(예: `http_requests)에` 대한 요청을 쿼리할 수 있습니다. `/.env`, `/.git`, `/wp-admin`)입니다. 

또한, `magic_ids_detections` 로그는 네트워크 계층에서 스캐닝을 식별하는 데 사용될 수도 있습니다. 이러한 로그를 통해 네트워크를 노리는 위협에 대한 패킷 수준의 가시성을 확보할 수 있습니다. 표준 HTTP 로그와 달리 이러한 로그는 네트워크 및 전송 계층(IP, TCP, UDP)에서의 **서명 기반 감지** 에 중점을 둡니다. 단일 `SourceIP` 가 짧은 시간 내에 광범위한 `DestinationPort` 값에 걸쳐 여러 고유한 감지를 트리거하는 경우를 발견하는 쿼리입니다. Magic IDS 시그니처는 특히 Nmap 스캔, SYN 은폐 스캔 등의 활동에 플래그를 지정할 수 있습니다.

### 유용 확인

공격자는 정찰을 수행하는 동안 동시 네트워크 폭주로 이를 위장하려고 시도할 수 있습니다. `network_analytics_logs` 로 전환하여 볼류메트릭 공격이 연막으로 사용되고 있는지 확인하세요.

### 접근 방식 식별 

공격자는 잠재적인 취약점을 식별하면 무기를 만들기 시작합니다. 공격자는 악의적인 페이로드(예: SQL 삽입 또는 대규모/손상된 파일 업로드)을 통해 취약점을 확인합니다. `http_requests` 및/또는 `fw_events` 를 검토하여 트리거된 Cloudflare 감지 도구가 있는지 확인하세요. Cloudflare에서는 이러한 데이터 세트에 보안 신호를 기록하여 `WAFAttackScore`, `WAFSQLiAttackScore`, `FraudAttack`, `ContentScanJobResults` 등의 필드를 사용하여 악의적인 페이로드가 포함된 요청을 쉽게 식별할 수 있습니다. [_당사 설명서_](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) 를 검토하여 이러한 필드를 완전히 이해하세요. `fw_events` 로그를 이용해, `action`, `source`, `ruleID` 필드를 검사하여 이러한 요청이 Cloudflare의 방어 시스템을 통과했는지 여부를 판단할 수 있습니다. Cloudflare의 관리형 규칙은 기본적으로 이러한 페이로드를 대부분 차단합니다. 애플리케이션 보안 개요를 검토하여 애플리케이션이 보호되고 있는지 확인하세요.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Showing the Managed rules Insight that displays on Security Overview if the current zone does not have Managed Rules enabled](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Z4WGGKCCC271C8VZ259Q.png&w=715&h=79&f=webp&fit=cover&position=center)

_현재 영역에 관리형 규칙이 활성화되어 있지 않은 경우 보안 개요에 표시되는 관리형 규칙 인사이트 표시_

### ID 감사

의심스러운 IP가 로그인에 성공했을까요? `ClientIP` 를 사용하여 `access_requests`를 검색하세요. 중요한 내부 앱에 대해 "`결정: 허용`"이 표시되면 계정이 손상된 것입니다.

### 유출 방지(데이터 유출)

공격자는 때때로 DNS 터널링을 사용하여 중요한 데이터(예: 비밀번호 또는 SSH 키)를 DNS 쿼리로 인코딩하여 방화벽을 우회합니다. `google.com`과 같은 일반적인 요청 대신 로그에 길고 인코딩된 문자열이 표시됩니다. 다음 필드를 검사하여 고유하고 길고 엔트로피가 높은 하위 도메인에 대해 비정상적으로 많은 양의 쿼리를 찾아냅니다. `QueryName`: [`_h3ldo293js92.example.com_`](http://h3ldo293js92.example.com)과 같은 문자열을 찾습니다. `QueryType`: 페이로드를 전달하기 위해 `TXT`, `CNAME` 또는 `NULL` 레코드를 자주 사용하며, `ClientIP`: 단일 내부 호스트에서 이러한 고유한 요청을 수천 건 생성 중인지 식별합니다.

또한 공격자는 중요한 데이터를 비표준 프로토콜 내에 숨기거나 DNS 또는 ICMP와 같은 일반적인 프로토콜을 비정상적인 방식으로 사용하여 표준 방화벽을 우회하는 방식으로 중요한 데이터 유출을 시도할 수 있습니다. `magic_ids_detections` 로그를 쿼리하여 `SignatureMessage`에서 "ICMP 터널링" 또는 "DNS 터널링" 감지와 같은 프로토콜 이상을 알리는 시그니처를 찾아 이를 알아보세요.

zero-day 취약점을 조사하든 정교한 봇넷을 추적하든, 이제 필요한 데이터를 손쉽게 이용할 수 있습니다.

## 데이터세트 간의 상관 관계

여러 동시 검색 사이를 전환하여 여러 데이터세트에서 악의적인 활동을 조사합니다. 이제 Log Explorer의 새로운 탭 기능을 사용하여 다수의 쿼리에 대해 동시에 작업할 수 있습니다. 탭 간을 전환하여 다른 데이터 세트를 쿼리하거나 쿼리 결과를 통해 필터링을 사용하거나 피봇하고 쿼리를 조정합니다.

여러 Cloudflare 로그 소스에서 데이터의 상관 관계를 파악하면, 멀리 떨어져서는 문제가 없는 정교한 다단계 공격을 감지할 수 있습니다. 이 교차 데이터 세트 분석을 통해 정찰부터 유출까지 전체 공격 체인을 확인할 수 있습니다.

### 세션 하이재킹(토큰 도용)

**시나리오:** 사용자가 Cloudflare Access를 통해 인증하지만, 후속 HTTP_request 트래픽이 봇처럼 보입니다.

**1단계:** `http_requests`에서 고위험 세션을 식별합니다.
    
    
    SELECT RayID, ClientIP, ClientRequestUserAgent, BotScore
    FROM http_requests
    WHERE date = '2026-02-22' 
      AND BotScore < 20 
    LIMIT 100

**2단계:** `RayID`를 복사하고 `access_requests`를 검색하여 어떤 사용자 계정이 의심스러운 봇 활동과 연관되어 있는지 확인합니다.
    
    
    SELECT Email, IPAddress, Allowed
    FROM access_requests
    WHERE date = '2026-02-22' 
      AND RayID = 'INSERT_RAY_ID_HERE'

### 피싱 이후의 C2 비커닝

**시나리오:** 한 직원이 피싱 이메일에 있는 링크를 클릭하여 워크스테이션을 손상시켰습니다. 이 워크스테이션은 알려진 악의적 도메인에 대한 DNS 쿼리를 전송한 후 즉시 IDS 경고를 트리거합니다.

**1단계:** Email_security_alerts에 위반 사항이 있는지 검사하여 피싱 공격을 찾습니다. 
    
    
    SELECT Timestamp, Threatcategories, To, Alertreason
    FROM email_security_alerts
    WHERE date = '2026-02-22' 
      AND Threatcategories LIKE 'phishing'

**2단계:** Access 로그를 사용하여 사용자의 이메일(수신자)과 IP 주소의 상관 관계를 파악합니다.
    
    
    SELECT Email, IPAddress
    FROM access_requests
    WHERE date = '2026-02-22' 

**3단계:** `gateway_dns` 로그에서 특정 악성 도메인을 쿼리하는 내부 IP를 찾습니다.
    
    
    SELECT SrcIP, QueryName, DstIP, 
    FROM gateway_dns
    WHERE date = '2026-02-22' 
      AND SrcIP = 'INSERT_IP_FROM_PREVIOUS_QUERY'
      AND QueryName LIKE '%malicious_domain_name%'

### 내부망 이동(액세스 → 네트워크 탐색)

**시나리오:** 사용자가 Zero Trust를 통해 로그인한 다음 내부 네트워크 검사를 시도합니다.

**1단계:** `access_requests`에서 예기치 않은 위치로부터 성공적인 로그인을 찾습니다.
    
    
    SELECT IPAddress, Email, Country
    FROM access_requests
    WHERE date = '2026-02-22' 
      AND Allowed = true 
      AND Country != 'US' -- Replace with your HQ country

**2단계:** `Magic_ids_detections에서` `IPAddress가` 네트워크 수준 서명을 트리거하고 있는지 확인합니다.
    
    
    SELECT SignatureMessage, DestinationIP, Protocol
    FROM magic_ids_detections
    WHERE date = '2026-02-22' 
      AND SourceIP = 'INSERT_IP_ADDRESS_HERE'

### 더 많은 데이터를 위한 문 열기 

Log Explorer는 처음부터 확장성을 염두에 두고 설계되었습니다. 모든 데이터세트 스키마는 JSON 데이터의 구조와 유형을 설명하기 위해 널리 채택되는 표준인 JSON 스키마를 사용하여 정의됩니다. 이러한 설계상의 결정으로 HTTP 요청 및 방화벽 이벤트를 넘어 Cloudflare의 원격 측정을 모든 범위로 쉽게 확장할 수 있었습니다. 초기 데이터 세트를 구동하는 것과 동일한 스키마 기반 접근 방식은 Zero Trust 로그, 네트워크 분석, 이메일 보안 경고 등 모든 것을 수용할 수 있도록 자연스럽게 확장되었습니다.

더 중요한 것은 이러한 표준화를 통해 Cloudflare의 기본 원격 측정을 넘어 데이터를 수집할 수 있는 문이 열리게 된다는 점입니다. 우리의 수집 파이프라인은 하드 코딩되지 않고 스키마 기반이므로 JSON 형식으로 표현할 수 있는 모든 정형 데이터를 받아들일 수 있습니다. 하이브리드 환경을 관리하는 보안 팀의 경우, 이는 Log Explorer가 궁극적으로 Cloudflare의 에지 원격 측정을 동일한 SQL 인터페이스를 통해 쿼리할 수 있는 타사 소스의 로그와 상관 관계를 지정하는 단일 창 역할을 할 수 있음을 의미합니다. 오늘 발표에서는 Cloudflare의 제품 포트폴리오를 마무리하는 데 초점을 맞추지만, 고객이 맞춤형 스키마로 자체 데이터 소스를 가져올 수 있는 미래를 위한 아키텍처 기반이 마련됩니다.

### 더 빠른 데이터, 더 빠른 대응: 아키텍처 업그레이드

멀티 벡터 공격을 효과적으로 조사하려면 타이밍이 관건입니다. 가용성 로그가 몇 분 지연되어도 사전 방어와 사후 피해 대응의 차이가 날 수 있습니다.

따라서 속도와 복원력을 향상할 수 있도록 수집을 최적화했습니다. 수집 경로의 한 부분에서 동시성을 증가시킴으로써 "시끄러운 이웃" 문제를 일으킬 수 있는 병목 현상을 제거하여 한 클라이언트의 데이터 급증으로 다른 클라이언트의 가시성이 저하되지 않도록 했습니다. 이러한 아키텍처 작업을 통해 P99 수집 대기 시간을 약 55% 단축하고 P50 수집 대기 시간을 25% 단축하여 에지에서 이벤트가 사용자의 SQL 쿼리에 도달하는 데 걸리는 시간이 단축되었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Grafana chart displaying the drop in ingest latency after architectural upgrades](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46E6JRTK5WZV8TQXJ49P3R.png&w=715&h=315&f=webp&fit=cover&position=center)

_아키텍처 업그레이드 후 수집 대기 시간 감소를 보여주는 Grafana 차트_

## 팔로우하여 더 많은 업데이트를 받아보세요

이제 겨우 시작일 뿐입니다. Log Explorer의 경험을 개선하기 위해, 사용자가 정의한 일정에 이러한 감지 쿼리를 실행하는 기능을 포함하여 더욱 강력한 기능을 적극적으로 개발하고 있습니다. 

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Scheduled Queries List](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456P12SSMET3N8VJFCQH67.png&w=715&h=432&f=webp&fit=cover&position=center)

 _출시 예정인 Log Explorer의 예약 쿼리 기능 목업 설계_

[ _블로그를 구독_](https://blog.cloudflare.com/) 하고 [_변경 로그_](https://developers.cloudflare.com/changelog/product/log-explorer/)에서 곧 더 많은 Log Explorer 업데이트를 기대해 주세요. 

## Log Explorer에 액세스

Log Explorer에 액세스하려면 대시보드에서 직접 셀프 서비스를 구매하거나, 계약 고객의 경우 [_상담_](https://www.cloudflare.com/application-services/products/log-explorer/) 을 위해 연락하거나 계정 관리자에게 문의할 수 있습니다. 또한 [_개발자 문서_](https://developers.cloudflare.com/logs/log-explorer/)에서 자세한 내용을 확인할 수 있습니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Finvestigating-multi-vector-attacks-in-log-explorer%2F&t=Log%20Explorer%EC%9D%98%20%EB%A9%80%ED%8B%B0%20%EB%B2%A1%ED%84%B0%20%EA%B3%B5%EA%B2%A9%20%EC%A1%B0%EC%82%AC)[](https://x.com/intent/post?text=Log+Explorer%EC%9D%98+%EB%A9%80%ED%8B%B0+%EB%B2%A1%ED%84%B0+%EA%B3%B5%EA%B2%A9+%EC%A1%B0%EC%82%AC&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://bsky.app/intent/compose?text=Log+Explorer%EC%9D%98+%EB%A9%80%ED%8B%B0+%EB%B2%A1%ED%84%B0+%EA%B3%B5%EA%B2%A9+%EC%A1%B0%EC%82%AC+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://mastodonshare.com/?text=Log+Explorer%EC%9D%98+%EB%A9%80%ED%8B%B0+%EB%B2%A1%ED%84%B0+%EA%B3%B5%EA%B2%A9+%EC%A1%B0%EC%82%AC&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)[](https://www.threads.net/intent/post?text=Log+Explorer%EC%9D%98+%EB%A9%80%ED%8B%B0+%EB%B2%A1%ED%84%B0+%EA%B3%B5%EA%B2%A9+%EC%A1%B0%EC%82%AC+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Finvestigating-multi-vector-attacks-in-log-explorer%2F)

## 관련 태그

[Analytics](https://blog.cloudflare.com/ko-kr/tag/analytics/)[R2](https://blog.cloudflare.com/ko-kr/tag/r2/)[SIEM](https://blog.cloudflare.com/ko-kr/tag/siem/)[로그](https://blog.cloudflare.com/ko-kr/tag/logs/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[스토리지](https://blog.cloudflare.com/ko-kr/tag/storage/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)[클라우드 연결성](https://blog.cloudflare.com/ko-kr/tag/connectivity-cloud/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
