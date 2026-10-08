---
url: https://developers.cloudflare.com/api-shield/security/mtls/configure/
title: Configure mTLS \u00b7 Cloudflare API Shield docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:19.602341+00:00
---

# Configure mTLS · Cloudflare API Shield docs

> Source: https://developers.cloudflare.com/api-shield/security/mtls/configure/

  1. [Home](https://developers.cloudflare.com/)
  2. /[API Shield](https://developers.cloudflare.com/api-shield/)
  3. /…

[Security](https://developers.cloudflare.com/api-shield/security/)

  4. /[Mutual TLS (mTLS)](https://developers.cloudflare.com/api-shield/security/mtls/)
  5. /Configure mTLS



# Configure mTLS

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/api-shield/security/mtls/configure/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCreate an mTLS rule via the Cloudflare dashboard Expression Builder Check for revoked certificates

When you configure [mTLS authentication](https://developers.cloudflare.com/api-shield/security/mtls/) for API hosts, Cloudflare can block requests that do not have a [client certificate](https://developers.cloudflare.com/ssl/client-certificates/) for mTLS authentication. Blocking applies only to requests that match the hostname and path conditions in your mTLS rule.

## Prerequisites

Before you can protect your API or web application with mTLS rules, you need to:

  * Check that the certificate installed on your origin server matches the hostname of the client certificate, for example `api.example.com`. Origin server wildcard certificates such as `*.example.com` are not supported.
  * [Create a client certificate](https://developers.cloudflare.com/ssl/client-certificates/create-a-client-certificate/).
  * [Configure your mobile app or IoT device](https://developers.cloudflare.com/ssl/client-certificates/configure-your-mobile-app-or-iot-device/) to use your Cloudflare-issued client certificate.
  * [Enable mutual Transport Layer Security (mTLS) for a host](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/) in your zone.



Note

While API Shield is not required to use mTLS, many teams may use mTLS to protect their APIs.

Caution

By default, API Shield mTLS uses client certificates issued by a Cloudflare-managed CA. If you need to use certificates issued by another CA, refer to [Bring your own CA for mTLS](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/).

## Create an mTLS rule via the Cloudflare dashboard

  1. In the Cloudflare dashboard, go to **Client Certificates** page.

[ Go to **Client Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates)
  2. Select **Create a mTLS rule**.

  3. In **Custom rules** , several rule parameters have already been filled in. Enter the URI path you want to protect in **Value**.

  4. (Optional) Add a `Hostname` field and enter the mTLS-enabled hostnames you wish to protect in **Value**.

  5. In **Choose action** , select `Block`.

  6. Select **Deploy** to make the rule active.




Once you have deployed your mTLS rule, requests without a [valid client certificate](https://developers.cloudflare.com/ssl/client-certificates/) are blocked only when they match the hostname and URI path conditions configured in the rule.

### Expression Builder

To review your mTLS rule in the Expression Builder, select the **wrench icon** associated with your rule.

In the **Expression Preview** , your mTLS rule includes a [compound expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/#compound-expressions) formed from two [simple expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/#simple-expressions) joined by the `and` operator.

The first expression — `not cf.tls_client_auth.cert_verified` — returns `true` when a request to access your API or web application does not present a valid client certificate.

The second expression uses the `http.request.uri.path` field, combined with the `in` operator, to capture the URI paths your mTLS rule applies to.

Because the [action](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/) for your rule is _Block_ , requests that match the configured hostname and path conditions must present a valid client certificate.

Cloudflare recommends also validating the issuer Subject Key Identifier (SKI) hash. Without this check, any valid client certificate is accepted regardless of which certificate authority (CA) issued it. Adding the SKI hash restricts access to certificates from a specific CA.

You can implement this by using an expression similar to the following:
    
    
    not (cf.tls_client_auth.cert_verified and cf.tls_client_auth.cert_issuer_ski eq "A5AC554235DBA6D963B9CDE0185CFAD6E3F55E9F")

To obtain the issuer Subject Key Identifier (SKI) hash of a client certificate stored in the `mtls.crt` file, you can run the following OpenSSL command:
    
    
    openssl x509 -noout -ext authorityKeyIdentifier -in mtls.crt | tail -n1 | tr -d ': '
    
    
    A5AC554235DBA6D963B9CDE0185CFAD6E3F55E9F

### Check for revoked certificates

To check for [revoked client certificates](https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/), you can either add a new mTLS rule or add a new expression to the default rule. To check for revoked certificates, you must use the Expression Builder.

When a request includes a revoked certificate, the `cf.tls_client_auth.cert_revoked` field is set to `true`. If you combined this with the default mTLS rule, it would look similar to the following:
    
    
    ((not cf.tls_client_auth.cert_verified or cf.tls_client_auth.cert_revoked) and http.request.uri.path in {"/admin"})

Caution

This check only applies to client certificates issued by the Cloudflare-managed CA. Cloudflare currently does not check certificate revocation lists (CRL) for [CAs that have been uploaded](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/).

[PreviousOverview](https://developers.cloudflare.com/api-shield/security/mtls/)[NextBring your own CA ↗︎](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/api-shield/security/mtls/configure.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
