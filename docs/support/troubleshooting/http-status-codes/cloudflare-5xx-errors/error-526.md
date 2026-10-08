---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/
title: Error 526 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:59.118972+00:00
---

# Error 526 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 5xx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)
  5. /Error 526



# Error 526

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 526: invalid SSL certificate Common causes Error 526 in the Zero Trust context Error 526 in the Workers context

## Error 526: invalid SSL certificate

This error indicates that Cloudflare is unable to verify the SSL certificate on your origin server, preventing a secure connection from being established.

### Common causes

This error occurs when these two conditions are true:

  * Cloudflare cannot validate the SSL certificate at your origin web server.
  * [_Full SSL (Strict)_](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/) **SSL** is set in the **Overview** tab of your Cloudflare **SSL/TLS** app.



#### Resolution

Here are some options to fix or workaround this issue:

  * For a potential quick fix, set **SSL** to _Full_ instead of _Full (strict)_ in the **Overview** tab of your Cloudflare **SSL/TLS** app for the domain.

  * Add your self-signed SSL certificate to the [Custom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/). This allows the Cloudflare edge to recognize your self-signed SSL certificate as valid.

  * Use a [Cloudflare Origin CA certificate](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/) at your origin.

  * Request your server administrator or hosting provider to review the origin web server's SSL certificates and verify that:

    * Certificate is not expired.
    * Certificate is not revoked.
    * Certificate is signed by a [Certificate Authority ↗︎](https://en.wikipedia.org/wiki/Certificate_authority) (not self-signed).
    * The requested or target domain name and hostname are in the certificate's **Common Name** or **Subject Alternative Name**.
    * The certificate chain is complete - the origin server must serve the leaf certificate along with any required intermediate CA certificates so that Cloudflare can build a trusted chain to a root CA.
    * Your origin web server accepts connections over port SSL port `443`.
    * [Temporarily pause Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/) and visit <https://www.sslshopper.com/ssl-checker.html#hostname=www.example.com>[ ↗︎](https://www.sslshopper.com/ssl-checker.html#hostname=www.example.com) (replace `www.example.com` with your hostname and domain) to verify no issues exists with the origin SSL certificate:
![Screen showing an SSL certificate with no errors.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=702,height=560,format=webp/_astro/hc-import-troubleshooting_5xx_errors_sslshopper_output.B54TP_B1.png)



### Error 526 in the Zero Trust context

When using [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/), an HTTP Error `526` might be returned in the [following cases](https://developers.cloudflare.com/cloudflare-one/traffic-policies/troubleshooting/#error-526-invalid-ssl-certificate):

  * **An untrusted certificate is presented from the origin to Gateway.** Gateway will consider a certificate is untrusted if any of these conditions are true:

    * The server certificate issuer is unknown or is not trusted by the service.
    * The server certificate is revoked and fails a CRL check.
    * There is at least one expired certificate in the certificate chain for the server certificate.
    * The common name on the certificate does not match the URL you are trying to reach.
    * The common name on the certificate contains invalid characters (such as underscores). Gateway uses [BoringSSL ↗︎](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Basic&Vendor=Google&CertificateStatus=Active&ValidationYear=0) to validate certificates. Chrome's [validation logic ↗︎](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/net/cert/x509_certificate.cc#429) allows non-RFC 1305 compliant certificates, which is why the website may load when you turn off WARP.
  * **The connection from Gateway to the origin is insecure.** Gateway does not trust origins which:

    * Only offer insecure cipher suites (such as RC4, RC4-MD5, or 3DES). You can use the [SSL Server Test tool ↗︎](https://www.ssllabs.com/ssltest/index.html) to check which ciphers are supported by the origin.
    * Do not support [FIPS-compliant ciphers](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/#cipher-suites) (if you have enabled [FIPS compliance mode](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/#fips-compliance)). In order to load the page, you can either disable FIPS mode or create a Do Not Inspect policy for this host (which has the effect of disabling FIPS compliance for this origin).
    * Redirect all HTTPS requests to HTTP.



### Error 526 in the Workers context

Workers subrequests to any hostname outside your Cloudflare zone that is not proxied by Cloudflare are always made using the **[Full (strict)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/)** SSL mode, regardless of the Workers zone configuration.

#### Resolution

  * Make sure the SSL certificate configured at the origin is valid.

  * Add your self-signed SSL certificate to the [Custom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/) and enable the [`cots_on_external_fetch` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#do-not-use-the-custom-origin-trust-store-for-external-subrequests) in your Worker's configuration. This flag enables the use of the [Custom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/) when making external (grey-clouded) subrequests from a Cloudflare Worker.




[PreviousError 525](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/)[NextError 530](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-530/)

Was this helpful?

YesNo
