---
url: https://blog.cloudflare.com/ko-kr/tag/rust/
title: \"Rust\" \ud0dc\uadf8\uac00 \uc9c0\uc815\ub41c \uac8c\uc2dc\ubb3c \u2014 Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:21:02.094214+00:00
---

# "Rust" 태그가 지정된 게시물 — Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/tag/rust/

태그

# Rust

[Rust RSS 피드 구독하기](https://blog.cloudflare.com/ko-kr/tag/rust/rss)

2026년 5월 12일## ['유휴'가 유휴가 아닐 때: Linux 커널 최적화가 QUIC 버그가 된 방법](https://blog.cloudflare.com/ko-kr/quic-death-spiral-fix/)

CUBIC에서는 CUBIC의 혼잡 기간이 최소 층에 고정되어 성능이 급감하는 버그를 조사했습니다. 이 문제를 해결하려면 RTT 대기 시간과 실제 애플리케이션 유휴 시간을 구분하기 위해 유휴 기간을 올바르게 측정해야 했습니다.

![Esteban Carisimo](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VSSKPEBK3K5ND6JZ67YP.webp&w=64&h=64&f=webp&fit=cover&position=center)![Antonio Vicente](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW487NFE7AY4B70WNGYX9WZ9.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Esteban Carisimo](https://blog.cloudflare.com/ko-kr/author/esteban-carisimo/) 및 [Antonio Vicente](https://blog.cloudflare.com/ko-kr/author/antonio-vicente/)

2026년 4월 22일## [Rust Workers를 안정적으로 만들기: wasm-bindgen에서의 패닉 및 중단 복구](https://blog.cloudflare.com/ko-kr/making-rust-workers-reliable/)

Rust Workers에서의 패닉은 역사적으로 치명적이었으며 전체 인스턴스를 중독시켰습니다. Rust Workers는 이제 Wasm-bindgen 프로젝트에서 업스트림과 협업하여 WebAssembly 예외 처리를 사용한 패닉 상태를 해결하는 등 탄력적인 중요 오류 복구를 지원합니다.

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/ko-kr/author/guy-bedford/), [Hood Chatham](https://blog.cloudflare.com/ko-kr/author/hood/) 및 [Logan Gatlin](https://blog.cloudflare.com/ko-kr/author/logan-gatlin/)

2026년 4월 17일## [Agents Week: 네트워크 성능 업데이트](https://blog.cloudflare.com/ko-kr/network-performance-agents-week/)

Cloudflare는 요청 처리 계층을 FL2라고 하는 Rust 기반 아키텍처로 마이그레이션하여 성능이 개선되어 전 세계 상위 네트워크의 60%에 도달했습니다. Cloudflare는 실제 사용자 측정값과 연결 삼평균을 사용하여 인터넷 사용자의 실제 경험을 데이터에 반영합니다.

![Lai Yi Ohlsen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DGMNXAW2CZQQAX92W97V.png&w=64&h=64&f=webp&fit=cover&position=center)

[Lai Yi Ohlsen](https://blog.cloudflare.com/ko-kr/author/lai-yi-ohlsen/)

2026년 3월 23일## [Cloudflare의 13세대 서버 출시: 캐시를 코어로 바꾸어 에지 컴퓨팅 성능 2배 향상](https://blog.cloudflare.com/ko-kr/gen13-launch/)

Cloudflare의 13세대 서버는 캐시와 코어의 균형을 다시 잡아 우리 컴퓨팅 처리량을 두 배로 늘렸습니다. 코어 수가 많은 AMD EPYC ™ Turin CPU로 이동하면서, 원시 컴퓨팅 밀도를 위해 대규모 L3 캐시를 바꿨습니다. 새로운 Rust 기반 FL2 스택을 실행함으로써 우리는 대기 시간 페널티를 완전히 완화하여 성능을 두 배나 개선했습니다.

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/ko-kr/author/syona/), [JQ Lau](https://blog.cloudflare.com/ko-kr/author/jq/) 및 [Jesse Brandeburg](https://blog.cloudflare.com/ko-kr/author/jesse-brandeburg/)

2026년 2월 13일## [ecdysis로 오래된 코드 사용하기: Cloudflare의 Rust 서비스를 위한 우아한 재시작](https://blog.cloudflare.com/ko-kr/ecdysis-rust-graceful-restarts/)

ecdysis는 네트워크 서비스의 다운타임 없이 업그레이드할 수 있는 Rust 라이브러리입니다. Cloudflare에서는 수백만 개의 연결을 5년 동안 보호해 온 이후, 이제 오픈 소스가 되었습니다.

![Manuel Olguín Muñoz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MRZQBM4H5K19ZVS98WTD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Manuel Olguín Muñoz](https://blog.cloudflare.com/ko-kr/author/manuel-olguin-munoz/)

2025년 12월 18일## [R2 SQL에서 GROUP BY, SUM 및 기타 집계 쿼리 지원 발표](https://blog.cloudflare.com/ko-kr/r2-sql-aggregations/)

분산 쿼리 엔진인 Cloudflare의 R2 SQL에서 이제 집계를 지원합니다. R2 데이터 카탈로그에서 직접 분석을 실행하기 위해 분산형 수집, 셔플링 전략을 사용하여 분산형 GROUP BY 실행을 구축한 방법을 알아보세요.

![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)![Nikita Lapkov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GWQBCE99JFFMKC6GVZEX.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Marc Selwan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455H274J0ZYJ6K4KHKJT25.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Jérôme Schneider](https://blog.cloudflare.com/ko-kr/author/jerome/), [Nikita Lapkov](https://blog.cloudflare.com/ko-kr/author/nikita-lapkov/) 및 [Marc Selwan](https://blog.cloudflare.com/ko-kr/author/marc-selwan/)

2025년 10월 28일## [인터넷의 빠른 속도와 보안 유지: 머클 트리 인증서 소개](https://blog.cloudflare.com/ko-kr/bootstrap-mtc/)

Cloudflare는 Chrome으로 실험을 시작하여 성능을 저하시키거나 WebPKI 신뢰 관계를 변경하지 않고도 빠르고 확장 가능하며 양자 준비 Merkle Tree 인증서를 평가하고 있습니다.

![Luke Valenta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BBR3DXDBC0E9512XF44.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Christopher Patton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW471WT491ZC11M0S5HA34X3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Vânia Gonçalves](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48DQDQ26SRVKPGYTBWBHMD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Bas Westerbaan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46N3BWJ6WS6790KRRJ4RWD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Luke Valenta](https://blog.cloudflare.com/ko-kr/author/luke/), [Christopher Patton](https://blog.cloudflare.com/ko-kr/author/christopher-patton/), [Vânia Gonçalves](https://blog.cloudflare.com/ko-kr/author/vania/) 및 [Bas Westerbaan](https://blog.cloudflare.com/ko-kr/author/bas/)

2025년 9월 26일## [Rust 덕분에 더 빠르고 안전해진 Cloudflare](https://blog.cloudflare.com/ko-kr/20-percent-internet-upgrade/)

Cloudflare의 기존 코어 시스템을 새로운 모듈식 Rust 기반 프록시로 교체하여 NGINX를 대체했습니다. 

![Richard Boulton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WPC6H4PY51ETZPAGBKZ9.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Steve Goldsmith](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW497YX7768BEJGS24P0FMX8.png&w=64&h=64&f=webp&fit=cover&position=center)![Maurizio Abba](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45R40JSMY4JX26YZV11150.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Matthew Bullock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48ABWPJWE9RP8CPZF1G4F5.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Richard Boulton](https://blog.cloudflare.com/ko-kr/author/richard/), [Steve Goldsmith](https://blog.cloudflare.com/ko-kr/author/steve-goldsmith/), [Maurizio Abba](https://blog.cloudflare.com/ko-kr/author/maurizio-abba/) 및 [Matthew Bullock](https://blog.cloudflare.com/ko-kr/author/matthew-bullock/)

2024년 2월 28일## [Pingora 오픈 소싱: 프로그래밍 가능한 네트워크 서비스 구축을 위한 Cloudflare의 Rust 프레임워크](https://blog.cloudflare.com/ko-kr/pingora-open-source/)

프로그래밍 가능하고 메모리가 안전한 네트워크 서비스를 구축하기 위한 프레임워크인 Pingora가 이제 오픈 소스가 되었습니다. 지금 Pingora 사용을 시작하세요

![Yuchen Wu](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47CEA1K0ZA59ZK5J7QNRVF.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Edward Wang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW461JESP3W5FAGRMPYV23AR.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Andrew Hauck](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44PMGPP5RFKJT72RPHZAYC.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Yuchen Wu](https://blog.cloudflare.com/ko-kr/author/yuchen/), [Edward Wang](https://blog.cloudflare.com/ko-kr/author/edward-h-wang/) 및 [Andrew Hauck](https://blog.cloudflare.com/ko-kr/author/andrew-hauck/)

2018년 1월 31일## [Rust 로 복잡한 매크로를 작성하기: 역폴란드 표기법​](https://blog.cloudflare.com/ko-kr/writing-complex-macros-in-rust-reverse-polish-notation/)

Rust에는 흥미로운 기능이 많지만 그중에도 강력한 매크로 시스템이 있습니다. 하지만 The Book과 여러가지 튜토리얼을 읽고 나서도 서로 다른 요소의 복잡한 리스트를 처리하는 매크로를 구현하려고 하면 저는 여전히 어떻게 만들어야 하는지를 이해하는데 힘들어 하며

![Ingvar Stepanyan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HXZCX2W0E3TV8QJY1YTY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ingvar Stepanyan](https://blog.cloudflare.com/ko-kr/author/ingvar-stepanyan/)
