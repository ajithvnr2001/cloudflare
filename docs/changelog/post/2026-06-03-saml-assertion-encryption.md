---
url: https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/
title: SAML assertion encryption for identity providers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:37.322565+00:00
---

# SAML assertion encryption for identity providers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-06-03-saml-assertion-encryption/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)June 3, 2026

## SAML assertion encryption for identity providers

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access now supports SAML assertion encryption for identity provider integrations. When turned on, your identity provider encrypts SAML assertions using a Cloudflare-managed certificate before sending them through the user's browser. Only Access can decrypt these assertions, protecting sensitive identity data even after TLS termination.

Without encryption, SAML assertions are transmitted in plaintext and could be visible to browser extensions or client-side malware.

![SAML encryption toggle in the identity provider configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1698,height=344,format=webp/_astro/saml-encryption.J5jmiYv8.png)

SAML encryption includes built-in certificate lifecycle management:

  * **Automatic certificate generation** : Access generates an encryption certificate when you turn on SAML encryption for an identity provider.
  * **Certificate rotation** : Rotate certificates without downtime. The previous certificate remains valid until expiration, giving you time to update your IdP.
  * **PEM export** : Copy the certificate in PEM format for manual upload to your IdP, or point your IdP to the SAML metadata endpoint for automatic retrieval.



To get started, refer to [Encrypt SAML assertions](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#encrypt-saml-assertions).
