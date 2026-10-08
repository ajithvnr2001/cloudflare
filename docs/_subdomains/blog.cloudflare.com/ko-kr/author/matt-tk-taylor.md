---
url: https://blog.cloudflare.com/ko-kr/author/matt-tk-taylor/
title: Matt \u201cTK\u201d Taylor - Cloudflare \ube14\ub85c\uadf8
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:24:41.195511+00:00
---

# Matt “TK” Taylor - Cloudflare 블로그

> Source: https://blog.cloudflare.com/ko-kr/author/matt-tk-taylor/

![Matt “TK” Taylor](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46YW143XXGWD5TFT0BBYBQ.webp&w=140&h=140&f=webp&fit=cover&position=center)

# Matt “TK” Taylor

Senior Product Manager

[](https://tk.gg)[](https://x.com/MattieTK)[](https://www.linkedin.com/in/mattietk/)[](http://github.com/mattietk)[](http://bsky.app/profile/tk.gg)

2026년 10월 2일## [전체 Cloudflare API를 위한 에이전틱 CLI, cf를 소개합니다](https://blog.cloudflare.com/ko-kr/cloudflare-cf-cli-launch/)

저희는 cf를 출시합니다. Cloudflare API 전체를 반영하고 프로그래밍 방식의 TypeScript 구성을 지원하는 새로운 명령줄 도구입니다. 또한 내부 SDK 생성기인 Forge를 오픈소스로 공개합니다.

![Matt “TK” Taylor](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46YW143XXGWD5TFT0BBYBQ.webp&w=64&h=64&f=webp&fit=cover&position=center)![Samuel Macleod](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498X1ZVM0N111DBDKB3MM1.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt “TK” Taylor](https://blog.cloudflare.com/ko-kr/author/matt-tk-taylor/) 및 [Samuel Macleod](https://blog.cloudflare.com/ko-kr/author/samuel/)

[![](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3KR63G9MAXHAG81FC5HKYRY.01M3KR64BVBYV5MM3YBHRRRWGF.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAHwAuKQAwOQAzQAYxPRAqMw0hJwAeIQAiMwowOQgyRQ85TSFDTjBKSDVKQC0/ORgsQCIxRh80USA+WjBRXUNgWUpjUkNUSi81RikxSyUzViY/YTdVZUtpYlNtWkxdUTg5QiMvSCEwViU7YTdRZklkY1FqWUlaTjQ4NhArPxIrUB4xXTFDYkBVXURaUTtOQyYyJgAoNAAmShQmWCkyWzNAVDRGRig+NQ0rHAAmLgAjRg4gViQoWC00UCo6QBs2LgAo)](https://blog.cloudflare.com/ko-kr/cloudflare-cf-cli-launch/)

2026년 10월 2일## [SDK, CLI, 문서 등을 생성하는 오픈 소스 파이프라인 Forge를 소개합니다](https://blog.cloudflare.com/ko-kr/forge-open-source-generation-pipeline/)

Forge는 CI에서 실행되어 API 정의에서 직접 SDK, CLI 및 문서를 생성하는 오픈소스의 플러거블 생성 파이프라인입니다. 생성 작업을 각 팀의 리포지터리 단계로 앞당김으로써 Forge는 개발자 도구를 지속적으로 동기화된 상태로 유지합니다.

![Dimitri Mitropoulos](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498DEF6RX03R0G7TNW7CR3.webp&w=64&h=64&f=webp&fit=cover&position=center)![Matt “TK” Taylor](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46YW143XXGWD5TFT0BBYBQ.webp&w=64&h=64&f=webp&fit=cover&position=center)![Samuel Macleod](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498X1ZVM0N111DBDKB3MM1.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Dimitri Mitropoulos](https://blog.cloudflare.com/ko-kr/author/dimitri-mitropoulos/), [Matt “TK” Taylor](https://blog.cloudflare.com/ko-kr/author/matt-tk-taylor/) 및 [Samuel Macleod](https://blog.cloudflare.com/ko-kr/author/samuel/)

[![](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3J4EWN0BM1HFWCRCV3ND3H8.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////5uz10d7xz9/12+f55+z16+vr/////v//4er3xtnzwdj30eL74er36uvt////////3un7vNX2tdP6yN/+3un76+3x////////4e3/vtj6ttb+yeL/4e3/7/H1////////6/X/zOP+xuH/1+z/6/X/9/j5////////+P//4fH/3fH/6vr/+P/////9////////////8fz/8P3/+v//////////////////////+P//9///////////////)](https://blog.cloudflare.com/ko-kr/forge-open-source-generation-pipeline/)

2026년 4월 13일## [Cloudflare 전체를 위한 CLI 구축](https://blog.cloudflare.com/ko-kr/cf-cli-local-explorer/)

Cloudflare 플랫폼 전반에 걸쳐 일관성을 유지하도록 설계된 새로운 통합 CLI인 cf와 로컬 데이터 디버깅을 함께 제공합니다. 이러한 도구는 개발자와 AI 에이전트가 거의 3,000개에 달하는 Cloudflare API 작업과 상호작용하는 방식을 간소화합니다. 

![Matt “TK” Taylor](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46YW143XXGWD5TFT0BBYBQ.webp&w=64&h=64&f=webp&fit=cover&position=center)![Dimitri Mitropoulos](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498DEF6RX03R0G7TNW7CR3.webp&w=64&h=64&f=webp&fit=cover&position=center)![Dan Carter](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46BJJATPEKV6ZZ0N22HHVH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matt “TK” Taylor](https://blog.cloudflare.com/ko-kr/author/matt-tk-taylor/), [Dimitri Mitropoulos](https://blog.cloudflare.com/ko-kr/author/dimitri-mitropoulos/) 및 [Dan Carter](https://blog.cloudflare.com/ko-kr/author/dan-carter/)

[![BLOG-3224 1](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485TAP9793CP805JNF10WC.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA////////7uvw3tng4N3f7Ovn8fTv7fLx////+fr/2NXou7LPurDFzcnP297g3+jt////7/P/wb7hkH6+iXGqqZ61xcjS0t/r////7/T/vLrjgWq7dU+jnI2uv8HQ0N/t/////P//0c/upZfNnIi7tqzE0dPe3+v1////////8e/+18/o0srf4Nzm7vH09f3/////////////+/f++fb7////////////////////////////////////////////)](https://blog.cloudflare.com/ko-kr/cf-cli-local-explorer/)

2026년 4월 1일## [WordPress의 정신적 후계자로서 플러그인 보안 문제를 해결하는 EmDash 소개](https://blog.cloudflare.com/ko-kr/emdash-wordpress/)

오늘 Astro 6.0에 구축된 전체 스택 서버리스 JavaScript CMS인 EmDash의 베타 버전을 출시합니다. 이는 기존 CMS의 기능과 최신 보안을 결합하여 샌드박스를 적용한 Worker 격리에서 플러그인을 실행합니다.

![Matt “TK” Taylor](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46YW143XXGWD5TFT0BBYBQ.webp&w=64&h=64&f=webp&fit=cover&position=center)![Matt Kane](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW475N68VWP3E9MWJKN27Q2B.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Matt “TK” Taylor](https://blog.cloudflare.com/ko-kr/author/matt-tk-taylor/) 및 [Matt Kane](https://blog.cloudflare.com/ko-kr/author/matt-kane/)

[![BLOG-3225 hero image](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47GK0E0NESPW440Q8G2ZT4.png&w=2400&h=1350&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAJgAAJgAAKgAEMAAPNgYWOQUVNwAKMwAAJQAAJwAELggUNxchPh4qPx0qOREeMAAAKAAGKwgONRgeQCQtSCs4SCo4QB8rMwYKLwcMMw8SPR0iSSkyUjA+Uy8+TCUxPw4ROQUNPAwSRRogUCYwWi48Xi09WiIxUQwUQwANRQEPTA8ZVhwoYSQ0ZyQ2ZhksYgAUSgALSwAKUAAPWgodZRUpbRYtbwsmbQASTAAKTQAHUgAJWwAXZgskbw4ocgIicQAS)](https://blog.cloudflare.com/ko-kr/emdash-wordpress/)
