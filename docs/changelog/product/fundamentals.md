---
url: https://developers.cloudflare.com/changelog/product/fundamentals/
title: Cloudflare Fundamentals Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:07.394135+00:00
---

# Cloudflare Fundamentals Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/fundamentals/

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

Oct 9, 2026

## [Improved HTTP/3 client cancellation reporting](https://developers.cloudflare.com/changelog/post/2026-10-09-http3-499-reporting-improvement/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare has improved how it handles and reports client-cancelled HTTP/3 requests across Free, Pro, Business, and Enterprise plans. Customers now get a clearer view of client behavior in Cloudflare analytics and, where available, logs.

Previously, Cloudflare did not always stop an HTTP/3 request when the client cancelled its request stream. Some cancellations were already recorded as `499`, while others continued to the origin and showed the eventual upstream status.

Cloudflare now stops affected requests sooner, reducing unnecessary origin work, and records them as `499`. Customers may notice more `499` status codes for HTTP/3 traffic. This reflects more consistent reporting of existing cancellations, not an increase in failed requests.

Customers who use `499` status codes in availability calculations should consider excluding them from server-side error rates because they represent requests cancelled by clients.

For more information, refer to [Error 499](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/).

Oct 9, 2026

## [More efficient Markdown for Agents conversion](https://developers.cloudflare.com/changelog/post/2026-10-09-markdown-for-agents-in-process-conversion/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) now converts HTML with an in-process streaming engine at the edge. It processes content as it arrives instead of buffering the HTML response and sending it to a separate conversion service. This reduces conversion overhead and memory use.

This release also changes the conversion limit and response headers:

  * Conversion supports up to 6 MiB (6,291,456 bytes) of decompressed HTML, increased from 2 MiB (2,097,152 bytes). The limit applies after decompression, not to the compressed response size.
  * Converted responses no longer generate the `x-markdown-tokens` or `x-original-tokens` headers. Clients that use these values need to calculate token counts themselves.
  * `Content-Length` is removed from converted responses rather than recalculated, because the Markdown body is streamed.



For more information, refer to the [Markdown for Agents documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/).

Oct 7, 2026

## [Cloudflare Organizations is generally available](https://developers.cloudflare.com/changelog/post/2026-10-07-organizations-generally-available/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations is now generally available for Enterprise customers and MSSP/Distributor partners.

Organizations provides a top-level container for centrally managing accounts, members, analytics, and shared policies. Organization Super Administrators receive implicit access to every account in their Organization without requiring separate account memberships.

Enterprise customers can manage accounts in a single-tier Organization. MSSP/Distributor partners can use nested sub-organizations to manage customer accounts.

Organization Roles remains in beta, and current product limitations still apply.

For more information, refer to [Cloudflare Organizations](https://developers.cloudflare.com/fundamentals/organizations/) and [current limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/).

Oct 2, 2026

## [Organizations support increased account and zone limits](https://developers.cloudflare.com/changelog/post/2026-10-02-organization-account-zone-limits/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Cloudflare Organizations now support up to **20,000 accounts** and **200,000 zones**. For MSSP/Distributors using sub-organizations, these limits are applied at the root Organization.

If you require a higher limit, reach out to your account team. The new limits apply to enterprise and MSSP/Distributor Organizations. Legacy reseller partner and brand partner tenants retain their existing quota behavior.

For more information, refer to [Account and zone limits](https://developers.cloudflare.com/fundamentals/organizations/limitations/#account-and-zone-limits).

Oct 1, 2026

## [Account members can self-serve create Account API tokens](https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Account API token creation is no longer limited to Super Administrators. Members with the **API Token Provisioning** role can now create Account API tokens via the Dashboard, API, Terraform, or CF CLI, making it easier for developers and platform teams to provision credentials without depending on a Super Administrator for Account API Token Provisioning.

![Creating an Account API Token via CF CLI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1540,height=818,format=webp/_astro/2026-10-01-account-api-token-provisioning.Dn0G5DUa.png)

#### What's new

  * **Delegated creation** : Members with the **API Token Provisioning** role can create Account API tokens from the dashboard. Administrators can grant this role through the dashboard, API, or Terraform.
  * **OAuth support for token creation** : OAuth clients that request the `account_api_tokens:create` scope, starting with Cloudflare CLI, can create Account API tokens.
  * **Account API token permissions limited to the creator’s access at creation time** : Members can only create an Account API Token using the permissions they already have. For OAuth-created tokens, permissions are also limited to the scopes granted during authorization.
  * **Creator attribution and visibility** : Account API tokens now include creator metadata. Super Administrators and Administrators can view all Account API tokens in an account, while members with the **API Token Provisioning** role can only view tokens they created.



For more information, refer to [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/), [Create tokens via API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/), and [Roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

Sep 17, 2026

## [Create additional Free accounts through the dashboard and API](https://developers.cloudflare.com/changelog/post/2026-09-15-free-account-creation/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're expanding how customers create accounts across Cloudflare, making it easier to self-serve account creation in the dashboard, automate standalone account creation with user-owned API tokens or OAuth access tokens, and create Free accounts directly within Enterprise Organizations.

#### What's New

**Dashboard account creation:** All cloudflare customers can create additional Free accounts directly through self-serve flows in the Cloudflare dashboard.

**Enterprise Organization account creation:** Super Administrators can now create up to five Free accounts directly within an Enterprise Organization. This makes it easier to provision and manage additional accounts and directly associate them with your Organization.

**API and OAuth account creation:** Customers can now create standalone Free accounts programmatically via User-owned API tokens or OAuth access tokens.

For more information:

  * [Create a Free account in the dashboard](https://developers.cloudflare.com/fundamentals/account/create-account/)
  * [Create an account via the API](https://developers.cloudflare.com/api/resources/accounts/methods/create/)
  * [Create Free accounts in an Enterprise Organization](https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/#create-new-accounts)



Sep 4, 2026

## [Enterprise customers can self-serve CDN upload limits up to 5 GB](https://developers.cloudflare.com/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)

Enterprise customers can now configure a zone's CDN **Maximum Upload Size** up to 5 GB directly from the **Network** page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.

The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).

Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.

Refer to [Cache upload limits](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#upload-limits) and [Workers request body size limits](https://developers.cloudflare.com/workers/platform/limits/#request-and-response-limits) for details.

Aug 21, 2026

## [Enriched 403 responses for the Cloudflare API](https://developers.cloudflare.com/changelog/post/2026-08-20-contextual-403s/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare API `403 Forbidden` responses now include a `documentation_url` field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.

**What's New**

**Enriched 403 error responses** : When a Cloudflare API request is denied, the error response now includes a `documentation_url` field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.

**Faster troubleshooting** : The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.

**Better support for tools and agents** : Agents can use the \documentation_url` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.`

Example 403 response:
    
    
    {
      "success": false,
      "errors": [
        {
          "code": 10000,
          "message": "Forbidden",
          "documentation_url": "https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list"
        }
      ],
      "messages": [],
      "result": null
    }

For more info:

  * [Browse the Cloudflare API documentation](https://developers.cloudflare.com/api/)
  * [Review Cloudflare roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/)
  * [Review API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/)



Aug 21, 2026

## [Saved login profiles for returning users](https://developers.cloudflare.com/changelog/post/2026-08-21-one-click-login/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare Dashboard users can now save login profiles on a device for faster sign-in on future visits.

![Saved login profiles for returning users](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2212,height=1544,format=webp/_astro/2026-08-21-one-click-login.CbMATqrT.png)

**What's New**

**Save login profiles on a device** : After a successful sign-in, users can choose to save a login profile on that device. Saved profiles store the email address, login method, and last-used profile locally in the browser.

**Faster sign-in for returning users** : Saved profiles appear directly on the login page. Selecting one can prefill the email field for password logins or resume the associated SSO or social login flow.

Up to five login profiles can be saved per device, and saved profiles can be removed from the profile list at any time.

For more info:

  * [Log in to Cloudflare](https://developers.cloudflare.com/fundamentals/user-profiles/login/)
  * [Set up dashboard SSO](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/)



Aug 21, 2026

## [Improved SCIM 2.0 group synchronization](https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Dashboard SCIM now supports replacing groups using HTTP `PUT`, as defined by [RFC 7644 section 3.5.1 ↗︎](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1). This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.

**What's New**

**Group replacement via`PUT`**: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.

Note

SCIM provisioning for the Cloudflare dashboard is available to Enterprise customers. You must be a Super Administrator to complete the initial setup.

For more information:

  * [SCIM provisioning overview](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)



Aug 20, 2026

## [Optional OAuth scopes](https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

We're announcing the GA of Optional OAuth Scopes.

OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .

#### What's New

**Optional Scopes:** OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.

**Scope Selection:** On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.

**Templates:** The consent screen now includes **Read Only** and **Full Access** templates to make scope selection faster and easier.

**Search:** Users can now search scopes in the consent screen.

Learn how to [select client scopes](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#select-scopes) and [edit optional permissions](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions).

Aug 19, 2026

## [Access resource lists now support resource-scoped roles](https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.

The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned `403` responses.

For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.

For role definitions and assignment details, refer to [Resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) and [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/).

Aug 5, 2026

## [Improved publisher verification details on OAuth consent screens](https://developers.cloudflare.com/changelog/post/2026-08-04-oauth-consent-shields/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

OAuth consent screens now display a shield icon with explanatory text beneath the consent screen title. Each shield icon indicates who owns the application and whether its domain ownership is verified.

  * **Green filled shield** : Cloudflare owns and manages the application.
  * **Blue outlined shield** : A third-party application with verified ownership of its domain.
  * **Amber filled shield** : A third-party application without verified ownership of a domain.



Domain verification only confirms that the application owner controls the displayed domain.

For more information, refer to [Authorizing an application](https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/).

Aug 4, 2026

## [Create Free accounts from the dashboard](https://developers.cloudflare.com/changelog/post/2026-08-04-free-dashboard-button/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now create standalone Free accounts directly from the Cloudflare dashboard using the new **Create Account** button. This feature is currently available to all users.

When creating a Free account:

  * You can create up to **5 Free accounts**.
  * Your user account must have at least **7 days of tenure** to be eligible.
  * The account is created immediately and ready to use.



To create a Free account, go to the [**Cloudflare dashboard** ↗︎](https://dash.cloudflare.com/) and select **Create Account** from either the account switcher in the top left (where your account name appears) or from the **Accounts** page.

#### Limitations

  * This feature can only be used to create a Cloudflare Free account. To create an Enterprise Account under your existing contract, please contact Cloudflare Support.
  * All users can create a Cloudflare Free account, however, Enterprises wish to restrict this action to only Super Administrators. We will deliver this improvement in a future release.



#### Next steps

After creating your Free account, you can:

  * [Add a payment method](https://developers.cloudflare.com/billing/get-started/create-billing-profile/) to enable additional Cloudflare products and services.
  * [Update billing information](https://developers.cloudflare.com/billing/get-started/update-billing-info/) to manage payment methods, billing address, or tax IDs.
  * [Review how Cloudflare billing works](https://developers.cloudflare.com/billing/understand/how-billing-works/) to understand the billing lifecycle and charge types.
  * [Assign accounts to an Enterprise Organization](https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/) to centrally manage multiple accounts from a single dashboard.



Jul 21, 2026

## [Account Role API deprecated](https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

The [Account Roles API](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/) is deprecated and is being replaced by the [Permission Groups API](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/). An end of life date has not yet been established.

#### What you need to do

Review the [Permission Groups API](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/) documentation; the response schema differs from the legacy Roles response.

#### Highlights

  * Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.
  * The legacy `Role` response includes a top-level `description` and a `permissions` object keyed by resource type with edit/read flags.
  * The `PermissionGroup` response replaces those with a `meta` object containing `label` and `scopes`. Individual permissions are not returned as part of the permission group.
  * The new API supports the [API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.



For more information, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).

Jul 17, 2026

## [Distributor, MSSP, and Agency partners can manage Organization members directly](https://developers.cloudflare.com/changelog/post/2026-07-17-distributor-mssp-self-serve-members/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Organizations](https://developers.cloudflare.com/fundamentals/organizations/)

Distributor, MSSP, and Agency partners on Cloudflare [Organizations](https://developers.cloudflare.com/fundamentals/organizations/) can now add and manage Organization Members directly from the Cloudflare dashboard, without help from Cloudflare.

Previously, adding a member to a Distributor, MSSP, or Agency Organization was a manual, Cloudflare-assisted process that required a request to Cloudflare and enrollment in a closed beta, and the dashboard **Add member** flow was blocked for these Organizations.

Now, Organization admins can add members themselves from **Organization** > **Members** > **Add member** , with no beta enrollment required.

New members receive access to the Organization's accounts through the same implicit-access model already used for enterprise Organizations. The **Accounts** list and the account switcher classify Distributor, MSSP, and Agency Organizations consistently with enterprise Organizations, so their accounts are labeled and grouped correctly in the dashboard.

Agency partners also gain access to the Organizations dashboard, while retaining access to their existing Tenant management dashboard.

Distributor, MSSP, and Agency Organizations are currently in beta.

For more information, refer to [Manage Organization members](https://developers.cloudflare.com/fundamentals/organizations/manage-members/).

Jul 13, 2026

## [Origin Content Signals for Markdown for Agents](https://developers.cloudflare.com/changelog/post/2026-07-13-markdown-for-agents-header-preservation/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown:

  * Markdown for Agents preserves security headers such as `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Frame-Options`, `Set-Cookie`, and CORS headers (for example, `Access-Control-Allow-Origin`) on the converted response.
  * Caching headers (`Cache-Control`, `Expires`, `Age`) continue to pass through.



Your origin's [Content Signals ↗︎](https://contentsignals.org/) policy is now authoritative. If your origin sets a `content-signal` header, Markdown for Agents preserves it. When the origin does not send one, Cloudflare adds the default `Content-Signal: ai-train=yes, search=yes, ai-input=yes`.

This release also fixes relative link resolution for directory-style base URLs (those ending in a trailing slash). Previously, relative links such as `../page/` could resolve one path segment too high and return a `404`. Links are now resolved correctly per [RFC 3986 ↗︎](https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3).

Refer to our [developer documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) for more details.

Jun 30, 2026

## [New permissions and roles for Gateway policies and lists](https://developers.cloudflare.com/changelog/post/2026-06-30-gateway-granular-permissions/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now assign granular, resource-scoped roles for [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) firewall policies and [Zero Trust lists](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/). Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the following resource-scoped roles are now available:

Role | Description  
---|---  
Zero Trust Gateway Firewall Policies Admin | Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.  
Zero Trust Gateway DNS Policies Admin | Can view and edit Gateway DNS policies.  
Zero Trust Gateway HTTP Policies Admin | Can view and edit Gateway HTTP policies.  
Zero Trust Gateway Network Policies Admin | Can view and edit Gateway Network policies.  
Zero Trust Gateway Egress Policies Admin | Can view and edit Gateway Egress policies.  
Zero Trust Gateway Resolver Policies Admin | Can view and edit Gateway Resolver policies.  
Zero Trust Gateway Policies Admin | Can view and edit all Gateway policies.  
Zero Trust Gateway Policies Read | Can view all Gateway policies.  
Zero Trust Gateway Read Only | Can view all Gateway resources.  
Zero Trust DNS Locations Admin | Can view and edit DNS locations.  
Zero Trust Proxy Endpoints Admin | Can view and edit Gateway Proxy Endpoints.  
Zero Trust Account Lists Admin | Can view and edit all Gateway and Access lists.  
Zero Trust Account Lists Read | Can view all Gateway and Access lists.  
  
These roles allow you to:

  * Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.
  * Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.
  * Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.



You can also now assign _Resource-scoped roles_. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. **Existing account-level roles continue to work.** A member with the `Cloudflare Gateway` or `Cloudflare Zero Trust` role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.

#### Get started

  * Refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) for setup instructions and supported resources.
  * Learn how to [create permission policies](https://developers.cloudflare.com/fundamentals/manage-members/policies/) that use these roles.



Jun 25, 2026

## [Search API tokens by name](https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now search API tokens by name, making it easier to find specific tokens across large token lists without manually paginating.

#### What's new

  * **Dashboard search** : Both [account API tokens ↗︎](https://dash.cloudflare.com/?to=/:account/account-api-tokens) and [user API tokens ↗︎](https://dash.cloudflare.com/profile/api-tokens) pages now include a search bar. Type a name to filter results.
  * **API search support** : The [`/user/tokens`](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/list/) and [`/accounts/{account_id}/tokens`](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/list/) endpoints now accept a `name` query parameter to filter tokens by name.



For more information, refer to [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) and [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/).

Jun 4, 2026

## [Billable usage and budget alerts now in product sidebars](https://developers.cloudflare.com/changelog/post/2026-06-04-billable-usage-product-sidebar/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Workers](https://developers.cloudflare.com/workers/)[D1](https://developers.cloudflare.com/d1/)[R2](https://developers.cloudflare.com/r2/)[KV](https://developers.cloudflare.com/kv/)[Queues](https://developers.cloudflare.com/queues/)[Vectorize](https://developers.cloudflare.com/vectorize/)[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Containers](https://developers.cloudflare.com/containers/)

Pay-as-you-go customers can now view billable usage and create [budget alerts](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) directly from the product overview pages for [Workers & Pages](https://developers.cloudflare.com/workers/), [D1](https://developers.cloudflare.com/d1/), [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Queues](https://developers.cloudflare.com/queues/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), and [Containers](https://developers.cloudflare.com/containers/). A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.

The widget pulls from the same data as the [Billable Usage dashboard](https://developers.cloudflare.com/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/) and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.

![Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2872,height=1614,format=webp/_astro/2026-06-04-billable-usage-product-sidebar.BUuIokn_.png)

Selecting **Create budget alert** opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.

For more information, refer to the [Usage-based billing documentation](https://developers.cloudflare.com/billing/).

Jun 3, 2026

## [Introducing self-managed OAuth clients](https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.

OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.

#### What is new

Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.

#### Create an application

To create an application, go to **Manage account** > **OAuth clients** in your account on the Cloudflare dashboard.

[ Go to **OAuth clients** ↗ ](https://dash.cloudflare.com/?to=/:account/oauth-clients)

#### Select limited scopes

If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.

Users can review the requested scopes before they consent.

#### Apps for both private and public use

Applications start with `private` visibility. Private applications can only be used by members of the account where the application was created.

To make an application available to any Cloudflare user, complete the prerequisites for `public` visibility.

For more information, refer to [client visibility](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients).

#### Client domain verification

Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.

After verification, users see a verified badge on the consent page.

For more information, refer to [domain verification](https://developers.cloudflare.com/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification).

#### Learn more

For more information, refer to [OAuth clients](https://developers.cloudflare.com/fundamentals/oauth/).

May 21, 2026

## [Granular permissions for Cloudflare Tunnel and Cloudflare Mesh](https://developers.cloudflare.com/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)

You can now scope Cloudflare permissions to individual [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.

#### What is new

When you [add a member](https://developers.cloudflare.com/fundamentals/manage-members/manage/) or create a [permission policy](https://developers.cloudflare.com/fundamentals/manage-members/policies/), the resource picker now lists [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) instances and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) nodes as scopable resource types. You can:

  * Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.
  * Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.
  * Scope a single policy to one or many Tunnels and Mesh nodes at once.



#### How it works

Granular permissions are a parallel layer to existing account-level roles — they do not replace them.

  * **Existing account-level roles continue to work.** A member with `Cloudflare Access` or `Cloudflare Zero Trust` retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.
  * **Granular permissions are additive.** For any API request on a specific Tunnel or Mesh node, access is granted if the principal has **either** the account-level role **or** a granular permission for that resource.
  * **Resource enumeration is authorization-aware.** Listing endpoints (`GET /accounts/{id}/cfd_tunnel`, `GET /accounts/{id}/warp_connector`) return only the resources the principal has at least read access to.



#### Get started

  * Configure [granular permissions for Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/guides/granular-permissions/).
  * Configure [granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One](https://developers.cloudflare.com/cloudflare-one/networks/connectors/granular-permissions/).
  * Review the [resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) on the Cloudflare role reference.



May 4, 2026

## [Keyboard shortcuts for the Cloudflare dashboard](https://developers.cloudflare.com/changelog/post/2026-05-04-keyboard-shortcuts/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now navigate, switch context, and take common actions in the Cloudflare dashboard without leaving your keyboard. Press `?` anywhere to see the full list. Keyboard shortcuts can be disabled by visiting your [profile settings ↗︎](https://dash.cloudflare.com/profile/settings).

#### Navigate

Shortcut | Action  
---|---  
`g h` | Go to Home  
`g a` | Go to account overview  
`g z` | Go to zone overview  
`g p` | Go to your profile  
`g w` | Go to Workers & Pages  
`g o` | Go to Zero Trust  
`g b` | Go to billing  
`g 1` – `g 5` | Go to a recent or pinned item (by position in sidebar)  
`t →` | Move to the next tab  
`t ←` | Move to the previous tab  
`p →` | Move to the next page of a table  
`p ←` | Move to the previous page of a table  
  
#### Take action

Shortcut | Action  
---|---  
`/` | Open quick search  
`?` | Show keyboard shortcuts  
`s a` | Switch account  
`s z` | Switch zone  
`s .` | Star or unstar the current zone  
`p .` | Pin or unpin the current page  
`t s` | Toggle the sidebar open or closed  
`t m` | Expand or collapse all sidebar menus  
`t a` | Toggle Ask AI sidebar  
`d .` | Toggle dark mode  
`c u` | Copy the current URL  
`c d` | Copy a deep link URL  
  
Apr 29, 2026

## [Instant Bank Payments via Link](https://developers.cloudflare.com/changelog/post/2026-04-29-instant-bank-payments-via-link/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

You can now pay for Cloudflare services directly from your bank account using [Instant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/).

#### What changed

[Link ↗︎](https://link.co/) now supports bank account payments in addition to cards. If you have a bank account saved in Link, it appears as a payment option at checkout. If not, you can connect one during the checkout flow.

![Instant Bank Payments via Link at checkout](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=413,height=562,format=webp/_astro/2026-04-29-instant-bank-payments-link.ChGd-t7M.png)

#### How to use it

  1. During checkout, select your bank account from your saved Link payment methods.
  2. Confirm the payment.



After your first Link authentication, your bank account is available for future purchases without re-entering details.

#### Who is eligible

Instant Bank Payments via Link is available to US-based self-serve accounts across all Cloudflare products. Your existing cards remain available at checkout.

Bank-based Link payments appear in your billing history with the payment method shown as `link` and last four digits as `0000`. For details, refer to the [Instant Bank Payments via Link documentation](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/).

Apr 27, 2026

## [Structured error responses for Cloudflare 5xx errors](https://developers.cloudflare.com/changelog/post/2026-04-27-structured-responses-for-5xx-errors/)

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Cloudflare-generated 5xx error responses now return structured JSON and Markdown when agents request them, matching the format already available for 1xxx errors. Responses follow [RFC 9457 (Problem Details for HTTP APIs) ↗︎](https://www.rfc-editor.org/rfc/rfc9457) and include a `Retry-After` HTTP header on retryable codes.

#### Changes

**5xx coverage.** Ten Cloudflare-generated error codes (500, 502, 504, 520-526) now serve structured responses. These are errors Cloudflare itself generates when it cannot reach or understand the origin server. Origin-generated 5xx responses that Cloudflare passes through are not affected.

**Fault attribution.** The `error_category` field tells agents where the fault lies:

  * `origin` (502, 504, 520-524) — the origin server is responsible. Transient; retry with the backoff in `retry_after`.
  * `cloudflare` (500) — Cloudflare's fault, not the website or the request. Short retry.
  * `ssl` (525, 526) — the origin's TLS configuration is broken. Do not retry.



**Retry-After header.** Retryable codes (500, 502, 504, 520-524) include a `Retry-After` HTTP header matching the `retry_after` body field. Non-retryable codes (525, 526) do not include the header.

#### Negotiation behavior

Request header sent | Response format  
---|---  
`Accept: application/json` | JSON (`application/json` content type)  
`Accept: application/problem+json` | JSON (`application/problem+json` content type)  
`Accept: application/json, text/markdown;q=0.9` | JSON  
`Accept: text/markdown` | Markdown  
`Accept: text/markdown, application/json` | Markdown (equal `q`, first-listed wins)  
`Accept: */*` | HTML (default)  
  
#### Availability

Available now for all zones on all plans.

#### Get started

Get JSON response for error 522:
    
    
    curl -s --compressed -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/522" | jq .

Check presence of the `Retry-After` HTTP header associated with the JSON response for error 521:
    
    
    curl -s --compressed -D - -o /dev/null -H "Accept: application/json" -A "TestAgent/1.0" -H "Accept-Encoding: gzip, deflate" "<YOUR_DOMAIN>/cdn-cgi/error/521" | grep -i retry-after

References:

  * [RFC 9457 — Problem Details for HTTP APIs ↗︎](https://www.rfc-editor.org/rfc/rfc9457)
  * [Cloudflare 5xx error documentation](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/)



← Prev

1[2](https://developers.cloudflare.com/changelog/product/fundamentals/2/)[3](https://developers.cloudflare.com/changelog/product/fundamentals/3/)

[Next →](https://developers.cloudflare.com/changelog/product/fundamentals/2/)
