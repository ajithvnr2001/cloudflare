---
url: https://blog.cloudflare.com/tag/hardware/
title: Posts tagged \"Hardware\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:09.497440+00:00
---

# Posts tagged "Hardware" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/hardware/

TAG

# Hardware

[Subscribe to Hardware RSS feed](https://blog.cloudflare.com/tag/hardware/rss)

March 23, 2026## [Inside Gen 13: how we built our most powerful server yet](https://blog.cloudflare.com/gen13-config/)

Cloudflare's Gen 13 servers introduce AMD EPYC™ Turin 9965 processors and a transition to 100 GbE networking to meet growing traffic demands. In this technical deep dive, we explain the engineering rationale behind each major component selection.

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Ma Xiong](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SJ3NTWPAG4GT7D5C6D7W.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Victor Hwang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46G24ZH6T4DQPBFY5FRAM7.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/author/syona/), [JQ Lau](https://blog.cloudflare.com/author/jq/), [Ma Xiong](https://blog.cloudflare.com/author/ma-xiong/), and [Victor Hwang](https://blog.cloudflare.com/author/victor-hwang/)

March 23, 2026## [Launching Cloudflare’s Gen 13 servers: trading cache for cores for 2x edge compute performance](https://blog.cloudflare.com/gen13-launch/)

Cloudflare’s Gen 13 servers double our compute throughput by rethinking the balance between cache and cores. Moving to high-core-count AMD EPYC ™ Turin CPUs, we traded large L3 cache for raw compute density. By running our new Rust-based FL2 stack, we completely mitigated the latency penalty to unlock twice the performance.

![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jesse Brandeburg](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4807Z4GQMH91EPHZ1WRAGR.png&w=64&h=64&f=webp&fit=cover&position=center)

[Syona Sarma](https://blog.cloudflare.com/author/syona/), [JQ Lau](https://blog.cloudflare.com/author/jq/), and [Jesse Brandeburg](https://blog.cloudflare.com/author/jesse-brandeburg/)

October 15, 2024## [Analysis of the EPYC 145% performance gain in Cloudflare Gen 12 servers](https://blog.cloudflare.com/analysis-of-the-epyc-145-performance-gain-in-cloudflare-gen-12-servers/)

Cloudflare’s Gen 12 server is the most powerful and power efficient server that we have deployed to date. Through sensitivity analysis, we found that Cloudflare workloads continue to scale with higher core count and higher CPU frequency, as well as achieving a significant boost in performance with larger L3 cache per core.

![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[JQ Lau](https://blog.cloudflare.com/author/jq/) and [Syona Sarma](https://blog.cloudflare.com/author/syona/)

October 7, 2024## [Thermal design supporting Gen 12 hardware: cool, efficient and reliable](https://blog.cloudflare.com/thermal-design-supporting-gen-12-hardware-cool-efficient-and-reliable/)

Great thermal solutions play a crucial role in hardware reliability and performance. Gen 12 servers have implemented an exhaustive thermal analysis to ensure optimal operations within a wide variety of temperature conditions and use cases. By implementing new design and control features for improved power efficiency on the compute nodes we also enabled the support of powerful accelerators to serve our customers.

![Leslye Paniagua](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45TG2FX67PV20XND5Q4SW2.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Leslye Paniagua](https://blog.cloudflare.com/author/leslye-paniagua/)

September 25, 2024## [Cloudflare’s 12th Generation servers — 145% more performant and 63% more efficient](https://blog.cloudflare.com/gen-12-servers/)

Cloudflare is thrilled to announce the general deployment of our next generation of server — Gen 12 powered by AMD Genoa-X processors. This new generation of server focuses on delivering exceptional performance across all Cloudflare services, enhanced support for AI/ML workloads, significant strides in power efficiency, and improved security features.

![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Ma Xiong](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44SJ3NTWPAG4GT7D5C6D7W.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[JQ Lau](https://blog.cloudflare.com/author/jq/), [Ma Xiong](https://blog.cloudflare.com/author/ma-xiong/), and [Syona Sarma](https://blog.cloudflare.com/author/syona/)

July 16, 2024## [Eliminating hardware with Load Balancing and Cloudflare One](https://blog.cloudflare.com/eliminating-hardware-with-load-balancing-and-cloudflare-one/)

Cloudflare is adding support for end-to-end private traffic flows to our local traffic management (LTM) load balancing solution, and allowing for the replacement of hardware load balancers

![Noah Crouch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45WVKKSSZYB0EH40T2R50C.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Noah Crouch](https://blog.cloudflare.com/author/noah-crouch/)

March 25, 2024## [Autonomous hardware diagnostics and recovery at scale](https://blog.cloudflare.com/autonomous-hardware-diagnostics-and-recovery-at-scale/)

Operating hardware in 310 cities in 120 countries means that hardware can break anywhere and anytime. Detecting and managing server failure at scale requires automation. Here's how we automated

![Jet Mariscal](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48JRWXCNJ5Y07TMTMPN5AJ.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Aakash Shah](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45HEVG2R0507VRSAZE8M74.png&w=64&h=64&f=webp&fit=cover&position=center)![Yilin Xiong](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49KGSFJ1EPE5KZBAR81CZD.png&w=64&h=64&f=webp&fit=cover&position=center)

[Jet Mariscal](https://blog.cloudflare.com/author/jet/), [Aakash Shah](https://blog.cloudflare.com/author/aakash/), and [Yilin Xiong](https://blog.cloudflare.com/author/yilin/)

March 19, 2024## [Redefining fleet management at Cloudflare](https://blog.cloudflare.com/redefining-fleet-management-at-cloudflare/)

Growing pains were inevitable given the sheer pace of Cloudflare’s growth. Processes around server provisioning, maintenance windows, repairs, and diagnostics reporting were reaching their limits

![Ryan De Lap](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW484HVX8JEDRMPNPZ2D90DJ.png&w=64&h=64&f=webp&fit=cover&position=center)![Donald Gary](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW447FYE305F2P5J48DQ26N0.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Dwayn Matthies](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48EDEMMAJKWRB83KKWZM25.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Ryan De Lap](https://blog.cloudflare.com/author/ryan-de-lap/), [Donald Gary](https://blog.cloudflare.com/author/donald/), and [Dwayn Matthies](https://blog.cloudflare.com/author/dwayn/)

December 7, 2023## [A look inside the Cloudflare ML Ops platform](https://blog.cloudflare.com/mlops/)

To help our team continue to innovate efficiently, our MLOps effort has collaborated with Cloudflare’s data scientists to implement the following best practices

![Keith Adler](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48G40036AR876A60CY1J6X.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Rio Harapan Pangihutan](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW467X4B122V82CQAJH4CB4Q.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Keith Adler](https://blog.cloudflare.com/author/keith/) and [Rio Harapan Pangihutan](https://blog.cloudflare.com/author/harapan/)

December 1, 2023## [Cloudflare Gen 12 Server: bigger, better, cooler in a 2U1N form factor](https://blog.cloudflare.com/cloudflare-gen-12-server-bigger-better-cooler-in-a-2u1n-form-factor/)

Cloudflare Gen 12 Compute servers are moving to 2U1N form factor to optimize the thermal design to accommodate both high-power CPUs (>350W) and GPUs effectively while maintaining performance and reliability

![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Syona Sarma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4929VS8GVC5HN85HAJE4B3.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[JQ Lau](https://blog.cloudflare.com/author/jq/) and [Syona Sarma](https://blog.cloudflare.com/author/syona/)

October 16, 2023## [Introducing the Project Argus Datacenter-ready Secure Control Module design specification](https://blog.cloudflare.com/introducing-the-project-argus-datacenter-ready-secure-control-module-design-specification/)

The DC-SCM (Datacenter-ready Secure Control Module) decouples server management from the server motherboard. It provides flexibility to implement multiple server management and security solutions with the same server motherboard design

![Xiaomin Shen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45W8XCRC6QCW488H91SJVD.jpg&w=64&h=64&f=webp&fit=cover&position=center)![JQ Lau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46JB6AXE54HDQ7T54BTQ8M.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Xiaomin Shen](https://blog.cloudflare.com/author/xiaomin/) and [JQ Lau](https://blog.cloudflare.com/author/jq/)

July 25, 2023## [How Cloudflare is staying ahead of the AMD vulnerability known as “Zenbleed”](https://blog.cloudflare.com/zenbleed-vulnerability/)

The Google Information Security Team revealed a new flaw in AMD's Zen 2 processors in a blog post today. The 'Zenbleed' flaw affects the entire Zen 2 product stack, from AMD's EPYC data center processors to the Ryzen 3000 CPUs, and can be exploited to steal sensitive data processed in the CPU, 

![Derek Chamorro](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47RW1M9SFFVHH45WPZCZ20.png&w=64&h=64&f=webp&fit=cover&position=center)![Martin Schwarzl](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Q44FVCNYF3AKGF6DGP9G.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Michal Melewski](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48K2XN86GKCQ87FC0D8GAN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Derek Chamorro](https://blog.cloudflare.com/author/derek-chamorro/), [Martin Schwarzl](https://blog.cloudflare.com/author/martin/), and [Michal Melewski](https://blog.cloudflare.com/author/michal/)

April 19, 2023## [DDR4 memory organization and how it affects memory bandwidth](https://blog.cloudflare.com/ddr4-memory-organization-and-how-it-affects-memory-bandwidth/)

In this blog, we will study the concepts of memory rank and organization, and how memory rank and organization affect the memory bandwidth performance by reviewing some benchmarking test results

![Xiaomin Shen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45W8XCRC6QCW488H91SJVD.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Xiaomin Shen](https://blog.cloudflare.com/author/xiaomin/)

March 10, 2023## [Deploying firmware at Cloudflare-scale: updating thousands of servers in more than 285 cities](https://blog.cloudflare.com/deploying-firmware-at-cloudflare-scale-how-we-update-thousands-of-servers-in-more-than-285-cities/)

We have a huge number of servers of varying kinds, from varying vendors, spread over 285 cities worldwide. We need to be able to rapidly deploy various types of firmware updates to all of them, reliably, and automatically, without any kind of manual intervention.

![Chris Howells](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47VWJNGG1RA6KPNYVE83BX.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Chris Howells](https://blog.cloudflare.com/author/chris-howells/)

January 25, 2023## [Armed to Boot: an enhancement to Arm's Secure Boot chain](https://blog.cloudflare.com/armed-to-boot/)

Enhancing the Arm Secure Boot chain to improve platform security on modern systems.

![Derek Chamorro](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47RW1M9SFFVHH45WPZCZ20.png&w=64&h=64&f=webp&fit=cover&position=center)![Ryan Chow](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47FP9YD719DQJ7ZWBN55MS.png&w=64&h=64&f=webp&fit=cover&position=center)

[Derek Chamorro](https://blog.cloudflare.com/author/derek-chamorro/) and [Ryan Chow](https://blog.cloudflare.com/author/ryan-chow/)

December 14, 2022## [How we’re making Cloudflare’s infrastructure more sustainable](https://blog.cloudflare.com/extending-the-life-of-hardware/)

Our hardware sustainability initiative encapsulates using hardware components for as long as possible, recycling them responsibly when it is time to decommission them, and selecting the most power-efficient options for our workloads.

![Rebecca Weekly](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45AYPG914A9FCQ67Z934D2.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Jon Rolfe](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW475EJ6930XK25G0PZJ0EJW.png&w=64&h=64&f=webp&fit=cover&position=center)

[Rebecca Weekly](https://blog.cloudflare.com/author/rebecca-weekly/) and [Jon Rolfe](https://blog.cloudflare.com/author/jon-rolfe/)

December 14, 2022## [A more sustainable end-of-life for your legacy hardware appliances with Cloudflare and Iron Mountain](https://blog.cloudflare.com/sustainable-end-of-life-hardware/)

Today, as part of Cloudflare’s Impact Week, we’re excited to announce an opportunity for Cloudflare customers to make it easier to decommission and dispose of their used hardware appliances sustainably.

![May Ma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45EFRH8ZCNXDVY0M049EJF.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Annika Garbers](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW485D91GWFS302KY7T9FVJF.png&w=64&h=64&f=webp&fit=cover&position=center)

[May Ma](https://blog.cloudflare.com/author/may/) and [Annika Garbers](https://blog.cloudflare.com/author/annika/)

May 26, 2022## [Cloudflare’s approach to handling BMC vulnerabilities](https://blog.cloudflare.com/bmc-vuln/)

Cloudflare’s approach to handling firmware vulnerabilities and how we keep our internal data protected

![Derek Chamorro](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47RW1M9SFFVHH45WPZCZ20.png&w=64&h=64&f=webp&fit=cover&position=center)![Rebecca Weekly](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45AYPG914A9FCQ67Z934D2.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Derek Chamorro](https://blog.cloudflare.com/author/derek-chamorro/) and [Rebecca Weekly](https://blog.cloudflare.com/author/rebecca-weekly/)

Load more
