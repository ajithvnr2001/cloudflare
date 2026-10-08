---
url: https://blog.cloudflare.com/tag/reliability/
title: Posts tagged \"Reliability\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:24:56.246106+00:00
---

# Posts tagged "Reliability" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/reliability/

TAG

# Reliability

[Subscribe to Reliability RSS feed](https://blog.cloudflare.com/tag/reliability/rss)

October 6, 2026## [The keys to the Internet change on October 11. Are you ready?](https://blog.cloudflare.com/root-ksk-2024-rollover/)

On October 11, 2026, the DNS root switches to a new key-signing key (KSK-2024). Learn what this means for you, and how RFC 8509 trust anchor sentinels allow you to test whether your DNS resolver is ready for the rollover.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![James Godlewski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M48ZN7537R9D7AB9PWK3P0Q9.01M48ZN84M75FBR63MKDCQTCED.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/) and [James Godlewski](https://blog.cloudflare.com/author/james-godlewski/)

September 28, 2026## [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/)

With the new experimental support for the Emscripten target in Rust Workers, many previously unsupported Rust libraries and applications can now be built and deployed directly to Cloudflare’s global Workers platform, including upcoming support for Tokio async. 

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Mitch Foley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3AKQWSJP6J7R9A91N8QTSGE.01M3AKR1JETQEG5MGZZENGC42C.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/author/guy-bedford/) and [Mitch Foley](https://blog.cloudflare.com/author/mitch-foley/)

July 14, 2026## [A broken DNSSEC rollover took down .al. Now 1.1.1.1 tells you when validation is bypassed](https://blog.cloudflare.com/dnssec-nta-ede-33/)

When a failed DNSSEC key rollover took down the .al TLD, we deployed a Negative Trust Anchor to restore resolution. This time, though, clients didn't have to take our word for it: 1.1.1.1 returned EDE 33, a new DNS error code that signals directly in the response that DNSSEC validation was bypassed.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/)

May 6, 2026## [When DNSSEC goes wrong: how we responded to the .de TLD outage](https://blog.cloudflare.com/de-tld-outage-dnssec/)

On May 5, 2026, DENIC published broken DNSSEC signatures for the .de TLD, making millions of domains unreachable. Here's what 1.1.1.1 saw, how serve stale cushioned the impact, and how we restored resolution.

![Sebastiaan Neuteboom](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48GH720TA5A2634QYMAXZR.png&w=64&h=64&f=webp&fit=cover&position=center)![Christian Elmerot](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW474H2CPWRSBJ9DXXAEA3KM.png&w=64&h=64&f=webp&fit=cover&position=center)![Max Worsley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46G5JWQ32WMKW8WD2K1HGX.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Sebastiaan Neuteboom](https://blog.cloudflare.com/author/sebastiaan-neuteboom/), [Christian Elmerot](https://blog.cloudflare.com/author/christian-elmerot/), and [Max Worsley](https://blog.cloudflare.com/author/max-worsley/)

April 22, 2026## [Making Rust Workers reliable: panic and abort recovery in wasm‑bindgen](https://blog.cloudflare.com/making-rust-workers-reliable/)

Panics in Rust Workers were historically fatal, poisoning the entire instance. By collaborating upstream on the wasm‑bindgen project, Rust Workers now support resilient critical error recovery, including panic unwinding using WebAssembly Exception Handling.

![Guy Bedford](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EK56GG251YRHAXKS587V.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Hood Chatham](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DGCR56ZBCN9NTBRE18MF.webp&w=64&h=64&f=webp&fit=cover&position=center)![Logan Gatlin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47MBZXTSY5013HEJC8611B.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guy Bedford](https://blog.cloudflare.com/author/guy-bedford/), [Hood Chatham](https://blog.cloudflare.com/author/hood/), and [Logan Gatlin](https://blog.cloudflare.com/author/logan-gatlin/)

December 22, 2025## [How Workers powers our internal maintenance scheduling pipeline](https://blog.cloudflare.com/building-our-maintenance-scheduler-on-workers/)

Physical data center maintenance is risky on a global network. We built a maintenance scheduler on Workers to safely plan disruptive operations, while solving scaling challenges by viewing the state of our infrastructure through a graph interface on top of multiple data sources and metrics pipelines.

![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kevin Deems](https://blog.cloudflare.com/author/kevin-deems/) and [Michael Hoffmann](https://blog.cloudflare.com/author/michael-hoffmann/)

May 16, 2025## [Vulnerability transparency: strengthening security through responsible disclosure](https://blog.cloudflare.com/vulnerability-transparency-strengthening-security-through-responsible/)

In line with CISA’s Secure By Design pledge, Cloudflare shares its vulnerability disclosure process, CVE issuance criteria, and CNA duties. 

![Sri Pulla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW488S03VFKMWA6R1576TKF2.webp&w=64&h=64&f=webp&fit=cover&position=center)![Martin Schwarzl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q44FVCNYF3AKGF6DGP9G.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Trishna](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473JDQZAHNE7Y35PPZ0HNB.webp&w=64&h=64&f=webp&fit=cover&position=center)

[Sri Pulla](https://blog.cloudflare.com/author/sri-pulla/), [Martin Schwarzl](https://blog.cloudflare.com/author/martin/), and [Trishna](https://blog.cloudflare.com/author/trishna/)

May 5, 2025## [Scaling with safety: Cloudflare's approach to global service health metrics and software releases](https://blog.cloudflare.com/safe-change-at-any-scale/)

Learn how Cloudflare tackles the challenge of scaling global service health metrics to safely release new software across our global network.

![Harshal Brahmbhatt](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW490090MSM5DHXJVA4Q6QKS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Kevin Deems](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DYXVM2ZEP0CAPVRVBRSS.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Nina Giunta](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4470FRM6R4D2BD2M7GE3R2.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michael Hoffmann](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46FZ19DMV4JVQ1GXNF27JJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Harshal Brahmbhatt](https://blog.cloudflare.com/author/harshal/), [Kevin Deems](https://blog.cloudflare.com/author/kevin-deems/), [Nina Giunta](https://blog.cloudflare.com/author/nina-giunta/), and [Michael Hoffmann](https://blog.cloudflare.com/author/michael-hoffmann/)

January 14, 2025## [Demonstrating reduction of vulnerability classes: a key step in CISA’s “Secure by Design” pledge](https://blog.cloudflare.com/cisa-pledge-commitment-reducing-vulnerability/)

Cloudflare strengthens its commitment to cybersecurity by joining CISA's "Secure by Design" pledge. In line with this, we're reducing the prevalence of vulnerability classes across our products.

![Sri Pulla](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW488S03VFKMWA6R1576TKF2.webp&w=64&h=64&f=webp&fit=cover&position=center)![Trishna](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW473JDQZAHNE7Y35PPZ0HNB.webp&w=64&h=64&f=webp&fit=cover&position=center)![Jordan Lilly](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46TD6HQFQN9DV6CE5GAKK8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Sri Pulla](https://blog.cloudflare.com/author/sri-pulla/), [Trishna](https://blog.cloudflare.com/author/trishna/), and [Jordan Lilly](https://blog.cloudflare.com/author/jordan-lilly/)

October 9, 2024## [Improving platform resilience at Cloudflare through automation](https://blog.cloudflare.com/improving-platform-resilience-at-cloudflare/)

We realized that we need a way to automatically heal our platform from an operations perspective, and designed and built a workflow orchestration platform to provide these self-healing capabilities 

![Opeyemi Onikute](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46MTRK7JGFXBPN75JQ23DW.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Opeyemi Onikute](https://blog.cloudflare.com/author/opeyemi/)

March 4, 2024## [Changing the industry with CISA’s Secure by Design principles](https://blog.cloudflare.com/secure-by-design-principles/)

Security considerations should be an integral part of software’s design, not an afterthought. Explore how Cloudflare adheres to CISA’s Secure by Design principles to shift the industry

![Kristina Galicova](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46SE6FVY39NNKJ8GYZXBZN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Edo Royker](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NPG0HKPB45GKW757SAW2.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kristina Galicova](https://blog.cloudflare.com/author/kristina-galicova/) and [Edo Royker](https://blog.cloudflare.com/author/edo-royker/)

August 2, 2023## [Hardening Workers KV](https://blog.cloudflare.com/workers-kv-restoring-reliability/)

A deep dive into the recent incidents relating to Workers KV, and how we’re going to fix them

![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Charles Burnett](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW486HGDG61NW3BS074QQ6DP.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Rob Sutter](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44VM3GCX6DGHVJ06XGV8XA.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Kris Evans](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW468R5MMKJMBEQRR7JPTXDX.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Silverlock](https://blog.cloudflare.com/author/silverlock/), [Charles Burnett](https://blog.cloudflare.com/author/charles/), [Rob Sutter](https://blog.cloudflare.com/author/rob/), and [Kris Evans](https://blog.cloudflare.com/author/kris-evans/)

June 23, 2023## [How we scaled and protected Eurovision 2023 voting with Pages and Turnstile](https://blog.cloudflare.com/how-cloudflare-scaled-and-protected-eurovision-2023-voting/)

More than 162 million fans tuned in to the 2023 Eurovision Song Contest, the first year that non-participating countries could also vote. Cloudflare helped scale and protect the voting application based.io, built by once.net using our rapid DNS infrastructure, CDN, Cloudflare Pages and Turnstile

![Dirk-Jan van Helmond](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46B7KN0JQQA17M3KZBDN3N.png&w=64&h=64&f=webp&fit=cover&position=center)![Michiel Appelman](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW453GRDP76R82Y5R610Z788.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jim de Beer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49EWNDH8M55ZFRMPZKS9D1.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Dirk-Jan van Helmond](https://blog.cloudflare.com/author/dirkjan/), [Michiel Appelman](https://blog.cloudflare.com/author/michiel/), and [Jim de Beer](https://blog.cloudflare.com/author/jim-de-beer/)

April 25, 2023## [SLP: a new DDoS amplification vector in the wild](https://blog.cloudflare.com/slp-new-ddos-amplification-vector/)

Researchers have recently published the discovery of a new DDoS reflection/amplification attack vector leveraging the SLP protocol. Cloudflare expects the prevalence of SLP-based DDoS attacks to rise in the coming weeks

![Alex Forster](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462TBPQQQGVSNE4R1Q55M1.png&w=64&h=64&f=webp&fit=cover&position=center)![Omer Yoachimik](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485W0MZ0R9VGWD75RQN9ZH.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Forster](https://blog.cloudflare.com/author/alex-forster/) and [Omer Yoachimik](https://blog.cloudflare.com/author/omer/)

April 20, 2023## [Oxy: Fish/Bumblebee/Splicer subsystems to improve reliability](https://blog.cloudflare.com/oxy-fish-bumblebee-splicer-subsystems-to-improve-reliability/)

We split a proxy application into multiple services to improve development agility and reliability. This blog also shares some common patterns we are leveraging to design a system supporting zero-downtime restart

![Quang Luong](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44RSZ6R8Y23616JGV04DKH.png&w=64&h=64&f=webp&fit=cover&position=center)![Chris Branch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW476HG12M7N37FGCK2XQ4CM.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Quang Luong](https://blog.cloudflare.com/author/quang/) and [Chris Branch](https://blog.cloudflare.com/author/chris/)

March 8, 2023## [Accelerate building resiliency into systems with Cloudflare Workers](https://blog.cloudflare.com/accelerate-building-resiliency-into-systems-with-cloudflare-workers/)

In this blog post we’ll discuss how Cloudflare Workers enabled us to quickly improve the resiliency of a legacy system

![Revathy Ramasundaram](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47JJAAENY9TSE13H59DYJV.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Revathy Ramasundaram](https://blog.cloudflare.com/author/revathy/)

July 29, 2021## [Cloudflare and COVID-19: Project Fair Shot Update](https://blog.cloudflare.com/cloudflare-and-covid-19-project-fair-shot-update/)

Cloudflare Waiting Room helping organizations around the world to stifle COVID-19 and aid with easy rapid vaccinations.

![Brian Batraski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48JSR9F0YADHRXYDNBEMCM.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Brian Batraski](https://blog.cloudflare.com/author/brian/)

July 15, 2021## [Automatic Remediation of Kubernetes Nodes](https://blog.cloudflare.com/automatic-remediation-of-kubernetes-nodes/)

In Cloudflare’s core data centers, we are using Kubernetes to run many of the diverse services that help us control Cloudflare’s edge. We are automating some aspects of node remediation to keep the Kubernetes clusters healthy.

![Andrew DeMaria](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HHS9CKKZA31T5GQQF66R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Andrew DeMaria](https://blog.cloudflare.com/author/andrew-demaria/)

Load more
