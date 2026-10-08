---
url: https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/
title: New mTLS certificate fields for Transform Rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:43.244529+00:00
---

# New mTLS certificate fields for Transform Rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 25, 2026

## New mTLS certificate fields for Transform Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in [RFC 9440 ↗︎](https://www.rfc-editor.org/rfc/rfc9440) format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized `Client-Cert` and `Client-Cert-Chain` header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.

Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, `:MIIDsT...Vw==:`. A chain of intermediates is expressed as a comma-separated list of such values.

#### New fields

Field | Type | Description  
---|---|---  
`cf.tls_client_auth.cert_rfc9440` | String | The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented.  
`cf.tls_client_auth.cert_rfc9440_too_large` | Boolean | `true` if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be `false`.  
`cf.tls_client_auth.cert_chain_rfc9440` | String | The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB.  
`cf.tls_client_auth.cert_chain_rfc9440_too_large` | Boolean | `true` if the intermediate chain exceeded 16 KB and was omitted.  
  
The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.

#### Example: Forwarding client certificate headers to your origin server

Add a request header transform rule to set the `Client-Cert` and `Client-Cert-Chain` headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:

**Rule expression:**
    
    
    cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked

**Header modifications:**

Operation | Header name | Value  
---|---|---  
Set | `Client-Cert` | `cf.tls_client_auth.cert_rfc9440`  
Set | `Client-Cert-Chain` | `cf.tls_client_auth.cert_chain_rfc9440`  
  
To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates `cf.tls_client_auth.cert_verified` and `cf.tls_client_auth.cert_revoked`.

Prevent header injection

You should ensure that `Client-Cert` and `Client-Cert-Chain` headers received by your origin server can only originate from this transform rule — any client could send these headers directly.

  * **If you use WAF custom rules to block requests with invalid mTLS connections:** The transform rule is sufficient. For all requests that reach your origin server, the rule will overwrite any existing `Client-Cert` and `Client-Cert-Chain` headers.
  * **If you do not enforce mTLS at the WAF:** Add another transform rule that removes any incoming `Client-Cert` and `Client-Cert-Chain` headers from all requests (use expression `true`), ordered before the rule above. This ensures your origin server cannot receive client-supplied values for these HTTP headers.



For more information, refer to [Mutual TLS authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/), [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/), and the [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).
