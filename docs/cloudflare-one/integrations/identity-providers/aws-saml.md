---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/
title: AWS IAM (SAML) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:01.504046+00:00
---

# AWS IAM (SAML) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /AWS IAM (SAML)



# AWS IAM (SAML)

Last updated Apr 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/aws-saml/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSet up AWS IAM as a SAML providerExample API configuration

AWS IAM Identity Center provides SSO identity management for users who interact with AWS resources (such as EC2 instances or S3 buckets). You can integrate AWS IAM with Cloudflare Zero Trust as a SAML identity provider, which allows users to authenticate to Zero Trust using their AWS credentials.

## Prerequisites

  * Admin access to an IAM Identity Center [organization instance ↗︎](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html)



## Set up AWS IAM as a SAML provider

To set up SAML with AWS IAM as your identity provider:

  1. Open your [IAM Identity Center console ↗︎](https://console.aws.amazon.com/singlesignon) and go to **Applications**.

  2. Select the **Customer managed** tab.

  3. Select **Add application**.

  4. Select **I have an application I want to set up**.

  5. For **Application type** , select **SAML 2.0**.

  6. Select **Next**.

  7. Enter a **Display name** for the application (for example, `Cloudflare One`).

  8. Download the **IAM Identity Center SAML metadata file**. You will need this file later when configuring the identity provider in Cloudflare One.

  9. Under **Application metadata** , select **Manually type your metadata values**.

  10. In **Application ACS URL** and **Application SAML audience** , enter the following URL:



    
    
    https://<your-team-name>.cloudflareaccess.com/cdn-cgi/access/callback

You can find your team name in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) under **Settings** > **Team name and domain** > **Team name**.

  11. Select **Submit**.

  12. Next, select the **Actions** dropdown menu and select _Edit attribute mappings_.

  13. For the `Subject` user attribute, enter `${user:email}`.

  14. (Recommended) Add user name attributes:




User attribute | String value  
---|---  
`name` | `${user:name}`  
`surName` | `${user:familyName}`  
  
| `givenName` | `${user:givenName}` |

![Configuring attribute statements in IAM Identity Center](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1505,height=542,format=webp/_astro/aws-saml-attributes.DuPGeU5b.png)

  15. Select **Save changes**.

  16. Under **Assign users and groups** , add individuals and/or groups that should be allowed to login to Cloudflare One.

  17. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.

  18. Under **Your identity providers** , select **Add new identity provider**.

  19. Select **SAML**.

  20. Enter a **Name** for the IdP integration (for example, `AWS`).

  21. Upload the **IAM Identity Center SAML metadata file** that you downloaded in Step 8.

  22. (Recommended) Enable [**Sign SAML authentication request**](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#sign-saml-authentication-request).

  23. Select **Save**.




To [test](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one) that your connection is working, select **Test**.

## Example API configuration
    
    
    {
    	"config": {
    		"issuer_url": "https://portal.sso.eu-central-1.amazonaws.com/saml/assertion/b2yJrC4kjy3ZAS0a2SeDJj74ebEAxozPfiURId0aQsal3",
    		"sso_target_url": "https://portal.sso.eu-central-1.amazonaws.com/saml/assertion/b2yJrC4kjy3ZAS0a2SeDJj74ebEAxozPfiURId0aQsal3",
    		"attributes": ["email"],
    		"email_attribute_name": "email",
    		"sign_request": true,
    		"idp_public_certs": [
    			"MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o"
    		]
    	},
    	"type": "saml",
    	"name": "AWS IAM SAML example"
    }

[PreviousAmazon Cognito](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/)[NextCentrify](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/aws-saml.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
