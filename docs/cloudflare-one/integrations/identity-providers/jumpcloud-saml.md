---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/
title: JumpCloud (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:04.285087+00:00
---

# JumpCloud (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /JumpCloud (SAML)



# JumpCloud (SAML)

Last updated Aug 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up Jumpcloud as a SAML provider 1\. Create an SSO application in JumpCloud 2\. Add JumpCloud to Cloudflare OneSynchronize users and groups 1\. Enable SCIM in Cloudflare One 2\. Configure SCIM in JumpCloud Provisioning attributesExample API configuration

[JumpCloud ↗︎](https://jumpcloud.com/#platform) provides SSO identity management. Cloudflare Access integrates with JumpCloud as a SAML identity provider.

The following steps are specific to setting up JumpCloud with Cloudflare Access. For more information on configuring JumpCloud SSO application, refer to the [JumpCloud documentation ↗︎](https://jumpcloud.com/support/integrate-with-cloudflare).

## Set up Jumpcloud as a SAML provider

### 1\. Create an SSO application in JumpCloud

  1. In the [JumpCloud Admin Portal ↗︎](https://console.jumpcloud.com/#/home), go to **SSO Applications**.

  2. Select **Add New Application**.

  3. In the search bar, enter `Cloudflare` and select the **Cloudflare Access** application.

  4. Select **Next**.

  5. In **Display Label** , enter an application name.

  6. Select **Save Application**.

  7. Review the application summary and select **Configure Application**.

  8. In the **SSO** tab, configure the following settings:

     1. In **IdP Entity ID** , enter your Cloudflare team domain:
            
            https://<your-team-name>.cloudflareaccess.com/

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

     2. Set both **SP Entity ID** and **ACS URL** to the following callback URL:
            
            https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

     3. (Optional) Configure SAML attributes that you want to send to Cloudflare Access.

     4. Scroll up to **JumpCloud Metadata** and select **Export Metadata**. Save this XML file for use in a later step.

  9. In the **User Groups** tab, [assign user groups ↗︎](https://jumpcloud.com/support/get-started-applications-saml-sso#managing-employee-access-to-applications) to this application.

  10. Select **Save**.




### 2\. Add JumpCloud to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Under **Your identity providers** , select **Add new identity provider**.

  3. Select **SAML**.

  4. Upload your JumpCloud XML metadata file.

  5. (Optional) To enable SCIM, refer to Synchronize users and groups.

  6. (Optional) Under **Optional configurations** , configure additional SAML options.

  7. Select **Save**.




You can now [test your connection](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one) and create [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) based on the configured login method and SAML attributes.

## Synchronize users and groups

The JumpCloud integration allows you to synchronize user groups and automatically deprovision users using [SCIM](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/).

SCIM affects Access and Gateway policy evaluation differently.

Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on **Enable user deprovisioning** , removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.

Gateway evaluates identity-based policies against the [User Registry identity](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/). SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.

### 1\. Enable SCIM in Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Find the JumpCloud integration and select **Edit**.

  3. Turn on **Enable SCIM**.

  4. (Optional) Configure the following settings:



  * **Enable user deprovisioning** : [Revoke a user's active session](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#per-user) when they are removed from the SCIM application in JumpCloud. This will invalidate all active Access sessions and prompt for reauthentication for any [Cloudflare One Client session policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/).
  * **Remove user seat on deprovision** : [Remove a user's seat](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/seat-management/) from your Cloudflare One account when they are removed from the SCIM application in JumpCloud.
  * **SCIM identity update behavior** : Choose what happens in Cloudflare One when the user's identity updates in JumpCloud. 
    * _Automatic identity updates_ : Automatically update the [User Registry identity](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/users/) when JumpCloud sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client [device profiles](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/); Access will read the user's updated identity when they reauthenticate.
    * _Group membership change reauthentication_ : [Revoke a user's active session](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#per-user) when their group membership changes in JumpCloud. This will invalidate all active Access sessions and prompt for reauthentication for any [Cloudflare One Client session policies](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/). Access will read the user's updated group membership when they reauthenticate.
    * _No action_ : Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.


  5. Select **Regenerate Secret**. Copy the **SCIM Endpoint** and **SCIM Secret**. You will need to enter these values into JumpCloud.

  6. Select **Save**.




The SCIM secret never expires, but you can manually regenerate the secret at any time.

### 2\. Configure SCIM in JumpCloud

  1. In the [JumpCloud Admin Portal ↗︎](https://console.jumpcloud.com/#/home), go to **SSO Applications**.
  2. Select the Cloudflare application that was created when you [Set up JumpCloud as a SAML provider](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/#set-up-jumpcloud-as-a-saml-provider).
  3. Select the **SSO** tab.
  4. To provision user groups, select **Include group attribute** and enter `groups`. The group attribute name has to exactly match `groups` or else it will be sent as a SAML attribute.
  5. Select the **Identity Management** tab.
  6. Make sure that **Enable management of User Groups and Group Membership in this application** is turned on.
  7. Select **Configure**.
  8. In the **Base URL** field, enter the **SCIM Endpoint** obtained from Cloudflare One.
  9. In the **Token Key** field, enter the **SCIM Secret** obtained from Cloudflare One.
  10. Select **Activate**. You will receive a confirmation that the Identity Management integration has been successfully verified.
  11. Select **Save**.



To check if user identities were updated in Cloudflare One, view your [SCIM provisioning logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/scim-logs/).

Note

New users must first [register the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/) or authenticate to an Access application before SCIM provisioning can begin.

### Provisioning attributes

Provisioning attributes define the user and group properties that JumpCloud will synchronize with Cloudflare Access. By default, JumpCloud will send the following attributes during a SCIM update event:

JumpCloud user attribute | Cloudflare Access attribute  
---|---  
`email` | `email`  
`firstname` | `givenName`  
`lastname` | `surname`  
  
JumpCloud group attribute | Cloudflare Access attribute  
---|---  
`name` | `groups`  
  
## Example API configuration
    
    
    {
    	"config": {
    		"issuer_url": "jumpcloud",
    		"sso_target_url": "https://sso.myexample.jumpcloud.com/saml2/cloudflareaccess",
    		"attributes": ["email", "name", "username"],
    		"email_attribute_name": "",
    		"sign_request": false,
    		"idp_public_cert": "MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o"
    	},
    	"type": "saml",
    	"name": "jumpcloud saml example"
    }

[PreviousGoogle Workspace](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google-workspace/)[NextKeycloak (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/keycloak/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/jumpcloud-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
