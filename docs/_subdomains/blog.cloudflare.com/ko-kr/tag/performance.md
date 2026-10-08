---
url: https://blog.cloudflare.com/ko-kr/tag/performance/
title: \"\uc131\ub2a5\" \ud0dc\uadf8\uac00 \uc9c0\uc815\ub41c \uac8c\uc2dc\ubb3c \u2014 Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:20:55.476814+00:00
---

# "성능" 태그가 지정된 게시물 — Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/tag/performance/

태그

# 성능

[성능 RSS 피드 구독하기](https://blog.cloudflare.com/ko-kr/tag/performance/rss)

2026년 5월 14일## [청구 파이프라인이 갑자기 느려졌습니다. 원인은 ClickHouse의 숨겨진 병목 현상이었습니다](https://blog.cloudflare.com/ko-kr/clickhouse-query-plan-contention/)

페타바이트급 ClickHouse 클러스터의 파티셔닝 변경으로 인해 중요한 청구 작업이 중단된 경우에도 표준 지표에서는 뚜렷한 오류가 보이지 않았습니다. 이 게시물에서는 Cloudflare가 ClickHouse의 쿼리 플래너에서 심각한 잠금 경합을 식별하고 이를 해결하기 위한 업스트림 패치를 구축한 방법을 살펴봅니다.

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/ko-kr/author/james-morrison/) 및 [Christian Endres](https://blog.cloudflare.com/ko-kr/author/christian-endres/)

2026년 4월 17일## [Agents Week: 네트워크 성능 업데이트](https://blog.cloudflare.com/ko-kr/network-performance-agents-week/)

Cloudflare는 요청 처리 계층을 FL2라고 하는 Rust 기반 아키텍처로 마이그레이션하여 성능이 개선되어 전 세계 상위 네트워크의 60%에 도달했습니다. Cloudflare는 실제 사용자 측정값과 연결 삼평균을 사용하여 인터넷 사용자의 실제 경험을 데이터에 반영합니다.

![Lai Yi Ohlsen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DGMNXAW2CZQQAX92W97V.png&w=64&h=64&f=webp&fit=cover&position=center)

[Lai Yi Ohlsen](https://blog.cloudflare.com/ko-kr/author/lai-yi-ohlsen/)

2026년 4월 17일## [플래그십 소개: AI 시대에 맞춰 구축된 기능 플래그](https://blog.cloudflare.com/ko-kr/flagship/)

서드파티 공급자 이용 시 발생하는 대기 시간을 근본적으로 해결하고자, Cloudflare의 글로벌 네트워크에 직접 구축한 네이티브 기능 플래그 서비스인 Flagship을 출시합니다. Flagship은 KV 및 Durable Objects를 활용하여 밀리초 미만의 속도로 플래그 평가를 수행합니다.

![Rohan Mukherjee](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49GNP12MJKQ0J7WAPF316S.webp&w=64&h=64&f=webp&fit=cover&position=center)![Abhishek Kankani](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45FNB9JVR6RAPTZN4YR8XM.png&w=64&h=64&f=webp&fit=cover&position=center)

[Rohan Mukherjee](https://blog.cloudflare.com/ko-kr/author/rohan-mukherjee/) 및 [Abhishek Kankani](https://blog.cloudflare.com/ko-kr/author/abhishek-kankani/)

2026년 3월 23일## [Cloudflare의 13세대 서버 출시: 캐시를 코어로 바꾸어 에지 컴퓨팅 성능 2배 향상](https://blog.cloudflare.com/ko-kr/gen13-launch/)

Cloudflare의 13세대 서버는 캐시와 코어의 균형을 다시 잡아 우리 컴퓨팅 처리량을 두 배로 늘렸습니다. 코어 수가 많은 AMD EPYC ™ Turin CPU로 이동하면서, 원시 컴퓨팅 밀도를 위해 대규모 L3 캐시를 바꿨습니다. 새로운 Rust 기반 FL2 스택을 실행함으로써 우리는 대기 시간 페널티를 완전히 완화하여 성능을 두 배나 개선했습니다.

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/ko-kr/author/syona/), [JQ Lau](https://blog.cloudflare.com/ko-kr/author/jq/) 및 [Jesse Brandeburg](https://blog.cloudflare.com/ko-kr/author/jesse-brandeburg/)

2026년 2월 27일## [우리에게는 더 나은 JavaScript용 스트림 API가 필요합니다](https://blog.cloudflare.com/ko-kr/a-better-web-streams-api/)

웹 스트림 API는 JavaScript 런타임에서 보편적으로 사용되지만, 다른 시대를 위해 설계되었습니다. 다음은 최신 스트리밍 API의 모습(이어야 할까요?)입니다.

![James M Snell](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47K5PBRD0MV43BH5TR121F.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[James M Snell](https://blog.cloudflare.com/ko-kr/author/jasnell/)

2026년 2월 24일## [Cloudflare가 일주일 만에 AI로 Next.js를 재구축한 방법](https://blog.cloudflare.com/ko-kr/vinext/)

한 엔지니어는 AI를 사용하여 일주일 만에 Vite에서 Next.js를 재구축했습니다. vinext는 최대 4배 더 빠르게 빌드하고, 57% 더 작은 번들을 생산하며, 단일 명령으로 Cloudflare Workers에 배포합니다.

![Steve Faulkner](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47EEQ3VXY2MHT2H3PH52N8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Steve Faulkner](https://blog.cloudflare.com/ko-kr/author/steve-faulkner/)

2026년 2월 3일## [R2 Local Upload로 글로벌 업로드 성능 개선](https://blog.cloudflare.com/ko-kr/r2-local-uploads/)

R2 로컬 업로드는 업로드 요청 시간을 최대 75%까지 단축합니다. 데이터가 즉시 사용 가능해지면, 가까운 위치에 개체 데이터를 작성하고 이를 버킷에 비동기적으로 복사합니다. 

![Frank Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45M7GJAFCCK19BX1XRJMG6.webp&w=64&h=64&f=webp&fit=cover&position=center)![Rahul Suresh](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48BG5QN16EADBCQVAZZMWT.webp&w=64&h=64&f=webp&fit=cover&position=center)![Anni Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4618C573MJFB0RNKW6K68R.png&w=64&h=64&f=webp&fit=cover&position=center)

[Frank Chen](https://blog.cloudflare.com/ko-kr/author/frank-chen/), [Rahul Suresh](https://blog.cloudflare.com/ko-kr/author/rahul-suresh/) 및 [Anni Wang](https://blog.cloudflare.com/ko-kr/author/anni/)

2025년 9월 29일## [더 나은 인터넷 구축을 지원하기 위한 15년의 여정: 2025년 창립기념일 주간 돌아보기](https://blog.cloudflare.com/ko-kr/birthday-week-2025-wrap-up/)

Rust 기반 코어 시스템, 포스트 퀀텀 업그레이드, 학생들을 위한 개발자 액세스 권한, PlanetScale 통합, 오픈 소스 파트너십, 그리고 2026년에만 1,111명의 인턴을 채용하는 역대 최대 규모의 인턴십 프로그램까지.

![Nikita Cano](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48AJSY9DYK5N26JP1Q24B7.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Korinne Alpers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JYW3RAS2PS81KW2DNQWC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nikita Cano](https://blog.cloudflare.com/ko-kr/author/nikita/) 및 [Korinne Alpers](https://blog.cloudflare.com/ko-kr/author/korinne-alpers/)

2025년 4월 1일## [“Instant Purge를 확보하면 즉시 제거 가능합니다!” — 이제 모든 고객이 모든 제거 방법을 사용할 수 있습니다](https://blog.cloudflare.com/ko-kr/instant-purge-for-all/)

업계에서 가장 빠른 제거 기능을 갖춘 데 이어, Cloudflare에서는 이제 모든 요금제에서 Instant Purge 할당량을 늘렸습니다. 

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Connor Harwood](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48PA3429BFXAR99YP0Z2ZX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Zaidoon Abd Al Hadi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45VAC8T0NPDPFZ06GAZW3H.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/ko-kr/author/alex/), [Connor Harwood](https://blog.cloudflare.com/ko-kr/author/connor-harwood/) 및 [Zaidoon Abd Al Hadi](https://blog.cloudflare.com/ko-kr/author/zaidoon/)

2024년 9월 30일## [또 한 번의 창립기념일 주간 축하를 마무리하며](https://blog.cloudflare.com/ko-kr/birthday-week-2024-wrap-up/)

2024년 창립기념일 주간 동안 발표된 주요 소식들을 다시 살펴보세요.

![Kelly May Johnston](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46WM5TMV3Y8S91FG1PQJ01.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Brendan Irvine-Broque](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H9641F9RZN2BA8BPX7HK.JPG&w=64&h=64&f=webp&fit=cover&position=center)

[Kelly May Johnston](https://blog.cloudflare.com/ko-kr/author/kelly-may-johnston/) 및 [Brendan Irvine-Broque](https://blog.cloudflare.com/ko-kr/author/brendan-irvine-broque/)

2024년 2월 28일## [Pingora 오픈 소싱: 프로그래밍 가능한 네트워크 서비스 구축을 위한 Cloudflare의 Rust 프레임워크](https://blog.cloudflare.com/ko-kr/pingora-open-source/)

프로그래밍 가능하고 메모리가 안전한 네트워크 서비스를 구축하기 위한 프레임워크인 Pingora가 이제 오픈 소스가 되었습니다. 지금 Pingora 사용을 시작하세요

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Edward Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461JESP3W5FAGRMPYV23AR.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/ko-kr/author/yuchen/), [Edward Wang](https://blog.cloudflare.com/ko-kr/author/edward-h-wang/) 및 [Andrew Hauck](https://blog.cloudflare.com/ko-kr/author/andrew-hauck/)

2023년 10월 24일## [캐시 규칙이 이제 GA이며, 캐시의 모든 부분을 정밀하게 제어할 수 있습니다](https://blog.cloudflare.com/ko-kr/cache-rules-go-ga/)

오늘, 캐시 규칙을 다른 몇 가지 규칙 제품과 함께 일반 공개(GA)로 제공하게 되어 매우 기쁘게 생각합니다. 하지만 이것으로 끝이 아닙니다. 캐시 규칙에 대한 새로운 구성 옵션도 도입합니다

![Alex Krivit](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q0QQ4YF44E63CZ5V25R6.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Krivit](https://blog.cloudflare.com/ko-kr/author/alex/)

2023년 6월 21일## [Zero Trust 스포트라이트: Cloudflare가 가장 빠르다는 증거](https://blog.cloudflare.com/ko-kr/spotlight-on-zero-trust/)

Cloudflare는 모든 중 공급자 가장 많은 테스트 시나리오의 42%에서 가장 빠른 보안 웹 게이트웨이입니다. Cloudflare는 ZTNA의 경우 Zscaler보다 46%, Netskope보다 56%, Palo Alto보다 10% 더 빠르며, RBI 시나리오의 경우 Zscaler보다 64% 더 빠릅니다

![David Tuber](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47E8A7R1CB3C4YH862R2QY.png&w=64&h=64&f=webp&fit=cover&position=center)

[David Tuber](https://blog.cloudflare.com/ko-kr/author/tubes/)
