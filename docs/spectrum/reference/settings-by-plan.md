---
url: https://developers.cloudflare.com/spectrum/reference/settings-by-plan/
title: Settings by plan \u00b7 Cloudflare Spectrum docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:34.595476+00:00
---

# Settings by plan · Cloudflare Spectrum docs

> Source: https://developers.cloudflare.com/spectrum/reference/settings-by-plan/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Spectrum](https://developers.cloudflare.com/spectrum/)
  3. /Reference
  4. /Settings by plan



# Settings by plan

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/spectrum/reference/settings-by-plan/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Certain fields in Spectrum request and response bodies require an Enterprise plan. To upgrade your plan, contact your account team.

Spectrum properties requiring an Enterprise plan:

Name | Type | Description | Example  
---|---|---|---  
`origin_dns` | object | Method and parameters used to discover the origin server address via DNS. Valid record types are `A`, `AAAA`, `SRV` and empty (both `A` and `AAA`).  
A request must contain either an `origin_dns` parameter or an `origin_direct` parameter. When both are specified the service returns an `HTTP 400 Bad Request`. | `origin_dns: {type: A, name: mqtt.example.com, ttl: 1200}`  
`origin_port` | integer | The destination port at the origin. | `22`  
`proxy_protocol` | string | Enables Proxy Protocol to the origin. Spectrum supports `v1`, `v2`, and `simple` proxy protocols. Refer to [Proxy Protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/) for more details. | `off`  
`ip_firewall` | boolean | Enables IP Access rules for this application. | `true`  
`tls` | string | Type of TLS termination for the application. Options are `off` (default, also known as Passthrough), `flexible`, `full`, and `strict`. Refer to [Configuration Options](https://developers.cloudflare.com/spectrum/reference/configuration-options/) for descriptions of each. | `full`  
`argo_smart_routing` | boolean | Enables Argo Smart Routing for the application. Note that it is only available for TCP applications with traffic_type set to `direct`. | `true`  
  
Review the [Spectrum API documentation](https://developers.cloudflare.com/api/resources/spectrum/subresources/apps/methods/list/) for example API requests.

[PreviousLimitations](https://developers.cloudflare.com/spectrum/reference/limitations/)[NextSimple Proxy Protocol Header](https://developers.cloudflare.com/spectrum/reference/simple-proxy-protocol-header/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/spectrum/reference/settings-by-plan.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
