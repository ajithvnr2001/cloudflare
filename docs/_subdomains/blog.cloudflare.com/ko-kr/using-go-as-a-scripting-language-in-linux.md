---
url: https://blog.cloudflare.com/ko-kr/using-go-as-a-scripting-language-in-linux/
title: \ub9ac\ub205\uc2a4\uc5d0\uc11c Go\ub97c \uc2a4\ud06c\ub9bd\ud2b8 \uc5b8\uc5b4\ub85c \uc0ac\uc6a9\ud558\uae30 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:49:20.015534+00:00
---

# 리눅스에서 Go를 스크립트 언어로 사용하기 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/using-go-as-a-scripting-language-in-linux/

[블로그](https://blog.cloudflare.com/ko-kr/)

[Go](https://blog.cloudflare.com/ko-kr/tag/go/)[Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[Programming](https://blog.cloudflare.com/ko-kr/tag/programming/)+33개의 태그 더 보기

6개 태그6개 태그 보기

  * 게시물 태그
  * [Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[자세히 보기](https://blog.cloudflare.com/ko-kr/tag/deep-dive/)
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



[Tech Talks](https://blog.cloudflare.com/ko-kr/tag/tech-talks/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[자세히 보기](https://blog.cloudflare.com/ko-kr/tag/deep-dive/)

[Go](https://blog.cloudflare.com/ko-kr/tag/go/)[Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[Programming](https://blog.cloudflare.com/ko-kr/tag/programming/)[Tech Talks](https://blog.cloudflare.com/ko-kr/tag/tech-talks/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[자세히 보기](https://blog.cloudflare.com/ko-kr/tag/deep-dive/)

2018년 2월 20일

# 리눅스에서 Go를 스크립트 언어로 사용하기

![Ignat Korchagin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BNP74V364MGRFD4YYQJW.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ignat Korchagin](https://blog.cloudflare.com/ko-kr/author/ignat/)

8분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/using-go-as-a-scripting-language-in-linux/), [Deutsch](https://blog.cloudflare.com/de-de/using-go-as-a-scripting-language-in-linux/), [Español](https://blog.cloudflare.com/es-es/using-go-as-a-scripting-language-in-linux/) 및 [Français](https://blog.cloudflare.com/fr-fr/using-go-as-a-scripting-language-in-linux/).

![Using Go as a scripting language in Linux](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B5PKF4S2NKRXT0DFRBGW.png&w=1500&h=1000&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAANUhUUGFtbYGPbIWbP2mNADZ1ADBvAFt/SVptYXSGf5WofpiwU3aXADZvACVjBF58WmuCcoWaj6e8jqnBZIGfADFlAAVPIV51ZnWMfI6jmK/Elq/GaoSeACNWAAAzK1lqa3eKfo2flqu8k6m8Z3ySAABCAAAAK0xZbHN/e4WQjp6oiJmlWmp8AAAkAAAAJDhCa21xdnx+hI6PeoeKSlVjAAAAAAAAGRsnampqdHd1f4eDdH58QktWAAAAAAAAEwEW)

* * *

Cloudflare에서는 Go를 좋아합니다. Go는 많은 [내부 소프트웨어 프로젝트](https://blog.cloudflare.com/what-weve-been-doing-with-go/)와 [거대한 파이프라인 시스템](https://blog.cloudflare.com/meet-gatebot-a-bot-that-allows-us-to-sleep/)의 일부로도 사용되고 있습니다. 하지만 Go를 한단계 더 끌어 올려서 우리가 선호하는 운영체제인 리눅스의 스크립트 언어로 사용할 수 있을까요?

[gopher image](https://golang.org/doc/gopher/gophercolor.png) [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) [Renee French](http://reneefrench.blogspot.com/) | [Tux image](https://pixabay.com/en/linux-penguin-tux-2025536/) [CC0 BY](https://creativecommons.org/publicdomain/zero/1.0/deed.en) [OpenClipart-Vectors](https://pixabay.com/en/users/OpenClipart-Vectors-30363/)

### Go를 왜 스크립트 언어로 고려하는가

간단한 답은: 왜 안되나요? Go는 비교적 쉽게 배울 수 있고 아주 복잡하지도 않고, 코드를 처음부터 작성해야 하는 일을 피하기 위해 재사용 가능한 라이브러리의 거대한 에코시스템이 있습니다. 추가로 다음과 같은 잠재적인 장점이 있습니다:

  * 여러분의 Go 프로젝트를 위한 Go 기반 빌드 시스템: `go build` 명령은 대부분의 소규모이며 독립적인 프로젝트에 적합합니다. 더 복잡한 프로젝트는 대부분 별도의 빌드 시스템/스크립트 세트를 채용하고 있습니다. 이런 스크립트도 Go로 작성 가능하지 않을까요?
  * 바로 이용 가능한 별도 권한 없는 패키지 관리: 여러분의 프로그램에서 서드 파티 라이브러리를 사용하고 싶다면 단순히 `go get` 을 사용하면 됩니다. 그리고 이 코드가 여러분의 `GOPATH`에 설치되므로, 서드파티 라이브러리를 받는 것은 시스템의 별도 운영 권한을 필요로 하지 않습니다(다른 일부 스크립트 언어와 달리). 이것은 대규모의 기업 환경에서 특히 유용합니다.
  * 초기 단계 프로젝트를 위한 빠른 코드 프로토타이핑: 최초로 돌아가는 코드를 작성할 때 컴파일 되기 위해서 많은 편집을 해야 하고 _"편집- >빌드->체크"_ 사이클을 위해 많은 키보드 입력을 낭비하게 됩니다. 대신 "빌드" 부분을 넘어가서 바로 소스 파일을 실행할 수 있습니다.
  * 강 타입 스크립트 언어: 스크립트안에 조그만 오류가 있다고 하면 대부분의 스크립트는 해당 지점까지 실행하고 나서 오류 부분에서 멈추게 됩니다. 이 경우 시스템이 불완전한 상황에 놓일 수 있습니다. 강 타입 언어의 경우 많은 오류가 컴파일 시간에 잡히게 되므로 오류가 있는 스크립트는 실행 자체가 되지 않을 것입니다.



### Go 스크립트의 현재 상황

처음 보았을 때 Go 스크립트는 스크립트를 위한 [셔뱅 라인](https://ko.wikipedia.org/wiki/%EC%85%94%EB%B1%85)의 유닉스 지원을 이용하면 쉬울 것 처럼 보였습니다. 셔뱅 라인은 스크립트의 첫번째 행으로 `#!` 으로 시작하며 스크립트를 실행하기 위한 스크립트 인터프리터를 지정하게 됩니다(예를 들어 `#!/bin/bash` 이나 `#!/usr/bin/env python`). 따라서 시스템은 사용된 프로그래밍 언어에 관계 없이 스크립트를 어떻게 실행하게 될지 정확히 알고 있습니다. 그리고 Go 는 `go run` 명령을 통해서 `.go` 파일을 인터프리터처럼 실행하는 것을 지원하고 있으므로 `.go` 파일에 `#!/usr/bin/env go run`과 같은 적절한 셔뱅 라인을 추가하고 실행 비트를 지정하는 것 만으로 준비가 다 되어야 겠죠.

하지만 `go run`을 직접 실행하는데에는 문제가 있습니다. [이 멋진 글](https://gist.github.com/posener/73ffd326d88483df6b1cb66e8ed1e0bd)에서는 `go run` 관련의 문제를 자세히 설명하고 가능한 대응 방안에 대해서 다룹니디만 미리 요약하면:
    
    
    package main:
    helloscript.go:1:1: illegal character U+0023 '#'

  * `go run`은 운영체제에 스크립트 오류 코드를 적절하게 전달하지 않습니다. 이는 스크립트에게 중요한데 오류 코드는 여러 스크립트간 또는 운영체제와 상호 동작하기 위한 가장 일반적인 방법이기 때문입니다.
  * 유효한 `.go` 파일에는 셔뱅 라인을 넣을 수 없는데 Go 는 `#`으로 시작하는 행을 어떻게 처리해야 하는지 알지 못하기 때문입니다. 다른 스크립트 언어는 이런 문제가 없는데, 대부분 `#`은 주석을 지정하는데 사용하고 있어서 최종적으로 이런 인터프리터는 셔뱅 라인을 단순히 무시하게 됩니다. 하지만 Go의 주석문은 `//`으로 시작하므로 셔뱅 라인은 `go run` 실행시 다음과 같은 오류를 냅니다:
  * package main:  
helloscript.go:1:1: illegal character U+0023 '#'



[이 글](https://gist.github.com/posener/73ffd326d88483df6b1cb66e8ed1e0bd)에서는 인터프리터로 사용하기 위한 커스텀 래퍼 프로그램 [gorun](https://github.com/erning/gorun)을 포함하여 위 문제들에 대한 여러가지 대처 방법을 설명합니다만 전부 이상적인 해결 방법을 제시하는 것 만은 아닙니다. 여러분은 다음 중에서 선택을 해야 합니다:

  * `//`으로 시작하는 비표준 셔뱅 라인을 사용합니다. 이것은 기술적으로는 셔뱅 라인이 아니고 `bash` 쉘이 실행 가능한 텍스트 파일을 처리하는 방식이므로 `bash`에 한정된 방법입니다. 또한 `go run`의 특정한 행동 때문에 이 행은 오히려 복잡하고 명확하지 않습니다 (예제를 위해서는 [원래 글](https://gist.github.com/posener/73ffd326d88483df6b1cb66e8ed1e0bd)을 보세요)
  * 셔뱅 라인에서 커스텀 래퍼 프로그램 [gorun](https://github.com/erning/gorun)을 사용합니다. 이것은 잘 동작하지만 허용되지 않는 `#` 문자를 사용하는 것 때문에 표준 `go build`명령과 호환되지 않는 `.go` 파일을 만들게 됩니다.



### 리눅스가 파일을 실행하는 방법

좋습니다. 셔뱅 방식은 만능의 해결책을 제공하지는 않는 것 같군요. 다른 방법이 없을까요? 먼저 리눅스 커널이 바이너리를 실행하는 방법에 대해서 자세히 보도록 합시다. 바이너리나 스크립트를 실행할 때 (또는 실행 비트가 설정되어 있는 어떤 파일에 대해서) 여러분의 쉘은 최종적으로 리눅스의 `execve` [시스템 콜](https://en.wikipedia.org/wiki/System_call)을 사용하고 여기에 실행하고자 하는 바이너리의 파일시스템 경로명, 명령행 인자와 현재 정의된 환경 변수를 전달 합니다. 그리고 나서 커널은 파일을 올바르게 파싱하는 일과 파일의 코드로부터 새 프로세스를 생성하는 일을 담당 합니다. 리눅스(그리고 많은 유닉스 파생 운영체제)가 실행 파일용으로 [ELF 바이너리 형식](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)을 사용하는 것은 잘 알려져 있습니다.

하지만 리눅스 커널 개발의 핵심 원칙 중 하나는 커널의 일부인 서브시스템에서 "벤더/포맷 제약"을 피하는 것입니다. 따라서 리눅스는 커널이 어떤 바이너리 형식도 지원할 수 있도록 하는 "추가 가능한" 시스템을 구현하였습니다 - 여러분이 해야 할 일은 선택한 형식을 파싱할 수 있는 올바른 모듈을 작성하는 것입니다. 그리고 커널 소스 코드를 잘 보면 리눅스는 기본적으로 여러가지 바이너리 형식을 지원하는 것을 알 수 있습니다. 예를 들어 최근의 `4.14` 리눅스 커널에서는 적어도 7개의 바이너리 형식을 지원하는 것을 [볼 수 있습니다](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git/tree/fs?h=linux-4.14.y)(여러 바이너리 형식의 커널 내장 모듈은 대부분 `binfmt_` 로 시작하는 이름입니다). 그중 [binfmt_script](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git/tree/fs/binfmt_script.c?h=linux-4.14.y) 모듈은 살펴볼 가치가 있는데, 이 모듈은 앞서 이야기한 셔뱅 라인을 해석하고 타겟 시스템에서 스크립트를 실행하는 것을 담당합니다(셔뱅 지원이 쉘이나 다른 대몬/프로세스가 아니라 실제 커널에 구현되어 있는 건 잘 알려진 사실은 아닙니다).

### 사용자 공간에서 바이너리 형식 지원을 추가하기

하지만 Go 스크립트를 위해서 셔뱅이 최선의 옵션이 아니라고 결론을 내렸으므로, 다른 것이 필요합니다. 놀랍게도 리눅스 커널에는 `binfmt_misc` 라는 적절한 이름을 갖는 ["다른" 바이너리 지원 모듈](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git/tree/fs/binfmt_misc.c?h=linux-4.14.y)이 이미 있습니다. 이 모듈은 관리자에게 동적으로 여러가지 실행 가능한 형식을 잘 정의된 `procfs` 인터페이스를 통해 사용자 공간에서 직접 추가로 지원할 수 있도록 해 주며 [문서화](https://www.kernel.org/doc/html/v4.14/admin-guide/binfmt-misc.html)도 잘 되어 있습니다.
    
    
    $ mount | grep binfmt_misc
    systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=27,pgrp=1,timeout=0,minproto=5,maxproto=5,direct)

[해당 문서](https://www.kernel.org/doc/html/v4.14/admin-guide/binfmt-misc.html)를 따라서 `.go` 파일을 위한 바이너리 형식을 설정해 보도록 합니다. 먼저 가이드 문서는 `binfmt_misc` 파일시스템을 `/proc/sys/fs/binfmt_misc`에 마운트하도록 설명하고 있습니다. 비교적 최신의 `systemd` 기반 리눅스 배포본을 사용하고 있다면 이 파일시스템은 이미 마운트되어 있을 것인데 `systemd`는 기본적으로 이 목적으로 특별한 [mount](https://github.com/systemd/systemd/blob/master/units/proc-sys-fs-binfmt_misc.mount)와 [automount](https://github.com/systemd/systemd/blob/master/units/proc-sys-fs-binfmt_misc.automount) 유닛을 설치하기 때문입니다. 확인하기 위해서는 다음을 실행해 보세요:

다른 방법은 `/proc/sys/fs/binfmt_misc` 안에 파일이 있는지 확인하는 것입니다: 제대로 마운트된 `binfmt_misc` 파일시스템은 그 디렉토리에 적어도 `register`와 `status`라는 두개의 파일을 생성할 것입니다.
    
    
    $ go get github.com/erning/gorun
    $ sudo mv ~/go/bin/gorun /usr/local/bin/

다음으로 우리의 `.go` 스크립트가 종료 코드를 운영체제에 적절하게 전달 하도록 하기 위해서 "인터프리터"로 사용될 커스텀 [gorun](https://github.com/erning/gorun) 래퍼가 필요 합니다:

기술적으로는 `binfmt_misc`는 인터프리터의 전체 경로를 필요로 하기 때문에 `gorun`을 `/usr/local/bin`이나 다른 시스템 경로에 옮길 필요는 없습니다만 시스템은 이 실행 파일을 임의의 권한으로 실행할 수 있으므로 보안 관점에서 파일 접근에 제한을 지정하는 것은 좋은 생각 입니다.
    
    
    package main
    
    import (
    	"fmt"
    	"os"
    )
    
    func main() {
    	s := "world"
    
    	if len(os.Args) > 1 {
    		s = os.Args[1]
    	}
    
    	fmt.Printf("Hello, %v!", s)
    	fmt.Println("")
    
    	if s == "fail" {
    		os.Exit(30)
    	}
    }

이 시점에서 간단한 장난감 Go 스트립트인 `helloscript.go`를 만들어서 제대로 "실행"하는지 확인해 봅니다. 스크립트는 다음과 같습니다:
    
    
    $ gorun helloscript.go
    Hello, world!
    $ echo $?
    0
    $ gorun helloscript.go gopher
    Hello, gopher!
    $ echo $?
    0
    $ gorun helloscript.go fail
    Hello, fail!
    $ echo $?
    30

명령행 인수 전달과 오류 처리도 제대로 되고 있는지 확인합니다:

이제 `binfmt_misc` 모듈에게 `gorun`으로 `.go` 파일을 실행하는 방법을 알려 주도록 합니다. [문서](https://www.kernel.org/doc/html/v4.14/admin-guide/binfmt-misc.html)에 따르면 다음과 같은 설정 문자열이 필요 합니다: `:golang:E::go::/usr/local/bin/gorun:OC`. 이것은 기본적으로 시스템에게 다음과 같이 말하는 것입니다: "`.go` 확장자를 갖는 설정 파일을 만나면 `/usr/local/bin/gorun` 인터프리터로 실행해 주세요". 문자열 끝의 `OC` 플래그는 이 스크립트가 인터프리터 실행 파일이 아니라 해당 스크립트의 사용자 정보과 권한 비트에 따라 실행하도록 해 줍니다. 이렇게 하여 리눅스의 다른 실행 파일이나 스크립트와 동일한 방식으로 실행이 가능하도록 합니다.
    
    
    $ echo ':golang:E::go::/usr/local/bin/gorun:OC' | sudo tee /proc/sys/fs/binfmt_misc/register
    :golang:E::go::/usr/local/bin/gorun:OC

이제 새 Go 스크립트 바이너리 형식을 등록합시다:
    
    
    $ chmod u+x helloscript.go
    $ ./helloscript.go
    Hello, world!
    $ ./helloscript.go gopher
    Hello, gopher!
    $ ./helloscript.go fail
    Hello, fail!
    $ echo $?
    30

시스템이 성공적으로 새 형식을 등록하면 `golang` 이라는 파일이 새로 `/proc/sys/fs/binfmt_misc` 디렉토리에 나타날 것입니다. 마지막으로 이제 `.go` 파일을 바로 실행할 수 있습니다:

잘 되는군요! 이제 `helloscript.go` 를 원하는대로 바꾸어서 변경 사항이 실행 되면 바로 반영 되는지 보도록 하세요. 추가적으로 이전의 셔뱅 방식과는 달리 이 파일은 `go build`를 사용해서 바로 진짜 실행 파일로도 컴파일할 수 있습니다.

* * *

_Go 나 리눅스 내부 구조를 들여다 보는 것에 관심이 있다면, 어느 한 쪽 또는 양쪽 모두를 위한 자리가 있습니다.[우리의 채용 페이지](https://www.cloudflare.com/careers/)를 참고 하세요._

_This is a Korean translation of a[existing post](https://blog.cloudflare.com/using-go-as-a-scripting-language-in-linux/) by [Ignat Korchagin](https://blog.cloudflare.com/author/ignat/), translated by [Junho Choi](https://blog.cloudflare.com/author/junho/)._

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fusing-go-as-a-scripting-language-in-linux%2F&t=%EB%A6%AC%EB%88%85%EC%8A%A4%EC%97%90%EC%84%9C%20Go%EB%A5%BC%20%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%20%EC%96%B8%EC%96%B4%EB%A1%9C%20%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)[](https://x.com/intent/post?text=%EB%A6%AC%EB%88%85%EC%8A%A4%EC%97%90%EC%84%9C+Go%EB%A5%BC+%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8+%EC%96%B8%EC%96%B4%EB%A1%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fusing-go-as-a-scripting-language-in-linux%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fusing-go-as-a-scripting-language-in-linux%2F)[](https://bsky.app/intent/compose?text=%EB%A6%AC%EB%88%85%EC%8A%A4%EC%97%90%EC%84%9C+Go%EB%A5%BC+%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8+%EC%96%B8%EC%96%B4%EB%A1%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fusing-go-as-a-scripting-language-in-linux%2F)[](https://mastodonshare.com/?text=%EB%A6%AC%EB%88%85%EC%8A%A4%EC%97%90%EC%84%9C+Go%EB%A5%BC+%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8+%EC%96%B8%EC%96%B4%EB%A1%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fusing-go-as-a-scripting-language-in-linux%2F)[](https://www.threads.net/intent/post?text=%EB%A6%AC%EB%88%85%EC%8A%A4%EC%97%90%EC%84%9C+Go%EB%A5%BC+%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8+%EC%96%B8%EC%96%B4%EB%A1%9C+%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Fusing-go-as-a-scripting-language-in-linux%2F)

## 관련 태그

[Go](https://blog.cloudflare.com/ko-kr/tag/go/)[Linux](https://blog.cloudflare.com/ko-kr/tag/linux/)[Programming](https://blog.cloudflare.com/ko-kr/tag/programming/)[Tech Talks](https://blog.cloudflare.com/ko-kr/tag/tech-talks/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[자세히 보기](https://blog.cloudflare.com/ko-kr/tag/deep-dive/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
