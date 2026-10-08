---
url: https://developers.cloudflare.com/tunnel/reference/origin-parameters/
title: Origin parameters \u00b7 Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:05.550742+00:00
---

# Origin parameters · Cloudflare Docs

> Source: https://developers.cloudflare.com/tunnel/reference/origin-parameters/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)
  3. /Reference
  4. /Origin parameters



# Origin parameters

Last updated Sep 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/tunnel/reference/origin-parameters/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUpdate origin parametersTLS settings originServerName matchSNItoHost caPool noTLSVerify tlsTimeout http2OriginHTTP settings httpHostHeader disableChunkedEncodingConnection settings connectTimeout noHappyEyeballs proxyType proxyAddress proxyPort keepAliveTimeout keepAliveConnections tcpKeepAliveAccess settings access

Origin parameters determine how `cloudflared` sends requests to the origin server of your [published application](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/).

## Update origin parameters

This section describes how to update origin parameters for a remotely-managed tunnel. If you are using a locally-managed tunnel, add these parameters to your [configuration file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/).

  1. In the Cloudflare dashboard, go to **Networking** > **Tunnels** and select your tunnel.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)
  2. Go to the **Routes** tab.

  3. Select **Edit route** from the action menu on the published application you want to configure, or select **Add route** to create a new one.

  4. Expand **Additional application settings** and modify origin parameters under the **HTTP** , **TLS** , or **Connection** categories.

  5. Select **Save changes**.




## TLS settings

### originServerName

Default | UI name  
---|---  
`""` | Origin Server Name  
  
Hostname that `cloudflared` should expect from your origin server certificate. If empty, `cloudflared` uses the hostname from the service URL, for example `localhost` if the service is `https://localhost:443`.

### matchSNItoHost

Default | UI name  
---|---  
`false` | Match SNI to host  
  
When `true`, `cloudflared` sets the Server Name Indication (SNI) during the TLS handshake to the request `Host` value sent to the origin. If you configure HTTP Host Header, `cloudflared` uses that value for SNI. This setting overrides Origin Server Name for each request.

This setting is useful when directing traffic to entry points that host multiple services and rely on SNI to route requests or present the correct certificate. It eliminates the need to explicitly configure `originServerName` for individual services when using wildcard routing.

### caPool

Default | UI name  
---|---  
`""` | CA Pool  
  
Local file path to the certificate authority (CA) for your origin server certificate (for example, `/root/certs/ca.pem`). The path should point to a certificate store file or a bundle file in `.pem` or `.crt` format that contains one or more trusted root CA certificates. `cloudflared` adds these certificates to its default trust pool. Configure this setting when a private CA signs the certificate and the CA is not in the default trust pool.

### noTLSVerify

Default | UI name  
---|---  
`false` | Disable TLS certificate verification  
  
When `false`, TLS verification is performed on the certificate presented by your origin.

When `true`, TLS verification is disabled. This will allow any certificate from the origin to be accepted.

### tlsTimeout

Default | UI name  
---|---  
`10s` | TLS Timeout  
  
Timeout for completing a TLS handshake to your origin server, if you have chosen to connect Tunnel to an HTTPS server.

### http2Origin

Default | UI name  
---|---  
`false` | Use HTTP/2 to origin  
  
When `false`, `cloudflared` will connect to your origin with HTTP/1.1.

When `true`, `cloudflared` attempts to connect to your origin server using HTTP/2 instead of HTTP/1.1. HTTP/2 to the origin requires HTTPS. For a certificate signed by a private CA, configure CA Pool and keep TLS verification enabled.

## HTTP settings

### httpHostHeader

Default | UI name  
---|---  
`""` | HTTP Host Header  
  
Sets the HTTP `Host` header on requests sent to the local service.

### disableChunkedEncoding

Default | UI name  
---|---  
`false` | Disable Chunked Encoding  
  
When `false`, `cloudflared` performs chunked transfer encoding when transferring data over HTTP/1.1.

When `true`, chunked transfer encoding is disabled. This is useful if you are running a Web Server Gateway Interface (WSGI) server.

## Connection settings

### connectTimeout

Default | UI name  
---|---  
`30s` | Connect Timeout  
  
Timeout for establishing a new TCP connection to your origin server. This excludes the time taken to establish TLS, which is controlled by tlsTimeout.

### noHappyEyeballs

Default | UI name  
---|---  
`false` | No Happy Eyeballs  
  
When `false`, `cloudflared` uses the Happy Eyeballs algorithm for IPv4/IPv6 fallback if your local network has misconfigured one of the protocols.

When `true`, Happy Eyeballs is disabled.

### proxyType

Default | UI name  
---|---  
`""` | Proxy Type  
  
`cloudflared` starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP. This configures what type of proxy will be started. Valid options are:

  * `""` for the regular proxy
  * `"socks"` for a SOCKS5 proxy. Refer to the [tutorial on connecting through Cloudflare Access using kubectl](https://developers.cloudflare.com/cloudflare-one/tutorials/kubectl/) for more information.



### proxyAddress

Note

For locally-managed tunnels only.

Default | UI name  
---|---  
`127.0.0.1` | \--  
  
`cloudflared` starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP. This configures the listen address for that proxy.

### proxyPort

Note

For locally-managed tunnels only.

Default | UI name  
---|---  
`0` | \--  
  
`cloudflared` starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP. This configures the listen port for that proxy. If set to zero, an unused port will randomly be chosen.

### keepAliveTimeout

Default | UI name  
---|---  
`1m30s` | Idle Connection Expiration Time  
  
Timeout after which an idle keepalive connection can be discarded.

### keepAliveConnections

Default | UI name  
---|---  
`100` | Keep Alive Connections  
  
Default: `100`

Maximum number of idle keepalive connections between `cloudflared` and your origin. This does not restrict the total number of concurrent connections.

### tcpKeepAlive

Default | UI name  
---|---  
`30s` | TCP Keep Alive Interval  
  
Default: `30s`

The timeout after which `cloudflared` sends a TCP keepalive packet to the origin server.

## Access settings

### access

Default | UI name  
---|---  
`""` | Protect with Access  
  
Requires `cloudflared` to validate the [Cloudflare Access JWT](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/) prior to proxying traffic to your origin. You can enforce this check on public hostname services that are protected by an Access application. For all L7 requests to these hostnames, Access will send the JWT to `cloudflared` as a `Cf-Access-Jwt-Assertion` request header.

To enable this security control in a [configuration file](https://developers.cloudflare.com/tunnel/features/locally-managed-tunnels/configuration-file/), [get the AUD tag](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#get-your-aud-tag) for your Access application and add the following rule to `originRequest`:
    
    
    access:
      required: true
      teamName: <your-team-name>
      audTag:
        - <Access-application-audience-tag>
        - <Optional-additional-tags>

[PreviousRun parameters](https://developers.cloudflare.com/tunnel/reference/run-parameters/)[NextTunnel tokens](https://developers.cloudflare.com/tunnel/reference/tunnel-tokens/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/tunnel/reference/origin-parameters.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
