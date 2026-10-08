---
url: https://blog.cloudflare.com/ko-kr/quic-death-spiral-fix/
title: '\uc720\ud734'\uac00 \uc720\ud734\uac00 \uc544\ub2d0 \ub54c: Linux \ucee4\ub110 \ucd5c\uc801\ud654\uac00 QUIC \ubc84\uadf8\uac00 \ub41c \ubc29\ubc95 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:46:37.419668+00:00
---

# '유휴'가 유휴가 아닐 때: Linux 커널 최적화가 QUIC 버그가 된 방법 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/quic-death-spiral-fix/

[블로그](https://blog.cloudflare.com/ko-kr/)

[HTTP3](https://blog.cloudflare.com/ko-kr/tag/http3/)[QUIC](https://blog.cloudflare.com/ko-kr/tag/quic/)[QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)+44개의 태그 더 보기

7개 태그7개 태그 보기

  * 게시물 태그
  * [HTTP3](https://blog.cloudflare.com/ko-kr/tag/http3/)[QUIC](https://blog.cloudflare.com/ko-kr/tag/quic/)[QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[네트워킹](https://blog.cloudflare.com/ko-kr/tag/networking/)[디버깅](https://blog.cloudflare.com/ko-kr/tag/debugging/)[정체 제어](https://blog.cloudflare.com/ko-kr/tag/congestion-control/)
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



[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[네트워킹](https://blog.cloudflare.com/ko-kr/tag/networking/)[디버깅](https://blog.cloudflare.com/ko-kr/tag/debugging/)[정체 제어](https://blog.cloudflare.com/ko-kr/tag/congestion-control/)

[HTTP3](https://blog.cloudflare.com/ko-kr/tag/http3/)[QUIC](https://blog.cloudflare.com/ko-kr/tag/quic/)[QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[네트워킹](https://blog.cloudflare.com/ko-kr/tag/networking/)[디버깅](https://blog.cloudflare.com/ko-kr/tag/debugging/)[정체 제어](https://blog.cloudflare.com/ko-kr/tag/congestion-control/)

2026년 5월 12일

# '유휴'가 유휴가 아닐 때: Linux 커널 최적화가 QUIC 버그가 된 방법

![Esteban Carisimo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VSSKPEBK3K5ND6JZ67YP.webp&w=64&h=64&f=webp&fit=cover&position=center)![Antonio Vicente](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487NFE7AY4B70WNGYX9WZ9.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Esteban Carisimo](https://blog.cloudflare.com/ko-kr/author/esteban-carisimo/) 및 [Antonio Vicente](https://blog.cloudflare.com/ko-kr/author/antonio-vicente/)

13분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/quic-death-spiral-fix/) 및 [日本語](https://blog.cloudflare.com/ja-jp/quic-death-spiral-fix/).

![BLOG-3260 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VSCEX3RARQSM9H9JQNVR.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////787/Hy5enu6uzy8vL28/Ly7Ozp////////7PH14Ojx5Ov17/L58fP16+3s////////6/L53Oj14Ov57fP98fT57PDw////////7fb+3ev54e397vX/8/f+7/P0////////9Pv/5fD+6PL/9Pn/+Pv/8/f5/////////P//8Pb/8/f/+/7//v//+fv9////////////+fv/+/z//////////f7//////////////f3///7//////////v//)

[_RFC 9438_](https://www.rfc-editor.org/rfc/rfc9438.html)로 표준화된 CUBIC은 Linux의 기본 정체 컨트롤러이며, 그 결과로 공용 인터넷에 있는 대부분의 TCP 및 QUIC 연결이 가용 대역폭을 탐색하고, 손실이 감지되면 후퇴하고, 그 후에 복구하는 방법을 관장합니다. Cloudflare에서 오픈 소스로 구현한 QUIC인 [ _quiche_](https://github.com/cloudflare/quiche)는 CUBIC을 기본 정체 컨트롤러로 사용하며, 이는 이 코드가 Cloudflare에서 제공하는 트래픽의 상당 부분에 대해 중요한 경로에 있음을 의미합니다.

이 게시물에서는 CUBIC의 혼잡 기간(cwnd)이 최소한으로 영구적으로 고정되어 혼잡 중단 이벤트에서 절대 복구되지 않는 버그에 대해 이야기하려고 합니다.

이야기는 CUBIC를 RFC [_9438 §4.2-12에_](https://www.rfc-editor.org/rfc/rfc9438.html#section-4.2-12) 설명된 앱 제한 제외 규정에 맞게 만들기 위한 [_Linux 커널 변경으로_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) 시작됩니다. TCP 의 실제 문제에 대한 수정 사항으로, QUIC 구현으로 포팅되었을 때 quiche에서 예상치 못한 동작이 나타났습니다. 한 줄 수정이 사이클을 깨뜨렸습니다. 결국 행복했습니다.

## CUBIC의 논리 요약

핵심 문제를 자세히 살펴보기 전에, 혼잡 제어 알고리즘(CCA)에 대해 간략히 살펴보세요.

CCA가 돌리는 중앙 조절 장치는 **혼잡 윈도우** (`cwnd`)입니다. 이는 언제든지 전송 중일 수 있는(전송되었지만 아직 승인되지 않은) 바이트 수에 대한 발신자 측 제한입니다. 더 큰 `cwnd`는 발신자가 왕복당 더 많은 데이터를 푸시할 수 있도록 하며, 더 작은 `cwnd`는 이를 제한합니다. CUBIC을 포함한 모든 손실 기반 CCA는 궁극적으로 네트워크가 정상일 때 `cwnd`를 늘리고 그렇지 않을 때 줄이는 방법에 대한 정책입니다.

본질적으로 CCA는 네트워크의 "가용한 대역폭"을 추론해 데이터 전송을 극대화하는 것을 목표로 합니다. 아무도 1Gbps 구독에 비용을 지불하고 그 일부만 사용하고 싶어 하지 않기 때문입니다. CUBIC가 속한 손실 기반 알고리즘 제품군은 다음과 같은 기본적인 전제를 기반으로 작동합니다. (1) 패킷 손실이 없는 경우, 전송 속도를 높입니다(즉, 대역폭 활용도를 높입니다). (2) 손실이 있는 경우, 손실 기반 알고리즘은 네트워크 용량이 초과되었다고 가정하고, 발신자는 다시 오프라인(즉, 대역폭 사용률 감소).

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image5](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45F1EAW72WCHZ78GX5HT44.png&w=715&h=310&f=webp&fit=cover&position=center)

이 논리는 여러 해에 걸쳐 재검토된 몇 가지 가정을 기반으로 합니다. 그러나 다음을 위해 해당 토론을 저장하겠습니다.

## 증상: 61% 실패하는 테스트

수신 프록시 통합 테스트 파이프라인에서 발생하는 예상치 못한 장애에 대한 보고를 통해 Cloudflare 조사는 시작되었습니다. 이러한 불규칙한 동작은 연결 초기에 큰 손실이 발생한 시나리오에서 CUBIC를 평가한 테스트에서 나타났습니다. 

혼잡도 붕괴 후 복구는 흔하지 않은 방식이지만, 혼잡 컨트롤러가 처리해야 하는 방식입니다. 대부분의 혼잡 제어 테스트는 알고리즘의 정상 상태 및 증가 단계를 시험합니다. 연결이 다운된 후 최소한 cwnd에서 발생하는 조사가 훨씬 적습니다. 상태 공간의 이 구석에 있는 버그는 처리량 대시보드에서 보이지 않으며, 정적 검토에서는 감지할 수 없으며, 의도적으로 CCA를 삽입하고 다시 올라갈 수 있는지 여부를 관찰할 때에만 표면화됩니다. 이것이 바로 이 테스트에서 수행한 결과입니다.

시뮬레이션된 테스트 설정에는 다음과 같은 세부 정보가 포함됩니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image6](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47XTRR7C32QNFXD4R2P2QP.png&w=715&h=224&f=webp&fit=cover&position=center)

  * 로컬(localhost)에서 실행되는 Quiche HTTP/3 클라이언트 및 서버
  * RTT = 10ms(구성에서 설정)
  * HTTP/3를 통한 10MB 파일 다운로드
  * CUBIC 정체 제어 사용
  * 처음 2초 동안 30% 무작위 패킷 손실이 주입됨
  * 2초 후, 손실이 완전히 멈춤
  * 이 테스트에서는 다운로드를 완료하는 데 10초의 넉넉한 제한 시간 초과가 있으며, 이는 4~5초 내에 완료될 것으로 예상됩니다



예상되는 동작은 간단합니다. CUBIC은 손실 단계에서 일부 히트를 수신하고, 정체 창을 줄이며, 손실이 멈춘 다음 꾸준히 속도를 높이고 제한 시간 초과 내에 다운로드를 잘 완료해야 합니다. 대신, 100번 실행한 결과, 약 60%의 테스트가 10초라는 넉넉한 제한 시간 초과 내에 다운로드를 완료하지 못했습니다.

## 이상: 손실이 없는 999개의 상태 전환

우리는 패킷 손실 이벤트로[ _quiche의 qlog_](https://github.com/cloudflare/quiche) 출력을 계측하고 시각화를 구축하여 정체 컨트롤러 내부에서 무슨 일이 일어나고 있는지 이해했습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image10](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44FRE5WJ50JFBR32K8E6Y2.png&w=715&h=459&f=webp&fit=cover&position=center)

_실패한 테스트의 연결 개요. T=2가 지나면 패킷 손실이 완전히 중지되지만, cwnd는 최소 레벨에 고정되어 있으며 혼잡 상태는 14ms마다 복구와 혼잡 회피 사이를 오가게 됩니다._

2초(2000ms)가 지나면 패킷 손실이 완전히 멈춥니다. 그러나 전송 중인 바이트 수는 변동 없이 유지되며, 이는 손실이 없으면 더 많은 가스를 적용하여 스로틀을 늘립니다(이 세상에서는 더 많은 바이트). _그러면 다음과 같은 의문이 생깁니다. 네트워크에서 패킷이 누락되지 않는다면, 혼잡 기간은 늘어나지 않는 이유는 무엇일까요?_

해당 지역을 자세히 살펴보면, 분석에 따르면 CUBIC은 그래프에서 확장된 복구 단계로 표시되어 있듯이, 혼잡 회피 상태(운영 체제 단계)와 복구 상태(패킷 손실 복구 상태) 사이에서 급격한 변화를 보이며 999 전환을 시작합니다. 6.7초 이내입니다. 약 14ms마다 하나의 전환이 발생하며, 의심스러울 정도로 연결의 RTT(10ms)에 가깝습니다. 이 전체 기간 동안 cwnd는 최소 최소값(2700바이트, 즉 최대 크기의 패킷 2개)에서 잠겨 있습니다.

CUBIC의 논리에 무언가가 연결 상태를 잘못 해석하고 있는 것이 분명합니다. 핵심 단서는 변동 주기입니다. ~14ms는 RTT와 일치합니다. 무엇이든 복구/회피 플립을 트리거하는 것은 연결의 ACK 클럭과 함께 왕복당 한 번 발생합니다. 클라이언트가 각 왕복 ACK를 전송하여 서버의 다음 전송을 트리거하는 셀프 클럭 주기입니다. 이는 다운로드(서버에서 클라이언트로)이고, 해당 ACK가 클라이언트에서 서버로 이동하고 CUBIC의 상태 시스템이 서버 측에서 실행되기 때문에 이러한 ACK가 도착할 때마다 bytes_in_flight 가 0으로 떨어지고 서버가 다음 2-패킷 버스트를 전송합니다. 이것이 버그를 트리거하는 것입니다.

이러한 행동이 CUBIC에만 해당하는지 확인하기 위해 손실 기반 제품군에 속한 또 다른 구성원이지만 성장률이 다른 [_Reno_](https://dl.acm.org/doi/10.1145/235160.235162)에 대해서도 동일한 테스트를 실행했습니다. 결과, 통과율이 100%로, Reno가 손실 단계 이후 깔끔하게 회복되었고, CUBIC 관련 버그로 밝혀졌습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image8](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44TV8WPG06X3CYZXY26X0G.png&w=715&h=505&f=webp&fit=cover&position=center)

_T=2초에서 손실 단계가 끝난 후 Reno가 정상적으로 복구되고 약 5초 후에 다운로드가 완료됨_

## 근본 원인 추적

손실 기반 알고리즘은 가속 방식과 브레이크 페달의 두 개를 갖추고 있으며 가속 방식이 다릅니다. CUBIC에는 몇 가지 추가 기능이 있습니다. 여기에서는 bytes_in_flight == 0에 초점을 맞출 것입니다.

### 유휴 후 TCP CUBIC(Linux, 2017)

버그를 이해하려면 먼저 버그가 발생한 최적화 과정을 이해해야 합니다. 2017년에 Linux 커널의 CUBIC 구현에서 문제가 발견되었습니다. [ _커밋 메시지에는_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) 다음과 같이 설명되어 있습니다.

> epoch는 최초에 손실이 발생했을 때만 업데이트/재설정됩니다. `now - epoch_start`의 차이 "t"는 `bic_target`뿐만 아니라 앱 유휴 후도 임의대로 클 수 있습니다. 결과적으로 기울기(`ca->cnt`의 역수)는 매우 커지며, 결국 `ca->cnt`는 지연된 ACK 느린 시작 동작을 위해 2로 하한이 정해집니다.
> 
> 이는 특히 `slow_start_after_idle`이 비활성화되어 있을 때 몇 초의 유휴 시간 후 위험한 cwnd 인플레이션(1.5 x RTT)으로 나타납니다.

**에포크는** CUBIC가 성장 곡선을 고정하는 데 사용하는 기준 타임스탬프입니다. `W_cubic(delta_t)`는 `delta_t =now - epoch_start`에 의해 매개변수화되며, CUBIC가 성장 함수를 재시작할 때마다, 특히 손실 이벤트가 `cwnd`를 감소시킨 후에 에포크가 재설정됩니다. 재설정 사이에서 `delta_t`는 실제 시간에 따라 단조 증가합니다.

애플리케이션이 잠시 유휴(전송 중지)했다가 다시 시작하면 CUBIC 성장 함수 `W_cubic(delta_t)`는 아래 그림에 설명된 것처럼 `delta_t`를 `now - epoch_start`로 계산합니다. 유휴 시간 동안 에포크가 업데이트되지 않았으므로 `delta_t`는 거대하여 막대한 목표 윈도우가 생성되어 CUBIC은 즉시 `cwnd`를 부당한 값으로 확장하려고 시도합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image7](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45PX0PXQBDHX7JSR6WBDTA.png&w=715&h=452&f=webp&fit=cover&position=center)

Jana Iyengar의 초기 해결 방법은 애플리케이션에서 전송을 재개할 때 `epoch_start`를 재설정하는 것이었습니다. 하지만 Neal Cardwell은 그러한 접근 방식의 결함을 [_지적했습니다_](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d).

> … CUBIC 알고리즘에 곡선을 다시 계산하도록 요청하여 현재 cwnd 위치에서 다시 가파르게 상승하기 시작합니다(손실 직후 CUBIC처럼). 이상적으로는 cwnd 증가 곡선이 동일한 모양이고 유휴 기간의 양만큼 나중에 이동하는 것이 좋습니다.

Eric Dumazet, Yuchung Cheng, Neal Cardwell이 작성한 멋진 솔루션은 에포크를 재설정하는 대신 유휴 기간만큼 앞으로 이동시키는 것이었습니다. 이렇게 하면 CUBIC 성장 곡선의 모양이 유지되며, 알고리즘이 중단된 지점에서 다시 시작하도록 시간을 줄이기만 하면 됩니다.

### 포트 투 키시(2020)

CUBIC가 Quiche에서 [_처음 구현되었을_](https://blog.cloudflare.com/cubic-and-hystart-support-in-quiche/) 때, 이 유휴 기간 조정은 포팅되었습니다. 그러나 사용자 공간에서 실행되는 QUIC에는 TCP의 커널 레벨 [`_CA_EVENT_TX_START_`](https://github.com/torvalds/linux/commit/30927520dbae297182990bb21d08762bcc35ce1d) 콜백이 없습니다. 대신, quiche 구현은 `on_packet_sent()` 내부에서 유휴 조건을 확인합니다.
    
    
    // cubic.rs — on_packet_sent() (simplified)
    /// Updates the state when a packet is sent.
    fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
        // If the sending burst is restarting (i.e., bytes_in_flight was zero before this send),
        // adjust the congestion recovery start time to account for the gap in sending.
        if bytes_in_flight == 0 {
            let delta = now - self.last_sent_time;
            self.congestion_recovery_start_time += delta;
        }
        // Record the time of this send event.
        self.last_sent_time = now;
    }

### 그 비결: QUIC의 차이

키체로 포팅된 수정 프로그램에는 원래 커널 변경에 있었던 버그가 포함되어 있었지만, 약 일주일 후 [_커널 큐빅 모듈에 대한 후속 변경_](https://github.com/torvalds/linux/commit/c2e7204d180f8efc80f27959ca9cf16fa17f67db) 으로 수정되었습니다. 두 번째 수정의 커밋 메시지는 다음과 같습니다.

> `tcp_cubic`: 향후에 `epoch_start`를 설정하지 않음 `bictcp_cwnd_event()` 에서 유휴 시간을 추적하는 것은 부정확합니다. `epoch_start`는  
>  일반적으로 송신 시간이 아닌 ACK 처리 시간에 설정되기 때문입니다.
> 
> 제대로 수정하려면 상태 변수를 더 추가해야 하며,  
>  CUBIC 버그가 Jana가 알아차리기 훨씬 전부터 존재했다는 점을 고려하면,  
>  굳이 손볼 가치가 없어 보입니다.
> 
> 앞으로 `epoch_start` 를 설정하지 맙시다. 그렇지 않으면  
> `bictcp_update()` 가 오버플로되어 CUBIC가 다시  
> `cwnd`가 너무 빠르게 증가할 수 있습니다.

커밋 메시지에서 언급했듯이 복구 시작 시간은 ACK 처리 중에 설정되며, 전송된 시간을 기반으로 조정 값을 계산하면 복구 시작 시간이 미래로 밀려날 수 있습니다. 이는 테스트에서 나타난 복구와 혼잡 회피 사이의 변동을 설명해줍니다. 이 함정은 모든 수신 ACK가 bytes_in_flight를 완전히 0으로 만들 때에만 일관되게 트리거됩니다. 이는 실제로 cwnd가 최소값(2 패킷)으로 축소되고 ACK가 도착하는 순간 애플리케이션에 다른 전체 창을 보낼 수 있는 데이터가 있음을 의미합니다. 이 영역을 벗어나면, bytes_in_flight == 0 은 모든 전송을 보류할 가능성이 적으므로 버그가 트리거될 가능성이 적습니다. 

연결을 시작할 때도 이런 일이 발생하지 않는 이유는 무엇입니까? 이 버그는 연결이 느린 시작을 벗어나 정체 회피로 전환될 때만 트리거됩니다. Slow-start를 종료하기 전에는 `congestion_recovery_start_time` 이(가) 설정되지 않아, `on_packet_sent` 의 버그가 있는 분기에는 앞으로 이동할 복구 경계가 없습니다. 슬로우 스타트 동안 CUBIC의 `cwnd`는 모든 손실 기반 CCA에서 공유하는 동일한 Reno 스타일 ACK 기반 규칙에 따라 증가합니다. 즉, 큐빅 곡선과 `congestion_recovery_start_time`에 대한 민감도는 연결이 혼잡 회피 상태에 있을 때만 적용됩니다. 즉, 트랩은 복구 경계를 설정하기 위한 실제 손실 이벤트, 혼잡 회피 실행, 그리고 `cwnd`가 2패킷 하한으로 축소되는 세 가지 조건을 동시에 충족해야 합니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image3](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TRJWX5RY1QFR0DK4FV15.png&w=715&h=533&f=webp&fit=cover&position=center)

_스스로 영속화되는 복구의 함정. 최소한 cwnd에서 모든 ACK 주기는 부풀려진 Delta를 가진 유휴 기간 조정을 트리거합니다._

최소한 cwnd(2 패킷)에서 연결의 역학은 유휴 기간 최적화가 자기 실현적 예측이 되는 "죽음의 나선"으로 전환됩니다. 이 함정은 연속 루프로 작동합니다.

  1. **전송 및 ACK 패킷:** 발신자가 2 패킷 윈도우 전체를 전송합니다. 하나의 RTT(~14ms) 후에 두 패킷 모두 ACK가 되어 bytes_in_flight는 0으로 떨어집니다.
  2. **잘못된 유휴 감지:** 다음 버스트가 전송되면 on_packet_sent()가 bytes_in_flight == 0을 확인하고 연결이 유휴 상태였지만 혼잡에 제한이 있었다고 가정합니다.
  3. **과장된 델타:** 계산은 now - last_sent_time을 사용하여 유휴 기간을 결정합니다. 정체 윈도우(`cwnd`)가 최소일 때, `last_sent_time`은 이전 RTT 사이클의 _시작_ 타임스탬프입니다. 따라서 결과 차이는 약 14ms(연결의 RTT + 추가 반올림 오류)입니다. 이 RTT 크기의 Delta는 "유휴" 시간으로 잘못 적용됩니다. 연결이 유휴 상태였던 _실제_ 시간(마지막 ACK 도착과 다음 패킷 전송 사이의 처리 격차)은 사실상 0입니다. 실제 격차 대신 전체 RTT를 측정함으로써 델타가 크게 부풀려져 복구 시작 시간을 적극적으로 앞당겨, 어쩌면 미래로까지 이동시킬 수 있습니다.
  4. **인식된 복구:** 복구 시작 시간이 현재 미래이므로 `in_congestion_recovery()` 검사는 모든 수신 ACK에 대해 true를 반환합니다. 다음 ACK를 처리하면 복구가 종료되고 복구 시작이 last_sent_time보다 큰 ACK 시간으로 설정되므로 정체 컨트롤러가 다음 전송을 수행할 때 복구 시간을 미래로 미룰 수 있습니다.
  5. **정체:** CUBIC은 복구 기간에 있는 것으로 인식된 모든 패킷에 대해 `cwnd` 증가를 건너뛰므로 창이 두 패킷으로 고정되어 다음 ACK에서 파이프가 완전히 배출되고 주기가 다시 시작됩니다.



그리고 이 루프가 스케줄러 지터 및 ACK 처리 차이와의 작은 편차가 누적될 때까지 수천 사이클 동안 반복되며, `in_congestion_recovery()`의 <= 경계가 다음 패킷의 전송 시간보다 늦어져 사이클이 중단됩니다.

## 해결책: 적절한 순간에 유휴 상태 측정

죽음의 나선을 해결하려면 bytes_in_flight 이 마지막으로 전송된 패킷이 아니라 실제로 0(처리된 마지막 ACK)으로 전환되는 유휴 지속 시간을 측정해야 합니다.

### 코드 변경

  1. CUBIC 상태에 last_ack_time 타임스탬프를 추가합니다.
  2. ACK가 도착하면 해당 타임스탬프를 업데이트합니다.
  3. 유휴 Delta 계산에 사용합니다.


    
    
    // cubic.rs — on_packet_sent()
    fn on_packet_sent(&mut self, bytes_in_flight: usize, now: Instant, ...) {
        // Check if the connection was idle before this packet was sent.
        if bytes_in_flight == 0 {
            if let Some(recovery_start_time) = r.congestion_recovery_start_time {
                // Measure idle from the most recent activity: either the
                // last ACK (approximating when bif hit 0) or the last data
                // send, whichever is later. Using last_sent_time alone
                // would inflate the delta by a full RTT when cwnd is small
                // and bif transiently hits 0 between ACK and send.
                let idle_start = cmp::max(cubic.last_ack_time, cubic.last_sent_time);
    
                if let Some(idle_start) = idle_start {
                    if idle_start < now {
                        let delta = now - idle_start;
                        r.congestion_recovery_start_time =
                            Some(recovery_start_time + delta);
                    }
                }
            }
    }

이제 Delta가 마지막 ACK 이후의 실제 격차를 반영하므로 복구 경계는 더 이상 전송 시간을 추적하지 않게 됩니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image2](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ASH8GZ33QEC3H67W7MMJ.png&w=715&h=369&f=webp&fit=cover&position=center)

_이전 코드: 경계가 주기당 하나의 RTT만큼 이동하여 항상 다음 전송 시점이나 그 이전에 도착합니다._

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4655NBGY57G0JX3FXN88XF.png&w=715&h=369&f=webp&fit=cover&position=center)

_수정: 경계가 거의 이동하지 않음. 다음 send가 그것보다 앞서고 cwnd가 커집니다._

실제 유휴 연결의 경우, `last_ack_time`이 훨씬 과거의 과거이고 동일한 식이 전체 유휴 기간을 캡처하면 원래의 epoch-shift 동작이 유지됩니다.

## 검증용

이 수정 프로그램이 적용되면서 키시 테스트 제품군의 통과율이 100%로 복구되었습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-3273 image11](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48KFFNQ428RM6AY394S59B.png&w=715&h=506&f=webp&fit=cover&position=center)

_수정한 후에는 cwnd가 예상 CUBIC 곡선을 따라 증가하고 4~5초 내에 다운로드가 완료됩니다._

우리는 연결 마지막에서의 손실에 대해 걱정하지 않습니다. 이는 라우터가 할당한 버퍼를 완전히 활용했기 때문에 가능한 일입니다. 즉, 이 테스트 사례에서 가용 대역폭을 완전히 활용하고 있습니다.

## 요점

  * **"유휴"는 생각보다 정의하기 어렵습니다.** 작은 윈도우에서의 정상적인 파이프라인 지연은 간단한 검사에 대한 게으름으로 보일 수 있습니다.
  * **최소-cwnd 역학은 독특한 코너 사례입니다.** 이 버그는 고속에서는 보이지 않았고 심각한 손실이 발생한 후에야 트리거되었습니다.
  * **문제의 복잡성에 비해 해결책의 규모는 놀라울 정도로 작았습니다.** 근본 원인을 찾기 위해 몇 주간 qlog를 도구화하고 시각화를 분석한 끝에, 단 세 줄의 코드만 변경하면 되었습니다. 조사 중에 언급했듯이 버그를 찾기 위한 노력은 엄청나게 많았지만, 수정 자체는 기본적으로 한 줄의 논리에 불과했습니다.



이 게시물에 설명된 수정 사항은 QUIC 및 HTTP/3의 Cloudflare 오픈 소스 구현인 **`_cloudflare/quiche_`** 에 기여했습니다. Cloudflare의 CCA 노력은 손실 기반 알고리즘에 그치지 않습니다. 또한 quiche의 모듈식 정체 제어 설계를 사용하여 모델 기반 [_BBRv3_](https://blog.cloudflare.com/new-standards/#congestion-control) 구현을 실험하고 조정하고 있으며, 현재 QUIC 배포의 점점 더 많은 부분에 적용되고 있습니다. QUIC 정체 제어 구현 및 성능에 대한 추가 업데이트를 기대해 주세요. 

정체 제어나 전송 프로토콜에 관심이 있거나 오픈 소스 네트워킹 코드에 기여하는 데 관심이 있으시면 **quiche** 리포지토리를 확인하세요. Cloudflare는 이러한 문제를 파헤치기를 좋아하는 재능 있는 엔지니어를 찾고 있으니,[ _채용 공고를_](https://www.cloudflare.com/careers/) 알아보세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fquic-death-spiral-fix%2F&t=%27%EC%9C%A0%ED%9C%B4%27%EA%B0%80%20%EC%9C%A0%ED%9C%B4%EA%B0%80%20%EC%95%84%EB%8B%90%20%EB%95%8C%3A%20Linux%20%EC%BB%A4%EB%84%90%20%EC%B5%9C%EC%A0%81%ED%99%94%EA%B0%80%20QUIC%20%EB%B2%84%EA%B7%B8%EA%B0%80%20%EB%90%9C%20%EB%B0%A9%EB%B2%95)[](https://x.com/intent/post?text=%27%EC%9C%A0%ED%9C%B4%27%EA%B0%80+%EC%9C%A0%ED%9C%B4%EA%B0%80+%EC%95%84%EB%8B%90+%EB%95%8C%3A+Linux+%EC%BB%A4%EB%84%90+%EC%B5%9C%EC%A0%81%ED%99%94%EA%B0%80+QUIC+%EB%B2%84%EA%B7%B8%EA%B0%80+%EB%90%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fquic-death-spiral-fix%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fquic-death-spiral-fix%2F)[](https://bsky.app/intent/compose?text=%27%EC%9C%A0%ED%9C%B4%27%EA%B0%80+%EC%9C%A0%ED%9C%B4%EA%B0%80+%EC%95%84%EB%8B%90+%EB%95%8C%3A+Linux+%EC%BB%A4%EB%84%90+%EC%B5%9C%EC%A0%81%ED%99%94%EA%B0%80+QUIC+%EB%B2%84%EA%B7%B8%EA%B0%80+%EB%90%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fquic-death-spiral-fix%2F)[](https://mastodonshare.com/?text=%27%EC%9C%A0%ED%9C%B4%27%EA%B0%80+%EC%9C%A0%ED%9C%B4%EA%B0%80+%EC%95%84%EB%8B%90+%EB%95%8C%3A+Linux+%EC%BB%A4%EB%84%90+%EC%B5%9C%EC%A0%81%ED%99%94%EA%B0%80+QUIC+%EB%B2%84%EA%B7%B8%EA%B0%80+%EB%90%9C+%EB%B0%A9%EB%B2%95&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fquic-death-spiral-fix%2F)[](https://www.threads.net/intent/post?text=%27%EC%9C%A0%ED%9C%B4%27%EA%B0%80+%EC%9C%A0%ED%9C%B4%EA%B0%80+%EC%95%84%EB%8B%90+%EB%95%8C%3A+Linux+%EC%BB%A4%EB%84%90+%EC%B5%9C%EC%A0%81%ED%99%94%EA%B0%80+QUIC+%EB%B2%84%EA%B7%B8%EA%B0%80+%EB%90%9C+%EB%B0%A9%EB%B2%95+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fquic-death-spiral-fix%2F)

## 관련 태그

[HTTP3](https://blog.cloudflare.com/ko-kr/tag/http3/)[QUIC](https://blog.cloudflare.com/ko-kr/tag/quic/)[QUICHE](https://blog.cloudflare.com/ko-kr/tag/quiche/)[Rust](https://blog.cloudflare.com/ko-kr/tag/rust/)[네트워킹](https://blog.cloudflare.com/ko-kr/tag/networking/)[디버깅](https://blog.cloudflare.com/ko-kr/tag/debugging/)[정체 제어](https://blog.cloudflare.com/ko-kr/tag/congestion-control/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
