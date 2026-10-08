---
url: https://blog.cloudflare.com/ko-kr/announcing-workers-smart-placement/
title: \uad6c\uc131\uc774 \ud544\uc694\ud558\uc9c0 \uc54a\uc73c\uba70 \ucf54\ub4dc\ub97c \ubc31\uc5d4\ub4dc\uc5d0 \uac00\uae5d\uac8c \uc774\ub3d9\ud558\uc5ec \uc560\ud50c\ub9ac\ucf00\uc774\uc158 \uc18d\ub3c4\ub97c \ub192\uc774\ub294 Smart Placement | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:39:57.609782+00:00
---

# 구성이 필요하지 않으며 코드를 백엔드에 가깝게 이동하여 애플리케이션 속도를 높이는 Smart Placement | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/announcing-workers-smart-placement/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)+33개의 태그 더 보기

6개 태그6개 태그 보기

  * 게시물 태그
  * [Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)
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



[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)

2023년 5월 16일

# 구성이 필요하지 않으며 코드를 백엔드에 가깝게 이동하여 애플리케이션 속도를 높이는 Smart Placement

![Michael Hart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Y5FGZZS90ZJA5EFQW15Q.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Serena Shah-Simpson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45E4TK6GHZXWH66VF37ZEZ.PNG&w=64&h=64&f=webp&fit=cover&position=center)![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michael Hart](https://blog.cloudflare.com/ko-kr/author/michael-hart/), [Serena Shah-Simpson](https://blog.cloudflare.com/ko-kr/author/serena/) 및 [Tanushree Sharma](https://blog.cloudflare.com/ko-kr/author/tanushree/)

8분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/announcing-workers-smart-placement/), [Español](https://blog.cloudflare.com/es-es/announcing-workers-smart-placement/), [日本語](https://blog.cloudflare.com/ja-jp/announcing-workers-smart-placement/), [繁體中文](https://blog.cloudflare.com/zh-tw/announcing-workers-smart-placement/), [简体中文](https://blog.cloudflare.com/zh-cn/announcing-workers-smart-placement/), [Português](https://blog.cloudflare.com/pt-br/announcing-workers-smart-placement/), [Русский](https://blog.cloudflare.com/ru-ru/announcing-workers-smart-placement/) 및 [Polski](https://blog.cloudflare.com/pl-pl/announcing-workers-smart-placement/).

![Smart Placement speeds up applications by moving code close to your backend — no config needed](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW463REMTYFQ9WDSW6E67JH9.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA///////+9PPv7ezk7+7l9PPs8vPv7O3s////////9fTu7erg7uvf8/Dm8vHs7u7t////////9/Xw7ure7+na8u7h8/Hr8PDw////////+vj08ezh8evc9fDj9vPu9PP1//////////379vLq9vHl+vXs+/n1+fj6////////////+/n1+/jz//35///+/f7////////////////+///+////////////////////////////////////////////)

웹 사이트 로딩 속도가 느리거나 애플리케이션이 업데이트를 위해 API를 호출해야 할 때 멈추는 것 같은 불편함을 누구나 경험해 본 적이 있을 것입니다. 즉각 이루어지지 않으면 신경이 다른 데 쏠리게 됩니다...

작업 속도가 빨라지게 하는 한 가지 방법은 리소스를 사용자에게 최대한 가까운 곳에서 가져오는 것이며, Cloudflare에서는 대부분의 사용자에 대하여 밀리초 이내에 실행하는 컴퓨팅으로 이를 실행하고 있습니다. 그러나 직관적이지 않은 것처럼 보일 수 있지만, 때로는 사용자에게 더 가까운 곳에서 리소스를 가져오면 실제로 애플리케이션 속도가 느려질 수 있습니다. 애플리케이션을 최종 사용자와 가까운 곳에 있지 않은 API, 데이터베이스, 기타 리소스에 연결해야 하는 경우, 사용자가 아니라 리소스 근처에서 애플리케이션을 실행하는 편이 성능이 더 좋을 수 있습니다.

따라서 오늘 모든 상호 작용을 가장 빠르게 수행하는 Workers 및 Pages Functions를 위한 Smart Placement를 발표하게 되어 기쁩니다. Cloudflare에서는 Smart Placement를 통해 컴퓨팅 자원을 최적의 위치로 이동시켜 애플리케이션의 속도를 높이는 방식으로 서버리스 컴퓨팅을 Supercloud로 도입하고 있습니다. 가장 좋은 점은 Smart Placement가 완전히 자동이며 추가 입력(예: 두려운 '지역')이 없다는 것입니다.

Smart Placement는 모든 Workers 및 Pages 고객이 지금 오픈 베타로 이용할 수 있습니다!

[Smart Placement 작동 방식에 대한 데모를 확인하세요!](https://smart-placement-demo.pages.dev/)

## 서버리스 전환

Cloudflare의 Anycast 네트워크는 _사용자와 가까운 곳에서 요청을 즉각_ 처리하도록 구축되었습니다. 개발자의 입장에서는, 바로 이런 점이 Cloudflare의 서버리스 컴퓨팅 제품인 Cloudflare Workers가 아주 매력적인 이유입니다. 경쟁업체는 '지역'에 국한되어 있는 반면, Workers는 모든 곳에서 실행되므로 지구라는 하나의 지역으로 묶여 있습니다. Workers에서만 전적으로 처리되는 요청은 원본 서버에 도달할 필요도 없이 바로 그 시점에 즉석에서 처리될 수 있습니다.

이 서버리스라는 개념은 원래 가벼운 작업을 위한 것으로 간주되었지만, 최근 몇 년 동안 서버리스 컴퓨팅도 변화하고 있습니다. 서버리스는 단순히 아키텍처를 보강하는 것이 아니라 원본 서버와 자체 관리형 인프라에 의존하는 전통적인 아키텍처를 대체하는 데 사용되고 있습니다. Workers 및 Pages 사용자에게 있어서 이러한 사용 사례가 늘어나고 있습니다.

### 서버리스에는 상태가 필요함

서버리스로 전환하고 전체 애플리케이션을 Workers에서 구축함에 따라 데이터가 필요하게 되었습니다. 이전 작업 또는 이벤트에 대한 정보를 저장하면 개인화된 대화형 애플리케이션을 구축할 수 있습니다. 예를 들어 사용자 프로필을 작성하고, 사용자가 어느 페이지에서 종료했는지, 사용자가 장바구니에 담은 SKU는 무엇인지 저장해야 하는 경우, 이러한 모든 정보는 상태를 유지하는 데 사용되는 데이터 포인트에 매핑됩니다. 관계형 데이터베이스, 키값 저장소, blob 스토리지, API 등의 백엔드 서비스를 통해 상태 저장 애플리케이션을 구축할 수 있습니다.

### Cloudflare 컴퓨팅 + 스토리지: 강력한 듀오

Cloudflare의 스토리지 제품군은 Workers KV, Durable Objects, D1, [R2](https://www.cloudflare.com/developer-platform/r2/) 등 점점 더 늘어나고 있습니다. 데이터 제품이 성숙해지면서 저희가 해당 제품과 Workers의 상호 작용에 대해 깊이 고려하므로 여러분은 그에 대해 숙고할 필요가 없습니다! 예를 들어, 경우에 따라 성능이 더 나아질 수 있는 또 다른 접근 방식은 사용자에게 가까운 곳에서 컴퓨팅하지 않고 스토리지를 이동시키는 것입니다. 사용자가 실시간 게임을 제작하기 위해 Durable Objects를 사용하는 경우, 저희는 모든 사용자의 대기 시간을 최소화하기 위해 Durable Objects를 이동시킬 수 있습니다.

향후 상태에 대한 Cloudflare의 목표는 사용자가 모드를 '스마트'로 설정하고 저희가 추가 구성 없이 사용자의 모든 리소스가 최적으로 배치되었는지 평가하는 것입니다.

### Cloudflare 컴퓨팅 + ${backendService}

오늘날 Smart Placement의 주요 사용 사례는 외부 데이터베이스나 타사 API와 같이 Cloudflare의 서비스가 아닌 서비스를 애플리케이션에 대하여 사용하는 경우입니다.

자체 호스팅이든 관리형 서비스이든 관계없이 많은 백엔드 서비스는 중앙 집중화되어 있으므로 데이터가 단일 위치에 저장되고 관리됩니다. 귀사의 사용자는 전 세계에 걸쳐 있고, Workers도 전 세계에 걸쳐 사용되지만, 백엔드는 중앙 집중화되어 있습니다.

코드가 백엔드 서비스에 여러 번 요청을 보내는 경우 해당 요청이 지구 전역을 여러 번 횡단하게 되어 성능에 큰 영향이 미칠 수 있습니다. 일부 서비스는 데이터 복제 및 캐싱을 제공하여 성능 향상에 도움이 되지만, 데이터 일관성 및 높은 비용과 같은 단점도 있으므로 사용 사례와 비교하여 고려해야 합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A map of the globe illustrating global users, global workers and a centralized database. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4877KTAFZ54HDMT6TVBXPP.png&w=715&h=402&f=webp&fit=cover&position=center)

Cloudflare 네트워크는 [전 세계 인터넷 연결 인구의 95%로부터 50ms](https://www.cloudflare.com/network/) 이내의 거리에 있습니다. 이를 뒤집어서 생각해 보면, Cloudflare는 귀사의 백엔드 서비스와도 매우 가깝습니다.

## 애플리케이션 성능이 곧 사용자 경험입니다

예를 들면서 백엔드 서비스와 가까운 곳으로 컴퓨팅을 이동시키면 애플리케이션 대기 시간을 어떻게 줄일 수 있는지 알아보겠습니다.

Workers에서 실행되는 애플리케이션에 액세스하는 사용자가 호주 시드니에 있다고 가정해 보겠습니다. 이 애플리케이션은 사용자의 요청을 처리하기 위해 독일 프랑크푸르트에 있는 데이터베이스까지 세 번 왕복합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-1787 Embedded Image - krvyST](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46K0J7CQVHJM69K0X2F7HW.png&w=715&h=254&f=webp&fit=cover&position=center)

우리는 병목 현상이 Worker가 데이터베이스를 여러 번 왕복하는 데 걸리는 시간일 것으로 직관적으로 추측할 수 있습니다. 사용자와 가까운 곳에서 Worker를 호출하는 대신 데이터베이스에 가장 가까운 데이터 센터에서 Worker를 호출한다면 어떻게 될까요?

![wAAAABJRU5ErkJggg==](https://blog.cloudflare.com/_emdash/api/media/file/01KW46JG8Q61D0TYTP363C4KP2)

이를 테스트해 보겠습니다.

Smart Placement가 활성화되지 않은 Worker의 요청 지속 시간을 측정하고 이를 Smart Placement가 활성화된 Worker와 비교했습니다. 두 테스트 모두를 위해 저희는 시드니에서 eu-central-1(프랑크푸르트)에 위치한 [Upstash](https://upstash.com/) 인스턴스(무료 등급)를 3번 왕복하는 Worker에 3,500개의 요청을 보냈습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![A graph showing request duration with and without Smart Placement enabled. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4768M6PTQMJX5HNQCQ2S8V.png&w=715&h=432&f=webp&fit=cover&position=center)

그 결과는 명확합니다! 이 예에서는 Worker를 백엔드에 가깝게 이동시켰을 때 **애플리케이션 성능이 4~8배개선되었습니다**.

## 네트워크상의 결정은 사람의 결정이 되어서는 안 됩니다

개발자는 가장 잘하는 일인 애플리케이션 구축에 집중해야 합니다. 애플리케이션을 더 빠르게 만들기 위한 네트워크 결정에 대해서는 걱정할 필요 없이 말입니다.

Cloudflaredptj는 고유한 관점을 가지고 있습니다. 저희 네트워크에서는 사용자, Cloudflare 데이터 센터, 백엔드 서버 간의 최적 경로에 대한 정보가 수집됩니다. 저희는 [Argo Smart Routing](https://blog.cloudflare.com/argo/)을 통해 이 분야에서 많은 경험을 쌓았습니다. Smart Placement는 이러한 요소를 고려하여 자동으로 Worker를 최상의 위치에 배치하여 전체 요청 지속 시간을 최소화합니다.

그렇다면 Smart Placement는 어떻게 작동할까요?

Smart Placement는 '설정' 탭이나 wrangler.toml 파일에서 Worker별로 활성화할 수 있습니다.
    
    
    [placement]
    mode = "smart"

Worker 또는 Pages Function에서 Smart Placement를 활성화하면 Smart Placement 알고리즘은 Worker의 가져오기 요청(하위 요청이라고도 함)을 실시간으로 분석합니다. 그런 다음 이를 네트워크에서 집계된 대기 시간 데이터와 비교합니다. 평균적으로 Worker가 백엔드 리소스에 대해 두 개 이상의 하위 요청을 하는 것이 감지되면 최적의 데이터 센터에서 자동으로 Worker가 호출됩니다!

정당한 이유로 스마트 배치 알고리즘에서 고려하지 않는 백엔드 서비스가 몇 가지 있습니다.

  * 전 세계적으로 분산된 서비스: Worker가 통신하는 서비스가 여러 지역에 걸쳐 분산된 경우 Smart Placement는 적합하지 않습니다. 이는 Smart Placement 최적화에서 자동으로 제외됩니다.
  * 분석 또는 로깅 서비스: 분석 또는 로깅 서비스에 대한 요청이 애플리케이션의 중요 경로에 있을 필요는 없습니다. 코드를 계측할 때 사용자에 대한 응답이 차단되지 않도록 [`WaitUntil()`](https://developers.cloudflare.com/workers/runtime-apis/fetch-event/?ref=blog.cloudflare.com#waituntil)을 사용해야 합니다. 사용자 관점에서는 `WaitUntil()`이 요청 지속 시간에 영향을 미치지 않으므로 저희는 Smart Placement 최적화에서 분석/로깅 서비스를 자동으로 제외합니다.



Smart Placement 알고리즘에서 고려되지 않는 서비스 목록은 Cloudflare [문서](https://developers.cloudflare.com/workers/platform/smart-placement/#supported-backends)를 참조하세요.

Smart Placement가 작동하면 Worker에서 새로운 'Request Duration' 탭을 확인할 수 있습니다. Cloudflare에서는 Smart Placement를 활성화하지 않은 상태에서 요청의 1%를 라우팅하므로 사용자는 요청 지속 시간에 미치는 영향을 확인할 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![Request duration with and without Smart Placement shown on the Workers dashboard. ](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW456H2J1AGEQ2GCCPGS38ZS.png&w=715&h=388&f=webp&fit=cover&position=center)

그리고, 정말이지 그 정도로 간단합니다!

저희 [데모](https://smart-placement-demo.pages.dev/)를 확인하여 Smart Placement를 사용해 보세요(너무 재미 있답니다!). 자세한 내용은 [개발자 문서](https://developers.cloudflare.com/workers/platform/smart-placement/)를 참조하세요.

## Smart Placement의 다음 단계는 무엇일까요?

이제 시작일 뿐입니다! Smart Placement를 개선할 수 있는 다양한 아이디어가 있습니다.

  * 애플리케이션에서 여러 백엔드를 사용할 때 최적의 위치 계산 지원
  * 미세 조정된 배치(예: Worker가 경로에 따라 여러 백엔드를 사용하는 경우. 저희는 Worker별이 아닌 경로별로 최적의 배치를 계산합니다)
  * TCP 기반 연결 지원



여러분의 의견을 듣고 싶습니다! 피드백이나 기능에 대한 요청이 있다면 [Cloudflare Developer Discord](https://discord.com/invite/cloudflaredev)를 통해 연락해 주시기 바랍니다.

### Cloudflare TV에서 보기

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fannouncing-workers-smart-placement%2F&t=%EA%B5%AC%EC%84%B1%EC%9D%B4%20%ED%95%84%EC%9A%94%ED%95%98%EC%A7%80%20%EC%95%8A%EC%9C%BC%EB%A9%B0%20%EC%BD%94%EB%93%9C%EB%A5%BC%20%EB%B0%B1%EC%97%94%EB%93%9C%EC%97%90%20%EA%B0%80%EA%B9%9D%EA%B2%8C%20%EC%9D%B4%EB%8F%99%ED%95%98%EC%97%AC%20%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%20%EC%86%8D%EB%8F%84%EB%A5%BC%20%EB%86%92%EC%9D%B4%EB%8A%94%20Smart%20Placement)[](https://x.com/intent/post?text=%EA%B5%AC%EC%84%B1%EC%9D%B4+%ED%95%84%EC%9A%94%ED%95%98%EC%A7%80+%EC%95%8A%EC%9C%BC%EB%A9%B0+%EC%BD%94%EB%93%9C%EB%A5%BC+%EB%B0%B1%EC%97%94%EB%93%9C%EC%97%90+%EA%B0%80%EA%B9%9D%EA%B2%8C+%EC%9D%B4%EB%8F%99%ED%95%98%EC%97%AC+%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98+%EC%86%8D%EB%8F%84%EB%A5%BC+%EB%86%92%EC%9D%B4%EB%8A%94+Smart+Placement&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fannouncing-workers-smart-placement%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fannouncing-workers-smart-placement%2F)[](https://bsky.app/intent/compose?text=%EA%B5%AC%EC%84%B1%EC%9D%B4+%ED%95%84%EC%9A%94%ED%95%98%EC%A7%80+%EC%95%8A%EC%9C%BC%EB%A9%B0+%EC%BD%94%EB%93%9C%EB%A5%BC+%EB%B0%B1%EC%97%94%EB%93%9C%EC%97%90+%EA%B0%80%EA%B9%9D%EA%B2%8C+%EC%9D%B4%EB%8F%99%ED%95%98%EC%97%AC+%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98+%EC%86%8D%EB%8F%84%EB%A5%BC+%EB%86%92%EC%9D%B4%EB%8A%94+Smart+Placement+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fannouncing-workers-smart-placement%2F)[](https://mastodonshare.com/?text=%EA%B5%AC%EC%84%B1%EC%9D%B4+%ED%95%84%EC%9A%94%ED%95%98%EC%A7%80+%EC%95%8A%EC%9C%BC%EB%A9%B0+%EC%BD%94%EB%93%9C%EB%A5%BC+%EB%B0%B1%EC%97%94%EB%93%9C%EC%97%90+%EA%B0%80%EA%B9%9D%EA%B2%8C+%EC%9D%B4%EB%8F%99%ED%95%98%EC%97%AC+%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98+%EC%86%8D%EB%8F%84%EB%A5%BC+%EB%86%92%EC%9D%B4%EB%8A%94+Smart+Placement&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fannouncing-workers-smart-placement%2F)[](https://www.threads.net/intent/post?text=%EA%B5%AC%EC%84%B1%EC%9D%B4+%ED%95%84%EC%9A%94%ED%95%98%EC%A7%80+%EC%95%8A%EC%9C%BC%EB%A9%B0+%EC%BD%94%EB%93%9C%EB%A5%BC+%EB%B0%B1%EC%97%94%EB%93%9C%EC%97%90+%EA%B0%80%EA%B9%9D%EA%B2%8C+%EC%9D%B4%EB%8F%99%ED%95%98%EC%97%AC+%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98+%EC%86%8D%EB%8F%84%EB%A5%BC+%EB%86%92%EC%9D%B4%EB%8A%94+Smart+Placement+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fannouncing-workers-smart-placement%2F)

## 관련 태그

[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)[데이터베이스](https://blog.cloudflare.com/ko-kr/tag/database/)[서버리스](https://blog.cloudflare.com/ko-kr/tag/serverless/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
