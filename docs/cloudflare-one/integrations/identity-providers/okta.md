---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/
title: Okta \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:05.120046+00:00
---

# Okta · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Okta



# Okta

Last updated Sep 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSupported featuresSet up Okta as an OIDC provider (Okta App Catalog)Set up Okta as an OIDC provider (Custom App Integration)Synchronize users and groups 1\. Enable SCIM in Cloudflare One 2\. Configure SCIM in OktaExample API ConfigurationTroubleshooting Failed to fetch user/group information from the identity Okta Groups selector is empty or missing groups in the policy builder

Okta provides cloud software that helps companies manage and secure user authentication to modern applications, and helps developers build identity controls into applications, website web services, and devices. You can integrate Okta with Cloudflare One and build rules based on user identity and group membership. Cloudflare One supports Okta integrations using either the OIDC (default) or [SAML](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta-saml/) protocol.

Additionally, you can configure Okta to use risk information from Cloudflare One [user risk scores](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/) to create SSO-level policies. For more information, refer to [Send risk score to Okta](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta).

## Prerequisites

  * A [Zero Trust Organization](https://developers.cloudflare.com/cloudflare-one/setup/) with any subscription tier (including Free)
  * A [Cloudflare One administrator role](https://developers.cloudflare.com/cloudflare-one/roles-permissions/) with `Access Edit` permissions



## Supported features

  * **SP-initiated SSO** : When a user goes to an Access application, Access redirects them to sign in with Okta.
  * **SCIM provisioning** : Synchronize Okta groups and automatically deprovision users. SCIM currently requires a separate custom OIDC application.



## Set up Okta as an OIDC provider (Okta App Catalog)

Active Directory limitation

The Okta App Catalog template does not support synchronizing [Active Directory groups ↗︎](https://help.okta.com/en-us/Content/Topics/Directory/ad-agent-import-groups.htm). If you would like to build policies using AD groups, use the Okta OIDC app integration or [SAML app integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta-saml/).

To set up the Okta integration using the Okta Integration Network (OIN) App Catalog:

  1. Log in to your Okta admin dashboard.

  2. Go to **Applications** > **Applications**.

  3. Select **Browse App Catalog**.

  4. Search for `Cloudflare` and select the **Cloudflare One** app.

  5. Select **Add integration**.

  6. In **Application label** , enter a name for the application (for example, `Cloudflare Access`).

  7. In **Team domain** , enter your Cloudflare Zero Trust team name (only the subdomain prefix, do not include `.cloudflareaccess.com`):
         
         <your-team-name>

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  8. In the **Sign On** tab, copy the **Client ID** and **Client secret** and paste these into `App ID` and `Client secret`.

  9. Copy your Okta Account URL (without the `-admin` value) and copy it into the Cloudflare Okta setup field.




## Set up Okta as an OIDC provider (Custom App Integration)

  1. Log in to your Okta admin dashboard and go to **Applications** > **Applications**.

  2. Select **Create App Integration**.

  3. For the **Sign-in method** , select **OIDC - OpenID Connect**.

![Creating an OIDC application in Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1332,height=1210,format=webp/_astro/okta-1.BlGKmCip.png)
  4. For the **Application type** , select **Web Application**. Select **Next**.

  5. Enter any name for the application. In the **Sign-in redirect URIs** field, enter the following URL:
         
         https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  6. Choose the desired **Assignment** option and select **Save**.

  7. From the application view, go to the **Sign On** tab.

  8. Scroll down to **Token claims** and select **Show legacy configuration** > **Edit**.

![Configuring the Groups claim filter in Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=737,height=658,format=webp/_astro/okta-2.DrNQXWIc.png)
  9. Set **Groups claim filter** to _Matches regex_ and its value to `.*`.




Token claim expressions

  * Groups managed outside of Okta (for example, Microsoft Entra ID or Google groups) may require different regex values. For more information, refer to the Okta documentation on [Groups Claims ↗︎](https://support.okta.com/help/s/article/Why-isnt-my-Groups-claim-returning-Active-Directory-groups) and [OpenID Connect Claims ↗︎](https://support.okta.com/help/s/article/Can-we-retrieve-both-Active-Directory-and-Okta-groups-in-OpenID-Connect-claims).
  * To configure more complex expressions, refer to Okta's [token claims documentation ↗︎](https://help.okta.com/okta_help.htm?type=oie&locale=en&id=federated-claims-overview).



  10. In the **General** tab, copy the **Client ID** and **Client secret**.

![Finding your Client credentials in Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=763,height=672,format=webp/_astro/okta-3.BzGr0OXt.png)


  11. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  12. Under **Your identity providers** , select **Add new identity provider**. Select **Okta** as your identity provider.

  13. Fill in the following information:

     * **Name** : Name your identity provider.
     * **App ID** : Enter your Okta client ID.
     * **Client secret** : Enter your Okta client secret.
     * **Okta account URL** : Enter your [Okta domain ↗︎](https://developer.okta.com/docs/guides/find-your-domain/main/), for example `https://my-company.okta.com`.
  14. (Optional) Create an Okta API token and enter it in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) under **Zero Trust** > **Integrations** > **Identity providers** (the token can be read-only). Use an API token if your Okta tenant has more than 100 groups. When the user's OIDC token contains no groups or reaches Okta's 100-group limit, Cloudflare uses this token during authentication to fetch the user's complete group membership. This setting is specific to Okta and is not part of SCIM. The API token does not add groups to the Access policy builder; the group options in the policy builder come from groups provisioned through SCIM.




Note

The API token field appears blank after you save the identity provider configuration. This is expected. Secret values are omitted from API responses, but the token is stored.

  15. (Optional) To configure [custom OIDC claims](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims):

     1. In Okta, create a [custom authorization server ↗︎](https://developer.okta.com/docs/guides/customize-authz-server/main/) and ensure that the `groups` scope is enabled.
     2. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), enter the **Authorization Server ID** obtained from Okta.
     3. Under **Optional configurations** , enter the claims that you wish to add to your users' identity.
  16. (Optional) Enable [Proof of Key Exchange (PKCE) ↗︎](https://www.oauth.com/oauth2-servers/pkce/). PKCE will be performed on all login attempts.

  17. Select **Save**.




To [test](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one) that your connection is working, select **Test**.

## Synchronize users and groups

The Okta integration allows you to synchronize IdP groups and automatically deprovision users using [SCIM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/). To enable SCIM provisioning between Access and Okta, you need two separate app integrations in Okta:

  * The OIDC application you created when adding Okta as an identity provider. You can create this application via the Okta App Catalog or via a Custom App Integration.
  * A second Okta application of type **SCIM 2.0 Test App (Header Auth)**. This is technically a SAML app but is responsible for sending user and group info via SCIM.



SCIM affects Access and Gateway policy evaluation differently.

Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on **Enable user deprovisioning** , removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.

Gateway evaluates identity-based policies against the [User Registry identity](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/). SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.

Note

If you would like to only maintain one Okta app instance, Okta does support SAML and SCIM within the same application. Create a [generic SAML integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/) and configure those values in the **Sign-On** field of your Okta SCIM application.

### 1\. Enable SCIM in Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Find the Okta integration and select **Edit**.

  3. Turn on **Enable SCIM**.

  4. (Optional) Configure the following settings:



  * **Enable user deprovisioning** : [Revoke a user's active session](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#per-user) when they are removed from the SCIM application in Okta. This will invalidate all active Access sessions and prompt for reauthentication for any [Cloudflare One Client session policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/).
  * **Remove user seat on deprovision** : [Remove a user's seat](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/) from your Cloudflare One account when they are removed from the SCIM application in Okta.
  * **SCIM identity update behavior** : Choose what happens in Cloudflare One when the user's identity updates in Okta. 
    * _Automatic identity updates_ : Automatically update the [User Registry identity](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/) when Okta sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client [device profiles](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/); Access will read the user's updated identity when they reauthenticate.
    * _Group membership change reauthentication_ : [Revoke a user's active session](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#per-user) when their group membership changes in Okta. This will invalidate all active Access sessions and prompt for reauthentication for any [Cloudflare One Client session policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/). Access will read the user's updated group membership when they reauthenticate.
    * _No action_ : Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.


  5. Select **Regenerate Secret**. Copy the **SCIM Endpoint** and **SCIM Secret**. You will need to enter these values into Okta.

  6. Select **Save**.




The SCIM secret never expires, but you can manually regenerate the secret at any time.

### 2\. Configure SCIM in Okta

  1. On your Okta admin dashboard, go to **Applications** > **Applications**.

  2. Select **Browse App Catalog**.

  3. Search for `SCIM Header Auth` and select **SCIM 2.0 Test App (Header Auth)**.

  4. Select **Add Integration**.

  5. On the **General Settings** tab, name your application and select **Next**.

  6. On the **Sign-on Options** tab, ensure that **SAML 2.0** is selected.

  7. Under **Credential Details** , set **Application username format** to either _Okta Username_ or _Email_. This value will be used for the SCIM `userName` attribute.

Note

The `userName` attribute must match the user's email address in Cloudflare One.

  8. Select **Done** to create the integration.

  9. On the **Provisioning** tab, select **Configure API Integration**.

  10. Select **Enable API integration**.

  11. In the **Base URL** field, enter the **SCIM Endpoint** obtained from Cloudflare One.

  12. In the **API Token** field, enter the **SCIM Secret** obtained from Cloudflare One.

![Enter SCIM values into Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1021,height=553,format=webp/_astro/enter-scim-values.CxQEosHF.png)
  13. Select **Test API Credentials** to ensure that the credentials were entered correctly. Select **Save**.

  14. On the **Provisioning** tab, select **Edit** and enable:

     * **Create Users**
     * **Update User Attributes**
     * **Deactivate Users**
![Configure provisioning settings in Okta](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1059,height=685,format=webp/_astro/enable-provisioning.CUZPrFdg.png)
  15. In the **Assignments** tab, add the users you want to synchronize with Cloudflare Access. You can add users in batches by assigning a group. If a user is removed from the application assignment via a either direct user assignment or removed from the group that was assigned to the app, this will trigger a deprovisioning event from Okta to Cloudflare.

  16. In the **Push Groups** tab, add the Okta groups you want to synchronize with Cloudflare Access. These groups will display in the Access policy builder and are the group memberships that will be added and removed upon membership change in Okta.

Note

Groups in this SCIM app Push Groups integration should match the groups in your base [OIDC app integration](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/#set-up-okta-as-an-oidc-provider). Matching the groups keeps the Gateway identity synchronized with the groups that Okta returns when the user authenticates to Access.




To verify the integration, select **View Logs** in the Okta SCIM application.

To check if user identities were updated in Cloudflare One, view your [SCIM provisioning logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/scim-logs/).

Note

New users must first [register the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/) or authenticate to an Access application before SCIM provisioning can begin.

## Example API Configuration
    
    
    {
    	"config": {
    		"client_id": "<your client id>",
    		"client_secret": "<your client secret>",
    		"okta_account": "https://dev-abc123.oktapreview.com"
    	},
    	"type": "okta",
    	"name": "my example idp"
    }

## Troubleshooting

### Failed to fetch user/group information from the identity

If you see the error `Failed to fetch user/group information from the identity`, double-check your Okta configuration:

  * If your Okta tenant has more than 100 groups, include an Okta API token in the identity provider configuration. When the user's OIDC token contains no groups or reaches Okta's 100-group limit, Cloudflare uses the API token during authentication to fetch the user's complete group membership. This setting is specific to Okta and is not part of SCIM. The API token does not populate group options in the Access policy builder; those come from groups provisioned through SCIM.
  * If Okta returns more than 100 groups in a user's OIDC token, Okta may omit some group memberships from the token. This is an Okta token claim limitation, not a Cloudflare limit. If a required group is omitted, Cloudflare cannot evaluate policies that depend on that group. To avoid this, narrow the Okta groups claim filter so that only groups used in Cloudflare policies are included. For more information, refer to [Okta's group functions and dynamic allowlists documentation ↗︎](https://support.okta.com/help/s/article/limitations-of-group-functions-dynamic-allowlists?language=en_US).
  * The request may be blocked by the [ThreatInsights feature ↗︎](https://help.okta.com/en/prod/Content/Topics/Security/threat-insight/ti-index.htm) within Okta.



### Okta Groups selector is empty or missing groups in the policy builder

The **Okta Groups** selector in the Access policy builder is populated by groups provisioned through SCIM, not by the optional Okta API token. If groups are missing from the selector:

  * In Okta, go to the SCIM application's **Push Groups** tab and push the groups you want to use in Access policies. For more information, refer to Configure SCIM in Okta.
  * Make sure the groups you push through SCIM match the groups returned in the OIDC `groups` claim.
  * Adding an Okta API token will not add groups to the selector. The API token is only used during authentication to fetch a user's group membership.



[PreviousMicrosoft Entra ID](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/entra-id/)[NextOkta (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta-saml/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/okta.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
