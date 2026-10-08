---
url: https://developers.cloudflare.com/data-localization/compatibility/
title: Cloudflare product compatibility \u00b7 Cloudflare Data Localization Suite docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:41.815779+00:00
---

# Cloudflare product compatibility · Cloudflare Data Localization Suite docs

> Source: https://developers.cloudflare.com/data-localization/compatibility/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Data Localization Suite](https://developers.cloudflare.com/data-localization/)
  3. /Product compatibility



# Product compatibility

Last updated Jul 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/data-localization/compatibility/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewApplication PerformanceApplication SecurityDeveloper PlatformNetwork ServicesPlatformZero Trust

The Data Localization Suite (DLS) has three features, each controlling a different aspect of where your data is handled:

  * **Geo Key Manager** : Controls where your private TLS keys are stored.
  * **Regional Services** : Controls which Cloudflare data centers can decrypt and process your HTTPS traffic.
  * **Customer Metadata Boundary (CMB)** : Controls which region stores your logs and analytics data.



The tables below show whether each Cloudflare product is compatible with each DLS feature. If you see 🚧, check the footnote number for specific restrictions.

✅ Fully compatible — no restrictions   
🚧 Compatible with caveats — check the footnote for details   
✘ Not compatible — this product cannot be used with this DLS feature   
⚫️ Not applicable — this product does not interact with this DLS feature

## Application Performance

Product | Geo Key Manager | Regional Services | Customer Metadata Boundary  
---|---|---|---  
Caching/CDN | ✅ | ✅ | ✅  
Cache Reserve | ⚫️ | 🚧 | ✅ 1  
DNS | ⚫️ | 🚧 2 | ✅  
HTTP/3 (with QUIC) | ⚫️ | ✘ | ⚫️  
Image Resizing | ✅ | ✅ 3 | 🚧 4  
Load Balancing | ✅ | ✅ | 🚧 4  
Network Error Logging (NEL) | ⚫️ | ⚫️ | ✘  
Onion Routing | ✘ | ✘ | ✘  
O2O | ✘ | ✘ | ✘  
Stream Delivery | ✅ | ✅ | ✅  
Tiered Caching | ✅ | 🚧 5 | 🚧 6  
Trace | ✘ | ✘ | ✘  
Waiting Room | ⚫️ | ✅ | ✅  
Web Analytics / Real User Monitoring (RUM) | ⚫️ | ⚫️ | ✘ 7  
Zaraz | ✅ | ✅ | ✅  
  
* * *

## Application Security

Product | Geo Key Manager | Regional Services | Customer Metadata Boundary  
---|---|---|---  
Advanced Certificate Manager | ⚫️ | ⚫️ | ⚫️  
Advanced DDoS Protection | ✅ | ✅ | 🚧 89  
API Shield | ✅ | ✅ | 🚧 10  
Bot Management | ✅ | ✅ | ✅  
Client-side security (formerly Page Shield) | ✅ | ✅ | ✅  
DNS Firewall | ⚫️ | ⚫️ | ✅  
Rate Limiting | ✅ | ✅ | ✅ 11  
SSL | ✅ | ✅ | ✅  
Cloudflare for SaaS | ✘ | ✅ | ✅  
Turnstile | ⚫️ | ✘ | ✅ 12  
WAF/L7 Firewall | ✅ | ✅ | 🚧 9  
DMARC Management | ⚫️ | ⚫️ | ✅  
  
* * *

## Developer Platform

Product | Geo Key Manager | Regional Services | Customer Metadata Boundary  
---|---|---|---  
Cloudflare Images | ⚫️ | ✅ 13 | 🚧 14  
AI Gateway | ✘ | ✘ | 🚧 15  
AI Search | ✘ 16 | ✘ 17 | 🚧 18  
AI Security for Apps | ✘ | ✘ | ✘  
Cloudflare Pages | ✅ 19 | ✅ 19 | 🚧 4  
Cloudflare D1 | ⚫️ | ⚫️ | 🚧 20  
Durable Objects | ⚫️ | ✅ 21 | 🚧 4  
Email Routing | ⚫️ | ⚫️ | ✅  
Remote MCP Server | ✅ 22 | ✅ 23 | 🚧 4  
R2 | ✅ 24 | ✅ 25 | ✅ 26  
Smart Placement | ⚫️ | ✘ | ✘  
Stream | ⚫️ | ✘ | 🚧 4  
Vectorize | ⚫️ | ✘ | ✘  
Workers (deployed on a Zone) | ✅ | ✅ | 🚧 27  
Workers AI | ⚫️ | ✘ | ✅  
Workers KV | ⚫️ | ✘ | ✅ 28  
Workers.dev | ✘ | ✘ | ✘  
Workers Analytics Engine (WAE) | ⚫️ | ⚫️ | 🚧 4  
  
* * *

## Network Services

Product | Geo Key Manager | Regional Services | Customer Metadata Boundary  
---|---|---|---  
Argo Smart Routing | ✅ | ✘ 29 | ✘ 30  
Static IP/BYOIP | ⚫️ | ✅ 31 | ⚫️  
Cloudflare Network Firewall | ⚫️ | ⚫️ | ✅  
Network Flow | ⚫️ | ⚫️ | 🚧 4  
Magic Transit | ⚫️ | ⚫️ | ✅ 8  
Cloudflare WAN | ⚫️ | ⚫️ | ✅  
Spectrum | ✅ | ✅ 32 | ✅  
  
* * *

## Platform

Product | Geo Key Manager | Regional Services | Customer Metadata Boundary  
---|---|---|---  
Logpull | ⚫️ | ⚫️ | 🚧 33  
Logpush | ⚫️ | ✅ | 🚧 34  
Log Explorer | ⚫️ | ⚫️ | ✘ 35  
  
* * *

## Zero Trust

Product | Geo Key Manager | Regional Services | Customer Metadata Boundary  
---|---|---|---  
Access | 🚧 36 | 🚧 37 | ✅ 38  
Browser Isolation | ⚫️ | 🚧 39 | ✅  
CASB | ⚫️ | ⚫️ | ✘  
Cloudflare Tunnel | ⚫️ | 🚧 40 | ⚫️  
Digital Experience | ⚫️ | ⚫️ | 🚧 41  
DLP | ⚫️ 42 | ⚫️ 42 | 🚧 43  
Gateway | 🚧 44 | 🚧 45 | 🚧 46  
Cloudflare One Client | ⚫️ | ⚫️ | 🚧 4  
  
## Footnotes

  1. You cannot yet specify region location for object storage itself. ↩

  2. If you use [outgoing zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/) (where Cloudflare sends your DNS records to non-Cloudflare nameservers), those transfers will include global Cloudflare IP addresses rather than region-specific ones. This means Regional Services will not function correctly when end users receive DNS answers from non-Cloudflare nameservers. ↩

  3. Only when using a Custom Domain set to a region, either through Workers or [Transform Rules](https://developers.cloudflare.com/images/optimization/transformations/rewrite-rules/) within the same zone. ↩

  4. Logs / Analytics not available outside US region when using Customer Metadata Boundary. ↩ ↩2 ↩3 ↩4 ↩5 ↩6 ↩7 ↩8 ↩9

  5. Regular and Custom Tiered Cache (where you define the caching hierarchy) work with Regional Services. Smart Tiered Caching (where Cloudflare automatically selects intermediate cache data centers) is not available with Regional Services. ↩

  6. Regular/Generic and Custom Tiered Cache work with Customer Metadata Boundary (CMB). Smart Tiered Caching (where Cloudflare automatically selects intermediate cache data centers) does not work with CMB.   
With CMB set to EU, the Zone Dashboard **Caching** > **Tiered Cache** > **Smart Tiered Caching** option will not populate the Dashboard Analytics. ↩

  7. Web Analytics collects the [minimum amount of information](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/). Alternatively, you can [exclude EU Visitors from RUM](https://developers.cloudflare.com/speed/observatory/rum-beacon/#rum-excluding-eeaeu). ↩

  8. [Adaptive DDoS Protection](https://developers.cloudflare.com/ddos-protection/managed-rulesets/adaptive-protection/) (which automatically adjusts DDoS rules based on your traffic patterns) is only supported when Customer Metadata Boundary is set to the US. All other DDoS protection features work with any CMB region. ↩ ↩2

  9. Email and webhook notifications for DDoS and WAF events may not fire reliably when Customer Metadata Boundary is set to `eu`. This behavior is intermittent and under investigation. If timely alerts are critical, use [Logpush](https://developers.cloudflare.com/logs/logpush/) as a complementary monitoring mechanism. ↩ ↩2

  10. The following API Shield sub-features do not work when CMB is set to EU: API Discovery (automatic detection of your API endpoints), Volumetric Abuse Detection (identifying unusually high API call volumes), and [Sequence Analytics and Mitigation](https://developers.cloudflare.com/api-shield/security/sequence-analytics/) (tracking the order of API calls to detect misuse). All other API Shield features work with any CMB region. ↩

  11. Legacy Zone Analytics & Logs section not available outside US region when using CMB. Use [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/) instead. ↩

  12. [Turnstile Analytics](https://developers.cloudflare.com/turnstile/turnstile-analytics/) are available. However, there are no regionalization guarantees for the Siteverify API yet. ↩

  13. Only when using a [Custom Domain](https://developers.cloudflare.com/images/optimization/hosted-images/serve-from-custom-domains/) set to a region. ↩

  14. Logs / Analytics not supported for CMB = EU. Jurisdictional Restrictions ([storage](https://developers.cloudflare.com/images/storage/upload-images/methods/)) options are not supported today. All other features are available to all CMB regions. Note that beta or future features may not be in scope and could be subject to change. ↩

  15. Jurisdictional Restrictions (storage) options for [Logs](https://developers.cloudflare.com/ai-gateway/observability/logging/) are not supported today. All other features are available to all CMB regions. ↩

  16. Only R2 Custom Domains and Custom Certificate are supported. ↩

  17. Only R2 Custom Domains are supported. ↩

  18. The following are exceptions and are supported: AI Gateway Analytics (GraphQL Analytics datasets) and Logs (Logpush), R2 Dashboard Metrics & Analytics, Workers AI GraphQL Analytics datasets like aiInferenceAdaptive. ↩

  19. Only when using [Custom Domain](https://developers.cloudflare.com/pages/configuration/custom-domains/) set to a region. ↩ ↩2

  20. Jurisdictional Restrictions ([data location](https://developers.cloudflare.com/d1/configuration/data-location/) / storage) options are not supported today. All other features are available to all CMB regions. Note that beta or future features may not be in scope and could be subject to change. ↩

  21. [Jurisdiction restrictions for Durable Objects](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction). ↩

  22. Only when using Workers Routes & Domains and Custom Certificate. ↩

  23. Only when using Workers Routes & Domains. ↩

  24. Only when using a Custom Domain and a [Custom Certificate](https://developers.cloudflare.com/r2/reference/data-security/#encryption-in-transit) or [Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/). ↩

  25. Only when using a [Custom Domain](https://developers.cloudflare.com/r2/buckets/public-buckets/#connect-a-bucket-to-a-custom-domain) set to a region and using [jurisdictions with the S3 API](https://developers.cloudflare.com/r2/reference/data-location/#using-jurisdictions-with-the-s3-api). ↩

  26. R2 Dashboard [Metrics and Analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/) are populated. [Jurisdictional Restrictions](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions) guarantee objects in a bucket are stored within a specific jurisdiction. ↩

  27. Logs / Analytics not available outside US region when using Customer Metadata Boundary. Use Logpush instead. ↩

  28. Jurisdictional Restrictions (storage) for Workers KV pairs is not supported today. ↩

  29. Argo cannot be used with Regional Services. ↩

  30. Argo cannot be used with Customer Metadata Boundary. ↩

  31. You can use Static IP/BYOIP with Regionalized Spectrum Applications. You can also regionalize BYOIP prefixes at the IP layer with [Regionalized IP Bindings](https://developers.cloudflare.com/data-localization/regional-services/ip-bindings/). ↩

  32. Only applies to HTTP/S Spectrum applications. Spectrum applications use a separate regionalization mechanism from the Regional Hostnames API. Configuring a regional hostname does not regionalize a Spectrum application on the same hostname. Contact your [Account Team](https://developers.cloudflare.com/support/contacting-cloudflare-support/) for Spectrum-specific regionalization. ↩

  33. Logpull available when using CMB = US only. Logpull is a legacy feature, consider using [Logpush](https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/) or [Log Explorer](https://developers.cloudflare.com/log-explorer/) instead. ↩

  34. Logpush available with Customer Metadata Boundary for [these datasets](https://developers.cloudflare.com/data-localization/metadata-boundary/logpush-datasets/). Contact your account team if you need another dataset. ↩

  35. Currently, customers do not have the ability to choose the location of the Cloudflare-managed R2 bucket for Log Explorer. ↩

  36. Access App SSL keys can use Geo Key Manager. [Access JWT](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/) is not yet localized. ↩

  37. Can be localized to US FedRAMP Moderate Domestic region only. ↩

  38. Customer Metadata Boundary can be used to limit data transfer outside region, but Access User Logs will not be available outside US region. EU customers must use Logpush to retain logs. ↩

  39. Currently may only be used with US FedRAMP region. ↩

  40. The [`--region` parameter](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#region) in `cloudflared` controls where the tunnel connector establishes its connection to Cloudflare. This setting is separate from Regional Services. For public hostnames served through a tunnel, Regional Services is configured at the DNS record level and operates independently from the tunnel connector region. For incoming web requests, Regional Services only applies when you have [published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/) (services exposed to users through the tunnel). In that case, the region associated with the DNS record will apply. ↩

  41. Dashboard Analytics are empty when using CMB outside the US region. Use [Logpush](https://developers.cloudflare.com/logs/logpush/) instead. ↩

  42. Uses Gateway HTTP and CASB. ↩ ↩2

  43. DLP is part of Gateway HTTP, however, [DLP detection entries](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/) are not available outside US region when using Customer Metadata Boundary. ↩

  44. You can [bring your own certificate ↗︎](https://blog.cloudflare.com/bring-your-certificates-cloudflare-gateway/) to Gateway but these cannot yet be restricted to a specific region. ↩

  45. Gateway HTTP (web traffic filtering) supports Regional Services. Gateway DNS (domain name filtering) does not yet support regionalization.   
ICMP proxy (forwarding network diagnostic traffic like ping) and Mesh proxy are not available to Regional Services users. [File Sandboxing](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/file-sandboxing/) (an add-on that quarantines and scans suspicious files in an isolated environment) is incompatible with DLS. ↩

  46. Dashboard Analytics and Logs are empty when using CMB outside the US region. Use Logpush instead. ↩




[PreviousRegion support](https://developers.cloudflare.com/data-localization/region-support/)[NextGeo Key Manager](https://developers.cloudflare.com/data-localization/geo-key-manager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/data-localization/compatibility.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
