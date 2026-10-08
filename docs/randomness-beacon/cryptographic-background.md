---
url: https://developers.cloudflare.com/randomness-beacon/cryptographic-background/
title: Cryptographic Background \u00b7 Cloudflare Randomness Beacon docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:51.492437+00:00
---

# Cryptographic Background · Cloudflare Randomness Beacon docs

> Source: https://developers.cloudflare.com/randomness-beacon/cryptographic-background/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Randomness Beacon](https://developers.cloudflare.com/randomness-beacon/)
  3. /Cryptographic Background



# Cryptographic Background

Last updated Apr 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/randomness-beacon/cryptographic-background/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

drand is an efficient randomness beacon daemon that utilizes pairing-based cryptography, `𝑡-of-𝑛` distributed key generation, and threshold BLS signatures to generate publicly-verifiable, unbiasable, unpredictable, distributed randomness.

This is an overview of the cryptographic building blocks drand uses to generate publicly-verifiable, unbiasable, and unpredictable randomness in a distributed manner.

The drand beacon has two phases: a setup phase and a beacon phase. Generally, we assume that there are _n_ participants, out of which at most _f <n_ are malicious. drand relies heavily on threshold cryptography primitives, where (at minimum) a threshold of _t-f+1_ nodes work together to successfully execute cryptographic operations.

Threshold cryptography has many applications as it avoids single points of failure. One application is cryptocurrency multi-sig wallets, where _t-of-n_ participants are required to sign a transaction using a threshold signature scheme.

Note

This document is intended for a general audience. No cryptographic background knowledge is required to understand these concepts.

[PreviousFuture of drand](https://developers.cloudflare.com/randomness-beacon/about/future/)[NextSetup Phase](https://developers.cloudflare.com/randomness-beacon/cryptographic-background/setup-phase/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/randomness-beacon/cryptographic-background/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
