---
url: https://blog.cloudflare.com/ko-kr/tag/infrastructure/
title: \"\uc778\ud504\ub77c\" \ud0dc\uadf8\uac00 \uc9c0\uc815\ub41c \uac8c\uc2dc\ubb3c \u2014 Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:20:44.829646+00:00
---

# "인프라" 태그가 지정된 게시물 — Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/tag/infrastructure/

태그

# 인프라

[인프라 RSS 피드 구독하기](https://blog.cloudflare.com/ko-kr/tag/infrastructure/rss)

2026년 6월 1일## [코어 장치의 부팅 시간을 몇 시간에서 몇 분으로 단축한 방법](https://blog.cloudflare.com/ko-kr/optimizing-core-unit-boot-time/)

우리는 펌웨어 업데이트로 인해 코어 서버가 재부팅되는 데 4시간이 걸리는 이유를 조사했습니다. UEFI 데이터 구조와 iPXE 자동화를 자세히 살펴본 결과, 불필요한 제한 시간 초과를 제거하고 부팅 시간을 몇 분 단위로 단축할 수 있었습니다.

![Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48NAJ0BZMGGKBFTQQ4C0AH.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nnamdi Ajah](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WTZG75GP6EEN6AE7KXBD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Omar Sheikh-Omar](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HRKA5D763GGGRFFTW2GB.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/ko-kr/author/giovanni/), [Nnamdi Ajah](https://blog.cloudflare.com/ko-kr/author/nnamdi/) 및 [Omar Sheikh-Omar](https://blog.cloudflare.com/ko-kr/author/omar-sheikh-omar/)

2026년 4월 16일## [초대형 언어 모델을 실행하기 위한 기반 다지기](https://blog.cloudflare.com/ko-kr/high-performance-llms/)

Cloudflare는 자체 인프라 환경에서 대규모 언어 모델을 신속하게 실행할 수 있도록 맞춤형 기술 스택을 구축했습니다. 본 게시물에서는 누구나 고성능 AI 추론 환경을 활용할 수 있도록 구현하는 과정에서 적용된 엔지니어링 측면의 절충 사항과 기술적 최적화 과정을 살펴봅니다.

![Michelle Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44R95PPSQQ82Z92P51M550.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Kevin Flansburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW452TM72EKFE8RQCD3JMXND.png&w=64&h=64&f=webp&fit=cover&position=center)![Vlad Krasnov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TTHCQACMZ5JZDGQP8RSQ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michelle Chen](https://blog.cloudflare.com/ko-kr/author/michelle/), [Kevin Flansburg](https://blog.cloudflare.com/ko-kr/author/kevin-flansburg/) 및 [Vlad Krasnov](https://blog.cloudflare.com/ko-kr/author/vlad-krasnov/)

2026년 3월 26일## [한 줄 쿠버네티스 수정으로 연간 600시간 절약](https://blog.cloudflare.com/ko-kr/one-line-kubernetes-fix-saved-600-hours-a-year/)

Atlantis 인스턴스를 다시 시작하는 데 30분이 걸리는 이유를 조사한 결과, Kubernetes가 볼륨 권한을 처리하는 방식에서 병목 현상을 발견했습니다. 우리는 fsGroupchangePolicy를 조정하여 재시작 시간을 30초로 단축했습니다.

![Braxton Schafer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N6SPVMSAH9848VNNQD2K.png&w=64&h=64&f=webp&fit=cover&position=center)

[Braxton Schafer](https://blog.cloudflare.com/ko-kr/author/braxton-schafer/)

2026년 3월 23일## [Cloudflare의 13세대 서버 출시: 캐시를 코어로 바꾸어 에지 컴퓨팅 성능 2배 향상](https://blog.cloudflare.com/ko-kr/gen13-launch/)

Cloudflare의 13세대 서버는 캐시와 코어의 균형을 다시 잡아 우리 컴퓨팅 처리량을 두 배로 늘렸습니다. 코어 수가 많은 AMD EPYC ™ Turin CPU로 이동하면서, 원시 컴퓨팅 밀도를 위해 대규모 L3 캐시를 바꿨습니다. 새로운 Rust 기반 FL2 스택을 실행함으로써 우리는 대기 시간 페널티를 완전히 완화하여 성능을 두 배나 개선했습니다.

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/ko-kr/author/syona/), [JQ Lau](https://blog.cloudflare.com/ko-kr/author/jq/) 및 [Jesse Brandeburg](https://blog.cloudflare.com/ko-kr/author/jesse-brandeburg/)

2026년 2월 13일## [ecdysis로 오래된 코드 사용하기: Cloudflare의 Rust 서비스를 위한 우아한 재시작](https://blog.cloudflare.com/ko-kr/ecdysis-rust-graceful-restarts/)

ecdysis는 네트워크 서비스의 다운타임 없이 업그레이드할 수 있는 Rust 라이브러리입니다. Cloudflare에서는 수백만 개의 연결을 5년 동안 보호해 온 이후, 이제 오픈 소스가 되었습니다.

![Manuel Olguín Muñoz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MRZQBM4H5K19ZVS98WTD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Manuel Olguín Muñoz](https://blog.cloudflare.com/ko-kr/author/manuel-olguin-munoz/)

2025년 12월 22일## [Workers가 내부 유지 관리 일정 파이프라인을 강화하는 방법](https://blog.cloudflare.com/ko-kr/building-our-maintenance-scheduler-on-workers/)

물리적 데이터 센터 유지 관리는 전역 네트워크에서 위험합니다. 당사는 중단되는 작업을 안전하게 계획할 수 있도록 워커스에 유지 관리 스케줄러를 구축했으며, 여러 데이터 소스와 메트릭 파이프라인 위에 있는 그래프 인터페이스를 통해 인프라 상태를 확인하여 확장 문제를 해결했습니다.

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/ko-kr/author/kevin-deems/) 및 [Michael Hoffmann](https://blog.cloudflare.com/ko-kr/author/michael-hoffmann/)
