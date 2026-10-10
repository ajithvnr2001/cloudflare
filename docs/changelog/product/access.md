---
url: https://developers.cloudflare.com/changelog/product/access/
title: Access Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:13.090866+00:00
---

# Access Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/access/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 2, 2026

## [New strict service token authentication setting for Access](https://developers.cloudflare.com/changelog/post/2026-10-02-strict-service-token-authentication/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

The strict service token authentication setting applies consistent behavior to requests made with service tokens. When the setting is on for a Zero Trust organization, Access handles requests with service token headers as follows:

  * If authentication or authorization fails, Access always returns `401` or `403` instead of redirecting the client to the login page with `302`.
  * Only Service Auth policies can authorize the request. Access ignores Allow policies and any `CF_Authorization` cookie sent with the request.
  * Access does not return a `CF_Authorization` cookie to the client after successful authentication. Subsequent requests should continue to use service token headers.
  * Failed requests for recognized service tokens appear in [Access authentication logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#non-identity-authentication).



Zero Trust organizations created on or after October 5, 2026 have strict service token authentication turned on by default and cannot turn it off. Cloudflare recommends that existing organizations turn it on as well.

Organizations created before October 5, 2026 can configure the setting in the dashboard or through the API.

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Access settings**.

[ Go to **Access settings** ↗ ](https://one.dash.cloudflare.com/?to=/:account/access-controls/settings)
  2. Under **Manage service tokens** , turn on **Strict service token authentication**.

  3. In the confirmation dialog, select **Enable**.




To turn off strict service token authentication, turn off the setting and select **Disable**.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/access/organizations" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"strict_service_token_auth": true
    	}'

To turn off strict service token authentication, set `strict_service_token_auth` to `false`.

For behavior and configuration details, refer to [Strict service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#strict-service-token-authentication).

Oct 1, 2026

## [Simplified permissions for tagging targets with Access for Infrastructure](https://developers.cloudflare.com/changelog/post/2026-10-01-infrastructure-target-tag-permissions/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now tag [targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets) using only the `Zero Trust Write` API token permission. Previously, tagging targets through the API required both `Zero Trust Write` and `Tag Write` permissions on the API token.

This change applies to inline target tagging through the [Infrastructure Access Targets API](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/infrastructure/subresources/targets/). Tagging resources through the general [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/) still requires the `Tag Admin`, `Tag Write`, or equivalent role.

For more information, refer to [Tag targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#tag-targets).

Sep 24, 2026

## [MCP server portals are now generally available](https://developers.cloudflare.com/changelog/post/2026-09-24-mcp-portals-ga/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) are now generally available to all Cloudflare customers. A portal gives users one endpoint for approved Model Context Protocol (MCP) servers. Cloudflare Access logs tool, prompt, and resource activity.

Since the open beta, MCP server portals have added:

  * [Gateway routing](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway) for HTTP logging and data loss prevention (DLP) scanning
  * [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies) that control how portals reduce tool definitions and token use
  * [Static OAuth client credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials) for providers that do not support Dynamic Client Registration
  * [Session management](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions) for reconnecting servers and changing authorizations from the portal
  * [Service token authentication](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token) for autonomous agents and machine-to-machine access
  * [Logpush support](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) for exporting portal activity to external storage or a security information and event management (SIEM) system



To create a portal and connect an MCP client, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

Sep 22, 2026

## [Automatically manage inactive Access service tokens](https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now automatically disable or delete inactive service tokens. Administrators can set an inactivity period from 30 to 365 days and choose what Access does when a token reaches that limit.

To be eligible for cleanup, a token must be older than the configured period, must not have successfully authenticated during that period, and must not be directly referenced by an Access policy rule. Cleanup runs gradually in the background, so eligible tokens may not be disabled or deleted immediately.

For configuration instructions, refer to [Manage inactive service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#manage-inactive-service-tokens).

Sep 22, 2026

## [Private MCP server support for MCP server portals](https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to MCP servers available only on your private network. The portal uses [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) to reach [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and IP addresses without exposing the MCP server to the public Internet.

Connect the server network to Cloudflare with [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/), or another [Cloudflare One connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/). Configure a private hostname or CIDR route, then turn on **Route traffic through Cloudflare Gateway** when you add the server. OAuth authorization server endpoints, such as the authorization and token endpoints, must be accessible on the public Internet. If Cloudflare automatically registers the OAuth client through Dynamic Client Registration (DCR), the registration endpoint must also be accessible on the public Internet.

For setup instructions, refer to [Connect a private MCP server](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-a-private-mcp-server).

Sep 15, 2026

## [Access for Infrastructure now supports tagged targets and tag-based target criteria](https://developers.cloudflare.com/changelog/post/2026-09-15-infrastructure-target-tags/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now integrates with [Resource Tagging](https://developers.cloudflare.com/resource-tagging/). You can attach key-value tags to [infrastructure targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target) and use them in access policies.

You can manage tags on targets inline when you create or edit a target or through the central [Resource Tagging API](https://developers.cloudflare.com/resource-tagging/how-to/manage-tags/). Cloudflare keeps tags in sync across both methods.

Infrastructure applications also support a target criteria model with `include`, `require`, and `exclude` operators. Each operator can match targets by hostname, tag, or both.

  * **Include** matches targets that have any of the specified values.
  * **Require** matches targets that have all of the specified values.
  * **Exclude** rejects targets that have any of the specified values.

![Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2372,height=1616,format=webp/_astro/tags-in-infra-app.ja2Tp-Gq.png)

For more information, refer to [Add an infrastructure application](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/).

Sep 14, 2026

## [Require fresh authentication for SAML identity providers](https://developers.cloudflare.com/changelog/post/2026-09-14-saml-force-authentication/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on **Require reauthentication** in the Cloudflare dashboard, or set `force_authn` to `true` through the API. Access will then set `ForceAuthn` to `true` in signed and unsigned SAML authentication requests.

This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is `false`.

For configuration details, refer to [Require fresh authentication at the identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider).

Aug 26, 2026

## [Access service token secrets use a scannable format](https://developers.cloudflare.com/changelog/post/2026-08-26-service-token-secret-format/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format `cfast_[40 alphanumeric characters][8-character checksum]`. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.

Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same `CF-Access-Client-Id` and `CF-Access-Client-Secret` authentication headers.

For more information, refer to [Service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Aug 25, 2026

## [Grace periods for service token rotation](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-rotation-grace-periods/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.

The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.

For configuration instructions, refer to [Rotate service token secrets](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets).

Aug 25, 2026

## [Temporarily turn off Access service tokens](https://developers.cloudflare.com/changelog/post/2026-08-25-service-token-status-controls/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.

Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.

For configuration instructions, refer to [Turn a service token on or off](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off).

Aug 25, 2026

## [MCP server portals support MCP 2026-07-28 specification](https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support the stateless MCP `2026-07-28` specification for client and upstream server connections.

The portal's `/mcp` endpoint automatically accepts stateless MCP `2026-07-28` requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP `2026-07-28` support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.

SSE connections continue to use the legacy protocol. For details, refer to [MCP server portal transport and protocol compatibility](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport).

Aug 19, 2026

## [Access resource lists now support resource-scoped roles](https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.

The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned `403` responses.

For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.

For role definitions and assignment details, refer to [Resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) and [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/).

Aug 14, 2026

## [You can now enable Access on a Worker or all Workers at once](https://developers.cloudflare.com/changelog/post/2026-08-14-workers-access/)

[Workers](https://developers.cloudflare.com/workers/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You now have two new ways to protect your [Workers](https://developers.cloudflare.com/workers/) with [Cloudflare Access](https://developers.cloudflare.com/workers/configuration/cloudflare-access/).

**Protect an application across all its domains at once**

Until now, if a Worker was reachable on a route, a Custom Domain, and a `workers.dev` URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.

Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.

![Access setting for protecting a single Worker](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1476,height=689,format=webp/_astro/protect-one-worker.BSpeeOry.png)

**Protect all new and existing Workers by default**

Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.

![Account-wide Access setting that protects all Workers](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2436,height=1432,format=webp/_astro/protect-all-workers._AWy-S-E.png)

If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.

![Make a Worker public when all Workers are protected](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1228,height=756,format=webp/_astro/make-worker-public.D3yjPjtf.png)

Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.

For more advanced policy options, edit the policy in [Zero Trust ↗︎](https://dash.cloudflare.com/?to=/:account/one/access/apps).

![Access policy configuration for controlling who can sign in](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1276,height=1220,format=webp/_astro/choose-who-can-sign-in.DKf3kWAK.png)

**View all of your Worker Access policies**

You can view and manage all of your Access policies in the **Access** tab of the Workers & Pages section in the dashboard.

![Access tab showing all configured Access policies](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1646,height=1366,format=webp/_astro/access-policies.DN7yCwHX.png)

**See who is accessing your Worker**

When Access is enabled on your Worker, every authenticated request includes `ctx.access`. Call [`ctx.access.getIdentity()`](https://developers.cloudflare.com/workers/runtime-apis/context/#access) to get the user's email, name, and groups — no manual JWT validation required.
    
    
    export default {
      async fetch(request, env, ctx) {
        if (!ctx.access) {
          return new Response("Access did not run", { status: 401 });
        }
    
        const identity = await ctx.access.getIdentity();
        return Response.json({ aud: ctx.access.aud, email: identity?.email });
      },
    };

**Test Access locally**

You can now test Cloudflare Access locally with `wrangler dev`. Add a `dev` block to your `wrangler.jsonc`:
    
    
    {
      "access": {
        "dev": {
          "aud": "my-app",
          "identity": { "email": "admin@example.com" }
        }
      }
    }

Your Worker will receive this identity through `ctx.access` and `ctx.access.getIdentity()`, letting you test authenticated and unauthenticated flows without deploying. Remove the `dev` block to simulate unauthenticated requests.

**API and programmatic access**

You can also set up these policies through the [Workers API](https://developers.cloudflare.com/workers/configuration/cloudflare-access/) instead of the dashboard.

Aug 12, 2026

## [Independent MFA supports FIDO2 for infrastructure applications](https://developers.cloudflare.com/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow `ssh_fido2_key`, `piv_key`, or both in application-level and policy-level MFA settings.

Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.

For setup instructions, refer to [Enroll a FIDO2 key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps) and [Configure MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

Aug 5, 2026

## [Identity-aware controls are now available in AI Gateway](https://developers.cloudflare.com/changelog/post/2026-08-05-access-user-id-metadata/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:

  * **Protect your gateway endpoint.** Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.
  * **Identity-aware controls.** When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.



With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as `cf.user_id`.

For setup instructions, refer to [Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access/).

Aug 3, 2026

## [Control authorization cookies for multi-domain Access applications](https://developers.cloudflare.com/changelog/post/2026-08-03-eager-redirect-cookie-setting/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.

Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.

The new **Eager redirect cookie** setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a `CF_Authorization` cookie. This supports applications that need to make requests across hostnames before the user visits each one.

For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.

To configure the setting, refer to [Authorization cookie](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie).

Jul 31, 2026

## [Static OAuth client credentials for MCP server portals](https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.

When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the `client_secret_post` and `client_secret_basic` token endpoint authentication methods.

Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.

For setup instructions, refer to [Configure manual OAuth credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials).

Jul 30, 2026

## [Admins can turn on Code Mode by default for MCP portal users](https://developers.cloudflare.com/changelog/post/2026-07-30-mcp-portal-code-mode-policies/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) now support four Code Mode policies: _Off_ , _Opt-in_ , _On by default_ , and _Enforced_. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.

Existing portals retain their current behavior. Portals that previously allowed Code Mode use _Opt-in_ , while portals that did not allow Code Mode use _Off_. New portals also use _Opt-in_ by default.

Clients turn on Code Mode for an _Opt-in_ portal with `?codemode=search_and_execute`. The _On by default_ policy lets clients opt out with `?codemode=off`, which avoids nested code execution when a client runs its own Code Mode implementation. The _Off_ and _Enforced_ policies ignore client overrides.

The Cloudflare API exposes these policies through the `code_mode` field:
    
    
    {
    	"code_mode": "default_on"
    }

The supported values are `off`, `opt_in`, `default_on`, and `enforced`. The previous `allow_code_mode` boolean is deprecated.

For configuration details and client behavior, refer to [Code Mode policies](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies).

Jul 20, 2026

## [Browser-based login for plaintext HTTP private applications](https://developers.cloudflare.com/changelog/post/2026-07-20-http-private-apps-l7-auth/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Cloudflare Access now uses the standard browser-based login flow for [private applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/) served over plaintext HTTP on port `80`.

Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an `Authentication required` pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access [application token](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/) on success.

This brings the HTTP experience in line with HTTPS apps (with [Gateway TLS decryption](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/) turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.

Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.

Jul 16, 2026

## [Bulk print PDFs for browser-based RDP](https://developers.cloudflare.com/changelog/post/2026-07-16-rdp-bulk-print/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select **Print all PDFs** in the clipboard panel. The files are combined into one PDF and sent to your local printer.

![The clipboard panel showing the Print all PDFs option for multiple selected PDF files.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=768,height=432,format=webp/_astro/rdp-bulk-print.DT4sCcI-.png)

Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to [Print PDFs for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs).

Jul 7, 2026

## [File transfer controls for browser-based RDP (beta)](https://developers.cloudflare.com/changelog/post/2026-07-07-rdp-file-transfer-beta/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.

![File transfer connection settings in the Access policy configuration.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1356,height=692,format=webp/_astro/file-transfer-policy-control.CiSEa5rr.png)

This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.

#### Configuration options

File transfer controls are configured per policy within your Access application, alongside existing [text clipboard controls](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings). For each policy, you can select one of the following options:

  * **Client to remote RDP session allowed** — Users can upload files from their local machine into the browser-based RDP session.
  * **Remote RDP session to client allowed** — Users can download files from the browser-based RDP session to their local machine.
  * **Both directions allowed** — Users can upload and download files between their local machine and the browser-based RDP session.
  * **Disable copying/pasting** — Users are not allowed to transfer files between their local machine and the browser-based RDP session.



By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.

#### How it works

To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.

![The clipboard side panel showing files available for transfer.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=812,height=532,format=webp/_astro/clipboard-side-panel.Us2RfXfs.png)![A remote document ready for download or local printing.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=770,height=442,format=webp/_astro/remote-doc-ready-for-download-or-print-local.Dcm5hrGD.png)

This feature is in beta and available on all Zero Trust plans. For more information, refer to [File transfer for browser-based RDP](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files).

Jul 1, 2026

## [Fix redirect URL fragment encoding for single-page applications](https://developers.cloudflare.com/changelog/post/2026-07-01-spa-redirect-fragment-fix/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Access now correctly preserves URL fragment characters (`/`, `?`, `=`, `&`, `;`) when redirecting users back to an application after login. Previously, these characters were encoded with `encodeURIComponent`, which mangled fragment-based routes used by single-page applications (SPAs).

For example, an SPA URL like `https://app.example.com/#/dashboard?tab=settings&view=advanced` would previously redirect to a broken URL after login. This is now handled correctly.

If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.

Jul 1, 2026

## [Independent MFA for infrastructure applications](https://developers.cloudflare.com/changelog/post/2026-07-01-ssh-mfa-piv-keys/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.

With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, `root`) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.

#### Enrollment

Users enroll their YubiKey PIV key through the [App Launcher](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/app-launcher/). For enrollment instructions and SSH client setup, refer to [Enroll a PIV key for infrastructure apps](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps).

#### Configuration

For setup instructions, refer to [Enforce MFA for infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications).

Jun 26, 2026

## [Service token support for MCP server portals](https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

You can now connect autonomous agents and bots to an [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) using an [Access service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/). Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.

To set this up:

  * Add a [Service Auth policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#service-auth) that matches your service token to the portal's Access application.
  * Add a Service Auth policy that matches the same token to each linked MCP server's Access application.
  * Turn **Require user auth** off (`on_behalf: false`) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.



The bot connects with `CF-Access-Client-Id` and `CF-Access-Client-Secret` headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.

For step-by-step setup, refer to [Connect with a service token](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token).

Jun 18, 2026

## [Cloudflare identity provider is now the default for new accounts](https://developers.cloudflare.com/changelog/post/2026-06-18-cloudflare-idp-default/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

When you create a new Zero Trust organization, Cloudflare now adds the [Cloudflare identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/) as your default login method. Previously, new organizations started with [one-time PIN (OTP)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/).

With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any [third-party identity provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/) whenever you need to.

This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.

← Prev

1[2](https://developers.cloudflare.com/changelog/product/access/2/)[3](https://developers.cloudflare.com/changelog/product/access/3/)

[Next →](https://developers.cloudflare.com/changelog/product/access/2/)
