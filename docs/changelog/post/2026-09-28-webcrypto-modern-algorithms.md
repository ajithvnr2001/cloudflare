---
url: https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/
title: Web Crypto adds ML-KEM and ML-DSA support \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:30.255632+00:00
---

# Web Crypto adds ML-KEM and ML-DSA support · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-28-webcrypto-modern-algorithms/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 1, 2026

## Web Crypto adds ML-KEM and ML-DSA support

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The Workers Web Crypto API now supports ML-KEM-768, ML-KEM-1024, ML-DSA-44, ML-DSA-65, and ML-DSA-87. ML-KEM establishes shared secrets, while ML-DSA signs and verifies data.

The opt-in API also adds key encapsulation and decapsulation methods, `getPublicKey()`, `SubtleCrypto.supports()`, and JSON Web Keys (JWKs) with the `AKP` key type.

Turn on the `webcrypto_modern_algorithms` compatibility flag to use these features:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "compatibility_flags": [
        "webcrypto_modern_algorithms"
      ]
    }
    
    
    compatibility_flags = ["webcrypto_modern_algorithms"]

This example uses ML-KEM-768 to establish the same shared secret on both sides:

src/index.jsjs
    
    
    const keyPair = await crypto.subtle.generateKey("ML-KEM-768", false, [
    	"encapsulateBits",
    	"decapsulateBits",
    ]);
    
    if (!("publicKey" in keyPair)) {
    	throw new Error("Expected an ML-KEM key pair");
    }
    
    const { sharedKey, ciphertext } = await crypto.subtle.encapsulateBits(
    	"ML-KEM-768",
    	keyPair.publicKey,
    );
    
    const recoveredSharedKey = await crypto.subtle.decapsulateBits(
    	"ML-KEM-768",
    	keyPair.privateKey,
    	ciphertext,
    );

src/index.tsts
    
    
    const keyPair = await crypto.subtle.generateKey("ML-KEM-768", false, [
    	"encapsulateBits",
    	"decapsulateBits",
    ]);
    
    if (!("publicKey" in keyPair)) {
    	throw new Error("Expected an ML-KEM key pair");
    }
    
    const { sharedKey, ciphertext } = await crypto.subtle.encapsulateBits(
    	"ML-KEM-768",
    	keyPair.publicKey,
    );
    
    const recoveredSharedKey = await crypto.subtle.decapsulateBits(
    	"ML-KEM-768",
    	keyPair.privateKey,
    	ciphertext,
    );

Workers implements a subset of the evolving [Modern Algorithms in the Web Cryptography API ↗︎](https://wicg.github.io/webcrypto-modern-algos/) draft. ML-KEM-512 and the draft's other algorithms are not supported. The API may change as the draft evolves.

For current algorithm and operation support, refer to [Web Crypto supported algorithms](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/#supported-algorithms).
