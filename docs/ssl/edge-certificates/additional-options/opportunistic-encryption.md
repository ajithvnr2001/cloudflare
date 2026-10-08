---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/opportunistic-encryption/
title: Opportunistic Encryption \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:38.733011+00:00
---

# Opportunistic Encryption · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/opportunistic-encryption/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /Additional options
  5. /Opportunistic Encryption



# Opportunistic Encryption

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/opportunistic-encryption/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityEnable Opportunistic Encryption

Opportunistic Encryption allows browsers to access HTTP URIs over an encrypted TLS channel. It's not a substitute for HTTPS, but provides additional security for otherwise vulnerable requests.

Use HTTPS when both strong encryption and authentication are required. HTTP Opportunistic Encryption provides a means of enabling TLS when needed for other protocols such as HTTP/2. It does not provide the same indications of security as HTTPS (the green lock icon in most browser address bars).

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## Enable Opportunistic Encryption

You do not need to configure your origin web server to support Opportunistic Encryption. All it requires is updating your settings in the Cloudflare dashboard.

To enable Opportunistic Encryption in the dashboard:

  1. In the Cloudflare dashboard, go to the **Edge Certificates** page.

[ Go to **Edge Certificates** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates)
  2. For **Opportunistic Encryption** , switch the toggle to **On**.




To adjust your Opportunistic Encryption settings with the API, send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `opportunistic_encryption` as the setting name in the URI path, and specify the `value` parameter with your desired setting (`"on"` or `"off"`).

Note

To use this feature on specific hostnames - instead of across your entire zone - use a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/).

[PreviousAlways Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/)[NextOverview](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/opportunistic-encryption.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
