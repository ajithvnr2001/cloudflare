---
url: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/
title: Cloudflare as identity provider \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:09:02.723102+00:00
---

# Cloudflare as identity provider · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Integrations

  4. /[Identity providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)
  5. /Cloudflare as identity provider



# Cloudflare as identity provider

Last updated Jun 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up Cloudflare as an identity providerConfiguration optionsUse Cloudflare account membership in policies

Cloudflare Access can use Cloudflare itself as an identity provider, allowing you to build Access policies that match on Cloudflare account membership. This is useful for scenarios where you want to restrict access to users who are members of a specific Cloudflare account, without requiring a third-party identity provider.

When a user authenticates through the Cloudflare identity provider, Access verifies their Cloudflare account membership and grants or denies access based on your policy configuration.

For newly created Zero Trust organizations, Cloudflare adds this identity provider automatically as the default login method, with **Restrict to account members** enabled. You do not need to set it up manually. The following steps describe how to add or reconfigure it.

## Set up Cloudflare as an identity provider

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Integrations** > **Identity providers**.
  2. Under **Your identity providers** , select **Add new identity provider**.
  3. Select **Cloudflare**.
  4. (Optional) Enable **Restrict to account members** if you want to limit authentication to users who are members of your Cloudflare account. When disabled, any user with a Cloudflare account can authenticate.
  5. Select **Save**.



Make a `POST` request to the [Identity Providers](https://developers.cloudflare.com/api/resources/zero_trust/subresources/identity_providers/methods/create/) endpoint:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Access: Organizations, Identity Providers, and Groups Write`

Add an Access identity providerbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/identity_providers" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "Cloudflare",
    		"type": "cloudflare",
    		"config": {
    				"restrict_to_account_members": true
    		}
    	}'

## Configuration options

Option | Description | Default  
---|---|---  
**Restrict to account members** | When enabled, only users who are members of your Cloudflare account can authenticate. When disabled, any Cloudflare user can authenticate (subject to your Access policies). | Disabled  
  
The **Default** column reflects the value when you add this identity provider manually. When Cloudflare configures it automatically for a new organization, **Restrict to account members** is enabled.

## Use Cloudflare account membership in policies

After configuring Cloudflare as an identity provider, you can use the **Cloudflare Account Member** selector in your [Access policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/). This selector matches users based on their membership in a Cloudflare account.

  * If you omit the account ID, the selector matches members of the current account (the account where the Access policy is configured).
  * If you specify an account ID, the selector matches members of that specific account.



This is useful for cross-account access scenarios where you need to grant access to users from a different Cloudflare account.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)[NextOne-time PIN login](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/integrations/identity-providers/cloudflare.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
