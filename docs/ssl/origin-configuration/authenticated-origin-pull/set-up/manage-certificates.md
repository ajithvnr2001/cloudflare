---
url: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/manage-certificates/
title: Manage AOP certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:43.485362+00:00
---

# Manage AOP certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/manage-certificates/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server[Authenticated Origin Pulls (mTLS)](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/)

  4. /Setup
  5. /Manage certificates



# Manage certificates

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/manage-certificates/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExpired certificatesUse specialized certificatesReplace a certificate without downtime via API Per-hostname Zone-level

Refer to the following sections to learn how to manage certificates used with [zone-level](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/) and [per-hostname](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/) Authenticated Origin Pulls. [Global AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/) uses a Cloudflare-provided certificate and does not require certificate management.

* * *

## Expired certificates

Cloudflare does not delete client certificates upon expiration unless you send a delete request to the Cloudflare API for the relevant certificate ([Delete a zone-level certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/delete/) or [Delete a hostname-level certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/)). If your origin only accepts a valid client certificate, it will drop requests when the certificate expires.

Make sure you have [notifications](https://developers.cloudflare.com/notifications/notification-available/#ssltls) set up to get alerts 30 days and 14 days before an AOP certificate expires.

* * *

## Use specialized certificates

To apply different client certificates simultaneously at the zone and hostname level, you can combine zone-level and per-hostname custom certificates.

First, set up [zone-level AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/) using your certificate. Then, upload specialized certificates for [individual hostnames](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/). Per-hostname certificates take precedence over zone-level certificates for the specified hostname.

* * *

## Replace a certificate without downtime via API

No automatic removal

Cloudflare does not delete client certificates upon expiration unless you send a delete request to the Cloudflare API for the relevant certificate ([Delete a zone-level certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/delete/) or [Delete a hostname-level certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/)).

### Per-hostname

  1. [Upload the new certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/create/).
  2. [List your certificates](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list/) and note the ID for the certificate you uploaded.
  3. [Enable Authenticated Origin Pulls for the specific hostname](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/), using the ID obtained in step 2 to specify the certificate you want to use:



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`

Enable or Disable a Hostname for Client Authenticationbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"config": [
    				{
    						"enabled": true,
    						"hostname": "<HOSTNAME>",
    						"cert_id": "<CERT_ID>"
    				}
    		]
    	}'

Note

If you keep both certificates, the API will state `active` for both but the most recently deployed certificate will be the one enabled and used.

### Zone-level

  1. [Upload the new certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/create/).
  2. [Check whether new certificate is Active](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/get/).
  3. Once certificate is active, [delete the previous certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/delete/).



Note

If you keep both certificates, the API will state `active` for both but the most recently deployed certificate will be the one enabled and used.

[PreviousPer-hostname](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/)[NextRollback](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/authenticated-origin-pull/set-up/manage-certificates.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
