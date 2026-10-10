---
url: https://developers.cloudflare.com/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/
title: Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:54.813573+00:00
---

# Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-02-14-cert-bundling-for-custom-hostnames/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 14, 2025

## Upload a certificate bundle with an RSA and ECDSA certificate per custom hostname

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has supported both RSA and ECDSA certificates across our platform for a number of years. Both certificates offer the same security, but ECDSA is more performant due to a smaller key size. However, RSA is more widely adopted and ensures compatibility with legacy clients. Instead of choosing between them, you may want both – that way, ECDSA is used when clients support it, but RSA is available if not.

Now, you can upload both an RSA and ECDSA certificate on a custom hostname via the API.
    
    
    curl -X POST https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames \
        -H 'Content-Type: application/json' \
        -H "X-Auth-Email: $CLOUDFLARE_EMAIL" \
        -H "X-Auth-Key: $CLOUDFLARE_API_KEY" \
        -d '{
        "hostname": "hostname",
        "ssl": {
            "custom_cert_bundle": [
                {
                    "custom_certificate": "RSA Cert",
                    "custom_key": "RSA Key"
                },
                {
                    "custom_certificate": "ECDSA Cert",
                    "custom_key": "ECDSA Key"
                }
            ],
            "bundle_method": "force",
            "wildcard": false,
            "settings": {
                "min_tls_version": "1.0"
            }
        }
    }’

You can also:

  * [Upload](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/) an RSA or ECDSA certificate to a custom hostname with an existing ECDSA or RSA certificate, respectively.

  * [Replace](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/update/) the RSA or ECDSA certificate with a certificate of its same type.

  * [Delete](https://developers.cloudflare.com/api/resources/custom_hostnames/subresources/certificate_pack/subresources/certificates/methods/delete/) the RSA or ECDSA certificate (if the custom hostname has both an RSA and ECDSA uploaded).




This feature is available for Business and Enterprise customers who have purchased custom certificates.
