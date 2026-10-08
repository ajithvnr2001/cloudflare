---
url: https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/
title: Hyperdrive now supports custom TLS/SSL certificates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:06:09.285277+00:00
---

# Hyperdrive now supports custom TLS/SSL certificates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)April 9, 2025

## Hyperdrive now supports custom TLS/SSL certificates

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now supports more SSL/TLS security options for your database connections:

  * Configure Hyperdrive to verify server certificates with `verify-ca` or `verify-full` SSL modes and protect against man-in-the-middle attacks
  * Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password



Use the new `wrangler cert` commands to create certificate authority (CA) certificate bundles or client certificate pairs:
    
    
    # Create CA certificate bundle
    npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name
    
    # Create client certificate pair
    npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name

Then create a Hyperdrive configuration with the certificates and desired SSL mode:
    
    
    npx wrangler hyperdrive create your-hyperdrive-config \
      --connection-string="postgres://user:password@hostname:port/database" \
      --ca-certificate-id <CA_CERT_ID> \
      --mtls-certificate-id <CLIENT_CERT_ID>
      --sslmode verify-full

Learn more about [configuring SSL/TLS certificates for Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/) to enhance your database security posture.
