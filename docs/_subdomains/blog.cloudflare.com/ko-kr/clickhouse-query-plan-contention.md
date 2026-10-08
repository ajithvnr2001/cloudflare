---
url: https://blog.cloudflare.com/ko-kr/clickhouse-query-plan-contention/
title: \uccad\uad6c \ud30c\uc774\ud504\ub77c\uc778\uc774 \uac11\uc790\uae30 \ub290\ub824\uc84c\uc2b5\ub2c8\ub2e4. \uc6d0\uc778\uc740 ClickHouse\uc758 \uc228\uaca8\uc9c4 \ubcd1\ubaa9 \ud604\uc0c1\uc774\uc5c8\uc2b5\ub2c8\ub2e4 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:43:03.309614+00:00
---

# 청구 파이프라인이 갑자기 느려졌습니다. 원인은 ClickHouse의 숨겨진 병목 현상이었습니다 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/clickhouse-query-plan-contention/

[블로그](https://blog.cloudflare.com/ko-kr/)

[ClickHouse](https://blog.cloudflare.com/ko-kr/tag/clickhouse/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[성능](https://blog.cloudflare.com/ko-kr/tag/performance/)+22개의 태그 더 보기

5개 태그5개 태그 보기

  * 게시물 태그
  * [ClickHouse](https://blog.cloudflare.com/ko-kr/tag/clickhouse/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[성능](https://blog.cloudflare.com/ko-kr/tag/performance/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)
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



[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)

[ClickHouse](https://blog.cloudflare.com/ko-kr/tag/clickhouse/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[성능](https://blog.cloudflare.com/ko-kr/tag/performance/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)

2026년 5월 14일

# 청구 파이프라인이 갑자기 느려졌습니다. 원인은 ClickHouse의 숨겨진 병목 현상이었습니다

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/ko-kr/author/james-morrison/) 및 [Christian Endres](https://blog.cloudflare.com/ko-kr/author/christian-endres/)

12분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/clickhouse-query-plan-contention/), [日本語](https://blog.cloudflare.com/ja-jp/clickhouse-query-plan-contention/), [繁體中文](https://blog.cloudflare.com/zh-tw/clickhouse-query-plan-contention/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/clickhouse-query-plan-contention/).

![BLOG-3299 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4999A46M2F3BCY3QF5F258.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////789PLy7evs7+3t8/Hx8/Hv7ezp///////+8vL06Oju5+jv7O3y7+/x7e3s////////8vP45Ofx4eXx5+r17O707u/v////////9ff95+r14+f26Oz57/H48vP0/////////P3/7/L77fD78vT/9/j++Pn6////////////+/v//Pv//////////v/+////////////////////////////////////////////////////////////////)

_본 콘텐츠는 사용자의 편의를 고려해 자동 기계 번역 서비스를 사용하였습니다. 영어 원문과 다른 오류, 누락 또는 해석상의 미묘한 차이가 포함될 수 있습니다. 필요하시다면 영어 원문을 참조하시기를 바랍니다._

Cloudflare는 오픈 소스 온라인 분석 처리(OLAP) 데이터베이스인 ClickHouse를 많이 사용합니다. 우리는 사용자에게 Cloudflare 제품 사용에 대해 요금을 청구할 금액을 결정하기 위해 매일 ClickHouse로 수백만 건의 호출을 합니다. 이러한 작업을 적시에 완료하지 않으면 송장을 조정하기가 아주 어려워집니다.

이 파이프라인은 사용 수익, 사기 시스템 등에서 수억 달러의 수익을 창출하므로 지연되면 다운스트림에도 큰 영향이 미칩니다.

Cloudflare의 청구서가 나가는 것을 담당하는 ClickHouse의 일일 집계 작업이 마이그레이션 후에 크게 느려졌을 때 큰 문제가 되었던 이유가 바로 그것입니다. I/O, 메모리, 스캔한 행, 읽은 부분 등 모든 일반적인 용의자가 깨끗해 보였습니다. ClickHouse 쿼리가 느리면 일반적으로 확인하는 모든 것이 정상적인 것으로 보였습니다. 

ClickHouse의 내부 깊숙이 위치한 숨겨진 병목 현상을 저희가 발견하고 이를 해결하기 위해 작성한 세 가지 패치에 대한 이야기를 들어보겠습니다.

## 그 구성: 페타바이트급 분석 플랫폼

우리는 ClickHouse를 사용하여 수십 개의 클러스터에 100페타바이트 이상의 데이터를 저장합니다. 많은 내부 팀을 위해 온보딩을 간소화하기 위해 2022년 초에 "준비된 분석"이라는 시스템을 구축했습니다.

전제는 간단합니다. 팀에서 새로운 테이블을 설계하는 대신 데이터를 하나의 방대한 테이블로 스트리밍할 수 있다는 것입니다. 데이터세트는 `네임스페이스`로 명확화되며 각 레코드는 표준 스키마(예: 부동 필드 20개, 문자열 필드 20개, 타임스탬프, `indexID`)를 사용합니다. 

ClickHouse에서 데이터 정렬 방식은 쿼리 성능에 매우 중요합니다. 여기에서 `indexID`가 필요합니다. 기본 키의 일부를 형성하는 문자열 필드이므로 모든 개별 네임스페이스는 해당 네임스페이스의 소유자가 실행할 것으로 예상되는 쿼리에 최적화된 방식으로 데이터를 정렬할 수 있습니다. 결국, 다음과 같은 기본 키가 완성됩니다. (`네임스페이스`, `indexID`, `타임스탬프`).

이 시스템은 수백 개의 애플리케이션에서 널리 사용 중입니다. 2024년 12월에는 이미 2PiB 이상의 데이터와 초당 수백만 행의 수집 속도를 달성했습니다. 하지만 여기에는 보존 정책이라는 치명적인 결함이 있었습니다.

## 문제: 모든 것을 관리하는 단일 보존 정책

Cloudflare는 Time-to-Live(TTL) 기능을 네이티브로 도입하기 전부터 여러 해 동안 ClickHouse를 사용해 왔습니다. 따라서 우리는 파티셔닝을 기반으로 하는 자체 보존 시스템을 구축했습니다. 레디-분석 테이블은 `요일`별로 분할되었고, 우리의 보존 작업은 31일 이상 된 파티션을 삭제했을 뿐입니다.

이 "만능" 31일 보존이 주요 한계였습니다. 법적 또는 계약 의무로 인해 데이터를 수년간 저장해야 하는 팀도 있었지만, 며칠만 필요한 팀도 있었습니다. 이러한 제약으로 인해 이러한 사용 사례에서는 레디 분석을 사용할 수 없었으며 훨씬 더 복잡한 온보딩 프로세스가 있는 기존 설정을 선택해야 했습니다.

**네임스페이스별로 보존할 수 있는** 새로운 시스템이 필요했습니다.

## 해결책: 새로운 파티셔닝 계획

Cloudflare에서는 두 가지 주요 접근 방식을 고려했습니다.

  1. **네임스페이스별 테이블:** 이는 당연히 보존 문제를 해결하지만, 온디맨드 수천 개의 테이블을 관리하려면 상당한 신규 자동화가 필요합니다.
  2. **새로운 파티셔닝 키:** 파티셔닝 키를 `(day)` 에서 `(namespace, day)`로 변경할 수 있습니다.



우리는 두 번째 옵션을 선택했습니다. 이를 통해 기존 유지 시스템으로 파티션을 계속 관리할 수 있지만, 이제는 네임스페이스별로 세분화할 수 있습니다.

이렇게 하면 테이블의 총 데이터 부분 수가 증가할 것이라는 것을 알고 있었지만, **모든 쿼리는 특정 네임스페이스로 필터링되므로 _단일 쿼리에서 읽는 부분 개수는_ 변경되지 않아야 합니다.** 따라서 성능에는 영향이 없을 것으로 생각했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image4](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4893FX4WFRGPEECQSTGMYN.png&w=715&h=709&f=webp&fit=cover&position=center)

_파티셔닝을 변경하여 단일 네임스페이스의 데이터를 저렴하게 삭제할 수 있었던 방법을 보여줍니다_

이 새로운 시스템을 통해 정교한 스토리지 관리 계층도 구축할 수 있었습니다. [ _최대-최소 공정성 알고리즘_](https://en.wikipedia.org/wiki/Max-min_fairness)을 사용하여 목표 디스크 사용률(예: 90%)을 설정할 수 있었고, 사용 가능한 공간을 자동으로 "공유"할 수 있습니다. 네임스페이스가 공정한 점유율보다 적게 사용하면 사용하지 않은 용량이 더 필요한 곳에 할당됩니다. 따라서 90%의 활용도로 자신 있게 클러스터를 실행할 수 있었습니다.

Cloudflare는 2025년 1월에 마이그레이션을 시작했습니다. 저희는 ClickHouse의 `Merge` 테이블 기능을 사용하여 기존 테이블과 새 테이블을 결합함으로써 기존 데이터가 노후화되는 동안 새 파티션을 나눈 테이블에 새 데이터를 모두 기록했습니다.

## 미스터리: 요금 청구가 시작되는 시기

두 달 후인 2025년 3월 말에, 청구팀에서는 일일 집계 작업이 둔화되고 있다고 보고했습니다. 이러한 작업은 시간이 중요합니다. 처리하지 않으면 청구서가 출력되지 않습니다. 작업은 점점 더 느려지고 있었고, 기한이 임박했습니다.

조사를 했지만 일반적인 용의자를 비난하지 않았습니다. I/O는 정상이었습니다. 메모리는 정상이었습니다. 개별 쿼리에 대한 메트릭을 보면 이전보다 더 많은 데이터나 더 많은 부분을 _읽지_ 않았던 것으로 나타났습니다. 처음에는 우리의 가정이 맞는 것 같았지만, 시스템은 점점 더 굳어가고 있었습니다.

이론을 갖기까지 며칠이 걸렸습니다. 마지막으로 클러스터의 _총 부품 수_ 에 대한 쿼리 지속 시간을 그래프로 그렸습니다. 이러한 상관관계는 부인할 수 없습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47YV50ASJA17DM0BX4JXF3.png&w=715&h=235&f=webp&fit=cover&position=center)

_준비되어 있는 Analytics ClickHouse 클러스터에 대한 평균 SELECT 쿼리 Duration으로, 점진적인 성능 저하를 보여줍니다._

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HY9NE8VMFT5Z5RMHRVCM.png&w=715&h=233&f=webp&fit=cover&position=center)

_새로운 (네임스페이스, 데이) 파티셔닝 방식에 따른 테이블 Replica당 총 데이터 파트 수의 선형적인 증가율._

하지만 _왜 그랬을까요_? 추가 부분을 _읽을 생각이_ 없다면 왜 그 자체만으로도 우리의 속도가 느려질까요?

## 조사: 플레임 그래프로 병목 현상 제거

저희는 ClickHouse의 내장 [`_trace_log_`](https://clickhouse.com/docs/operations/system-tables/trace_log) 를 사용하여 플레임 그래프를 생성했습니다. 이는 실행 중인 ClickHouse 서버의 트레이스를 기록하는 기본 제공 테이블입니다. 여기에는 어떤 코드가 실행 중인지에 대한 추적도 포함되어 있을 뿐만 아니라 이를 특정 사용자, 쿼리 ID 및 기타 메타데이터와 연결하기도 합니다. 즉, 필요한 경우 아주 정확한 이벤트 세트로 필터링할 수 있습니다. 저희의 경우, _리프 SELECT 쿼리_ 를 구체적으로 살펴보고자 했습니다. 이 작업은 이 표에 나와 있는 메타데이터 덕분에 쉬웠습니다.

첫 번째 CPU 기반 플레임 그래프는 **쿼리 계획** 에 엄청난 시간이 소요되고 있다는 우리의 의심을 빠르게 확인시켜 주었습니다. 이 단계는 ClickHouse가 읽을 부분을 결정하는 실행 _전_ 입니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46RG580ZDKK07KCTRDD0MK.png&w=715&h=368&f=webp&fit=cover&position=center)

_리프 쿼리 CPU 시간의 45%가 파티션 ID를 기반으로 파트 벡터를 필터링하는 데 사용되고 있음을 보여주는 Flame 그래프_

플레임 그래프는 명확했습니다. 샘플링된 CPU 시간의 45%가 `filterPartsByPartition`이라는 단일 함수에서 사용되고 있었습니다.

해결을 위한 첫 번째 시도는 이 정확한 코드 경로에 대한 작은 패치였습니다. 플래너가 휴리스틱을 평가하여 부분을 정리하는데, 우리는 테이블에서 최적의 순서로 평가되지 않는다고 생각했습니다. Cloudflare의 패치로 인해 순서가 바뀌면서 소폭 5%의 개선이 있었습니다. 우리는 올바른 길을 가고 있었지만, 진짜 문제를 놓치고 있었습니다.

우리는 활성 스레드만 샘플링하는 "CPU" 트레이스를 생성하고 있었습니다. 비활성 상태이거나 대기 중인 스레드를 포함한 _모든_ 스레드를 샘플링하는 "실제" 트레이스로 전환했습니다. 새로운 Flame 그래프가 공개되었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HV7ET9Z7PXF66NF9GT9Y.png&w=715&h=351&f=webp&fit=cover&position=center)

_리프 쿼리 지속 시간의 절반 이상이 활성 파트 목록을 보호하는 뮤텍스트를 기다리는 데 소요된다는 것을 보여주는 Flame 그래프_

문제는 CPU 위주의 작업이 아니었습니다. 바로 **대규모 잠금 경합** 이었습니다. 쿼리 지속 시간의 절반 이상이 테이블의 _부분_ 목록을 보호하는 단일 뮤텍스(`MergeTreeData`)를 획득하기 위해 대기 하는 데 사용되었습니다. 쿼리를 계획하려면 모든 스레드가 다음을 거쳐야 했습니다.

  1. 이 뮤텍스에 대한 **배타적 잠금** 을 획득합니다.
  2. 표에 있는 _모든_ 부품 목록의 전체 사본을 만드세요.
  3. 잠금을 해제합니다.
  4. 해당 목록을 관련 있는 부분으로 필터링합니다.



수만 개의 부분과 수백 개의 동시 쿼리를 통해 모든 작업이 하나의 파일 줄에 서 있었습니다.

## 수정 사항: 세 개의 패치

이러한 인사이트는 이러한 핫스팟을 완화하기 위한 일련의 최적화를 계획하는 데 도움이 되었습니다. ClickHouse의 모든 패치와 마찬가지로 우리는 일반화하려고 노력하며 결국 업스트림 코드베이스에 기여합니다. 따라서 포크를 더 쉽게 유지할 수 있으며, 커뮤니티에서도 Cloudflare가 적용할 수 있는 이점을 누릴 수 있습니다!

### 최적화 1: 공유 잠금 사용

쿼리 플래너는 부품 목록을 _수정하지_ 않습니다. 그냥 _읽습니다_. 이 회사는 독점 잠금을 사용하는 업무가 없었습니다.

**수정:** 대신 **공유 잠금** (`std::shared_lock`)을 획득하도록 코드를 수정했습니다. 이를 통해 모든 쿼리 플래너가 중요 섹션에 동시에 진입할 수 있었습니다.

**결과:** 쿼리 지속 시간이 즉각적으로 엄청나게 줄어듭니다. 잠금 경합이 사라졌습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CCVN8NX5N7V0Q8SYKEFN.png&w=715&h=235&f=webp&fit=cover&position=center)

_공유 잠금 최적화(최적화 1)가 평균 SELECT 쿼리 지속 시간에 미치는 즉각적인 영향은 잠금 경합의 해결 방법을 보여줍니다._

### 최적화 2: 벡터 복사 중지

성능이 크게 개선되었지만, 여전히 기준선으로는 돌아가지 않았습니다. 다시 트레이스 로그로 돌아가 '실제' 플레임 그래프를 만들었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48M55TB5PVRTEDJNTSB64J.png&w=715&h=351&f=webp&fit=cover&position=center)

_리프 쿼리 지속 시간의 4분의 1이 모든 부분의 벡터를 복사하는 데 소비되고, 또 다른 4분의 1은 벡터를 필터링하는 데 소비됨(다시 복사)을 보여주는 Flame 그래프._

새로운 프레임 그래프는 병목 현상이 단순히 이동한 것으로 나타났습니다. 이제는 공유 자물쇠를 사용하더라도 엄청난 양의 부품을 _복제하는_ 데 시간이 소모되고 있었습니다. 벡터를 복사하는 것은 직관적으로 비용이 적게 드는 것처럼 보이지만, 여기에는 수만 개의 요소가 있고 초당 수백 번 수행하면 비용이 더 많이 듭니다.

**수정 사항:** 복사를 완전히 미루었습니다. Cloudflare는 부품 목록의 "공유 사본"을 생성했습니다. 읽기 전용 작업(예: 쿼리 계획)은 이 사본에서 읽기만 합니다. 부품 세트를 _수정하는_ 모든 작업(새 삽입과 같은)은 캐시를 재생성합니다. 이제 플래너는 실제로 필요한 부품의 _필터링된_ 목록만 복사합니다.

**결과:** 또 다른 중요한 성능 향상.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PPRSHYTZ68EXGM666V41.png&w=715&h=236&f=webp&fit=cover&position=center)

_벡터 카피 최적화 도입 후 추가적인 성능 개선(최적화 2)._

이러한 엄청난 비용 절감을 내부적으로 확인한 후, Cloudflare는 이러한 변경 사항을 커뮤니티에도 적용하기로 결정했습니다. ClickHouse Inc.의 유지 관리자와 함께 약간의 설계 반복을 거쳐, 변경 사항을[ _PR #85535_](https://github.com/ClickHouse/ClickHouse/pull/85535)에 병합했습니다 _._ 이들은 [_ClickHouse 버전 25.11_](https://clickhouse.com/docs/whats-new/changelog/2025#performance-improvement-1)부터 사용할 수 있었습니다.

### 최적화 3: 부분에 대한 이진 검색

아직 끝난 것이 아닙니다. 부품 수가 늘어날수록 성능은 _여전히_ 훨씬 더 느리게 저하됩니다. 부품 수와의 상관관계는 여전히 있었습니다. 몇 달 후 다시 이 그래프를 보면, 새로운 프레임 그래프(그림 3과 동일하게 표시됨)에는 필터링 코드 경로(우리가 먼저 해결하려고 했던 경로)에 소요되는 시간이 표시됩니다. 이 코드는 모든 부분에 대해 **선형 스캔** 을 수행하여 각 부분에 대해 조건자를 평가합니다. 몇 달에 걸쳐 최적화 전의 지속 시간을 선택할 수 있었습니다.

하지만 이 부분 목록은 파티셔닝 키 기준으로 정렬되어 있습니다. 파티션 키의 첫 번째 열은 "테넌트"를 식별하기 때문에 대부분의 쿼리가 필터링되는 네임스페이스입니다. 이를 어떻게 활용할 수 있을까요?

**수정:** 파티션 ID의 `네임스페이스` 부분을 기반으로 바이너리 검색을 구현했습니다. 이 방법은 벡터가 정렬되어 있어 항목을 실제로 보지 않고도 많은 항목을 필터링할 수 있기 때문에 효과가 있습니다. `네임스페이스` 가 해당 정렬 키의 첫 번째 부분이므로 이 방법은 특히 효과적입니다. 이 바이너리 검색의 첫 번째 단계 후에는 검사해야 하는 부분의 범위가 훨씬 작아졌으며, 각 항목에 대해서는 여전히 이전과 동일한 논리를 적용하여 다른 조건에 따라 부분을 제외하면서 각 항목을 검토합니다.

**결과:** 2026년 3월에 이 패치를 배포한 후 쿼리 지속 시간이 50% 감소했습니다(그림 8 참조). 더 중요한 것은 이렇게 하면 쿼리 지속 시간과 부분 수의 상관관계가 결국 깨졌다는 점입니다. 안타깝게도 이 솔루션은 임의의 쿼리 조건(예: `(5,10)의 네임스페이스와` 같은 조건). 저희는 부분 필터링을 포함하기 위해 [_쿼리 조건 캐시_](https://clickhouse.com/blog/introducing-the-clickhouse-query-condition-cache)를 확장하는 것과 같은 보다 일반적인 접근 방식을 찾고 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3299 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46ZC0AXABREP5Q1ES3D0CS.png&w=715&h=239&f=webp&fit=cover&position=center)

_부품 프루닝을 위한 이진 검색 구현 후 대기 시간 지속 감소(최적화 3)._

## 불안한 휴전

이러한 최적화로 대금 청구 시스템으로 즉각적인 위기 상황이 해결되었습니다. 하지만 이 여정을 통해 파티셔닝 선택에 따르는 명확하지 않은 큰 비용이 노출되었습니다.

다른 문제가 남아 있습니다. 이 블로그 게시물에서는 부품 수를 늘리면 선택한 기간에서 발생한 문제에 대해서만 설명했지만, 이는 ClickHouse의 모든 부품에 대한 메타데이터를 추적하는 ZoomKeeper에도 문제를 발생시켰습니다. 언젠가 우리도 100기가바이트의 ZoomKeeper 클러스터에 대해 이야기할 날이 올 것입니다.

상당한 여유 공간은 확보했지만, 근본적인 질문은 여전히 남아 있습니다. 이 파티셔닝 계획이 장기적으로 올바른 선택이었을까요? 아니면 결국 큰 고통을 겪고 다른 아키텍처로 옮겨가야 할까요? 일단 패치는 현재 상태를 유지하고 있지만, 이번 경험은 잘 계획된 변경조차도 잘못된 가정의 희생양이 될 수 있음을 보여주는 분명한 예였습니다.

대금 청구 팀에서 이 문제를 처음 보고했을 때 복제본당 부품 개수는 30,000개였습니다. 부품 비율은 멈추지 않았고, 1년 후 복제본당 160,000개의 부품을 기록했지만, 여기에서 수행한 최적화 덕분에 쿼리 지속 시간은 안정적으로 유지되었습니다.

Cloudflare에서는 복잡한 엔지니어링 문제를 대규모로 해결합니다. 여기에서 설명한 디버깅 및 최적화가 이러한 문제와 관련이 있다고 생각하신다면, Cloudflare에서 [_채용하고 있는 채용 중인 직무를_](https://www.cloudflare.com/careers/jobs/?department=Engineering) 확인해 보세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fclickhouse-query-plan-contention%2F&t=%EC%B2%AD%EA%B5%AC%20%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%B4%20%EA%B0%91%EC%9E%90%EA%B8%B0%20%EB%8A%90%EB%A0%A4%EC%A1%8C%EC%8A%B5%EB%8B%88%EB%8B%A4.%20%EC%9B%90%EC%9D%B8%EC%9D%80%20ClickHouse%EC%9D%98%20%EC%88%A8%EA%B2%A8%EC%A7%84%20%EB%B3%91%EB%AA%A9%20%ED%98%84%EC%83%81%EC%9D%B4%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4)[](https://x.com/intent/post?text=%EC%B2%AD%EA%B5%AC+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%B4+%EA%B0%91%EC%9E%90%EA%B8%B0+%EB%8A%90%EB%A0%A4%EC%A1%8C%EC%8A%B5%EB%8B%88%EB%8B%A4.+%EC%9B%90%EC%9D%B8%EC%9D%80+ClickHouse%EC%9D%98+%EC%88%A8%EA%B2%A8%EC%A7%84+%EB%B3%91%EB%AA%A9+%ED%98%84%EC%83%81%EC%9D%B4%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fclickhouse-query-plan-contention%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fclickhouse-query-plan-contention%2F)[](https://bsky.app/intent/compose?text=%EC%B2%AD%EA%B5%AC+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%B4+%EA%B0%91%EC%9E%90%EA%B8%B0+%EB%8A%90%EB%A0%A4%EC%A1%8C%EC%8A%B5%EB%8B%88%EB%8B%A4.+%EC%9B%90%EC%9D%B8%EC%9D%80+ClickHouse%EC%9D%98+%EC%88%A8%EA%B2%A8%EC%A7%84+%EB%B3%91%EB%AA%A9+%ED%98%84%EC%83%81%EC%9D%B4%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fclickhouse-query-plan-contention%2F)[](https://mastodonshare.com/?text=%EC%B2%AD%EA%B5%AC+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%B4+%EA%B0%91%EC%9E%90%EA%B8%B0+%EB%8A%90%EB%A0%A4%EC%A1%8C%EC%8A%B5%EB%8B%88%EB%8B%A4.+%EC%9B%90%EC%9D%B8%EC%9D%80+ClickHouse%EC%9D%98+%EC%88%A8%EA%B2%A8%EC%A7%84+%EB%B3%91%EB%AA%A9+%ED%98%84%EC%83%81%EC%9D%B4%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fclickhouse-query-plan-contention%2F)[](https://www.threads.net/intent/post?text=%EC%B2%AD%EA%B5%AC+%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%9D%B4+%EA%B0%91%EC%9E%90%EA%B8%B0+%EB%8A%90%EB%A0%A4%EC%A1%8C%EC%8A%B5%EB%8B%88%EB%8B%A4.+%EC%9B%90%EC%9D%B8%EC%9D%80+ClickHouse%EC%9D%98+%EC%88%A8%EA%B2%A8%EC%A7%84+%EB%B3%91%EB%AA%A9+%ED%98%84%EC%83%81%EC%9D%B4%EC%97%88%EC%8A%B5%EB%8B%88%EB%8B%A4+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fclickhouse-query-plan-contention%2F)

## 관련 태그

[ClickHouse](https://blog.cloudflare.com/ko-kr/tag/clickhouse/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[성능](https://blog.cloudflare.com/ko-kr/tag/performance/)[엔지니어링](https://blog.cloudflare.com/ko-kr/tag/engineering/)[오픈 소스](https://blog.cloudflare.com/ko-kr/tag/open-source/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
