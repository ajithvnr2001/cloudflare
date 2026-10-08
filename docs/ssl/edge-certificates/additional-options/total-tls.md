---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/
title: Total TLS \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:38.998458+00:00
---

# Total TLS · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /Additional options
  5. /Total TLS



# Total TLS

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReferenceAvailabilityLimitations Hostnames used with other Cloudflare products Deleting certificates

Total TLS allows Cloudflare to issue individual certificates for your proxied hostnames. These certificates will protect proxied hostnames not covered by [Universal certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/).

Caution

Total TLS certificates follow the Common Name (CN) restriction of 64 characters ([RFC 5280 ↗︎](https://www.rfc-editor.org/rfc/rfc5280.html)). If you have a hostname that exceeds this length, you can create an [Advanced Certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate) via API to cover it.

When issued, these certificates will have a type of **Advanced - Total TLS** , and their default validity period is 90 days.

## Reference

  * [Enable](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/)
  * [Error messages](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/)



## Availability

Total TLS is available for domains that have purchased [Advanced Certificate Manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) and are currently using a [full DNS setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/).

## Limitations

### Hostnames used with other Cloudflare products

Total TLS does not issue certificates for any hostnames used with:

  * [Cloudflare Load Balancing](https://developers.cloudflare.com/load-balancing/)
  * [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/)
  * [Cloudflare Spectrum](https://developers.cloudflare.com/spectrum/)



You can use other types of certificates or manually [order advanced certificates](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate) for these hostnames.

### Deleting certificates

Once you [enable Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/), be careful deleting any Total TLS certificates associated with proxied hostnames.

If you do, our system assumes you want to opt that hostname out of Total TLS certificate and will not order new certificates for the hostname in the future. This behavior applies even if you delete and re-create the hostname's DNS record.

[PreviousAutomatic HTTPS Rewrites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/)[NextEnable](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/total-tls/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
