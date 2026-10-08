---
url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/
title: Always Use HTTPS \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:37.673542+00:00
---

# Always Use HTTPS · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

[Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/)

  4. /Additional options
  5. /Always Use HTTPS



# Always Use HTTPS

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityEncrypt all visitor trafficLimitations

Always Use HTTPS redirects all your visitor requests from `http` to `https`, for all subdomains and hosts in your application.

Note

This process does not impact certificate validation. If you use [HTTP DCV](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/), you can still enable Always Use HTTPS.

Cloudflare recommends not performing redirects at your origin web server, as this can cause [redirect loop errors](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/).

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
  
## Encrypt all visitor traffic

To redirect traffic for all subdomains and hosts in your application, you can enable **Always Use HTTPS**.

Note

If only some parts of your application can support HTTPS traffic, do not enable **Always Use HTTPS** and use a [single redirect](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/) to selectively perform the redirect to HTTPS. Refer to [Redirect admin area requests to HTTPS](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/) for an example.

To enable **Always Use HTTPS** in the dashboard:

  1. In the Cloudflare dashboard, go to the **SSL/TLS Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls)
  2. Make sure that your [SSL/TLS encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/) is not set to **Off**. When you set your encryption mode to **Off** , the **Always Use HTTPS** option will not be visible in your Cloudflare dashboard.

  3. Go to the [**Edge Certificates** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates) page.

  4. Turn on **Always Use HTTPS**.




To enable or disable **Always Use HTTPS** with the API:

  1. Make sure that your [SSL/TLS encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/) **is not** set to **Off**.
  2. Send a [`PATCH`](https://developers.cloudflare.com/api/resources/zones/subresources/settings/methods/edit/) request with `always_use_https` as the setting name in the URI path, and the `value` parameter set to your desired setting (`"on"` or `"off"`).



## Limitations

Forcing HTTPS does not resolve issues with [mixed content](https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/), as browsers check the protocol of included resources before making a request. You will need to use only relative links or HTTPS links on pages that you force to HTTPS. Cloudflare can automatically resolve some mixed-content links using our [Automatic HTTPS Rewrites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/) functionality.

[PreviousError messages](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/)[NextOpportunistic Encryption](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/opportunistic-encryption/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/edge-certificates/additional-options/always-use-https.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
