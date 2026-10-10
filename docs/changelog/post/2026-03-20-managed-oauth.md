---
url: https://developers.cloudflare.com/changelog/post/2026-03-20-managed-oauth/
title: Managed OAuth for Cloudflare Access \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:42.100761+00:00
---

# Managed OAuth for Cloudflare Access · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-03-20-managed-oauth/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)March 20, 2026

## Managed OAuth for Cloudflare Access

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Access supports managed OAuth, which allows non-browser clients — such as CLIs, AI agents, SDKs, and scripts — to authenticate with Access-protected applications using a standard OAuth 2.0 authorization code flow.

Previously, non-browser clients that attempted to access a protected application received a `302` redirect to a login page they could not complete. The established workaround was `cloudflared access curl`, which required installing additional tooling.

With managed OAuth, clients instead receive a `401` response with a `WWW-Authenticate` header that points to Access's OAuth discovery endpoints ([RFC 8414 ↗︎](https://datatracker.ietf.org/doc/html/rfc8414) and [RFC 9728 ↗︎](https://datatracker.ietf.org/doc/html/rfc9728)). The client opens the end user's browser to the Access login page. The end user authenticates with their identity provider, and the client receives an OAuth access token for subsequent requests.

Access enforces the same policies as a browser login; the OAuth layer is a new transport mechanism, not a separate authentication path.

Managed OAuth can be enabled on any self-hosted Access application or [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/). It is opt-in for existing applications to avoid interfering with those that run their own OAuth servers and rely on their own `WWW-Authenticate` headers.

Note

For MCP server portals, managed OAuth is enabled by default on new portals. It remains opt-in for self-hosted applications.

To enable managed OAuth, go to **Zero Trust** > **Access controls** > **Applications** , edit the application, and turn on **Managed OAuth** under **Advanced settings**.

You can also enable it via the API by setting `oauth_configuration.enabled` to `true` on the [Access applications endpoint](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/).

![Managed OAuth settings in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2914,height=1042,format=webp/_astro/managed-oauth.BirLnBpy.png)

For setup instructions, refer to [Enable managed OAuth](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/managed-oauth/).
