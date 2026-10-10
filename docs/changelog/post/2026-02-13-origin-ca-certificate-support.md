---
url: https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/
title: Origin CA certificate support for Workers VPC \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:43.782180+00:00
---

# Origin CA certificate support for Workers VPC · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-02-13-origin-ca-certificate-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)February 13, 2026

## Origin CA certificate support for Workers VPC

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers VPC now supports [Cloudflare Origin CA certificates](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/) when connecting to your private services over HTTPS. Previously, Workers VPC only trusted certificates issued by publicly trusted certificate authorities (for example, Let's Encrypt, DigiCert).

With this change, you can use free Cloudflare Origin CA certificates on your origin servers within private networks and connect to them from Workers VPC using the `https` scheme. This is useful for encrypting traffic between the tunnel and your service without needing to provision certificates from a public CA.

For more information, refer to [Supported TLS certificates](https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/#supported-tls-certificates).
