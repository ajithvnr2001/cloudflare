---
url: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/
title: Roll back per-hostname AOP \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:43.911380+00:00
---

# Roll back per-hostname AOP · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server[Authenticated Origin Pulls (mTLS)](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/)

  4. /Setup
  5. /Rollback



# Roll back per-hostname AOP

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

If you need to disable or remove your [per-hostname](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/) Authenticated Origin Pulls configuration, follow these steps.

Note

[Global AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/), [zone-level AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/), and [per-hostname AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/) are three independent configurations. Enabling or disabling one does not affect the others.

  1. Use a [`PUT` request](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/) to disable Authenticated Origin Pulls on the hostname.

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
    						"enabled": false,
    						"cert_id": "<CERT_ID>",
    						"hostname": "<YOUR_HOSTNAME>"
    				}
    		]
    	}'

  2. (Optional) Use a [`GET` request](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list/) to obtain a list of the client certificate IDs. You will need the ID of the certificate you want to remove for the following step.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `SSL and Certificates Write`
     * `SSL and Certificates Read`
List Certificatesbash
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames/certificates" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

  3. Use the [Delete hostname client certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/) endpoint to remove the certificate you had uploaded.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `SSL and Certificates Write`
Delete Hostname Client Certificatebash
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames/certificates/$CERTIFICATE_ID" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"




[PreviousManage certificates](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/manage-certificates/)[NextCustom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
