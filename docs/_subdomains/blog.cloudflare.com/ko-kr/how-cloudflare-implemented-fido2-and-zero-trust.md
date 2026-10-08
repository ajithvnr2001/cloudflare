---
url: https://blog.cloudflare.com/ko-kr/how-cloudflare-implemented-fido2-and-zero-trust/
title: Cloudflare\uac00 \ud53c\uc2f1\uc744 \ubc29\uc9c0\ud558\uae30 \uc704\ud574 FIDO2 \ubc0f Zero Trust\ub85c \ud558\ub4dc\uc6e8\uc5b4 \ud0a4\ub97c \uad6c\ud604\ud558\ub294 \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:40:34.765421+00:00
---

# Cloudflare가 피싱을 방지하기 위해 FIDO2 및 Zero Trust로 하드웨어 키를 구현하는 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/how-cloudflare-implemented-fido2-and-zero-trust/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Zero Trust](https://blog.cloudflare.com/ko-kr/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/ko-kr/tag/zero-trust/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)+11개의 태그 더 보기

4개 태그4개 태그 보기

  * 게시물 태그
  * [Cloudflare Zero Trust](https://blog.cloudflare.com/ko-kr/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/ko-kr/tag/zero-trust/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[창립기념일 주간](https://blog.cloudflare.com/ko-kr/tag/birthday-week/)
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



[창립기념일 주간](https://blog.cloudflare.com/ko-kr/tag/birthday-week/)

[Cloudflare Zero Trust](https://blog.cloudflare.com/ko-kr/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/ko-kr/tag/zero-trust/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[창립기념일 주간](https://blog.cloudflare.com/ko-kr/tag/birthday-week/)

2022년 9월 29일

# Cloudflare가 피싱을 방지하기 위해 FIDO2 및 Zero Trust로 하드웨어 키를 구현하는 방법

![Evan Johnson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47BS1WVZYVJDW7MV0RH2BM.png&w=64&h=64&f=webp&fit=cover&position=center)![Derek Pitts](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46384YHDK7BZNAPKRR6A3X.png&w=64&h=64&f=webp&fit=cover&position=center)

[Evan Johnson](https://blog.cloudflare.com/ko-kr/author/evan-johnson/) 및 [Derek Pitts](https://blog.cloudflare.com/ko-kr/author/derek-pitts/)

8분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/how-cloudflare-implemented-fido2-and-zero-trust/), [Deutsch](https://blog.cloudflare.com/de-de/how-cloudflare-implemented-fido2-and-zero-trust/), [Español](https://blog.cloudflare.com/es-es/how-cloudflare-implemented-fido2-and-zero-trust/), [Français](https://blog.cloudflare.com/fr-fr/how-cloudflare-implemented-fido2-and-zero-trust/), [日本語](https://blog.cloudflare.com/ja-jp/how-cloudflare-implemented-fido2-and-zero-trust/), [繁體中文](https://blog.cloudflare.com/zh-tw/how-cloudflare-implemented-fido2-and-zero-trust/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/how-cloudflare-implemented-fido2-and-zero-trust/).

![How Cloudflare implemented hardware keys with FIDO2 and Zero Trust to prevent phishing](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW449SQG6FZK347ME5C2QNBQ.png&w=1800&h=1013&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////+8vHs7Ofe8Ovf9vPn9fXu7vDu////////8fDs6OTe6+fd8/Dl9fTt8PHw////////8fHv5eLe6OTc8u7l9vTu8/Ty////////9PTz5+Tj6eXg9PDp+ffy9/j3////////+vr67evr8Ozp+vfx/v35+/z8////////////9/T0+fbz///7/////////////////////vz7///8///////////////////////////+////////////////)

Cloudflare 보안 아키텍처는 몇년 전만 해도 전형적인 “성과 해자” VPN 아키텍처였습니다. Cloudflare 직원들은 기업 VPN을 사용하여 내부 애플리케이션과 서버에 연결하여 업무를 수행했습니다. VPN에 로그인할 때 Google Authenticator 또는 Authy와 같은 인증기 앱을 사용하여 시간 기반 일회용 비밀번호(TOTP)를 통한 2단계 인증을 적용했지만, 단지 몇 가지 내부 애플리케이션에만 두 번째 인증 계층이 있었습니다. 이 아키텍처는 외관이 강력해 보이지만, 보안 모델은 취약합니다. Cloudflare는 최근에 [방지했던 피싱 공격의 메커니즘을 자세히 설명했으며](https://blog.cloudflare.com/2022-07-sms-phishing-attacks/), 공격자가 TOTP와 같은 2단계 인증 방법으로 “보안이 강화된” 애플리케이션을 피싱하는 방법을 살펴보았습니다. 다행히 Cloudflare는 오래 전에 TOTP를 폐지했고 하드웨어 보안 키와 Cloudflare Access로 교체했습니다. 이 블로그에서는 이것을 어떻게 수행했는지 설명합니다.

피싱 문제에 대한 솔루션은 _FIDO2/WebAuthn_라고 하는 [다단계 인증(MFA)](https://www.cloudflare.com/learning/access-management/what-is-multi-factor-authentication/) 프로토콜을 통하는 것입니다. 현재 모든 Cloudflare 직원은 안전한 다단계인 FIDO2로 로그인하고 당사의 Zero Trust 제품을 사용하여 Cloudflare 시스템을 인증합니다. Cloudflare 최신 아키텍처는 피싱 방지 기능을 갖추고 있어 최소 권한 액세스 제어를 더 쉽게 적용할 수 있습니다.

### 보안 키 용어와 Cloudflare에서 사용하는 용어 몇 가지

2018년 Cloudflare에서는 피싱 차단 MFA로 마이그레이션하고 싶었습니다. Cloudflare는 [evilginx2](https://github.com/kgretzky/evilginx2)와 피싱 푸시 기반 모바일 인증기의 성숙도 및 TOTP를 살펴보았습니다. 소셜 엔지니어링과 자격 증명 도용 공격을 견뎌낸 유일한 피싱 차단 MFA는 FIDO 표준을 구현한 보안 키였습니다. FIDO 기반 MFA는 FIDO2, WebAuthn, 하드(웨어) 키, 보안 키, 특히 YubiKey(잘 알려진 하드웨어 키 제조업체 이름)와 같은 새로운 용어를 소개하고 이 게시물에서 사용합니다.

**WebAuthn** 은 [웹 인증 표준](https://www.w3.org/TR/webauthn-2/)을 지칭하는데, [Cloudflare Dashboard의 보안 키 지원](https://blog.cloudflare.com/cloudflare-now-supports-security-keys-with-web-authentication-webauthn/)을 출시했을 당시 우리는 해당 프로토콜의 작동 원리를 심층적으로 작성하였습니다.

**CTAP1(U2F) 및 CTAP2** 는 인증 기관 프로토콜에 대한 클라이언트를 지칭하며, 이는 소프트웨어와 하드웨어 기기가 WebAuthn 프로토콜을 수행하는 플랫폼과 상호작용하는 방법을 상세히 설명합니다.

**FIDO2** 는 인증에 사용되는 이 두 가지 프로토콜의 모음입니다. 차이는 중요하지 않지만, 명명 규칙이 혼란스러울 수 있습니다.

알아두어야 할 가장 중요한 점은 모든 프로토콜과 표준이 피싱을 막아내는 개방적 인증 프로토콜을 구현하도록 개발되었고 하드웨어 기기와 함께 구현할 수 있다는 것입니다. 소프트웨어에서는 Face ID, Touch ID, Windows Assistant 등과 함께 구현됩니다. 하드웨어에서는 YubiKey 또는 다른 별도의 물리적 기기를 사용하여 USB, Lightning, NFC로 인증합니다.

FIDO2를 사용하면 피싱이 차단되는 이유는 암호화되어 안전한 챌린지/응답을 구현하고, 챌린지 프로토콜에 사용자가 인증하려는 특정 웹사이트나 도메인이 포함되기 때문입니다. 보안 키는 example.net에서 로그인 시 사용자가 example.com에 정상적으로 로그인을 시도할 때와는 다른 응답을 생성합니다.

Cloudflare에서는 오랫동안 직원에게 여러 가지 유형의 보안 키를 발급했지만, 지금은 모든 직원에 대해 두 가지 FIPS 검증 보안 키를 발급합니다. 첫 번째 키는 YubiKey 5 Nano 또는 YubiKey 5C Nano로, 언제나 직원의 노트북 USB 슬롯에 꽂아두어야 합니다. 두 번째 키는 YubiKey 5 NFC 또는 YubiKey 5C NFC로, NFC 또는 USB-C를 통해 데스크톱과 모바일에서 작동합니다.

2018년 말에 Cloudflare에서는 전사적 행사에 보안 키를 배포했습니다. 모든 직원에게 키를 등록하고 인증을 받도록 요청했으며, 간단한 워크숍을 통해 장치에 대한 질문을 받았습니다. 이 프로그램은 엄청난 성공을 거두었지만, 아직 개선해야 할 점과 WebAuthn과 작동하지 않는 애플리케이션이 있었습니다. Cloudflare에서는 보안 키를 완전히 적용할 준비가 되어 있지 않았으며, 문제를 해결하는 동안 중간에 사용할 솔루션이 필요했습니다.

### 시작: Cloudflare Zero Trust로 선택적 보안 키 적용

Cloudflare에는 관리해야 할 수천 개의 애플리케이션과 서버가 있고, 이는 VPN을 통해 보호합니다. 직원에게 보안 키 세트를 발급하는 것과 동시에 이 모든 애플리케이션을 Zero Trust 액세스 프록시로 마이그레이션하기 시작했습니다.

Cloudflare Access를 사용하는 직원은 한때는 VPN으로 보호되었던 사이트에 안전하게 액세스할 수 있습니다. 각 내부 서비스에서는 서명된 자격 증명을 검증하여 사용자를 인증하고, 사용자가 ID 공급자로 로그인했는지 확인합니다. 보안 키를 롤아웃하는 데 Cloudflare Access가 _필수_인 이유는 일부 내부 애플리케이션에 보안 키 인증을 선택적으로 적용하기 위한 도구를 제공했기 때문입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - Zc8fCw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4937A2KW8CQJPZ0GXKQB78.png&w=715&h=343&f=webp&fit=cover&position=center)

우리는 애플리케이션을 Zero Trust 제품으로 온보딩할 때 Terraform을 사용했고, 이 Cloudflare Access 정책에 처음으로 보안 키를 적용했습니다. ID 공급자와 통합할 때 OAuth2를 사용하도록 Cloudflare Access를 설정했고, ID 공급자는 OAuth 플로에서 두 번째 인증 유형으로 무엇을 사용하는지 Access에 알립니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - RPatyG](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458G8SCJEBMHZKPA8RDBH0.png&w=624&h=325&f=webp&fit=cover&position=center)

우리의 경우, [swk](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-amr-values-04)가 보안 키를 소유한 증거가 됩니다. 누군가가 로그인을 했는데 보안 키를 사용하지 않은 경우, 다시 로그인하고 메시지가 표시되었을 때 보안 키를 누르라는 오류 정보 메시지가 표시됩니다.

선택적으로 보안 키를 적용하자마자 보안 키 롤아웃의 궤도가 바뀌었습니다. 2020년 7월 29일에 단일 서비스에 적용을 시작했고, 그 이후 2개월에 걸쳐 보안 키를 사용한 인증이 엄청나게 증가했습니다. 이 단계는 우리 직원이 새로운 기술에 익숙해질 기회를 제공하는 데 중요했습니다. 선택적 적용 기간은 휴가 중인 직원을 고려하여 1개월 이상이어야 했지만, 지금 생각해 보면 그보다 길 필요는 없었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - LBAlSU](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48JEQF1XSNFJVFDNB8C7ZB.png&w=715&h=193&f=webp&fit=cover&position=center)

VPN을 포기하고 Zero Trust 제품을 사용하도록 애플리케이션을 마이그레이션한 후 어떤 보안 이익을 얻었을까요? 기존 애플리케이션이나 SAML을 구현하지 않는 애플리케이션의 경우, 역할 기반 액세스 제어와 최소 권한 원칙을 적용하기 위해서는 마이그레이션이 필요했습니다. VPN으로 네트워크 트래픽이 인증되지만, 어떤 애플리케이션도 네트워크 트래픽이 누구에게 속했는지 알 수 없습니다. Cloudflare의 애플리케이션은 여러 레벨의 권한을 적용하는 데 어려움이 있었고, 각각 자체적인 인증 체계를 다시 개발해야 했습니다.

Cloudflare Access에 온보딩했을 때 RBAC를 적용할 그룹을 생성했고 애플리케이션에는 각 사용자에게 어떤 권한이 있어야 하는지 알렸습니다.

다음은 ACL-CFA-CFDATA-argo-config-admin-svc 그룹의 구성원만 액세스할 수 있는 사이트입니다. 직원은 로그인했을 때 보안 키를 사용해야 했고, 여기에는 복잡한 OAuth나 SAML 통합이 필요하지 않았습니다. 이와 동일한 패턴을 사용하는 내부 사이트가 600개가 넘으며, 이들 사이트에서는 모두 보안 키를 적용합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - Z0NvTw](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WCWVWGR5TXY3KNPVJS2Y.png&w=715&h=754&f=webp&fit=cover&position=center)

### 의무 기간으로의 전환: Cloudflare에서 TOTP를 완전히 폐지한 날

2021년 2월에 우리 직원들이 보안 팀에 소셜 엔지니어링 시도를 신고하기 시작했습니다. 보안 팀에서는 우리 IT 부서의 누군가를 사칭하는 사람으로부터 전화를 받아서 깜짝 놀란 상태였습니다. 그래서 직원이 소셜 엔지니어링 공격의 피해자가 되지 않도록 모든 인증에 보안 키를 의무화하기로 했습니다.

WebAuthn을 제외한 다른 모든 형식의 MFA(SMS, TOTP 등)를 비활성화한 후, 공식적으로 FIDO2만 사용하게 되었습니다. 하지만 이 그래프에서 “소프트 토큰”(TOTP)이 완전히 제로는 아닙니다. 그 이유는 보안 키를 잃어버렸거나 계정이 잠긴 사람들이 다른 방법으로 로그인을 지원하는 보안 오프라인 복구를 거쳐야 했기 때문입니다. 이런 상황이 발생할 경우 백업이 가능하도록 여러 보안 키를 배포하는 것이 좋습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1355 Embedded Image - qj40tH](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48CB24MZPBFMS83XK33K5Z.png&w=715&h=295&f=webp&fit=cover&position=center)

이제 모든 직원이 피싱 예방을 위해 YubiKeys를 사용하고 있는데, 이것으로 충분할까요? SSH와 HTTP 외의 프로토콜은 어떨까요? ID 및 액세스 관리를 위한 단일 통합 전략을 통해 보안 키를 임의의 다른 프로토콜에 적용하는 것이 다음으로 고려해야 할 단계였습니다.

### SSH로 보안 키 사용

SSH 연결에 보안 키 적용을 지원하기 위해 모든 프로덕션 인프라에 [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/)을 배포했습니다. Cloudflare Tunnel은 터널을 통과시키는 프로토콜과 관계없이 Cloudflare Access와 매끄럽게 통합되고, 터널을 실행하려면 터널 클라이언트 [cloudflared](https://github.com/cloudflare/cloudflared)가 필요합니다. 즉, cloudflared 바이너리를 모든 인프라에 배포하고 각 머신에 대해 터널을 생성하며, 보안 키가 필요한 곳에 Cloudflare Access 정책을 생성할 수 있고, ssh 연결이 Cloudflare Access를 통해 보안 키를 요청하기 시작합니다.

실질적으로는 이러한 단계는 보기보다 어렵지 않고 Zero Trust 개발자 문서에 구현 방법에 대한 [훌륭한 튜토리얼](https://developers.cloudflare.com/cloudflare-one/tutorials/ssh-cert-bastion/)이 나와 있습니다. 각 서버에는 터널을 시작하는 데 필요한 구성 파일이 있습니다. Systemd는 cloudflared를 호출하고, 이는 터널을 시작할 때 이 구성 파일(또는 이와 유사한 구성 파일)을 사용합니다.

작업자가 인프라에 SSH를 적용해야 할 때는 ProxyCommand SSH 지침을 사용하여 cloudflared를 호출하고, Cloudflare Access를 사용하여 인증한 다음, Cloudflare를 통해 SSH 연결을 포워딩합니다. 우리 직원의 SSH 구성에는 이와 유사한 항목이 있고, cloudflared에서 도우미 명령으로 생성할 수 있습니다.
    
    
    tunnel: 37b50fe2-a52a-5611-a9b1-ear382bd12a6
    credentials-file: /root/.cloudflared/37b50fe2-a52a-5611-a9b1-ear382bd12a6.json
    
    ingress:
      - hostname: <identifier>.ssh.cloudflare.com
        service: ssh://localhost:22
      - service: http_status:404

참고로 OpenSSH는 [버전 8.2](https://www.openssh.com/txt/release-8.2) 이후로 FIDO2를 지원했지만, 우리는 모든 액세스 제어 목록이 한 곳에서 관리되는 통합적 액세스 제어 전략이 있는 것이 유리하다는 것을 알게 되었습니다.
    
    
    Host *.ssh.cloudflare.com
        ProxyCommand /usr/local/bin/cloudflared access ssh –hostname %h.ssh.cloudflare.com

### Cloudflare에서 얻은 유용한 교훈과 경험

지난 몇 개월을 거쳐, FIDO2 및 WebAuthn이 곧 인증의 미래인 점에는 의문의 여지가 없습니다. 이 작업을 모두 완료하는 데는 몇 년이 걸렸고, 이를 통해 얻은 교훈이 FIDO 기반 인증을 최신화하려는 다른 조직에도 도움이 되기를 바랍니다.

자신의 조직에 보안 키를 롤아웃하는 데 관심이 있거나 Cloudflare의 Zero Trust 제품에 관심이 있으면 [securitykeys@cloudflare.com](mailto:securitykeys@cloudflare.com)으로 문의해 주세요. 우리의 예방적 활동이 최근의 피싱 및 소셜 엔지니어링 공격을 차단하는 데 도움이 되어 기쁘기는 하지만, 우리 [보안 팀](https://www.cloudflare.com/careers/jobs/?department=Security)은 앞으로의 공격 차단을 지원하기 위해 꾸준히 노력하고 있습니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F&t=Cloudflare%EA%B0%80%20%ED%94%BC%EC%8B%B1%EC%9D%84%20%EB%B0%A9%EC%A7%80%ED%95%98%EA%B8%B0%20%EC%9C%84%ED%95%B4%20FIDO2%20%EB%B0%8F%20Zero%20Trust%EB%A1%9C%20%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4%20%ED%82%A4%EB%A5%BC%20%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94%20%EB%B0%A9%EB%B2%95)[](https://x.com/intent/post?text=Cloudflare%EA%B0%80+%ED%94%BC%EC%8B%B1%EC%9D%84+%EB%B0%A9%EC%A7%80%ED%95%98%EA%B8%B0+%EC%9C%84%ED%95%B4+FIDO2+%EB%B0%8F+Zero+Trust%EB%A1%9C+%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4+%ED%82%A4%EB%A5%BC+%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://bsky.app/intent/compose?text=Cloudflare%EA%B0%80+%ED%94%BC%EC%8B%B1%EC%9D%84+%EB%B0%A9%EC%A7%80%ED%95%98%EA%B8%B0+%EC%9C%84%ED%95%B4+FIDO2+%EB%B0%8F+Zero+Trust%EB%A1%9C+%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4+%ED%82%A4%EB%A5%BC+%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://mastodonshare.com/?text=Cloudflare%EA%B0%80+%ED%94%BC%EC%8B%B1%EC%9D%84+%EB%B0%A9%EC%A7%80%ED%95%98%EA%B8%B0+%EC%9C%84%ED%95%B4+FIDO2+%EB%B0%8F+Zero+Trust%EB%A1%9C+%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4+%ED%82%A4%EB%A5%BC+%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)[](https://www.threads.net/intent/post?text=Cloudflare%EA%B0%80+%ED%94%BC%EC%8B%B1%EC%9D%84+%EB%B0%A9%EC%A7%80%ED%95%98%EA%B8%B0+%EC%9C%84%ED%95%B4+FIDO2+%EB%B0%8F+Zero+Trust%EB%A1%9C+%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4+%ED%82%A4%EB%A5%BC+%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fhow-cloudflare-implemented-fido2-and-zero-trust%2F)

## 관련 태그

[Cloudflare Zero Trust](https://blog.cloudflare.com/ko-kr/tag/cloudflare-zero-trust/)[Zero Trust](https://blog.cloudflare.com/ko-kr/tag/zero-trust/)[보안](https://blog.cloudflare.com/ko-kr/tag/security/)[창립기념일 주간](https://blog.cloudflare.com/ko-kr/tag/birthday-week/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
