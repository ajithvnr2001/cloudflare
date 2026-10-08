---
url: https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/
title: Custom Origin Trust Store \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:43.868469+00:00
---

# Custom Origin Trust Store · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /Origin server
  4. /Custom Origin Trust Store



# Custom Origin Trust Store

Last updated Jun 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityPost-quantum certificate authoritiesHow toLimitationsAPI commands

By default, Cloudflare's global network maintains [a list of publicly trusted certificate authorities ↗︎](https://github.com/cloudflare/cfssl_trust). This means that when using [Full (strict) encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/), Cloudflare will only trust origin server certificates issued by a CA included in this trust store.

Custom Origin Trust Store allows you to upload certificate authorities (CAs) that Cloudflare will use to authenticate connections to your origin server. Use this feature to override the default trust store with your preferred CA or CAs.

  


When a CA has been uploaded to Custom Origin Trust Store, Cloudflare will ignore all default publicly trusted CAs and exclusively use the CA or CAs that have been uploaded to authenticate the origin server.

## Availability

To get access to Custom Origin Trust Store, [Advanced Certificate Manager](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) must be enabled on the zone.

## Post-quantum certificate authorities

Custom Origin Trust Store accepts ML-DSA (FIPS 204) post-quantum certificate authorities. Refer to [Post-quantum signatures](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures) for certificate generation and upload guidance.

## How to

To manage origin trust stores in the dashboard:

  1. Go to the **Origin Server** page.

[ Go to **Origin Server** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/origin)
  2. Select the **Custom Origin Trust Store** tab.

  3. Select **Upload trust store** to add a CA certificate, or use the table to manage existing trust stores.




To manage origin trust stores using the API, refer to the API commands.

## Limitations

With [Full (strict) encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/) enabled, if your uploaded CA expires and no alternative CAs are valid within the trust store, Cloudflare will not be able to properly authenticate connections to the origin server.

## API commands

#### List Custom Origin Trust Store Details

  * API documentation: [List Custom Origin Trust Store Details](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/list/)
  * Method: `GET`
  * Endpoint: `/zones/$ZONE_ID/acm/custom_trust_store`



#### Custom Origin Trust Store Details

  * API documentation: [Custom Origin Trust Store Details](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/get/)
  * Method: `GET`
  * Endpoint: `/zones/$ZONE_ID/acm/custom_trust_store/$CUSTOM_ORIGIN_TRUST_STORE_ID`

Note

The `$CUSTOM_ORIGIN_TRUST_STORE_ID` can be found via the List command.




#### Upload Custom Origin Trust Store

  * API documentation: [Upload Custom Origin Trust Store](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/create/)
  * Method: `POST`
  * Endpoint: `/zones/$ZONE_ID/acm/custom_trust_store`



#### Delete Custom Origin Trust Store

  * API documentation: [Delete Custom Origin Trust Store](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/delete/)
  * Method: `DELETE`
  * Endpoint: `/zones/$ZONE_ID/acm/custom_trust_store/$CUSTOM_ORIGIN_TRUST_STORE_ID`

Note

The `$CUSTOM_ORIGIN_TRUST_STORE_ID` can be found via the List command.




[PreviousRollback](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/)[NextCipher suites](https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/custom-origin-trust-store.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
