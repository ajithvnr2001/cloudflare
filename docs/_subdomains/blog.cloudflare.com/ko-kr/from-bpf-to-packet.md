---
url: https://blog.cloudflare.com/ko-kr/from-bpf-to-packet/
title: \ubc14\uc774\ud2b8\ucf54\ub4dc\uc5d0\uc11c \ubc14\uc774\ud2b8\ub85c- \uc790\ub3d9\ud654\ub41c Magic \ud328\ud0b7 \uc0dd\uc131 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:40.138340+00:00
---

# 바이트코드에서 바이트로- 자동화된 Magic 패킷 생성 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/from-bpf-to-packet/

[블로그](https://blog.cloudflare.com/ko-kr/)

[BPF](https://blog.cloudflare.com/ko-kr/tag/bpf/)[Z3](https://blog.cloudflare.com/ko-kr/tag/z3/)[네트워크](https://blog.cloudflare.com/ko-kr/tag/network/)+22개의 태그 더 보기

5개 태그5개 태그 보기

  * 게시물 태그
  * [BPF](https://blog.cloudflare.com/ko-kr/tag/bpf/)[Z3](https://blog.cloudflare.com/ko-kr/tag/z3/)[네트워크](https://blog.cloudflare.com/ko-kr/tag/network/)[리버스 엔지니어링](https://blog.cloudflare.com/ko-kr/tag/reverse-engineering/)[맬웨어](https://blog.cloudflare.com/ko-kr/tag/malware/)
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



[리버스 엔지니어링](https://blog.cloudflare.com/ko-kr/tag/reverse-engineering/)[맬웨어](https://blog.cloudflare.com/ko-kr/tag/malware/)

[BPF](https://blog.cloudflare.com/ko-kr/tag/bpf/)[Z3](https://blog.cloudflare.com/ko-kr/tag/z3/)[네트워크](https://blog.cloudflare.com/ko-kr/tag/network/)[리버스 엔지니어링](https://blog.cloudflare.com/ko-kr/tag/reverse-engineering/)[맬웨어](https://blog.cloudflare.com/ko-kr/tag/malware/)

2026년 4월 8일

# 바이트코드에서 바이트로: 자동화된 매직 패킷 생성

![Axel Boesenach](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VY2SG6VR1A7V1898SDG8.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Axel Boesenach](https://blog.cloudflare.com/ko-kr/author/axel-boesenach/)

8분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/from-bpf-to-packet/) 및 [日本語](https://blog.cloudflare.com/ja-jp/from-bpf-to-packet/).

![BLOG-3174 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4780X76NCAX209CBY30JSY.png&w=1200&h=675&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v/96Orx1trr1drw4OX36ez07Ozr/////v3/4uTyytHrydHw2N735uj27Ovt//////3/3uH0wcrswMrw1Nr45uf47evx////////4uX4xM7vxM/02d/86+z88vD1////////7vH919/11+D66O7/9vf/+vj6////////////7/T88Pb/+//////////+////////////////////////////////////////////////////////////////)

Linux 맬웨어는 종종 Linux 커널에 임베드하여 네트워크 트래픽 처리 방법을 사용자 지정할 수 있는 작은 실행 로직 비트인 버클리 패킷 필터(BPF) 소켓 프로그램에 숨어 있습니다. 인터넷에 가장 지속적으로 존재하는 위협 중 일부는 이러한 필터를 이용해 특정 "마법의" 패킷을 수신할 때까지 휴면 상태를 유지합니다. 이러한 필터는 길이가 수백 개에 달할 수 있고 복잡한 논리적 점프를 포함할 수 있으므로, 수작업으로 리버스 엔지니어링하려면 느린 프로세스이며 이로 인해 보안 연구자에게는 병목 현상이 발생합니다.

더 나은 방법을 찾기 위해 저희는 코드를 단순한 명령이 아닌 일련의 제약 조건으로 처리하는 방법인 기호 실행을 살펴보았습니다. Z3 정리 증명을 이용하면 악의적 필터의 역순으로 작업하여 이를 트리거하는 데 필요한 패킷을 자동으로 생성할 수 있습니다. 이번 게시물에서는 이를 자동화하는 도구를 구축하여, 몇 시간에 걸친 수동 조립 분석 작업을 단 몇 초 만에 끝낼 수 있는 작업을 소개합니다.

## 복잡성 한계

악성 필터를 분석하는 방법을 알아보기 전에 해당 필터를 실행하는 엔진을 이해해야 합니다. 버클리 패킷 필터(BPF)는 커널이 바이트코드 명령 세트를 기반으로 네트워크 스택에서 특정 패킷을 가져올 수 있는 매우 효율적인 기술입니다.

많은 최신 개발자가 관찰 가능성 및 보안을 위해 사용되는 강력한 기술인 [eBPF](https://blog.cloudflare.com/tag/ebpf/) (Extended BPF)에 익숙하지만, 이 게시물에서는 "기존" BPF에 초점을 맞춥니다. 원래 tcpdump와 같은 도구를 위해 설계된 클래식 BPF는 단 두 개의 레지스트리가 있는 단순한 가상 머신을 사용하여 네트워크 트래픽을 고속으로 평가합니다. 커널 내 깊숙이에서 실행되고 사용자 공간 도구로부터 트래픽을 "숨길 수 있으므로" 은밀한 백도어를 구축하려는 맬웨어 작성자가 선호하는 도구가 되었습니다.

[_LLM_](https://www.cloudflare.com/learning/ai/what-is-large-language-model/) 을 사용하여 BPF 명령의 컨텍스트 기반 표현을 생성하면 이미 분석가의 수동 오버헤드가 줄어들고 있으며, LLM을 통해 제공되는 컨텍스트가 추가되더라도 검증 조건에 해당하는 네트워크 패킷을 생성하는 것은 여전히 많은 작업이 될 수 있습니다.

BPF 프로그램이 20개 이하의 명령어만 있는 경우에는 대부분 이것이 문제가 되지 않지만, 일부 샘플에서 관찰된 바와 같이 BPF 프로그램이 100개 이상의 명령어로 구성되면 이것이 기하급수적으로 더 복잡해지고 시간이 많이 소요될 수 있습니다.

문제를 분석해 보면 결과에 따라 실행 경로를 계속 진행하거나, 실행을 중지하고 최종 결과를 확인하는 결과를 볼 수 있습니다.

이런 종류의 문제는 결정론적 결과를 가져옵니다. Z3는 주어진 제약 조건에서 문제를 해결할 방법을 갖춘 정리 증명인 Z3로 해결할 수 있습니다.

## 자료 A: BPFDoor

BPFDoor는 정교하고 패시브한 Linux 백도어로서, Red Menshen(Earth Bluecrow라고도 함)을 비롯한 중국 기반의 위협 행위자들이 사이버 스파이 활동을 하는 데 주로 사용됩니다. 이 맬웨어는 최소 2021년부터 활동해 왔으며, 통신, 교육, 정부 부문을 대상으로 손상된 네트워크에 은밀한 발판을 유지하도록 설계되었으며 아시아와 중동에서의 사업을 중심으로 합니다.

BPFDoor는 BPF를 사용하여 특정 네트워크 포트를 열지 않고도 모든 들어오는 트래픽을 모니터링합니다. 

### BPFDoor 예시 지침

[ _Fortinet_](https://www.fortinet.com/blog/threat-research/new-ebpf-filters-for-symbiote-and-bpfdoor-malware) 의 연구에서 공유된 샘플에 주목해 보겠습니다(82ed617816453eba2d755642e3efebfcbd19705ac626f6bc8ed238f4fc111bb0). BPF 명령어를 분석하고 몇 가지 주석을 추가하면 다음과 같이 작성할 수 있습니다.
    
    
    (000) ldh [0xc]                   ; Read halfword at offset 12 (EtherType)
    (001) jeq #0x86dd, jt 2, jf 6     ; 0x86DD (IPv6) -> ins 002 else ins 006
    (002) ldb [0x14]                  ; Read byte at offset 20 (Protocol)
    (003) jeq #0x11, jt 4, jf 15      ; 0x11 (UDP) -> ins 004 else DROP
    (004) ldh [0x38]                  ; Read halfword at offset 56 (Dst Port)
    (005) jeq #0x35, jt 14, jf 15     ; 0x35 (DNS) -> ACCEPT else DROP
    (006) jeq #0x800, jt 7, jf 15     ; 0x800 (IPv4) -> ins 007 else DROP
    (007) ldb [23]                    ; Read byte at offset 23 (Protocol)
    (008) jeq #0x11, jt 9, jf 15      ; 0x11 (UDP) -> ins 009 else DROP
    (009) ldh [20]                    ; Read halfword at offset 20 (fragment)
    (010) jset #0x1fff, jt 15, jf 11  ; fragmented -> DROP else ins 011
    (011) ldxb 4*([14]&0xf)           ; Load index (x) register ihl & 0xf
    (012) ldh [x + 16]                ; Read halfword at offset x+16 (Dst Port)
    (013) jeq #0x35, jt 14, jf 15     ; 0x35 (DNS) -> ACCEPT else DROP
    (014) ret #0x40000 (ACCEPT)
    (015) ret #0 (DROP)

위의 예에서는 ACCEPT 결과로 이어지는 두 가지 경로(5단계와 13단계)가 있음을 확인할 수 있습니다. 또한 오프셋과 값을 포함하여 특정 바이트를 검사하는 것을 명확하게 관찰할 수 있습니다. 

이러한 유효성 검사를 수행하고 ACCEPT 경로와 일치하는 모든 것을 추적하면 자동으로 패킷을 만들 수 있습니다.

### 최단 경로 계산

BPF 명령어에 제시된 조건을 검증하는 패킷의 최단 경로를 찾으려면 바람직하지 않은 조건으로 끝나지 않는 경로를 추적해야 합니다.

작은 대기열을 만드는 것으로 시작합니다. 이 대기열에는 몇 가지 중요한 데이터 포인트가 있습니다.

  * 다음 명령어에 대한 포인터입니다.
  * 실행된 명령어의 현재 경로 + 다음 명령어.



조건을 확인하는 명령어를 만날 때마다 부울 값을 사용하여 결과를 추적하고 이를 대기열에 저장하므로 ACCEPT 조건에 도달하기 전에 조건의 개수에 따라 경로를 비교하고 최단 경로를 계산할 수 있습니다. 의사 코드에서는 다음과 같이 가장 잘 표현할 수 있습니다.
    
    
    paths = []
    queue = dequeue([(0, [0])])
    
    while queue:
    	pc, path = queue.popleft()
    
    	if pc >= len(instructions):
                continue
    
    instruction = instructions[pc]
    	
    	if instruction.class == return_instruction:
    		if instruction_constant != 0:  # accept
    			paths.append(path)
    		continue  # drop or accept, stop parsing this instruction
    
    if instruction.class == jump_instruction:
    	if instruction.operation == unconditional_jump:
    		next_pc = pc + 1 + instruction_constant
    		queue.append((next_pc, path + [next_pc]))
    		continue
    
    	# Conditional jump, explore both
    	pc_true = pc + 1 + instruction.jump_true
    	pc_false = pc + 1 + instruction.jump_false
    	
    	if instruction.jump_true <= instruction.jump_false:
    		queue.append((pc_true, path + [pc_true]))
    		queue.append((pc_false, path + [pc_false]))
    	# else: same as above but reverse order of appending
    # else: sequential instruction, append to the queue

이전의 BPDoor 예시에 대해 이 로직을 실행하면 허용된 패킷의 최단 경로가 표시됩니다.
    
    
    (000) code=0x28 jt=0 jf=0  k=0xc     ; Read halfword at offset 12 (EtherType)
    (001) code=0x15 jt=0 jf=4  k=0x86dd  ; IPv6 packet
    (002) code=0x30 jt=0 jf=0  k=0x14    ; Read byte at offset 20 (Protocol)
    (003) code=0x15 jt=0 jf=11 k=0x11    ; Protocol number 17 (UDP)
    (004) code=0x28 jt=0 jf=0  k=0x38    ; Read word at offset 56 (Destination Port)
    (005) code=0x15 jt=8 jf=9  k=0x35    ; Destination port 53
    (014) code=0x06 jt=0 jf=0  k=0x40000 ; Accept

이는 이미 BPF 명령을 분석하고 백도어에 허용된 패킷이 어떻게 표시되는지 파악할 때 BPF 제약을 자동으로 해결하는 데 유용한 자동화입니다. 하지만 여기서 한 걸음 더 나아갈 수 있다면 어떨까요?

예상된 패킷을 자동화된 방식으로 다시 제공하는 작은 도구를 만들 수 있다면 어떨까요?

## Z3 및 scapy 사용

일련의 제약 조건이 주어질 때 문제를 해결하는 데 완벽한 도구 중 하나는 [_Z3_](https://github.com/z3Prover/z3)입니다. Microsoft에서 개발한 이 도구는 정리 증명이라고 할 수 있으며 내부에서 매우 복잡한 수학 연산을 수행하는 사용하기 쉬운 함수를 노출합니다.

유효한 Magic 패킷을 만들기 위해 사용할 또 다른 도구는 대화형 패킷 조작에 널리 사용되는 Python 라이브러리인 [_scapy_](https://github.com/secdev/scapy)입니다.

허용된 패킷의 경로를 파악할 방법이 이미 있다는 점을 고려할 때, 문제를 자체적으로 해결한 다음 이 솔루션을 네트워크 패킷의 각 오프셋에 있는 바이트로 변환하는 일만 남았습니다.

### 기호 실행

지정된 프로그램에서 수행된 경로를 탐색하는 일반적인 기술을 기호 실행이라고 합니다. 이 기술을 위해 Cloudflare는 제약 조건을 포함하여 변수로 사용할 수 있는 입력을 제공합니다. Cloudflare는 경로가 성공한 결과의 결과를 알고 있으므로, 도구를 조율하여 이러한 모든 성공적인 경로를 찾고 최종 결과를 맥락에 맞는 형식으로 표시할 수 있습니다.

이를 위해서는 확인 중인 조건의 결과로 상수, 레지스트리, 다양한 부울 연산자 등의 상태를 추적할 수 있는 소형 머신을 구현해야 합니다.
    
    
    class BPFPacketCrafter:
        MIN_PKT_SIZE = 64           # Minimum packet size (Ethernet + IP + UDP headers)
        LINK_ETHERNET = "ethernet"  # DLT_EN10MB - starts with Ethernet header
        LINK_RAW = "raw"            # DLT_RAW - starts with IP header directly
        MEM_SLOTS = 16              # Number of scratch memory slots (M[0] to M[15])
    
        def __init__(self, ins: list[BPFInsn], pkt_size: int = 128, ltype: str = "ethernet"):
            self.instructions = ins
            self.pkt_size = max(self.MIN_PKT_SIZE, pkt_size)
            self.ltype = ltype
    
            # Symbolic packet bytes
            self.packet = [BitVec(f"pkt_{i}", 8) for i in range(self.pkt_size)]
    
            # Symbolic registers (32-bit)
            self.A = BitVecVal(0, 32)  # Accumulator
            self.X = BitVecVal(0, 32)  # Index register
    
            # Scratch memory M[0-15] (32-bit words)
            self.M = [BitVecVal(0, 32) for _ in range(self.MEM_SLOTS)]

위의 코드로는 기호 실행 중에 상태를 유지하는 기계의 대부분을 다루었습니다. 물론 추적해야 할 조건이 더 있지만, 이러한 조건은 해결 과정에서 처리됩니다. ADD 명령어를 처리하기 위해 컴퓨터는 BPF 연산을 Z3 덧셈에 매핑합니다.
    
    
    def _execute_ins(self, insn: BPFInsn):
        cls = insn.cls
        if cls == BPFClass.ALU:
            op = insn.op
            src_val = BitVecVal(insn.k, 32) if insn.src == BPFSrc.K else self.X
            if op == BPFOp.ADD:
                self.A = self.A + src_val

다행히 BPF 명령어 세트는 비교적 구현하기 쉬운 작은 명령어 세트에 불과하므로 추적할 수 있는레지스터가 두 개뿐이라는 점은 분명히 환영할 만한 제약입니다!

이 상징적 처형의 전반적인 작용은 다음과 같이 추상적인 개요로 설명할 수 있습니다.

  * "x"(인덱싱) 및 "a"(누산기) 레지스를 기본 상태로 초기화합니다.
  * 성공적인 경로로 식별된 경로의 지침을 반복합니다.
    * 레지스트리 상태를 추적하여 비점프 명령어를 있는 그대로 실행합니다.
    * 점프 명령이 있는지 확인하고 분기를 사용해야 하는지 확인합니다.
  * Z3 check() 함수를 사용하여 조건이 주어진 제약(ACCEPT)을 충족하는지 확인합니다.
  * Z3 비트벡터 배열을 바이트로 변환합니다.
  * scapy를 사용하여 변환된 바이트의 패킷을 생성합니다.



Z3 솔버에서 구축한 제약 조건을 살펴보면 패킷 바이트를 구축하기 위해 Z3이 취한 실행 단계를 추적할 수 있습니다.
    
    
    [If(Concat(pkt_12, pkt_13) == 0x800,
        pkt_14 & 0xF0 == 0x40,
        True),
     If(Concat(pkt_12, pkt_13) == 0x800, pkt_14 & 0x0F >= 5, True),
     If(Concat(pkt_12, pkt_13) == 0x800, pkt_14 & 0x0F == 5, True),
     If(Concat(pkt_12, pkt_13) == 0x86DD,
        pkt_14 & 0xF0 == 0x60,
        True),
     0x86DD == ZeroExt(16, Concat(pkt_12, pkt_13)),
     0x11 == ZeroExt(24, pkt_20),
     0x35 == ZeroExt(16, Concat(pkt_56, pkt_57))]

Z3에 표시되는 제약 조건의 첫 번째 부분은 링크 계층 BPF 명령을 처리할 때 유효한 이더넷 IP를 구축할 수 있도록 추가된 제약 조건입니다. "If" 문은 감지된 프로토콜에 따라 특정 제약 조건을 적용합니다.

  * IPv4 로직(0x0800):
    * pkt_14 & 240 == 64: 바이트 14가 IP 헤더의 시작입니다. 0xF0 마스크는 버전이 4(0x40)인지 확인하기 위해 높은 니블(버전 필드)을 격리합니다.
    * pkt_14 & 15 == 5: 15 (0x0F), 낮은 니블을 격리(Ihl - 인터넷 Header Length). 따라서 헤더 길이는 5(20바이트)가 되어야 하며, 이는 옵션을 제외한 표준 크기입니다.
  * IPv6 로직(0x86dd):
    * pkt_14 & 240 == 0x60: 버전 필드가 버전 6(0x60)인지 확인



다른 값을 검사하는 두 번째 부분을 보면 네트워크 패킷 값을 관찰할 수 있습니다.

  * 0x86DD: IPv6 헤더의 패킷 조건입니다.
  * 0x11: UDP 프로토콜 번호.
  * 0x35: 대상 포트(53).



예상 값 옆에 주어진 패킷에서 해당 값이 존재해야 하는 위치의 바이트 오프셋을 볼 수 있습니다(예: pkt_12, pkt_13).

### 패킷 제작

특정 오프셋에 어떤 바이트가 존재해야 하는지 확인했으니, 이제 scapy를 사용해 이를 실제 네트워크 패킷으로 변환할 수 있습니다. 이전 Z3 제약 조건의 바이트에서 새 패킷을 생성하면 패킷이 어떻게 보이는지 명확하게 확인할 수 있으며 추가 처리를 위해 저장할 수 있습니다.
    
    
    ###[ Ethernet ]###
      dst       = 00:00:00:00:00:00
      src       = 00:00:00:00:00:00
      type      = IPv6                 <-- IPv6 Packet
    ###[ IPv6 ]###
         version   = 6
         tc        = 0
         fl        = 0
         plen      = 0
         nh        = UDP               <-- UDP Protocol
         hlim      = 0
         src       = ::
         dst       = ::
    ###[ UDP ]###
            sport     = 0
            dport     = domain         <-- Port 53
            len       = 0
            chksum    = 0x0

이 새로 만들어진 패킷은 추가 연구에 사용하거나 네트워크를 통해 스캔하여 이러한 임플란트의 존재를 식별하는 데 사용할 수 있습니다. 

## 직접 사용해 보세요

특정 BPF 지침 세트가 수행하는 작업을 이해하는 것은 번거롭고 시간이 많이 소모되는 작업일 수 있습니다. 사용된 예는 총 16개 명령에 불과하지만, 200개 이상의 명령인 샘플을 이해하는 데 적어도 하루는 걸렸을 것입니다. 이제 Z3 솔버를 사용하여 이 시간을 초 단위로 단축하고 허용된 패킷의 경로뿐만 아니라 이 패킷의 뼈대까지 표시할 수 있습니다.

커뮤니티에서 BPF 기반 임플란트의 해체를 자동화할 수 있도록 **filterforge** 도구를 오픈 소스로 제공했습니다. 여러분은 [_저희 GitHub 리포지토리_](https://github.com/cloudflare/filterforge)에서 소스 코드와 사용 예시를 찾아보실 수 있습니다.

이 연구 결과를 게시하고, 분석가가 BPF 명령어를 알아내는 데 소요되는 시간을 줄여주는 도구를 공유함으로써, 다른 분들의 추가 연구에 이 형태의 자동화를 확장하기 위한 계기가 되길 바랍니다.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffrom-bpf-to-packet%2F&t=%EB%B0%94%EC%9D%B4%ED%8A%B8%EC%BD%94%EB%93%9C%EC%97%90%EC%84%9C%20%EB%B0%94%EC%9D%B4%ED%8A%B8%EB%A1%9C%3A%20%EC%9E%90%EB%8F%99%ED%99%94%EB%90%9C%20%EB%A7%A4%EC%A7%81%20%ED%8C%A8%ED%82%B7%20%EC%83%9D%EC%84%B1)[](https://x.com/intent/post?text=%EB%B0%94%EC%9D%B4%ED%8A%B8%EC%BD%94%EB%93%9C%EC%97%90%EC%84%9C+%EB%B0%94%EC%9D%B4%ED%8A%B8%EB%A1%9C%3A+%EC%9E%90%EB%8F%99%ED%99%94%EB%90%9C+%EB%A7%A4%EC%A7%81+%ED%8C%A8%ED%82%B7+%EC%83%9D%EC%84%B1&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffrom-bpf-to-packet%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffrom-bpf-to-packet%2F)[](https://bsky.app/intent/compose?text=%EB%B0%94%EC%9D%B4%ED%8A%B8%EC%BD%94%EB%93%9C%EC%97%90%EC%84%9C+%EB%B0%94%EC%9D%B4%ED%8A%B8%EB%A1%9C%3A+%EC%9E%90%EB%8F%99%ED%99%94%EB%90%9C+%EB%A7%A4%EC%A7%81+%ED%8C%A8%ED%82%B7+%EC%83%9D%EC%84%B1+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffrom-bpf-to-packet%2F)[](https://mastodonshare.com/?text=%EB%B0%94%EC%9D%B4%ED%8A%B8%EC%BD%94%EB%93%9C%EC%97%90%EC%84%9C+%EB%B0%94%EC%9D%B4%ED%8A%B8%EB%A1%9C%3A+%EC%9E%90%EB%8F%99%ED%99%94%EB%90%9C+%EB%A7%A4%EC%A7%81+%ED%8C%A8%ED%82%B7+%EC%83%9D%EC%84%B1&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffrom-bpf-to-packet%2F)[](https://www.threads.net/intent/post?text=%EB%B0%94%EC%9D%B4%ED%8A%B8%EC%BD%94%EB%93%9C%EC%97%90%EC%84%9C+%EB%B0%94%EC%9D%B4%ED%8A%B8%EB%A1%9C%3A+%EC%9E%90%EB%8F%99%ED%99%94%EB%90%9C+%EB%A7%A4%EC%A7%81+%ED%8C%A8%ED%82%B7+%EC%83%9D%EC%84%B1+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffrom-bpf-to-packet%2F)

## 관련 태그

[BPF](https://blog.cloudflare.com/ko-kr/tag/bpf/)[Z3](https://blog.cloudflare.com/ko-kr/tag/z3/)[네트워크](https://blog.cloudflare.com/ko-kr/tag/network/)[리버스 엔지니어링](https://blog.cloudflare.com/ko-kr/tag/reverse-engineering/)[맬웨어](https://blog.cloudflare.com/ko-kr/tag/malware/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
