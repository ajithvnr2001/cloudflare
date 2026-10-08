---
url: https://blog.cloudflare.com/ko-kr/how-we-built-spectrum/
title: \ub9ac\ub205\uc2a4 \ubc29\ud654\ubcbd\uc744 \ub0a8\uc6a9\ud558\uae30: Spectrum \uc744 \ub9cc\ub4e4 \uc218 \uc788\uc5c8\ub358 \u200b\ud574\ud0b9\u200b | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:48:24.629001+00:00
---

# 리눅스 방화벽을 남용하기: Spectrum 을 만들 수 있었던 ​해킹​ | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/how-we-built-spectrum/

[블로그](https://blog.cloudflare.com/ko-kr/)

[DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[Spectrum](https://blog.cloudflare.com/ko-kr/tag/spectrum/)+33개의 태그 더 보기

6개 태그6개 태그 보기

  * 게시물 태그
  * [DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[Spectrum](https://blog.cloudflare.com/ko-kr/tag/spectrum/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)
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



[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)

[DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[Spectrum](https://blog.cloudflare.com/ko-kr/tag/spectrum/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)

2018년 4월 12일

# 리눅스 방화벽을 남용하기: Spectrum 을 만들 수 있었던 ​해킹​

![Marek Majkowski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44F10W94YWR7RW8E70MQW4.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Marek Majkowski](https://blog.cloudflare.com/ko-kr/author/marek-majkowski/)

7분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/how-we-built-spectrum/), [Deutsch](https://blog.cloudflare.com/de-de/how-we-built-spectrum/), [Español](https://blog.cloudflare.com/es-es/how-we-built-spectrum/), [Français](https://blog.cloudflare.com/fr-fr/how-we-built-spectrum/), [日本語](https://blog.cloudflare.com/ja-jp/how-we-built-spectrum/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/how-we-built-spectrum/).

![13334109713_0b32435032_z](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44E12BDNQKMKCCGSM4BXZA.jpg&w=640&h=425&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAmZacm5menJyglpebioqQg4KKioqRmJqflZCUlpKWlJOViomLeHZ6cGx0f3yDlZWYjoeKjomKioiGenh2YFpdV0tUcWpvj42Ph3+Bh4GBgn98cG1pUEdIQy46ZFpgh4SFgXp8gn19f357cG9sVk9RSDZEX1RefXl8fHd8fnx+gIKBeXt6aWZrXFJgYlpncnB3eXd+fX2Cg4eIg4eIenqAbWh2Z2Jyamp0eHd/fX6DhYqLh4yOgIGIdHB+amZ2Z2h0)

* * *

얼마전 우리는 [Spectrum을 발표](https://blog.cloudflare.com/spectrum/)하였습니다: 어떤 TCP 기반의 프로토콜이라도 DDoS 방어, 로드밸런싱 그리고 컨텐츠 가속을 할 수 있는 새로운 Cloudflare의 기능입니다.

[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/) [image](https://www.flickr.com/photos/liftarn/13334109713) by [Staffan Vilcans](https://www.flickr.com/photos/liftarn)

Spectrum을 만들기 시작하고 얼마 되지 않아서 중요한 기술적 난관에 부딛히게 되었습니다: Spectrum은 1부터 65535 사이의 어떤 유효한 TCP 포트라도 접속을 허용해야 합니다. 우리의 리눅스 엣지 서버에서는 "_임의의_ 포트 번호에 인바운드 연결을 허용"은 불가능합니다. 이것은 리눅스만의 제한은 아닙니다: 이것은 대부분 운영 체제의 네트워크 어플리케이션의 기반인 BSD 소켓 API의 특성입니다. 내부적으로 Spectrum을 완성하기 위해서 풀어야 하는 서로 겹치는 문제가 둘 있었습니다:

  * 1에서 65535 사이의 모든 포트 번호에 TCP 연결을 어떻게 받아들일 것인가
  * 매우 많은 수의 IP 주소로 오는 연결을 받아들이도록 단일 리눅스 서버를 어떻게 설정할 것인가 (우리는 애니캐스트 대역에 수많은 IP주소를 갖고 있습니다)



### 서버에 수백만의 IP를 할당

Cloudflare의 엣지 서버는 거의 동일한 구성을 갖고 있습니다. 초창기에는 루프백 네트워크 인터페이스에 특정한 /32 (그리고 /128) IP 주소를 할당하였습니다[1]. 이것은 수십개의 IP주소만 갖고 있었을 때에는 잘 동작 하였지만 더 성장함에 따라 확대 적용하는 것에는 실패하였습니다.

그때 ["AnyIP" 트릭](https://blog.widodh.nl/2016/04/anyip-bind-a-whole-subnet-to-your-linux-machine/)이 등장하였습니다. AnyIP는 단일 주소가 아니라 전체 IP 프리픽스 (서브넷)을 루프백 인터페이스에 할당하도록 해 줍니다. 사실 AnyIP를 많이 사용하고 있습니다: 여러분 컴퓨터에는 루브백 인터페이스에 127.0.0.0/8 이 할당되어 있습니다. 컴퓨터의 관점에서 본다면 127.0.0.1 에서 127.255.255.254 사이의 모든 주소가 로컬 머신에 할당된 것입니다.
    
    
    ip route add local 192.0.2.0/24 dev lo

이 트릭은 127.0.0.1/8 대역 이외에도 적용 가능합니다. 192.0.2.0/24 전체를 로컬에 할당한 것처럼 보이게 하려면 다음을 실행하세요:
    
    
    nc -l 192.0.2.1 8080

다음으로 이 IP 주소 중 하나의 포트 8080에 바인딩하는 것도 문제 없습니다:
    
    
    ip route add local 2001:db8::/64 dev lo

IPv6 을 그렇게 동작하게 하는것은 조금 더 어렵습니다:

불행히도 v4 예제처럼 v6 IP주소를 그렇게 할당할 수는 없습니다. 이걸 하기 위해서는 추가적인 권한이 필요한 `IP_FREEBIND` 소켓 옵션을 사용해야 합니다. 완벽히 하자면 `net.ipv6.ip_nonlocal_bind` sysctl 이 있습니다만 수정하기 않기를 권장합니다.
    
    
    $ ip addr show
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
        inet 1.1.1.0/24 scope global lo
           valid_lft forever preferred_lft forever
        inet 104.16.0.0/16 scope global lo
           valid_lft forever preferred_lft forever
    ...

이 AnyIP 트릭은 각 서버에 로컬 인터페이스로 할당된 수백만의 IP 주소를 가능하게 합니다:

### 모든 포트에 바인딩

두번째로 큰 문제는 임의의 포트 번호에 TCP 소켓을 여는 기능입니다. 리눅스와 BSD 소켓 API를 지원하는 시스템에서는 일반적으로 하나의 `bind`시스템 콜로 특정 TCP 포트 번호에만 바인딩이 가능 합니다. 한번의 명령으로 여러 포트에 바인드하는 것은 가능하지 않습니다.

단순히 생각하면 가능한 65535 포트 각각에 대해 `bind`를 65535 번하는 것입니다. 물론 이것도 생각해 볼 수 있습니다만 끔찍한 결과를 초래할 수 있습니다:

  * [리스닝 소켓의 복수](https://blog.cloudflare.com/revenge-listening-sockets/)


    
    
    /* Yes, really, this is all you need. */
    #define INET_LHTABLE_SIZE       32

내부적으로 리눅스 커널은 리스닝 소켓을 포트 번호로 인덱싱된 해시 테이블 [LHTABLE](https://elixir.bootlin.com/linux/latest/source/include/net/inet_hashtables.h#L118) 에 저장하고 32 버킷을 사용 합니다.

6.5만개의 포트를 열게 된다면 이 테이블에서 찾는 것은 매우 느려집니다: 각각의 해시 테이블 버킷이 2천개의 아이템을 포함할 수 있기 때문입니다.

이 문제를 해결하는 또 다른 방법은 iptable 의 풍부한 NAT 기능을 사용하는 것입니다. 들어오는 패킷의 수신 주소를 특정 주소/포트로 바꾸어 쓰고 거기에서 어플리케이션이 바인드하고 있는 것입니다.

이 방법을 해 보지는 않았습니다만 그 이유는 iptables의 `conntrack`모듈이 필요하기 때문입니다. 예전에 우리는 [성능 문제가 되는 경우](http://patchwork.ozlabs.org/cover/810566/)를 찾아 내었고 `conntrack`은 우리가 접하게 되는 큰 DDoS 공격을 처리할 수 없습니다.

추가적으로 NAT방식으로는 수신자 IP 주소 정보를 잃어버릴 수 있습니다. 이 문제를 보완하기 위해서 `SO_ORIGINAL_DST`라는 잘 알려지지 않은 소켓 옵션이 있습니다만 [코드가 그렇게 좋아 보이지는 않습니다.](https://github.com/torvalds/linux/blob/b5dbc28762fd3fd40ba76303be0c7f707826f982/net/ipv4/netfilter/nf_conntrack_l3proto_ipv4.c)

다행히 6.5만개 포트에 모두 바인딩하거나 `conntrack`을 사용하지 않아도 문제를 해결할 방법이 있습니다.

### 구조용 방화벽

더 자세히 들어가기 전에 운영체제에서 네트워크 패킷의 일반적인 흐름에 대해 다시 알아봅시다.

공통적으로 수신 패킷 경로에는 두가지의 나뉘어진 계층이 있습니다:

  * IP 방화벽
  * 네트워크 스택



이것들은 개념적으로 별개입니다. IP 방화벽은 일반적으로 상태 없는 소프트웨어입니다(`conntrack`과 IP 조각 재조립은 일단 별개로 합시다). 방화벽은 IP 패킷을 분석해서 ACCEPT할지 DROP할지를 결정합니다. 참고로 이 계층은 _어플리케이션_이나 _소켓_이 아니라 _패킷_ 과 _포트 번호_에 대한 것입니다.

그리고 네트워크 스택이 있습니다. 이 괴물은 많은 상태를 관리합니다. 주된 작업은 IP패킷을 수신하여 _소켓_으로 보내는 것이며 이후 사용자 공간의 _어플리케이션_에 의해 처리됩니다. 네트워크 스택은 사용자 공간에서 공유되는 추상화 계층을 관리합니다. TCP 흐름을 재조립하고, 라우팅을 처리하며, 어떤 IP가 로컬인지를 판별합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![upload-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45V16KF1141QKP2QTJM6F1.jpg&w=640&h=360&f=webp&fit=cover&position=center)

### 마법의 먼지

Source: [still from YouTube](https://www.youtube.com/watch?v=9CS7j5I6aOc)
    
    
    TPROXY
    This target is only valid in the mangle table, in the 
    PREROUTING chain and user-defined chains which are only 
    called from this chain.  It redirects the packet to a local 
    socket without changing the packet header in any way. It can
    also change the mark value which can then be used in 
    advanced routing rules. 

그러다 `TPROXY` iptable 모듈을 만나게 되었습니다. [공식 문서](http://ipset.netfilter.org/iptables-extensions.man.html)는 지나치기 쉽습니다:

추가적인 문서는 커널에서 찾을 수 있습니다.

  * [docs/networking/tproxy.txt](https://www.kernel.org/doc/Documentation/networking/tproxy.txt)



더 생각해 볼 수도록 더 궁금하게 되었습니다.

그래서... 결국 `TPROXY`가 하는 일은 무엇일까요?

### 마술 트릭을 밝히자
    
    
    case NFT_LOOKUP_LISTENER:
      sk = inet_lookup_listener(net, &tcp_hashinfo, skb,
    				    ip_hdrlen(skb) +
    				      __tcp_hdrlen(tcph),
    				    saddr, sport,
    				    daddr, dport,
    				    in->ifindex, 0);

`TPROXY` 코드는 [놀랍게도 간단합니다](https://elixir.bootlin.com/linux/v4.16.1/source/net/netfilter/xt_TPROXY.c#L119):

이 내용을 다시 이야기 하면: 방화벽의 일부인 `iptables` 모듈에서 `inet_lookup_listener`를 호출합니다. 이 함수는 src/dst/port/IP 의 4개 튜플을 인수로 받으며 그 연결을 성립시킬 수 있는 리스닝 소켓을 리턴합니다. 이것은 네트워크 스택 소켓 처리의 핵심 기능입니다.

다시 말합니다: 방화벽 코드가 소켓 처리 함수를 부릅니다.
    
    
    skb->sk = sk;

이후 `TPROXY` [는 실제로 소켓 할당을 합니다](https://elixir.bootlin.com/linux/v4.16.1/source/net/netfilter/xt_TPROXY.c#L299):

이 행에서 `struct sock` 소켓을 수신 패킷에 할당하고 처리를 완료 합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![3649474619_3b800400e9_z-1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW475B6E6KWBFRMM268YX25R.jpg&w=640&h=424&f=webp&fit=cover&position=center)

### 모자에서 토끼를 끌어내자

[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/) [image](https://www.flickr.com/photos/angelaboothroyd/3649474619) by [Angela Boothroyd](https://www.flickr.com/photos/angelaboothroyd)
    
    
    # Set 192.0.2.0/24 to be routed locally with AnyIP.
    # Make it explicit that the source IP used for this network
    # when connecting locally should be in 127.0.0.0/8 range.
    # This is needed since otherwise the TPROXY rule would match
    # both forward and backward traffic. We want it to catch 
    # forward traffic only.
    sudo ip route add local 192.0.2.0/24 dev lo src 127.0.0.1
    
    # Set the magical TPROXY routing
    sudo iptables -t mangle -I PREROUTING \
            -d 192.0.2.0/24 -p tcp \
            -j TPROXY --on-port=1234 --on-ip=127.0.0.1

`TPROXY`를 이용하면 모든 포트에 바인딩하는 트릭을 매우 쉽게 할 수 있습니다. 다음과 같이 설정합니다:
    
    
    IP_TRANSPARENT (since Linux 2.6.24)
    Setting this boolean option enables transparent proxying on
    this socket.  This socket option allows the calling applica‐
    tion to bind to a nonlocal IP address and operate both as a
    client and a server with the foreign address as the local
    end‐point.  NOTE: this requires that routing be set up in
    a way that packets going to the foreign address are routed 
    through the TProxy box (i.e., the system hosting the 
    application that employs the IP_TRANSPARENT socket option).
    Enabling this socket option requires superuser privileges
    (the CAP_NET_ADMIN capability).
    
    TProxy redirection with the iptables TPROXY target also
    requires that this option be set on the redirected socket.

이 설정에 추가하여 TCP 서버를 `SO_TRANSPARENT` 소켓 옵션과 같이 시작해야 합니다. 아래 예제가 동작하려면 tcp://127.0.0.1:1234 에서 리스닝할 필요가 있습니다. `SO_TRANSPARENT` [매뉴얼 페이지](http://man7.org/linux/man-pages/man7/ip.7.html)에는 다음과 같이 나와 있습니다:
    
    
    import socket
    
    IP_TRANSPARENT = 19
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.IPPROTO_IP, IP_TRANSPARENT, 1)
    
    s.bind(('127.0.0.1', 1234))
    s.listen(32)
    print("[+] Bound to tcp://127.0.0.1:1234")
    while True:
        c, (r_ip, r_port) = s.accept()
        l_ip, l_port = c.getsockname()
        print("[ ] Connection from tcp://%s:%d to tcp://%s:%d" % (r_ip, r_port, l_ip, l_port))
        c.send(b"hello world\n")
        c.close()

여기 간단한 파이썬 서버가 있습니다:
    
    
    $ nc -v 192.0.2.1 9999
    Connection to 192.0.2.1 9999 port [tcp/*] succeeded!
    hello world

서버를 실행 후에 임의의 IP주소로 연결할 수 있습니다:
    
    
    $ sudo python3 transparent2.py
    [+] Bound to tcp://127.0.0.1:1234
    [ ] Connection from tcp://127.0.0.1:60036 to tcp://192.0.2.1:9999

더 중요한 건 _아무도 해당 IP와 포트에 리스닝하고 있지 않아도_ 이 연결의 수신 주소가 192.0.2.1 포트 9999라고 서버가 보고하고 있다는 것입니다.

짠! 이것이 `conntrack`을 사용하지 않고 리눅스의 _임의의 포트에 바인딩하는_ 방법입니다.

### 이게 끝!

이 글에서 우리는 원래 투명 프록시을 돕기 위해 만들어졌던 잘 알려져 있지 않은 `iptables` 모듈을 사용하는 방법에 대해서 알아 보았습니다. 이것의 도움을 받아서 표준 BSD 소켓 API로는 불가능하다고 생각했던 것을을 할 수 있었고 별도의 커널 패치를 만들지 않아도 되었습니다.

`TPROXY` 모듈은 리눅스 방화벽이 일반적으로 네트워크 스택에서 이루어지는 일을 수행한다는 점에서 매우 특이합니다. 공식 문서는 다소 부족해서 많은 리눅스 사용자들이 이 모듈의 진정한 힘을 이해하고 있다고 보기는 어렵습니다.

`TPROXY`는 우리의 Spectrum 제품이 수정 없는 커널에서 잘 동작하도록 하고 있습니다. 이건 `iptables`와 네트워크 스택을 이해하도록 노력하는 것이 얼마나 중요한지 보여주는 또 다른 예이기도 합니다!

* * *

_저수준 소켓 작업이 재미있어 보이나요? 런던, 오스틴, 샌프란시스코 및 폴란드 바르샤바의[세계 최고 수준의 팀](https://boards.greenhouse.io/cloudflare/jobs/589572)에 합류 하세요._

* * *

  1. 적절한 `rp_filter`와 BGP 설정에 추가로 IP 주소를 루프백 인터페이스에 할당하여 우리의 엣지 서버에서 임의의 IP대역을 처리하도록 합니다. ↩︎



 _This is a Korean translation of a[existing post](https://blog.cloudflare.com/how-we-built-spectrum/) by [Marek Majkowski](https://blog.cloudflare.com/author/marek-majkowski), translated by [Junho Choi](https://blog.cloudflare.com/author/junho/)._

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-spectrum%2F&t=%EB%A6%AC%EB%88%85%EC%8A%A4%20%EB%B0%A9%ED%99%94%EB%B2%BD%EC%9D%84%20%EB%82%A8%EC%9A%A9%ED%95%98%EA%B8%B0%3A%20Spectrum%20%EC%9D%84%20%EB%A7%8C%EB%93%A4%20%EC%88%98%20%EC%9E%88%EC%97%88%EB%8D%98%20%E2%80%8B%ED%95%B4%ED%82%B9%E2%80%8B)[](https://x.com/intent/post?text=%EB%A6%AC%EB%88%85%EC%8A%A4+%EB%B0%A9%ED%99%94%EB%B2%BD%EC%9D%84+%EB%82%A8%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Spectrum+%EC%9D%84+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%97%88%EB%8D%98+%E2%80%8B%ED%95%B4%ED%82%B9%E2%80%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-spectrum%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-spectrum%2F)[](https://bsky.app/intent/compose?text=%EB%A6%AC%EB%88%85%EC%8A%A4+%EB%B0%A9%ED%99%94%EB%B2%BD%EC%9D%84+%EB%82%A8%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Spectrum+%EC%9D%84+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%97%88%EB%8D%98+%E2%80%8B%ED%95%B4%ED%82%B9%E2%80%8B+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-spectrum%2F)[](https://mastodonshare.com/?text=%EB%A6%AC%EB%88%85%EC%8A%A4+%EB%B0%A9%ED%99%94%EB%B2%BD%EC%9D%84+%EB%82%A8%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Spectrum+%EC%9D%84+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%97%88%EB%8D%98+%E2%80%8B%ED%95%B4%ED%82%B9%E2%80%8B&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-spectrum%2F)[](https://www.threads.net/intent/post?text=%EB%A6%AC%EB%88%85%EC%8A%A4+%EB%B0%A9%ED%99%94%EB%B2%BD%EC%9D%84+%EB%82%A8%EC%9A%A9%ED%95%98%EA%B8%B0%3A+Spectrum+%EC%9D%84+%EB%A7%8C%EB%93%A4+%EC%88%98+%EC%9E%88%EC%97%88%EB%8D%98+%E2%80%8B%ED%95%B4%ED%82%B9%E2%80%8B+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-we-built-spectrum%2F)

## 관련 태그

[DDoS](https://blog.cloudflare.com/ko-kr/tag/ddos/)[Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[Spectrum](https://blog.cloudflare.com/ko-kr/tag/spectrum/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[속도 및 신뢰성](https://blog.cloudflare.com/ko-kr/tag/speed-and-reliability/)[제품 뉴스](https://blog.cloudflare.com/ko-kr/tag/product-news/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
