---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/
title: Tunnels | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:11.653415+00:00
---

# Tunnels | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Tunnels

##### [List All Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/methods/list)

GET/accounts/{account_id}/tunnels

##### ModelsExpand Collapse 

TunnelListResponse = [CloudflareTunnel](https://developers.cloudflare.com/api/resources/$shared#\(resource\)%20%24shared%20%3E%20\(model\)%20cloudflare_tunnel%20%3E%20\(schema\)) { id, account_tag, config_src, 10 more }  or object { id, account_tag, connections, 8 more } 

A Cloudflare Tunnel that connects your origin to Cloudflare’s edge.

One of the following:

CloudflareTunnel object { id, account_tag, config_src, 10 more } 

A Cloudflare Tunnel that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

config_src: optional "local" or "cloudflare"

Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the tunnel on the Zero Trust dashboard.

One of the following:

"local"

"cloudflare"

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

Deprecatedremote_config: optional boolean

Use the config_src field instead.

If `true`, the tunnel can be configured remotely from the Zero Trust dashboard. If `false`, the tunnel must be configured locally on the origin machine.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

TunnelWARPConnectorTunnel object { id, account_tag, connections, 8 more } 

A Mesh node that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

#### TunnelsCloudflared

##### [List Cloudflare Tunnels](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list)

GET/accounts/{account_id}/cfd_tunnel

##### [Get a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}

##### [Create a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/create)

POST/accounts/{account_id}/cfd_tunnel

##### [Update a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/edit)

PATCH/accounts/{account_id}/cfd_tunnel/{tunnel_id}

##### [Delete a Cloudflare Tunnel](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/delete)

DELETE/accounts/{account_id}/cfd_tunnel/{tunnel_id}

#### TunnelsCloudflaredConfigurations

##### [Get Tunnel configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/configurations/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations

##### [Update Tunnel configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/configurations/methods/update)

PUT/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations

##### ModelsExpand Collapse 

ConfigurationGetResponse object { account_id, config, created_at, 3 more } 

Cloudflare Tunnel configuration

account_id: optional string

Identifier.

maxLength32

config: optional object { ingress, originRequest } 

The tunnel configuration and ingress rules.

ingress: optional array of object { hostname, service, originRequest, path } 

List of public hostname definitions. At least one ingress rule needs to be defined for the tunnel.

hostname: string

Public hostname for this service.

service: string

Protocol and address of destination server. Supported protocols: http://, https://, unix://, tcp://, ssh://, rdp://, unix+tls://, smb://. Alternatively can return a HTTP status code http_status:[code] e.g. ‘http_status:404’.

originRequest: optional object { access, caPool, connectTimeout, 12 more } 

Configuration parameters for the public hostname specific connection settings between cloudflared and origin server.

access: optional object { audTag, teamName, required } 

For all L7 requests to this hostname, cloudflared will validate each request’s Cf-Access-Jwt-Assertion request header.

audTag: array of string

Access applications that are allowed to reach this hostname for this Tunnel. Audience tags can be identified in the dashboard or via the List Access policies API.

teamName: string

required: optional boolean

Deny traffic that has not fulfilled Access authorization.

caPool: optional string

Path to the certificate authority (CA) for the certificate of your origin. This option should be used only if your certificate is not signed by Cloudflare.

connectTimeout: optional number

Timeout for establishing a new TCP connection to your origin server. This excludes the time taken to establish TLS, which is controlled by tlsTimeout.

disableChunkedEncoding: optional boolean

Disables chunked transfer encoding. Useful if you are running a WSGI server.

http2Origin: optional boolean

Attempt to connect to origin using HTTP2. Origin must be configured as https.

httpHostHeader: optional string

Sets the HTTP Host header on requests sent to the local service.

keepAliveConnections: optional number

Maximum number of idle keepalive connections between Tunnel and your origin. This does not restrict the total number of concurrent connections.

keepAliveTimeout: optional number

Timeout after which an idle keepalive connection can be discarded.

matchSNItoHost: optional boolean

Auto configure the Hostname on the origin server certificate.

noHappyEyeballs: optional boolean

Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local network has misconfigured one of the protocols.

noTLSVerify: optional boolean

Disables TLS verification of the certificate presented by your origin. Will allow any certificate from the origin to be accepted.

originServerName: optional string

Hostname that cloudflared should expect from your origin server certificate.

proxyType: optional string

cloudflared starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP. This configures what type of proxy will be started. Valid options are: "" for the regular proxy and “socks” for a SOCKS5 proxy.

tcpKeepAlive: optional number

The timeout after which a TCP keepalive packet is sent on a connection between Tunnel and the origin server.

tlsTimeout: optional number

Timeout for completing a TLS handshake to your origin server, if you have chosen to connect Tunnel to an HTTPS server.

path: optional string

Requests with this path route to this public hostname.

originRequest: optional object { access, caPool, connectTimeout, 12 more } 

Configuration parameters for the public hostname specific connection settings between cloudflared and origin server.

access: optional object { audTag, teamName, required } 

For all L7 requests to this hostname, cloudflared will validate each request’s Cf-Access-Jwt-Assertion request header.

audTag: array of string

Access applications that are allowed to reach this hostname for this Tunnel. Audience tags can be identified in the dashboard or via the List Access policies API.

teamName: string

required: optional boolean

Deny traffic that has not fulfilled Access authorization.

caPool: optional string

Path to the certificate authority (CA) for the certificate of your origin. This option should be used only if your certificate is not signed by Cloudflare.

connectTimeout: optional number

Timeout for establishing a new TCP connection to your origin server. This excludes the time taken to establish TLS, which is controlled by tlsTimeout.

disableChunkedEncoding: optional boolean

Disables chunked transfer encoding. Useful if you are running a WSGI server.

http2Origin: optional boolean

Attempt to connect to origin using HTTP2. Origin must be configured as https.

httpHostHeader: optional string

Sets the HTTP Host header on requests sent to the local service.

keepAliveConnections: optional number

Maximum number of idle keepalive connections between Tunnel and your origin. This does not restrict the total number of concurrent connections.

keepAliveTimeout: optional number

Timeout after which an idle keepalive connection can be discarded.

matchSNItoHost: optional boolean

Auto configure the Hostname on the origin server certificate.

noHappyEyeballs: optional boolean

Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local network has misconfigured one of the protocols.

noTLSVerify: optional boolean

Disables TLS verification of the certificate presented by your origin. Will allow any certificate from the origin to be accepted.

originServerName: optional string

Hostname that cloudflared should expect from your origin server certificate.

proxyType: optional string

cloudflared starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP. This configures what type of proxy will be started. Valid options are: "" for the regular proxy and “socks” for a SOCKS5 proxy.

tcpKeepAlive: optional number

The timeout after which a TCP keepalive packet is sent on a connection between Tunnel and the origin server.

tlsTimeout: optional number

Timeout for completing a TLS handshake to your origin server, if you have chosen to connect Tunnel to an HTTPS server.

created_at: optional string

formatdate-time

source: optional "local" or "cloudflare"

Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the tunnel’s configuration on the Zero Trust dashboard.

One of the following:

"local"

"cloudflare"

tunnel_id: optional string

UUID of the tunnel.

formatuuid

maxLength36

version: optional number

The version of the Tunnel Configuration.

ConfigurationUpdateResponse object { account_id, config, created_at, 3 more } 

Cloudflare Tunnel configuration

account_id: optional string

Identifier.

maxLength32

config: optional object { ingress, originRequest } 

The tunnel configuration and ingress rules.

ingress: optional array of object { hostname, service, originRequest, path } 

List of public hostname definitions. At least one ingress rule needs to be defined for the tunnel.

hostname: string

Public hostname for this service.

service: string

Protocol and address of destination server. Supported protocols: http://, https://, unix://, tcp://, ssh://, rdp://, unix+tls://, smb://. Alternatively can return a HTTP status code http_status:[code] e.g. ‘http_status:404’.

originRequest: optional object { access, caPool, connectTimeout, 12 more } 

Configuration parameters for the public hostname specific connection settings between cloudflared and origin server.

access: optional object { audTag, teamName, required } 

For all L7 requests to this hostname, cloudflared will validate each request’s Cf-Access-Jwt-Assertion request header.

audTag: array of string

Access applications that are allowed to reach this hostname for this Tunnel. Audience tags can be identified in the dashboard or via the List Access policies API.

teamName: string

required: optional boolean

Deny traffic that has not fulfilled Access authorization.

caPool: optional string

Path to the certificate authority (CA) for the certificate of your origin. This option should be used only if your certificate is not signed by Cloudflare.

connectTimeout: optional number

Timeout for establishing a new TCP connection to your origin server. This excludes the time taken to establish TLS, which is controlled by tlsTimeout.

disableChunkedEncoding: optional boolean

Disables chunked transfer encoding. Useful if you are running a WSGI server.

http2Origin: optional boolean

Attempt to connect to origin using HTTP2. Origin must be configured as https.

httpHostHeader: optional string

Sets the HTTP Host header on requests sent to the local service.

keepAliveConnections: optional number

Maximum number of idle keepalive connections between Tunnel and your origin. This does not restrict the total number of concurrent connections.

keepAliveTimeout: optional number

Timeout after which an idle keepalive connection can be discarded.

matchSNItoHost: optional boolean

Auto configure the Hostname on the origin server certificate.

noHappyEyeballs: optional boolean

Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local network has misconfigured one of the protocols.

noTLSVerify: optional boolean

Disables TLS verification of the certificate presented by your origin. Will allow any certificate from the origin to be accepted.

originServerName: optional string

Hostname that cloudflared should expect from your origin server certificate.

proxyType: optional string

cloudflared starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP. This configures what type of proxy will be started. Valid options are: "" for the regular proxy and “socks” for a SOCKS5 proxy.

tcpKeepAlive: optional number

The timeout after which a TCP keepalive packet is sent on a connection between Tunnel and the origin server.

tlsTimeout: optional number

Timeout for completing a TLS handshake to your origin server, if you have chosen to connect Tunnel to an HTTPS server.

path: optional string

Requests with this path route to this public hostname.

originRequest: optional object { access, caPool, connectTimeout, 12 more } 

Configuration parameters for the public hostname specific connection settings between cloudflared and origin server.

access: optional object { audTag, teamName, required } 

For all L7 requests to this hostname, cloudflared will validate each request’s Cf-Access-Jwt-Assertion request header.

audTag: array of string

Access applications that are allowed to reach this hostname for this Tunnel. Audience tags can be identified in the dashboard or via the List Access policies API.

teamName: string

required: optional boolean

Deny traffic that has not fulfilled Access authorization.

caPool: optional string

Path to the certificate authority (CA) for the certificate of your origin. This option should be used only if your certificate is not signed by Cloudflare.

connectTimeout: optional number

Timeout for establishing a new TCP connection to your origin server. This excludes the time taken to establish TLS, which is controlled by tlsTimeout.

disableChunkedEncoding: optional boolean

Disables chunked transfer encoding. Useful if you are running a WSGI server.

http2Origin: optional boolean

Attempt to connect to origin using HTTP2. Origin must be configured as https.

httpHostHeader: optional string

Sets the HTTP Host header on requests sent to the local service.

keepAliveConnections: optional number

Maximum number of idle keepalive connections between Tunnel and your origin. This does not restrict the total number of concurrent connections.

keepAliveTimeout: optional number

Timeout after which an idle keepalive connection can be discarded.

matchSNItoHost: optional boolean

Auto configure the Hostname on the origin server certificate.

noHappyEyeballs: optional boolean

Disable the “happy eyeballs” algorithm for IPv4/IPv6 fallback if your local network has misconfigured one of the protocols.

noTLSVerify: optional boolean

Disables TLS verification of the certificate presented by your origin. Will allow any certificate from the origin to be accepted.

originServerName: optional string

Hostname that cloudflared should expect from your origin server certificate.

proxyType: optional string

cloudflared starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP. This configures what type of proxy will be started. Valid options are: "" for the regular proxy and “socks” for a SOCKS5 proxy.

tcpKeepAlive: optional number

The timeout after which a TCP keepalive packet is sent on a connection between Tunnel and the origin server.

tlsTimeout: optional number

Timeout for completing a TLS handshake to your origin server, if you have chosen to connect Tunnel to an HTTPS server.

created_at: optional string

formatdate-time

source: optional "local" or "cloudflare"

Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the tunnel’s configuration on the Zero Trust dashboard.

One of the following:

"local"

"cloudflare"

tunnel_id: optional string

UUID of the tunnel.

formatuuid

maxLength36

version: optional number

The version of the Tunnel Configuration.

#### TunnelsCloudflaredConnections

##### [List Cloudflare Tunnel connections](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections

##### [Clean up Cloudflare Tunnel connections](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/delete)

DELETE/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections

##### ModelsExpand Collapse 

Client object { id, arch, config_version, 4 more } 

A client (typically cloudflared) that maintains connections to a Cloudflare data center.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

arch: optional string

The cloudflared OS architecture used to establish this connection.

config_version: optional number

The version of the remote tunnel configuration. Used internally to sync cloudflared with the Zero Trust dashboard.

conns: optional array of object { id, client_id, client_version, 5 more } 

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

features: optional array of string

Features enabled for the Cloudflare Tunnel.

run_at: optional string

Timestamp of when the tunnel connection was started.

formatdate-time

version: optional string

The cloudflared version used to establish this connection.

ConnectionDeleteResponse = unknown

#### TunnelsCloudflaredToken

##### [Get a Cloudflare Tunnel token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/token/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/token

##### ModelsExpand Collapse 

TokenGetResponse = string

The Tunnel Token is used as a mechanism to authenticate the operation of a tunnel.

#### TunnelsCloudflaredConnectors

##### [Get Cloudflare Tunnel connector](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connectors/methods/get)

GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}

#### TunnelsCloudflaredManagement

##### [Get a Cloudflare Tunnel management token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/management/methods/create)

POST/accounts/{account_id}/cfd_tunnel/{tunnel_id}/management

##### ModelsExpand Collapse 

ManagementCreateResponse = string

The Tunnel Token is used as a mechanism to authenticate the operation of a tunnel.

#### TunnelsWARP Connector

##### [List Mesh nodes](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list)

GET/accounts/{account_id}/warp_connector

##### [Get a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}

##### [Create a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/create)

POST/accounts/{account_id}/warp_connector

##### [Update a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/edit)

PATCH/accounts/{account_id}/warp_connector/{tunnel_id}

##### [Delete a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/delete)

DELETE/accounts/{account_id}/warp_connector/{tunnel_id}

##### ModelsExpand Collapse 

WARPConnectorListResponse object { id, account_tag, connections, 8 more } 

A Mesh node that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

WARPConnectorGetResponse object { id, account_tag, connections, 8 more } 

A Mesh node that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

WARPConnectorCreateResponse object { id, account_tag, connections, 8 more } 

A Mesh node that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

WARPConnectorEditResponse object { id, account_tag, connections, 8 more } 

A Mesh node that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

WARPConnectorDeleteResponse object { id, account_tag, connections, 8 more } 

A Mesh node that connects your origin to Cloudflare’s edge.

id: optional string

UUID of the tunnel.

formatuuid

maxLength36

account_tag: optional string

Cloudflare account ID

maxLength32

Deprecatedconnections: optional array of object { id, client_id, client_version, 5 more } 

This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/{account_id}/{tunnel_type}/{tunnel_id}/connections`

The Cloudflare Tunnel connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

Deprecatedis_pending_reconnect: optional boolean

This functionality has been removed. The is_pending_reconnect field will now always report false.

Cloudflare continues to track connections for several minutes after they disconnect. This is an optimization to improve latency and reliability of reconnecting. If `true`, the connection has disconnected but is still being tracked. If `false`, the connection is actively serving traffic.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running cloudflared.

uuid: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

conns_active_at: optional string

Timestamp of when the tunnel established at least one connection to Cloudflare’s edge. If `null`, the tunnel is inactive.

formatdate-time

conns_inactive_at: optional string

Timestamp of when the tunnel became inactive (no connections to Cloudflare’s edge). If `null`, the tunnel is active.

formatdate-time

created_at: optional string

Timestamp of when the resource was created.

formatdate-time

deleted_at: optional string

Timestamp of when the resource was deleted. If `null`, the resource has not been deleted.

formatdate-time

metadata: optional unknown

Metadata associated with the tunnel.

name: optional string

A user-friendly name for a tunnel.

status: optional "inactive" or "degraded" or "healthy" or "down"

The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge).

One of the following:

"inactive"

"degraded"

"healthy"

"down"

tun_type: optional "cfd_tunnel" or "warp_connector" or "warp" or 4 more

The type of tunnel.

One of the following:

"cfd_tunnel"

"warp_connector"

"warp"

"magic"

"ip_sec"

"gre"

"cni"

#### TunnelsWARP ConnectorToken

##### [Get a Mesh node token](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/token/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/token

##### ModelsExpand Collapse 

TokenGetResponse = string

The Tunnel Token is used as a mechanism to authenticate the operation of a tunnel.

#### TunnelsWARP ConnectorConnections

##### [List Mesh node connections](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/connections

##### ModelsExpand Collapse 

ConnectionGetResponse object { id, arch, conns, 4 more } 

A Mesh node connector that maintains a connection to a Cloudflare data center.

id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

arch: optional string

The cloudflared OS architecture used to establish this connection.

conns: optional array of object { id, client_id, client_version, 3 more } 

The Mesh node connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running the Mesh node connector.

features: optional array of string

Features enabled for the Cloudflare Tunnel.

ha_status: optional "offline" or "passive" or "active"

The HA status of a Mesh node connector.

One of the following:

"offline"

"passive"

"active"

run_at: optional string

Timestamp of when the tunnel connection was started.

formatdate-time

version: optional string

The cloudflared version used to establish this connection.

#### TunnelsWARP ConnectorConnectors

##### [Get a Mesh node connector](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connectors/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/connectors/{connector_id}

##### ModelsExpand Collapse 

ConnectorGetResponse object { id, arch, conns, 4 more } 

A Mesh node connector that maintains a connection to a Cloudflare data center.

id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

arch: optional string

The cloudflared OS architecture used to establish this connection.

conns: optional array of object { id, client_id, client_version, 3 more } 

The Mesh node connections between your origin and Cloudflare’s edge.

id: optional string

UUID of the Cloudflare Tunnel connection.

formatuuid

maxLength36

client_id: optional string

UUID of the Cloudflare Tunnel connector.

formatuuid

maxLength36

client_version: optional string

The cloudflared version used to establish this connection.

colo_name: optional string

The Cloudflare data center used for this connection.

opened_at: optional string

Timestamp of when the connection was established.

formatdate-time

origin_ip: optional string

The public IP address of the host running the Mesh node connector.

features: optional array of string

Features enabled for the Cloudflare Tunnel.

ha_status: optional "offline" or "passive" or "active"

The HA status of a Mesh node connector.

One of the following:

"offline"

"passive"

"active"

run_at: optional string

Timestamp of when the tunnel connection was started.

formatdate-time

version: optional string

The cloudflared version used to establish this connection.

#### TunnelsWARP ConnectorFailover

##### [Trigger a manual failover for a Mesh node](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/failover/methods/update)

PUT/accounts/{account_id}/warp_connector/{tunnel_id}/failover

##### ModelsExpand Collapse 

FailoverUpdateResponse = unknown

#### TunnelsWARP ConnectorConfigurations

##### [Get Mesh node HA configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/configurations/methods/get)

GET/accounts/{account_id}/warp_connector/{tunnel_id}/configurations

##### [Update Mesh node HA configuration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/configurations/methods/update)

PUT/accounts/{account_id}/warp_connector/{tunnel_id}/configurations

##### ModelsExpand Collapse 

ConfigurationGetResponse object { configuration_version, created_at, ha_mode, 3 more } 

configuration_version: number

Monotonically increasing configuration version, incremented on each PUT.

created_at: string

Timestamp of when the resource was created.

formatdate-time

ha_mode: "none" or "disabled" or "aws" or "local"

High-availability mode for the Mesh node. `none` means HA is enabled but no provider is configured yet (newly created nodes default to this). `disabled` means HA is explicitly turned off. `aws` uses AWS ENI move for failover. `local` uses virtual IPs (VIPs) on the local interface.

One of the following:

"none"

"disabled"

"aws"

"local"

tunnel_id: string

UUID of the tunnel.

formatuuid

maxLength36

config: optional object { fnr_id }  or object { vips, vips_previous } 

Provider-specific configuration. Present for `aws` and `local` modes.

One of the following:

TunnelMeshAwsConfig object { fnr_id } 

fnr_id: string

Floating Network Resource ID — the secondary ENI that is moved between nodes on failover.

TunnelMeshLocalConfig object { vips, vips_previous } 

vips: array of object { address } 

VIPs to assign on the CloudflareWARP interface.

address: string

Virtual IP address (IPv4 or IPv6).

vips_previous: optional array of object { address } 

VIPs to clean up on demotion or version drift.

address: string

Virtual IP address (IPv4 or IPv6).

updated_at: optional string

Timestamp of the last update. Null if never updated.

formatdate-time

ConfigurationUpdateResponse object { configuration_version, created_at, ha_mode, 3 more } 

configuration_version: number

Monotonically increasing configuration version, incremented on each PUT.

created_at: string

Timestamp of when the resource was created.

formatdate-time

ha_mode: "none" or "disabled" or "aws" or "local"

High-availability mode for the Mesh node. `none` means HA is enabled but no provider is configured yet (newly created nodes default to this). `disabled` means HA is explicitly turned off. `aws` uses AWS ENI move for failover. `local` uses virtual IPs (VIPs) on the local interface.

One of the following:

"none"

"disabled"

"aws"

"local"

tunnel_id: string

UUID of the tunnel.

formatuuid

maxLength36

config: optional object { fnr_id }  or object { vips, vips_previous } 

Provider-specific configuration. Present for `aws` and `local` modes.

One of the following:

TunnelMeshAwsConfig object { fnr_id } 

fnr_id: string

Floating Network Resource ID — the secondary ENI that is moved between nodes on failover.

TunnelMeshLocalConfig object { vips, vips_previous } 

vips: array of object { address } 

VIPs to assign on the CloudflareWARP interface.

address: string

Virtual IP address (IPv4 or IPv6).

vips_previous: optional array of object { address } 

VIPs to clean up on demotion or version drift.

address: string

Virtual IP address (IPv4 or IPv6).

updated_at: optional string

Timestamp of the last update. Null if never updated.

formatdate-time

[ Previous

* * *

ISPs ](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/devices/subresources/isps)[ Next

* * *

Cloudflared ](https://developers.cloudflare.com/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared)
