---
url: https://developers.cloudflare.com/fundamentals/account/create-account/
title: Create account \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:19.997479+00:00
---

# Create account · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/account/create-account/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /Accounts
  4. /Create account



# Create account

Last updated Sep 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/account/create-account/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate an additional Free account Eligibility Create an account in the dashboard Create an account with the API Resolve account creation errorsAccount nameBest practicesInteract with Cloudflare

To create your first Cloudflare account:

  1. Go to the [Sign up page ↗︎](https://dash.cloudflare.com/sign-up).
  2. Enter your **Email** and **Password**.
  3. Select **Create Account**.



Once you create your account, Cloudflare will automatically send an email to your address to [verify that email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

## Create an additional Free account

Existing users can create additional Free accounts in the dashboard or with the API.

### Eligibility

The following requirements apply to Free account creation:

  * Your Cloudflare user must be active and at least seven days old.
  * You must have the Super Administrator role on an existing account.
  * You can create up to five additional Free accounts.



### Create an account in the dashboard

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/) and go to **Accounts**.

[ Go to **Accounts** ↗ ](https://dash.cloudflare.com/)
  2. Select **Create Account**.

  3. Enter an account name.

  4. Select **Create Account**.




### Create an account with the API

Use a user-owned API token or OAuth access token. Account-owned API tokens cannot create accounts.

A user-owned API token requires the **User Details Read** permission. An OAuth access token requires the `user-details.read` scope.

Set the `standalone` field to `true` and omit `unit`. Every Free account creation request requires exactly one valid `Idempotency-Key` header. Reuse the same key when retrying the same request.

Set `CLOUDFLARE_API_TOKEN` to a user-owned API token. Set `IDEMPOTENCY_KEY` to a unique value for this account creation request.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--header "Content-Type: application/json" \
    	--header "Idempotency-Key: $IDEMPOTENCY_KEY" \
    	--data '{"name":"Example account","type":"standard","standalone":true}'

Set `CLOUDFLARE_OAUTH_TOKEN` to an OAuth access token. Set `IDEMPOTENCY_KEY` to a unique value for this account creation request.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_OAUTH_TOKEN" \
    	--header "Content-Type: application/json" \
    	--header "Idempotency-Key: $IDEMPOTENCY_KEY" \
    	--data '{"name":"Example account","type":"standard","standalone":true}'

For the complete request schema, refer to [Create Account](https://developers.cloudflare.com/api/resources/accounts/methods/create/).

### Resolve account creation errors

Use the error message to resolve common account creation failures:

Error | Resolution  
---|---  
Your user is less than seven days old. | Wait until the user is at least seven days old.  
You are not a Super Administrator. | Confirm that you have the Super Administrator role on an existing account.  
You reached an account creation limit. | Use an existing account or contact your account team.  
Account creation is temporarily unavailable. | Retry the request later with the same idempotency key.  
The idempotency key was used for a different request. | Use a new key for the new request. Reuse the original key only for an identical retry.  
Your user is suspended. | Contact [Cloudflare Support](https://developers.cloudflare.com/support/contacting-cloudflare-support/).  
  
## Account name

Your account name defaults to `<<YOUR_EMAIL_ADDRESS>>'s Account`.

You may want to customize the name of this account, either to help specify its purpose or to help associate it with multiple accounts.

To change your account name:

  1. In the Cloudflare dashboard, go to the **Configurations** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. For **Account Name** , select **Change Name**.

  3. Enter a new account name.

  4. Select **Save**.




## Best practices

If you are creating an account for your team or a business, we recommend choosing an email alias or distribution list for your **Email** , such as `cloudflare@example.com`.

This email address is the main point of contact for your Cloudflare billing, usage notifications, and account recovery.

Refer to [Account and domain management best practices](https://developers.cloudflare.com/fundamentals/reference/best-practices/) for a detailed list of ways to protect your account and domain.

Once you [set up an account](https://developers.cloudflare.com/fundamentals/account/), you have several ways to interact with Cloudflare.

## Interact with Cloudflare

If you prefer working without code, you can manage your account and domain settings through the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/login).

Note

If your domain was added to Cloudflare by a hosting partner, manage your DNS records via the hosting partner.

For those who prefer to interact with Cloudflare programmatically, you can use several methods:

Resource | Docs | Description  
---|---|---  
[Cloudflare API](https://developers.cloudflare.com/fundamentals/api/) | [API docs](https://developers.cloudflare.com/api/) | RESTful API based on HTTPS requests and JSON responses.  
[Terraform ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) | [Terraform docs](https://developers.cloudflare.com/terraform/) | Configure Cloudflare using HashiCorp's Infrastructure as Code tool, Terraform.  
[cloudflare-go ↗︎](https://github.com/cloudflare/cloudflare-go) | [README ↗︎](https://github.com/cloudflare/cloudflare-go#readme) | The official Go library for the Cloudflare API.  
[cloudflare-typescript ↗︎](https://github.com/cloudflare/cloudflare-typescript) | [README ↗︎](https://github.com/cloudflare/cloudflare-typescript#readme) | The official TypeScript library for the Cloudflare API.  
[cloudflare-python ↗︎](https://github.com/cloudflare/cloudflare-python) | [README ↗︎](https://github.com/cloudflare/cloudflare-python#readme) | The official Python library for the Cloudflare API.  
  
[PreviousGet started](https://developers.cloudflare.com/fundamentals/get-started/)[NextAdd abuse contact](https://developers.cloudflare.com/fundamentals/account/account-security/abuse-contact/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/account/create-account.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
