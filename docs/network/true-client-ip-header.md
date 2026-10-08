---
url: https://developers.cloudflare.com/network/true-client-ip-header/
title: Understanding the True-Client-IP Header \u00b7 Cloudflare Network settings docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:25.215055+00:00
---

# Understanding the True-Client-IP Header · Cloudflare Network settings docs

> Source: https://developers.cloudflare.com/network/true-client-ip-header/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Network](https://developers.cloudflare.com/network/)
  3. /Understanding the True-Client-IP Header



# Understanding the True-Client-IP Header

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/network/true-client-ip-header/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityAdd True-Client-IP HeaderAdditional resources

Enabling the True-Client-IP Header adds the [`True-Client-IP` header](https://developers.cloudflare.com/fundamentals/reference/http-headers/#true-client-ip-enterprise-plan-only) to all requests to your origin server, which includes the end user's IP address.

## Availability

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | No | No | No | Yes  
  
## Add True-Client-IP Header

The recommended procedure to access client IP information is to [enable the **Add "True-Client-IP" header** Managed Transform](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/#add-true-client-ip-header).

Note

To use this data, you will need to then retrieve it from the [`True-Client-IP` header](https://developers.cloudflare.com/fundamentals/reference/http-headers/#cf-ipcountry).

## Additional resources

For additional guidance on using True-Client-IP Header with Cloudflare, refer to the following resources:

  * [Available Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/reference/#add-true-client-ip-header)
  * [Cloudflare HTTP headers](https://developers.cloudflare.com/fundamentals/reference/http-headers/#true-client-ip-enterprise-plan-only)
  * [Restoring original visitor IPs](https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/)



[PreviousPseudo IPv4](https://developers.cloudflare.com/network/pseudo-ipv4/)[NextWebSockets](https://developers.cloudflare.com/network/websockets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/network/true-client-ip-header.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
