---
url: https://developers.cloudflare.com/ssl/client-certificates/byo-ca/
title: Bring your own CA for mTLS \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:36.663406+00:00
---

# Bring your own CA for mTLS · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/client-certificates/byo-ca/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Client certificates (mTLS)](https://developers.cloudflare.com/ssl/client-certificates/)
  4. /Bring your own CA (BYOCA)



# Bring your own CA for mTLS

Last updated Sep 8, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityWhen to use BYOCACA certificate requirementsSet up mTLS with your CA Multiple CAs for one hostnameDelete an uploaded CAList CA hostname associations

This page explains how you can manage client certificates that have not been issued by Cloudflare CA. For a broader overview, refer to the [mTLS at Cloudflare learning path](https://developers.cloudflare.com/learning-paths/mtls/concepts/).

Bring your own CA (BYOCA) is especially useful if you already have mTLS implemented and [client certificates are already installed](https://developers.cloudflare.com/ssl/client-certificates/#how-it-works) on devices.

## Availability

  * This feature is only available on Enterprise accounts.
  * Each Enterprise account can upload up to five CAs. This quota does not apply to CAs uploaded through [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/).
  * The CA certificate quota is shared across [API Shield](https://developers.cloudflare.com/api-shield/security/mtls/configure/), [Workers mTLS](https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls/), and [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).
  * To increase this quota, contact your account team.



Note

If you exceed the CA certificate quota, the API returns error `1489` with the message "Hit maximum CA cert allocation." Contact your account team to request a quota increase.

Cloudflare Access uses a separate quota

CAs uploaded through [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/) use a separate quota that is not counted against the five-CA limit. If you see error `12130` ("maximum number of certificates has been reached") in Access, this relates to the Access certificate quota, not the BYOCA CA quota.

## When to use BYOCA

BYOCA works well if:

  * You already have an internal CA and client certificates are installed on your devices.
  * You issue certificates at high volume or high churn — for example, one certificate per ephemeral virtual machine, container, or device. With BYOCA, Cloudflare stores only your CA certificate, not individual issued certificates, so there is no per-certificate quota.
  * You want full control over certificate validity periods, key types, and revocation through your own CA tooling.



If you only have a small, stable set of devices or services to authenticate, the [Cloudflare-managed CA](https://developers.cloudflare.com/ssl/client-certificates/create-a-client-certificate/) is simpler to set up.

## CA certificate requirements

When you upload your CA, Cloudflare validates the certificate according to certain requirements.

  * The CA certificate can be from a publicly trusted CA or self-signed.

  * In the certificate `Basic Constraints`, the attribute `CA` must be set to `TRUE`.

  * The certificate must use one of the signature algorithms listed below:

Allowed signature algorithms

`x509.SHA1WithRSA`

`x509.SHA256WithRSA`

`x509.SHA384WithRSA`

`x509.SHA512WithRSA`

`x509.ECDSAWithSHA1`

`x509.ECDSAWithSHA256`

`x509.ECDSAWithSHA384`

`x509.ECDSAWithSHA512`




Note

Uploading the CA private key is only required if you wish to use [Zero Trust's block page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/). To upload your own CA with the private key, use the [Upload mTLS certificate](https://developers.cloudflare.com/api/resources/mtls_certificates/methods/create/) endpoint.

## Set up mTLS with your CA

  1. In the Cloudflare dashboard, go to the **Client Certificates** page.

[ Go to **Client Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates)
  2. Select **Add Certificate**.

  3. In the **Certificate Authority** dropdown, select **Bring your own CA**.

  4. Upload your CA certificate file (PEM encoded) and enter a name for the CA.

  5. Select **Continue**.

  6. On the **Associate Hostnames** page, enter the hostname that should use this CA for mTLS validation and select **Add** for each one. You can also skip this step and associate hostnames later.

  7. Select **Save** to confirm.




  1. Use the [Upload mTLS certificate endpoint](https://developers.cloudflare.com/api/resources/mtls_certificates/methods/create/) to upload the CA root certificate.


  * `ca` boolean required

    * Set to `true` to indicate that the certificate is a CA certificate.
  * `certificates` string required

    * Insert content from the `.pem` file associated with the CA certificate, formatted as a single string with `\n` replacing the line breaks.
  * `name` string optional

    * Indicate a unique name for your CA certificate.
  * `private_key` string optional

    * Insert content from the `.pem` file associated with the private key for the certificate, formatted as a single string with `\n` replacing the line breaks.


  2. Take note of the certificate ID (`id`) that is returned in the API response.
  3. Use the [Replace Hostname Associations endpoint](https://developers.cloudflare.com/api/resources/certificate_authorities/subresources/hostname_associations/methods/update/) to enable mTLS in each hostname that should use the CA for mTLS validation. Use the following parameters:


  * `hostnames` array required

    * List the hostnames that will be using the CA for client certificate validation.

Caution

Submitting an empty array will remove all hostname associations.

  * `mtls_certificate_id` string required

    * Indicate the certificate ID obtained from the previous step.

Caution

If no `mtls_certificate_id` is provided, the action will be performed against the [Cloudflare-managed CA](https://developers.cloudflare.com/ssl/client-certificates/).



  4. (Optional) Make a GET request to confirm the CA hostname associations.



After uploading the CA and associating hostnames, create a custom rule to enforce client certificate validation. You can do this [via the dashboard](https://developers.cloudflare.com/learning-paths/mtls/mtls-app-security/#3-validate-the-client-certificate-in-the-waf) or [via API](https://developers.cloudflare.com/waf/custom-rules/create-api/).
    
    
      "expression": "(http.host in {\"<HOSTNAME_1>\" \"<HOSTNAME_2>\"} and not cf.tls_client_auth.cert_verified)",
      "action": "block"

Note

When using [CNAME records](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#cname), enforce mTLS on the specific hostname where it should be checked. It is not enough to have it set on the CNAME target.

### Multiple CAs for one hostname

There can be multiple CAs (Cloudflare-managed or BYOCA) associated with the same hostname. For BYOCA certificates, the most recently deployed certificate will be prioritized.

If you wish to remove the association from the Cloudflare-managed certificate and only use your BYOCA certificate(s):

  1. In the Cloudflare dashboard, go to the **Client Certificates** page.

[ Go to **Client Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates)
  2. On the **Hosts** section under **Cloudflare-issued Client Certificates** , select **Edit**.

  3. Select the cross next to the hostname you want to remove.

  4. Select **Save** to confirm.




  1. [List the hostname associations](https://developers.cloudflare.com/api/resources/certificate_authorities/subresources/hostname_associations/methods/get/) **without** the `mtls_certificate_id` parameter.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`
  * `SSL and Certificates Read`

List Hostname Associationsbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/certificate_authorities/hostname_associations" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

  2. Copy the `hostnames` array returned by the API and update it, removing the hostname that should no longer use the Cloudflare-managed CA.
  3. Use the [Replace Hostname Associations endpoint](https://developers.cloudflare.com/api/resources/certificate_authorities/subresources/hostname_associations/methods/update/) **without** the `mtls_certificate_id` parameter to perform the action against the Cloudflare-managed CA. For `hostnames` use the list from the previous step.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`

Replace Hostname Associationsbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/certificate_authorities/hostname_associations" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"hostnames": [
    				"<UPDATED_HOSTNAME_ASSOCIATIONS>"
    		]
    	}'

## Delete an uploaded CA

If you want to remove a CA that you have previously uploaded, you must first remove any hostname associations that it has.

  1. In the Cloudflare dashboard, go to the **Client Certificates** page.

[ Go to **Client Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates)
  2. Select the **BYOCA** tab.

  3. Find the CA you want to delete and select the three dots next to it.

  4. Remove all associated hostnames first, if any exist.

  5. Select the delete option and confirm.




  1. Make a request to the [Replace Hostname Associations endpoint](https://developers.cloudflare.com/api/resources/certificate_authorities/subresources/hostname_associations/methods/update/), with an empty array for `hostnames` and specifying your CA certificate ID in `mtls_certificate_id`:


    
    
      "hostnames": [],
      "mtls_certificate_id": "<CERTIFICATE_ID>"

  2. Use the [Delete mTLS certificate endpoint](https://developers.cloudflare.com/api/resources/mtls_certificates/methods/delete/) to delete the certificate.



## List CA hostname associations

  1. In the Cloudflare dashboard, go to the **Client Certificates** page.

[ Go to **Client Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates)
  2. Select the **BYOCA** tab.

  3. Find the CA you want to inspect and select the three dots next to it.

  4. Select **Edit hostnames**. The **Certificate Details** panel displays the associated hostnames.




Use the [List Hostname Associations endpoint](https://developers.cloudflare.com/api/resources/certificate_authorities/subresources/hostname_associations/methods/get/) with the `mtls_certificate_id` query parameter set to the certificate ID of the uploaded CA.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`
  * `SSL and Certificates Read`

List Hostname Associationsbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/certificate_authorities/hostname_associations?mtls_certificate_id=ID_FROM_STEP_2" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

[PreviousEnable mTLS](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/)[NextForward certificate to server](https://developers.cloudflare.com/ssl/client-certificates/forward-a-client-certificate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/client-certificates/byo-ca.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
