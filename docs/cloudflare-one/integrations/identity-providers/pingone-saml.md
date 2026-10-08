---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/
title: PingOne (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:05.822386+00:00
---

# PingOne (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /PingOne (SAML)



# PingOne (SAML)

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up PingOne as a SAML provider1\. Create an application in PingOne 2\. Add PingOne to Cloudflare One

The PingOne cloud platform from PingIdentity provides SSO identity management. Cloudflare Access supports PingOne as a SAML identity provider.

## Set up PingOne as a SAML provider

## 1\. Create an application in PingOne

  1. In your PingIdentity environment, go to **Connections** > **Applications**.

  2. Select **Add Application**.

  3. Enter an **Application Name**.

  4. Select **SAML Application**.

  5. Select **Configure**.

  6. To fill in your Cloudflare Access metadata:

     1. Select **Import from URL**.
     2. Set the **Import URL** to:
    
    https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/saml-metadata

where `<your-team-name>` is your Cloudflare One team name. 3. Select **Import**. 4. **Save** the configuration.

  7. In the **Configuration** tab, select **Download metadata** and save the XML metadata file. This file will be used in a later step to add PingOne to Cloudflare One.

  8. In the **Attribute Mappings** tab, add the following required attributes (case sensitive) and select **Save**.

Application attribute | Outgoing value  
---|---  
`email` | Email Address  
`givenName` | Given Name  
`surName` | Family Name  
  
These [SAML attributes](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#saml-attributes) tell Cloudflare Access who the user is.

  9. Set the application to **Active**.




### 2\. Add PingOne to Cloudflare One

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  2. Under **Your identity providers** , select **Add new identity provider**.

  3. Select **SAML**.

  4. Upload your PingOne XML metadata file.

  5. (Optional) To enable SCIM, refer to [Synchronize users and groups](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#synchronize-users-and-groups).

  6. (Optional) Under **Optional configurations** , configure [additional SAML options](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#optional-configurations).

  7. Select **Save**.




You can now [test your connection](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one) and create [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) based on the configured login method and SAML attributes.

[PreviousPingOne](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/)[NextSigned AuthN requests (SAML)](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/signed_authn/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/pingone-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
