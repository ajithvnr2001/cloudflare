---
url: https://blog.cloudflare.com/tag/database/
title: Posts tagged \"Database\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:45.274535+00:00
---

# Posts tagged "Database" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/database/

TAG

# Database

[Subscribe to Database RSS feed](https://blog.cloudflare.com/tag/database/rss)

July 8, 2026## [Introducing Meerkat: an experiment in global consensus](https://blog.cloudflare.com/meerkat-introduction/)

Cloudflare Research is building a global consensus service called Meerkat that uses a new consensus algorithm called QuePaxa. We plan to use Meerkat to build a strongly consistent, fault-tolerant key-value store, and other applications.

![James Larisch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44C9J5HQA4MAD7AN1K285E.jpg&w=64&h=64&f=webp&fit=cover&position=center)![ Bob Halley](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KXJFYHRZYTBR06JDENDTQ12N.jpg&w=64&h=64&f=webp&fit=cover&position=center)![João Pedro Leite](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KWW2Q3HR5NWBDTW5N6DCXWKT.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Larisch](https://blog.cloudflare.com/author/james-larisch/), [ Bob Halley](https://blog.cloudflare.com/author/bob-halley/), and [João Pedro Leite](https://blog.cloudflare.com/author/joao-pedro-leite/)

May 14, 2026## [Our billing pipeline was suddenly slow. The culprit was a hidden bottleneck in ClickHouse](https://blog.cloudflare.com/clickhouse-query-plan-contention/)

When a partitioning change to our petabyte-scale ClickHouse cluster caused critical billing jobs to stall, standard metrics showed no obvious errors. This post explores how we identified severe lock contention in ClickHouse's query planner and built upstream patches to fix it.

![James Morrison](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47DJ4SH6R0522V96RWBCS5.webp&w=64&h=64&f=webp&fit=cover&position=center)![Christian Endres](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW446RYCN9GFDAVP4BR4X64Q.webp&w=64&h=64&f=webp&fit=cover&position=center)

[James Morrison](https://blog.cloudflare.com/author/james-morrison/) and [Christian Endres](https://blog.cloudflare.com/author/christian-endres/)

April 16, 2026## [Deploy Postgres and MySQL databases with PlanetScale + Workers](https://blog.cloudflare.com/deploy-planetscale-postgres-with-workers/)

Learn how to deploy PlanetScale Postgres and MySQL databases via Cloudflare and connect Cloudflare Workers.

![Vy Ton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GN8Z682JZ0XNFK5QN096.png&w=64&h=64&f=webp&fit=cover&position=center)![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Vy Ton](https://blog.cloudflare.com/author/vy/) and [Matt Silverlock](https://blog.cloudflare.com/author/silverlock/)

September 25, 2025## [Partnering to make full-stack fast: deploy PlanetScale databases directly from Workers](https://blog.cloudflare.com/planetscale-postgres-workers/)

We’ve teamed up with PlanetScale to make shipping full-stack applications on Cloudflare Workers even easier. 

![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Thomas Gauvin](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45J4TRGWP46SWRWBD5YV1M.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Adrian Gracia](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW448TPSR7G90N0WMA91C2F6.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Silverlock](https://blog.cloudflare.com/author/silverlock/), [Thomas Gauvin](https://blog.cloudflare.com/author/thomas-gauvin/), and [Adrian Gracia](https://blog.cloudflare.com/author/adrian-gracia/)

October 29, 2024## [Migrating billions of records: moving our active DNS database while it’s in use](https://blog.cloudflare.com/migrating-billions-of-records-moving-our-active-dns-database-while-in-use/)

DNS records have moved to a new database, bringing improved performance and reliability to all customers.

![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)![Corey Horton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455RXC9SP67GW0ZACX19AQ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Fattouche](https://blog.cloudflare.com/author/alex-fattouche/) and [Corey Horton](https://blog.cloudflare.com/author/corey-horton/)

September 23, 2024## [Making zone management more efficient with batch DNS record updates](https://blog.cloudflare.com/batched-dns-changes/)

In response to customer demand, we now support the ability to DELETE, PATCH, PUT and POST multiple DNS records in a single API call, enabling more efficient and reliable zone management. 

![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Fattouche](https://blog.cloudflare.com/author/alex-fattouche/)

April 1, 2024## [Building D1: a Global Database](https://blog.cloudflare.com/building-d1-a-global-database/)

D1, Cloudflare’s SQL database, is now generally available. 

![Vy Ton](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46GN8Z682JZ0XNFK5QN096.png&w=64&h=64&f=webp&fit=cover&position=center)![Justin Mazzola Paluska](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW462TBPQQQGVSNE4R1Q55M1.png&w=64&h=64&f=webp&fit=cover&position=center)

[Vy Ton](https://blog.cloudflare.com/author/vy/) and [Justin Mazzola Paluska](https://blog.cloudflare.com/author/justin-mazzola-paluska/)

September 28, 2023## [Hyperdrive: making databases feel like they’re global](https://blog.cloudflare.com/hyperdrive-making-regional-databases-feel-distributed/)

Hyperdrive makes accessing your existing databases from Cloudflare Workers, wherever they are running, hyper fast

![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Alex Robinson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW479T0YHMKPZQQ2VAYMDQ3A.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Silverlock](https://blog.cloudflare.com/author/silverlock/) and [Alex Robinson](https://blog.cloudflare.com/author/alex-robinson/)

September 28, 2023## [D1: open beta is here](https://blog.cloudflare.com/d1-open-beta-is-here/)

D1 is now in open beta, and the theme is “scale”: with higher per-database storage limits and the ability to create more databases, we’re unlocking the ability for developers to build production-scale applications on D1

![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Ben Yule](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45RD76B1QPXZWG6AJH8HCK.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Silverlock](https://blog.cloudflare.com/author/silverlock/) and [Ben Yule](https://blog.cloudflare.com/author/ben-yule/)

September 27, 2023## [Workers AI: serverless GPU-powered inference on Cloudflare’s global network](https://blog.cloudflare.com/workers-ai/)

We are excited to launch Workers AI - an AI inference as a service platform, empowering developers to run AI models with just a few lines of code, all powered by our global network of GPUs

![Phil Wittig](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW455BX0J00059NX1R4GGRT1.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Rita Kozlov](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4775C0A7PYM3T9XKH4PH9J.png&w=64&h=64&f=webp&fit=cover&position=center)![Rebecca Weekly](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45AYPG914A9FCQ67Z934D2.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Celso Martinho](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45K1GG0634XMEFX9CSSGM2.png&w=64&h=64&f=webp&fit=cover&position=center)![Meaghan Choi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44WS4W5MTE5MKQFAMKMVPY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Phil Wittig](https://blog.cloudflare.com/author/phil/), [Rita Kozlov](https://blog.cloudflare.com/author/rita/), [Rebecca Weekly](https://blog.cloudflare.com/author/rebecca-weekly/), [Celso Martinho](https://blog.cloudflare.com/author/celso/), and [Meaghan Choi](https://blog.cloudflare.com/author/meaghan-choi/)

September 27, 2023## [Vectorize: a vector database for shipping AI-powered applications to production, fast](https://blog.cloudflare.com/vectorize-vector-database-open-beta/)

Vectorize is our brand-new vector database offering, designed to let you build full-stack, AI-powered applications entirely on Cloudflare’s global network: and you can start building with it right away

![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Jérôme Schneider](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47478FBJFPA57ZWACE3FDC.png&w=64&h=64&f=webp&fit=cover&position=center)

[Matt Silverlock](https://blog.cloudflare.com/author/silverlock/) and [Jérôme Schneider](https://blog.cloudflare.com/author/jerome/)

August 2, 2023## [Cloudflare Workers database integration with Upstash](https://blog.cloudflare.com/cloudflare-workers-database-integration-with-upstash/)

Announcing the new Upstash database integrations for Workers. Now it is easier to use Upstash Redis, Kafka and QStash inside your Worker 

![Joaquin Gimenez](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW498FW7X971WCRQ8NS7JVRK.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Shaun Persad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48T5RABET27D3130C97GS3.png&w=64&h=64&f=webp&fit=cover&position=center)

[Joaquin Gimenez](https://blog.cloudflare.com/author/joaquingimenez1/) and [Shaun Persad](https://blog.cloudflare.com/author/shaun/)

May 16, 2023## [Announcing database integrations: a few clicks to connect to Neon, PlanetScale and Supabase on Workers](https://blog.cloudflare.com/announcing-database-integrations/)

Today we’re announcing Database Integrations – making it seamless to connect to your database of choice on Workers. 

![Shaun Persad](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48T5RABET27D3130C97GS3.png&w=64&h=64&f=webp&fit=cover&position=center)![Emily Chen](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46EFMZ1ZZ502KJW9AN3QSY.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Shaun Persad](https://blog.cloudflare.com/author/shaun/), [Emily Chen](https://blog.cloudflare.com/author/emily-chen/), and [Tanushree Sharma](https://blog.cloudflare.com/author/tanushree/)

May 16, 2023## [Smart Placement speeds up applications by moving code close to your backend — no config needed](https://blog.cloudflare.com/announcing-workers-smart-placement/)

Smart Placement automatically places your workloads in an optimal location that minimizes latency and speeds up your applications!

![Michael Hart](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44Y5FGZZS90ZJA5EFQW15Q.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Serena Shah-Simpson](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45E4TK6GHZXWH66VF37ZEZ.PNG&w=64&h=64&f=webp&fit=cover&position=center)![Tanushree Sharma](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46NT9GBM742JJW1W4G7ND8.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Michael Hart](https://blog.cloudflare.com/author/michael-hart/), [Serena Shah-Simpson](https://blog.cloudflare.com/author/serena/), and [Tanushree Sharma](https://blog.cloudflare.com/author/tanushree/)

May 16, 2023## [Announcing connect() — a new API for creating TCP sockets from Cloudflare Workers](https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/)

Today, we are excited to announce a new API in Cloudflare Workers for creating outbound TCP sockets, making it possible to connect directly to databases and any TCP-based service from Workers

![Brendan Irvine-Broque](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49H9641F9RZN2BA8BPX7HK.JPG&w=64&h=64&f=webp&fit=cover&position=center)![Matt Silverlock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW492M11VMJ0WCWAND287DEN.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Brendan Irvine-Broque](https://blog.cloudflare.com/author/brendan-irvine-broque/) and [Matt Silverlock](https://blog.cloudflare.com/author/silverlock/)

November 16, 2022## [UPDATE Supercloud SET status = 'open alpha' WHERE product = 'D1';](https://blog.cloudflare.com/d1-open-alpha/)

As we continue down the road to making D1 production ready, it wouldn’t be “the Cloudflare way” unless we stopped for feedback first. D1 is now in Open Alpha!

![Nevi Shah](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3YB9DTTT6JXZABS5PH7NZQV.01M3YB9FY7HP0VT0NC74Y1H4PV.png&w=64&h=64&f=webp&fit=cover&position=center)![Glen Maddern](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48VHZGFE5SHCB4QANQRSFZ.jpg&w=64&h=64&f=webp&fit=cover&position=center)![Sven Sauleau](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46HRDMNZR42T04V7Y1R5XY.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nevi Shah](https://blog.cloudflare.com/author/nevi/), [Glen Maddern](https://blog.cloudflare.com/author/glen/), and [Sven Sauleau](https://blog.cloudflare.com/author/sven/)

September 27, 2022## [D1: our quest to simplify databases](https://blog.cloudflare.com/whats-new-with-d1/)

Get an inside look on the D1 experience today, what the team is currently working on and what’s coming up! 

![Nevi Shah](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3YB9DTTT6JXZABS5PH7NZQV.01M3YB9FY7HP0VT0NC74Y1H4PV.png&w=64&h=64&f=webp&fit=cover&position=center)![Glen Maddern](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48VHZGFE5SHCB4QANQRSFZ.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Nevi Shah](https://blog.cloudflare.com/author/nevi/) and [Glen Maddern](https://blog.cloudflare.com/author/glen/)
