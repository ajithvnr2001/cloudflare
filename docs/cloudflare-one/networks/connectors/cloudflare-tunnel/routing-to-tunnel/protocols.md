---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/
title: Protocols for published applications \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:19.800524+00:00
---

# Protocols for published applications · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

  4. /[Published applications](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/)
  5. /Protocols



# Protocols for published applications

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When you [add a published application route](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2a-publish-an-application) to a Cloudflare Tunnel, you are instructing Cloudflare to proxy requests for your public hostname to a service running privately behind `cloudflared`.

The table below lists the service types you can route to a public hostname. Non-HTTP services require [installing `cloudflared` on the client](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/) for end users to connect.

Service type | Description | Example `service` value  
---|---|---  
HTTP | Proxies incoming HTTPS requests to your local web service over HTTP. | `http://localhost:8000`  
HTTPS | Proxies incoming HTTPS requests directly to your local web service. You can [disable TLS verification](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#notlsverify) for self-signed certificates. | `https://localhost:8000`  
UNIX | Same as HTTP, but uses a Unix socket. | `unix:/home/production/echo.sock`  
UNIX + TLS | Same as HTTPS, but uses a Unix socket. | `unix+tls:/home/production/echo.sock`  
TCP | Streams TCP over a WebSocket connection. End users run `cloudflared access tcp` to [connect](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/). For long-lived connections, use [Client-to-Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/) instead. | `tcp://localhost:2222`  
SSH | Streams SSH over a WebSocket connection. End users run `cloudflared access ssh` to [connect](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/). For long-lived connections, use [Client-to-Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/) instead. | `ssh://localhost:22`  
RDP | Streams RDP over a WebSocket connection. For more information, refer to [Connect to RDP with client-side cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/). | `rdp://localhost:3389`  
SMB | Streams SMB over a WebSocket connection. For more information, refer to [Connect to SMB with client-side cloudflared](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/#connect-to-smb-server-with-cloudflared-access). | `smb://localhost:445`  
HTTP_STATUS | Responds to all requests with a fixed HTTP status code. | `http_status:404`  
BASTION | Allows `cloudflared` to act as a jump host, providing access to any local address. | `bastion`  
HELLO_WORLD | Test server for validating your Cloudflare Tunnel connection (for [locally managed tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/#file-structure-for-published-applications) only). | `hello_world`  
  
## IPv6 service addresses

When the service value is an IPv6 literal, wrap the address in square brackets as defined by [RFC 3986 ↗︎](https://datatracker.ietf.org/doc/html/rfc3986#section-3.2.2). The brackets are required so that the `:` characters in the address are not confused with the port separator.

Service type | Example `service` value  
---|---  
HTTP | `http://[2001:db8::1]:8000`  
HTTPS | `https://[2001:db8::1]:443`  
TCP | `tcp://[2001:db8::1]:2222`  
SSH | `ssh://[2001:db8::1]:22`  
RDP | `rdp://[2001:db8::1]:3389`  
  
Hostnames and IPv4 addresses do not need brackets — `http://localhost:8000` and `http://192.0.2.1:8000` are valid as-is.

[PreviousPublic load balancers](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/protocols.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
