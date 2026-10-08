---
url: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/mtls/
title: Mutual TLS (mTLS) \u00b7 Cloudflare Learning Paths
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:42.868219+00:00
---

# Mutual TLS (mTLS) · Cloudflare Learning Paths

> Source: https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/mtls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Learning Paths](https://developers.cloudflare.com/learning-paths/)
  3. /…

Application Security

  4. /[Default traffic security](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/)
  5. /Mutual TLS (mTLS)



# Mutual TLS (mTLS)

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/mtls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreating a mTLS rule

Mutual TLS (mTLS) authentication uses client certificates to ensure traffic between client and server is bidirectionally secure and trusted. mTLS also allows requests that do not authenticate via an identity provider — such as Internet-of-things (IoT) devices — to demonstrate they can reach a given resource.

![mTLS sequence diagram](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=900,height=1256,format=webp/_astro/api-shield-call-sequence.DjXyNgan.png)

Support includes [gRPC ↗︎](https://grpc.io/docs/what-is-grpc/introduction/)-based APIs, which use binary formats such as protocol buffers rather than JSON.

## Creating a mTLS rule

  1. In the Cloudflare dashboard, go to **Client Certificates** page.

[ Go to **Client Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/client-certificates)
  2. Select **Create a mTLS rule**.

  3. In **Custom rules** , several rule parameters have already been filled in. Enter the URI path you want to protect in **Value**.

  4. (Optional) Add a `Hostname` field and enter the mTLS-enabled hostnames you wish to protect in **Value**.

  5. In **Choose action** , select `Block`.

  6. Select **Deploy** to make the rule active.




Once you have deployed your mTLS rule, requests without a [valid client certificate](https://developers.cloudflare.com/ssl/client-certificates/) are blocked only when they match the hostname and URI path conditions configured in the rule.

[PreviousSSL / TLS](https://developers.cloudflare.com/learning-paths/application-security/default-traffic-security/ssl/)[NextOverview](https://developers.cloudflare.com/learning-paths/application-security/firewall/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/learning-paths/application-security/default-traffic-security/mtls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
