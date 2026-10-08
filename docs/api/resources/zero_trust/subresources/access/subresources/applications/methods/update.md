---
url: https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/
title: Update an Access application | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:27:35.680291+00:00
---

# Update an Access application | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Access](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access)

[Applications](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Update an Access application

PUT/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}

Updates an Access application.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Accepted Permissions (at least one required)

`Access: Apps and Policies Write`

##### Path ParametersExpand Collapse 

app_id: [AppID](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20app_id%20%3E%20\(schema\))

Identifier.

maxLength32

account_id: optional string

The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

zone_id: optional string

The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

##### Body ParametersJSONExpand Collapse 

body: object { oauth_configuration, type, user_populations, 5 more }  or object { domain, type, allow_authenticate_via_warp, 29 more }  or object { allowed_idps, app_launcher_visible, auto_redirect_to_identity, 8 more }  or 11 more

An end user application is a public self-hosted application backed by exactly one organization-owned user population. End user applications use a canonical allow-everyone policy and do not support custom policies, SCIM configuration, MFA configuration, or private destinations.

One of the following:

AccessEndUserProps object { oauth_configuration, type, user_populations, 5 more } 

An end user application is a public self-hosted application backed by exactly one organization-owned user population. End user applications use a canonical allow-everyone policy and do not support custom policies, SCIM configuration, MFA configuration, or private destinations.

oauth_configuration: object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional true

Managed OAuth is required for end user applications and cannot be disabled.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

user_populations: array of string

The single user population associated with this application.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

destinations: optional array of object { uri, overrides, type }  or object { type, worker_id, overrides }  or object { type, worker_id, overrides }  or 2 more

Public hostname and Workers destinations secured by Access.

One of the following:

AccessEndUserPublicDestination object { uri, overrides, type } 

uri: string

The public hostname and optional path to secure.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

AccessEndUserWorkerDestination object { type, worker_id, overrides } 

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to secure.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AccessEndUserPreviewWorkerDestination object { type, worker_id, overrides } 

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose previews to secure.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AccessEndUserAllWorkersDestination object { type, overrides } 

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AccessEndUserAllPreviewWorkersDestination object { type, overrides } 

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

name: optional string

The name of the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

SelfHostedApplication object { domain, type, allow_authenticate_via_warp, 29 more } 

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

SaaSApplication object { allowed_idps, app_launcher_visible, auto_redirect_to_identity, 8 more } 

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

saas_app: optional [SAMLSaaSApp](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20saml_saas_app%20%3E%20\(schema\)) { auth_type, consumer_service_url, custom_attributes, 8 more }  or [OIDCSaaSApp](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20oidc_saas_app%20%3E%20\(schema\)) { access_token_lifetime, allow_pkce_without_client_secret, app_launcher_url, 11 more } 

One of the following:

SAMLSaaSApp object { auth_type, consumer_service_url, custom_attributes, 8 more } 

auth_type: optional "saml" or "oidc"

Optional identifier indicating the authentication protocol used for the saas app. Required for OIDC. Default if unset is “saml”

One of the following:

"saml"

"oidc"

consumer_service_url: optional string

The service provider’s endpoint that is responsible for receiving and parsing a SAML assertion.

custom_attributes: optional array of object { friendly_name, name, name_format, 2 more } 

friendly_name: optional string

The SAML FriendlyName of the attribute.

name: optional string

The name of the attribute.

name_format: optional "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified" or "urn:oasis:names:tc:SAML:2.0:attrname-format:basic" or "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"

A globally unique name for an identity or service provider.

One of the following:

"urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified"

"urn:oasis:names:tc:SAML:2.0:attrname-format:basic"

"urn:oasis:names:tc:SAML:2.0:attrname-format:uri"

required: optional boolean

If the attribute is required when building a SAML assertion.

source: optional object { name, name_by_idp } 

name: optional string

The name of the IdP attribute.

name_by_idp: optional array of object { idp_id, source_name } 

A mapping from IdP ID to attribute name.

idp_id: optional string

The UID of the IdP.

source_name: optional string

The name of the IdP provided attribute.

default_relay_state: optional string

The URL that the user will be redirected to after a successful login for IDP initiated logins.

idp_entity_id: optional string

The unique identifier for your SaaS application.

name_id_format: optional [SaaSAppNameIDFormat](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20saas_app_name_id_format%20%3E%20\(schema\))

The format of the name identifier sent to the SaaS application.

One of the following:

"id"

"email"

name_id_transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms an application’s user identities into a NameID value for its SAML assertion. This expression should evaluate to a singular string. The output of this expression can override the `name_id_format` setting.

public_key: optional string

The Access public certificate that will be used to verify your identity.

saml_attribute_transform_jsonata: optional string

A [JSONata] (<https://jsonata.org/>) expression that transforms an application’s user identities into attribute assertions in the SAML response. The expression can transform id, email, name, and groups values. It can also transform fields listed in the saml_attributes or oidc_fields of the identity provider used to authenticate. The output of this expression must be a JSON object.

sp_entity_id: optional string

A globally unique name for an identity or service provider.

sso_endpoint: optional string

The endpoint where your SaaS application will send login requests.

OIDCSaaSApp object { access_token_lifetime, allow_pkce_without_client_secret, app_launcher_url, 11 more } 

access_token_lifetime: optional string

The lifetime of the OIDC Access Token after creation. Valid units are m,h. Must be greater than or equal to 1m and less than or equal to 24h.

allow_pkce_without_client_secret: optional boolean

If client secret should be required on the token endpoint when authorization_code_with_pkce grant is used.

app_launcher_url: optional string

The URL where this applications tile redirects users

auth_type: optional "saml" or "oidc"

Identifier of the authentication protocol used for the saas app. Required for OIDC.

One of the following:

"saml"

"oidc"

client_id: optional string

The application client id

client_secret: optional string

The application client secret, only returned on POST request.

custom_claims: optional array of object { name, required, scope, source } 

name: optional string

The name of the claim.

required: optional boolean

If the claim is required when building an OIDC token.

scope: optional "groups" or "profile" or "email" or "openid"

The scope of the claim.

One of the following:

"groups"

"profile"

"email"

"openid"

source: optional object { name, name_by_idp } 

name: optional string

The name of the IdP claim.

name_by_idp: optional map[string]

A mapping from IdP ID to claim name.

grant_types: optional array of "authorization_code" or "authorization_code_with_pkce" or "refresh_tokens" or 2 more

The OIDC flows supported by this application

One of the following:

"authorization_code"

"authorization_code_with_pkce"

"refresh_tokens"

"hybrid"

"implicit"

group_filter_regex: optional string

A regex to filter Cloudflare groups returned in ID token and userinfo endpoint

hybrid_and_implicit_options: optional object { return_access_token_from_authorization_endpoint, return_id_token_from_authorization_endpoint } 

return_access_token_from_authorization_endpoint: optional boolean

If an Access Token should be returned from the OIDC Authorization endpoint

return_id_token_from_authorization_endpoint: optional boolean

If an ID Token should be returned from the OIDC Authorization endpoint

public_key: optional string

The Access public certificate that will be used to verify your identity.

redirect_uris: optional array of string

The permitted URL’s for Cloudflare to return Authorization codes and Access/ID tokens

refresh_token_options: optional object { lifetime } 

lifetime: optional string

How long a refresh token will be valid for after creation. Valid units are m,h,d. Must be longer than 1m.

scopes: optional array of "openid" or "groups" or "email" or "profile"

Define the user information shared with access, “offline_access” scope will be automatically enabled if refresh tokens are enabled

One of the following:

"openid"

"groups"

"email"

"profile"

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

type: optional [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

BrowserSSHApplication object { domain, type, allow_authenticate_via_warp, 29 more } 

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

BrowserVNCApplication object { domain, type, allow_authenticate_via_warp, 29 more } 

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

AppLauncherApplication object { type, allowed_idps, app_launcher_logo_url, 13 more } 

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_logo_url: optional string

The image URL of the logo shown in the App Launcher header.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

bg_color: optional string

The background color of the App Launcher page.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

footer_links: optional array of object { name, url } 

The links in the App Launcher footer.

name: string

The hypertext in the footer link.

url: string

the hyperlink in the footer link.

header_bg_color: optional string

The background color of the App Launcher header.

landing_page_design: optional object { button_color, button_text_color, image_url, 2 more } 

The design of the App Launcher landing page shown to users when they log in.

button_color: optional string

The background color of the log in button on the landing page.

button_text_color: optional string

The color of the text in the log in button on the landing page.

image_url: optional string

The URL of the image shown on the landing page.

message: optional string

The message shown on the landing page.

title: optional string

The title shown on the landing page.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_app_launcher_login_page: optional boolean

Determines when to skip the App Launcher landing page.

DeviceEnrollmentPermissionsApplication object { type, allowed_idps, auto_redirect_to_identity, 7 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

BrowserIsolationPermissionsApplication object { type, allowed_idps, auto_redirect_to_identity, 7 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

GatewayIdentityProxyEndpointApplication object { type, allowed_idps, auto_redirect_to_identity, 7 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The proxy endpoint domain in the format: 10 alphanumeric characters followed by .proxy.cloudflare-gateway.com

name: optional string

The name of the application.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

BookmarkApplication object { app_launcher_visible, domain, logo_url, 4 more } 

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

domain: optional string

The URL or domain of the bookmark.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

type: optional [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

InfrastructureApplication object { target_criteria, type, mfa_config, 2 more } 

target_criteria: array of object { port, protocol, exclude, 3 more } 

port: number

The port that the targets use for the chosen communication protocol. A port cannot be assigned to multiple protocols.

protocol: "SSH"

The communication protocol your application secures.

exclude: optional object { tags, target_attributes } 

Target is excluded when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

include: optional object { tags, target_attributes } 

Target matches when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

require: optional object { tags, target_attributes } 

Target matches only when every selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

Deprecatedtarget_attributes: optional map[array of string]

Contains a map of target attribute keys to target attribute values.

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings for infrastructure applications.

allowed_authenticators: optional array of "piv_key" or "ssh_fido2_key"

Lists the MFA methods that users can authenticate with. For infrastructure applications, supported values are `piv_key` and `ssh_fido2_key`.

One of the following:

"piv_key"

"ssh_fido2_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples: `5m` or `24h`.

name: optional string

The name of the application.

policies: optional array of object { decision, include, name, 4 more } 

The policies that Access applies to the application.

decision: [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

include: array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

name: string

The name of the Access policy.

connection_rules: optional object { ssh } 

The rules that define how users may connect to the targets secured by your application.

ssh: optional object { usernames, allow_email_alias } 

The SSH-specific rules that define how users may connect to the targets secured by your application.

usernames: array of string

Contains the Unix usernames that may be used when connecting over SSH.

allow_email_alias: optional boolean

Enables using Identity Provider email alias as SSH username.

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings for infrastructure applications.

allowed_authenticators: optional array of "piv_key" or "ssh_fido2_key"

Lists the MFA methods that users can authenticate with. For infrastructure applications, supported values are `piv_key` and `ssh_fido2_key`.

One of the following:

"piv_key"

"ssh_fido2_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples: `5m` or `24h`.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

BrowserRDPApplication object { domain, target_criteria, type, 30 more } 

Contains the targets secured by the application.

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

target_criteria: array of object { port, protocol, exclude, 3 more } 

port: number

The port that the targets use for the chosen communication protocol. A port cannot be assigned to multiple protocols.

protocol: "RDP"

The communication protocol your application secures.

exclude: optional object { tags, target_attributes } 

Target is excluded when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

include: optional object { tags, target_attributes } 

Target matches when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

require: optional object { tags, target_attributes } 

Target matches only when every selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

Deprecatedtarget_attributes: optional map[array of string]

Contains a map of target attribute keys to target attribute values.

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

McpServerApplication object { type, allow_authenticate_via_warp, allowed_idps, 16 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

McpServerPortalApplication object { type, allow_authenticate_via_warp, allowed_idps, 17 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

policies: optional array of object { id, account_id, precedence }  or string or object { id, approval_groups, approval_required, 7 more } 

The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.

One of the following:

AccessAppPolicyLink object { id, account_id, precedence } 

A JSON that links a reusable policy to an application.

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

AccessUUID2 = string

The UUID of the policy

object { id, approval_groups, approval_required, 7 more } 

id: optional string

The UUID of the policy

maxLength36

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

##### ReturnsExpand Collapse 

errors: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

messages: array of object { code, message, documentation_url, source } 

code: number

minimum1000

message: string

documentation_url: optional string

source: optional object { pointer } 

pointer: optional string

success: true

Whether the API call was successful.

result: optional object { oauth_configuration, type, user_populations, 7 more }  or object { domain, type, id, 31 more }  or object { id, allowed_idps, app_launcher_visible, 10 more }  or 11 more

One of the following:

EndUserApplication object { oauth_configuration, type, user_populations, 7 more } 

oauth_configuration: object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional true

Managed OAuth is required for end user applications and cannot be disabled.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

user_populations: array of string

The single user population associated with this application.

id: optional string

UUID.

maxLength36

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

aud: optional string

Audience tag.

maxLength64

destinations: optional array of object { uri, overrides, type }  or object { type, worker_id, overrides }  or object { type, worker_id, overrides }  or 2 more

Public hostname and Workers destinations secured by Access.

One of the following:

AccessEndUserPublicDestination object { uri, overrides, type } 

uri: string

The public hostname and optional path to secure.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

AccessEndUserWorkerDestination object { type, worker_id, overrides } 

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to secure.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AccessEndUserPreviewWorkerDestination object { type, worker_id, overrides } 

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose previews to secure.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AccessEndUserAllWorkersDestination object { type, overrides } 

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AccessEndUserAllPreviewWorkersDestination object { type, overrides } 

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

name: optional string

The name of the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

SelfHostedApplication object { domain, type, id, 31 more } 

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

SaaSApplication object { id, allowed_idps, app_launcher_visible, 10 more } 

id: optional string

UUID.

maxLength36

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

saas_app: optional [SAMLSaaSApp](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20saml_saas_app%20%3E%20\(schema\)) { auth_type, consumer_service_url, custom_attributes, 8 more }  or [OIDCSaaSApp](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20oidc_saas_app%20%3E%20\(schema\)) { access_token_lifetime, allow_pkce_without_client_secret, app_launcher_url, 11 more } 

One of the following:

SAMLSaaSApp object { auth_type, consumer_service_url, custom_attributes, 8 more } 

auth_type: optional "saml" or "oidc"

Optional identifier indicating the authentication protocol used for the saas app. Required for OIDC. Default if unset is “saml”

One of the following:

"saml"

"oidc"

consumer_service_url: optional string

The service provider’s endpoint that is responsible for receiving and parsing a SAML assertion.

custom_attributes: optional array of object { friendly_name, name, name_format, 2 more } 

friendly_name: optional string

The SAML FriendlyName of the attribute.

name: optional string

The name of the attribute.

name_format: optional "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified" or "urn:oasis:names:tc:SAML:2.0:attrname-format:basic" or "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"

A globally unique name for an identity or service provider.

One of the following:

"urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified"

"urn:oasis:names:tc:SAML:2.0:attrname-format:basic"

"urn:oasis:names:tc:SAML:2.0:attrname-format:uri"

required: optional boolean

If the attribute is required when building a SAML assertion.

source: optional object { name, name_by_idp } 

name: optional string

The name of the IdP attribute.

name_by_idp: optional array of object { idp_id, source_name } 

A mapping from IdP ID to attribute name.

idp_id: optional string

The UID of the IdP.

source_name: optional string

The name of the IdP provided attribute.

default_relay_state: optional string

The URL that the user will be redirected to after a successful login for IDP initiated logins.

idp_entity_id: optional string

The unique identifier for your SaaS application.

name_id_format: optional [SaaSAppNameIDFormat](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20saas_app_name_id_format%20%3E%20\(schema\))

The format of the name identifier sent to the SaaS application.

One of the following:

"id"

"email"

name_id_transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms an application’s user identities into a NameID value for its SAML assertion. This expression should evaluate to a singular string. The output of this expression can override the `name_id_format` setting.

public_key: optional string

The Access public certificate that will be used to verify your identity.

saml_attribute_transform_jsonata: optional string

A [JSONata] (<https://jsonata.org/>) expression that transforms an application’s user identities into attribute assertions in the SAML response. The expression can transform id, email, name, and groups values. It can also transform fields listed in the saml_attributes or oidc_fields of the identity provider used to authenticate. The output of this expression must be a JSON object.

sp_entity_id: optional string

A globally unique name for an identity or service provider.

sso_endpoint: optional string

The endpoint where your SaaS application will send login requests.

OIDCSaaSApp object { access_token_lifetime, allow_pkce_without_client_secret, app_launcher_url, 11 more } 

access_token_lifetime: optional string

The lifetime of the OIDC Access Token after creation. Valid units are m,h. Must be greater than or equal to 1m and less than or equal to 24h.

allow_pkce_without_client_secret: optional boolean

If client secret should be required on the token endpoint when authorization_code_with_pkce grant is used.

app_launcher_url: optional string

The URL where this applications tile redirects users

auth_type: optional "saml" or "oidc"

Identifier of the authentication protocol used for the saas app. Required for OIDC.

One of the following:

"saml"

"oidc"

client_id: optional string

The application client id

client_secret: optional string

The application client secret, only returned on POST request.

custom_claims: optional array of object { name, required, scope, source } 

name: optional string

The name of the claim.

required: optional boolean

If the claim is required when building an OIDC token.

scope: optional "groups" or "profile" or "email" or "openid"

The scope of the claim.

One of the following:

"groups"

"profile"

"email"

"openid"

source: optional object { name, name_by_idp } 

name: optional string

The name of the IdP claim.

name_by_idp: optional map[string]

A mapping from IdP ID to claim name.

grant_types: optional array of "authorization_code" or "authorization_code_with_pkce" or "refresh_tokens" or 2 more

The OIDC flows supported by this application

One of the following:

"authorization_code"

"authorization_code_with_pkce"

"refresh_tokens"

"hybrid"

"implicit"

group_filter_regex: optional string

A regex to filter Cloudflare groups returned in ID token and userinfo endpoint

hybrid_and_implicit_options: optional object { return_access_token_from_authorization_endpoint, return_id_token_from_authorization_endpoint } 

return_access_token_from_authorization_endpoint: optional boolean

If an Access Token should be returned from the OIDC Authorization endpoint

return_id_token_from_authorization_endpoint: optional boolean

If an ID Token should be returned from the OIDC Authorization endpoint

public_key: optional string

The Access public certificate that will be used to verify your identity.

redirect_uris: optional array of string

The permitted URL’s for Cloudflare to return Authorization codes and Access/ID tokens

refresh_token_options: optional object { lifetime } 

lifetime: optional string

How long a refresh token will be valid for after creation. Valid units are m,h,d. Must be longer than 1m.

scopes: optional array of "openid" or "groups" or "email" or "profile"

Define the user information shared with access, “offline_access” scope will be automatically enabled if refresh tokens are enabled

One of the following:

"openid"

"groups"

"email"

"profile"

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

type: optional [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

BrowserSSHApplication object { domain, type, id, 31 more } 

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

BrowserVNCApplication object { domain, type, id, 31 more } 

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

AppLauncherApplication object { type, id, allowed_idps, 15 more } 

type: "self_hosted" or "end_user" or "saas" or 12 more

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_logo_url: optional string

The image URL of the logo shown in the App Launcher header.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

bg_color: optional string

The background color of the App Launcher page.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

footer_links: optional array of object { name, url } 

The links in the App Launcher footer.

name: string

The hypertext in the footer link.

url: string

the hyperlink in the footer link.

header_bg_color: optional string

The background color of the App Launcher header.

landing_page_design: optional object { button_color, button_text_color, image_url, 2 more } 

The design of the App Launcher landing page shown to users when they log in.

button_color: optional string

The background color of the log in button on the landing page.

button_text_color: optional string

The color of the text in the log in button on the landing page.

image_url: optional string

The URL of the image shown on the landing page.

message: optional string

The message shown on the landing page.

title: optional string

The title shown on the landing page.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_app_launcher_login_page: optional boolean

Determines when to skip the App Launcher landing page.

DeviceEnrollmentPermissionsApplication object { type, id, allowed_idps, 9 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

BrowserIsolationPermissionsApplication object { type, id, allowed_idps, 9 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

GatewayIdentityProxyEndpointApplication object { type, id, allowed_idps, 9 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

domain: optional string

The proxy endpoint domain in the format: 10 alphanumeric characters followed by .proxy.cloudflare-gateway.com

name: optional string

The name of the application.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

BookmarkApplication object { id, app_launcher_visible, aud, 6 more } 

id: optional string

UUID.

maxLength36

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

aud: optional string

Audience tag.

maxLength64

domain: optional string

The URL or domain of the bookmark.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

type: optional [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

InfrastructureApplication object { target_criteria, type, id, 4 more } 

target_criteria: array of object { port, protocol, exclude, 3 more } 

port: number

The port that the targets use for the chosen communication protocol. A port cannot be assigned to multiple protocols.

protocol: "SSH"

The communication protocol your application secures.

exclude: optional object { tags, target_attributes } 

Target is excluded when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

include: optional object { tags, target_attributes } 

Target matches when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

require: optional object { tags, target_attributes } 

Target matches only when every selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

Deprecatedtarget_attributes: optional map[array of string]

Contains a map of target attribute keys to target attribute values.

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

aud: optional string

Audience tag.

maxLength64

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings for infrastructure applications.

allowed_authenticators: optional array of "piv_key" or "ssh_fido2_key"

Lists the MFA methods that users can authenticate with. For infrastructure applications, supported values are `piv_key` and `ssh_fido2_key`.

One of the following:

"piv_key"

"ssh_fido2_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples: `5m` or `24h`.

name: optional string

The name of the application.

policies: optional array of object { id, connection_rules, created_at, 7 more } 

id: optional string

The UUID of the policy

maxLength36

connection_rules: optional object { ssh } 

The rules that define how users may connect to the targets secured by your application.

ssh: optional object { usernames, allow_email_alias } 

The SSH-specific rules that define how users may connect to the targets secured by your application.

usernames: array of string

Contains the Unix usernames that may be used when connecting over SSH.

allow_email_alias: optional boolean

Enables using Identity Provider email alias as SSH username.

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings for infrastructure applications.

allowed_authenticators: optional array of "piv_key" or "ssh_fido2_key"

Lists the MFA methods that users can authenticate with. For infrastructure applications, supported values are `piv_key` and `ssh_fido2_key`.

One of the following:

"piv_key"

"ssh_fido2_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples: `5m` or `24h`.

name: optional string

The name of the Access policy.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

updated_at: optional string

formatdate-time

BrowserRDPApplication object { domain, target_criteria, type, 32 more } 

domain: string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

target_criteria: array of object { port, protocol, exclude, 3 more } 

port: number

The port that the targets use for the chosen communication protocol. A port cannot be assigned to multiple protocols.

protocol: "RDP"

The communication protocol your application secures.

exclude: optional object { tags, target_attributes } 

Target is excluded when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

include: optional object { tags, target_attributes } 

Target matches when any selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

require: optional object { tags, target_attributes } 

Target matches only when every selector in this rule matches.

tags: optional map[array of string]

Map of target tag keys to values. Values within a key are OR’d.

target_attributes: optional object { hostname } 

Hostname selector map for include, require, or exclude rules. This is distinct from the deprecated top-level target_attributes field and only supports the hostname key.

hostname: optional array of string

Deprecatedtarget_attributes: optional map[array of string]

Contains a map of target attribute keys to target attribute values.

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allow_iframe: optional boolean

Enables loading application content in an iFrame.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

app_launcher_visible: optional boolean

Displays the application in the App Launcher.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

cors_headers: optional [CORSHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20cors_headers%20%3E%20\(schema\)) { allow_all_headers, allow_all_methods, allow_all_origins, 5 more } 

allow_all_headers: optional boolean

Allows all HTTP request headers.

allow_all_methods: optional boolean

Allows all HTTP request methods.

allow_all_origins: optional boolean

Allows all origins.

allow_credentials: optional boolean

When set to `true`, includes credentials (cookies, authorization headers, or TLS client certificates) with requests.

allowed_headers: optional array of [AllowedHeaders](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_headers%20%3E%20\(schema\))

Allowed HTTP request headers.

allowed_methods: optional array of [AllowedMethods](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_methods%20%3E%20\(schema\))

Allowed HTTP request methods.

One of the following:

"GET"

"POST"

"HEAD"

"PUT"

"DELETE"

"CONNECT"

"OPTIONS"

"TRACE"

"PATCH"

allowed_origins: optional array of [AllowedOrigins](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_origins%20%3E%20\(schema\))

Allowed origins.

max_age: optional number

The maximum number of seconds the results of a preflight request can be cached.

maximum86400

minimum-1

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

eager_redirect_cookie_setting: optional boolean

Preemptively sets the Access session cookie on every hostname in a multi-hostname self-hosted application during the initial redirect chain, rather than setting it lazily on first visit. Defaults to true. Set to false to disable the eager redirect cookie behavior.

enable_binding_cookie: optional boolean

Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

path_cookie_attribute: optional boolean

Enables cookie paths to scope an application’s JWT to the application path. If disabled, the JWT will scope to the hostname by default

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

read_service_tokens_from_header: optional string

Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { “cf-access-client-id”: “88bf3b6d86161464f6509f7219099e57.access.example.com”, “cf-access-client-secret”: “bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5” }

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

Deprecatedself_hosted_domains: optional array of [SelfHostedDomains](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20self_hosted_domains%20%3E%20\(schema\))

List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.

service_auth_401_redirect: optional boolean

Returns a 401 status code when the request is blocked by a Service Auth policy.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

skip_interstitial: optional boolean

Enables automatic authentication through cloudflared.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

use_clientless_isolation_app_launcher_url: optional boolean

Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.

McpServerApplication object { type, id, allow_authenticate_via_warp, 18 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

McpServerPortalApplication object { type, id, allow_authenticate_via_warp, 19 more } 

type: [ApplicationType](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20application_type%20%3E%20\(schema\))

The application type.

One of the following:

"self_hosted"

"end_user"

"saas"

"ssh"

"vnc"

"app_launcher"

"warp"

"biso"

"bookmark"

"dash_sso"

"infrastructure"

"rdp"

"mcp"

"mcp_portal"

"proxy_endpoint"

id: optional string

UUID.

maxLength36

allow_authenticate_via_warp: optional boolean

When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.

allowed_idps: optional array of [AllowedIdPs](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20allowed_idps%20%3E%20\(schema\))

The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.

aud: optional string

Audience tag.

maxLength64

auto_redirect_to_identity: optional boolean

When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.

custom_deny_message: optional string

The custom error message shown to a user when they are denied access to the application.

custom_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.

custom_non_identity_deny_url: optional string

The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.

custom_pages: optional array of string

The custom pages that will be displayed when applicable for this application

destinations: optional array of object { overrides, type, uri }  or object { cidr, hostname, l4_protocol, 3 more }  or object { mcp_server_id, type }  or 4 more

List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.

One of the following:

PublicDestination object { overrides, type, uri } 

A public hostname that Access will secure. Public destinations support sub-domain and path. Wildcard ’*’ can be used in the definition.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

type: optional "public"

uri: optional string

The URI of the destination. Public destinations’ URIs can include a domain and path with [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).

PrivateDestination object { cidr, hostname, l4_protocol, 3 more } 

cidr: optional string

The CIDR range of the destination. Single IPs will be computed as /32.

hostname: optional string

The hostname of the destination. Matches a valid SNI served by an HTTPS origin.

l4_protocol: optional "tcp" or "udp"

The L4 protocol of the destination. When omitted, both UDP and TCP traffic will match.

One of the following:

"tcp"

"udp"

port_range: optional string

The port range of the destination. Can be a single port or a range of ports. When omitted, all ports will match.

type: optional "private"

vnet_id: optional string

The VNET ID to match the destination. When omitted, all VNETs will match.

ViaMcpServerPortalDestination object { mcp_server_id, type } 

A MCP server id configured in ai-controls. Access will secure the MCP server if accessed through a MCP portal.

mcp_server_id: optional string

The MCP server id configured in ai-controls.

type: optional "via_mcp_server_portal"

WorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker that Access will secure. All requests routed to the specified Worker, including its preview deployments, will be protected. The `preview_worker` and `public` destination types takes precedence, so you can create separate applications to override the policies for the Worker’s previews or specific paths.

type: "worker"

worker_id: string

The ID of the Cloudflare Worker to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

PreviewWorkerDestination object { type, worker_id, overrides } 

A specific Cloudflare Worker whose preview deployments Access will secure. Only requests routed to the preview deployments of the specified Worker will be protected. The `public` destination type takes precedence, so you can create separate applications to override the policies for specific paths.

type: "preview_worker"

worker_id: string

The ID of the Cloudflare Worker whose preview deployments to protect with Access.

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllWorkersDestination object { type, overrides } 

Protects all Cloudflare Workers on the account with Access, including their preview deployments. At most one destination of this type can exist per account. The `worker`, `preview_worker`, `all_preview_workers`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

AllPreviewWorkersDestination object { type, overrides } 

Protects the preview deployments of all Cloudflare Workers on the account with Access. At most one destination of this type can exist per account. The `worker`, `preview_worker`, and `public` destination types take precedence, so you can create separate applications to override the policies for specific Workers, their previews, or specific paths.

type: "all_preview_workers"

overrides: optional array of [DestinationOverride](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20destination_override%20%3E%20\(schema\)) { behavior, path_pattern } 

Rules that override how Access handles requests to this destination. Each rule can make a matching path public, bypassing Access authentication. Overrides are supported for public destinations and Worker destinations.

behavior: "public"

The behavior to apply to matching requests.

path_pattern: string

The request path pattern to match. Wildcards (`*`) are supported, but each path segment may have at most one wildcard. Unlike the `uri` in public destinations, override path patterns do not implicitly cover subpaths; to do that, use a wildcard.

maxLength512

domain: optional string

The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.

http_only_cookie_attribute: optional boolean

Enables the HttpOnly cookie attribute, which increases security against XSS attacks.

logo_url: optional string

The image URL for the logo shown in the App Launcher dashboard.

name: optional string

The name of the application.

oauth_configuration: optional object { dynamic_client_registration, enabled, grant } 

**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.

dynamic_client_registration: optional object { allow_any_on_localhost, allow_any_on_loopback, allowed_uris, enabled } 

Settings for OAuth dynamic client registration.

allow_any_on_localhost: optional boolean

Allows any client with redirect URIs on localhost.

allow_any_on_loopback: optional boolean

Allows any client with redirect URIs on 127.0.0.1.

allowed_uris: optional array of string

The URIs that are allowed as redirect URIs for dynamically registered clients. HTTP and HTTPS paths may end in `/*` to match all sub-paths. Custom-scheme URIs must be explicitly configured and match exactly.

enabled: optional boolean

Whether dynamic client registration is enabled.

enabled: optional boolean

Whether the OAuth configuration is enabled for this application. When set to `false`, Access will not handle OAuth for this application. Defaults to `true` if omitted.

grant: optional object { access_token_lifetime, session_duration } 

Settings for OAuth grant behavior.

access_token_lifetime: optional string

The lifetime of the access token. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

session_duration: optional string

The duration of the OAuth session. Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs), ms, s, m, h.

options_preflight_bypass: optional boolean

Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.

policies: optional array of object { id, account_id, approval_groups, 15 more } 

id: optional string

The UUID of the policy

maxLength36

account_id: optional string

Identifier.

maxLength32

approval_groups: optional array of [ApprovalGroup](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.policies%20%3E%20\(model\)%20approval_group%20%3E%20\(schema\)) { approvals_needed, email_addresses, email_list_uuid } 

Administrators who can approve a temporary authentication request.

approvals_needed: number

The number of approvals needed to obtain access.

minimum0

email_addresses: optional array of string

A list of emails that can approve the access request.

email_list_uuid: optional string

The UUID of an re-usable email list.

approval_required: optional boolean

Requires the user to request access from an administrator at the start of each session.

connection_rules: optional object { rdp } 

The rules that define how users may connect to targets secured by your application.

rdp: optional object { allowed_clipboard_local_to_remote_formats, allowed_clipboard_remote_to_local_formats } 

The RDP-specific rules that define clipboard behavior for RDP connections.

allowed_clipboard_local_to_remote_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from local machine to remote RDP session.

One of the following:

"text"

"file"

allowed_clipboard_remote_to_local_formats: optional array of "text" or "file"

Clipboard formats allowed when copying from remote RDP session to local machine.

One of the following:

"text"

"file"

created_at: optional string

formatdate-time

decision: optional [Decision](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20decision%20%3E%20\(schema\))

The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.

One of the following:

"allow"

"deny"

"non_identity"

"bypass"

exclude: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

include: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

isolation_required: optional boolean

Require this application to be served in an isolated browser for users matching this policy. ‘Client Web Isolation’ must be on for the account in order to use this feature.

mfa_config: optional object { allowed_authenticators, mfa_disabled, session_duration } 

Configures multi-factor authentication (MFA) settings.

allowed_authenticators: optional array of "totp" or "biometrics" or "security_key"

Lists the MFA methods that users can authenticate with.

One of the following:

"totp"

"biometrics"

"security_key"

mfa_disabled: optional boolean

Indicates whether to disable MFA for this resource. This option is available at the application and policy level.

session_duration: optional string

Defines the duration of an MFA session. Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days). Examples:`5m` or `24h`.

name: optional string

The name of the Access policy.

precedence: optional number

The order of execution for this policy. Must be unique for each policy within an app.

purpose_justification_prompt: optional string

A custom message that will appear on the purpose justification screen.

purpose_justification_required: optional boolean

Require users to enter a justification when they log in to the application.

require: optional array of [AccessRule](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications.policies%20%3E%20\(model\)%20access_rule%20%3E%20\(schema\))

Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

One of the following:

GroupRule object { group } 

Matches an Access group.

group: object { id } 

id: string

The ID of a previously created Access group.

AnyValidServiceTokenRule object { any_valid_service_token } 

Matches any valid Access Service Token

any_valid_service_token: object { } 

An empty object which matches on all service tokens.

AccessAuthContextRule object { auth_context } 

Matches an Azure Authentication Context. Requires an Azure identity provider.

auth_context: object { id, ac_id, identity_provider_id } 

id: string

The ID of an Authentication context.

ac_id: string

The ACID of an Authentication context.

identity_provider_id: string

The ID of your Azure identity provider.

AuthenticationMethodRule object { auth_method } 

Enforce different MFA options

auth_method: object { auth_method } 

auth_method: string

The type of authentication method <https://datatracker.ietf.org/doc/html/rfc8176#section-2>.

AzureGroupRule object { azureAD } 

Matches an Azure group. Requires an Azure identity provider.

azureAD: object { id, identity_provider_id } 

id: string

The ID of an Azure group.

identity_provider_id: string

The ID of your Azure identity provider.

CertificateRule object { certificate } 

Matches any valid client certificate.

certificate: object { } 

AccessCommonNameRule object { common_name } 

Matches a specific common name.

common_name: object { common_name } 

common_name: string

The common name to match.

CountryRule object { geo } 

Matches a specific country

geo: object { country_code } 

country_code: string

The country code that should be matched.

AccessDevicePostureRule object { device_posture } 

Enforces a device posture rule has run successfully

device_posture: object { integration_uid, account_id } 

integration_uid: string

The ID of a device posture integration.

account_id: optional string

The ID of the account that owns the device posture integration.

maxLength32

DomainRule object { email_domain } 

Match an entire email domain.

email_domain: object { domain } 

domain: string

The email domain to match.

EmailListRule object { email_list } 

Matches an email address from a list.

email_list: object { id } 

id: string

The ID of a previously created email list.

EmailRule object { email } 

Matches a specific email.

email: object { email } 

email: string

The email of the user.

formatemail

EveryoneRule object { everyone } 

Matches everyone.

everyone: object { } 

An empty object which matches on all users.

ExternalEvaluationRule object { external_evaluation } 

Create Allow or Block policies which evaluate the user based on custom criteria.

external_evaluation: object { evaluate_url, keys_url } 

evaluate_url: string

The API endpoint containing your business logic.

keys_url: string

The API endpoint containing the key that Access uses to verify that the response came from your API.

GitHubOrganizationRule object { "github-organization" } 

Matches a Github organization. Requires a Github identity provider.

"github-organization": object { identity_provider_id, name, team } 

identity_provider_id: string

The ID of your Github identity provider.

name: string

The name of the organization.

team: optional string

The name of the team

GSuiteGroupRule object { gsuite } 

Matches a group in Google Workspace. Requires a Google Workspace identity provider.

gsuite: object { email, identity_provider_id } 

email: string

The email of the Google Workspace group.

identity_provider_id: string

The ID of your Google Workspace identity provider.

AccessLoginMethodRule object { login_method } 

Matches a specific identity provider id.

login_method: object { id } 

id: string

The ID of an identity provider.

IPListRule object { ip_list } 

Matches an IP address from a list.

ip_list: object { id } 

id: string

The ID of a previously created IP list.

IPRule object { ip } 

Matches an IP address block.

ip: object { ip } 

ip: string

An IPv4 or IPv6 CIDR block.

OktaGroupRule object { okta } 

Matches an Okta group. Requires an Okta identity provider.

okta: object { identity_provider_id, name } 

identity_provider_id: string

The ID of your Okta identity provider.

name: string

The name of the Okta group.

SAMLGroupRule object { saml } 

Matches a SAML group. Requires a SAML identity provider.

saml: object { attribute_name, attribute_value, identity_provider_id } 

attribute_name: string

The name of the SAML attribute.

attribute_value: string

The SAML attribute value to look for.

identity_provider_id: string

The ID of your SAML identity provider.

AccessOIDCClaimRule object { oidc } 

Matches an OIDC claim. Requires an OIDC identity provider.

oidc: object { claim_name, claim_value, identity_provider_id } 

claim_name: string

The name of the OIDC claim.

claim_value: string

The OIDC claim value to look for.

identity_provider_id: string

The ID of your OIDC identity provider.

ServiceTokenRule object { service_token } 

Matches a specific Access Service Token

service_token: object { token_id } 

token_id: string

The ID of a Service Token.

AccessLinkedAppTokenRule object { linked_app_token } 

Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.

linked_app_token: object { app_uid } 

app_uid: string

The ID of an Access OIDC SaaS application

AccessUserRiskScoreRule object { user_risk_score } 

Matches a user’s risk score.

user_risk_score: object { user_risk_score } 

user_risk_score: array of "low" or "medium" or "high" or "unscored"

A list of risk score levels to match. Values can be low, medium, high, or unscored.

One of the following:

"low"

"medium"

"high"

"unscored"

AccessCloudflareAccountMemberRule object { cloudflare_account_member } 

Matches users who are members of a specific Cloudflare account. Requires a Cloudflare identity provider.

cloudflare_account_member: object { account_id } 

account_id: optional string

Identifier.

maxLength32

session_duration: optional string

The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h.

updated_at: optional string

formatdate-time

same_site_cookie_attribute: optional string

Sets the SameSite cookie setting, which provides increased security against CSRF attacks.

scim_config: optional object { idp_uid, remote_uri, authentication, 3 more } 

Configuration for provisioning to this application via SCIM. This is currently in closed beta.

idp_uid: string

The UID of the IdP to use as the source for SCIM resources to provision to this application.

remote_uri: string

The base URI for the application’s SCIM-compatible API.

authentication: optional [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or 2 more

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

AccessSCIMConfigMultiAuthentication = array of [SCIMConfigAuthenticationHTTPBasic](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_http_basic%20%3E%20\(schema\)) { password, scheme, user }  or [SCIMConfigAuthenticationOAuthBearerToken](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth_bearer_token%20%3E%20\(schema\)) { token, scheme }  or [SCIMConfigAuthenticationOauth2](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_authentication_oauth2%20%3E%20\(schema\)) { authorization_url, client_id, client_secret, 3 more }  or object { client_id, client_secret, scheme } 

Multiple authentication schemes

One of the following:

SCIMConfigAuthenticationHTTPBasic object { password, scheme, user } 

Attributes for configuring HTTP Basic authentication scheme for SCIM provisioning to an application.

password: string

Password used to authenticate with the remote SCIM service.

scheme: "httpbasic"

The authentication scheme to use when making SCIM requests to this application.

user: string

User name used to authenticate with the remote SCIM service.

SCIMConfigAuthenticationOAuthBearerToken object { token, scheme } 

Attributes for configuring OAuth Bearer Token authentication scheme for SCIM provisioning to an application.

token: string

Token used to authenticate with the remote SCIM service.

scheme: "oauthbearertoken"

The authentication scheme to use when making SCIM requests to this application.

SCIMConfigAuthenticationOauth2 object { authorization_url, client_id, client_secret, 3 more } 

Attributes for configuring OAuth 2 authentication scheme for SCIM provisioning to an application.

authorization_url: string

URL used to generate the auth code used during token generation.

client_id: string

Client ID used to authenticate when generating a token for authenticating with the remote SCIM service.

client_secret: string

Secret used to authenticate when generating a token for authenticating with the remove SCIM service.

scheme: "oauth2"

The authentication scheme to use when making SCIM requests to this application.

token_url: string

URL used to generate the token used to authenticate with the remote SCIM service.

scopes: optional array of string

The authorization scopes to request when generating the token used to authenticate with the remove SCIM service.

AccessSCIMConfigAuthenticationAccessServiceToken object { client_id, client_secret, scheme } 

Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.

client_id: string

Client ID of the Access service token used to authenticate with the remote service.

client_secret: string

Client secret of the Access service token used to authenticate with the remote service.

scheme: "access_service_token"

The authentication scheme to use when making SCIM requests to this application.

deactivate_on_delete: optional boolean

If false, propagates DELETE requests to the target application for SCIM resources. If true, sets ‘active’ to false on the SCIM resource. Note: Some targets do not support DELETE operations.

enabled: optional boolean

Whether SCIM provisioning is turned on for this application.

mappings: optional array of [SCIMConfigMapping](https://developers.cloudflare.com/api/resources/zero_trust#\(resource\)%20zero_trust.access.applications%20%3E%20\(model\)%20scim_config_mapping%20%3E%20\(schema\)) { schema, enabled, filter, 3 more } 

A list of mappings to apply to SCIM resources before provisioning them in this application. These can transform or filter the resources to be provisioned.

schema: string

Which SCIM resource type this mapping applies to.

enabled: optional boolean

Whether or not this mapping is enabled.

filter: optional string

A [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2) that matches resources that should be provisioned to this application.

operations: optional object { create, delete, update } 

Whether or not this mapping applies to creates, updates, or deletes.

create: optional boolean

Whether or not this mapping applies to create (POST) operations.

delete: optional boolean

Whether or not this mapping applies to DELETE operations.

update: optional boolean

Whether or not this mapping applies to update (PATCH/PUT) operations.

strictness: optional "strict" or "passthrough"

The level of adherence to outbound resource schemas when provisioning to this mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown values to the target.

One of the following:

"strict"

"passthrough"

transform_jsonata: optional string

A [JSONata](https://jsonata.org/) expression that transforms the resource before provisioning it in the application.

session_duration: optional string

The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.

tags: optional array of string

The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.

### Update an Access application

HTTP

HTTP

HTTP

TypeScript

TypeScript

Python

Python

Go

Go

Terraform

Terraform
    
    
    curl https://api.cloudflare.com/client/v4/$ACCOUNTS_OR_ZONES/$ACCOUNT_OR_ZONE_ID/access/apps/$APP_ID \
        -X PUT \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{
              "oauth_configuration": {},
              "type": "self_hosted",
              "user_populations": [
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"
              ],
              "domain": "test.example.com/admin",
              "name": "Admin Site",
              "self_hosted_domains": [
                "test.example.com/admin",
                "test.anotherexample.com/staff"
              ]
            }'

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "success": true,
      "result": {
        "oauth_configuration": {
          "dynamic_client_registration": {
            "allow_any_on_localhost": true,
            "allow_any_on_loopback": true,
            "allowed_uris": [
              "https://example.com/callback",
              "com.example.app:/oauth/callback"
            ],
            "enabled": true
          },
          "enabled": true,
          "grant": {
            "access_token_lifetime": "5m",
            "session_duration": "24h"
          }
        },
        "type": "self_hosted",
        "user_populations": [
          "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"
        ],
        "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        "allowed_idps": [
          "699d98642c564d2e855e9661899b7252"
        ],
        "aud": "737646a56ab1df6ec9bddc7e5ca84eaf3b0768850f3ffb5d74f1534911fe3893",
        "created_at": "2014-01-01T05:20:00.12345Z",
        "destinations": [
          {
            "uri": "uri",
            "overrides": [
              {
                "behavior": "public",
                "path_pattern": "/health/*"
              }
            ],
            "type": "public"
          }
        ],
        "domain": "test.example.com/admin",
        "name": "Admin Site",
        "self_hosted_domains": [
          "test.example.com/admin",
          "test.anotherexample.com/staff"
        ],
        "updated_at": "2014-01-01T05:20:00.12345Z"
      }
    }

##### Returns Examples

200 example
    
    
    {
      "errors": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "messages": [
        {
          "code": 1000,
          "message": "message",
          "documentation_url": "documentation_url",
          "source": {
            "pointer": "pointer"
          }
        }
      ],
      "success": true,
      "result": {
        "oauth_configuration": {
          "dynamic_client_registration": {
            "allow_any_on_localhost": true,
            "allow_any_on_loopback": true,
            "allowed_uris": [
              "https://example.com/callback",
              "com.example.app:/oauth/callback"
            ],
            "enabled": true
          },
          "enabled": true,
          "grant": {
            "access_token_lifetime": "5m",
            "session_duration": "24h"
          }
        },
        "type": "self_hosted",
        "user_populations": [
          "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"
        ],
        "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        "allowed_idps": [
          "699d98642c564d2e855e9661899b7252"
        ],
        "aud": "737646a56ab1df6ec9bddc7e5ca84eaf3b0768850f3ffb5d74f1534911fe3893",
        "created_at": "2014-01-01T05:20:00.12345Z",
        "destinations": [
          {
            "uri": "uri",
            "overrides": [
              {
                "behavior": "public",
                "path_pattern": "/health/*"
              }
            ],
            "type": "public"
          }
        ],
        "domain": "test.example.com/admin",
        "name": "Admin Site",
        "self_hosted_domains": [
          "test.example.com/admin",
          "test.anotherexample.com/staff"
        ],
        "updated_at": "2014-01-01T05:20:00.12345Z"
      }
    }
