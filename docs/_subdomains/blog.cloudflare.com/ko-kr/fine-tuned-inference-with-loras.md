---
url: https://blog.cloudflare.com/ko-kr/fine-tuned-inference-with-loras/
title: Workers AI\uc5d0\uc11c LoRA\ub97c \uc0ac\uc6a9\ud558\uc5ec \uc138\ubc00\ud558\uac8c \uc870\uc815\ub41c \ubaa8\ub378 \uc2e4\ud589\ud558\uae30 | Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:41:31.331403+00:00
---

# Workers AI에서 LoRA를 사용하여 세밀하게 조정된 모델 실행하기 | Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/fine-tuned-inference-with-loras/

[블로그](https://blog.cloudflare.com/ko-kr/)

[AI](https://blog.cloudflare.com/ko-kr/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)+33개의 태그 더 보기

6개 태그6개 태그 보기

  * 게시물 태그
  * [AI](https://blog.cloudflare.com/ko-kr/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Workers AI](https://blog.cloudflare.com/ko-kr/tag/workers-ai/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)
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



[Workers AI](https://blog.cloudflare.com/ko-kr/tag/workers-ai/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)

[AI](https://blog.cloudflare.com/ko-kr/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Workers AI](https://blog.cloudflare.com/ko-kr/tag/workers-ai/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)

2024년 4월 2일

# Workers AI에서 LoRA를 사용하여 세밀하게 조정된 모델 실행하기

![Michelle Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44R95PPSQQ82Z92P51M550.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Logan Grasby](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW477NKW4WMXFM6419VZGJXK.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michelle Chen](https://blog.cloudflare.com/ko-kr/author/michelle/) 및 [Logan Grasby](https://blog.cloudflare.com/ko-kr/author/logan/)

12분 읽기

URL 복사

이 포스트는 다음 언어로도 제공됩니다 [English](https://blog.cloudflare.com/fine-tuned-inference-with-loras/), [Deutsch](https://blog.cloudflare.com/de-de/fine-tuned-inference-with-loras/), [Español](https://blog.cloudflare.com/es-es/fine-tuned-inference-with-loras/), [Français](https://blog.cloudflare.com/fr-fr/fine-tuned-inference-with-loras/), [日本語](https://blog.cloudflare.com/ja-jp/fine-tuned-inference-with-loras/), [繁體中文](https://blog.cloudflare.com/zh-tw/fine-tuned-inference-with-loras/) 및 [简体中文](https://blog.cloudflare.com/zh-cn/fine-tuned-inference-with-loras/).

![Running fine-tuned models on Workers AI with LoRAs](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473BMAQJ2JS4TZQ9FYEM63.png&w=1600&h=900&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA//////787/Dw4+jq4+rv6vD27fD06+nr///////+7/Hy4+fs4+rx6vD37fD26+rt////////8fL14+jv4+r06/H67/L57ezx////////9PX65ev05e347vT/8/X98fD1////////+Pr/6O/66fH+8vj/+Pr/9/b7/////////f//7PT/7fb/9/3//v///vz/////////////7/f/8Pn/+///////////////////////8fn/8fv//f//////////)

### LoRA를 통해 미세 조정된 LLM으로부터의 추론이 현재 오픈 베타 버전으로 제공됩니다

오늘, 이제 Workers AI에서 LoRA로 미세 조정된 추론을 실행할 수 있게 되었다는 기쁜 소식을 알려드립니다. 이 기능은 오픈 베타 버전으로 사전 학습된 LoRA 어댑터에서 Mistral, Gemma, Llama 2와 함께 사용할 수 있으며, 몇 가지 제약이 있습니다. [제품 발표 블로그 게시물](https://blog.cloudflare.com/workers-ai-ga-huggingface-loras-python-support/)에서 BYO(Bring Your Own) LoRA 기능에 대한 간략한 개요를 살펴보세요.

이 게시물에서는 미세 조정과 LoRA가 무엇인지 자세히 살펴보고, Workers AI 플랫폼에서 이를 사용하는 방법을 소개한 다음, 이를 저희 플랫폼에서 구현한 방법에 대한 기술적 세부 사항을 자세히 알아보겠습니다.

## 미세 조정이란?

미세 조정은 추가 데이터로 계속 학습시켜 AI 모델을 수정하는 것을 가리키는 일반적인 용어입니다. 미세 조정의 목표는 데이터 세트와 유사한 세대가 생성될 확률을 높이는 것입니다. 모델을 처음부터 학습시키는 것은 학습에 많은 비용과 시간이 소요될 수 있으므로 많은 사용 사례에서 실용적이지 않습니다. 기존의 사전 학습된 모델을 미세 조정하면 모델의 기능을 활용하면서 원하는 작업을 수행할 수 있습니다. [Low-Rank Adaptation](https://arxiv.org/abs/2106.09685)(LoRA)은 LLM뿐만 아니라 다양한 모델 아키텍처에 적용할 수 있는 특정 미세 조정 방법입니다. 기존의 미세 조정 방법에서는 사전 학습된 모델 가중치를 직접 수정하거나 추가 미세 조정 가중치를 융합하는 것이 일반적입니다. 반면 LoRA에서는 미세 조정 가중치와 사전 학습된 모델이 분리된 상태로 유지되며, 사전 학습된 모델은 변경되지 않습니다. 그 결과 코드 생성, 특정 성격, 특정 스타일의 이미지 생성 등 특정 작업을 더 정확하게 수행하도록 모델을 학습시킬 수 있습니다. 특정 주제에 대한 추가 정보를 이해하도록 기존 [LLM](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)을 미세 조정할 수도 있습니다.

원래의 기본 모델 가중치를 유지하는 방식은 상대적으로 적은 연산으로 새로운 미세 조정 가중치를 생성할 수 있다는 것을 의미합니다. 기존의 기본 모델(예: Llama, Mistral, Gemma)을 활용하고 필요에 맞게 조정할 수 있습니다.

## 미세 조정은 어떻게 이루어질까요?

미세 조정과 LoRA가 그처럼 효과적인 이유를 더 잘 이해하려면 AI 모델의 작동 방식을 한 걸음 뒤로 물러나서 이해해야 합니다. AI 모델(LLM과 같은)은 딥러닝 기법을 통해 학습된 신경망입니다. 신경망에는 모델의 도메인 지식을 수학적으로 표현하는 역할을 하는 일련의 매개변수가 있으며, 이는 가중치와 편향성(쉽게 말해 숫자)으로 구성됩니다. 이러한 매개변수는 일반적으로 큰 숫자 행렬로 표현됩니다. 모델에 매개변수가 많을수록 모델의 크기가 커지므로 llama-2-7b와 같은 모델을 볼 때 "7b"를 읽으면 이 모델에 70억 개의 매개변수가 있음을 알 수 있습니다.

모델의 매개변수는 모델의 동작을 정의합니다. 모델을 처음부터 학습시킬 때 이들 매개 변수는 일반적으로 임의의 숫자로 시작합니다. 데이터 세트에 대해 모델을 학습시키면 모델이 데이터 세트를 반영하고 올바른 동작을 보일 때까지 이러한 매개변수가 조금씩 조정됩니다. 어떤 매개변수는 다른 매개변수보다 더 중요할 수 있으므로 우리는 가중치를 적용하여 그 가중치를 중요도를 표시하는 데 사용합니다. 가중치는 학습 대상 데이터의 패턴과 관계를 포착하는 모델의 능력에 중요한 역할을 합니다.

기존의 미세 조정은 학습된 모델의 _모든_ 매개변수를 새로운 가중치 세트로 조정합니다 . 따라서 미세 조정된 모델은 원래 모델과 동일한 양의 매개변수를 제공해야 하므로 완전히 미세 조정된 모델을 학습하고 추론을 실행하는 데 많은 시간과 계산이 소요될 수 있습니다. 게다가 새로운 최신 모델 또는 기존 모델의 버전이 정기적으로 출시되므로 완전히 미세 조정된 모델을 학습, 유지, 저장하려면 많은 비용이 들 수 있습니다.

## LoRA는 효율적인 미세 조정 방법입니다

간단히 말해, LoRA는 사전 학습된 모델에서 매개변수를 조정하지 않고 대신 소수의 추가 매개변수를 적용할 수 있습니다. 이러한 추가 매개변수는 모델 동작을 효과적으로 제어하기 위해 기본 모델에 일시적으로 적용됩니다. LoRA 어댑터라고 하는 이러한 추가 매개변수를 학습하는 데 필요한 시간과 컴퓨팅은 기존의 미세 조정 방식에 비해 훨씬 줄어듭니다. 학습이 끝나면 LoRA 어댑터를 별도의 모델 파일로 패키지화하여 학습한 기본 모델에 연결할 수 있습니다. 완전히 미세 조정된 모델은 크기가 수십 기가바이트에 달할 수 있지만, 이러한 어댑터는 일반적으로 몇 메가바이트에 불과합니다. 따라서 배포가 훨씬 쉬워지며, LoRA로 미세 조정된 추론을 제공하면 총 추론 시간에 대기 시간이 몇 ms만 추가됩니다.

LoRA가 왜 효과적인지 궁금하면 먼저 선형 대수학에 대한 간단한 강의를 들어보시기 바랍니다. 대학 시절부터 접해 본 용어가 아니더라도 걱정하지 마세요. 자세히 설명해 드립니다.

## 수학 살펴보기

기존의 미세 조정을 사용하면 모델의 가중치(_W0_)를 가져와 조정하여 새로운 가중치 집합을 출력할 수 있으므로 원래 모델 가중치와 새 가중치 사이의 차이는 _ΔW_가 되며 이는 가중치의 변화를 나타냅니다_._ 따라서 조정된 모델은 새로운 가중치 집합을 가지게 되며, 이는 원래 모델 가중치와 가중치 변화(_W0_ \+ _ΔW_)로 표현할 수 있습니다.

이러한 모든 모델 가중치는 실제로는 큰 숫자 행렬로 표현된다는 점을 기억하세요. 수학에서 모든 행렬에는 행렬에서 선형적으로 독립적인 열 또는 행의 수를 나타내는 랭크(_r_)라는 속성이 있습니다. 행렬의 랭크가 낮으면 "중요한" 열이나 행이 몇 개 밖에 없으므로 실제로 가장 중요한 매개변수를 사용하여 행렬을 두 개의 작은 행렬로 분해하거나 분할할 수 있습니다(대수에서 인수분해하는 것처럼 생각하세요). 이 기술을 랭크 분해라고 하는데, 이를 통해 가장 중요한 비트는 유지하면서 행렬을 크게 줄이고 단순화할 수 있습니다. 미세 조정의 맥락에서 랭크는 원래 모델에서 변경되는 매개변수의 수를 결정하며, 랭크가 높을수록 미세 조정이 더 강력해져 출력에 대한 세분성이 더 커집니다.

[원래 LoRA 논문](https://arxiv.org/abs/2106.09685)에 따르면 , 연구자들은 모델이 낮은 랭크인 경우 가중치의 변화를 나타내는 행렬도 낮은 랭크라는 사실을 발견했습니다. 따라서 가중치의 변화를 나타내는 행렬 _ΔW_에 랭크 분해를 적용하여 _ΔW = BA_인 두 개의 작은 행렬 _A, B_를 만들 수 있습니다 . 이제 모델의 변화는 랭크가 더 낮은 두 개의 행렬로 표현할 수 있습니다_._ 이것이 바로 이 미세 조정 방법을 Low-Rank Adaptation이라고 부르는 이유입니다.

추론을 실행할 때는 모델의 동작을 변경하기 위해 더 작은 행렬 _A, B_만 필요합니다. _A, B_의 모델 가중치는 구성 파일과 함께 LoRA 어댑터를 구성합니다. 런타임에 모델 가중치를 합산하여 원래 모델(_W0_)과 LoRA 어댑터(_A, B_)를 결합합니다. 더하기와 빼기는 간단한 수학적 연산이므로 _A, B_를 _W0_에서 더하고 빼는 방식으로 다른 LoRA 어댑터를 빠르게 교체할 수 있습니다. 원래 모델의 가중치를 일시적으로 조정함으로써 모델의 동작과 출력을 수정하고 그 결과로 대기 시간을 최소화하면서 미세 조정된 추론을 얻을 수 있습니다.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%201%201%22%3E%3Crect%20width%3D%221%22%20height%3D%221%22%20fill%3D%22rgb\(243%2C243%2C243\)%22%2F%3E%3C%2Fsvg%3E)![BLOG-2383 Embedded Image - b17iRL](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW448KWCGC9JV05EA1NJ42VQ.png&w=715&h=358&f=webp&fit=cover&position=center)

[원래 LoRA 논문](https://arxiv.org/abs/2106.09685)에 따르면, "LoRA는 학습 가능한 매개변수의 수를 10,000배, GPU 메모리 요구량을 3배까지 줄일 수 있다"고 합니다. 이 때문에 LoRA는 완전히 미세 조정된 모델보다 계산 비용이 훨씬 적게 들고, 자료 추론 시간이 추가되지 않으며, 훨씬 작고 휴대가 간편하므로 가장 많이 사용되는 미세 조정 방법 중 하나입니다.

## LoRA를 Workers AI와 함께 사용하는 방법은?

Workers AI는 서버리스 추론을 실행하는 방식 때문에 LoRA를 실행하는 데 매우 적합합니다. 저희 카탈로그에 있는 모델은 항상 GPU에 사전 로드되어 있으므로 요청 시 콜드 스타트 문제가 발생하지 않도록 예열 상태가 유지됩니다. 이는 기본 모델을 항상 사용할 수 있으며 필요에 따라 LoRA 어댑터를 동적으로 로드하고 교체할 수 있음을 의미합니다. 실제로 하나의 기본 모델에 여러 개의 LoRA 어댑터를 연결할 수 있으므로 여러 가지 미세 조정된 추론 요청을 한 번에 제공할 수 있습니다.

LoRA로 미세 조정하면 사용자 지정 모델 가중치( [세이프텐서](https://huggingface.co/docs/safetensors/en/index) 형식)와 어댑터 구성 파일(json 형식)의 두 가지 파일이 출력됩니다. 이러한 가중치를 직접 생성하려면 [Hugging Face PEFT](https://huggingface.co/docs/peft/en/tutorial/peft_model_config)(매개변수 효율적 미세 조정) 라이브러리와 [Hugging Face AutoTrain LLM 라이브러리](https://huggingface.co/docs/autotrain/en/llm_finetuning)를 함께 사용하여 자체 데이터에 대해 LoRA를 학습시킬 수 있습니다. [Auto Train](https://huggingface.co/autotrain) 및 [Google Colab](https://colab.research.google.com/) 등의 서비스에서 학습 작업을 실행할 수도 있습니다. 아니면, 현재 [Hugging Face](https://huggingface.co/models?pipeline_tag=text-generation&sort=trending&search=mistral+lora)에도 다양한 사용 사례를 지원하는 많은 오픈 소스 LoRA 어댑터가 있습니다.

저희는 궁극적으로는 플랫폼에서 LoRA 학습 워크로드를 지원하고자 하지만, 지금 당장 학습된 LoRA 어댑터를 Workers AI에 가져와야 하므로 이 기능을 BYO(Bring Your Own) LoRA라고 부르고 있습니다.

초기 오픈 베타 릴리스에서는 저희 Mistral, Llama, Gemma 모델에서 LoRA를 사용할 수 있도록 허용하고 있습니다. 이러한 모델의 경우 LoRA를 허용하는 버전이 따로 마련되어 있으며, 모델 이름 끝에 ``-lora``를 추가하면 액세스할 수 있습니다. 아래 나열된 지원되는 기본 모델 중 하나에서 어댑터를 미세 조정해야 합니다.

  * `@cf/meta-llama/llama-2-7b-chat-hf-lora`
  * `@cf/mistral/mistral-7b-instruct-v0.2-lora`
  * `@cf/google/gemma-2b-it-lora`
  * `@cf/google/gemma-7b-it-lora`



이 기능은 오픈 베타 버전으로 출시하는 만큼, 현재 몇 가지 제약이 있습니다. 양자화된 LoRA 모델은 아직 지원되지 않고, LoRA 어댑터는 100MB 미만이어야 하며 최대 랭크 8까지만 지원되고, 초기 오픈 베타 버전에서는 계정당 최대 30개의 LoRA를 사용해 볼 수 있습니다. Workers AI에서 LoRA를 시작하려면 [개발자 문서](https://developers.cloudflare.com/workers-ai/fine-tunes/loras)를 참조하세요.

항상 그렇듯이, 저희는 고객이 모델별 라이선스 약관에 포함된 모델별 사용 제약을 포함하여 [서비스 약관](https://www.cloudflare.com/service-specific-terms-developer-platform/#developer-platform-terms)을 염두에 두면서 Workers AI와 새로운 BYO LoRA 기능을 사용하길 기대합니다.

## 다중 테넌트 LoRA 서비스를 어떻게 구축했을까요?

여러 LoRA 모델을 동시에 서비스하면 GPU 리소스 사용률 측면에서 문제가 발생합니다. 추론 요청을 기본 모델에 일괄 처리할 수는 있지만, 고유한 LoRA 어댑터에 서비스를 제공해야 하는 복잡성이 추가되므로 요청을 일괄 처리하는 것이 훨씬 더 어렵습니다. 이 문제를 해결하기 위해 저희는 글로벌 캐시 최적화와 함께 Punica CUDA 커널 설계를 활용하여 다중 테넌트 LoRA 서비스의 메모리 집약적인 워크로드를 처리하는 동시에 짧은 추론 대기 시간을 제공합니다.

Punica CUDA 커널은 [Punica: 다중 테넌트 LoRA 서비스](https://arxiv.org/abs/2310.18547) 논문에서 동일한 기본 모델에 적용된 상당히 다른 여러 개의 LoRA 모델을 서비스하는 방법으로 소개되었습니다. 이 방법은 이전의 추론 기법에 비해 처리량과 대기 시간이 크게 개선되었습니다. 이러한 최적화는 부분적으로는 서로 다른 LoRA 어댑터에 서비스를 제공하는 요청 간에도 요청 일괄 처리를 가능하게 함으로써 달성됩니다.

Punica 커널 시스템의 핵심은 Segmented Gather Matrix-Vector Multiplication(SGMV)이라는 새로운 CUDA 커널입니다. SGMV를 사용하면 GPU가 사전 학습된 모델의 사본 하나만 저장하면서 다른 LoRA 모델을 제공할 수 있습니다. Punica 커널 설계 시스템은 고유한 LoRA 모델에 대한 요청을 일괄 처리하여 다양한 요청의 기능 가중치 곱셈을 병렬화함으로써 성능을 개선합니다. 그런 다음 동일한 LoRA 모델에 대한 요청을 그룹화하여 운영 강도를 높입니다. 처음에 GPU는 기본 모델을 로드하면서 대부분의 GPU 메모리를 KV 캐시용으로 예약합니다. 그런 다음 수신 요청에 의해 필요할 때 원격 스토리지(Cloudflare의 캐시 또는 R2)에서 LoRA 구성 요소(A 및 B 행렬)를 온디맨드 방식으로 로드합니다. 이 온디맨드 로딩은 밀리초의 대기 시간만 발생하므로 추론 성능에 미치는 영향을 최소화하면서 여러 개의 LoRA 어댑터를 원활하게 가져와 제공할 수 있습니다. 자주 요청되는 LoRA 어댑터는 최대한 빠른 추론을 위해 캐시됩니다.

요청된 LoRA가 로컬에 캐시된 후에는 추론에 사용할 수 있는 속도가 PCIe 대역폭에 따라서만 제한됩니다. 그럼에도 불구하고 각 요청마다 자체 LoRA가 필요할 수 있으므로 LoRA 다운로드 및 메모리 복사 작업이 비동기적으로 수행되는 것이 중요합니다. Punica 스케줄러는 이 문제를 정확히 해결하여 현재 GPU 메모리에서 필요한 LoRA 가중치를 사용할 수 있는 요청만 일괄 처리하고, 필요한 가중치를 사용할 수 있고 요청이 효율적으로 일괄 처리에 참여할 수 있을 때까지 가중치를 사용할 수 없는 요청은 대기열에 대기시킵니다.

KV 캐시를 효과적으로 관리하고 이러한 요청을 일괄 처리하면 상당한 규모의 다중 테넌트 LoRA 서비스 워크로드를 처리할 수 있습니다. 또 다른 중요한 최적화는 연속 일괄 처리를 사용하는 것입니다. 일반적인 일괄 처리 방법은 동일한 어댑터에 대한 모든 요청이 중지 조건에 도달해야 해제됩니다. 연속 일괄 처리를 사용하면 일괄 처리 요청을 조기에 릴리스하여 가장 오래 실행 중인 요청을 기다릴 필요가 없도록 할 수 있습니다.

Cloudflare의 네트워크에 배포된 LLM은 전 세계에 걸쳐 사용 가능하므로, LoRA 어댑터 모델도 전 세계에 걸쳐 사용 가능한지 확인하는 것이 중요합니다. 저희는 조만간 Cloudflare의 에지에서 캐시되는 원격 모델 파일을 구현하여 추론 대기 시간을 더욱 줄일 예정입니다.

## Workers AI의 미세 조정을 위한 로드맵

LoRA 어댑터에 대한 지원을 시작하는 것은 플랫폼의 미세 조정을 위한 중요한 단계입니다. 현재 제공되는 LLM 미세 조정 외에도 이미지 생성을 비롯한 더 많은 모델과 다양한 작업 유형을 지원할 수 있기를 기대합니다.

Workers AI의 저희 비전은 개발자가 AI 워크로드를 실행할 수 있는 최고의 공간을 마련하는 것이며, 여기에는 자체 미세 조정 프로세스도 포함됩니다. 궁극적으로는 미세 조정 학습 작업은 물론 완전히 미세 조정된 모델을 Workers AI에서 직접 실행할 계획입니다. 이를 통해 특정 작업에 대해 모델이 더 세분화되고 세부적인 기능을 갖출 수 있도록 지원함으로써 조직에서 AI의 활용도를 높일 수 있는 많은 사용 사례가 열리게 됩니다.

AI Gateway를 통해 개발자가 프롬프트와 응답을 기록하여 프로덕션 데이터로 모델을 미세 조정하는 데 사용할 수 있도록 지원할 수 있습니다. 저희 비전은 AI Gateway의 로그 데이터를 사용하여 모델을 재학습(Cloudflare에서)시킨 다음, 미세 조정된 모델을 추론을 위해 Workers AI에 다시 배포할 수 있는 원클릭 미세 조정 서비스를 제공하는 것입니다. 이를 통해 개발자는 자신의 앱에 맞게 AI 모델을 맞춤화할 수 있으며, 사용자별 수준까지 세분화할 수 있습니다. 이렇게 미세 조정된 모델은 더 작고 최적화되어 사용자가 AI 추론에 소요되는 시간과 비용을 절약할 수 있습니다. 이 모든 것이 저희 [개발자 플랫폼](https://www.cloudflare.com/developer-platform/)내에서 이루어질 수 있다는 점이 가장 큰 장점입니다.

고객들이 BYO LoRA의 오픈 베타를 사용해 보실 수 있게 되어 기쁩니다! 자세한 내용은 [개발자 문서](https://developers.cloudflare.com/workers-ai/fine-tunes)를 읽어보시고 [Discord](https://discord.cloudflare.com)에 의견을 남겨주세요.

이 페이지의 내용

온라인 토론

[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffine-tuned-inference-with-loras%2F&t=Workers%20AI%EC%97%90%EC%84%9C%20LoRA%EB%A5%BC%20%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC%20%EC%84%B8%EB%B0%80%ED%95%98%EA%B2%8C%20%EC%A1%B0%EC%A0%95%EB%90%9C%20%EB%AA%A8%EB%8D%B8%20%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0)[](https://x.com/intent/post?text=Workers+AI%EC%97%90%EC%84%9C+LoRA%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+%EC%84%B8%EB%B0%80%ED%95%98%EA%B2%8C+%EC%A1%B0%EC%A0%95%EB%90%9C+%EB%AA%A8%EB%8D%B8+%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffine-tuned-inference-with-loras%2F)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffine-tuned-inference-with-loras%2F)[](https://bsky.app/intent/compose?text=Workers+AI%EC%97%90%EC%84%9C+LoRA%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+%EC%84%B8%EB%B0%80%ED%95%98%EA%B2%8C+%EC%A1%B0%EC%A0%95%EB%90%9C+%EB%AA%A8%EB%8D%B8+%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffine-tuned-inference-with-loras%2F)[](https://mastodonshare.com/?text=Workers+AI%EC%97%90%EC%84%9C+LoRA%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+%EC%84%B8%EB%B0%80%ED%95%98%EA%B2%8C+%EC%A1%B0%EC%A0%95%EB%90%9C+%EB%AA%A8%EB%8D%B8+%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0&url=https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffine-tuned-inference-with-loras%2F)[](https://www.threads.net/intent/post?text=Workers+AI%EC%97%90%EC%84%9C+LoRA%EB%A5%BC+%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC+%EC%84%B8%EB%B0%80%ED%95%98%EA%B2%8C+%EC%A1%B0%EC%A0%95%EB%90%9C+%EB%AA%A8%EB%8D%B8+%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0+https%3A%2F%2Fblog.cloudflare.com%2Fko-kr%2Ffine-tuned-inference-with-loras%2F)

## 관련 태그

[AI](https://blog.cloudflare.com/ko-kr/tag/ai/)[Cloudflare Workers](https://blog.cloudflare.com/ko-kr/tag/workers/)[Developer Week](https://blog.cloudflare.com/ko-kr/tag/developer-week/)[Workers AI](https://blog.cloudflare.com/ko-kr/tag/workers-ai/)[개발자](https://blog.cloudflare.com/ko-kr/tag/developers/)[개발자 플랫폼](https://blog.cloudflare.com/ko-kr/tag/developer-platform/)

소셜 미디어 팔로우

  * ![Cloudflare](https://blog.cloudflare.com/images/placeholder__cloudflare.png)Cloudflare

[](https://blog.cloudflare.com/rss/)[](https://x.com/Cloudflare)[](https://www.linkedin.com/company/cloudflare-inc-)[](https://www.youtube.com/cloudflare)[](https://instagram.com/cloudflare)[](https://github.com/cloudflare)[](https://bsky.app/profile/cloudflare.social)[](https://www.threads.com/@cloudflare)[](https://www.tiktok.com/@cloudflare)




## 새 포스트 알림을 받아보세요

이메일 주소

이메일 주소를 절대 공유하지 않습니다.

구독하기

구독해 주셔서 감사합니다! 확인을 위해 수신함을 확인해 주세요.
