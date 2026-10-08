---
url: https://developers.cloudflare.com/data-localization/geo-key-manager/
title: Geo Key Manager \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:42.110049+00:00
---

# Geo Key Manager · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/geo-key-manager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /Geo Key Manager



# Geo Key Manager

Last updated Jul 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/geo-key-manager/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCustomize key storageCloudflare data center flow example

Geo Key Manager offers enhanced control over the storage location of your private SSL/TLS keys — the cryptographic keys that Cloudflare uses to decrypt your HTTPS traffic. By restricting where these keys are stored, you can ensure compliance with regional data regulations and security requirements.

## Customize key storage

By default, your private keys are encrypted and securely distributed to each Cloudflare data center, where they are used for local TLS termination (the process of decrypting incoming HTTPS traffic). Geo Key Manager allows you to choose where you want to store your private keys.

Geo Key Manager was restricted to the US, EU, and high-security data centers, but with the new version of Geo Key Manager, available in [Closed Beta ↗︎](https://blog.cloudflare.com/configurable-and-scalable-geo-key-manager-closed-beta/), you can now create `allowlists` and `blocklists` of countries in which your private keys will be stored. That means that you will be able define specific geographic locations where to store keys, for instance you can store your private keys exclusively in Australia or limit private keys storage to the EU and the UK.

Geo Key Manager uses its own country-based storage model, separate from [Regional Services regions](https://developers.cloudflare.com/data-localization/region-support/#region-types). For the regions supported by each Data Localization Suite feature, refer to [Region support](https://developers.cloudflare.com/data-localization/region-support/).

## Cloudflare data center flow example

The following diagram shows what happens when an end user connects to a Cloudflare data center that does not hold your private key. Because TLS termination requires the private key, the local data center must request a temporary session key (a short-lived symmetric encryption key) from a data center in an authorized region. Once the session key is established, the local data center can decrypt traffic for the remainder of the connection without contacting the key-holding data center again. This extra step adds latency on the first request, which can be as much as a second if the key-holding data center is geographically distant.

  

    
    
    sequenceDiagram
        participant User as End user
        participant CloudflarePoP as Closest data center without TLS Key
        participant CloudflarePoPwTLS as Data center with TLS Key
    
        User->>CloudflarePoP: Initial request
        Note right of CloudflarePoP: Closest data center cannot decrypt
        CloudflarePoP-->>CloudflarePoPwTLS: Requests TLS Signature
        CloudflarePoPwTLS-->>CloudflarePoP: Sends TLS Signature in order to establish Session Key
        Note right of CloudflarePoP: Decrypts and performs business logic (for example, WAF, Configuration Rules, Load Balancing)
        CloudflarePoP-->>User: Subsequent requests use the Session Key
        User-->>CloudflarePoP: Subsequent requests use the Session Key
    

  


For detailed information on setup and supported options, refer to [Geo Key Manager documentation](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/).

[PreviousProduct compatibility](https://developers.cloudflare.com/data-localization/compatibility/)[NextOverview](https://developers.cloudflare.com/data-localization/metadata-boundary/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/geo-key-manager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
