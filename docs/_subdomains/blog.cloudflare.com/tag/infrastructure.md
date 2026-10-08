---
url: https://blog.cloudflare.com/tag/infrastructure/
title: Posts tagged \"Infrastructure\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:15.527661+00:00
---

# Posts tagged "Infrastructure" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/infrastructure/

TAG

# Infrastructure

[Subscribe to Infrastructure RSS feed](https://blog.cloudflare.com/tag/infrastructure/rss)

June 1, 2026## [How we reduced core unit boot time from hours to minutes](https://blog.cloudflare.com/optimizing-core-unit-boot-time/)

We investigated why firmware updates were causing our core servers to take four hours to reboot. By diving into UEFI data structures and iPXE automation, we eliminated unnecessary timeouts and cut boot times back down to minutes.

![Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48NAJ0BZMGGKBFTQQ4C0AH.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nnamdi Ajah](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WTZG75GP6EEN6AE7KXBD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Omar Sheikh-Omar](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HRKA5D763GGGRFFTW2GB.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/author/giovanni/), [Nnamdi Ajah](https://blog.cloudflare.com/author/nnamdi/), and [Omar Sheikh-Omar](https://blog.cloudflare.com/author/omar-sheikh-omar/)

April 16, 2026## [Building the foundation for running extra-large language models](https://blog.cloudflare.com/high-performance-llms/)

We built a custom technology stack to run fast large language models on Cloudflare’s infrastructure. This post explores the engineering trade-offs and technical optimizations required to make high-performance AI inference accessible.

![Michelle Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44R95PPSQQ82Z92P51M550.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Kevin Flansburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW452TM72EKFE8RQCD3JMXND.png&w=64&h=64&f=webp&fit=cover&position=center)![Vlad Krasnov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TTHCQACMZ5JZDGQP8RSQ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michelle Chen](https://blog.cloudflare.com/author/michelle/), [Kevin Flansburg](https://blog.cloudflare.com/author/kevin-flansburg/), and [Vlad Krasnov](https://blog.cloudflare.com/author/vlad-krasnov/)

March 26, 2026## [A one-line Kubernetes fix that saved 600 hours a year](https://blog.cloudflare.com/one-line-kubernetes-fix-saved-600-hours-a-year/)

When we investigated why our Atlantis instance took 30 minutes to restart, we discovered a bottleneck in how Kubernetes handles volume permissions. By adjusting the fsGroupChangePolicy, we reduced restart times to 30 seconds.

![Braxton Schafer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N6SPVMSAH9848VNNQD2K.png&w=64&h=64&f=webp&fit=cover&position=center)

[Braxton Schafer](https://blog.cloudflare.com/author/braxton-schafer/)

March 23, 2026## [Inside Gen 13: how we built our most powerful server yet](https://blog.cloudflare.com/gen13-config/)

Cloudflare's Gen 13 servers introduce AMD EPYC™ Turin 9965 processors and a transition to 100 GbE networking to meet growing traffic demands. In this technical deep dive, we explain the engineering rationale behind each major component selection.

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Ma Xiong](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SJ3NTWPAG4GT7D5C6D7W.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Victor Hwang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46G24ZH6T4DQPBFY5FRAM7.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/author/syona/), [JQ Lau](https://blog.cloudflare.com/author/jq/), [Ma Xiong](https://blog.cloudflare.com/author/ma-xiong/), and [Victor Hwang](https://blog.cloudflare.com/author/victor-hwang/)

March 23, 2026## [Launching Cloudflare’s Gen 13 servers: trading cache for cores for 2x edge compute performance](https://blog.cloudflare.com/gen13-launch/)

Cloudflare’s Gen 13 servers double our compute throughput by rethinking the balance between cache and cores. Moving to high-core-count AMD EPYC ™ Turin CPUs, we traded large L3 cache for raw compute density. By running our new Rust-based FL2 stack, we completely mitigated the latency penalty to unlock twice the performance.

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/author/syona/), [JQ Lau](https://blog.cloudflare.com/author/jq/), and [Jesse Brandeburg](https://blog.cloudflare.com/author/jesse-brandeburg/)

February 13, 2026## [Shedding old code with ecdysis: graceful restarts for Rust services at Cloudflare](https://blog.cloudflare.com/ecdysis-rust-graceful-restarts/)

ecdysis is a Rust library enabling zero-downtime upgrades for network services. After five years protecting millions of connections at Cloudflare, it’s now open source.

![Manuel Olguín Muñoz](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45MRZQBM4H5K19ZVS98WTD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Manuel Olguín Muñoz](https://blog.cloudflare.com/author/manuel-olguin-munoz/)

December 22, 2025## [How Workers powers our internal maintenance scheduling pipeline](https://blog.cloudflare.com/building-our-maintenance-scheduler-on-workers/)

Physical data center maintenance is risky on a global network. We built a maintenance scheduler on Workers to safely plan disruptive operations, while solving scaling challenges by viewing the state of our infrastructure through a graph interface on top of multiple data sources and metrics pipelines.

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/author/kevin-deems/) and [Michael Hoffmann](https://blog.cloudflare.com/author/michael-hoffmann/)

October 22, 2024## [Is this thing on? Using OpenBMC and ACPI power states for reliable server boot](https://blog.cloudflare.com/how-we-use-openbmc-and-acpi-power-states-to-monitor-the-state-of-our-servers/)

Cloudflare’s global fleet benefits from being managed by open source firmware for the Baseboard Management Controller (BMC), OpenBMC. This has come with various challenges, some of which we discuss here with an explanation of how the open source nature of the firmware for the BMC enabled us to fix the issues and maintain a more stable fleet.

![Nnamdi Ajah](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WTZG75GP6EEN6AE7KXBD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Ryan Chow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47FP9YD719DQJ7ZWBN55MS.png&w=64&h=64&f=webp&fit=cover&position=center)![Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48NAJ0BZMGGKBFTQQ4C0AH.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nnamdi Ajah](https://blog.cloudflare.com/author/nnamdi/), [Ryan Chow](https://blog.cloudflare.com/author/ryan-chow/), and [Giovanni Pereira Zantedeschi](https://blog.cloudflare.com/author/giovanni/)

October 8, 2024## [Leveraging Kubernetes virtual machines at Cloudflare with KubeVirt](https://blog.cloudflare.com/leveraging-kubernetes-virtual-machines-with-kubevirt/)

The Kubernetes team runs several multi-tenant clusters across Cloudflare’s core data centers. When multi-tenant cluster isolation is too limiting for an application, we use KubeVirt. KubeVirt is a cloud-native solution that enables our developers to run virtual machines alongside containers.

![Justin Cichra](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48EAA1E9PF3JQT3M2B9H89.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Justin Cichra](https://blog.cloudflare.com/author/justin-cichra/)
