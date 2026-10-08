---
url: https://developers.cloudflare.com/ssl/client-certificates/label-client-certificate/
title: Label client certificates \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:37.445020+00:00
---

# Label client certificates · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/client-certificates/label-client-certificate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /[Client certificates (mTLS)](https://developers.cloudflare.com/ssl/client-certificates/)
  4. /Label client certificates



# Label client certificates

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/client-certificates/label-client-certificate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRoot CauseSolution

After [creating client certificates](https://developers.cloudflare.com/ssl/client-certificates/) at Cloudflare, it may be hard to differentiate the generated certificates.

## Root Cause

The option to generate private key and CSR with Cloudflare is meant for simpler cases and the certificates will be generated with just "CN=Cloudflare, C=US".

## Solution

If you need to differentiate client certificates for your clients on a per-organization basis, you can generate your own private key and CSR. When you generate the private key and CSR, you can then enter information that will be incorporated into your certificate request.

For example, if you run the following command (with OpenSSL installed):
    
    
    openssl req -new -newkey rsa:2048 -nodes -keyout client1.key -out client1.csr

You can then specify:
    
    
    Country Name (2 letter code) []:
    State or Province Name (full name) []:
    Locality Name (eg, city) []:
    Organization Name (eg, company) []:
    Organizational Unit Name (eg, section) []:
    Common Name (eg, fully qualified host name) []:
    Email Address []:

Usually, adding `Country Name` and `Organization Name` is enough, but you can provide as much information as you need or want.

The additional information will be included in the **Certificate Subject** , allowing you to easily identify which certificate belongs to which client. This can also make it easier to revoke a specific certificate when needed.

The following image displays an example of how a certificate with `Country Name`, `Organization Name`, and `Organizational Unit Name` will look like on the Cloudflare dashboard:

![](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=710,height=86,format=webp/_astro/chrome_mQRJVOpkTQ.BiKeZMXO.png)

[PreviousForward certificate to server](https://developers.cloudflare.com/ssl/client-certificates/forward-a-client-certificate/)[NextRevoke a client certificate](https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/client-certificates/label-client-certificate.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
