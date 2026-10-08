---
url: https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/
title: Hyperdrive now supports custom TLS/SSL certificates for MySQL \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:41.679818+00:00
---

# Hyperdrive now supports custom TLS/SSL certificates for MySQL · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 19, 2026

## Hyperdrive now supports custom TLS/SSL certificates for MySQL

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now supports custom TLS/SSL certificates for MySQL databases, bringing the same certificate options previously available for PostgreSQL to MySQL connections.

You can now configure:

  * **Server certificate verification** with `VERIFY_CA` or `VERIFY_IDENTITY` SSL modes to verify that your MySQL database server's certificate is signed by the expected certificate authority (CA).
  * **Client certificates** (mTLS) for Hyperdrive to authenticate itself to your MySQL database with credentials beyond username and password.



Create a Hyperdrive configuration with custom certificates for MySQL:
    
    
    # Upload a CA certificate
    npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name
    
    # Create a Hyperdrive with VERIFY_IDENTITY mode
    npx wrangler hyperdrive create your-hyperdrive-config \
      --connection-string="mysql://user:password@hostname:port/database" \
      --ca-certificate-id <CA_CERT_ID> \
      --sslmode VERIFY_IDENTITY

For more information, refer to [SSL/TLS certificates for Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/) and [MySQL TLS/SSL modes](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/).
