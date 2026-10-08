---
url: https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/
title: Troubleshooting client certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:37.815169+00:00
---

# Troubleshooting client certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Client certificates (mTLS)](https://developers.cloudflare.com/ssl/client-certificates/)
  4. /Troubleshooting



# Troubleshooting

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCheck SSL/TLS handshakeCheck mTLS hostsReview mTLS rulesAdvanced debuggingCertificate quota reached Cloudflare-managed CA Bring your own CA (BYOCA)BYOCA certificate upload errors Upload the CA certificate, not a leaf certificate Unsupported signature algorithm Malformed PEM content

If your query returns an error even after configuring and embedding a client SSL certificate, check the following settings.

Note

Before troubleshooting, disable VPNs and proxies. These can interfere with the mTLS handshake.

* * *

## Check SSL/TLS handshake

On your terminal, use the following command to check whether an SSL/TLS connection can be established successfully between the client and the API endpoint.
    
    
    curl --verbose --cert /path/to/certificate.pem --key /path/to/key.pem https://your-api-endpoint.com

If the SSL/TLS handshake cannot be completed, check whether the certificate and the private key are correct. If the handshake completes but requests are still blocked, confirm that Cloudflare is verifying the client certificate.

* * *

## Check mTLS hosts

Check whether [mTLS has been enabled](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/) for the correct host. The host should match the API endpoint that you want to protect.

* * *

## Review mTLS rules

To review mTLS rules, consider the steps below. For further guidance refer to [Custom rules](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/).

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. On a specific rule, select **Edit**.

  3. On that rule, check whether:

     * The Expression Preview is correct.

     * The hostname, if defined, matches your API endpoint. For example, for the API endpoint `api.trackers.ninja/time`, the rule should look like:
           
           (http.host in {"api.trackers.ninja"} and not cf.tls_client_auth.cert_verified)

  4. To edit the rule, either use the user interface or select **Edit expression**.




* * *

## Advanced debugging

You can use [Cloudflare Workers](https://developers.cloudflare.com/workers/) to debug client certificate validation failures.

  1. Create a Worker to debug print [cf.properties](https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties):
         
         export default {
           async fetch(request, env, ctx) {
             console.info({ message: JSON.stringify(request.cf, null, 2) });
             return new Response(JSON.stringify(request.cf, null, 2))
           }
         };

  2. Associate the Worker with the hostname where mTLS is enabled using a [Worker route](https://developers.cloudflare.com/workers/configuration/routing/routes/) or a [Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/).

  3. Make requests to the hostname and/or path configured, with and without sending the mTLS client certificate.

  4. View your logs on the [Observability](https://developers.cloudflare.com/workers/observability/) dashboard and compare the responses against the expected values listed below.

[ Go to **Observability** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability)


  * Valid certificate
        
        "tlsClientAuth": {
          "certPresented": "1",
          "certVerified": "SUCCESS",
        },

  * Invalid certificate (for example, self-signed certificates)
        
        "tlsClientAuth": {
          "certPresented": "1",
          "certVerified": "FAILED:self signed certificate",
        },

  * No certificate
        
        "tlsClientAuth": {
          "certPresented": "0",
          "certVerified": "NONE",
        },




* * *

## Certificate quota reached

### Cloudflare-managed CA

Cloudflare-managed client certificates count against a per-zone quota. To free up a slot, revoke certificates you no longer need. Revoking a certificate immediately releases the slot.

To list and revoke certificates, refer to the [client certificates API](https://developers.cloudflare.com/api/resources/ssl/subresources/client_certificates/).

### Bring your own CA (BYOCA)

Each Enterprise account can upload up to five CA certificates for [BYOCA](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/). This quota is shared across [API Shield](https://developers.cloudflare.com/api-shield/security/mtls/configure/), [Workers mTLS](https://developers.cloudflare.com/workers/runtime-apis/bindings/mtls/), and [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/).

If you exceed this limit, the API returns:
    
    
    {
      "code": 1489,
      "message": "Hit maximum CA cert allocation."
    }

To free a slot, you must first remove all hostname associations from the CA before deleting it. To increase your quota, contact your account team.

Note

CAs uploaded through [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/identity/devices/warp-client-checks/client-certificate/) use a separate quota. Error `12130` ("maximum number of certificates has been reached") in Access refers to the Access-specific certificate limit, not the BYOCA quota described in Bring your own CA (BYOCA).

* * *

## BYOCA certificate upload errors

When uploading a CA certificate for [Bring your own CA (BYOCA)](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/), the certificate must meet the following requirements:

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




### Upload the CA certificate, not a leaf certificate

The certificate you upload must be a CA certificate — that is, it must have `Basic Constraints: CA=TRUE` in its extensions. It is the certificate that directly issued your client certificates, not a client certificate itself.

A common cause of upload failure is uploading a leaf (client) certificate instead of the CA certificate. If your certificate chain is `Root CA → Intermediate CA → Client certificate`, upload the Intermediate CA (which has `CA:TRUE`), not the client certificate.

To confirm whether a certificate is a CA certificate, run:
    
    
    openssl x509 -in certificate.pem -noout -text | grep -A1 "Basic Constraints"

The output should include `CA:TRUE`. If it shows `CA:FALSE` or the field is absent, the certificate is not a CA certificate and cannot be uploaded.

### Unsupported signature algorithm

The CA certificate must use one of the following signature algorithms:

  * `SHA1WithRSA`, `SHA256WithRSA`, `SHA384WithRSA`, `SHA512WithRSA`
  * `ECDSAWithSHA1`, `ECDSAWithSHA256`, `ECDSAWithSHA384`, `ECDSAWithSHA512`



If the CA certificate uses a different algorithm, re-issue it using a supported one.

### Malformed PEM content

The `certificates` field in the upload request must contain valid, properly delimited PEM content. Ensure the certificate starts with `-----BEGIN CERTIFICATE-----` and ends with `-----END CERTIFICATE-----`. Do not include private keys or certificate signing requests in this field.

[PreviousClient certificate variables](https://developers.cloudflare.com/ssl/client-certificates/client-certificate-variables/)[NextmTLS for Zero Trust ↗︎](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/client-certificates/troubleshooting.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
