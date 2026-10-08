---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/
title: Generic OIDC \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:03.057849+00:00
---

# Generic OIDC · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Generic OIDC



# Generic OIDC

Last updated Aug 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Create an application in your identity provider2\. Add an OIDC provider to Cloudflare One3\. Test the connectionSynchronize users and groups Prerequisites 1\. Enable SCIM in Cloudflare One 2\. Configure SCIM in the IdP 3\. Verify SCIM provisioningOptional configurations Custom OIDC claimsSupported algorithms for generic OIDC tokens

Cloudflare Access has a generic OpenID Connect (OIDC) connector to help you integrate IdPs not already set in Access.

## 1\. Create an application in your identity provider

  1. Visit your identity provider and create a client/app.

  2. When creating a client/app, your IdP may request an **authorized redirect URI**. Enter the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  3. Copy the content of these fields:

     * Client ID
     * Client secret
     * Auth URL: The `authorization_endpoint` URL of your IdP
     * Token URL: The `token_endpoint` URL of your IdP
     * Certificate URL: The `jwks_uri` endpoint of your IdP to allow the IdP keys to sign the tokens

You can find these values on your identity provider's **OIDC discovery endpoint**. Some providers call this the "well-known URL".




## 2\. Add an OIDC provider to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Under **Your identity providers** , select **Add new identity provider**.

  3. Choose **OpenID Connect**.

  4. Name your identity provider and fill in the required fields with the information obtained from your identity provider.

  5. (Optional) Enable [Proof of Key Exchange (PKCE) ↗︎](https://www.oauth.com/oauth2-servers/pkce/) if the protocol is supported by your IdP. PKCE will be performed on all login attempts.

  6. (Optional) To enable SCIM, refer to Synchronize users and groups.

  7. (Optional) Under **Optional configurations** , enter custom OIDC claims that you wish to add to users' identity. This information will be available in the [user identity endpoint](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#user-identity).

  8. Select **Save**.




Make a `POST` request to the [Identity Providers](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/methods/create/) endpoint:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Access: Organizations, Identity Providers, and Groups Write`

Add an Access identity providerbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/identity_providers" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "Generic OIDC example",
    		"type": "oidc",
    		"config": {
    				"client_id": "<your client id>",
    				"client_secret": "<your client secret>",
    				"auth_url": "https://accounts.google.com/o/oauth2/auth",
    				"token_url": "https://accounts.google.com/o/oauth2/token",
    				"certs_url": "https://www.googleapis.com/oauth2/v3/certs",
    				"pkce_enabled": false,
    				"email_claim_name": "email",
    				"claims": [
    						"employeeID",
    						"groups"
    				],
    				"scopes": [
    						"openid",
    						"email",
    						"profile"
    				]
    		}
    	}'

  1. Add the following permission to your [`cloudflare_api_token` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/api_token):

     * `Access: Organizations, Identity Providers, and Groups Write`
  2. Configure the [`cloudflare_zero_trust_access_identity_provider` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_access_identity_provider) resource:
         
         resource "cloudflare_zero_trust_access_identity_provider" "generic_oidc_example" {
         	account_id = var.cloudflare_account_id
         	name       = "Generic OIDC example"
         	type       = "oidc"
         	config 		 = {
         		client_id = "<your client id>"
         		client_secret = "<your client secret>"
         		auth_url = "https://accounts.google.com/o/oauth2/auth"
         		token_url = "https://accounts.google.com/o/oauth2/token"
         		certs_url = "https://www.googleapis.com/oauth2/v3/certs"
         		pkce_enabled = false
         		email_claim_name = "email"
         		claims = ["employeeID", "groups"]
         		scopes = ["openid", "email", "profile"]
         	}
         }




## 3\. Test the connection

To test that your connection is working, go to **Authentication** > **Login methods** and select **Test** next to the login method you want to test. On success, a confirmation screen displays.

## Synchronize users and groups

The generic OIDC integration allows you to synchronize user groups and automatically deprovision users using [SCIM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/).

SCIM affects Access and Gateway policy evaluation differently.

Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on **Enable user deprovisioning** , removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.

Gateway evaluates identity-based policies against the [User Registry identity](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/). SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.

### Prerequisites

Your identity provider must support SCIM version 2.0.

### 1\. Enable SCIM in Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Find the IdP integration and select **Edit**.

  3. Turn on **Enable SCIM**.

  4. (Optional) Configure the following settings:



  * **Enable user deprovisioning** : [Revoke a user's active session](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#per-user) when they are removed from the SCIM application in IdP. This will invalidate all active Access sessions and prompt for reauthentication for any [Cloudflare One Client session policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/).
  * **Remove user seat on deprovision** : [Remove a user's seat](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/) from your Cloudflare One account when they are removed from the SCIM application in IdP.
  * **SCIM identity update behavior** : Choose what happens in Cloudflare One when the user's identity updates in IdP. 
    * _Automatic identity updates_ : Automatically update the [User Registry identity](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/) when IdP sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client [device profiles](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/); Access will read the user's updated identity when they reauthenticate.
    * _Group membership change reauthentication_ : [Revoke a user's active session](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#per-user) when their group membership changes in IdP. This will invalidate all active Access sessions and prompt for reauthentication for any [Cloudflare One Client session policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/). Access will read the user's updated group membership when they reauthenticate.
    * _No action_ : Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.


  5. Select **Regenerate Secret**. Copy the **SCIM Endpoint** and **SCIM Secret**. You will need to enter these values into IdP.

  6. Select **Save**.




The SCIM secret never expires, but you can manually regenerate the secret at any time.

### 2\. Configure SCIM in the IdP

Setup instructions vary depending on the identity provider. In your identity provider, you will either need to edit the [original SSO application](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#1-create-an-application-in-your-identity-provider) or create a new SCIM application. Refer to your identity provider's documentation for more details. For example instructions, refer to our [Okta](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/#synchronize-users-and-groups) or [Jumpcloud](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/#synchronize-users-and-groups) guides.

#### IdP groups

If you would like to build policies based on IdP groups:

  * Ensure that your IdP sends a `groups` field. The naming must match exactly (case insensitive). All other values will be sent as a OIDC claim.
  * If your IdP requires a new SCIM application, ensure that its groups match the groups in the [original SSO application](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#1-create-an-application-in-your-identity-provider). Matching the groups keeps the Gateway identity synchronized with the groups that the IdP returns when the user authenticates to Access.



### 3\. Verify SCIM provisioning

To check if user identities were updated in Cloudflare One, view your [SCIM provisioning logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/scim-logs/).

Note

New users must first [register the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/) or authenticate to an Access application before SCIM provisioning can begin.

## Optional configurations

### Custom OIDC claims

All OIDC IdP integrations support the use of custom OIDC claims. Once configured, Access will add the claims to the [Access JWT](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/) for consumption by your origin services. You can reference the custom OIDC claims in [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) and [Gateway policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims), offering a means to control user access to applications based on custom identity attributes.

To add a custom OIDC claim to an IdP integration:

  1. In your identity provider, ensure that the custom claim is included in your OIDC ID token.

  2. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  3. Under **Your identity providers** , find your identity provider and select **Edit**.

  4. Under **OIDC Claims** , enter the name of your custom claim (for example, `oid`).

  5. Select **Save**.

  6. Select **Test** and verify that the custom claim appears in `oidc_fields`. For example,
         
         	"oidc_fields": {
         		"oid": "54eb1ed2-7150-44e6-bbe4-ead24c132fd4"
         	},




You can now build an Access policy for the custom claim using the **OIDC Claim** or **IdP OIDC Claim** selector. You can also use custom OIDC claims as [identity-based selectors in Gateway policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims). The custom claim will be passed to origins behind Access in a [JWT](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#custom-saml-attributes-and-oidc-claims).

#### Email claim

You can specify a custom **Email claim** name that Access will use to identify user emails. This is useful if your IdP does not return the standard `email` claim in the OIDC ID token.

#### Multi-record OIDC claims

Cloudflare Access extends support for multi-record OIDC claims. These claims are parsed out and can be individually referenced in policies. This feature enables granular access control and precise user authorization in applications.

Cloudflare Access does not support partial OIDC claim value references or OIDC scopes.

## Supported algorithms for generic OIDC tokens

Cloudflare supports the following algorithms for verifying generic OIDC tokens:

  * RS512
  * RS256
  * PS512
  * ES256
  * ES384
  * ES512



[PreviousOne-time PIN login](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/)[NextGeneric SAML 2.0](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/generic-oidc.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
